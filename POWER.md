---
name: "iac-checkov-aws"
displayName: "IaC Checkov AWS"
description: "Scan và bảo mật AWS Infrastructure as Code (Terraform, CloudFormation) bằng Checkov. Chạy trực tiếp local với plan, tracking, memory giữa sessions, và remediation tự động."
keywords: ["iac", "checkov", "terraform", "cloudformation", "aws", "security", "compliance", "cis", "pci-dss", "hipaa", "soc2", "policy-as-code", "cloud-security", "infrastructure-as-code", "devsecops", "scanning"]
author: "TDFS-Dom"
---

# IaC Checkov AWS — Kiro Power

Scan và bảo mật AWS Infrastructure as Code bằng Checkov. Power này chạy trực tiếp trên máy local, lifecycle-driven với plan → memory → tracking.

## Overview

Power này cung cấp **lifecycle-driven SecOps workflow** — từ planning đến reporting, với state tracking và session continuity.

**SecOps Lifecycle:**
```
plan → scan → analyze → track → remediate → verify → report
```

**Key capabilities:**
- Chạy Checkov trực tiếp trên local machine
- Full scan mặc định (456 AWS checks — KHÔNG filter)
- Plan trước mỗi scan (user approve trước khi execute)
- Tracking history giữa các lần scan (delta comparison)
- Project memory (decisions, suppressions, patterns)
- State-aware continuation ("tiếp tục" → inspect → recommend)
- Auto-remediation với verify loop
- Compliance mapping (CIS, PCI-DSS, HIPAA, SOC2, NIST, GDPR)
- Impact analysis khi thay đổi scope/suppression

## When to Load Steering Files

### Always-loaded (core contract + routing)
- Understanding lifecycle, paths, prerequisites, behavior rules → `secops-contract.md`
- Routing user intent to correct workflow → `secops-routing.md`

### On-demand (load per active command)
- Running scan workflow → `checkov-aws-scan.md`
- Compliance analysis → `checkov-aws-compliance.md`
- Reviewing skip/suppression logic + outdated skips → `checkov-aws-skip-review.md`
- Detecting next step → `secops-contract.md` (Next Step section)
- Token budget management → `secops-token-budget.md`
- Export report to .docx → `docx-export.md`

## Quick Start

### Scan lần đầu
```
Scan Terraform infrastructure cho AWS security
```

### Tiếp tục sau session trước
```
Tiếp tục — bước tiếp theo là gì?
```

### Fix specific finding
```
Fix CKV_AWS_93 trong s3.tf
```

### Compliance report
```
Report compliance CIS AWS cho infrastructure hiện tại
```

### Review skip logic
```
Review skip — kiểm tra logic các checkov:skip trong code
```

### Check outdated suppressions
```
Review outdate — tìm skip hết hạn hoặc không còn valid
```

### Đánh giá thay đổi
```
Tôi muốn suppress CKV_AWS_17 cho dev environment — đánh giá impact
```

## Output Directory Structure

```
{project}/
├── .checkov-reports/
│   ├── state/
│   │   ├── tracking.md          # Scan timeline (append-only)
│   │   └── project-memory.md    # Decisions, config, suppressions
│   ├── scans/
│   │   ├── 001/                 # Per-scan self-contained snapshot
│   │   │   ├── plan.md
│   │   │   ├── metadata.md
│   │   │   ├── results.json
│   │   │   ├── summary.md
│   │   │   ├── remediation-plan.md
│   │   │   └── tech-debt.md
│   │   ├── 002/
│   │   │   ├── ... (same + delta.md)
│   │   └── latest.txt           # "002"
│   └── reports/
│       └── compliance/
├── .checkov.yaml
└── .checkov.baseline
```

## Behavior Rules (Summary)

Full rules in `secops-contract.md`. Key points:

1. **Plan-First** — KHÔNG scan khi chưa có user approve plan
2. **Full-Scan Default** — Quét TẤT CẢ 456 checks, phân loại SAU
3. **Append-Only** — Tracking history chỉ append, KHÔNG overwrite
4. **Fail-Closed** — Ambiguous directory? Stop and ask
5. **Impact-First** — Thay đổi scope/suppression → impact analysis trước
6. **Auto-Verify** — Fix xong → tự re-scan check đó
7. **Overwrite Protection** — KHÔNG ghi đè files khi chưa approve
8. **Security** — KHÔNG scan directories chứa secrets

## Execution Model

### Phase 1: PLAN
- Detect IaC files (find .tf, .yaml)
- Check checkov installed
- Check existing state (tracking.md, baseline)
- Present plan → wait for approval

### Phase 2: SCAN (local execution)
```bash
checkov -d {target} --framework {fw} --compact -o json \
  --output-file-path .checkov-reports/scans/{NNN}
```

### Phase 3: ANALYZE
- Parse JSON → severity breakdown
- Top findings list (CRITICAL → HIGH → MEDIUM → LOW)
- Present summary tables

### Phase 4: TRACK
- Append scan entry to tracking.md
- Calculate delta vs previous scan
- Update remediation log

### Phase 5: REMEDIATE (on request)
- Read finding detail → suggest fix
- Apply fix → re-scan targeted → verify PASS/FAIL
- Update tracking

### Phase 6: VERIFY
- Re-scan targeted checks after fix
- Report PASS/FAIL

### Phase 7: REPORT
- Generate compliance report
- Map findings to frameworks (CIS/PCI/HIPAA/SOC2)

## Session Continuity

Khi user quay lại (new session):
1. Đọc `.checkov-reports/state/tracking.md` → scan history
2. Đọc `.checkov-reports/state/project-memory.md` → decisions
3. Báo context + recommend next action

```
📊 SecOps Status
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Scans: 3 performed
Last: 2026-05-26 — 12 findings (2 CRITICAL, 5 HIGH)
Fixed: 7/12
Pending: 5 (0 CRITICAL, 3 HIGH, 2 MEDIUM)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
→ Next: Fix 3 HIGH findings
→ Priority: CKV_AWS_23 — vpc.tf:42
```

## Key AWS Checks (Quick Reference)

| Check ID | Service | Description | Severity |
|----------|---------|-------------|----------|
| CKV_AWS_93 | S3 | Public access not blocked | CRITICAL |
| CKV_AWS_19 | S3 | No encryption at rest | HIGH |
| CKV_AWS_20 | S3 | SSL not enforced | HIGH |
| CKV_AWS_21 | S3 | No versioning | MEDIUM |
| CKV_AWS_23 | VPC | SG open to 0.0.0.0/0 | HIGH |
| CKV_AWS_7 | EC2 | EBS not encrypted | HIGH |
| CKV_AWS_16 | RDS | Storage not encrypted | HIGH |
| CKV_AWS_40 | IAM | Wildcard actions in policy | HIGH |
| CKV_AWS_49 | CloudTrail | Not enabled | HIGH |
| CKV_AWS_41 | EKS | Encryption not enabled | HIGH |

## Tech Stack

| Framework | File Types | Command |
|---|---|---|
| Terraform | `.tf` | `checkov -d . --framework terraform` |
| CloudFormation | `.yaml/.json` | `checkov -d . --framework cloudformation` |
| Serverless (SAM) | `.yaml` | `checkov -d . --framework serverless` |

---

## Changelog

### v1.2.0 (2026-05-28)
- Add `checkov-aws-skip-review.md` steering — review logic + detect outdated suppressions
- Add `references/severity-classification.md` — single source of truth cho severity classification khi Checkov OSS không có severity metadata
- New commands: `review-skip`, `review-outdate`
- Suppress command enhanced: severity-gated validation, mandatory justification
- Known false positive auto-detection (GWLB, module SGs, EIP NAT, Lambda monitoring)
- Quarterly review reminder mechanism
- Remediation-plan template now references severity-classification.md (không inline rules)
- Now 7 steering files (2 always-loaded + 5 on-demand)

### v1.1.0 (2026-05-28)
- Add `docx-export.md` steering (export security reports to .docx)
- Fix severity UNKNOWN handling (classification rules for Checkov OSS)
- Upgrade `remediation-plan.md` and `tech-debt.md` templates to v2.0
- Add Level 1/2 approach for tech-debt (auto-generate vs user-enriched)
- Fix cross-file path inconsistencies
- Now 6 steering files (2 always-loaded + 4 on-demand)

### v1.0.0 (2026-05-26)
- Initial release
- Lifecycle-driven architecture (contract, routing, token-budget)
- 5 steering files (2 always-loaded + 3 on-demand)
- Full scan default (456 AWS checks)
- Plan → Scan → Analyze → Track → Remediate → Verify → Report
- State-aware continuation (tiếp tục → inspect → recommend)
- Project memory pattern for cross-session continuity
- Compliance mapping: CIS, PCI-DSS, HIPAA, SOC2, NIST, GDPR
- Auto-verify after remediation
