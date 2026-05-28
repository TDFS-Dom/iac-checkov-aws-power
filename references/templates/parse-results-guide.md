# Parse Results Guide — Cách fill templates từ results.json

> Agent PHẢI follow hướng dẫn này để fill templates. KHÔNG đoán, KHÔNG bỏ trống.

## Cấu trúc results.json (Checkov output)

```json
{
  "check_type": "terraform",
  "results": {
    "passed_checks": [...],
    "failed_checks": [
      {
        "check_id": "CKV_AWS_93",
        "check_result": { "result": "FAILED" },
        "resource": "aws_s3_bucket.data",
        "file_path": "/level0-foundation/s3.tf",
        "file_line_range": [15, 25],
        "severity": "CRITICAL",
        "check_name": "Ensure S3 bucket policy does not lockout all but root user"
      }
    ],
    "skipped_checks": [...]
  },
  "summary": {
    "passed": 45,
    "failed": 12,
    "skipped": 3,
    "parsing_errors": 0
  }
}
```

## Field Mapping — từ JSON → Template columns

| Template Column | JSON Path | Example |
|-----------------|-----------|---------|
| Check ID | `failed_checks[].check_id` | CKV_AWS_93 |
| Severity | `failed_checks[].severity` | CRITICAL |
| Resource | `failed_checks[].resource` | `aws_s3_bucket.data` |
| File | `failed_checks[].file_path` | `/level0-foundation/s3.tf` |
| Line | `failed_checks[].file_line_range[0]` | 15 |
| Description | `failed_checks[].check_name` | Ensure S3 bucket policy... |
| Passed count | `summary.passed` | 45 |
| Failed count | `summary.failed` | 12 |
| Skipped count | `summary.skipped` | 3 |

## Cách fill summary.md

```python
import json

with open('results.json') as f:
    data = json.load(f)

summary = data['summary']
failed = data['results']['failed_checks']

# Count by severity
sev_count = {}
for f in failed:
    s = f.get('severity', 'UNKNOWN')
    sev_count[s] = sev_count.get(s, 0) + 1

# Count by folder
folder_count = {}
for f in failed:
    folder = f['file_path'].split('/')[1] if '/' in f['file_path'] else '.'
    folder_count[folder] = folder_count.get(folder, 0) + 1

# Top findings (sorted by severity)
severity_order = {'CRITICAL': 0, 'HIGH': 1, 'MEDIUM': 2, 'LOW': 3}
top = sorted(failed, key=lambda x: severity_order.get(x.get('severity', ''), 4))[:10]
```

## Cách fill remediation-plan.md

```python
# Group by priority — using CLASSIFICATION RULES (not raw severity)
# Because Checkov OSS often returns severity=null or UNKNOWN

failed = data.get('results', {}).get('failed_checks', [])

# Step 1: Try to use Checkov severity
# Step 2: If severity is null/UNKNOWN, classify by check type
IAM_ADMIN_CHECKS = {'CKV_AWS_274', 'CKV_AWS_40'}
IAM_WILDCARD_CHECKS = {'CKV_AWS_111', 'CKV_AWS_109', 'CKV_AWS_356'}
NETWORK_EXPOSURE_CHECKS = {'CKV_AWS_260', 'CKV_AWS_382', 'CKV_AWS_23', 'CKV_AWS_24'}
NETWORK_VISIBILITY_CHECKS = {'CKV2_AWS_11', 'CKV2_AWS_12'}
ENCRYPTION_CHECKS = {'CKV_AWS_19', 'CKV_AWS_7', 'CKV_AWS_16', 'CKV_AWS_61'}

def classify_priority(finding):
    sev = finding.get('severity')
    check_id = finding.get('check_id', '')
    
    # Use Checkov severity if available and not UNKNOWN
    if sev and sev != 'UNKNOWN':
        return {'CRITICAL': 'P0', 'HIGH': 'P1', 'MEDIUM': 'P2', 'LOW': 'P3'}[sev]
    
    # Classify by check type
    if check_id in IAM_ADMIN_CHECKS:
        return 'P0'
    if check_id in IAM_WILDCARD_CHECKS:
        return 'P1'
    if check_id in NETWORK_EXPOSURE_CHECKS or check_id in NETWORK_VISIBILITY_CHECKS:
        return 'P1'
    if check_id in ENCRYPTION_CHECKS:
        return 'P1'
    if 'S3' in finding.get('check_name', '') or 'SSM' in check_id or 'KMS' in check_id:
        return 'P2'
    return 'P3'

p0 = [f for f in failed if classify_priority(f) == 'P0']
p1 = [f for f in failed if classify_priority(f) == 'P1']
p2 = [f for f in failed if classify_priority(f) == 'P2']
p3 = [f for f in failed if classify_priority(f) == 'P3']

# Fill Priority Matrix counts
# P0 count = len(p0), P1 count = len(p1), etc.

# Group findings by subcategory within each priority
# Subcategories: IAM, Network, Storage, Compute, Logging, Other

# CRITICAL: For each group, ALWAYS extract per-resource detail:
for check_id, group in grouped_by_check_id.items():
    # Header row: Check ID | Count | Description
    # Then list EVERY resource:
    for finding in group:
        # resource = finding['resource']
        # file = finding['file_path']
        # line = finding['file_line_range'][0]
        # caller = finding.get('caller_file_path', None)  # for module instances
        pass

# NEVER just write "8 findings" without listing WHERE they are
# Each finding has unique resource + file + line — MUST be shown
```

## Cách fill delta.md

```python
# Load previous and current
with open(f'scans/{prev}/results.json') as f:
    prev_data = json.load(f)
with open(f'scans/{curr}/results.json') as f:
    curr_data = json.load(f)

prev_ids = {(f['check_id'], f['resource']) for f in prev_data['results']['failed_checks']}
curr_ids = {(f['check_id'], f['resource']) for f in curr_data['results']['failed_checks']}

new_findings = curr_ids - prev_ids      # In current but not previous
resolved = prev_ids - curr_ids          # In previous but not current
unchanged = curr_ids & prev_ids         # In both
```

## Cách fill tech-debt.md

```python
# Tech debt = P2 + P3 findings (from priority classification above)
# Level 1: auto-generate compact format (no user input needed)

tech_debt_candidates = [f for f in failed if classify_priority(f) in ('P2', 'P3')]

# Separate into categories:
# 1. "Accepted Debt" — findings with clear justification pattern:
#    - False positives (GWLB HTTPS check on GENEVE, SG module unattached by design)
#    - Non-production (scripts/, test/)
#    - Managed appliance (Palo Alto, vendor-managed)
#    - Architecture pattern (module creates for attachment elsewhere)
#
# 2. "Needs Review" — findings that SHOULD be fixed but need decision:
#    - Low-effort fixes that aren't blocked
#    - Compliance-relevant (logging, retention)
#
# 3. "Suppression Candidates" — clear false positives for .checkov.baseline

# Justification generation (context-specific, NEVER generic):
def suggest_justification(finding):
    check_id = finding['check_id']
    resource = finding['resource']
    file_path = finding['file_path']
    
    # Pattern: GWLB/NLB non-HTTPS listener
    if check_id == 'CKV_AWS_2' and 'gwlb' in file_path.lower():
        return "GWLB uses GENEVE protocol, not HTTPS — false positive for this LB type"
    
    # Pattern: SG module creates unattached SGs
    if check_id == 'CKV2_AWS_5' and 'modules/sg' in file_path:
        return "SG module creates SGs for attachment elsewhere — expected pattern"
    
    # Pattern: Script/test infrastructure
    if 'scripts/' in file_path or 'test/' in file_path:
        return "Non-production infrastructure — script/test environment"
    
    # Pattern: Vendor-managed appliance
    if 'pan-firewall' in file_path or 'palo' in file_path.lower():
        return "Managed appliance (Palo Alto) — vendor-controlled config"
    
    # Default: needs review
    return None  # → goes to "Needs Review" section

# Level 2 enrichment (when user requests):
# - Add Risk Assessment per item
# - Add Acceptance Criteria (trigger conditions)
# - Add Compensating Controls
# - Add Target Fix Date + Review Date
# - Convert to detailed TD-NNN blocks
```

## QUAN TRỌNG — Agent Rules

1. **PHẢI chạy parse logic** trên results.json — KHÔNG hardcode values
2. **Remediation plan PHẢI liệt kê TẤT CẢ findings** — không chỉ top 3
3. **Nếu >5 findings cùng Check ID** → group header + list ALL affected resources with file:line (KHÔNG truncate, KHÔNG "... và N items khác")
4. **File path phải giữ nguyên** từ JSON (relative path) — KHÔNG modify
5. **Line = first element** của `file_line_range` array
6. **Severity mapping**: CRITICAL→P0, HIGH→P1, MEDIUM→P2, LOW→P3
7. **Agent KHÔNG ĐƯỢC** tạo file trống rồi nói "sẽ fill sau" — fill NGAY từ data
