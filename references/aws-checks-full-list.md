# Checkov AWS Checks - Full Reference List

Total unique AWS checks: 456

Generated from: checkov v3.2.526 (Terraform + CloudFormation)

> This file is for OFFLINE REFERENCE only. NOT loaded into context.
> Checkov runtime uses ALL checks automatically during full scan.

---

## CKV_AWS_* Checks (384 checks)

| Check ID | Description | Severity |
|----------|-------------|----------|
| CKV_AWS_1 | Ensure IAM policies that allow full "*-*" administrative privileges are not created | CRITICAL |
| CKV_AWS_2 | Ensure ALB protocol is HTTPS | HIGH |
| CKV_AWS_3 | Ensure all data stored in the EBS is securely encrypted | HIGH |
| CKV_AWS_5 | Ensure all data stored in the Elasticsearch is securely encrypted at rest | HIGH |
| CKV_AWS_6 | Ensure all Elasticsearch has node-to-node encryption enabled | HIGH |
| CKV_AWS_7 | Ensure rotation for customer created CMKs is enabled | HIGH |
| CKV_AWS_8 | Ensure all data stored in the Launch configuration or instance Elastic Blocks Store is securely encrypted | HIGH |
| CKV_AWS_9 | Ensure IAM password policy expires passwords within 90 days or less | HIGH |
| CKV_AWS_10 | Ensure IAM password policy requires minimum length of 14 or greater | MEDIUM |
| CKV_AWS_11 | Ensure IAM password policy requires at least one lowercase letter | MEDIUM |
| CKV_AWS_12 | Ensure IAM password policy requires at least one number | MEDIUM |
| CKV_AWS_13 | Ensure IAM password policy prevents password reuse | MEDIUM |
| CKV_AWS_14 | Ensure IAM password policy requires at least one symbol | MEDIUM |
| CKV_AWS_15 | Ensure IAM password policy requires at least one uppercase letter | MEDIUM |
| CKV_AWS_16 | Ensure all data stored in the RDS is securely encrypted at rest | HIGH |
| CKV_AWS_17 | Ensure all data stored in RDS is not publicly accessible | CRITICAL |
| CKV_AWS_18 | Ensure the S3 bucket has access logging enabled | HIGH |
| CKV_AWS_19 | Ensure all data stored in the S3 bucket is securely encrypted at rest | HIGH |
| CKV_AWS_20 | S3 Bucket has an ACL defined which allows public READ access. | CRITICAL |
| CKV_AWS_21 | Ensure all data stored in the S3 bucket have versioning enabled | MEDIUM |
| CKV_AWS_22 | Ensure SageMaker Notebook is encrypted at rest using KMS CMK | LOW |
| CKV_AWS_23 | Ensure every security group and rule has a description | LOW |
| CKV_AWS_24 | Ensure no security groups allow ingress from 0.0.0.0:0 to port 22 | CRITICAL |
| CKV_AWS_25 | Ensure no security groups allow ingress from 0.0.0.0:0 to port 3389 | CRITICAL |
| CKV_AWS_26 | Ensure all data stored in the SNS topic is encrypted | HIGH |
| CKV_AWS_27 | Ensure all data stored in the SQS queue is encrypted | HIGH |
| CKV_AWS_28 | Ensure DynamoDB point in time recovery (backup) is enabled | MEDIUM |
| CKV_AWS_29 | Ensure all data stored in the ElastiCache Replication Group is securely encrypted at rest | HIGH |
| CKV_AWS_30 | Ensure all data stored in the ElastiCache Replication Group is securely encrypted at transit | HIGH |
| CKV_AWS_31 | Ensure all data stored in the ElastiCache Replication Group is securely encrypted at transit and has auth token | HIGH |
| CKV_AWS_32 | Ensure ECR policy is not set to public | CRITICAL |
| CKV_AWS_33 | Ensure KMS key policy does not contain wildcard (*) principal | HIGH |
| CKV_AWS_34 | Ensure CloudFront distribution ViewerProtocolPolicy is set to HTTPS | HIGH |
| CKV_AWS_35 | Ensure CloudTrail logs are encrypted at rest using KMS CMKs | HIGH |
| CKV_AWS_36 | Ensure CloudTrail log file validation is enabled | HIGH |
| CKV_AWS_37 | Ensure Amazon EKS control plane logging is enabled for all log types | HIGH |
| CKV_AWS_38 | Ensure Amazon EKS public endpoint not accessible to 0.0.0.0/0 | HIGH |
| CKV_AWS_39 | Ensure Amazon EKS public endpoint disabled | HIGH |
| CKV_AWS_40 | Ensure IAM policies are attached only to groups or roles (Reducing access management complexity may in-turn reduce opportunity for a principal to inadvertently receive or retain excessive privileges.) | HIGH |
| CKV_AWS_41 | Ensure no hard coded AWS access key and secret key exists in provider | CRITICAL |
| CKV_AWS_42 | Ensure EFS is securely encrypted | HIGH |
| CKV_AWS_43 | Ensure Kinesis Stream is securely encrypted | HIGH |
| CKV_AWS_44 | Ensure Neptune storage is securely encrypted | HIGH |
| CKV_AWS_45 | Ensure no hard-coded secrets exist in lambda environment | CRITICAL |
| CKV_AWS_46 | Ensure no hard-coded secrets exist in EC2 user data | CRITICAL |
| CKV_AWS_47 | Ensure DAX is encrypted at rest (default is unencrypted) | HIGH |
| CKV_AWS_48 | Ensure MQ Broker logging is enabled | HIGH |
| CKV_AWS_49 | Ensure no IAM policies documents allow "*" as a statement's actions | HIGH |
| CKV_AWS_50 | X-Ray tracing is enabled for Lambda | MEDIUM |
| CKV_AWS_51 | Ensure ECR Image Tags are immutable | MEDIUM |
| CKV_AWS_53 | Ensure S3 bucket has block public ACLS enabled | CRITICAL |
| CKV_AWS_54 | Ensure S3 bucket has block public policy enabled | CRITICAL |
| CKV_AWS_55 | Ensure S3 bucket has ignore public ACLs enabled | CRITICAL |
| CKV_AWS_56 | Ensure S3 bucket has 'restrict_public_buckets' enabled | CRITICAL |
| CKV_AWS_57 | S3 Bucket has an ACL defined which allows public WRITE access. | CRITICAL |
| CKV_AWS_58 | Ensure EKS Cluster has Secrets Encryption Enabled | HIGH |
| CKV_AWS_59 | Ensure there is no open access to back-end resources through API | MEDIUM |
| CKV_AWS_60 | Ensure IAM role allows only specific services or principals to assume it | HIGH |
| CKV_AWS_61 | Ensure AWS IAM policy does not allow assume role permission across all services | HIGH |
| CKV_AWS_62 | Ensure IAM policies that allow full "*-*" administrative privileges are not created | CRITICAL |
| CKV_AWS_63 | Ensure no IAM policies documents allow "*" as a statement's actions | HIGH |
| CKV_AWS_64 | Ensure all data stored in the Redshift cluster is securely encrypted at rest | HIGH |
| CKV_AWS_65 | Ensure container insights are enabled on ECS cluster | MEDIUM |
| CKV_AWS_66 | Ensure that CloudWatch Log Group specifies retention days | MEDIUM |
| CKV_AWS_67 | Ensure CloudTrail is enabled in all Regions | HIGH |
| CKV_AWS_68 | CloudFront Distribution should have WAF enabled | HIGH |
| CKV_AWS_69 | Ensure MQ Broker is not publicly exposed | CRITICAL |
| CKV_AWS_70 | Ensure S3 bucket does not allow an action with any Principal | CRITICAL |
| CKV_AWS_71 | Ensure Redshift Cluster logging is enabled | HIGH |
| CKV_AWS_72 | Ensure SQS policy does not allow ALL (*) actions. | MEDIUM |
| CKV_AWS_73 | Ensure API Gateway has X-Ray Tracing enabled | MEDIUM |
| CKV_AWS_74 | Ensure DocumentDB is encrypted at rest (default is unencrypted) | HIGH |
| CKV_AWS_75 | Ensure Global Accelerator accelerator has flow logs enabled | HIGH |
| CKV_AWS_76 | Ensure API Gateway has Access Logging enabled | HIGH |
| CKV_AWS_77 | Ensure Athena Database is encrypted at rest (default is unencrypted) | HIGH |
| CKV_AWS_78 | Ensure that CodeBuild Project encryption is not disabled | MEDIUM |
| CKV_AWS_79 | Ensure Instance Metadata Service Version 1 is not enabled | HIGH |
| CKV_AWS_80 | Ensure MSK Cluster logging is enabled | HIGH |
| CKV_AWS_81 | Ensure MSK Cluster encryption in rest and transit is enabled | MEDIUM |
| CKV_AWS_82 | Ensure Athena Workgroup should enforce configuration to prevent client disabling encryption | MEDIUM |
| CKV_AWS_83 | Ensure Elasticsearch Domain enforces HTTPS | HIGH |
| CKV_AWS_84 | Ensure Elasticsearch Domain Logging is enabled | HIGH |
| CKV_AWS_85 | Ensure DocumentDB Logging is enabled | HIGH |
| CKV_AWS_86 | Ensure CloudFront distribution has Access Logging enabled | HIGH |
| CKV_AWS_87 | Redshift cluster should not be publicly accessible | CRITICAL |
| CKV_AWS_88 | EC2 instance should not have public IP. | CRITICAL |
| CKV_AWS_89 | DMS replication instance should not be publicly accessible | CRITICAL |
| CKV_AWS_90 | Ensure DocumentDB TLS is not disabled | HIGH |
| CKV_AWS_91 | Ensure the ELBv2 (Application/Network) has access logging enabled | MEDIUM |
| CKV_AWS_92 | Ensure the ELB has access logging enabled | MEDIUM |
| CKV_AWS_93 | Ensure S3 bucket policy does not lockout all but root user. (Prevent lockouts needing root account fixes) | CRITICAL |
| CKV_AWS_94 | Ensure Glue Data Catalog Encryption is enabled | HIGH |
| CKV_AWS_95 | Ensure API Gateway V2 has Access Logging enabled | HIGH |
| CKV_AWS_96 | Ensure all data stored in Aurora is securely encrypted at rest | HIGH |
| CKV_AWS_97 | Ensure Encryption in transit is enabled for EFS volumes in ECS Task definitions | HIGH |
| CKV_AWS_98 | Ensure all data stored in the Sagemaker Endpoint is securely encrypted at rest | HIGH |
| CKV_AWS_99 | Ensure Glue Security Configuration Encryption is enabled | HIGH |
| CKV_AWS_100 | Ensure AWS EKS node group does not have implicit SSH access from 0.0.0.0/0 | HIGH |
| CKV_AWS_101 | Ensure Neptune logging is enabled | HIGH |
| CKV_AWS_102 | Ensure Neptune Cluster instance is not publicly available | CRITICAL |
| CKV_AWS_103 | Ensure that load balancer is using at least TLS 1.2 | HIGH |
| CKV_AWS_104 | Ensure DocumentDB has audit logs enabled | MEDIUM |
| CKV_AWS_105 | Ensure Redshift uses SSL | HIGH |
| CKV_AWS_106 | Ensure EBS default encryption is enabled | HIGH |
| CKV_AWS_107 | Ensure IAM policies does not allow credentials exposure | HIGH |
| CKV_AWS_108 | Ensure IAM policies does not allow data exfiltration | HIGH |
| CKV_AWS_109 | Ensure IAM policies does not allow permissions management / resource exposure without constraints | HIGH |
| CKV_AWS_110 | Ensure IAM policies does not allow privilege escalation | HIGH |
| CKV_AWS_111 | Ensure IAM policies does not allow write access without constraints | HIGH |
| CKV_AWS_112 | Ensure Session Manager data is encrypted in transit | HIGH |
| CKV_AWS_113 | Ensure Session Manager logs are enabled and encrypted | MEDIUM |
| CKV_AWS_114 | Ensure that EMR clusters with Kerberos have Kerberos Realm set | MEDIUM |
| CKV_AWS_115 | Ensure that AWS Lambda function is configured for function-level concurrent execution limit | MEDIUM |
| CKV_AWS_116 | Ensure that AWS Lambda function is configured for a Dead Letter Queue(DLQ) | MEDIUM |
| CKV_AWS_117 | Ensure that AWS Lambda function is configured inside a VPC | MEDIUM |
| CKV_AWS_118 | Ensure that enhanced monitoring is enabled for Amazon RDS instances | MEDIUM |
| CKV_AWS_119 | Ensure DynamoDB Tables are encrypted using a KMS Customer Managed CMK | LOW |
| CKV_AWS_120 | Ensure API Gateway caching is enabled | MEDIUM |
| CKV_AWS_121 | Ensure AWS Config is enabled in all regions | HIGH |
| CKV_AWS_122 | Ensure that direct internet access is disabled for an Amazon SageMaker Notebook Instance | MEDIUM |
| CKV_AWS_123 | Ensure that VPC Endpoint Service is configured for Manual Acceptance | MEDIUM |
| CKV_AWS_124 | Ensure that CloudFormation stacks are sending event notifications to an SNS topic | MEDIUM |
| CKV_AWS_126 | Ensure that detailed monitoring is enabled for EC2 instances | MEDIUM |
| CKV_AWS_127 | Ensure that Elastic Load Balancer(s) uses SSL certificates provided by AWS Certificate Manager | HIGH |
| CKV_AWS_129 | Ensure that respective logs of Amazon Relational Database Service (Amazon RDS) are enabled | MEDIUM |
| CKV_AWS_130 | Ensure VPC subnets do not assign public IP by default | HIGH |
| CKV_AWS_131 | Ensure that ALB drops HTTP headers | MEDIUM |
| CKV_AWS_133 | Ensure that RDS instances has backup policy | MEDIUM |
| CKV_AWS_134 | Ensure that Amazon ElastiCache Redis clusters have automatic backup turned on | MEDIUM |
| CKV_AWS_135 | Ensure that EC2 is EBS optimized | MEDIUM |
| CKV_AWS_136 | Ensure that ECR repositories are encrypted using KMS | LOW |
| CKV_AWS_137 | Ensure that Elasticsearch is configured inside a VPC | MEDIUM |
| CKV_AWS_138 | Ensure that ELB is cross-zone-load-balancing enabled | MEDIUM |
| CKV_AWS_139 | Ensure that RDS clusters have deletion protection enabled | MEDIUM |
| CKV_AWS_140 | Ensure that RDS global clusters are encrypted | HIGH |
| CKV_AWS_141 | Ensured that Redshift cluster allowing version upgrade by default | MEDIUM |
| CKV_AWS_142 | Ensure that Redshift cluster is encrypted by KMS | MEDIUM |
| CKV_AWS_143 | Ensure that S3 bucket has lock configuration enabled by default | HIGH |
| CKV_AWS_144 | Ensure that S3 bucket has cross-region replication enabled | MEDIUM |
| CKV_AWS_145 | Ensure that S3 buckets are encrypted with KMS by default | LOW |
| CKV_AWS_146 | Ensure that RDS database cluster snapshot is encrypted | MEDIUM |
| CKV_AWS_147 | Ensure that CodeBuild projects are encrypted using CMK | LOW |
| CKV_AWS_148 | Ensure no default VPC is planned to be provisioned | MEDIUM |
| CKV_AWS_149 | Ensure that Secrets Manager secret is encrypted using KMS CMK | LOW |
| CKV_AWS_150 | Ensure that Load Balancer has deletion protection enabled | MEDIUM |
| CKV_AWS_152 | Ensure that Load Balancer (Network/Gateway) has cross-zone load balancing enabled | MEDIUM |
| CKV_AWS_153 | Autoscaling groups should supply tags to launch configurations | LOW |
| CKV_AWS_154 | Ensure Redshift is not deployed outside of a VPC | MEDIUM |
| CKV_AWS_155 | Ensure that Workspace user volumes are encrypted | MEDIUM |
| CKV_AWS_156 | Ensure that Workspace root volumes are encrypted | MEDIUM |
| CKV_AWS_157 | Ensure that RDS instances have Multi-AZ enabled | MEDIUM |
| CKV_AWS_158 | Ensure that CloudWatch Log Group is encrypted by KMS | LOW |
| CKV_AWS_159 | Ensure that Athena Workgroup is encrypted | MEDIUM |
| CKV_AWS_160 | Ensure that Timestream database is encrypted with KMS CMK | LOW |
| CKV_AWS_161 | Ensure RDS database has IAM authentication enabled | MEDIUM |
| CKV_AWS_162 | Ensure RDS cluster has IAM authentication enabled | MEDIUM |
| CKV_AWS_163 | Ensure ECR image scanning on push is enabled | MEDIUM |
| CKV_AWS_164 | Ensure Transfer Server is not exposed publicly. | CRITICAL |
| CKV_AWS_165 | Ensure DynamoDB point in time recovery (backup) is enabled for global tables | MEDIUM |
| CKV_AWS_166 | Ensure Backup Vault is encrypted at rest using KMS CMK | LOW |
| CKV_AWS_167 | Ensure Glacier Vault access policy is not public by only allowing specific services or principals to access it | MEDIUM |
| CKV_AWS_168 | Ensure SQS queue policy is not public by only allowing specific services or principals to access it | MEDIUM |
| CKV_AWS_169 | Ensure SNS topic policy is not public by only allowing specific services or principals to access it | MEDIUM |
| CKV_AWS_170 | Ensure QLDB ledger permissions mode is set to STANDARD | MEDIUM |
| CKV_AWS_171 | Ensure EMR Cluster security configuration encryption is using SSE-KMS | MEDIUM |
| CKV_AWS_172 | Ensure QLDB ledger has deletion protection enabled | MEDIUM |
| CKV_AWS_173 | Check encryption settings for Lambda environmental variable | HIGH |
| CKV_AWS_174 | Verify CloudFront Distribution Viewer Certificate is using TLS v1.2 or higher | HIGH |
| CKV_AWS_175 | Ensure WAF has associated rules | MEDIUM |
| CKV_AWS_176 | Ensure Logging is enabled for WAF Web Access Control Lists | HIGH |
| CKV_AWS_177 | Ensure Kinesis Video Stream is encrypted by KMS using a customer managed Key (CMK) | LOW |
| CKV_AWS_178 | Ensure fx ontap file system is encrypted by KMS using a customer managed Key (CMK) | LOW |
| CKV_AWS_179 | Ensure FSX Windows filesystem is encrypted by KMS using a customer managed Key (CMK) | LOW |
| CKV_AWS_180 | Ensure Image Builder component is encrypted by KMS using a customer managed Key (CMK) | LOW |
| CKV_AWS_181 | Ensure S3 Object Copy is encrypted by KMS using a customer managed Key (CMK) | LOW |
| CKV_AWS_182 | Ensure DocumentDB is encrypted by KMS using a customer managed Key (CMK) | LOW |
| CKV_AWS_183 | Ensure EBS Snapshot Copy is encrypted by KMS using a customer managed Key (CMK) | LOW |
| CKV_AWS_184 | Ensure resource is encrypted by KMS using a customer managed Key (CMK) | LOW |
| CKV_AWS_185 | Ensure Kinesis Stream is encrypted by KMS using a customer managed Key (CMK) | LOW |
| CKV_AWS_186 | Ensure S3 bucket Object is encrypted by KMS using a customer managed Key (CMK) | LOW |
| CKV_AWS_187 | Ensure Sagemaker domain and notebook instance are encrypted by KMS using a customer managed Key (CMK) | LOW |
| CKV_AWS_189 | Ensure EBS Volume is encrypted by KMS using a customer managed Key (CMK) | LOW |
| CKV_AWS_190 | Ensure lustre file systems is encrypted by KMS using a customer managed Key (CMK) | LOW |
| CKV_AWS_191 | Ensure ElastiCache replication group is encrypted by KMS using a customer managed Key (CMK) | MEDIUM |
| CKV_AWS_192 | Ensure WAF prevents message lookup in Log4j2. See CVE-2021-44228 aka log4jshell | HIGH |
| CKV_AWS_193 | Ensure AppSync has Logging enabled | HIGH |
| CKV_AWS_194 | Ensure AppSync has Field-Level logs enabled | MEDIUM |
| CKV_AWS_195 | Ensure Glue component has a security configuration associated | MEDIUM |
| CKV_AWS_196 | Ensure no aws_elasticache_security_group resources exist | MEDIUM |
| CKV_AWS_197 | Ensure MQ Broker Audit logging is enabled | HIGH |
| CKV_AWS_198 | Ensure no aws_db_security_group resources exist | MEDIUM |
| CKV_AWS_199 | Ensure Image Builder Distribution Configuration encrypts AMI's using KMS - a customer managed Key (CMK) | LOW |
| CKV_AWS_200 | Ensure that Image Recipe EBS Disk are encrypted with CMK | LOW |
| CKV_AWS_201 | Ensure MemoryDB is encrypted at rest using KMS CMKs | LOW |
| CKV_AWS_202 | Ensure MemoryDB data is encrypted in transit | HIGH |
| CKV_AWS_203 | Ensure resource is encrypted by KMS using a customer managed Key (CMK) | LOW |
| CKV_AWS_204 | Ensure AMIs are encrypted using KMS CMKs | LOW |
| CKV_AWS_205 | Ensure to Limit AMI launch Permissions | MEDIUM |
| CKV_AWS_206 | Ensure API Gateway Domain uses a modern security Policy | MEDIUM |
| CKV_AWS_207 | Ensure MQ Broker minor version updates are enabled | MEDIUM |
| CKV_AWS_208 | Ensure MQ Broker version is current | MEDIUM |
| CKV_AWS_209 | Ensure MQ broker encrypted by KMS using a customer managed Key (CMK) | LOW |
| CKV_AWS_210 | Batch job does not define a privileged container | MEDIUM |
| CKV_AWS_211 | Ensure RDS uses a modern CaCert | MEDIUM |
| CKV_AWS_212 | Ensure DMS replication instance is encrypted by KMS using a customer managed Key (CMK) | LOW |
| CKV_AWS_213 | Ensure ELB Policy uses only secure protocols | MEDIUM |
| CKV_AWS_214 | Ensure AppSync API Cache is encrypted at rest | HIGH |
| CKV_AWS_215 | Ensure AppSync API Cache is encrypted in transit | HIGH |
| CKV_AWS_216 | Ensure CloudFront distribution is enabled | MEDIUM |
| CKV_AWS_217 | Ensure Create before destroy for API deployments | LOW |
| CKV_AWS_218 | Ensure that CloudSearch is using latest TLS | HIGH |
| CKV_AWS_219 | Ensure CodePipeline Artifact store is using a KMS CMK | LOW |
| CKV_AWS_220 | Ensure that CloudSearch is using https | HIGH |
| CKV_AWS_221 | Ensure CodeArtifact Domain is encrypted by KMS using a customer managed Key (CMK) | LOW |
| CKV_AWS_222 | Ensure DMS replication instance gets all minor upgrade automatically | MEDIUM |
| CKV_AWS_223 | Ensure ECS Cluster enables logging of ECS Exec | MEDIUM |
| CKV_AWS_224 | Ensure ECS Cluster logging is enabled and client to container communication uses CMK | LOW |
| CKV_AWS_225 | Ensure API Gateway method setting caching is enabled | MEDIUM |
| CKV_AWS_226 | Ensure DB instance gets all minor upgrades automatically | MEDIUM |
| CKV_AWS_227 | Ensure KMS key is enabled | MEDIUM |
| CKV_AWS_228 | Verify Elasticsearch domain is using an up to date TLS policy | HIGH |
| CKV_AWS_229 | Ensure no NACL allow ingress from 0.0.0.0:0 to port 21 | HIGH |
| CKV_AWS_230 | Ensure no NACL allow ingress from 0.0.0.0:0 to port 20 | HIGH |
| CKV_AWS_231 | Ensure no NACL allow ingress from 0.0.0.0:0 to port 3389 | HIGH |
| CKV_AWS_232 | Ensure no NACL allow ingress from 0.0.0.0:0 to port 22 | HIGH |
| CKV_AWS_233 | Ensure Create before destroy for ACM certificates | LOW |
| CKV_AWS_234 | Verify logging preference for ACM certificates | MEDIUM |
| CKV_AWS_235 | Ensure that copied AMIs are encrypted | MEDIUM |
| CKV_AWS_236 | Ensure AMI copying uses a CMK | LOW |
| CKV_AWS_237 | Ensure Create before destroy for API Gateway | LOW |
| CKV_AWS_238 | Ensure that GuardDuty detector is enabled | HIGH |
| CKV_AWS_239 | Ensure DAX cluster endpoint is using TLS | HIGH |
| CKV_AWS_240 | Ensure Kinesis Firehose delivery stream is encrypted | MEDIUM |
| CKV_AWS_241 | Ensure that Kinesis Firehose Delivery Streams are encrypted with CMK | LOW |
| CKV_AWS_242 | Ensure MWAA environment has scheduler logs enabled | MEDIUM |
| CKV_AWS_243 | Ensure MWAA environment has worker logs enabled | MEDIUM |
| CKV_AWS_244 | Ensure MWAA environment has webserver logs enabled | MEDIUM |
| CKV_AWS_245 | Ensure replicated backups are encrypted at rest using KMS CMKs | LOW |
| CKV_AWS_246 | Ensure RDS Cluster activity streams are encrypted using KMS CMKs | LOW |
| CKV_AWS_247 | Ensure all data stored in the Elasticsearch is encrypted with a CMK | LOW |
| CKV_AWS_248 | Ensure that Elasticsearch is not using the default Security Group | MEDIUM |
| CKV_AWS_249 | Ensure that the Execution Role ARN and the Task Role ARN are different in ECS Task definitions | MEDIUM |
| CKV_AWS_250 | Ensure that RDS PostgreSQL instances use a non vulnerable version with the log_fdw extension (https://aws.amazon.com/security/security-bulletins/AWS-2022-004/) | HIGH |
| CKV_AWS_251 | Ensure CloudTrail logging is enabled | HIGH |
| CKV_AWS_252 | Ensure CloudTrail defines an SNS Topic | HIGH |
| CKV_AWS_253 | Ensure DLM cross region events are encrypted | MEDIUM |
| CKV_AWS_254 | Ensure DLM cross region events are encrypted with Customer Managed Key | LOW |
| CKV_AWS_255 | Ensure DLM cross region schedules are encrypted | MEDIUM |
| CKV_AWS_256 | Ensure DLM cross region schedules are encrypted using a Customer Managed Key | LOW |
| CKV_AWS_257 | Ensure CodeCommit branch changes have at least 2 approvals | MEDIUM |
| CKV_AWS_258 | Ensure that Lambda function URLs AuthType is not None | HIGH |
| CKV_AWS_259 | Ensure CloudFront response header policy enforces Strict Transport Security | MEDIUM |
| CKV_AWS_260 | Ensure no security groups allow ingress from 0.0.0.0:0 to port 80 | HIGH |
| CKV_AWS_261 | Ensure HTTP HTTPS Target group defines Healthcheck | HIGH |
| CKV_AWS_262 | Ensure Kendra index Server side encryption uses CMK | LOW |
| CKV_AWS_263 | Ensure AppFlow flow uses CMK | LOW |
| CKV_AWS_264 | Ensure AppFlow connector profile uses CMK | LOW |
| CKV_AWS_265 | Ensure Keyspaces Table uses CMK | LOW |
| CKV_AWS_266 | Ensure DB Snapshot copy uses CMK | LOW |
| CKV_AWS_267 | Ensure that Comprehend Entity Recognizer's model is encrypted by KMS using a customer managed Key (CMK) | LOW |
| CKV_AWS_268 | Ensure that Comprehend Entity Recognizer's volume is encrypted by KMS using a customer managed Key (CMK) | LOW |
| CKV_AWS_269 | Ensure Connect Instance Kinesis Video Stream Storage Config uses CMK | LOW |
| CKV_AWS_270 | Ensure Connect Instance S3 Storage Config uses CMK | LOW |
| CKV_AWS_271 | Ensure DynamoDB table replica KMS encryption uses CMK | LOW |
| CKV_AWS_272 | Ensure AWS Lambda function is configured to validate code-signing | MEDIUM |
| CKV_AWS_273 | Ensure access is controlled through SSO and not AWS IAM defined users | HIGH |
| CKV_AWS_274 | Disallow IAM roles, users, and groups from using the AWS AdministratorAccess policy | CRITICAL |
| CKV_AWS_275 | Disallow policies from using the AWS AdministratorAccess policy | CRITICAL |
| CKV_AWS_276 | Ensure Data Trace is not enabled in API Gateway Method Settings | MEDIUM |
| CKV_AWS_277 | Ensure no security groups allow ingress from 0.0.0.0:0 to port -1 | CRITICAL |
| CKV_AWS_278 | Ensure MemoryDB snapshot is encrypted by KMS using a customer managed Key (CMK) | LOW |
| CKV_AWS_279 | Ensure Neptune snapshot is securely encrypted | HIGH |
| CKV_AWS_280 | Ensure Neptune snapshot is encrypted by KMS using a customer managed Key (CMK) | LOW |
| CKV_AWS_281 | Ensure RedShift snapshot copy is encrypted by KMS using a customer managed Key (CMK) | LOW |
| CKV_AWS_282 | Ensure that Redshift Serverless namespace is encrypted by KMS using a customer managed key (CMK) | LOW |
| CKV_AWS_283 | Ensure no IAM policies documents allow ALL or any AWS principal permissions to the resource | CRITICAL |
| CKV_AWS_284 | Ensure State Machine has X-Ray tracing enabled | MEDIUM |
| CKV_AWS_285 | Ensure State Machine has execution history logging enabled | HIGH |
| CKV_AWS_286 | Ensure IAM policies does not allow privilege escalation | HIGH |
| CKV_AWS_287 | Ensure IAM policies does not allow credentials exposure | HIGH |
| CKV_AWS_288 | Ensure IAM policies does not allow data exfiltration | HIGH |
| CKV_AWS_289 | Ensure IAM policies does not allow permissions management / resource exposure without constraints | HIGH |
| CKV_AWS_290 | Ensure IAM policies does not allow write access without constraints | HIGH |
| CKV_AWS_291 | Ensure MSK nodes are private | HIGH |
| CKV_AWS_292 | Ensure DocumentDB Global Cluster is encrypted at rest (default is unencrypted) | HIGH |
| CKV_AWS_293 | Ensure that AWS database instances have deletion protection enabled | MEDIUM |
| CKV_AWS_294 | Ensure CloudTrail Event Data Store uses CMK | LOW |
| CKV_AWS_295 | Ensure DataSync Location Object Storage doesn't expose secrets | CRITICAL |
| CKV_AWS_296 | Ensure DMS endpoint uses Customer Managed Key (CMK) | LOW |
| CKV_AWS_297 | Ensure EventBridge Scheduler Schedule uses Customer Managed Key (CMK) | LOW |
| CKV_AWS_298 | Ensure DMS S3 uses Customer Managed Key (CMK) | LOW |
| CKV_AWS_300 | Ensure S3 lifecycle configuration sets period for aborting failed uploads | MEDIUM |
| CKV_AWS_301 | Ensure that AWS Lambda function is not publicly accessible | CRITICAL |
| CKV_AWS_302 | Ensure DB Snapshots are not Public | CRITICAL |
| CKV_AWS_303 | Ensure SSM documents are not Public | CRITICAL |
| CKV_AWS_304 | Ensure Secrets Manager secrets should be rotated within 90 days | MEDIUM |
| CKV_AWS_305 | Ensure CloudFront distribution has a default root object configured | MEDIUM |
| CKV_AWS_306 | Ensure SageMaker notebook instances should be launched into a custom VPC | MEDIUM |
| CKV_AWS_307 | Ensure SageMaker Users should not have root access to SageMaker notebook instances | MEDIUM |
| CKV_AWS_308 | Ensure API Gateway method setting caching is set to encrypted | MEDIUM |
| CKV_AWS_309 | Ensure API GatewayV2 routes specify an authorization type | MEDIUM |
| CKV_AWS_310 | Ensure CloudFront distributions should have origin failover configured | MEDIUM |
| CKV_AWS_311 | Ensure that CodeBuild S3 logs are encrypted | MEDIUM |
| CKV_AWS_312 | Ensure Elastic Beanstalk environments have enhanced health reporting enabled | MEDIUM |
| CKV_AWS_313 | Ensure RDS cluster configured to copy tags to snapshots | MEDIUM |
| CKV_AWS_314 | Ensure CodeBuild project environments have a logging configuration | MEDIUM |
| CKV_AWS_315 | Ensure EC2 Auto Scaling groups use EC2 launch templates | MEDIUM |
| CKV_AWS_316 | Ensure CodeBuild project environments do not have privileged mode enabled | MEDIUM |
| CKV_AWS_317 | Ensure Elasticsearch Domain Audit Logging is enabled | HIGH |
| CKV_AWS_318 | Ensure Elasticsearch domains are configured with at least three dedicated master nodes for HA | MEDIUM |
| CKV_AWS_319 | Ensure that CloudWatch alarm actions are enabled | MEDIUM |
| CKV_AWS_320 | Ensure Redshift clusters do not use the default database name | LOW |
| CKV_AWS_321 | Ensure Redshift clusters use enhanced VPC routing | MEDIUM |
| CKV_AWS_322 | Ensure ElastiCache for Redis cache clusters have auto minor version upgrades enabled | MEDIUM |
| CKV_AWS_323 | Ensure ElastiCache clusters do not use the default subnet group | LOW |
| CKV_AWS_324 | Ensure that RDS Cluster log capture is enabled | MEDIUM |
| CKV_AWS_325 | Ensure that RDS Cluster audit logging is enabled for MySQL engine | HIGH |
| CKV_AWS_326 | Ensure that RDS Aurora Clusters have backtracking enabled | MEDIUM |
| CKV_AWS_327 | Ensure RDS Clusters are encrypted using KMS CMKs | LOW |
| CKV_AWS_328 | Ensure that ALB is configured with defensive or strictest desync mitigation mode | MEDIUM |
| CKV_AWS_329 | EFS access points should enforce a root directory | LOW |
| CKV_AWS_330 | EFS access points should enforce a user identity | LOW |
| CKV_AWS_331 | Ensure Transit Gateways do not automatically accept VPC attachment requests | MEDIUM |
| CKV_AWS_332 | Ensure ECS Fargate services run on the latest Fargate platform version | MEDIUM |
| CKV_AWS_333 | Ensure ECS services do not have public IP addresses assigned to them automatically | HIGH |
| CKV_AWS_334 | Ensure ECS containers should run as non-privileged | MEDIUM |
| CKV_AWS_335 | Ensure ECS task definitions should not share the host's process namespace | MEDIUM |
| CKV_AWS_336 | Ensure ECS containers are limited to read-only access to root filesystems | MEDIUM |
| CKV_AWS_337 | Ensure SSM parameters are using KMS CMK | LOW |
| CKV_AWS_338 | Ensure CloudWatch log groups retains logs for at least 1 year | MEDIUM |
| CKV_AWS_339 | Ensure EKS clusters run on a supported Kubernetes version | MEDIUM |
| CKV_AWS_340 | Ensure Elastic Beanstalk managed platform updates are enabled | MEDIUM |
| CKV_AWS_341 | Ensure Launch template should not have a metadata response hop limit greater than 1 | MEDIUM |
| CKV_AWS_342 | Ensure WAF rule has any actions | MEDIUM |
| CKV_AWS_343 | Ensure Amazon Redshift clusters should have automatic snapshots enabled | MEDIUM |
| CKV_AWS_344 | Ensure that Network firewalls have deletion protection enabled | MEDIUM |
| CKV_AWS_345 | Ensure that Network firewall encryption is via a CMK | LOW |
| CKV_AWS_346 | Ensure Network Firewall Policy defines an encryption configuration that uses a customer managed Key (CMK) | LOW |
| CKV_AWS_347 | Ensure Neptune is encrypted by KMS using a customer managed Key (CMK) | LOW |
| CKV_AWS_348 | Ensure IAM root user does not have Access keys | CRITICAL |
| CKV_AWS_349 | Ensure EMR Cluster security configuration encrypts local disks | MEDIUM |
| CKV_AWS_350 | Ensure EMR Cluster security configuration encrypts EBS disks | MEDIUM |
| CKV_AWS_351 | Ensure EMR Cluster security configuration encrypts InTransit | MEDIUM |
| CKV_AWS_352 | Ensure NACL ingress does not allow all Ports | HIGH |
| CKV_AWS_353 | Ensure that RDS instances have performance insights enabled | MEDIUM |
| CKV_AWS_354 | Ensure RDS Performance Insights are encrypted using KMS CMKs | MEDIUM |
| CKV_AWS_355 | Ensure no IAM policies documents allow "*" as a statement's resource for restrictable actions | HIGH |
| CKV_AWS_356 | Ensure no IAM policies documents allow "*" as a statement's resource for restrictable actions | HIGH |
| CKV_AWS_357 | Ensure Transfer Server allows only secure protocols | MEDIUM |
| CKV_AWS_358 | Ensure AWS GitHub Actions OIDC authorization policies only allow safe claims and claim order | MEDIUM |
| CKV_AWS_359 | Neptune DB clusters should have IAM database authentication enabled | MEDIUM |
| CKV_AWS_360 | Ensure DocumentDB has an adequate backup retention period | MEDIUM |
| CKV_AWS_361 | Ensure that Neptune DB cluster has automated backups enabled with adequate retention | MEDIUM |
| CKV_AWS_362 | Neptune DB clusters should be configured to copy tags to snapshots | MEDIUM |
| CKV_AWS_363 | Ensure Lambda Runtime is not deprecated | MEDIUM |
| CKV_AWS_364 | Ensure that AWS Lambda function permissions delegated to AWS services are limited by SourceArn or SourceAccount | MEDIUM |
| CKV_AWS_365 | Ensure SES Configuration Set enforces TLS usage | HIGH |
| CKV_AWS_366 | Ensure AWS Cognito identity pool does not allow unauthenticated guest access | HIGH |
| CKV_AWS_367 | Ensure Amazon Sagemaker Data Quality Job uses KMS to encrypt model artifacts | MEDIUM |
| CKV_AWS_368 | Ensure Amazon Sagemaker Data Quality Job uses KMS to encrypt data on attached storage volume | MEDIUM |
| CKV_AWS_369 | Ensure Amazon Sagemaker Data Quality Job encrypts all communications between instances used for monitoring jobs | MEDIUM |
| CKV_AWS_370 | Ensure Amazon SageMaker model uses network isolation | MEDIUM |
| CKV_AWS_371 | Ensure Amazon SageMaker Notebook Instance only allows for IMDSv2 | MEDIUM |
| CKV_AWS_372 | Ensure Amazon SageMaker Flow Definition uses KMS for output configurations | MEDIUM |
| CKV_AWS_373 | Ensure Bedrock Agent is encrypted with a CMK | LOW |
| CKV_AWS_374 | Ensure AWS CloudFront web distribution has geo restriction enabled | MEDIUM |
| CKV_AWS_375 | Ensure AWS S3 bucket does not have global view ACL permissions enabled | MEDIUM |
| CKV_AWS_376 | Ensure AWS Elastic Load Balancer listener uses TLS/SSL | HIGH |
| CKV_AWS_377 | Ensure Route 53 domains have transfer lock protection | MEDIUM |
| CKV_AWS_378 | Ensure AWS Load Balancer doesn't use HTTP protocol | MEDIUM |
| CKV_AWS_379 | Ensure AWS S3 bucket is configured with secure data transport policy | MEDIUM |
| CKV_AWS_380 | Ensure AWS Transfer Server uses latest Security Policy | MEDIUM |
| CKV_AWS_381 | Make sure that aws_codegurureviewer_repository_association has a CMK | LOW |
| CKV_AWS_382 | Ensure no security groups allow egress from 0.0.0.0:0 to port -1 | HIGH |
| CKV_AWS_383 | Ensure AWS Bedrock agent is associated with Bedrock guardrails | MEDIUM |
| CKV_AWS_384 | Ensure no hard-coded secrets exist in Parameter Store values | CRITICAL |
| CKV_AWS_385 | Ensure AWS SNS topic policies do not allow cross-account access | MEDIUM |
| CKV_AWS_386 | Reduce potential for WhoAMI cloud image name confusion attack | MEDIUM |
| CKV_AWS_387 | Ensure SQS policy does not allow public access through wildcards | CRITICAL |
| CKV_AWS_388 | Ensure AWS Aurora PostgreSQL is not exposed to local file read vulnerability | MEDIUM |
| CKV_AWS_389 | Ensure AWS Auto Scaling group launch configuration doesn't have public IP address assignment enabled | HIGH |
| CKV_AWS_390 | Ensure AWS EMR block public access setting is enabled | MEDIUM |
| CKV_AWS_391 | Avoid AWS Redshift cluster with commonly used master username and public access setting enabled | MEDIUM |
| CKV_AWS_392 | Ensure AWS S3 access point block public access setting is enabled | MEDIUM |

## CKV2_AWS_* Checks (72 graph-based checks)

| Check ID | Description | Severity |
|----------|-------------|----------|
| CKV2_AWS_1 | Ensure that all NACL are attached to subnets | MEDIUM |
| CKV2_AWS_2 | Ensure that only encrypted EBS volumes are attached to EC2 instances | MEDIUM |
| CKV2_AWS_3 | Ensure GuardDuty is enabled to specific org/region | HIGH |
| CKV2_AWS_4 | Ensure API Gateway stage have logging level defined as appropriate | MEDIUM |
| CKV2_AWS_5 | Ensure that Security Groups are attached to another resource | MEDIUM |
| CKV2_AWS_6 | Ensure that S3 bucket has a Public Access block | CRITICAL |
| CKV2_AWS_7 | Ensure that Amazon EMR clusters' security groups are not open to the world | MEDIUM |
| CKV2_AWS_8 | Ensure that RDS clusters has backup plan of AWS Backup | MEDIUM |
| CKV2_AWS_9 | Ensure that EBS are added in the backup plans of AWS Backup | MEDIUM |
| CKV2_AWS_10 | Ensure CloudTrail trails are integrated with CloudWatch Logs | HIGH |
| CKV2_AWS_11 | Ensure VPC flow logging is enabled in all VPCs | HIGH |
| CKV2_AWS_12 | Ensure the default security group of every VPC restricts all traffic | HIGH |
| CKV2_AWS_14 | Ensure that IAM groups includes at least one IAM user | LOW |
| CKV2_AWS_15 | Ensure that auto Scaling groups that are associated with a load balancer are using Elastic Load Balancing health checks. | MEDIUM |
| CKV2_AWS_16 | Ensure that Auto Scaling is enabled on your DynamoDB tables | MEDIUM |
| CKV2_AWS_18 | Ensure that Elastic File System (Amazon EFS) file systems are added in the backup plans of AWS Backup | MEDIUM |
| CKV2_AWS_19 | Ensure that all EIP addresses allocated to a VPC are attached to EC2 instances | MEDIUM |
| CKV2_AWS_20 | Ensure that ALB redirects HTTP requests into HTTPS ones | MEDIUM |
| CKV2_AWS_21 | Ensure that all IAM users are members of at least one IAM group. | LOW |
| CKV2_AWS_22 | Ensure an IAM User does not have access to the console | LOW |
| CKV2_AWS_23 | Route53 A Record has Attached Resource | MEDIUM |
| CKV2_AWS_27 | Ensure Postgres RDS as aws_rds_cluster has Query Logging enabled | HIGH |
| CKV2_AWS_28 | Ensure public facing ALB are protected by WAF | MEDIUM |
| CKV2_AWS_29 | Ensure public API gateway are protected by WAF | MEDIUM |
| CKV2_AWS_30 | Ensure Postgres RDS as aws_db_instance has Query Logging enabled | HIGH |
| CKV2_AWS_31 | Ensure WAF2 has a Logging Configuration | MEDIUM |
| CKV2_AWS_32 | Ensure CloudFront distribution has a response headers policy attached | MEDIUM |
| CKV2_AWS_33 | Ensure AppSync is protected by WAF | MEDIUM |
| CKV2_AWS_34 | AWS SSM Parameter should be Encrypted | LOW |
| CKV2_AWS_35 | AWS NAT Gateways should be utilized for the default route | MEDIUM |
| CKV2_AWS_36 | Ensure terraform is not sending SSM secrets to untrusted domains over HTTP | MEDIUM |
| CKV2_AWS_37 | Ensure CodeCommit associates an approval rule | MEDIUM |
| CKV2_AWS_38 | Ensure Domain Name System Security Extensions (DNSSEC) signing is enabled for Amazon Route 53 public hosted zones | MEDIUM |
| CKV2_AWS_39 | Ensure Domain Name System (DNS) query logging is enabled for Amazon Route 53 hosted zones | HIGH |
| CKV2_AWS_40 | Ensure AWS IAM policy does not allow full IAM privileges | CRITICAL |
| CKV2_AWS_41 | Ensure an IAM role is attached to EC2 instance | MEDIUM |
| CKV2_AWS_42 | Ensure AWS CloudFront distribution uses custom SSL certificate | HIGH |
| CKV2_AWS_43 | Ensure S3 Bucket does not allow access to all Authenticated users | CRITICAL |
| CKV2_AWS_44 | Ensure AWS route table with VPC peering does not contain routes overly permissive to all traffic | MEDIUM |
| CKV2_AWS_45 | Ensure AWS Config recorder is enabled to record all supported resources | HIGH |
| CKV2_AWS_46 | Ensure AWS CloudFront Distribution with S3 have Origin Access set to enabled | MEDIUM |
| CKV2_AWS_47 | Ensure AWS CloudFront attached WAFv2 WebACL is configured with AMR for Log4j Vulnerability | HIGH |
| CKV2_AWS_48 | Ensure AWS Config must record all possible resources | MEDIUM |
| CKV2_AWS_49 | Ensure AWS Database Migration Service endpoints have SSL configured | HIGH |
| CKV2_AWS_50 | Ensure AWS ElastiCache Redis cluster with Multi-AZ Automatic Failover feature set to enabled | MEDIUM |
| CKV2_AWS_51 | Ensure AWS API Gateway endpoints uses client certificate authentication | MEDIUM |
| CKV2_AWS_52 | Ensure AWS ElasticSearch/OpenSearch Fine-grained access control is enabled | MEDIUM |
| CKV2_AWS_53 | Ensure AWS API gateway request is validated | MEDIUM |
| CKV2_AWS_54 | Ensure AWS CloudFront distribution is using secure SSL protocols for HTTPS communication | HIGH |
| CKV2_AWS_55 | Ensure AWS EMR cluster is configured with security configuration | MEDIUM |
| CKV2_AWS_56 | Ensure AWS Managed IAMFullAccess IAM policy is not used. | CRITICAL |
| CKV2_AWS_57 | Ensure Secrets Manager secrets should have automatic rotation enabled | MEDIUM |
| CKV2_AWS_58 | Ensure AWS Neptune cluster deletion protection is enabled | MEDIUM |
| CKV2_AWS_59 | Ensure ElasticSearch/OpenSearch has dedicated master node enabled | MEDIUM |
| CKV2_AWS_60 | Ensure RDS instance with copy tags to snapshots is enabled | MEDIUM |
| CKV2_AWS_61 | Ensure that an S3 bucket has a lifecycle configuration | MEDIUM |
| CKV2_AWS_62 | Ensure S3 buckets should have event notifications enabled | MEDIUM |
| CKV2_AWS_63 | Ensure Network firewall has logging configuration defined | MEDIUM |
| CKV2_AWS_64 | Ensure KMS key Policy is defined | HIGH |
| CKV2_AWS_65 | Ensure access control lists for S3 buckets are disabled | MEDIUM |
| CKV2_AWS_66 | Ensure MWAA environment is not publicly accessible | CRITICAL |
| CKV2_AWS_68 | Ensure SageMaker notebook instance IAM policy is not overly permissive | MEDIUM |
| CKV2_AWS_69 | Ensure AWS RDS database instance configured with encryption in transit | MEDIUM |
| CKV2_AWS_70 | Ensure API gateway method has authorization or API key set | MEDIUM |
| CKV2_AWS_71 | Ensure AWS ACM Certificate domain name does not include wildcards | MEDIUM |
| CKV2_AWS_72 | Ensure AWS CloudFront origin protocol policy enforces HTTPS-only | HIGH |
| CKV2_AWS_73 | Ensure AWS SQS uses CMK not AWS default keys for encryption | LOW |
| CKV2_AWS_74 | Ensure AWS Load Balancers use strong ciphers | MEDIUM |
| CKV2_AWS_75 | Ensure no open CORS policy | MEDIUM |
| CKV2_AWS_76 | Ensure AWS ALB attached WAFv2 WebACL is configured with AMR for Log4j Vulnerability | HIGH |
| CKV2_AWS_77 | Ensure AWS API Gateway Rest API attached WAFv2 WebACL is configured with AMR for Log4j Vulnerability | HIGH |
| CKV2_AWS_78 | Ensure AWS AppSync attached WAFv2 WebACL is configured with AMR for Log4j Vulnerability | HIGH |
