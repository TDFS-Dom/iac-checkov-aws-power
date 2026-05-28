# Severity Classification Reference (Checkov OSS — No Prisma API Key)

> **Mục đích**: Chuẩn hoá severity classification khi Checkov OSS trả `severity = null/UNKNOWN`.
> Agent PHẢI dùng file này làm single source of truth — KHÔNG tự classify theo cảm tính.
> File này được reference từ: `remediation-plan.md`, `summary.md`, `tech-debt.md`.

---

## Nguyên tắc phân loại

Classification dựa trên **IMPACT nếu bị exploit**, không phải effort-to-fix.

| Severity | Định nghĩa | SLA |
|----------|------------|-----|
| **CRITICAL** | Exposure trực tiếp ra internet HOẶC privilege escalation không giới hạn. Attacker có thể exploit NGAY mà không cần thêm điều kiện. | 24h — block deploy |
| **HIGH** | Over-permissive access, thiếu encryption cho sensitive data, hoặc thiếu visibility (logging/monitoring) cho critical resources. Cần thêm 1 điều kiện để exploit. | 1 sprint (2 weeks) |
| **MEDIUM** | Best practices bị thiếu — defense-in-depth layers, operational hygiene. Cần chain nhiều điều kiện để gây impact. | 1 quarter |
| **LOW** | Nice-to-have hardening. Impact thấp hoặc chỉ ảnh hưởng non-sensitive resources. | Backlog |

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
| 6 | Root account không có MFA | CKV_AWS_9 |

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
| 2 | **Backup/versioning không enabled** cho data stores | CKV_AWS_21 (S3 versioning), CKV_AWS_17 (RDS backup) |
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
| 13 | **S3 event notifications** không configured | CKV2_AWS_62 |
| 14 | **EIP không attached** tới instance (wasted resource) | CKV2_AWS_19 |

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
1. Check ID có trong bảng CRITICAL? → CRITICAL
2. Check ID có trong bảng HIGH? → HIGH
3. Check ID có trong bảng MEDIUM? → MEDIUM
4. Check ID có trong bảng LOW? → LOW
5. Không match → check_name keyword pattern match? → dùng severity tương ứng
6. Vẫn không match → resource type fallback table
7. Vẫn không match → MEDIUM (default)
```

**KHÔNG BAO GIỜ để finding ở UNKNOWN** — mọi finding PHẢI được classify vào 1 trong 4 levels.

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
| 1.0 | 2026-05-28 | Initial classification with 4 severity levels, 50+ check mappings |

