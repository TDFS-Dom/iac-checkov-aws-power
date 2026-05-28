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
test -f .checkov-reports/state/tracking.md && echo "EXISTING_TRACKING" || echo "FIRST_SCAN"

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
# Determine next scan number
LATEST=$(cat .checkov-reports/scans/latest.txt 2>/dev/null || echo "000")
NEXT=$(printf "%03d" $((10#$LATEST + 1)))
mkdir -p .checkov-reports/scans/$NEXT
mkdir -p .checkov-reports/state
mkdir -p .checkov-reports/reports
```

### Step 2.2: Save Plan

Lưu plan đã approve vào scan folder:

Tạo file `.checkov-reports/scans/{NNN}/plan.md` với nội dung plan.

### Step 2.3: Run Scan

**MẶC ĐỊNH: Quét TOÀN BỘ checks mà Checkov cung cấp cho AWS** — KHÔNG filter hay limit checks trừ khi user yêu cầu cụ thể.

```bash
# FULL AWS SCAN — tất cả built-in checks (456 AWS checks)
checkov -d {target_dir} \
  --framework {framework} \
  --compact \
  -o json \
  --output-file-path .checkov-reports/scans/$NEXT \
  

# Update latest pointer
echo "$NEXT" > .checkov-reports/scans/latest.txt
```

**Nếu có baseline:**
```bash
checkov -d {target_dir} \
  --framework {framework} \
  --baseline .checkov.baseline \
  --compact \
  -o json \
  --output-file-path .checkov-reports/scans/$NEXT
```

**CHỈ KHI user yêu cầu compliance-specific mới filter:**
```bash
# CIS AWS (chỉ khi user hỏi CIS)
checkov -d {target_dir} --check CIS_AWS -o json --output-file-path .checkov-reports/scans/$NEXT

# PCI-DSS (chỉ khi user hỏi PCI)
checkov -d {target_dir} --check CKV_AWS_19,CKV_AWS_61,CKV_AWS_7,CKV_AWS_89,CKV_AWS_23,CKV_AWS_40,CKV_AWS_18,CKV_AWS_49 -o json --output-file-path .checkov-reports/scans/$NEXT

# HIPAA (chỉ khi user hỏi HIPAA)
checkov -d {target_dir} --check CKV_AWS_19,CKV_AWS_7,CKV_AWS_61,CKV_AWS_20,CKV_AWS_18,CKV_AWS_40,CKV_AWS_49,CKV_AWS_23,CKV_AWS_27 -o json --output-file-path .checkov-reports/scans/$NEXT
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

### Step 2.5: Post-Scan Files (BẮT BUỘC — KHÔNG ĐƯỢC SKIP)

Sau khi checkov chạy xong, agent PHẢI tạo TẤT CẢ files sau trong `.checkov-reports/scans/$NEXT/`:

```bash
# Rename checkov output
mv .checkov-reports/scans/$NEXT/results_json.json .checkov-reports/scans/$NEXT/results.json 2>/dev/null
```

**Checklist — tạo từng file từ template:**

> Parse results.json theo hướng dẫn `references/templates/parse-results-guide.md`
> PHẢI extract data thực từ JSON — KHÔNG để placeholder, KHÔNG bỏ trống.

- [ ] `results.json` — renamed từ Checkov output (KHÔNG tự tạo)
- [ ] `metadata.md` — fill template, ghi scan context (date, scope, duration, version)
- [ ] `summary.md` — parse results.json → fill TẤT CẢ fields (counts, severity, by-folder, top findings)
- [ ] `remediation-plan.md` — parse results.json → liệt kê TẤT CẢ findings grouped by P0/P1/P2/P3
- [ ] `tech-debt.md` — parse results.json → list MEDIUM+LOW items với justification
- [ ] `delta.md` — so sánh 2 results.json → list new/resolved/unchanged (CHỈ từ scan #002)
- [ ] `plan.md` — đã tạo trước scan, PHẢI nằm trong folder này

**Update state:**

- [ ] `state/tracking.md` — APPEND row mới vào Timeline
- [ ] `state/project-memory.md` — update nếu có decision mới
- [ ] `scans/latest.txt` — overwrite với scan number hiện tại

**KHÔNG ĐƯỢC dừng sau bước này nếu user yêu cầu "scan toàn bộ dự án" hoặc "scan full" — PHẢI tiếp tục Phase 3 → Phase 7 (full pipeline).**

Verify:
```bash
echo "=== Verify scan $NEXT files ==="
for f in results.json metadata.md summary.md remediation-plan.md tech-debt.md plan.md; do
  test -f ".checkov-reports/scans/$NEXT/$f" && echo "✅ $f" || echo "❌ MISSING: $f"
done
```

---

## PHASE 3: ANALYZE

### Step 3.1: Parse Results

Đọc `.checkov-reports/scans/{NNN}/results.json` và extract:

```bash
# Summary counts
python3 -c "
import json
with open('.checkov-reports/scans/$NEXT/results.json') as f:
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
with open('.checkov-reports/results.json') as f:
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
with open('.checkov-reports/results.json') as f:
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

### Step 4.1: Generate Scan Artifacts

Sau mỗi scan, tạo các files trong `scans/{NNN}/`:
- `metadata.md` — from template `references/templates/metadata.md`
- `summary.md` — from template `references/templates/summary.md`
- `delta.md` — from template `references/templates/delta.md` (từ scan #002)

### Step 4.2: Update Tracking

**APPEND** entry mới vào `.checkov-reports/state/tracking.md`:
- Nếu file chưa tồn tại → tạo từ template `references/templates/tracking.md`
- Thêm row mới vào Timeline table
- Update "Total Scans" và "Latest Scan" trong header

### Step 4.3: Delta Calculation

So sánh với scan trước (`scans/{NNN-1}/results.json`):
- Tổng failed: +/- bao nhiêu
- New findings (có trong current, không có trong previous)
- Resolved findings (có trong previous, không có trong current)
- Ghi vào `scans/{NNN}/delta.md`

---

## FULL PIPELINE RULE

**Khi user nói "scan toàn bộ dự án" / "scan full" / "quét hết":**

Agent PHẢI chạy TOÀN BỘ pipeline KHÔNG DỪNG giữa chừng:

```
Phase 1 (Plan) → Phase 2 (Scan) → Phase 3 (Analyze) → Phase 4 (Track)
```

Output cuối cùng trình user = `summary.md` content (hiển thị trong chat) + tất cả files đã tạo trong `scans/{NNN}/`.

Agent KHÔNG HỎI "bạn muốn làm gì tiếp?" giữa các phase — chạy hết rồi mới trình kết quả.

---

## PHASE 5: REMEDIATE (Khi user yêu cầu fix)

### Step 5.1: Identify Fix

Đọc finding detail từ scan results:
```bash
LATEST=$(cat .checkov-reports/scans/latest.txt)
python3 -c "
import json
with open(f'.checkov-reports/scans/$LATEST/results.json') as f:
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

1. Check `.checkov-reports/state/project-memory.md` → đọc decisions
2. Check `.checkov-reports/state/tracking.md` → đọc timeline
3. Check `.checkov-reports/scans/latest.txt` → lấy scan number
4. Đọc `scans/{latest}/summary.md` → current findings
5. Báo user context:
   ```
   � SecOps Status
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   Scans: {N} performed (latest: #{NNN})
   Last: {date} — {failed} findings ({critical} CRITICAL)
   Pending: {N} items unfixed
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   → Next: [re-scan] [fix pending] [report] [new scope]
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
