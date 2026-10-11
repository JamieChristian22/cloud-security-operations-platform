resource "aws_vpc" "this" {
  cidr_block           = var.vpc_cidr
  enable_dns_support   = true
  enable_dns_hostnames = true
  tags = merge(var.tags, {
    Name = "${var.name}-vpc"
  })
}
resource "aws_subnet" "private" {
  for_each                = var.private_subnets
  vpc_id                  = aws_vpc.this.id
  cidr_block              = each.value.cidr
  availability_zone       = each.value.az
  map_public_ip_on_launch = false
  tags = merge(var.tags, {
    Name = "${var.name}-${each.key}"
  })
}
resource "aws_security_group" "workload" {
  #checkov:skip=CKV2_AWS_5:LAB-002: reusable foundation has no workload instances; attach the group during workload deployment.
  name        = "${var.name}-workload"
  description = "Private workload security group"
  vpc_id      = aws_vpc.this.id
  egress {
    description = "HTTPS egress only; private subnets have no default internet route"
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
  tags = var.tags
}
resource "aws_s3_bucket" "audit" {
  #checkov:skip=CKV_AWS_144:LAB-005: cross-region replication is an explicit DR design decision with cost and key-policy implications.
  #checkov:skip=CKV_AWS_18:LAB-004: separate S3 server-access logging destination is deferred; live access-monitoring design is an acceptance requirement.
  #checkov:skip=CKV2_AWS_62:LAB-003: event-driven object processing is outside this audit archive lab; live delivery monitoring is required.
  lifecycle { prevent_destroy = true }
  bucket_prefix = "${var.name}-audit-"
  force_destroy = false
  tags = merge(var.tags, {
    Purpose = "SecurityAudit"
  })
}
resource "aws_s3_bucket_public_access_block" "audit" {
  bucket                  = aws_s3_bucket.audit.id
  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}
resource "aws_s3_bucket_versioning" "audit" {
  bucket = aws_s3_bucket.audit.id
  versioning_configuration {
    status = "Enabled"
  }
}
resource "aws_s3_bucket_server_side_encryption_configuration" "audit" {
  bucket = aws_s3_bucket.audit.id
  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm     = "aws:kms"
      kms_master_key_id = aws_kms_key.audit.arn
    }
  }
}
resource "aws_s3_bucket_lifecycle_configuration" "audit" {
  bucket = aws_s3_bucket.audit.id
  rule {
    id     = "retain-audit"
    status = "Enabled"
    filter {}
    abort_incomplete_multipart_upload { days_after_initiation = 7 }
    noncurrent_version_expiration { noncurrent_days = var.log_retention_days }
    expiration {
      days = var.log_retention_days
    }
  }
}

