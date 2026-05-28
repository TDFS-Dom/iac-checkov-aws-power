# Severity Classification Reference (Checkov OSS — No Prisma API Key)

> **Mục đích**: Chuẩn hoá severity classification khi Checkov OSS trả `severity = null/UNKNOWN`.
> Agent PHẢI dùng file này làm single source of truth — KHÔNG tự classify theo cảm tính.
> File này được reference từ: `remediation-plan.md`, `summary.md`, `tech-debt.md`.

---

## Nguồn tham chiếu

Bộ tiêu chí dưới đây được xây dựng dựa trên:
- [AWS Security Hub Severity Labels](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_Severity.html) — CRITICAL/HIGH/MEDIUM/LOW definitions
- [AWS Prescriptive Guidance — Vulnerability Management](https://docs.aws.amazon.com/prescriptive-guidance/latest/vulnerability-management/assess-and-prioritize-security-findings.html) — prioritization factors
- [Prisma Cloud Policy Severity](https://knowledgebase.paloaltonetworks.com/KCSArticleDetail?id=kA14u000000scJiCAI) — IaC-specific severity model
- [NIST CCSS (Common Configuration Scoring System)](https://csrc.nist.gov/publications/nistir/ir7502/nistir-7502_CCSS.pdf) — configuration vulnerability scoring

Content was rephrased for compliance with licensing restrictions.

---

## Nguyên tắc phân loại

Dựa trên AWS Security Hub severity model, classification đánh giá 2 yếu tố:

1. **Difficulty to exploit** — mức độ phức tạp để attacker lợi dụng misconfiguration
2. **Likelihood of compromise** — khả năng misconfiguration dẫn tới breach/disruption

| Severity | Định nghĩa (AWS Security Hub aligned) | SLA |
|----------|---------------------------------------|-----|
| **CRITICAL** | Issue phải được remediate **ngay lập tức** để tránh escalation. Attacker có thể exploit trực tiếp, không cần điều kiện phụ. Tương đương normalized score 90–100. | 24h — block deploy |
| **HIGH** | Issue phải được address **ưu tiên cao**. Resource có thể bị compromised và sử dụng cho mục đích unauthorized. Tương đương normalized score 70–89. | 1 sprint (2 weeks) |
| **MEDIUM** | Issue phải được address nhưng **không khẩn cấp**. Cần chain nhiều điều kiện hoặc sophistication cao hơn để exploit. Tương đương normalized score 40–69. | 1 quarter |
| **LOW** | Issue **không yêu cầu action riêng**. Là hardening recommendation, defense-in-depth layer. Tương đương normalized score 1–39. | Backlog |

---

## Bộ tiêu chí phân loại (Scoring Matrix)

### Ma trận 2 chiều: Exploitability × Impact

Agent classify bằng cách đánh giá finding trên 2 trục:

**Trục 1: Exploitability (Difficulty to Exploit)**

| Level | Mô tả | Ví dụ |
|-------|--------|-------|
| **TRIVIAL** | Không cần authentication, không cần network position đặc biệt. Public internet access đủ. | S3 public bucket, SG open 0.0.0.0/0 tới SSH |
| **LOW** | Cần 1 điều kiện đơn giản (có AWS credentials, hoặc access vào internal network) | IAM wildcard policy (cần credentials), unencrypted EBS (cần EC2 access) |
| **MODERATE** | Cần chain 2+ điều kiện hoặc cần privilege level nhất định | Missing DLQ (cần trigger failure), missing VPC flow logs (cần other exploit first) |
| **HIGH** | Cần advanced attack path, multiple layers, hoặc insider access | Missing CMK cho SSM parameter (default encryption vẫn có), missing detailed monitoring |

**Trục 2: Impact (nếu exploit thành công)**

| Level | Mô tả | Ví dụ |
|-------|--------|-------|
| **CATASTROPHIC** | Full account takeover, toàn bộ data exposed, total loss of control | AdministratorAccess policy, root MFA disabled |
| **SIGNIFICANT** | Data breach cho 1 service, credential theft, hoặc lateral movement | Unencrypted RDS, open SG tới DB port, IAM privilege escalation |
| **MODERATE** | Partial visibility loss, 1 resource compromised, operational disruption | Missing flow logs, missing access logging, deletion without protection |
| **MINIMAL** | No direct security impact. Operational improvement, compliance checkbox | Missing tags, missing CMK (default encryption exists), missing monitoring |

### Severity = f(Exploitability, Impact)

| | Impact: CATASTROPHIC | Impact: SIGNIFICANT | Impact: MODERATE | Impact: MINIMAL |
|---|---|---|---|---|
| **Exploit: TRIVIAL** | 🔴 CRITICAL | 🔴 CRITICAL | 🟠 HIGH | 🟡 MEDIUM |
| **Exploit: LOW** | 🔴 CRITICAL | 🟠 HIGH | 🟠 HIGH | 🟡 MEDIUM |
| **Exploit: MODERATE** | 🟠 HIGH | 🟠 HIGH | 🟡 MEDIUM | 🟢 LOW |
| **Exploit: HIGH** | 🟠 HIGH | 🟡 MEDIUM | 🟢 LOW | 🟢 LOW |

**Cách dùng**: Cho mỗi finding, agent xác định Exploitability level + Impact level → tra ma trận → ra Severity.

---

## Pre-computed Mappings

**→ Xem `references/aws-checks-full-list.md`** — file này chứa severity cho TẤT CẢ 456 checks (cột Severity).

Agent tra severity bằng cách lookup Check ID trong `aws-checks-full-list.md`. KHÔNG cần bảng riêng ở đây.

### Justified Deviations từ AWS Security Hub

Một số checks có severity khác với Security Hub FSBP. Lý do:

| Check ID | Chúng ta | SH Sev | Lý do deviation |
|----------|----------|--------|-----------------|
| CKV_AWS_54, CKV_AWS_56 | CRITICAL | MEDIUM | SH check ở account-level (S3.1). IaC context = bucket-level → disable = exposed trực tiếp |
| CKV_AWS_111/109/356/63/40 | HIGH | CRITICAL | SH maps tới IAM.1 (full admin). Checkov fires trên broader wildcard patterns (not always full admin) → cần credentials + not full takeover |
| CKV_AWS_19/7/16 | HIGH | MEDIUM | SH = MEDIUM cho encryption at rest. IaC = data protection gap cho sensitive stores |
| CKV_AWS_24/25 | CRITICAL | HIGH | SH = HIGH (EC2.19). IaC = direct internet brute-force without any barrier |

---

## CRITICAL — Tiêu chí (P0)

Finding là CRITICAL khi thoả **BẤT KỲ** điều kiện sau:

| # | Tiêu chí | Ví dụ Check IDs |
|---|----------|-----------------|
| 1 | IAM policy cho phép **full admin access** (`*:*` hoặc AdministratorAccess managed policy) | CKV_AWS_274, CKV_AWS_62 |
| 2 | S3 bucket **public access không bị block** (Block Public Access = false) | CKV_AWS_93, CKV_AWS_54, CKV_AWS_56 |
| 3 | Security Group cho phép **0.0.0.0/0 ingress tới port sensitive** (22/SSH, 3389/RDP, DB ports 3306/5432/1433/27017) | CKV_AWS_24, CKV_AWS_25 |
| 4 | Credentials/secrets **hardcoded** trong code | CKV_AWS_41, CKV_AWS_46 |
| 5 | RDS/Database **publicly accessible = true** | CKV_AWS_17 |
| 6 | IAM **root user has access keys** | CKV_AWS_348 |

**Keyword pattern**: Nếu check description chứa "public access", "admin", "AdministratorAccess", "hardcoded credentials", "publicly accessible" → likely CRITICAL.

---

## HIGH — Tiêu chí (P1)

Finding là HIGH khi thoả **BẤT KỲ** điều kiện sau:

| # | Tiêu chí | Ví dụ Check IDs |
|---|----------|-----------------|
| 1 | IAM policy dùng **wildcard actions** (`kms:*`, `s3:*`, `ec2:*`) hoặc **wildcard resource** (`"Resource": "*"`) nhưng KHÔNG phải full admin | CKV_AWS_111, CKV_AWS_109, CKV_AWS_356, CKV_AWS_63, CKV_AWS_40, CKV_AWS_288, CKV_AWS_289, CKV_AWS_290 |
| 2 | **Encryption at rest bị tắt** cho data stores (S3, EBS, RDS, DynamoDB, EFS, ElastiCache, Redshift) | CKV_AWS_19, CKV_AWS_7, CKV_AWS_16, CKV_AWS_35, CKV_AWS_36, CKV_AWS_64, CKV_AWS_29 |
| 3 | **Encryption in transit bị tắt** (SSL/TLS not enforced) | CKV_AWS_20, CKV_AWS_2 (khi resource là ALB/NLB, KHÔNG phải GWLB) |
| 4 | **VPC Flow Logs không enabled** — mất visibility vào network traffic | CKV2_AWS_11 |
| 5 | **Default Security Group không restrict** — cho phép traffic qua default SG | CKV2_AWS_12 |
| 6 | Security Group cho phép **0.0.0.0/0 ingress tới port 80/443** (web traffic — risky nếu không có WAF) | CKV_AWS_260 |
| 7 | Security Group cho phép **0.0.0.0/0 egress tới all ports** | CKV_AWS_382 |
| 8 | **CloudTrail không enabled** hoặc không encrypt logs | CKV_AWS_49, CKV_AWS_35 |
| 9 | **EC2 IMDSv1 enabled** (SSRF → credential theft) | CKV_AWS_79 |
| 10 | **Lambda environment variables không encrypted** với CMK | CKV_AWS_173 |
| 11 | **KMS key rotation không enabled** | CKV2_AWS_64 |
| 12 | **S3 bucket không có access logging** — mất audit trail | CKV_AWS_18 |
| 13 | IAM role cho phép **cross-account assume** không giới hạn | CKV_AWS_61, CKV_AWS_60 |

**Keyword pattern**: "encryption", "wildcard", "flow log", "SSL", "IMDSv2", "logging", "rotation", "0.0.0.0/0" → likely HIGH.

---

## MEDIUM — Tiêu chí (P2)

Finding là MEDIUM khi thoả **BẤT KỲ** điều kiện sau:

| # | Tiêu chí | Ví dụ Check IDs |
|---|----------|-----------------|
| 1 | **Deletion protection tắt** cho stateful resources (RDS, ALB, DynamoDB, EFS) | CKV_AWS_150, CKV_AWS_104, CKV_AWS_165 |
| 2 | **Backup/versioning không enabled** cho data stores | CKV_AWS_21 (S3 versioning), CKV_AWS_133 (RDS backup retention) |
| 3 | **Cross-region replication không enabled** cho critical buckets | CKV_AWS_144 |
| 4 | **Lambda missing operational best practices**: DLQ, X-Ray tracing, code signing, reserved concurrency | CKV_AWS_116, CKV_AWS_50, CKV_AWS_272, CKV_AWS_115 |
| 5 | **Lambda không trong VPC** (khi function access private resources) | CKV_AWS_117 |
| 6 | **CloudWatch log retention < 1 year** | CKV_AWS_338 |
| 7 | **S3 lifecycle/event notifications** không configured | CKV_AWS_300, CKV2_AWS_62, CKV2_AWS_61 |
| 8 | **Load Balancer** missing access logs, drop invalid headers | CKV_AWS_91, CKV_AWS_131 |
| 9 | **Security Groups không attached** (unused resources) | CKV2_AWS_5 |
| 10 | **Transit Gateway auto-accept** shared attachments enabled | CKV_AWS_331 |
| 11 | **EC2 detailed monitoring** không enabled | CKV_AWS_126 |
| 12 | **EC2 EBS optimized** không enabled | CKV_AWS_135 |
| 13 | **EIP không attached** tới instance (wasted resource) | CKV2_AWS_19 |

**Keyword pattern**: "deletion protection", "backup", "versioning", "replication", "DLQ", "tracing", "lifecycle", "retention", "monitoring" → likely MEDIUM.

---

## LOW — Tiêu chí (P3)

Finding là LOW khi thoả **BẤT KỲ** điều kiện sau:

| # | Tiêu chí | Ví dụ Check IDs |
|---|----------|-----------------|
| 1 | **SSM Parameter** không encrypted với CMK (default encryption vẫn có) | CKV2_AWS_34 |
| 2 | **CloudWatch Log Group** không encrypted với CMK (default encryption vẫn có) | CKV_AWS_158 |
| 3 | **Tagging** không đầy đủ | CKV_AWS_153 |
| 4 | **Description** field trống trong Security Group | CKV_AWS_23 (description variant) |
| 5 | Resource naming conventions | — |
| 6 | **Deprecated/old generation** resource types | — |

**Keyword pattern**: "CMK" (khi đã có default encryption), "tag", "description", "naming" → likely LOW.

---

## Fallback Rules (khi Check ID KHÔNG có trong bảng trên)

Nếu một finding không match bất kỳ tiêu chí cụ thể nào ở trên, classify theo **resource type + action type**:

### Theo Resource Type

| Resource Type | Default Severity | Rationale |
|---------------|-----------------|-----------|
| `aws_iam_*` (policy, role, user, group) | HIGH | IAM = blast radius lớn |
| `aws_security_group*` | HIGH | Network exposure |
| `aws_vpc*`, `aws_subnet*` | HIGH | Network foundation |
| `aws_s3_bucket*` (encryption/access related) | HIGH | Data protection |
| `aws_s3_bucket*` (config/lifecycle) | MEDIUM | Operational |
| `aws_rds_*`, `aws_db_*` | HIGH | Data store |
| `aws_lambda_*` | MEDIUM | Compute — isolation |
| `aws_lb*`, `aws_alb*` | MEDIUM | Infrastructure |
| `aws_ec2*`, `aws_instance*` | MEDIUM | Compute |
| `aws_cloudwatch*` | MEDIUM | Observability |
| `aws_ssm*`, `aws_secretsmanager*` | MEDIUM | Secrets management |
| `aws_kms*` | HIGH | Encryption backbone |
| `aws_cloudtrail*` | HIGH | Audit trail |
| `aws_guardduty*`, `aws_securityhub*` | HIGH | Detection |
| Other | MEDIUM | Default |

### Theo Check Name Patterns

| Pattern trong check_name | → Severity |
|--------------------------|-----------|
| "public" + ("access" \| "facing" \| "exposed") | CRITICAL |
| "admin" + "privilege" | CRITICAL |
| "encrypt" + ("rest" \| "transit" \| "storage") | HIGH |
| "wildcard" \| `"*"` + "action" | HIGH |
| "logging" \| "log" + "enable" | HIGH |
| "flow log" | HIGH |
| "backup" \| "retention" \| "versioning" | MEDIUM |
| "deletion protection" | MEDIUM |
| "monitoring" \| "tracing" | MEDIUM |
| "tag" \| "description" | LOW |

---

## Decision Tree (cho agent khi classify)

```
1. Check ID có trong `references/aws-checks-full-list.md`? → dùng severity từ cột Severity (456 checks)
2. Check ID mới (chưa có trong list)? → dùng Scoring Matrix (Exploitability × Impact) ở trên
3. Vẫn không xác định được? → check_name keyword pattern match (xem bảng bên dưới)
4. Vẫn không match? → resource type fallback table
5. Vẫn không match? → MEDIUM (default)
```

**KHÔNG BAO GIỜ để finding ở UNKNOWN** — mọi finding PHẢI được classify vào 1 trong 4 levels.

> `aws-checks-full-list.md` là lookup table hoàn chỉnh. Scoring Matrix + Fallback rules chỉ dùng khi Checkov release checks MỚI chưa có trong list.

---

## Exceptions / Overrides

| Condition | Override |
|-----------|---------|
| GWLB listener + CKV_AWS_2 (HTTPS check) | → **SKIP** (false positive — GWLB uses GENEVE) |
| Module-defined SG + CKV2_AWS_5 | → **MEDIUM** (không phải HIGH vì là structural pattern) |
| Lambda monitoring/notification + CKV_AWS_117 | → **MEDIUM** (không cần VPC cho AWS API calls) |
| Dev/test environment resources (tagged or path-based) | → Downgrade 1 level (HIGH→MEDIUM, MEDIUM→LOW) |

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 2.0 | 2026-05-28 | Add scoring matrix (Exploitability × Impact), align with AWS Security Hub + Prisma Cloud + NIST CCSS, add source references |
| 1.0 | 2026-05-28 | Initial classification with 4 severity levels, 50+ check mappings |

