# Scan Plan — #{scan_number}

> Status: {⏳ Pending Approval / ✅ Approved / ❌ Rejected}
> Created: {YYYY-MM-DD HH:MM}

## Scope

| Attribute | Value |
|-----------|-------|
| Target | {directory} |
| Framework | {terraform/cloudformation} |
| Mode | FULL SCAN (all 456 AWS checks) |
| External Modules | {download: yes/no} |
| Baseline | {applied: yes/no} |
| Config | {.checkov.yaml: exists/will create/none} |

## Files Detected

| Type | Count | Directories |
|------|-------|-------------|
| .tf | {N} | {top dirs} |
| .yaml/.json (CFN) | {N} | {top dirs} |

## Skip Paths

- .terraform/
- {other configured skips}

## Estimated

| Metric | Value |
|--------|-------|
| Checks | 456 AWS (full) |
| Estimated Time | ~{N}s |
| Previous Scan | #{N} ({N} findings) |

## Approval

- [ ] User confirmed: proceed with scan
