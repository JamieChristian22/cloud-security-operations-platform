resource "aws_vpc" "this" { cidr_block=var.vpc_cidr enable_dns_support=true enable_dns_hostnames=true tags=merge(var.tags,{Name="${var.name}-vpc"}) }
resource "aws_subnet" "private" { for_each=var.private_subnets vpc_id=aws_vpc.this.id cidr_block=each.value.cidr availability_zone=each.value.az map_public_ip_on_launch=false tags=merge(var.tags,{Name="${var.name}-${each.key}"}) }
resource "aws_security_group" "workload" { name="${var.name}-workload" description="Private workload security group" vpc_id=aws_vpc.this.id egress { from_port=443 to_port=443 protocol="tcp" cidr_blocks=["0.0.0.0/0"] } tags=var.tags }
resource "aws_s3_bucket" "audit" { bucket_prefix="${var.name}-audit-" force_destroy=true tags=merge(var.tags,{Purpose="SecurityAudit"}) }
resource "aws_s3_bucket_public_access_block" "audit" { bucket=aws_s3_bucket.audit.id block_public_acls=true block_public_policy=true ignore_public_acls=true restrict_public_buckets=true }
resource "aws_s3_bucket_versioning" "audit" { bucket=aws_s3_bucket.audit.id versioning_configuration { status="Enabled" } }
resource "aws_s3_bucket_server_side_encryption_configuration" "audit" { bucket=aws_s3_bucket.audit.id rule { apply_server_side_encryption_by_default { sse_algorithm="AES256" } } }
resource "aws_s3_bucket_lifecycle_configuration" "audit" { bucket=aws_s3_bucket.audit.id rule { id="retain-audit" status="Enabled" expiration { days=var.log_retention_days } } }
