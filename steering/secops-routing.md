# IaC Checkov AWS — Routing

Khi user dùng ngôn ngữ tự nhiên, route intent theo bảng sau. Đây là dispatcher — KHÔNG tự làm downstream work.

## Routing Table

| User nói... | Route to | Load steering |
|---|---|---|
| Scan Terraform / quét IaC / check security | `plan` → `scan` | `checkov-aws-scan.md` |
| Kiểm tra compliance / CIS / PCI / HIPAA | `compliance` | `checkov-aws-compliance.md` |
| Fix finding / sửa lỗi {CHECK_ID} | `fix` | `checkov-aws-scan.md` (Phase 5) |
| Tiếp tục / bước tiếp theo | `next` | Inspect artifacts → recommend |
| Trạng thái / status / đang ở đâu | `status` | Inspect `.checkov-reports/` |
| Tạo baseline / lock hiện trạng | `baseline` | `checkov-aws-scan.md` |
| Suppress / bỏ qua check | `suppress` | `secops-contract.md` (Overwrite Protection) |
| Report / báo cáo | `report` | `checkov-aws-compliance.md` |
| Tạo remediation plan / plan fix | `remediation-plan` | Generate from results + template |
| Tạo tech debt / debt register | `tech-debt` | Generate from baseline + template |
| Scan lại / re-scan | `plan` → `scan` | `checkov-aws-scan.md` |
| Custom policy / tạo rule riêng | `custom-policy` | `checkov-aws-compliance.md` |
| So sánh / delta / thay đổi gì | `delta` | Inspect tracking.md |
| Cài đặt checkov / install | `install` | `checkov-aws-scan.md` (Auto-Install) |

## Routing Priority

Khi ambiguous:
- **Prefer `plan` → `scan`** nếu chưa có scan nào (first time)
- **Prefer `next`** nếu user nói "tiếp tục" và đã có scan trước đó
- **Prefer `fix`** nếu user mention CHECK_ID cụ thể (CKV_AWS_*)
- **Prefer `compliance`** nếu user nói framework name (CIS, PCI, HIPAA, SOC2)

## Natural Language Aliases

| User nói | Agent hiểu |
|---|---|
| Quét / scan / check | plan → scan |
| An toàn không? / secure? | plan → scan → analyze |
| Có lỗi gì? / findings? | analyze (nếu có results) hoặc scan (nếu chưa) |
| Fix / sửa / remediate | fix (cần CHECK_ID) |
| Bỏ qua / suppress / skip | suppress |
| Tạo baseline | baseline |
| Báo cáo / report / tổng hợp | report |
| Tiếp tục / next / làm gì tiếp | next |
| Delta / so sánh / thay đổi | delta (so sánh 2 scans) |
| CIS / PCI / HIPAA / SOC2 | compliance {framework} |
| Custom rule / policy riêng | custom-policy |
| Plan fix / ưu tiên / roadmap | remediation-plan |
| Tech debt / debt / nợ kỹ thuật | tech-debt |

## Display Format

After routing, show:
```
🛡️ SecOps Routing
Input: {short excerpt}
→ Route: {command}
→ Load: {steering file}
→ Reason: {one-line reason}
```

Then load the steering file and execute.

## State-Aware Continuation

Khi user nói "tiếp tục" hoặc "bước tiếp theo":

1. Inspect `.checkov-reports/` directory
2. Check which artifacts exist:
   - `tracking.md` exists? → có history
   - `scans/latest.txt` exists? → có scan gần nhất
   - `.checkov.baseline` exists? → đã baseline
   - Pending CRITICAL/HIGH trong tracking? → suggest fix
3. Recommend next action theo priority:
   - Có CRITICAL chưa fix → suggest fix
   - Có HIGH chưa fix → suggest fix
   - Tất cả fixed → suggest re-scan verify
   - Clean scan → suggest baseline hoặc report

```
📊 SecOps Status
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Scans performed: 3
Last scan: 2026-05-26 14:30
Findings: 12 (2 CRITICAL, 5 HIGH, 3 MEDIUM, 2 LOW)
Fixed: 7/12
Pending: 5 (0 CRITICAL, 3 HIGH, 2 MEDIUM)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
→ Next: Fix 3 HIGH findings còn lại
→ Top priority: CKV_AWS_23 (Security group open) — vpc.tf:42
```
