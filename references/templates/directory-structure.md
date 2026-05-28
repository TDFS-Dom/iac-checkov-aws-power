# Output Directory Structure Template

> Agent PHẢI tạo đúng cấu trúc này khi chạy. Không tự ý thêm/bớt folders.

## Khi lần đầu scan (init)

```bash
mkdir -p .checkov-reports/state
mkdir -p .checkov-reports/scans/001
mkdir -p .checkov-reports/reports/compliance
```

Tạo files:
```
.checkov-reports/
├── state/
│   ├── tracking.md            ← from templates/tracking.md
│   └── project-memory.md     ← from references/project-memory-template.md
└── scans/
    ├── 001/
    │   ├── plan.md            ← scan plan đã approve
    │   ├── metadata.md        ← from templates/metadata.md
    │   ├── results.json       ← checkov output (raw, không sửa)
    │   └── summary.md         ← from templates/summary.md
    └── latest.txt             ← nội dung: "001"
```

## Khi scan lần 2+ (increment)

```bash
LATEST=$(cat .checkov-reports/scans/latest.txt)
NEXT=$(printf "%03d" $((10#$LATEST + 1)))
mkdir -p .checkov-reports/scans/$NEXT
```

Tạo files:
```
.checkov-reports/
└── scans/
    ├── {NEXT}/
    │   ├── plan.md
    │   ├── metadata.md
    │   ├── results.json
    │   ├── summary.md
    │   └── delta.md           ← from templates/delta.md (so sánh vs previous)
    └── latest.txt             ← update nội dung: "{NEXT}"
```

Update:
- `state/tracking.md` → APPEND row mới vào Timeline table

## Khi user yêu cầu report

```bash
mkdir -p .checkov-reports/reports/compliance
```

```
.checkov-reports/
└── reports/
    ├── remediation-plan.md    ← from references/remediation-plan-template.md
    ├── tech-debt.md           ← from references/tech-debt-template.md
    └── compliance/
        ├── cis-aws.md         ← generated
        └── pci-dss.md         ← generated
```

## Full structure (sau nhiều scans + reports)

```
.checkov-reports/
├── state/                              # PERSISTENT — đọc mỗi session
│   ├── tracking.md                    # Timeline + remediation progress
│   └── project-memory.md             # Decisions + config + suppressions
│
├── scans/                              # VERSIONED — immutable sau khi tạo
│   ├── 001/
│   │   ├── plan.md
│   │   ├── metadata.md
│   │   ├── results.json
│   │   └── summary.md
│   ├── 002/
│   │   ├── plan.md
│   │   ├── metadata.md
│   │   ├── results.json
│   │   ├── summary.md
│   │   └── delta.md
│   ├── 003/
│   │   ├── plan.md
│   │   ├── metadata.md
│   │   ├── results.json
│   │   ├── summary.md
│   │   └── delta.md
│   └── latest.txt                     # "003"
│
└── reports/                            # ON-DEMAND — chỉ khi user yêu cầu
    ├── remediation-plan.md
    ├── tech-debt.md
    └── compliance/
        ├── cis-aws.md
        └── pci-dss.md
```

## Rules

| Rule | Description |
|------|-------------|
| Scan folder = immutable | SAU khi tạo, KHÔNG sửa files trong `scans/{NNN}/` |
| State = append-only | `tracking.md` chỉ append, KHÔNG overwrite entries cũ |
| Memory = update in-place | `project-memory.md` có thể update sections |
| Reports = overwrite ok | Reports được regenerate khi user yêu cầu lại |
| latest.txt = overwrite | Luôn chứa số scan mới nhất |
| Folder naming = 3 digits | 001, 002, ..., 999 (zero-padded) |
| No nesting deeper | Không tạo subfolder trong `scans/{NNN}/` |
| No date in folder name | Dùng scan number, date nằm trong metadata.md |

## Checkov Output Mapping

Khi chạy `checkov -o json -o cli --output-file-path .checkov-reports/scans/{NNN}`:

Checkov tạo:
- `results_json.json` → rename thành `results.json`
- `results_cli.txt` → có thể xóa (summary.md thay thế)

Agent PHẢI rename sau khi scan:
```bash
mv .checkov-reports/scans/$NEXT/results_json.json .checkov-reports/scans/$NEXT/results.json 2>/dev/null
rm -f .checkov-reports/scans/$NEXT/results_cli.txt 2>/dev/null
```
