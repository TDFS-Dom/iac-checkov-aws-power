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
# Group by priority
p0 = [f for f in failed if f.get('severity') == 'CRITICAL']
p1 = [f for f in failed if f.get('severity') == 'HIGH']
p2 = [f for f in failed if f.get('severity') == 'MEDIUM']
p3 = [f for f in failed if f.get('severity') == 'LOW']

# Fill Priority Matrix counts
# P0 count = len(p0), P1 count = len(p1), etc.

# Fill each table row:
for i, finding in enumerate(p0):
    # Check ID = finding['check_id']
    # Finding = finding['check_name']
    # Resource = finding['resource']
    # File = finding['file_path']
    # Line = finding['file_line_range'][0]
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
# Tech debt = MEDIUM + LOW findings (accepted, not fixed immediately)
# HIGH findings CHỈ vào tech-debt khi user explicitly approve
tech_debt_items = [f for f in failed if f.get('severity') in ('MEDIUM', 'LOW')]

# Each item becomes TD-NNN entry with:
# - Check ID, Severity, Resource, File, Line from JSON
# - Environment = agent asks user OR infer from file path (e.g., /dev/ → dev)
# - Risk Assessment:
#   - Impact = based on severity (MEDIUM→MEDIUM, LOW→LOW)
#   - Likelihood = based on resource exposure (public-facing→HIGH, internal→LOW)
#   - Blast radius = based on resource type (IAM→wide, single bucket→narrow)
#   - Data sensitivity = infer from resource name/type or ask user
# - Business Justification = agent asks user OR suggest based on context
#   KHÔNG ĐƯỢC viết generic "Low priority" — phải context-specific
# - Compensating Controls = agent suggests based on check type:
#   - Missing encryption → "Data not sensitive" or "Network isolation"
#   - Missing logging → "CloudTrail enabled at account level"
#   - Missing versioning → "Lifecycle policy, data is ephemeral"
#   - Open SG (MEDIUM) → "WAF/NLB in front, monitoring alert"
# - Acceptance Criteria = trigger condition khi nào PHẢI fix:
#   - "If resource stores PII → fix immediately"
#   - "If environment promoted to prod → fix before promotion"
#   - "If public access detected → fix within 4h"
# - Target Fix Date = end of next quarter
# - Review Date = accepted date + 90 days
```

## QUAN TRỌNG — Agent Rules

1. **PHẢI chạy parse logic** trên results.json — KHÔNG hardcode values
2. **Remediation plan PHẢI liệt kê TẤT CẢ findings** — không chỉ top 3
3. **Nếu >20 findings cùng severity** → group bằng "... và {N} items khác" ở cuối table
4. **File path phải giữ nguyên** từ JSON (relative path) — KHÔNG modify
5. **Line = first element** của `file_line_range` array
6. **Severity mapping**: CRITICAL→P0, HIGH→P1, MEDIUM→P2, LOW→P3
7. **Agent KHÔNG ĐƯỢC** tạo file trống rồi nói "sẽ fill sau" — fill NGAY từ data
