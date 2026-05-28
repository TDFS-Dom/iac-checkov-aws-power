# IaC Checkov AWS — Contract

Core contract cho IaC Checkov AWS Power. File này được load TRƯỚC mọi steering file khác.

## Defaults

- Language: `vi` (Vietnamese) cho giải thích, English cho commands/output
- Scan mode: **FULL SCAN** — tất cả checks Checkov cung cấp (456)
- Framework detection: Auto (Terraform/CloudFormation/Serverless)
- Execution: Trực tiếp trên máy local
- Output format: JSON + CLI
- Tracking: Append-only (KHÔNG overwrite history)

## SecOps Lifecycle

```
plan → scan → analyze → track → remediate → verify → report
```

| Phase | Command | Output |
|---|---|---|
| 1. Plan | `plan` | scans/{NNN}/plan.md |
| 2. Scan | `scan` | scans/{NNN}/results.json |
| 3. Analyze | `analyze` | Summary tables + severity breakdown |
| 4. Track | `track` | tracking.md (append scan entry) |
| 5. Remediate | `fix` | Modified .tf/.yaml files |
| 6. Verify | `verify` | Re-scan targeted checks |
| 7. Report | `report` | compliance-report.md |

## Paths

```yaml
# State (persistent, read every session)
state_tracking: .checkov-reports/state/tracking.md
state_memory: .checkov-reports/state/project-memory.md

# Scans (versioned per scan)
scans_dir: .checkov-reports/scans/
scan_folder: .checkov-reports/scans/{NNN}/
scan_metadata: .checkov-reports/scans/{NNN}/metadata.md
scan_results: .checkov-reports/scans/{NNN}/results.json
scan_summary: .checkov-reports/scans/{NNN}/summary.md
scan_plan: .checkov-reports/scans/{NNN}/plan.md
scan_delta: .checkov-reports/scans/{NNN}/delta.md
scan_latest: .checkov-reports/scans/latest.txt

# Per-scan artifacts (snapshot per scan)
scan_remediation_plan: .checkov-reports/scans/{NNN}/remediation-plan.md
scan_tech_debt: .checkov-reports/scans/{NNN}/tech-debt.md

# Reports (on-demand, aggregated cross-scan)
reports_dir: .checkov-reports/reports/
compliance_report: .checkov-reports/reports/compliance/{framework}.md

# Config
config: .checkov.yaml
baseline: .checkov.baseline
```

### Scan Versioning Rules
- Folder name = 3-digit zero-padded: `001/`, `002/`, `003/`
- `latest.txt` = single line containing current scan number (e.g. "003")
- `delta.md` created from scan #002 onwards
- `results.json` = raw Checkov JSON output (KHÔNG modify)
- `summary.md` = human-readable (generated from results.json)
- `metadata.md` = scan context (date, version, scope, duration)
- Templates in `references/templates/` — agent PHẢI dùng đúng format

## Commands & Prerequisites

| Command | Requires | Outputs |
|---|---|---|
| plan | IaC files detected | scans/{NNN}/plan.md |
| scan | plan approved + checkov installed | scans/{NNN}/results.json |
| analyze | scan results exist | Summary (display only) |
| track | scan results exist | tracking.md (append) |
| fix {CHECK_ID} | scan results + finding in JSON | Modified source file |
| verify {CHECK_ID} | fix applied | Re-scan result (PASS/FAIL) |
| report | ≥1 scan in tracking | compliance-report.md |
| baseline | scan results exist | .checkov.baseline |
| status | — | Current state inspection |
| next | — | Recommended next action |
| compliance {framework} | scan results exist | Filtered compliance view |
| suppress {CHECK_ID} | scan results | Inline comment added to .tf |

## Resolution Rules

### Target Directory
1. Prefer explicit path từ user
2. Scan workspace cho `.tf` files → use parent directory
3. If multiple directories → stop and ask

### Framework
1. `.tf` → terraform
2. `.yaml/.yml` with `AWSTemplateFormatVersion` → cloudformation
3. `.yaml/.yml` with `Transform: AWS::Serverless` → serverless
4. Mixed → scan all frameworks

## Behavior Rules

### Fail-Closed
- KHÔNG tự chọn directory khi ambiguous → hỏi user
- KHÔNG tự chạy scan khi chưa có plan approval
- KHÔNG tự install checkov khi chưa hỏi user

### Plan-First Rule
- MỌI scan PHẢI có plan được user approve trước
- Plan show: target, files count, framework, mode, estimated time
- Ngoại lệ: `verify` (re-scan targeted) không cần plan mới

### Full-Scan Default
- KHÔNG dùng `--check` hoặc `--hard-fail-on` khi scan
- Quét TẤT CẢ 456 checks → phân loại severity SAU
- Chỉ filter khi user yêu cầu compliance-specific
- **Severity UNKNOWN**: Checkov OSS thường không có severity metadata → agent lookup `references/aws-checks-full-list.md` (cột Severity) trước. Nếu check mới không có trong list → dùng `references/severity-classification.md` Scoring Matrix.

### Severity Lookup Rule (BẮT BUỘC — vi phạm = kết quả sai)
- **MỌI lần classify severity** (generate summary, remediation-plan, tech-debt, hoặc hiển thị cho user) → agent PHẢI đọc file `references/severity-map.md` và tìm Check ID thuộc section nào (CRITICAL/HIGH/MEDIUM/LOW).
- **KHÔNG ĐƯỢC** tự đoán severity từ check description hay "cảm giác".
- **KHÔNG ĐƯỢC** dùng keyword "encrypted" → HIGH. Keyword-based classification bị cấm.
- **CÁCH LÀM ĐÚNG**: Mở file `references/severity-map.md` → tìm Check ID → severity = heading chứa nó.

#### COMMON MISTAKES (agent PHẢI nhớ — đây là checks hay bị classify SAI):

| Check ID | Mô tả | ❌ Agent HAY GÁN SAI | ✅ ĐÚNG (theo file) | Lý do |
|----------|--------|---------------------|---------------------|-------|
| CKV_AWS_189 | EBS Volume encrypted by KMS CMK | HIGH | **LOW** | CMK upgrade — default encryption đã có |
| CKV_AWS_158 | CloudWatch Log Group encrypted by KMS | HIGH | **LOW** | CMK upgrade — default encryption đã có |
| CKV2_AWS_34 | SSM Parameter encrypted | HIGH | **LOW** | CMK upgrade — default encryption đã có |
| CKV_AWS_331 | TGW auto-accept attachments | HIGH | **MEDIUM** | Internal org only, not public exposure |
| CKV_AWS_123 | VPC Endpoint manual acceptance | HIGH | **MEDIUM** | Operational control, not direct exploit |
| CKV_AWS_144 | S3 cross-region replication | HIGH | **MEDIUM** | DR gap, not security breach |
| CKV2_AWS_19 | EIP not attached | HIGH/MEDIUM | **MEDIUM** | Cost waste, not security |
| CKV_AWS_272 | Lambda code signing | HIGH | **MEDIUM** | Defense-in-depth, not immediate risk |
| CKV2_AWS_62 | S3 event notifications | HIGH | **MEDIUM** | Operational hygiene, not security breach |
| CKV2_AWS_61 | S3 lifecycle configuration | HIGH | **MEDIUM** | Operational hygiene, not security breach |
| CKV2_AWS_64 | KMS key policy not defined | MEDIUM | **HIGH** | Key policy = access control for encryption keys |

**Pattern rule**: Bất kỳ check nào nói "encrypted by KMS using CMK" hoặc "encrypted using customer managed Key" = **LOW** (trừ CloudTrail CMK = HIGH vì tamper protection).

### Append-Only Tracking
- tracking.md chỉ APPEND, KHÔNG overwrite
- Mỗi scan = 1 entry mới với timestamp
- Delta tính so với scan trước

### Overwrite Protection
- KHÔNG ghi đè results cũ khi re-scan (archive nếu cần)
- KHÔNG sửa source file khi chưa user approve fix
- KHÔNG tạo baseline khi chưa user approve

### Impact-First Rule (cho remediation)
- Khi user nói "fix all" → show impact matrix trước
- List tất cả files sẽ bị modify
- CHỈ fix sau khi user approve

### Auto-Verify Rule
- Sau mỗi fix → TỰ ĐỘNG chạy `checkov -f {file} --check {CHECK_ID}`
- Report PASS/FAIL ngay
- Nếu FAIL → báo user, suggest alternative fix

### Large Scan Protocol
- Scan >100 findings → show top 20 (sorted by severity) trước
- Hỏi "Muốn xem thêm?" trước khi list all
- Group by: service > severity > file

## Security Rules (ƯU TIÊN CAO NHẤT)

- **CẤM** scan directories chứa secrets (.env, credentials, keys)
- **CẤM** log credentials trong scan-log.txt
- **CẤM** push .checkov-reports/ lên git nếu chứa sensitive paths
- Credentials (Prisma/Bridgecrew API key) chỉ qua environment variables
- `.checkov-reports/` PHẢI có trong `.gitignore`

## Project Memory

File `state/project-memory.md` lưu trữ:
- Scan scope decisions (which dirs, which frameworks)
- Suppression decisions (why skip specific checks)
- Known false positives (approved suppressions)
- Compliance targets (CIS/PCI/HIPAA đã chọn)
- Fix patterns applied (recurring remediation patterns)
- Environment notes (dev/staging/prod differences)
- Decisions log (mỗi quyết định quan trọng)
- Session history (last 5 actions)

**Template**: Tạo từ `references/templates/project-memory.md` khi lần đầu scan.

Cập nhật project-memory sau:
- User approve suppression
- User fix finding
- User change scan scope
- User select compliance target
- User make ANY configuration decision

## What Goes Where (CRITICAL — tránh loạn)

| Thông tin | File | Khi nào ghi |
|-----------|------|-------------|
| Scan results (raw) | `scans/{NNN}/results.json` | Mỗi scan |
| Scan context | `scans/{NNN}/metadata.md` | Mỗi scan |
| Findings summary | `scans/{NNN}/summary.md` | Mỗi scan |
| Scan plan (approved) | `scans/{NNN}/plan.md` | Mỗi scan |
| Delta vs previous | `scans/{NNN}/delta.md` | Từ scan #002 |
| Remediation plan | `scans/{NNN}/remediation-plan.md` | Mỗi scan (per-scan snapshot) |
| Tech debt register | `scans/{NNN}/tech-debt.md` | Mỗi scan (per-scan snapshot) |
| Latest scan number | `scans/latest.txt` | Mỗi scan (overwrite) |
| Scan history timeline | `state/tracking.md` | Mỗi scan (APPEND) |
| Config decisions | `state/project-memory.md` | Khi user quyết định |
| Compliance report | `reports/compliance/{fw}.md` | Khi user yêu cầu (aggregated) |
| Scan config | `.checkov.yaml` | Lần đầu setup |
| Baseline lock | `.checkov.baseline` | Khi user approve |

### Quy tắc:
1. **state/** = persistent cross-session — đọc MỌI session
2. **scans/{NNN}/** = self-contained snapshot (plan + results + summary + remediation + debt + delta)
3. **reports/** = aggregated cross-scan (compliance only)
4. **Mỗi scan folder = đủ context riêng** — không cần xem folder khác
5. **Session resumption**: `state/` → `scans/latest.txt` → `scans/{latest}/summary.md`
6. **Templates**: agent PHẢI dùng format từ `references/templates/`
