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

---

## P0 — CRITICAL (Fix Immediately)

| # | Check ID | Finding | Resource | File | Line | Owner | ETA | Status |
|---|----------|---------|----------|------|------|-------|-----|--------|
| 1 | CKV_AWS_{N} | {description} | `aws_{type}.{name}` | `{path/to/file.tf}` | {N} | {person} | {date} | ⬚ Open |

**Definition of Done**: Re-scan PASS + PR merged + no regression

---

## P1 — HIGH (This Sprint)

| # | Check ID | Finding | Resource | File | Line | Owner | Sprint | Status |
|---|----------|---------|----------|------|------|-------|--------|--------|
| 1 | CKV_AWS_{N} | {description} | `aws_{type}.{name}` | `{path/to/file.tf}` | {N} | {person} | S{N} | ⬚ Open |

---

## P2 — MEDIUM (This Quarter)

| # | Check ID | Finding | Resource | File | Line | Target Date | Status |
|---|----------|---------|----------|------|------|-------------|--------|
| 1 | CKV_AWS_{N} | {description} | `aws_{type}.{name}` | `{path/to/file.tf}` | {N} | {YYYY-MM} | ⬚ Planned |

---

## P3 — LOW (Backlog / Accept)

| # | Check ID | Finding | Resource | File | Line | Decision |
|---|----------|---------|----------|------|------|----------|
| 1 | CKV_AWS_{N} | {description} | `aws_{type}.{name}` | `{path/to/file.tf}` | {N} | ⬚ Backlog / ⬚ Suppress |

---

## Execution Timeline

```
Week 1          Week 2          Week 3-4        Quarter
─────────────────────────────────────────────────────────
[P0 CRITICAL]   [P1 HIGH]       [P1 cont.]      [P2 MEDIUM]
Fix + verify    Fix + verify    Baseline lock   Scheduled fix
                                Create .baseline
```

## Effort Estimation

| Priority | Items | Avg Fix Time | Total Effort |
|----------|-------|--------------|--------------|
| P0 | {N} | ~30 min/item | {N}h |
| P1 | {N} | ~1h/item | {N}h |
| P2 | {N} | ~2h/item | {N}h |
| P3 | {N} | N/A (suppress) | 0h |
| **Total** | **{N}** | | **{N}h** |

---

## Dependencies & Blockers

| # | Finding | Blocker | Needed From | Status |
|---|---------|---------|-------------|--------|
| 1 | {check} | {what blocks fix} | {team/person} | ⬚ Waiting |

---

## Success Criteria

- [ ] 0 CRITICAL findings
- [ ] 0 HIGH findings (or approved exception)
- [ ] Baseline created for remaining MEDIUM/LOW
- [ ] `.checkov.yaml` committed with agreed skip-checks
- [ ] CI/CD gate: `--hard-fail-on CRITICAL,HIGH`
- [ ] Next scan shows delta ≤ 0 (no regression)

---

## Sign-off

| Role | Name | Date | Approval |
|------|------|------|----------|
| DevOps Lead | | | ⬚ |
| Security Team | | | ⬚ |
| Project Owner | | | ⬚ |

---

*Template version: 1.0 | Power: iac-checkov-aws*
