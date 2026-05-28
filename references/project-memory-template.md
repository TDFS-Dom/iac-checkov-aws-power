# Project Memory — {project_name}

> Auto-maintained by IaC Checkov AWS Power
> Last updated: {YYYY-MM-DD}

---

## Scan Configuration

| Key | Value | Set Date |
|-----|-------|----------|
| Target Directory | `.` (full workspace) | {date} |
| Framework | terraform | {date} |
| Skip Paths | `.terraform/`, `docs/`, `scripts/` | {date} |
| External Modules | download=true | {date} |

---

## Compliance Targets

| Framework | Status | Set Date |
|-----------|--------|----------|
| CIS AWS | ⬚ Not selected | |
| PCI-DSS | ⬚ Not selected | |
| HIPAA | ⬚ Not selected | |
| SOC2 | ⬚ Not selected | |

---

## Approved Suppressions

| Check ID | Resource | Justification | Approved By | Date |
|----------|----------|---------------|-------------|------|
| — | — | — | — | — |

---

## Known False Positives

| Check ID | Resource | Why False Positive | Permanent |
|----------|----------|--------------------|-----------|
| — | — | — | — |

---

## Fix Patterns (Recurring)

| Pattern | Check IDs | Fix Applied | Count |
|---------|-----------|-------------|-------|
| — | — | — | — |

---

## Environment Notes

| Env | Differences | Impact on Scan |
|-----|-------------|----------------|
| dev | No encryption required | Suppress CKV_AWS_16,17 |
| staging | Same as prod | Full scan |
| prod | Full compliance | No suppressions |

---

## Decisions Log

| # | Date | Decision | Reason | By |
|---|------|----------|--------|-----|
| 1 | {date} | {what was decided} | {why} | {who} |

---

## Session History (Last 5)

| # | Date | Action | Outcome |
|---|------|--------|---------|
| 1 | {date} | {scan/fix/report} | {result} |
