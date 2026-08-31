mock_provider "aws" {}

run "aws_security_baseline" {
  command = plan

  variables {
    name     = "northstar-test"
    vpc_cidr = "10.20.0.0/16"
    private_subnets = {
      private_a = { cidr = "10.20.10.0/24", az = "us-east-1a" }
      private_b = { cidr = "10.20.20.0/24", az = "us-east-1b" }
    }
    tags = {
      Environment = "test"
      ManagedBy   = "Terraform"
    }
    log_retention_days = 90
  }

  assert {
    condition     = aws_vpc.this.enable_dns_support && aws_vpc.this.enable_dns_hostnames
    error_message = "The VPC must keep DNS support and hostnames enabled for private workload resolution."
  }

  assert {
    condition     = alltrue([for subnet in aws_subnet.private : subnet.map_public_ip_on_launch == false])
    error_message = "Private subnets must not auto-assign public IP addresses."
  }

  assert {
    condition     = aws_s3_bucket_public_access_block.audit.block_public_acls && aws_s3_bucket_public_access_block.audit.block_public_policy && aws_s3_bucket_public_access_block.audit.ignore_public_acls && aws_s3_bucket_public_access_block.audit.restrict_public_buckets
    error_message = "Audit storage must block every supported path to public access."
  }

  assert {
    condition     = aws_s3_bucket_versioning.audit.versioning_configuration[0].status == "Enabled"
    error_message = "Audit storage versioning must remain enabled."
  }

  assert {
    condition     = aws_s3_bucket_server_side_encryption_configuration.audit.rule[0].apply_server_side_encryption_by_default[0].sse_algorithm == "AES256"
    error_message = "Audit storage must use server-side encryption."
  }

  assert {
    condition     = aws_s3_bucket_lifecycle_configuration.audit.rule[0].expiration[0].days == 90
    error_message = "Audit lifecycle retention must match the approved log retention input."
  }
}
