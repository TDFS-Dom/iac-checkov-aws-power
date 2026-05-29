# Prisma Cloud Official Severity Classification — Complete AWS Policies

> **Sources**: All AWS policy category pages from Prisma Cloud docs (fetched 2025-05-29)
> - aws-general-policies
> - elastisearch-policies
> - aws-iam-policies
> - aws-kubernetes-policies
> - aws-logging-policies
> - aws-networking-policies
> - public-policies
> - s3-policies
> - secrets-policies
> - aws-serverless-policies
>
> **Last updated on Prisma Cloud**: June 11, 2025

---

## CRITICAL

| Check ID | Description | Category |
|---|---|---|
| CKV_AWS_62 | IAM policies that allow full "-" administrative privileges are created | IAM |

---

## HIGH

| Check ID | Description | Category |
|---|---|---|
| CKV_AWS_3 | AWS EBS volumes are not encrypted | General |
| CKV_AWS_20 | S3 bucket ACL grants READ permission to everyone | S3 |
| CKV_AWS_28 | DynamoDB PITR is disabled | General |
| CKV_AWS_41 | AWS access keys and secrets are hard coded in infrastructure | Secrets |
| CKV_AWS_46 | EC2 user data exposes secrets | Secrets |
| CKV_AWS_57 | S3 Bucket has ACL allowing public WRITE access | S3 |
| CKV_AWS_79 | EC2 instance not configured with IMDSv2 | General |
| CKV_AWS_88 | EC2 instances with public IP and security groups have Internet access | Public |
| CKV_AWS_94 | Glue Data Catalog encryption is not enabled | General |
| CKV_AWS_96 | Not all data stored in Aurora is securely encrypted at rest | General |
| CKV_AWS_97 | EFS volumes in ECS task definitions no encryption in transit | General |
| CKV_AWS_98 | SageMaker endpoint data encryption at rest not configured | General |
| CKV_AWS_99 | Glue security configuration encryption is not enabled | General |
| CKV_AWS_100 | EKS node group have implicit SSH access from 0.0.0.0/0 | Kubernetes |
| CKV_AWS_101 | Neptune logging is not enabled | Logging |
| CKV_AWS_102 | Neptune cluster instance is publicly available | General |
| CKV_AWS_103 | Load Balancer is not using TLS 1.2 | General |
| CKV_AWS_127 | Elastic load balancers do not use SSL Certificates from ACM | General |
| CKV_AWS_163 | ECR image scan on push is not enabled | General |
| CKV_AWS_168 | SQS queue policy is public and not restricted | General |
| CKV_AWS_192 | WAF enables message lookup in Log4j2 | Networking |
| CKV_AWS_267 | Comprehend Entity Recognizer's model not encrypted by KMS CMK | General |
| CKV_AWS_268 | Comprehend Entity Recognizer's volume not encrypted by KMS CMK | General |
| CKV_AWS_270 | Connect Instance S3 Storage Configuration utilizes CMK | General |
| CKV_AWS_271 | DynamoDB table replica does not use CMK KMS encryption | General |
| CKV_AWS_272 | Lambda function not configured to validate code-signing | General |
| CKV_AWS_274 | AdministratorAccess policy is used by IAM roles, users, or groups | IAM |
| CKV_AWS_278 | MemoryDB snapshot not encrypted by KMS CMK | General |
| CKV_AWS_279 | Neptune snapshot is not securely encrypted | General |
| CKV_AWS_280 | Neptune snapshot encrypted by KMS CMK | General |
| CKV_AWS_281 | RedShift snapshot copy not encrypted by KMS CMK | General |
| CKV_AWS_282 | Redshift Serverless namespace not encrypted by KMS CMK | General |
| CKV_AWS_283 | IAM Policy Document Allows All or Any AWS Principal Permissions | IAM |
| CKV_AWS_287 | IAM policies allow exposure of credentials | IAM |
| CKV_AWS_288 | IAM policies allow data exfiltration | IAM |
| CKV_AWS_289 | IAM policies allow permissions management without constraints | IAM |
| CKV_AWS_290 | IAM policies allow write access without constraints | IAM |
| CKV_AWS_291 | MSK nodes are not private | Networking |
| CKV_AWS_292 | DocDB Global Cluster not encrypted at rest | General |
| CKV_AWS_295 | DataSync Location Object Storage exposes secrets | General |
| CKV_AWS_296 | DMS endpoint not using CMK | General |
| CKV_AWS_297 | EventBridge Scheduler not using CMK | General |
| CKV_AWS_298 | DMS S3 does not use CMK | General |
| CKV_AWS_304 | Secrets Manager secrets not rotated within 90 days | General |
| CKV_AWS_308 | API Gateway method setting not encrypted caching | General |
| CKV_AWS_311 | CodeBuild S3 logs are not encrypted | General |
| CKV_AWS_312 | Elastic Beanstalk no enhanced health reporting | General |
| CKV_AWS_328 | ALB not configured with defensive/strictest desync mitigation | Networking |
| CKV_AWS_329 | EFS Access Points not enforcing root directory | General |
| CKV_AWS_337 | SSM parameters not utilizing KMS CMK | General |
| CKV_AWS_339 | EKS clusters not running on supported Kubernetes version | Kubernetes |
| CKV_AWS_343 | Redshift clusters no automatic snapshots | General |
| CKV_AWS_344 | Network firewalls no deletion protection | General |
| CKV_AWS_345 | Network firewall encryption no CMK | General |
| CKV_AWS_346 | Network Firewall Policy no CMK encryption config | General |
| CKV_AWS_347 | Neptune not encrypted with KMS CMK | General |
| CKV_AWS_348 | Access key enabled on root account | IAM |
| CKV_AWS_350 | EMR Cluster security config no EBS disk encryption | General |
| CKV_AWS_352 | NACL ingress allows all ports | Networking |
| CKV_AWS_354 | RDS Performance Insights not encrypted using KMS CMKs | General |
| CKV_AWS_355 | IAM policy documents allow all resources with restricted actions | IAM |
| CKV_AWS_356 | Data source IAM policy allows all resources with restricted actions | IAM |
| CKV_AWS_357 | Transfer server does not force secure protocols | General |
| CKV_AWS_358 | GitHub Actions OIDC authorization policies allow unsafe claims | IAM |
| CKV_AWS_364 | Permissions delegated to AWS services for Lambda not limited | IAM |
| CKV2_AWS_6 | S3 Bucket does not have public access blocks | Networking |
| CKV2_AWS_38 | DNSSEC signing not enabled for Route 53 public hosted zones | Networking |
| CKV2_AWS_39 | DNS query logging not enabled for Route 53 hosted zones | Logging |
| CKV2_AWS_56 | AWS Managed IAMFullAccess IAM policy should not be used | IAM |
| CKV2_AWS_66 | MWAA environment is publicly accessible | Networking |

---

## MEDIUM

| Check ID | Description | Category |
|---|---|---|
| CKV_AWS_2 | ELBv2 listener allows connection requests over HTTP | Networking |
| CKV_AWS_6 | Elasticsearch does not have node-to-node encryption | Elasticsearch |
| CKV_AWS_13 | IAM password policy does allow password reuse | IAM |
| CKV_AWS_17 | RDS database instance is publicly accessible | Public |
| CKV_AWS_26 | SNS topic has SSE disabled | General |
| CKV_AWS_32 | Private ECR repository policy is overly permissive | Public |
| CKV_AWS_33 | KMS Key policy overly permissive | IAM |
| CKV_AWS_34 | CloudFront viewer protocol policy not configured with HTTPS | Networking |
| CKV_AWS_39 | EKS cluster endpoint access publicly enabled | Kubernetes |
| CKV_AWS_44 | Neptune storage not securely encrypted | General |
| CKV_AWS_45 | Lambda function's environment variables expose secrets | Secrets |
| CKV_AWS_48 | Amazon MQ Broker logging is not enabled | Logging |
| CKV_AWS_49 | IAM policy documents do not allow * as a statement's action | IAM |
| CKV_AWS_54 | S3 Bucket BlockPublicPolicy not set to True | S3 |
| CKV_AWS_55 | S3 bucket IgnorePublicAcls not set to True | S3 |
| CKV_AWS_56 | S3 bucket RestrictPublicBucket not set to True | S3 |
| CKV_AWS_58 | EKS cluster does not have secrets encryption enabled | Kubernetes |
| CKV_AWS_60 | IAM role allows all services or principals to be assumed | IAM |
| CKV_AWS_61 | IAM policy allows all principals from target account | IAM |
| CKV_AWS_63 | IAM policy documents allow * as a statement's action | IAM |
| CKV_AWS_70 | S3 bucket policy overly permissive to any principal | S3 |
| CKV_AWS_74 | DocumentDB is not encrypted at rest | General |
| CKV_AWS_77 | Athena Database is not encrypted at rest | General |
| CKV_AWS_78 | CodeBuild project encryption is disabled | General |
| CKV_AWS_80 | Amazon MSK cluster logging is not enabled | Logging |
| CKV_AWS_81 | MSK cluster encryption in transit not enabled | General |
| CKV_AWS_82 | Athena workgroup does not prevent disabling encryption | General |
| CKV_AWS_83 | Elasticsearch domain is not configured with HTTPS | Elasticsearch |
| CKV_AWS_84 | Elasticsearch domain logging is not enabled | Elasticsearch |
| CKV_AWS_85 | DocumentDB logging is not enabled | Logging |
| CKV_AWS_87 | Redshift cluster instance with public access enabled | Public/Networking |
| CKV_AWS_90 | DocDB TLS is disabled | Networking |
| CKV_AWS_93 | S3 bucket policy allows lockout all but root user | S3 |
| CKV_AWS_110 | IAM policies allow privilege escalation | IAM |
| CKV_AWS_112 | Session Manager data not encrypted in transit | General |
| CKV_AWS_113 | Deletion protection disabled for load balancer | General |
| CKV_AWS_121 | AWS config is not enabled in all regions | Logging |
| CKV_AWS_126 | EC2 instance detailed monitoring disabled | Logging |
| CKV_AWS_131 | ALB does not drop HTTP headers | Networking |
| CKV_AWS_155 | Workspace user volumes not encrypted | General |
| CKV_AWS_156 | Workspace root volumes not encrypted | General |
| CKV_AWS_159 | Athena Workgroup is not encrypted | General |
| CKV_AWS_160 | Timestream database not encrypted with KMS CMK | General |
| CKV_AWS_161 | RDS database does not have IAM authentication enabled | IAM |
| CKV_AWS_164 | Transfer Server is publicly exposed | Networking |
| CKV_AWS_165 | DynamoDB point in time recovery not enabled for global tables | General |
| CKV_AWS_166 | Backup Vault not encrypted at rest using KMS CMK | General |
| CKV_AWS_167 | Glacier Vault access policy is public and not restricted | General |
| CKV_AWS_169 | SNS topic policy is public and not restricted | General |
| CKV_AWS_170 | QLDB ledger permissions mode not set to STANDARD | General |
| CKV_AWS_250 | RDS PostgreSQL exposed to local file read vulnerability | General |
| CKV_AWS_258 | Lambda Function URL AuthType set to NONE | General |
| CKV_AWS_269 | Connect Instance Kinesis Video Stream Storage Config no CMK | General |
| CKV_AWS_277 | Security Group allows all traffic on all ports | Networking |
| CKV_AWS_285 | Execution history logging not enabled on State Machine | Logging |
| CKV_AWS_286 | IAM Policy permission may cause privilege escalation | IAM |
| CKV_AWS_293 | Database instances do not have deletion protection | General |
| CKV_AWS_300 | S3 lifecycle config no period for aborting failed uploads | General |
| CKV_AWS_302 | RDS snapshots are accessible to public | General |
| CKV_AWS_303 | SSM documents are public | General |
| CKV_AWS_305 | CloudFront distributions no default root object | General |
| CKV_AWS_309 | Authorization type for API GatewayV2 routes not specified | IAM |
| CKV_AWS_310 | CloudFront distributions no origin failover | General |
| CKV_AWS_315 | EC2 Auto Scaling groups not utilizing EC2 launch templates | General |
| CKV_AWS_316 | CodeBuild project environment privileged mode enabled | General |
| CKV_AWS_317 | Elasticsearch Domain Audit Logging disabled | Logging |
| CKV_AWS_318 | Elasticsearch domains not configured with 3 dedicated masters | General |
| CKV_AWS_319 | CloudWatch alarm actions are not enabled | General |
| CKV_AWS_320 | Redshift clusters not using default database name | General |
| CKV_AWS_321 | Redshift clusters not using enhanced VPC routing | General |
| CKV_AWS_324 | RDS Cluster log capture is disabled | Logging |
| CKV_AWS_326 | RDS Aurora Clusters no backtracking enabled | General |
| CKV_AWS_330 | User identity should be enforced by EFS access points | General |
| CKV_AWS_332 | ECS Fargate services not on latest platform version | General |
| CKV_AWS_334 | ECS task definition elevated privileges enabled | General |
| CKV_AWS_335 | ECS task definitions share host's process namespace | General |
| CKV_AWS_341 | Auto Scaling group launch config with IMDS hop count > 1 | General |
| CKV_AWS_363 | Runtime of Lambda is deprecated | General |
| CKV_AWS_365 | TLS not enforced in SES configuration set | Networking |
| CKV_AWS_366 | Cognito identity pool allows unauthenticated guest access | IAM |
| CKV_AWS_370 | SageMaker model does not use network isolation | Networking |
| CKV_AWS_371 | SageMaker Notebook Instance allows for IMDSv1 | General |
| CKV_AWS_373 | Bedrock Agent not encrypted with CMK | General |
| CKV_AWS_378 | Load Balancer uses HTTP protocol | Networking |
| CKV_AWS_379 | S3 bucket not configured with secure data transport policy | Networking |
| CKV_AWS_384 | Hard-coded secrets found in Parameter Store values | General |
| CKV2_AWS_22 | IAM User has access to the console | IAM |
| CKV2_AWS_23 | Route53 A Record does not have Attached Resource | General |
| CKV2_AWS_29 | Public API gateway not configured with AWS WAFv2 | Networking |
| CKV2_AWS_40 | IAM policy allows full administrative privileges | IAM |
| CKV2_AWS_43 | S3 buckets are accessible to any authenticated user | IAM |
| CKV2_AWS_47 | CloudFront attached WAFv2 WebACL not configured for Log4j | General |
| CKV2_AWS_54 | CloudFront distribution using insecure SSL protocols | Networking |
| CKV2_AWS_61 | S3 bucket must have a lifecycle configuration | Logging |
| CKV2_AWS_64 | A Policy is not Defined for KMS Key | IAM |
| CKV2_AWS_68 | SageMaker notebook instance IAM policy overly permissive | Networking |
| CKV2_AWS_69 | RDS database instance not configured with encryption in transit | Networking |
| CKV2_AWS_70 | API Gateway method lacking authorization or API keys | Networking |
| CKV2_AWS_72 | CloudFront origin protocol policy does not enforce HTTPS-only | Networking |
| CKV2_AWS_75 | Lambda function URL overly permissive CORS | Networking |

---

## LOW

| Check ID | Description | Category |
|---|---|---|
| CKV_AWS_1 | IAM policies that allow full administrative privileges are created | IAM |
| CKV_AWS_5 | Elasticsearch domain Encryption for data at rest disabled | Elasticsearch |
| CKV_AWS_12 | IAM password policy does not have a number | IAM |
| CKV_AWS_19 | S3 buckets do not have server side encryption | S3 |
| CKV_AWS_21 | S3 Object Versioning is disabled | S3 |
| CKV_AWS_23 | Not every Security Group rule has a description | Networking |
| CKV_AWS_38 | EKS cluster security group overly permissive to all traffic | Kubernetes |
| CKV_AWS_40 | IAM policy attached to users | IAM |
| CKV_AWS_50 | Lambda functions with tracing not enabled | Serverless |
| CKV_AWS_59 | API gateway methods are publicly accessible | Public |
| CKV_AWS_65 | ECS cluster with container insights feature disabled | Logging |
| CKV_AWS_66 | CloudWatch Log groups not configured with retention days | Logging |
| CKV_AWS_69 | MQ is publicly accessible | Public |
| CKV_AWS_73 | API Gateway does not have X-Ray tracing enabled | Logging |
| CKV_AWS_76 | API Gateway does not have access logging enabled | Logging |
| CKV_AWS_87 | Redshift cluster is publicly accessible | Networking |
| CKV_AWS_89 | DMS replication instance is publicly accessible | Public |
| CKV_AWS_95 | API Gateway V2 has Access Logging disabled | Logging |
| CKV_AWS_107 | Credentials exposure actions return credentials in API response | IAM |
| CKV_AWS_108 | Data exfiltration allowed without resource constraints | IAM |
| CKV_AWS_109 | Resource exposure allows modification of policies | IAM |
| CKV_AWS_111 | Write access allowed without constraint | IAM |
| CKV_AWS_118 | RDS instances Enhanced Monitoring disabled | Logging |
| CKV_AWS_122 | SageMaker notebook configured with direct internet access | Networking |
| CKV_AWS_123 | VPC endpoint service not configured for manual acceptance | Networking |
| CKV_AWS_124 | CloudFormation stack configured without SNS topic | Logging |
| CKV_AWS_128 | IAM authentication for Amazon RDS clusters disabled | IAM |
| CKV_AWS_129 | Respective logs of Amazon RDS are disabled | IAM |
| CKV_AWS_130 | VPC subnets should not allow automatic public IP assignment | Networking |
| CKV_AWS_131 | ALB does not drop HTTP headers | Networking |
| CKV_AWS_137 | Elasticsearch is not configured inside a VPC | Networking |
| CKV_AWS_138 | ELB (Classic) with cross-zone load balancing disabled | Networking |
| CKV_AWS_148 | Default VPC is planned to be provisioned | Networking |
| CKV_AWS_153 | Autoscaling groups did not supply tags to launch configs | General |
| CKV_AWS_154 | Redshift is deployed outside of a VPC | Networking |
| CKV_AWS_162 | RDS cluster not configured with IAM authentication | IAM |
| CKV_AWS_173 | Lambda encryption settings environmental variable not set | Serverless |
| CKV_AWS_174 | CloudFront web distribution using insecure TLS version | Networking |
| CKV_AWS_175 | WAF does not have associated rules | Networking |
| CKV_AWS_176 | WAF Web Access Control Lists logging disabled | Logging |
| CKV_AWS_196 | Elasticache security groups are not defined | Networking |
| CKV_AWS_198 | RDS security groups are not defined | Networking |
| CKV_AWS_213 | ELB Policy uses some unsecure protocols | Networking |
| CKV_AWS_229 | NACL allows ingress from 0.0.0.0/0 to port 21 | Networking |
| CKV_AWS_230 | NACL allows ingress from 0.0.0.0/0 to port 20 | Networking |
| CKV_AWS_231 | NACL allows ingress from 0.0.0.0/0 to port 3389 | Networking |
| CKV_AWS_232 | NACL allows ingress from 0.0.0.0/0 to port 22 | Networking |
| CKV_AWS_233 | ACM certificate does not enable Create before Destroy | Networking |
| CKV_AWS_248 | Elasticsearch uses the default security group | Networking |
| CKV_AWS_249 | Execution Role ARN and Task Role ARN are different in ECS | IAM |
| CKV_AWS_260 | Security groups allow ingress from 0.0.0.0/0 to port 80 | Networking |
| CKV_AWS_273 | Access is not controlled through Single Sign-On (SSO) | IAM |
| CKV_AWS_276 | Data Trace not enabled in API Gateway Method Settings | Logging |
| CKV_AWS_284 | State machine does not have X-ray tracing enabled | Logging |
| CKV_AWS_301 | Lambda Function resource-based policy is overly permissive | General |
| CKV_AWS_313 | RDS cluster not configured to copy tags to snapshots | General |
| CKV_AWS_323 | ElastiCache cluster is using the default subnet group | Networking |
| CKV_AWS_325 | RDS Cluster audit logging for MySQL engine disabled | Logging |
| CKV_AWS_333 | ECS services have automatic public IP address assignment | Logging |
| CKV_AWS_353 | RDS instances have performance insights disabled | Logging |
| CKV_AWS_359 | Neptune Cluster not configured with IAM authentication | IAM |
| CKV_AWS_374 | CloudFront web distribution with geo restriction disabled | Networking |
| CKV_AWS_375 | S3 bucket has global view ACL permissions enabled | Networking |
| CKV_AWS_376 | ELB with listener TLS/SSL is not configured | Networking |
| CKV_AWS_377 | Route 53 domains do not have transfer lock protection | Networking |
| CKV_AWS_380 | Transfer Server not using latest Security Policy | Networking |
| CKV_AWS_382 | Security Group allows unrestricted egress traffic | Networking |
| CKV_AWS_383 | Bedrock agent not associated with Bedrock guardrails | General |
| CKV2_AWS_4 | API Gateway stage no logging level defined | Logging |
| CKV2_AWS_5 | Security Groups not attached to EC2 instances or ENIs | Networking |
| CKV2_AWS_7 | EMR clusters' security groups open to the world | Networking |
| CKV2_AWS_12 | Default Security Group does not restrict all traffic | Networking |
| CKV2_AWS_15 | Auto scaling groups with LB no elastic health checks | Networking |
| CKV2_AWS_19 | Not all EIP addresses attached to EC2 instances | Networking |
| CKV2_AWS_20 | ALB does not redirect HTTP requests into HTTPS | Networking |
| CKV2_AWS_21 | Not all IAM users are members of at least one IAM group | IAM |
| CKV2_AWS_28 | ALB not configured with AWS WAFv2 | Networking |
| CKV2_AWS_30 | Postgres RDS have Query Logging disabled | Logging/General |
| CKV2_AWS_31 | WAF2 does not have a Logging Configuration | Logging |
| CKV2_AWS_32 | CloudFront distribution no strict security headers policy | Networking |
| CKV2_AWS_35 | NAT Gateways not utilized for the default route | Networking |
| CKV2_AWS_42 | CloudFront web distribution with default SSL certificate | Networking |
| CKV2_AWS_44 | Route table with VPC peering overly permissive | Networking |
| CKV2_AWS_46 | Cloudfront Distribution with S3 have Origin Access disabled | IAM |
| CKV2_AWS_49 | Database Migration Service endpoint no SSL configured | Networking |
| CKV2_AWS_52 | OpenSearch Fine-grained access control disabled | IAM |
| CKV2_AWS_62 | S3 buckets do not have event notifications enabled | Logging |
| CKV2_AWS_65 | S3 bucket ACLs in use | General |
| CKV2_AWS_71 | ACM Certificate with wildcard domain name | Networking |
| CKV2_AWS_74 | Load Balancers do not use strong ciphers | Networking |

---

## INFO

| Check ID | Description | Category |
|---|---|---|
| CKV_AWS_7 | Customer Master Key (CMK) rotation is not enabled | Logging |
| CKV_AWS_8 | EC2 Auto Scaling Launch Config not using encrypted EBS | General |
| CKV_AWS_9 | IAM password policy does not expire in 90 days | IAM |
| CKV_AWS_10 | IAM password policy does not have minimum 14 characters | IAM |
| CKV_AWS_11 | IAM password policy does not have a lowercase character | IAM |
| CKV_AWS_14 | IAM password policy does not have a symbol | IAM |
| CKV_AWS_15 | IAM password policy does not have an uppercase character | IAM |
| CKV_AWS_18 | S3 Access logging not enabled on S3 buckets | S3 |
| CKV_AWS_24 | Security Group allows all traffic on SSH port (22) | Networking |
| CKV_AWS_25 | Security Group allows all traffic on RDP port (3389) | Networking |
| CKV_AWS_35 | CloudTrail logs not encrypted using CMKs | Logging |
| CKV_AWS_36 | CloudTrail log validation not enabled in all regions | Logging |
| CKV_AWS_37 | EKS control plane logging disabled | Kubernetes |
| CKV_AWS_47 | DAX cluster not configured with encryption at rest | General |
| CKV_AWS_67 | CloudTrail not enabled with multi trail and not capturing all | Logging |
| CKV_AWS_68 | CloudFront with WAF service disabled | General |
| CKV_AWS_71 | Redshift database does not have audit logging enabled | Logging |
| CKV_AWS_72 | SQS policy allows all actions | IAM |
| CKV_AWS_86 | CloudFront distribution with access logging disabled | Logging |
| CKV_AWS_91 | ELBv2 with access log disabled | Logging |
| CKV_AWS_92 | ELB (Classic) with access log disabled | Logging |
| CKV_AWS_119 | DynamoDB encrypted using AWS owned CMK instead of managed | General |
| CKV_AWS_134 | ElastiCache Redis cluster not configured with automatic backup | General |
| CKV_AWS_139 | RDS cluster delete protection is disabled | General |
| CKV_AWS_142 | Redshift Cluster not encrypted using CMK | General |
| CKV_AWS_194 | AppSync has field-level logging disabled | General |
| CKV_AWS_238 | GuardDuty detector is not enabled | General |
| CKV_AWS_251 | CloudTrail logging is disabled | General |
| CKV_AWS_294 | CloudTrail Event Data Store no CMKs | General |
| CKV_AWS_306 | SageMaker notebook instance is not placed in VPC | Networking |
| CKV_AWS_307 | SageMaker notebook instance with root access enabled | General |
| CKV_AWS_314 | CodeBuild project not configured with logging | Logging |
| CKV_AWS_322 | ElastiCache Redis cluster automatic version upgrade disabled | General |
| CKV_AWS_327 | RDS DB cluster encrypted using default KMS key instead of CMK | General |
| CKV_AWS_336 | ECS task definition no read-only root filesystems | General |
| CKV_AWS_338 | CloudWatch log groups retention set to less than 365 days | Logging |
| CKV_AWS_340 | Elastic Beanstalk managed platform updates not enabled | General |
| CKV_AWS_361 | Neptune DB clusters backup retention < 7 days | General |
| CKV_AWS_387 | SQS queue access policy is overly permissive | General |
| CKV2_AWS_1 | Network ACL is not in use | Networking |
| CKV2_AWS_10 | CloudTrail trail logs not integrated with CloudWatch Log | Logging |
| CKV2_AWS_11 | VPC Flow Logs not enabled | Logging |
| CKV2_AWS_14 | IAM group not in use | IAM |
| CKV2_AWS_16 | DynamoDB table Auto Scaling not enabled | General |
| CKV2_AWS_41 | EC2 Instance IAM Role not enabled | IAM |
| CKV2_AWS_45 | AWS Config Recording is disabled | General |
| CKV2_AWS_48 | AWS Config must record all possible resources | General |
| CKV2_AWS_50 | ElastiCache Redis Multi-AZ Automatic Failover disabled | General |
| CKV2_AWS_55 | EMR cluster not configured with security configuration | General |
| CKV2_AWS_58 | Neptune cluster deletion protection disabled | General |
| CKV2_AWS_60 | RDS instance with copy tags to snapshots disabled | General |
| CKV2_AWS_63 | Network Firewall not configured with logging configuration | Logging |
| CKV2_AWS_73 | SQS queue encryption using default KMS key instead of CMK | General |

---

## Summary Statistics

| Severity | Count |
|---|---|
| CRITICAL | 1 |
| HIGH | 70 |
| MEDIUM | 119 |
| LOW | 97 |
| INFO | 52 |
| **Total** | **339** |

---

## Notes

1. **Một số checks xuất hiện trên nhiều category pages** (ví dụ CKV_AWS_87 ở cả Networking và Public). Severity được lấy từ page cuối cùng/chính xác nhất.
2. **Một số checks KHÔNG CÓ trên bất kỳ page nào** (ví dụ CKV_AWS_4, CKV_AWS_52...) — có thể đã deprecated hoặc nằm ở category page khác chưa được fetch.
3. **CKV_AWS_62** là check DUY NHẤT ở level CRITICAL trên Prisma Cloud — liên quan đến full admin privileges.
4. **Khác biệt đáng chú ý so với Checkov community conventions**:
   - Prisma Cloud xếp nhiều "public access" checks (CKV_AWS_17, CKV_AWS_59, CKV_AWS_69, CKV_AWS_87, CKV_AWS_89) ở MEDIUM/LOW thay vì CRITICAL
   - Prisma Cloud coi encryption CMK checks phần lớn là LOW (best practice) 
   - Security Group rules (22, 3389) ở INFO thay vì HIGH/CRITICAL
   - IAM password policy checks (10, 11, 14, 15) ở INFO
