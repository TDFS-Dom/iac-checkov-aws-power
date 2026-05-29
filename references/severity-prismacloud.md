# Prisma Cloud Official Severity Classification — Complete AWS Policies

> **Sources**: All AWS policy category pages from Prisma Cloud docs (fetched 2025-05-29)
> - GitHub: `hlxsites/prisma-cloud-docs` → `docs/en/enterprise-edition/policy-reference/aws-policies/`
> - Categories: aws-general-policies, elastisearch-policies, aws-iam-policies, aws-kubernetes-policies,
>   aws-logging-policies, aws-networking-policies, public-policies, s3-policies, secrets-policies, aws-serverless-policies, aws-supply-chain-policies

<details>
<summary>🔄 Câu lệnh cập nhật (click để mở)</summary>

```bash
# Step 1: Download all adoc files from GitHub raw
BASE="https://raw.githubusercontent.com/hlxsites/prisma-cloud-docs/main/docs/en/enterprise-edition/policy-reference/aws-policies"

curl -sL "$BASE/aws-general-policies/aws-general-policies.adoc" > prisma-cloud-docs/aws-general-policies.adoc
curl -sL "$BASE/elastisearch-policies/elastisearch-policies.adoc" > prisma-cloud-docs/elastisearch-policies.adoc
curl -sL "$BASE/aws-iam-policies/aws-iam-policies.adoc" > prisma-cloud-docs/aws-iam-policies.adoc
curl -sL "$BASE/aws-kubernetes-policies/aws-kubernetes-policies.adoc" > prisma-cloud-docs/aws-kubernetes-policies.adoc
curl -sL "$BASE/aws-logging-policies/aws-logging-policies.adoc" > prisma-cloud-docs/aws-logging-policies.adoc
curl -sL "$BASE/aws-networking-policies/aws-networking-policies.adoc" > prisma-cloud-docs/aws-networking-policies.adoc
curl -sL "$BASE/public-policies/public-policies.adoc" > prisma-cloud-docs/public-policies.adoc
curl -sL "$BASE/s3-policies/s3-policies.adoc" > prisma-cloud-docs/s3-policies.adoc
curl -sL "$BASE/aws-serverless-policies/aws-serverless-policies.adoc" > prisma-cloud-docs/aws-serverless-policies.adoc
curl -sL "$BASE/aws-supply-chain-policies/aws-supply-chain-policies.adoc" > prisma-cloud-docs/aws-supply-chain-policies.adoc

# Step 2: Verify downloads
wc -l prisma-cloud-docs/*.adoc

# Step 3: Check if any new category folders appeared
curl -sL "https://api.github.com/repos/hlxsites/prisma-cloud-docs/contents/docs/en/enterprise-edition/policy-reference/aws-policies" | python3 -c "import json,sys; data=json.load(sys.stdin); [print(x['name'], x['type']) for x in data]"
```

</details>

---

## AWS General Policies

| Policy | Checkov ID | Severity |
|--------|-----------|----------|
| Amazon Redshift clusters do not have automatic snapshots enabled | CKV_AWS_343 | HIGH |
| API Gateway method setting is not set to encrypted caching | CKV_AWS_308 | HIGH |
| AWS EBS volumes are not encrypted | CKV_AWS_3 | HIGH |
| AWS EC2 instance not configured with Instance Metadata Service v2 (IMDSv2) | CKV_AWS_79 | HIGH |
| AWS Glue security configuration encryption is not enabled | CKV_AWS_99 | HIGH |
| AWS Lambda function is not configured to validate code-signing | CKV_AWS_272 | HIGH |
| AWS Load Balancer is not using TLS 1.2 | CKV_AWS_103 | HIGH |
| AWS provisioned resources are manually modified | N/A | HIGH |
| AWS SageMaker endpoint data encryption at rest not configured | CKV_AWS_98 | HIGH |
| CodeBuild S3 logs are not encrypted | CKV_AWS_311 | HIGH |
| Comprehend Entity Recognizer's model is not encrypted by KMS using a customer managed Key (CMK) | CKV_AWS_267 | HIGH |
| Comprehend Entity Recognizer's volume is not encrypted by KMS using a customer managed Key (CMK) | CKV_AWS_268 | HIGH |
| DataSync Location Object Storage exposes secrets | CKV_AWS_295 | HIGH |
| DMS endpoint is not using a Customer Managed Key (CMK) | CKV_AWS_296 | HIGH |
| DocDB Global Cluster is not encrypted at rest | CKV_AWS_292 | HIGH |
| DynamoDB PITR is disabled | CKV_AWS_28 | HIGH |
| DynamoDB table replica does not use CMK KMS encryption | CKV_AWS_271 | HIGH |
| ECR image scan on push is not enabled | CKV_AWS_163 | HIGH |
| EFS Access Points are not enforcing a root directory | CKV_AWS_329 | HIGH |
| EFS volumes in ECS task definitions do not have encryption in transit enabled | CKV_AWS_97 | HIGH |
| Elastic Beanstalk environments do not have enhanced health reporting enabled | CKV_AWS_312 | HIGH |
| Elastic load balancers do not use SSL Certificates provided by AWS Certificate Manager | CKV_AWS_127 | HIGH |
| EventBridge Scheduler Schedule is not using a Customer Managed Key (CMK) | CKV_AWS_297 | HIGH |
| Glue Data Catalog encryption is not enabled | CKV_AWS_94 | HIGH |
| MemoryDB snapshot is not encrypted by KMS using a customer managed Key (CMK) | CKV_AWS_278 | HIGH |
| Neptune cluster instance is publicly available | CKV_AWS_102 | HIGH |
| Neptune is not encrypted with KMS using a customer managed Key (CMK) | CKV_AWS_347 | HIGH |
| Neptune snapshot is encrypted by KMS using a customer managed Key (CMK) | CKV_AWS_280 | HIGH |
| Neptune snapshot is not securely encrypted | CKV_AWS_279 | HIGH |
| Network firewall encryption does not use a CMK | CKV_AWS_345 | HIGH |
| Network Firewall Policy does not define an encryption configuration that uses a CMK | CKV_AWS_346 | HIGH |
| Network firewalls do not have deletion protection enabled | CKV_AWS_344 | HIGH |
| Not all data stored in Aurora is securely encrypted at rest | CKV_AWS_96 | HIGH |
| RDS Performance Insights are not encrypted using KMS CMKs | CKV_AWS_354 | HIGH |
| Redshift Serverless namespace is not encrypted by KMS using a customer managed key (CMK) | CKV_AWS_282 | HIGH |
| RedShift snapshot copy is not encrypted by KMS using a customer managed Key (CMK). | CKV_AWS_281 | HIGH |
| Secrets Manager secrets are not rotated within 90 days | CKV_AWS_304 | HIGH |
| Security configuration of the EMR Cluster does not ensure the encryption of EBS disks | CKV_AWS_350 | HIGH |
| SQS queue policy is public and access is not restricted to specific services or principals | CKV_AWS_168 | HIGH |
| SSM parameters are not utilizing KMS CMK. | CKV_AWS_337 | HIGH |
| The Connect Instance S3 Storage Configuration utilizes Customer Managed Key. | CKV_AWS_270 | HIGH |
| The DMS S3 does not use a Customer Managed Key (CMK) | CKV_AWS_298 | HIGH |
| Transfer server does not force secure protocols. | CKV_AWS_357 | HIGH |
| Athena Database is not encrypted at rest | CKV_AWS_77 | MEDIUM |
| Athena workgroup does not prevent disabling encryption | CKV_AWS_82 | MEDIUM |
| Athena Workgroup is not encrypted | CKV_AWS_159 | MEDIUM |
| AWS Auto Scaling group launch configuration configured with Instance Metadata Service hop count greater than 1 | CKV_AWS_341 | MEDIUM |
| AWS CloudFront attached WAFv2 WebACL is not configured with AMR for Log4j Vulnerability | CKV2_AWS_47 | MEDIUM |
| AWS CloudFront distributions does not have a default root object configured | CKV_AWS_305 | MEDIUM |
| AWS CodeBuild project environment privileged mode is enabled | CKV_AWS_316 | MEDIUM |
| AWS database instances do not have deletion protection enabled | CKV_AWS_293 | MEDIUM |
| AWS ECS task definition elevated privileges enabled | CKV_AWS_334 | MEDIUM |
| AWS Lambda function URL AuthType set to NONE | CKV_AWS_258 | MEDIUM |
| AWS MSK cluster encryption in transit is not enabled | CKV_AWS_81 | MEDIUM |
| AWS RDS PostgreSQL exposed to local file read vulnerability | CKV_AWS_250 | MEDIUM |
| AWS RDS snapshots are accessible to public | CKV_AWS_302 | MEDIUM |
| AWS SageMaker Notebook Instance allows for IMDSv1 | CKV_AWS_371 | MEDIUM |
| AWS SNS topic has SSE disabled | CKV_AWS_26 | MEDIUM |
| AWS SSM documents are public | CKV_AWS_303 | MEDIUM |
| Backup Vault is not encrypted at rest using KMS CMK | CKV_AWS_166 | MEDIUM |
| Bedrock Agent not encrypted with Customer Master Key (CMK) | CKV_AWS_373 | MEDIUM |
| CloudFront distributions do not have origin failover configured | CKV_AWS_310 | MEDIUM |
| CloudWatch alarm actions are not enabled | CKV_AWS_319 | MEDIUM |
| CodeBuild project encryption is disabled | CKV_AWS_78 | MEDIUM |
| CodeBuild projects are not encrypted | CKV_AWS_147 | MEDIUM |
| Connect Instance Kinesis Video Stream Storage Config is not using CMK for encryption | CKV_AWS_269 | MEDIUM |
| Deletion protection disabled for load balancer | CKV_AWS_113 | MEDIUM |
| Deletion protection disabled for load balancer | CKV_AWS_113 | MEDIUM |
| DocumentDB is not encrypted at rest | CKV_AWS_74 | MEDIUM |
| Dynamodb point in time recovery is not enabled for global tables | CKV_AWS_165 | MEDIUM |
| EC2 Auto Scaling groups are not utilizing EC2 launch templates | CKV_AWS_315 | MEDIUM |
| ECS Fargate services are not ensured to run on the latest Fargate platform version | CKV_AWS_332 | MEDIUM |
| ECS task definitions have their own unique process namespace or share the host's process namespace | CKV_AWS_335 | MEDIUM |
| Elasticsearch domains are not configured with a minimum of three dedicated master nodes | CKV_AWS_318 | MEDIUM |
| Glacier Vault access policy is public and not restricted to specific services or principals | CKV_AWS_167 | MEDIUM |
| Hard-coded secrets found in Parameter Store values | CKV_AWS_384 | MEDIUM |
| Neptune storage is not securely encrypted | CKV_AWS_44 | MEDIUM |
| Not all data stored in the EBS snapshot is securely encrypted | N/A | MEDIUM |
| QLDB ledger permissions mode is not set to STANDARD | CKV_AWS_170 | MEDIUM |
| RDS Aurora Clusters do not have backtracking enabled | CKV_AWS_326 | MEDIUM |
| Redshift clusters are not using enhanced VPC routing | CKV_AWS_321 | MEDIUM |
| Redshift clusters are not using the default database name. | CKV_AWS_320 | MEDIUM |
| Route53 A Record does not have Attached Resource | CKV2_AWS_23 | MEDIUM |
| Runtime of Lambda is deprecated | CKV_AWS_363 | MEDIUM |
| S3 lifecycle configuration does not set a period for aborting failed uploads | CKV_AWS_300 | MEDIUM |
| Session Manager data is not encrypted in transit | CKV_AWS_112 | MEDIUM |
| SNS topic policy is public and access is not restricted to specific services or principals | CKV_AWS_169 | MEDIUM |
| Timestream database is not encrypted with KMS CMK | CKV_AWS_160 | MEDIUM |
| User identity should be enforced by EFS access points | CKV_AWS_330 | MEDIUM |
| Workspace root volumes are not encrypted | CKV_AWS_156 | MEDIUM |
| Workspace user volumes are not encrypted | CKV_AWS_155 | MEDIUM |
| Alibaba Cloud MongoDB is not deployed inside a VPC | N/A | LOW |
| Amazon EFS does not have an AWS Backup backup plan | CKV2_AWS_18 | LOW |
| Autoscaling groups did not supply tags to launch configurations | CKV_AWS_153 | LOW |
| AWS ACM certificates does not have logging preference | CKV_AWS_234 | LOW |
| AWS all data stored in the Elasticsearch domain is not encrypted using a Customer Managed Key (CMK) | CKV_AWS_247 | LOW |
| AWS AMI copying does not use a Customer Managed Key (CMK) | CKV_AWS_236 | LOW |
| AWS AMI launch permissions are not limited | CKV_AWS_205 | LOW |
| AWS AMIs are not encrypted by Key Management Service (KMS) using Customer Managed Keys (CMKs) | CKV_AWS_204 | LOW |
| AWS API deployments do not enable Create before Destroy | CKV_AWS_217 | LOW |
| AWS API Gateway caching is disabled | CKV_AWS_120 | LOW |
| AWS API Gateway Domain does not use a modern security policy | CKV_AWS_206 | LOW |
| AWS API Gateway endpoints without client certificate authentication | CKV2_AWS_51 | LOW |
| AWS API Gateway method settings do not enable caching | CKV_AWS_225 | LOW |
| AWS API gateway request parameter is not validated | CKV2_AWS_53 | LOW |
| AWS App Flow connector profile does not use Customer Managed Keys (CMKs) | CKV_AWS_264 | LOW |
| AWS App Flow flow does not use Customer Managed Keys (CMKs) | CKV_AWS_263 | LOW |
| AWS Appsync API Cache is not encrypted at rest | CKV_AWS_214 | LOW |
| AWS Appsync API Cache is not encrypted in transit | CKV_AWS_215 | LOW |
| AWS AppSync is not protected by WAF | CKV2_AWS_33 | LOW |
| AWS AppSync's logging is disabled | CKV_AWS_193 | LOW |
| AWS Batch Job is defined as a privileged container | CKV_AWS_210 | LOW |
| AWS Bedrock agent is not associated with Bedrock guardrails | CKV_AWS_383 | LOW |
| AWS Cloudfront distribution is disabled | CKV_AWS_216 | LOW |
| AWS CloudFront response header policy does not enforce Strict Transport Security | CKV_AWS_259 | LOW |
| AWS Cloudsearch does not use HTTPs | CKV_AWS_220 | LOW |
| AWS Cloudsearch does not use the latest (Transport Layer Security) TLS | CKV_AWS_218 | LOW |
| AWS CloudTrail does not define an SNS Topic | CKV_AWS_252 | LOW |
| AWS CloudWatch Log groups encrypted using default encryption key instead of KMS CMK | CKV_AWS_158 | LOW |
| AWS cluster logging is not enabled or client to container communication not encrypted using a Customer Managed Key (CMK) | CKV_AWS_224 | LOW |
| AWS Code Artifact Domain is not encrypted by KMS using a Customer Managed Key (CMK) | CKV_AWS_221 | LOW |
| AWS Codecommit branch changes has less than 2 approvals | CKV_AWS_257 | LOW |
| AWS Codecommit is not associated with an approval rule | CKV2_AWS_37 | LOW |
| AWS CodeGuru Reviewer repository association does not use a Customer Managed Key (CMK) | CKV_AWS_381 | LOW |
| AWS CodePipeline artifactStore is not encrypted by Key Management Service (KMS) using a Customer Managed Key (CMK) | CKV_AWS_219 | LOW |
| AWS copied AMIs are not encrypted | CKV_AWS_235 | LOW |
| AWS DAX cluster endpoint does not use TLS (Transport Layer Security) | CKV_AWS_239 | LOW |
| AWS DB instance does not get all minor upgrades automatically | CKV_AWS_226 | LOW |
| AWS DLM cross-region events are not encrypted | CKV_AWS_253 | LOW |
| AWS DLM cross-region events are not encrypted with a Customer Managed Key (CMK) | CKV_AWS_254 | LOW |
| AWS DLM cross-region schedules are not encrypted using a Customer Managed Key (CMK) | CKV_AWS_256 | LOW |
| AWS DLM-cross region schedules are not encrypted | CKV_AWS_255 | LOW |
| AWS DMS replication instance automatic version upgrade disabled | CKV_AWS_222 | LOW |
| AWS Doc DB not encrypted using Customer Managed Key | CKV_AWS_182 | LOW |
| AWS DocumentDB clusters have backup retention period less than 7 days | CKV_AWS_360 | LOW |
| AWS EBS Snapshot Copy not encrypted using Customer Managed Key | CKV_AWS_183 | LOW |
| AWS EBS Volume is not encrypted by Key Management Service (KMS) using a Customer Managed Key (CMK) | CKV_AWS_212 | LOW |
| AWS EBS Volume not encrypted using Customer Managed Key | CKV_AWS_189 | LOW |
| AWS EBS volume region with encryption is disabled | CKV_AWS_106 | LOW |
| AWS ECS Cluster does not enable logging of ECS Exec | CKV_AWS_223 | LOW |
| AWS Elastic File System (EFS) is not encrypted using Customer Managed Key | CKV_AWS_184 | LOW |
| AWS Elastic File System (EFS) with encryption for data at rest is disabled | CKV_AWS_42 | LOW |
| AWS Elastic Load Balancer v2 with deletion protection feature disabled | CKV_AWS_150 | LOW |
| AWS ElastiCache Redis cluster with encryption for data at rest disabled | CKV_AWS_29 | LOW |
| AWS ElastiCache Redis cluster with in-transit encryption disabled (Replication group) | CKV_AWS_30 | LOW |
| AWS ElastiCache Redis cluster with Redis AUTH feature disabled | CKV_AWS_31 | LOW |
| AWS Elasticache replication group not configured with CMK key | CKV_AWS_191 | LOW |
| AWS Elasticsearch domain does not use an updated TLS policy | CKV_AWS_228 | LOW |
| AWS Elasticsearch domain has Dedicated master set to disabled | CKV2_AWS_59 | LOW |
| AWS EMR cluster is not configured with Kerberos Authentication | CKV_AWS_114 | LOW |
| AWS EMR cluster is not configured with SSE KMS for data at rest encryption (Amazon S3 with EMRFS) | CKV_AWS_171 | LOW |
| AWS EMR cluster is not enabled with data encryption in transit | CKV_AWS_351 | LOW |
| AWS EMR cluster is not enabled with local disk encryption | CKV_AWS_349 | LOW |
| AWS Execution Role ARN and Task Role ARN are different in ECS Task definitions | CKV_AWS_249 | LOW |
| AWS FSX openzfs is not encrypted by AWS' Key Management Service (KMS) using a Customer Managed Key (CMK) | CKV_AWS_203 | LOW |
| AWS FSX Windows filesystem not encrypted using Customer Managed Key | CKV_AWS_179 | LOW |
| AWS fx ontap file system not encrypted using Customer Managed Key | CKV_AWS_178 | LOW |
| AWS Glue component is not associated with a security configuration | CKV_AWS_195 | LOW |
| AWS HTTP and HTTPS target groups do not define health check | CKV_AWS_261 | LOW |
| AWS Image Builder component not encrypted using Customer Managed Key | CKV_AWS_180 | LOW |
| AWS Image Builder Distribution Configuration is not encrypting AMI by Key Management Service (KMS) using a Customer Managed Key (CMK) | CKV_AWS_199 | LOW |
| AWS Image Recipe EBS Disk are not encrypted using a Customer Managed Key (CMK) | CKV_AWS_200 | LOW |
| AWS Kendra index Server side encryption does not use Customer Managed Keys (CMKs) | CKV_AWS_262 | LOW |
| AWS Key Management Service (KMS) key is disabled | CKV_AWS_227 | LOW |
| AWS Keyspace Table does not use Customer Managed Keys (CMKs) | CKV_AWS_265 | LOW |
| AWS Kinesis Firehose Delivery Streams are not encrypted with CMK | CKV_AWS_241 | LOW |
| AWS Kinesis Firehose's delivery stream is not encrypted | CKV_AWS_240 | LOW |
| AWS Kinesis streams are not encrypted using Server Side Encryption | CKV_AWS_43 | LOW |
| AWS Kinesis streams encryption is using default KMS keys instead of Customer's Managed Master Keys | CKV_AWS_185 | LOW |
| AWS Kinesis Video Stream not encrypted using Customer Managed Key | CKV_AWS_177 | LOW |
| AWS Lambda Function is not assigned to access within VPC | CKV_AWS_117 | LOW |
| AWS Lambda function is not configured for a DLQ | CKV_AWS_116 | LOW |
| AWS Lambda function is not configured for function-level concurrent execution Limit | CKV_AWS_115 | LOW |
| AWS Lambda Function resource-based policy is overly permissive | CKV_AWS_301 | LOW |
| AWS lustre file system not configured with CMK key | CKV_AWS_190 | LOW |
| AWS MemoryDB data is not encrypted in transit | CKV_AWS_202 | LOW |
| AWS MemoryDB is not encrypted at rest by AWS' Key Management Service KMS using CMKs | CKV_AWS_201 | LOW |
| AWS MQ Broker is not encrypted by Customer Managed Key (CMK) | CKV_AWS_209 | LOW |
| AWS MQBroker audit logging is disabled | CKV_AWS_197 | LOW |
| AWS MQBroker version is not up to date | CKV_AWS_208 | LOW |
| AWS MQBroker's minor version updates are disabled | CKV_AWS_207 | LOW |
| AWS MWAA environment has scheduler logs disabled | CKV_AWS_242 | LOW |
| AWS MWAA environment has webserver logs disabled | CKV_AWS_244 | LOW |
| AWS MWAA environment has worker logs disabled | CKV_AWS_243 | LOW |
| AWS Postgres RDS have Query Logging disabled | CKV2_AWS_30 | LOW |
| AWS QLDB ledger has deletion protection is disabled | CKV_AWS_172 | LOW |
| AWS RDS Cluster activity streams are not encrypted by Key Management Service (KMS) using Customer Managed Keys (CMKs) | CKV_AWS_246 | LOW |
| AWS RDS DB cluster encryption is disabled | CKV_AWS_16 | LOW |
| AWS RDS DB snapshot does not use Customer Managed Keys (CMKs) | CKV_AWS_266 | LOW |
| AWS RDS DB snapshot is not encrypted | CKV_AWS_146 | LOW |
| AWS RDS does not use a modern CaCert | CKV_AWS_211 | LOW |
| AWS RDS instance without Automatic Backup setting | CKV_AWS_133 | LOW |
| AWS Redshift does not have require_ssl configured | CKV_AWS_105 | LOW |
| AWS Redshift instances are not encrypted | CKV_AWS_64 | LOW |
| AWS replicated backups are not encrypted at rest by Key Management Service (KMS) using a Customer Managed Key (CMK) | CKV_AWS_245 | LOW |
| AWS resources that support tags do not have Tags | N/A | LOW |
| AWS S3 bucket access control lists (ACLs) in use | CKV2_AWS_65 | LOW |
| AWS S3 bucket Object not encrypted using Customer Managed Key | CKV_AWS_186 | LOW |
| AWS S3 Object Copy not encrypted using Customer Managed Key | CKV_AWS_181 | LOW |
| AWS Sagemaker Data Quality Job not encrypting communications between instances used for monitoring jobs | CKV_AWS_369 | LOW |
| AWS Sagemaker data quality job not encrypting model artifacts with KMS | CKV_AWS_367 | LOW |
| AWS Sagemaker Data Quality Job not using KMS to encrypt data on attached storage volume | CKV_AWS_368 | LOW |
| AWS Sagemaker domain not encrypted using Customer Managed Key | CKV_AWS_187 | LOW |
| AWS SageMaker Flow Definition does not use KMS for output configurations | CKV_AWS_372 | LOW |
| AWS SageMaker notebook instance not configured with data encryption at rest using KMS key | CKV_AWS_22 | LOW |
| AWS Secret Manager Automatic Key Rotation is not enabled | CKV2_AWS_57 | LOW |
| AWS Secrets Manager secret not encrypted by Customer Managed Key (CMK) | CKV_AWS_149 | LOW |
| AWS SQS Queue not configured with server side encryption | CKV_AWS_27 | LOW |
| AWS SSM Parameter is not encrypted | CKV2_AWS_34 | LOW |
| AWS Terraform sends SSM secrets to untrusted domains over HTTP | CKV2_AWS_36 | LOW |
| AWS Transit Gateway auto accept vpc attachment is enabled | CKV_AWS_331 | LOW |
| Clusters of Neptune DB do not replicate tags to snapshots | CKV_AWS_362 | LOW |
| DocDB does not have audit logs enabled | CKV_AWS_104 | LOW |
| EBS does not have an AWS Backup backup plan | CKV2_AWS_9 | LOW |
| EC2 EBS is not optimized | CKV_AWS_135 | LOW |
| ECR image tags are not immutable | CKV_AWS_51 | LOW |
| Ensure AWS API gateway enables Create before Destroy | CKV_AWS_237 | LOW |
| GuardDuty is not enabled to specific org/region | CKV2_AWS_3 | LOW |
| Not only encrypted EBS volumes are attached to EC2 instances | CKV2_AWS_2 | LOW |
| RDS cluster is not configured to copy tags to snapshots | CKV_AWS_313 | LOW |
| RDS clusters do not have an AWS Backup backup plan | CKV2_AWS_8 | LOW |
| RDS instances do not have Multi-AZ enabled | CKV_AWS_157 | LOW |
| Redshift clusters version upgrade is not default | CKV_AWS_141 | LOW |
| S3 bucket cross-region replication disabled | CKV_AWS_144 | LOW |
| S3 bucket lock configuration disabled | CKV_AWS_143 | LOW |
| S3 buckets are not encrypted with KMS | CKV_AWS_145 | LOW |
| Unencrypted ECR repositories | CKV_AWS_136 | LOW |
| Unencrypted RDS global clusters | CKV_AWS_140 | LOW |
| WAF rule does not have any actions | CKV_AWS_342 | LOW |
| AWS AppSync has field-level logging disabled | CKV_AWS_194 | LOW |
| AWS CloudFront web distribution with AWS Web Application Firewall (AWS WAF) service disabled | CKV_AWS_68 | LOW |
| AWS CloudTrail logging is disabled | CKV_AWS_251 | LOW |
| AWS Config must record all possible resources | CKV2_AWS_48 | LOW |
| AWS Config Recording is disabled | CKV2_AWS_45 | LOW |
| AWS DAX cluster not configured with encryption at rest | CKV_AWS_47 | LOW |
| AWS DynamoDB encrypted using AWS owned CMK instead of AWS managed CMK | CKV_AWS_119 | LOW |
| AWS DynamoDB table Auto Scaling not enabled | CKV2_AWS_16 | LOW |
| AWS EC2 Auto Scaling Launch Configuration is not using encrypted EBS volumes | CKV_AWS_8 | LOW |
| AWS ECS task definition is not configured with read-only access to container root filesystems | CKV_AWS_336 | LOW |
| AWS Elastic Beanstalk environment managed platform updates are not enabled | CKV_AWS_340 | LOW |
| AWS ElastiCache Redis cluster automatic version upgrade disabled | CKV_AWS_322 | LOW |
| AWS ElastiCache Redis cluster is not configured with automatic backup | CKV_AWS_134 | LOW |
| AWS ElastiCache Redis cluster with Multi-AZ Automatic Failover feature set to disabled | CKV2_AWS_50 | LOW |
| AWS EMR cluster is not configured with security configuration | CKV2_AWS_55 | LOW |
| AWS GuardDuty detector is not enabled | CKV_AWS_238 | LOW |
| AWS Neptune cluster deletion protection is disabled | CKV2_AWS_58 | LOW |
| AWS Neptune DB clusters have backup retention period less than 7 days | CKV_AWS_361 | LOW |
| AWS RDS cluster delete protection is disabled | CKV_AWS_139 | LOW |
| AWS RDS DB cluster is encrypted using default KMS key instead of CMK | CKV_AWS_327 | LOW |
| AWS RDS instance with copy tags to snapshots disabled | CKV2_AWS_60 | LOW |
| AWS RDS Postgres Cluster does not have query logging enabled | CKV2_AWS_27 | LOW |
| AWS Redshift Cluster not encrypted using Customer Managed Key | CKV_AWS_142 | LOW |
| AWS SageMaker notebook instance with root access enabled | CKV_AWS_307 | LOW |
| AWS SQS queue access policy is overly permissive | CKV_AWS_387 | LOW |
| AWS SQS queue encryption using default KMS key instead of CMK | CKV2_AWS_73 | LOW |
| CloudTrail Event Data Store does not use Customer Managed Keys (CMKs) | CKV_AWS_294 | LOW |

## AWS Elasticsearch Policies

| Policy | Checkov ID | Severity |
|--------|-----------|----------|
| AWS Elasticsearch does not have node-to-node encryption enabled | CKV_AWS_6 | MEDIUM |
| AWS Elasticsearch domain is not configured with HTTPS | CKV_AWS_83 | MEDIUM |
| AWS Elasticsearch domain logging is not enabled | CKV_AWS_84 | MEDIUM |
| AWS Elasticsearch domain Encryption for data at rest is disabled | CKV_AWS_5 | LOW |

## AWS IAM Policies

| Policy | Checkov ID | Severity |
|--------|-----------|----------|
| AWS IAM policies that allow full \"*-*\" administrative privileges are created | CKV_AWS_62 | CRITICAL |
| AWS Access key enabled on root account | CKV_AWS_348 | HIGH |
| AWS AdministratorAccess policy is used by IAM roles, users, or groups | CKV_AWS_274 | HIGH |
| AWS GitHub Actions OIDC authorization policies allow for unsafe claims or claim order | CKV_AWS_358 | HIGH |
| AWS IAM password policy does allow password reuse | CKV_AWS_13 | HIGH |
| AWS IAM policy allows all principals used by any AWS service from target account to assume role | CKV_AWS_61 | HIGH |
| AWS IAM policy documents allow * (asterisk) as a statement's action | CKV_AWS_63 | HIGH |
| AWS IAM policy documents do not allow * (asterisk) as a statement's action | CKV_AWS_49 | HIGH |
| AWS IAM role allows all services or principals to be assumed | CKV_AWS_60 | HIGH |
| Data source IAM policy document allows all resources with restricted actions | CKV_AWS_356 | HIGH |
| IAM policies allow data exfiltration | CKV_AWS_288 | HIGH |
| IAM policies allow exposure of credentials | CKV_AWS_287 | HIGH |
| IAM policies allow permissions management or resource exposure without constraints | CKV_AWS_289 | HIGH |
| IAM policies allow write access without constraints | CKV_AWS_290 | HIGH |
| IAM Policy Document Allows All or Any AWS Principal Permissions to Resources | CKV_AWS_283 | HIGH |
| IAM policy document allows all resources with restricted actions | CKV_AWS_355 | HIGH |
| IAM policy uses the AWS AdministratorAccess policy | CKV_AWS_275 | HIGH |
| Permissions delegated to AWS services for AWS Lambda functions are not limited by SourceArn or SourceAccount | CKV_AWS_364 | HIGH |
| The AWS Managed IAMFullAccess IAM policy should not be used | CKV2_AWS_56 | HIGH |
| A Policy is not Defined for KMS Key | CKV2_AWS_64 | MEDIUM |
| Authorization type for API GatewayV2 routes is not specified | CKV_AWS_309 | MEDIUM |
| AWS Cognito identity pool allows unauthenticated guest access | CKV_AWS_366 | MEDIUM |
| AWS IAM policy allows full administrative privileges | CKV2_AWS_40 | MEDIUM |
| AWS IAM Policy permission may cause privilege escalation | CKV_AWS_286 | MEDIUM |
| AWS KMS Key policy overly permissive | CKV_AWS_33 | MEDIUM |
| AWS S3 buckets are accessible to any authenticated user | CKV2_AWS_43 | MEDIUM |
| IAM policies allow privilege escalation | CKV_AWS_110 | MEDIUM |
| IAM User has access to the console | CKV2_AWS_22 | MEDIUM |
| RDS database does not have IAM authentication enabled | CKV_AWS_161 | MEDIUM |
| Access is not controlled through Single Sign-On (SSO) | CKV_AWS_273 | LOW |
| AWS Cloudfront Distribution with S3 have Origin Access set to disabled | CKV2_AWS_46 | LOW |
| AWS Execution Role ARN and Task Role ARN are different in ECS Task definitions | CKV_AWS_249 | LOW |
| AWS IAM password policy does not have a number | CKV_AWS_12 | LOW |
| AWS IAM policies that allow full administrative privileges are created | CKV_AWS_1 | LOW |
| AWS IAM policy attached to users | CKV_AWS_40 | LOW |
| AWS Neptune Cluster not configured with IAM authentication | CKV_AWS_359 | LOW |
| AWS OpenSearch Fine-grained access control is disabled | CKV2_AWS_52 | LOW |
| AWS RDS cluster not configured with IAM authentication | CKV_AWS_162 | LOW |
| Credentials exposure actions return credentials in an API response | CKV_AWS_107 | LOW |
| Data exfiltration allowed without resource constraints | CKV_AWS_108 | LOW |
| IAM authentication for Amazon RDS clusters is disabled | CKV_AWS_128 | LOW |
| Not all IAM users are members of at least one IAM group | CKV2_AWS_21 | LOW |
| Resource exposure allows modification of policies and exposes resources | CKV_AWS_109 | LOW |
| Respective logs of Amazon RDS are disabled | CKV_AWS_129 | LOW |
| Write access allowed without constraint | CKV_AWS_111 | LOW |
| AWS EC2 Instance IAM Role not enabled | CKV2_AWS_41 | LOW |
| AWS IAM group not in use | CKV2_AWS_14 | LOW |
| AWS IAM password policy does not expire in 90 days | CKV_AWS_9 | LOW |
| AWS IAM password policy does not have a lowercase character | CKV_AWS_11 | LOW |
| AWS IAM password policy does not have a minimum of 14 characters | CKV_AWS_10 | LOW |
| AWS IAM password policy does not have a symbol | CKV_AWS_14 | LOW |
| AWS IAM password policy does not have an uppercase character | CKV_AWS_15 | LOW |
| SQS policy allows all actions | CKV_AWS_72 | LOW |

## AWS Kubernetes Policies

| Policy | Checkov ID | Severity |
|--------|-----------|----------|
| AWS EKS node group have implicit SSH access from 0.0.0.0/0 | CKV_AWS_100 | HIGH |
| EKS clusters are not running on a supported Kubernetes version | CKV_AWS_339 | HIGH |
| AWS EKS cluster does not have secrets encryption enabled | CKV_AWS_58 | MEDIUM |
| AWS EKS cluster endpoint access publicly enabled | CKV_AWS_39 | LOW |
| AWS EKS cluster security group overly permissive to all traffic | CKV_AWS_38 | LOW |
| AWS EKS control plane logging disabled | CKV_AWS_37 | LOW |

## AWS Logging Policies

| Policy | Checkov ID | Severity |
|--------|-----------|----------|
| Neptune logging is not enabled | CKV_AWS_101 | HIGH |
| Amazon MQ Broker logging is not enabled | CKV_AWS_48 | MEDIUM |
| Amazon MSK cluster logging is not enabled | CKV_AWS_80 | MEDIUM |
| An S3 bucket must have a lifecycle configuration | CKV2_AWS_61 | MEDIUM |
| AWS config is not enabled in all regions | CKV_AWS_121 | MEDIUM |
| AWS DocumentDB logging is not enabled | CKV_AWS_85 | MEDIUM |
| AWS EC2 instance detailed monitoring disabled | CKV_AWS_126 | MEDIUM |
| Elasticsearch Domain Audit Logging is disabled | CKV_AWS_317 | MEDIUM |
| Execution history logging is not enabled on the State Machine | CKV_AWS_285 | MEDIUM |
| RDS Cluster log capture is disabled | CKV_AWS_324 | MEDIUM |
| API Gateway does not have access logging enabled | CKV_AWS_76 | LOW |
| API Gateway does not have X-Ray tracing enabled | CKV_AWS_73 | LOW |
| API Gateway stage does not have logging level defined appropriately | CKV2_AWS_4 | LOW |
| AWS Amazon RDS instances Enhanced Monitoring is disabled | CKV_AWS_118 | LOW |
| AWS API Gateway V2 has Access Logging is disabled | CKV_AWS_95 | LOW |
| AWS CloudFormation stack configured without SNS topic | CKV_AWS_124 | LOW |
| AWS CloudTrail log validation is not enabled in all regions | CKV_AWS_36 | LOW |
| AWS CloudWatch Log groups not configured with definite retention days | CKV_AWS_66 | LOW |
| AWS ECS cluster with container insights feature disabled | CKV_AWS_65 | LOW |
| AWS ECS services have automatic public IP address assignment enabled | CKV_AWS_333 | LOW |
| AWS Postgres RDS have Query Logging disabled | CKV2_AWS_30 | LOW |
| AWS WAF Web Access Control Lists logging is disabled | CKV_AWS_176 | LOW |
| AWS WAF2 does not have a Logging Configuration | CKV2_AWS_31 | LOW |
| Data Trace is not enabled in the API Gateway Method Settings | CKV_AWS_276 | LOW |
| Domain Name System (DNS) query logging is not enabled for Amazon Route 53 hosted zones | CKV2_AWS_39 | LOW |
| Global Accelerator does not have Flow logs enabled | CKV_AWS_75 | LOW |
| RDS Cluster audit logging for MySQL engine is disabled | CKV_AWS_325 | LOW |
| RDS instances have performance insights disabled | CKV_AWS_353 | LOW |
| S3 buckets do not have event notifications enabled | CKV2_AWS_62 | LOW |
| State machine does not have X-ray tracing enabled | CKV_AWS_284 | LOW |
| AWS CloudFront distribution with access logging disabled | CKV_AWS_86 | LOW |
| AWS CloudTrail is not enabled with multi trail and not capturing all management events | CKV_AWS_67 | LOW |
| AWS CloudTrail logs are not encrypted using Customer Master Keys (CMKs) | CKV_AWS_35 | LOW |
| AWS CloudTrail trail logs is not integrated with CloudWatch Log | CKV2_AWS_10 | LOW |
| AWS CloudWatch log groups retention set to less than 365 days | CKV_AWS_338 | LOW |
| AWS CodeBuild project not configured with logging configuration | CKV_AWS_314 | LOW |
| AWS Customer Master Key (CMK) rotation is not enabled | CKV_AWS_7 | LOW |
| AWS Elastic Load Balancer (Classic) with access log disabled | CKV_AWS_92 | LOW |
| AWS Elastic Load Balancer v2 (ELBv2) with access log disabled | CKV_AWS_91 | LOW |
| AWS Network Firewall is not configured with logging configuration | CKV2_AWS_63 | LOW |
| AWS Redshift database does not have audit logging enabled | CKV_AWS_71 | LOW |
| AWS VPC Flow Logs not enabled | CKV2_AWS_11 | LOW |

## AWS Networking Policies

| Policy | Checkov ID | Severity |
|--------|-----------|----------|
| ALB is not configured with the defensive or strictest desync mitigation mode | CKV_AWS_328 | HIGH |
| Domain Name System Security Extensions (DNSSEC) signing is not enabled for Amazon Route 53 public hosted zones | CKV2_AWS_38 | HIGH |
| MSK nodes are not private | CKV_AWS_291 | HIGH |
| MWAA environment is publicly accessible | CKV2_AWS_66 | HIGH |
| NACL ingress allows all ports | CKV_AWS_352 | HIGH |
| WAF enables message lookup in Log4j2 | CKV_AWS_192 | HIGH |
| ALB does not drop HTTP headers | CKV_AWS_131 | MEDIUM |
| AWS API Gateway method lacking authorization or API keys | CKV2_AWS_70 | MEDIUM |
| AWS CloudFront distribution is using insecure SSL protocols for HTTPS communication | CKV2_AWS_54 | MEDIUM |
| AWS CloudFront origin protocol policy does not enforce HTTPS-only | CKV2_AWS_72 | MEDIUM |
| AWS CloudFront viewer protocol policy is not configured with HTTPS | CKV_AWS_34 | MEDIUM |
| AWS Elastic Load Balancer v2 (ELBv2) listener that allow connection requests over HTTP | CKV_AWS_2 | MEDIUM |
| AWS Lambda function URL having overly permissive cross-origin resource sharing permissions | CKV2_AWS_75 | MEDIUM |
| AWS Load Balancer uses HTTP protocol | CKV_AWS_378 | MEDIUM |
| AWS RDS database instance not configured with encryption in transit | CKV2_AWS_69 | MEDIUM |
| AWS S3 bucket not configured with secure data transport policy | CKV_AWS_379 | MEDIUM |
| AWS SageMaker model does not use network isolation | CKV_AWS_370 | MEDIUM |
| AWS SageMaker notebook instance IAM policy is overly permissive | CKV2_AWS_68 | MEDIUM |
| AWS Security Group allows all traffic on all ports | CKV_AWS_277 | MEDIUM |
| AWS Transfer Server is publicly exposed | CKV_AWS_164 | MEDIUM |
| DocDB TLS is disabled | CKV_AWS_90 | MEDIUM |
| Public API gateway not configured with AWS Web Application Firewall v2 (AWS WAFv2) | CKV2_AWS_29 | MEDIUM |
| TLS not enforced in SES configuration set | CKV_AWS_365 | MEDIUM |
| ALB does not redirect HTTP requests into HTTPS ones | CKV2_AWS_20 | LOW |
| Amazon EMR clusters' security groups are open to the world | CKV2_AWS_7 | LOW |
| Auto scaling groups associated with a load balancer do not use elastic load balancing health checks | CKV2_AWS_15 | LOW |
| AWS ACM certificate does not enable Create before Destroy | CKV_AWS_233 | LOW |
| AWS ACM Certificate with wildcard domain name | CKV2_AWS_71 | LOW |
| AWS Application Load Balancer (ALB) not configured with AWS Web Application Firewall v2 (AWS WAFv2) | CKV2_AWS_28 | LOW |
| AWS CloudFront distribution does not have a strict security headers policy attached | CKV2_AWS_32 | LOW |
| AWS CloudFront web distribution using insecure TLS version | CKV_AWS_174 | LOW |
| AWS CloudFront web distribution with default SSL certificate | CKV2_AWS_42 | LOW |
| AWS CloudFront web distribution with geo restriction disabled | CKV_AWS_374 | LOW |
| AWS Database Migration Service endpoint do not have SSL configured | CKV2_AWS_49 | LOW |
| AWS Default Security Group does not restrict all traffic | CKV2_AWS_12 | LOW |
| AWS Elastic Load Balancer (Classic) with cross-zone load balancing disabled | CKV_AWS_138 | LOW |
| AWS Elastic Load Balancer with listener TLS/SSL is not configured | CKV_AWS_376 | LOW |
| AWS Elasticache security groups are not defined | CKV_AWS_196 | LOW |
| AWS Elasticsearch is not configured inside a VPC | CKV_AWS_137 | LOW |
| AWS Elasticsearch uses the default security group | CKV_AWS_248 | LOW |
| AWS ELB Policy uses some unsecure protocols | CKV_AWS_213 | LOW |
| AWS Load Balancers do not use strong ciphers | CKV2_AWS_74 | LOW |
| AWS NACL allows ingress from 0.0.0.0/0 to port 20 | CKV_AWS_230 | LOW |
| AWS NACL allows ingress from 0.0.0.0/0 to port 21 | CKV_AWS_229 | LOW |
| AWS NACL allows ingress from 0.0.0.0/0 to port 22 | CKV_AWS_232 | LOW |
| AWS NACL allows ingress from 0.0.0.0/0 to port 3389 | CKV_AWS_231 | LOW |
| AWS NAT Gateways are not utilized for the default route | CKV2_AWS_35 | LOW |
| AWS RDS security groups are not defined | CKV_AWS_198 | LOW |
| AWS Redshift cluster is publicly accessible | CKV_AWS_87 | LOW |
| AWS route table with VPC peering overly permissive to all traffic | CKV2_AWS_44 | LOW |
| AWS S3 bucket has global view ACL permissions enabled | CKV_AWS_375 | LOW |
| AWS SageMaker notebook instance configured with direct internet access feature | CKV_AWS_122 | LOW |
| AWS Security Group allows unrestricted egress traffic | CKV_AWS_382 | LOW |
| AWS security groups allow ingress from 0.0.0.0/0 to port 80 | CKV_AWS_260 | LOW |
| AWS Transfer Server not using latest Security Policy | CKV_AWS_380 | LOW |
| AWS VPC subnets should not allow automatic public IP assignment | CKV_AWS_130 | LOW |
| AWS WAF does not have associated rules | CKV_AWS_175 | LOW |
| Default VPC is planned to be provisioned | CKV_AWS_148 | LOW |
| ElastiCache cluster is using the default subnet group | CKV_AWS_323 | LOW |
| Not all EIP addresses allocated to a VPC are attached to EC2 instances | CKV2_AWS_19 | LOW |
| Not every Security Group rule has a description | CKV_AWS_23 | LOW |
| Redshift is deployed outside of a VPC | CKV_AWS_154 | LOW |
| Route 53 domains do not have transfer lock protection | CKV_AWS_377 | LOW |
| S3 Bucket does not have public access blocks | CKV2_AWS_6 | LOW |
| Security Groups are not attached to EC2 instances or ENIs | CKV2_AWS_5 | LOW |
| VPC endpoint service is not configured for manual acceptance | CKV_AWS_123 | LOW |
| AWS Elastic Load Balancer v2 (ELBv2) with cross-zone load balancing disabled | CKV_AWS_152 | LOW |
| AWS Network ACL is not in use | CKV2_AWS_1 | LOW |
| AWS SageMaker notebook instance is not placed in VPC | CKV_AWS_306 | LOW |
| AWS Security Group allows all traffic on RDP port (3389) | CKV_AWS_25 | LOW |
| AWS Security Group allows all traffic on SSH port (22) | CKV_AWS_24 | LOW |

## AWS Public Policies

| Policy | Checkov ID | Severity |
|--------|-----------|----------|
| AWS EC2 instances with public IP and associated with security groups have Internet access | CKV_AWS_88 | HIGH |
| AWS Private ECR repository policy is overly permissive | CKV_AWS_32 | MEDIUM |
| AWS RDS database instance is publicly accessible | CKV_AWS_17 | MEDIUM |
| AWS Redshift cluster instance with public access setting enabled | CKV_AWS_87 | MEDIUM |
| AWS API gateway methods are publicly accessible | CKV_AWS_59 | LOW |
| AWS DMS replication instance is publicly accessible | CKV_AWS_89 | LOW |
| AWS MQ is publicly accessible | CKV_AWS_69 | LOW |

## AWS S3 Policies

| Policy | Checkov ID | Severity |
|--------|-----------|----------|
| Bucket ACL grants WRITE permission to AWS users | N/A | CRITICAL |
| AWS S3 bucket ACL grants READ permission to everyone | CKV_AWS_20 | HIGH |
| AWS S3 Bucket has an ACL defined which allows public WRITE access | CKV_AWS_57 | HIGH |
| AWS S3 Bucket BlockPublicPolicy is not set to True | CKV_AWS_54 | MEDIUM |
| AWS S3 bucket IgnorePublicAcls is not set to True | CKV_AWS_55 | MEDIUM |
| AWS S3 bucket policy overly permissive to any principal | CKV_AWS_70 | MEDIUM |
| AWS S3 bucket RestrictPublicBucket is not set to True | CKV_AWS_56 | MEDIUM |
| AWS S3 Buckets has block public access setting disabled | CKV_AWS_53 | MEDIUM |
| S3 bucket policy allows lockout all but root user | CKV_AWS_93 | MEDIUM |
| AWS S3 buckets do not have server side encryption | CKV_AWS_19 | LOW |
| AWS S3 Object Versioning is disabled | CKV_AWS_21 | LOW |
| AWS Access logging not enabled on S3 buckets | CKV_AWS_18 | LOW |

## AWS Secrets Policies

| Policy | Checkov ID | Severity |
|--------|-----------|----------|
| AWS access keys and secrets are hard coded in infrastructure | CKV_AWS_41 | HIGH |
| EC2 user data exposes secrets | CKV_AWS_46 | HIGH |
| Lambda function's environment variables expose secrets | CKV_AWS_45 | MEDIUM |

## AWS Serverless Policies

| Policy | Checkov ID | Severity |
|--------|-----------|----------|
| AWS Lambda encryption settings environmental variable is not set properly | CKV_AWS_173 | LOW |
| AWS Lambda functions with tracing not enabled | CKV_AWS_50 | LOW |

## AWS Supply Chain Policies

| Policy | Checkov ID | Severity |
|--------|-----------|----------|
| Potential WhoAMI name confusion attack exposure | CKV_AWS_386 | LOW |
