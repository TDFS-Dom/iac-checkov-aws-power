# IaC Security Remediation Plan

> Generated after scan #{scan_number} | Date: {YYYY-MM-DD}
> Project: {project_name} | Total findings: {N}

## HARD CONSTRAINT — Per-Resource Detail (KHÔNG ĐƯỢC BỎ QUA)

**MỌI finding PHẢI có `resource + file_path + line`.** Cụ thể:

- Mỗi finding từ `results.json` = 1 row HOẶC 1 item trong "Affected Resources" list
- KHÔNG BAO GIỜ chỉ ghi "8 findings" hoặc "CKV_AWS_111 | 8 | description" mà không liệt kê 8 resources đó
- Format bắt buộc cho grouped findings:

```markdown
### CKV_AWS_111 — {description} ({N} findings)

| # | Resource | File | Line |
|---|----------|------|------|
| 1 | `aws_iam_policy_document.kms_policy` | `_modules/kms/main.tf` | 23 |
| 2 | `aws_iam_policy_document.kms_policy` | `_modules/kms/main.tf` | 23 |
...mỗi instance 1 row — KHÔNG skip, KHÔNG truncate...

**Remediation:** {fix guidance}
```

- Nếu cùng resource + cùng file nhưng khác caller (module instances) → vẫn list từng row, thêm cột `Caller`:

```markdown
| # | Resource | File | Line | Caller |
|---|----------|------|------|--------|
| 1 | `aws_iam_policy_document.kms_policy` | `_modules/kms/main.tf` | 23 | `information-security/kms/main.tf:5` |
| 2 | `aws_iam_policy_document.kms_policy` | `_modules/kms/main.tf` | 23 | `log-archive/kms/main.tf:3` |
```

**Data source**: `results.json` → `results.failed_checks[]` → extract `resource`, `file_path`, `file_line_range[0]`, `caller_file_path`

---

## Priority Matrix

| Priority | Severity | SLA | Count | Action |
|----------|----------|-----|-------|--------|
| P0 | 🔴 CRITICAL | 24h — block deploy | {N} | Fix NOW |
| P1 | 🟠 HIGH | 1 sprint (2 weeks) | {N} | Fix this sprint |
| P2 | 🟡 MEDIUM | 1 quarter | {N} | Plan + schedule |
| P3 | 🟢 LOW | Backlog | {N} | Track or suppress |

### Severity Classification Rules

Khi Checkov trả `severity = null` hoặc `UNKNOWN` (phổ biến với Checkov OSS), agent PHẢI classify theo file:

**→ `references/severity-map.md`** (456 checks grouped by severity — compact lookup)
**→ `references/severity-classification.md`** (Scoring Matrix — chỉ dùng cho checks MỚI không có trong list)

Agent PHẢI:
1. Đọc `references/severity-map.md` → tìm Check ID thuộc section nào (CRITICAL/HIGH/MEDIUM/LOW)
2. Nếu Check ID KHÔNG có trong file (check mới) → đọc `references/severity-classification.md` → dùng Scoring Matrix
3. KHÔNG tự classify theo cảm tính — MỌI classification phải trace được tới 1 trong 2 files trên

GHI NOTE ở đầu remediation-plan: "Severity lookup from `references/severity-map.md` (Checkov OSS does not provide severity metadata)"

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
- Agent PHẢI lookup `references/severity-map.md` (cột Severity) cho mỗi Check ID. Nếu check mới → dùng `references/severity-classification.md` Scoring Matrix.
- GHI NOTE ở đầu file: "Severity lookup from `references/severity-map.md` (Checkov OSS does not provide severity metadata)"
- KHÔNG để cả findings trong "UNKNOWN" — PHẢI phân loại

---

*Template version: 2.0 | Power: iac-checkov-aws v1.0.0*
