# Checkov AWS Compliance Mapping

Detailed mapping of Checkov checks to compliance frameworks for AWS infrastructure.

---

## CIS AWS Foundations Benchmark v1.4

### Section 2: Storage

| Check ID | CIS Control | Description | Severity | Remediation |
|----------|-------------|-------------|----------|-------------|
| CKV_AWS_19 | 2.1.1 | S3 bucket encryption at rest | HIGH | Add `server_side_encryption_configuration` |
| CKV_AWS_21 | 2.1.3 | S3 bucket versioning | MEDIUM | Set `versioning { enabled = true }` |
| CKV_AWS_18 | 2.1.5 | S3 bucket access logging | MEDIUM | Add `logging` block with target bucket |
| CKV_AWS_93 | 2.1.1 | S3 public access blocked | CRITICAL | Add `aws_s3_bucket_public_access_block` |
| CKV_AWS_7 | 2.9 | EBS encryption by default | HIGH | Set `encrypted = true` |

### Section 4: Networking

| Check ID | CIS Control | Description | Severity | Remediation |
|----------|-------------|-------------|----------|-------------|
| CKV_AWS_23 | 4.1 | SG ingress not open to 0.0.0.0/0 | HIGH | Restrict `cidr_blocks` |
| CKV_AWS_24 | 4.2 | SG ingress not open to ::/0 | HIGH | Restrict `ipv6_cidr_blocks` |

### Section 1: Identity & Access

| Check ID | CIS Control | Description | Severity | Remediation |
|----------|-------------|-------------|----------|-------------|
| CKV_AWS_40 | 1.16 | IAM no wildcard actions | HIGH | Use specific actions in policy |
| CKV_AWS_49 | 1.1 | CloudTrail enabled | HIGH | Add `aws_cloudtrail` resource |

### Section 2: Database

| Check ID | CIS Control | Description | Severity | Remediation |
|----------|-------------|-------------|----------|-------------|
| CKV_AWS_16 | 2.3.1 | RDS storage encrypted | HIGH | Set `storage_encrypted = true` |
| CKV_AWS_17 | 2.3.2 | RDS backup retention | MEDIUM | Set `backup_retention_period >= 7` |
| CKV_AWS_61 | 2.3.1 | RDS encryption at rest | HIGH | Set `storage_encrypted = true` |

### Run CIS Scan

```bash
checkov -d ./terraform --check CIS_AWS
checkov -d ./terraform --check CIS_AWS -o json --output-file-path ./cis-report
```

---

## PCI-DSS v3.2.1

### Requirement 2: No Vendor-Supplied Defaults

| Check ID | PCI Req | Description | Remediation |
|----------|---------|-------------|-------------|
| CKV_AWS_41 | 2.1 | EKS encryption enabled | Set `encryption_config` in EKS cluster |
| CKV_AWS_58 | 2.2 | EKS public access restricted | Set `endpoint_public_access = false` |

### Requirement 3: Protect Stored Data

| Check ID | PCI Req | Description | Remediation |
|----------|---------|-------------|-------------|
| CKV_AWS_19 | 3.4 | S3 bucket encrypted | Add SSE configuration |
| CKV_AWS_61 | 3.4 | RDS encrypted at rest | `storage_encrypted = true` |
| CKV_AWS_7 | 3.4 | EBS encryption | `encrypted = true` |
| CKV_AWS_89 | 3.4 | DynamoDB encryption | Set `server_side_encryption` |

### Requirement 6: Secure Systems

| Check ID | PCI Req | Description | Remediation |
|----------|---------|-------------|-------------|
| CKV_AWS_23 | 6.2 | Security groups not open | Restrict CIDR blocks |
| CKV_AWS_40 | 6.5 | IAM no wildcard | Least privilege policies |

### Requirement 10: Track & Monitor Access

| Check ID | PCI Req | Description | Remediation |
|----------|---------|-------------|-------------|
| CKV_AWS_18 | 10.2 | S3 access logging | Enable logging |
| CKV_AWS_49 | 10.3 | CloudTrail enabled | Add CloudTrail |
| CKV_AWS_51 | 10.3 | ECR image scanning | Enable scan on push |

### Run PCI-DSS Scan

```bash
checkov -d ./terraform \
  --check CKV_AWS_19,CKV_AWS_61,CKV_AWS_7,CKV_AWS_89,CKV_AWS_23,CKV_AWS_40,CKV_AWS_18,CKV_AWS_49
```

---

## HIPAA Security Rule

### §164.308 Administrative Safeguards

| Check ID | HIPAA Control | Description |
|----------|---------------|-------------|
| CKV_AWS_40 | §164.308(a)(3) | IAM access controls (minimum necessary) |
| CKV_AWS_49 | §164.308(a)(4) | CloudTrail logging (audit controls) |
| CKV_AWS_38 | §164.308(a)(5) | EKS RBAC enabled |

### §164.310 Physical Safeguards

| Check ID | HIPAA Control | Description |
|----------|---------------|-------------|
| CKV_AWS_19 | §164.310(d)(1) | Encryption at rest (S3) |
| CKV_AWS_7 | §164.310(d)(1) | Encryption at rest (EBS) |
| CKV_AWS_61 | §164.310(d)(1) | Encryption at rest (RDS) |

### §164.312 Technical Safeguards

| Check ID | HIPAA Control | Description |
|----------|---------------|-------------|
| CKV_AWS_23 | §164.312(a)(1) | Network access control |
| CKV_AWS_18 | §164.312(b) | Audit logging (S3) |
| CKV_AWS_27 | §164.312(c)(1) | SQS encryption |
| CKV_AWS_20 | §164.312(e)(1) | S3 SSL/TLS enforced (transit encryption) |

### Run HIPAA Scan

```bash
checkov -d ./terraform \
  --check CKV_AWS_19,CKV_AWS_7,CKV_AWS_61,CKV_AWS_20,CKV_AWS_18,CKV_AWS_40,CKV_AWS_49,CKV_AWS_23,CKV_AWS_27
```

---

## SOC 2 Trust Service Criteria

### CC6.1: Logical & Physical Access Controls

| Check ID | TSC | Description |
|----------|-----|-------------|
| CKV_AWS_40 | CC6.1 | IAM least privilege |
| CKV_AWS_23 | CC6.1 | Network segmentation |

### CC6.6: Encryption

| Check ID | TSC | Description |
|----------|-----|-------------|
| CKV_AWS_19 | CC6.6 | S3 encryption |
| CKV_AWS_7 | CC6.6 | EBS encryption |
| CKV_AWS_61 | CC6.6 | RDS encryption |
| CKV_AWS_20 | CC6.6 | S3 SSL enforced |

### CC7.2: System Monitoring

| Check ID | TSC | Description |
|----------|-----|-------------|
| CKV_AWS_18 | CC7.2 | S3 access logging |
| CKV_AWS_49 | CC7.2 | CloudTrail enabled |

### Run SOC 2 Scan

```bash
checkov -d ./terraform \
  --check CKV_AWS_40,CKV_AWS_23,CKV_AWS_19,CKV_AWS_7,CKV_AWS_61,CKV_AWS_20,CKV_AWS_18,CKV_AWS_49
```

---

## NIST 800-53 Rev 5

### AC (Access Control)

| Check ID | NIST Control | Description |
|----------|--------------|-------------|
| CKV_AWS_40 | AC-3 | IAM least privilege |
| CKV_AWS_23 | AC-4 | Network access control |

### AU (Audit & Accountability)

| Check ID | NIST Control | Description |
|----------|--------------|-------------|
| CKV_AWS_18 | AU-2 | S3 access logging |
| CKV_AWS_49 | AU-12 | CloudTrail logging |

### SC (System & Communications Protection)

| Check ID | NIST Control | Description |
|----------|--------------|-------------|
| CKV_AWS_19 | SC-28 | Encryption at rest (S3) |
| CKV_AWS_20 | SC-8 | Encryption in transit (S3) |
| CKV_AWS_7 | SC-28 | Encryption at rest (EBS) |
| CKV_AWS_61 | SC-28 | Encryption at rest (RDS) |

---

## GDPR

### Article 32: Security of Processing

| Check ID | GDPR Article | Description |
|----------|--------------|-------------|
| CKV_AWS_19 | Art. 32(1)(a) | Encryption of personal data (S3) |
| CKV_AWS_7 | Art. 32(1)(a) | EBS encryption |
| CKV_AWS_61 | Art. 32(1)(a) | RDS encryption |
| CKV_AWS_21 | Art. 32(1)(b) | Data backup (S3 versioning) |
| CKV_AWS_18 | Art. 32(1)(d) | Access logging |

### Article 25: Data Protection by Design

| Check ID | GDPR Article | Description |
|----------|--------------|-------------|
| CKV_AWS_93 | Art. 25 | S3 public access block |
| CKV_AWS_23 | Art. 25 | Network isolation |
| CKV_AWS_20 | Art. 25 | Secure transmission |

---

## Comprehensive Compliance Report

Generate a full report covering multiple frameworks:

```bash
# All-in-one compliance scan
checkov -d ./terraform \
  --framework terraform \
  --check CIS_AWS \
  -o json -o cli -o sarif \
  --output-file-path ./compliance-report \
  --repo-id my-aws-infrastructure \
  --branch main

# Parse findings by severity
cat .checkov-reports/scans/$(cat .checkov-reports/scans/latest.txt)/results.json | \
  jq '[.results.failed_checks[] | {id: .check_id, severity: .severity, resource: .resource}] | group_by(.severity)'
```

---

## Custom Compliance Policies

### Require Encryption on All Storage

```python
# custom_checks/require_aws_encryption.py
from checkov.terraform.checks.resource.base_resource_check import BaseResourceCheck
from checkov.common.models.enums import CheckResult, CheckCategories

class RequireEncryption(BaseResourceCheck):
    def __init__(self):
        super().__init__(
            name="Ensure all storage resources are encrypted",
            id="CKV_AWS_CUSTOM_ENC_001",
            categories=[CheckCategories.ENCRYPTION],
            supported_resources=[
                'aws_s3_bucket', 'aws_ebs_volume', 'aws_db_instance',
                'aws_rds_cluster', 'aws_dynamodb_table', 'aws_efs_file_system'
            ]
        )

    def scan_resource_conf(self, conf):
        # Check various encryption configurations
        if conf.get('storage_encrypted') == [True]:
            return CheckResult.PASSED
        if conf.get('encrypted') == [True]:
            return CheckResult.PASSED
        if conf.get('server_side_encryption_configuration'):
            return CheckResult.PASSED
        if conf.get('kms_key_id') or conf.get('kms_key_arn'):
            return CheckResult.PASSED
        return CheckResult.FAILED

check = RequireEncryption()
```

### Run with custom + built-in policies

```bash
checkov -d ./terraform \
  --external-checks-dir ./custom_checks \
  --check CIS_AWS,CKV_AWS_CUSTOM_ENC_001
```

---

## Compliance Matrix Summary

| Framework | Checkov Support | Key Checks | Focus Area |
|-----------|-----------------|------------|------------|
| CIS AWS v1.4 | ✓ Full | 100+ | All AWS services |
| PCI-DSS 3.2.1 | ✓ Partial | 30+ | Encryption, access, logging |
| HIPAA | ✓ Partial | 40+ | PHI protection, audit |
| SOC 2 | ✓ Partial | 35+ | Access, encryption, monitoring |
| NIST 800-53 | ✓ Mapping | 60+ | Comprehensive security |
| GDPR | ✓ Mapping | 25+ | Data protection |
