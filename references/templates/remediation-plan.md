# IaC Security Remediation Plan

> Generated after scan #{scan_number} | Date: {YYYY-MM-DD}
> Project: {project_name} | Total findings: {N}

---

## Priority Matrix

| Priority | Severity | SLA | Count | Action |
|----------|----------|-----|-------|--------|
| P0 | 🔴 CRITICAL | 24h — block deploy | {N} | Fix NOW |
| P1 | 🟠 HIGH | 1 sprint (2 weeks) | {N} | Fix this sprint |
| P2 | 🟡 MEDIUM | 1 quarter | {N} | Plan + schedule |
| P3 | 🟢 LOW | Backlog | {N} | Track or suppress |

### Severity Classification Rules

Khi Checkov trả `severity = null` hoặc `UNKNOWN` (phổ biến với Checkov OSS), agent PHẢI tự classify theo bảng sau:

| Check Category | → Priority | Rationale |
|----------------|-----------|-----------|
| IAM admin/wildcard (`CKV_AWS_274`, `CKV_AWS_40`) | P0 | Direct privilege escalation risk |
| IAM resource wildcard (`CKV_AWS_111`, `CKV_AWS_109`, `CKV_AWS_356`) | P1 | Over-permissive but scoped |
| Network 0.0.0.0/0 ingress (`CKV_AWS_260`, `CKV_AWS_382`, `CKV_AWS_23`) | P1 | Public exposure |
| VPC flow logs, default SG (`CKV2_AWS_11`, `CKV2_AWS_12`) | P1 | Visibility gap |
| Encryption at rest (`CKV_AWS_19`, `CKV_AWS_7`, `CKV_AWS_16`) | P1 | Data protection |
| S3 logging/replication (`CKV_AWS_18`, `CKV_AWS_144`) | P2 | Observability |
| S3 lifecycle/notifications (`CKV_AWS_300`, `CKV2_AWS_62`) | P2 | Operational hygiene |
| SSM/KMS config (`CKV2_AWS_34`, `CKV2_AWS_64`) | P2 | Defense in depth |
| ALB config (logging, headers, deletion protection) | P3 | Best practice |
| EC2 config (IMDSv2, monitoring, EBS optimized) | P3 | Hardening |
| Unattached resources (`CKV2_AWS_5`, `CKV2_AWS_19`) | P3 | Cleanup |
| Log retention (`CKV_AWS_338`) | P2 | Compliance requirement |

**Nếu check KHÔNG có trong bảng**: classify dựa trên resource type:
- IAM/STS → P1
- Network/SG/VPC → P1
- Storage (S3/EBS/RDS) encryption → P1
- Storage config (logging/lifecycle) → P2
- Compute/monitoring → P3
- Other → P3

---

## P0 — Fix Immediately

| # | Check ID | Finding | Resource | File | Line | Status |
|---|----------|---------|----------|------|------|--------|
| 1 | {CKV_AWS_N} | {check_name} | `{resource}` | `{file_path}` | {line} | ⬚ Open |

**Remediation:** {specific fix guidance per check group}

**Definition of Done**: Re-scan PASS + PR merged + no regression

---

## P1 — Fix This Sprint

### {Subcategory — e.g., "IAM Wildcard Policies"} ({N} findings)

| # | Check ID | Finding | Resource | File | Line | Status |
|---|----------|---------|----------|------|------|--------|
| 1 | {CKV_AWS_N} | {check_name} | `{resource}` | `{file_path}` | {line} | ⬚ Open |

> Nếu >5 cùng Check ID, dùng format grouped:

| Check ID | Count | Description |
|----------|-------|-------------|
| {CKV_AWS_N} | {N} | {check_name} |

**Affected Resources:**
1. `{resource_1}` — `{file_path}:{line}` (caller: `{caller_file if module}`)
2. `{resource_2}` — `{file_path}:{line}`
3. ...

**Remediation:** {specific fix guidance}

---

## P2 — Plan Remediation (This Quarter)

| # | Check ID | Finding | Resource | File | Line | Status |
|---|----------|---------|----------|------|------|--------|
| 1 | {CKV_AWS_N} | {check_name} | `{resource}` | `{file_path}` | {line} | ⬚ Planned |

---

## P3 — Track / Improve (Backlog)

| # | Check ID | Finding | Resource | File | Line | Decision |
|---|----------|---------|----------|------|------|----------|
| 1 | {CKV_AWS_N} | {check_name} | `{resource}` | `{file_path}` | {line} | ⬚ Backlog / ⬚ Suppress / ⬚ Tech Debt |

---

## Effort Estimation

| Priority | Items | Avg Fix Time | Total Effort |
|----------|-------|--------------|--------------|
| P0 | {N} | ~30 min/item | {N}h |
| P1 | {N} | ~1h/item | {N}h |
| P2 | {N} | ~2h/item | {N}h |
| P3 | {N} | N/A (track) | 0h |
| **Total** | **{N}** | | **{N}h** |

---

## Success Criteria

- [ ] 0 P0 findings
- [ ] 0 P1 findings (or approved exception with compensating control)
- [ ] P2 items scheduled with target dates
- [ ] P3 items tracked in tech-debt.md or suppressed
- [ ] Baseline created for accepted items
- [ ] Next scan shows delta ≤ 0 (no regression)

---

## Agent Rules (cho AI khi generate file này)

### Auto-Generate (Level 1 — từ scan data, KHÔNG cần user input):
1. Priority Matrix counts — từ classification rules ở trên
2. ALL findings listed — grouped by priority, subcategorized by check type
3. Remediation guidance per group — từ fix patterns (xem checkov-aws-scan.md Phase 5.2)
4. Effort Estimation — based on item counts × avg time
5. Success Criteria — standard checklist

### Enrich (Level 2 — cần user input, OPTIONAL):
- Owner per finding/group — agent hỏi "Ai chịu trách nhiệm fix nhóm IAM?"
- ETA/Sprint per priority — agent hỏi "Sprint nào fix P1?"
- Dependencies & Blockers — agent hỏi "Có blocker nào không?"
- Sign-off — chỉ khi user yêu cầu formal approval flow

### Grouping Rules:
- Nếu >5 findings cùng Check ID → group thành 1 header row + detail list bên dưới
- Detail list format (ngay sau group header):
  ```
  **Affected Resources:**
  1. `{resource}` — `{file_path}:{line}`
  2. `{resource}` — `{file_path}:{line}`
  ```
- Nếu ≤5 findings cùng Check ID → list từng row riêng (không group)
- Nếu findings cùng file + cùng module → group theo module, vẫn list per-resource
- Subcategories: IAM, Network, Storage, Compute, Logging, Other
- **KHÔNG BAO GIỜ** chỉ ghi "8 findings" mà không liệt kê resource nào + file:line nào

### CRITICAL — Severity UNKNOWN Handling:
- Checkov OSS (free) KHÔNG có severity metadata cho hầu hết checks
- Agent PHẢI classify theo bảng "Severity Classification Rules" ở trên
- GHI NOTE ở đầu file: "Severity classified by check type (Checkov OSS does not provide severity metadata)"
- KHÔNG để cả 85 findings trong "UNKNOWN" — PHẢI phân loại

---

*Template version: 2.0 | Power: iac-checkov-aws v1.0.0*
