# Checkov AWS Scan — Execution Workflow

Hướng dẫn chi tiết để AI agent thực thi scan trên máy local. PHẢI follow đúng thứ tự.

---

## PHASE 1: PLAN (Bắt buộc trước mọi scan)

### Step 1.1: Detect IaC Files

Chạy commands sau để xác định scope:

```bash
# Tìm Terraform files
find . -name "*.tf" -not -path "*/.terraform/*" -not -path "*/node_modules/*" | wc -l

# Tìm CloudFormation/SAM files
find . -name "*.yaml" -o -name "*.yml" | xargs grep -l "AWSTemplateFormatVersion\|Transform.*AWS::Serverless" 2>/dev/null | wc -l

# List directories chứa IaC
find . -name "*.tf" -not -path "*/.terraform/*" -exec dirname {} \; | sort -u
```

### Step 1.2: Check Prerequisites

```bash
# Verify checkov
checkov --version 2>/dev/null || echo "CHECKOV_NOT_INSTALLED"

# Check Python version (checkov needs >= 3.8)
python3 --version
```

**Nếu CHECKOV_NOT_INSTALLED:**
- Hỏi user: "Checkov chưa được cài. Cài bằng `pip install checkov` hay `brew install checkov`?"
- KHÔNG tự install khi chưa được approve

### Step 1.3: Check Existing State

```bash
# Có tracking file từ lần scan trước không?
test -f .checkov-reports/tracking.md && echo "EXISTING_TRACKING" || echo "FIRST_SCAN"

# Có baseline không?
test -f .checkov.baseline && echo "HAS_BASELINE" || echo "NO_BASELINE"

# Có config không?
test -f .checkov.yaml && echo "HAS_CONFIG" || echo "NO_CONFIG"
```

**Nếu EXISTING_TRACKING:**
- Đọc tracking.md → lấy scan history
- Báo user: "Đã có N lần scan trước. Lần scan gần nhất: {date}, {failed_count} findings."
- Suggest: re-scan để check delta

### Step 1.4: Create Plan

Tạo scan plan và trình user. Format:

```markdown
## 📋 Scan Plan

| Attribute | Value |
|-----------|-------|
| Target | {dir} ({N} .tf files) |
| Framework | terraform |
| Mode | **FULL SCAN** — tất cả checks Checkov cung cấp |
| Checks | ALL (~456 AWS checks) |
| Baseline | {Yes/No — nếu có .checkov.baseline} |
| Output | .checkov-reports/ |
| Estimated Time | ~{N}s |

### Scope
- Files: {list top 5 .tf files}
- Excluded: .terraform/, vendor/, test/

### Coverage (quét hết)
- S3, EC2, RDS, IAM, VPC, EKS, Lambda, DynamoDB, SQS, SNS
- CloudFront, API Gateway, ECS, EFS, KMS, CloudTrail, Config
- ElastiCache, Redshift, Elasticsearch, Secrets Manager, SSM
- CloudWatch, GuardDuty, WAF, Route53, ACM, CodeBuild...
- Custom: {N custom policies nếu có ./custom_checks}
- Phân loại severity/compliance SAU KHI scan xong

Confirm để bắt đầu scan?
```

**KHÔNG chạy scan khi chưa có user confirm.**

---

## PHASE 2: EXECUTE

### Step 2.1: Prepare Output Directory

```bash
mkdir -p .checkov-reports/plans
```

### Step 2.2: Save Plan

Lưu plan đã approve vào file:

```bash
# Ghi plan (dùng fsWrite, KHÔNG heredoc)
```

Tạo file `.checkov-reports/plans/plan-{NNN}.md` với nội dung plan.

### Step 2.3: Run Scan

**MẶC ĐỊNH: Quét TOÀN BỘ checks mà Checkov cung cấp cho AWS** — KHÔNG filter hay limit checks trừ khi user yêu cầu cụ thể.

```bash
# FULL AWS SCAN — tất cả built-in checks (456 AWS checks)
checkov -d {target_dir} \
  --framework {framework} \
  --compact \
  -o json -o cli \
  --output-file-path .checkov-reports \
  2>&1 | tee .checkov-reports/scan-log.txt
```

**Nếu có baseline:**
```bash
checkov -d {target_dir} \
  --framework {framework} \
  --baseline .checkov.baseline \
  --compact \
  -o json -o cli \
  --output-file-path .checkov-reports
```

**CHỈ KHI user yêu cầu compliance-specific mới filter:**
```bash
# CIS AWS (chỉ khi user hỏi CIS)
checkov -d {target_dir} --check CIS_AWS -o json --output-file-path .checkov-reports

# PCI-DSS (chỉ khi user hỏi PCI)
checkov -d {target_dir} --check CKV_AWS_19,CKV_AWS_61,CKV_AWS_7,CKV_AWS_89,CKV_AWS_23,CKV_AWS_40,CKV_AWS_18,CKV_AWS_49 -o json --output-file-path .checkov-reports

# HIPAA (chỉ khi user hỏi HIPAA)
checkov -d {target_dir} --check CKV_AWS_19,CKV_AWS_7,CKV_AWS_61,CKV_AWS_20,CKV_AWS_18,CKV_AWS_40,CKV_AWS_49,CKV_AWS_23,CKV_AWS_27 -o json --output-file-path .checkov-reports
```

**Nguyên tắc: Quét hết → phân tích sau. KHÔNG bỏ sót check nào.**

### Step 2.4: Handle Errors

| Error | Action |
|-------|--------|
| `command not found: checkov` | Offer install |
| `No files found` | Check target path |
| Timeout (>60s) | Add `--skip-path`, reduce scope |
| Module download fail | Skip `--download-external-modules` |
| Permission denied | Report to user |

---

## PHASE 3: ANALYZE

### Step 3.1: Parse Results

Đọc `.checkov-reports/results_json.json` và extract:

```bash
# Summary counts
python3 -c "
import json
with open('.checkov-reports/results_json.json') as f:
    data = json.load(f)
s = data.get('summary', {})
print(f'passed={s.get(\"passed\",0)}')
print(f'failed={s.get(\"failed\",0)}')
print(f'skipped={s.get(\"skipped\",0)}')
"
```

```bash
# Findings by severity
python3 -c "
import json
with open('.checkov-reports/results_json.json') as f:
    data = json.load(f)
failed = data.get('results', {}).get('failed_checks', [])
sev = {}
for f in failed:
    s = f.get('severity', 'UNKNOWN')
    sev[s] = sev.get(s, 0) + 1
for k in ['CRITICAL','HIGH','MEDIUM','LOW','UNKNOWN']:
    if k in sev:
        print(f'{k}: {sev[k]}')
"
```

```bash
# Top findings list
python3 -c "
import json
with open('.checkov-reports/results_json.json') as f:
    data = json.load(f)
failed = data.get('results', {}).get('failed_checks', [])
# Sort by severity
order = {'CRITICAL':0,'HIGH':1,'MEDIUM':2,'LOW':3,'UNKNOWN':4}
failed.sort(key=lambda x: order.get(x.get('severity','UNKNOWN'), 4))
for f in failed[:10]:
    print(f'{f[\"check_id\"]} | {f.get(\"severity\",\"?\")} | {f[\"check_result\"][\"evaluated_keys\"]} | {f[\"file_path\"]}:{f[\"file_line_range\"][0]}')
"
```

### Step 3.2: Present Summary

Trình user theo format bảng:

```markdown
## 📊 Scan Results — {date}

| Metric | Count |
|--------|-------|
| ✅ Passed | {N} |
| ❌ Failed | {N} |
| ⏭️ Skipped | {N} |
| ⏱️ Duration | {N}s |

### Findings by Severity
| Severity | Count | Action Required |
|----------|-------|-----------------|
| 🔴 CRITICAL | {N} | Fix immediately — blocks deploy |
| 🟠 HIGH | {N} | Fix before merge |
| 🟡 MEDIUM | {N} | Plan remediation |
| 🟢 LOW | {N} | Track/improve |

### Top Findings
| # | Check ID | Severity | Resource | File:Line | Description |
|---|----------|----------|----------|-----------|-------------|
| 1 | CKV_AWS_93 | CRITICAL | aws_s3_bucket.data | s3.tf:15 | S3 public access not blocked |
| 2 | CKV_AWS_23 | HIGH | aws_security_group.web | vpc.tf:42 | SG open to 0.0.0.0/0 |
| ... | | | | | |

### Recommended Actions
1. Fix {N} CRITICAL findings first
2. Review {N} HIGH findings
3. Consider creating baseline for existing MEDIUM/LOW findings
```

---

## PHASE 4: TRACK

### Step 4.1: Update Tracking File

Sau mỗi scan, **APPEND** vào `.checkov-reports/tracking.md`:

**Nếu file chưa tồn tại** → tạo mới với header:
```markdown
# Checkov AWS Scan Tracking

## Project Info
| Key | Value |
|-----|-------|
| Project | {current directory name} |
| Target | {target_dir} |
| Framework | {framework} |
| First Scan | {YYYY-MM-DD} |
| Power Version | 1.0.0 |

## Scan History
```

**Append scan entry:**
```markdown

---

### Scan #{N} — {YYYY-MM-DD HH:MM}
| Metric | Value |
|--------|-------|
| Passed | {N} |
| Failed | {N} |
| CRITICAL | {N} |
| HIGH | {N} |
| MEDIUM | {N} |
| LOW | {N} |
| Duration | {N}s |
| Plan | plan-{NNN}.md |

**Top CRITICAL/HIGH:**
- {check_id} → {file}:{line} ({description})
- ...

**Delta vs Previous:** {+/-N} findings ({detail})
**Status:** {⏳ Pending / ✅ All clear / 🔴 CRITICAL open}
```

### Step 4.2: Delta Calculation

So sánh với scan trước:
- Tổng failed: +/- bao nhiêu
- New findings (chưa có ở scan trước)
- Resolved findings (có ở scan trước nhưng mất ở scan này)
- CRITICAL count change

### Step 4.3: Remediation Log

Khi user fix finding → cập nhật section cuối tracking.md:

```markdown
## Remediation Log
| Check ID | File | Status | Fixed Date | Notes |
|----------|------|--------|------------|-------|
| CKV_AWS_93 | s3.tf:15 | ✅ Fixed | 2026-05-26 | Added public_access_block |
| CKV_AWS_23 | vpc.tf:42 | ⏳ Pending | — | Need team review |
```

---

## PHASE 5: REMEDIATE (Khi user yêu cầu fix)

### Step 5.1: Identify Fix

Đọc finding detail từ JSON:
```bash
python3 -c "
import json
with open('.checkov-reports/results_json.json') as f:
    data = json.load(f)
for f in data.get('results',{}).get('failed_checks',[]):
    if f['check_id'] == '{CHECK_ID}':
        print(f'File: {f[\"file_path\"]}')
        print(f'Lines: {f[\"file_line_range\"]}')
        print(f'Resource: {f[\"resource\"]}')
        print(f'Guide: {f.get(\"guideline\", \"N/A\")}')
        break
"
```

### Step 5.2: Apply Fix

Đọc file → sửa resource → apply. Cụ thể theo check:

| Check ID | Fix Pattern |
|----------|-------------|
| CKV_AWS_93 | Add `aws_s3_bucket_public_access_block` resource |
| CKV_AWS_19 | Add `server_side_encryption_configuration` block |
| CKV_AWS_23 | Replace `0.0.0.0/0` with specific CIDR |
| CKV_AWS_40 | Replace `"*"` actions with specific actions |
| CKV_AWS_16/61 | Set `storage_encrypted = true` |
| CKV_AWS_7 | Set `encrypted = true` on EBS |
| CKV_AWS_21 | Add `versioning { enabled = true }` |
| CKV_AWS_20 | Add bucket policy requiring SSL |

### Step 5.3: Verify Fix

```bash
# Re-scan chỉ check vừa fix
checkov -f {file} --check {CHECK_ID} --compact
```

### Step 5.4: Update Tracking

Mark finding as Fixed trong remediation log.

---

## Session Resumption

Khi user quay lại (new session), AI PHẢI:

1. Check `.checkov-reports/tracking.md` exists
2. Đọc tracking → lấy last scan info
3. Báo user context:
   ```
   📋 Scan history: {N} scans performed
   Last scan: {date} — {failed} findings ({critical} CRITICAL)
   Pending remediation: {N} items
   
   Bạn muốn: [re-scan] [fix pending] [new scope]?
   ```

---

## Configuration Defaults

Nếu chưa có `.checkov.yaml`, suggest tạo:

```yaml
framework:
  - terraform

skip-path:
  - .terraform/
  - .terragrunt-cache/
  - node_modules/
  - vendor/

soft-fail-on:
  - LOW
  - MEDIUM

hard-fail-on:
  - CRITICAL
  - HIGH

compact: true
download-external-modules: true

output:
  - cli
  - json

output-file-path: .checkov-reports
```

---

## Important Rules for AI Agent

1. **KHÔNG tự chạy scan** khi chưa có user approve plan
2. **LUÔN tạo tracking** sau mỗi scan
3. **LUÔN đọc tracking** ở đầu session (nếu có)
4. **APPEND** vào tracking — KHÔNG overwrite history
5. **Report delta** khi có scan trước đó
6. **Offer remediation** cho CRITICAL/HIGH findings
7. **Verify fix** bằng re-scan targeted check
8. **Handle errors gracefully** — báo nguyên nhân, suggest workaround
