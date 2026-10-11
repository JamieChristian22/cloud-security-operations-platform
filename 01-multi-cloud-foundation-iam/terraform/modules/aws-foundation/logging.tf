data "aws_caller_identity" "current" {}
data "aws_partition" "current" {}
data "aws_region" "current" {}
locals {
  trail_arn = "arn:${data.aws_partition.current.partition}:cloudtrail:${data.aws_region.current.name}:${data.aws_caller_identity.current.account_id}:trail/${var.name}-audit"
}
resource "aws_s3_bucket_policy" "audit" {
  bucket = aws_s3_bucket.audit.id
  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Sid       = "DenyInsecureTransport"
        Effect    = "Deny"
        Principal = "*"
        Action    = "s3:*"
        Resource  = [aws_s3_bucket.audit.arn, "${aws_s3_bucket.audit.arn}/*"]
        Condition = { Bool = { "aws:SecureTransport" = "false" } }
      },
      {
        Sid       = "CloudTrailBucketCheck"
        Effect    = "Allow"
        Principal = { Service = "cloudtrail.amazonaws.com" }
        Action    = "s3:GetBucketAcl"
        Resource  = aws_s3_bucket.audit.arn
        Condition = { StringEquals = { "aws:SourceArn" = local.trail_arn } }
      },
      {
        Sid       = "CloudTrailDelivery"
        Effect    = "Allow"
        Principal = { Service = "cloudtrail.amazonaws.com" }
        Action    = "s3:PutObject"
        Resource  = "${aws_s3_bucket.audit.arn}/AWSLogs/${data.aws_caller_identity.current.account_id}/*"
        Condition = { StringEquals = { "aws:SourceArn" = local.trail_arn, "s3:x-amz-acl" = "bucket-owner-full-control" } }
      }
    ]
  })
}
resource "aws_cloudtrail" "security" {
  #checkov:skip=CKV_AWS_252:LAB-001: CloudWatch log integration is the demonstrated path; SNS fanout is an environment-specific integration.
  kms_key_id                    = aws_kms_key.audit.arn
  cloud_watch_logs_group_arn    = "${aws_cloudwatch_log_group.trail.arn}:*"
  cloud_watch_logs_role_arn     = aws_iam_role.trail.arn
  name                          = "${var.name}-audit"
  s3_bucket_name                = aws_s3_bucket.audit.id
  include_global_service_events = true
  is_multi_region_trail         = true
  enable_log_file_validation    = true
  enable_logging                = true
  event_selector {
    read_write_type           = "All"
    include_management_events = true
  }
  tags       = var.tags
  depends_on = [aws_s3_bucket_policy.audit, aws_iam_role_policy.trail]
}
resource "aws_cloudwatch_log_group" "flow" {
  name              = "/csop/${var.name}/vpc-flow"
  retention_in_days = 365
  kms_key_id        = aws_kms_key.audit.arn
  tags              = var.tags
}
resource "aws_iam_role" "flow" {
  name_prefix = "${var.name}-flow-"
  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{ Effect = "Allow", Principal = { Service = "vpc-flow-logs.amazonaws.com" }, Action = "sts:AssumeRole",
      Condition = { StringEquals = { "aws:SourceAccount" = data.aws_caller_identity.current.account_id } }
    }]
  })
  tags = var.tags
}
resource "aws_iam_role_policy" "flow" {
  role = aws_iam_role.flow.id
  policy = jsonencode({ Version = "2012-10-17", Statement = [{
    Effect   = "Allow"
    Action   = ["logs:CreateLogStream", "logs:PutLogEvents", "logs:DescribeLogStreams"]
    Resource = "${aws_cloudwatch_log_group.flow.arn}:*"
  }] })
}
resource "aws_flow_log" "security" {
  iam_role_arn    = aws_iam_role.flow.arn
  log_destination = aws_cloudwatch_log_group.flow.arn
  traffic_type    = "ALL"
  vpc_id          = aws_vpc.this.id
  tags            = var.tags
  depends_on      = [aws_iam_role_policy.flow]
}
