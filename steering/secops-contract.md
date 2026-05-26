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
| 1. Plan | `plan` | scan-plan.md |
| 2. Scan | `scan` | results_json.json + scan-log.txt |
| 3. Analyze | `analyze` | Summary tables + severity breakdown |
| 4. Track | `track` | tracking.md (append scan entry) |
| 5. Remediate | `fix` | Modified .tf/.yaml files |
| 6. Verify | `verify` | Re-scan targeted checks |
| 7. Report | `report` | compliance-report.md |

## Paths

```yaml
project_root: .checkov-reports/
tracking: .checkov-reports/tracking.md
project_memory: .checkov-reports/project-memory.md
plans: .checkov-reports/plans/
results_json: .checkov-reports/results_json.json
results_cli: .checkov-reports/results_cli.txt
scan_log: .checkov-reports/scan-log.txt
compliance_report: .checkov-reports/compliance-report.md
baseline: .checkov.baseline
config: .checkov.yaml
custom_checks: ./custom_checks/
```

## Commands & Prerequisites

| Command | Requires | Outputs |
|---|---|---|
| plan | IaC files detected | scan-plan.md |
| scan | plan approved + checkov installed | results_json.json |
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

File `.checkov-reports/project-memory.md` lưu trữ:
- Scan scope decisions (which dirs, which frameworks)
- Suppression decisions (why skip specific checks)
- Known false positives (approved suppressions)
- Compliance targets (CIS/PCI/HIPAA đã chọn)
- Fix patterns applied (recurring remediation patterns)
- Environment notes (dev/staging/prod differences)

Cập nhật project-memory sau:
- User approve suppression
- User fix finding
- User change scan scope
- User select compliance target
