# IaC Checkov AWS — Kiro Power

Scan và bảo mật AWS Infrastructure as Code (Terraform, CloudFormation) bằng [Checkov](https://www.checkov.io/). Chạy trực tiếp trên máy local với plan, tracking, memory giữa sessions, và remediation tự động.

## Cài đặt

### 1. Cài Checkov

```bash
pip install checkov
# hoặc
brew install checkov
```

### 2. Cài Power vào Kiro

Mở Kiro → Powers panel → Install from repository:

```
https://github.com/TDFS-Dom/iac-checkov-aws-power
```

Hoặc clone về local:

```bash
git clone https://github.com/TDFS-Dom/iac-checkov-aws-power.git
```

Rồi cài từ local folder trong Kiro Powers panel.

## Sử dụng

### Bắt đầu scan

Mở chat trong Kiro và nói:

```
Scan Terraform infrastructure cho AWS security
```

Power sẽ:
1. Detect IaC files trong workspace
2. Tạo scan plan → hỏi bạn confirm
3. Chạy Checkov full scan (456 AWS checks)
4. Phân tích kết quả → hiển thị summary
5. Lưu tracking để nhớ giữa sessions

### Tiếp tục sau session trước

```
Tiếp tục — bước tiếp theo là gì?
```

### Fix finding cụ thể

```
Fix CKV_AWS_93 trong s3.tf
```

### Xem compliance report

```
Report compliance CIS AWS
```

### Tạo baseline

```
Tạo baseline cho infrastructure hiện tại
```

## Workflow

```
[1] PLAN → [2] SCAN → [3] ANALYZE → [4] TRACK → [5] REMEDIATE → [6] VERIFY → [7] REPORT
```

| Phase | Mô tả |
|-------|--------|
| Plan | Detect files, check prerequisites, tạo plan → user approve |
| Scan | Chạy `checkov` full scan local (tất cả 456 AWS checks) |
| Analyze | Parse JSON → severity breakdown → top findings |
| Track | Append vào tracking.md (lịch sử, delta) |
| Remediate | Fix finding → sửa file .tf trực tiếp |
| Verify | Re-scan targeted check → confirm PASS |
| Report | Map findings sang CIS/PCI-DSS/HIPAA/SOC2 |

## Output

Sau khi scan, power tạo:

```
{project}/
├── .checkov-reports/
│   ├── tracking.md              # Scan history + delta
│   ├── project-memory.md        # Decisions, suppressions
│   ├── results_json.json        # Latest results
│   ├── scan-log.txt             # Execution log
│   └── plans/
│       └── plan-001.md
└── .checkov.yaml                # Config (nếu chưa có)
```

## Coverage

- **456 unique AWS checks** (CKV_AWS_1 → CKV_AWS_392, CKV2_AWS_1 → CKV2_AWS_78)
- **Frameworks**: Terraform, CloudFormation, Serverless (SAM)
- **Compliance**: CIS AWS, PCI-DSS, HIPAA, SOC2, NIST 800-53, GDPR
- **Full list**: xem [`references/aws-checks-full-list.md`](references/aws-checks-full-list.md)

## Architecture

```
iac-checkov-aws-power/
├── POWER.md                     # Metadata + documentation (Kiro reads this)
├── README.md                    # Hướng dẫn sử dụng (bạn đang đọc)
├── references/
│   └── aws-checks-full-list.md  # 456 checks offline reference
└── steering/                    # Workflow guides (Kiro loads on-demand)
    ├── secops-contract.md       # Core rules, paths, behavior
    ├── secops-routing.md        # Intent → command dispatch
    ├── secops-token-budget.md   # Context window management
    ├── checkov-aws-scan.md      # Execution workflow
    └── checkov-aws-compliance.md # Compliance mapping tables
```

## Key Principles

- **Plan-First**: Không scan khi chưa có user approve
- **Full-Scan Default**: Quét tất cả 456 checks, phân loại sau
- **Append-Only Tracking**: History chỉ append, không overwrite
- **Session Continuity**: Nhớ context giữa sessions qua tracking + memory files
- **Auto-Verify**: Fix xong → tự re-scan check đó

## Yêu cầu

- [Kiro IDE](https://kiro.dev)
- Python ≥ 3.8
- Checkov (`pip install checkov`)
- Terraform hoặc CloudFormation files trong workspace

## License

MIT
