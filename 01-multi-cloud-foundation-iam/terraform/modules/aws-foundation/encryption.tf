resource "aws_kms_key" "audit" {
  description             = "CloudTrail, S3 audit archive and CloudWatch encryption"
  enable_key_rotation     = true
  deletion_window_in_days = 30
  lifecycle { prevent_destroy = true }
  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      { Sid       = "AccountKeyAdministration", Effect = "Allow",
        Principal = { AWS = "arn:${data.aws_partition.current.partition}:iam::${data.aws_caller_identity.current.account_id}:root" },
        Action    = "kms:*", Resource = "*"
      },
      { Sid       = "TrailEncryption", Effect = "Allow", Principal = { Service = "cloudtrail.amazonaws.com" },
        Action    = ["kms:GenerateDataKey*", "kms:DescribeKey"], Resource = "*",
        Condition = { StringEquals = { "aws:SourceArn" = local.trail_arn } }
      },
      { Sid       = "CloudWatchEncryption", Effect = "Allow",
        Principal = { Service = "logs.${data.aws_region.current.name}.amazonaws.com" },
        Action    = ["kms:Encrypt", "kms:Decrypt", "kms:ReEncrypt*", "kms:GenerateDataKey*", "kms:DescribeKey"], Resource = "*",
        Condition = { ArnLike = { "kms:EncryptionContext:aws:logs:arn" = "arn:${data.aws_partition.current.partition}:logs:${data.aws_region.current.name}:${data.aws_caller_identity.current.account_id}:log-group:/csop/${var.name}/*" } }
      }
    ]
  })
  tags = var.tags
}
resource "aws_kms_alias" "audit" {
  name          = "alias/${var.name}-audit"
  target_key_id = aws_kms_key.audit.key_id
}
resource "aws_default_security_group" "closed" {
  vpc_id  = aws_vpc.this.id
  ingress = []
  egress  = []
  tags    = merge(var.tags, { Name = "${var.name}-default-deny" })
}
resource "aws_cloudwatch_log_group" "trail" {
  name              = "/csop/${var.name}/cloudtrail"
  retention_in_days = 365
  kms_key_id        = aws_kms_key.audit.arn
  tags              = var.tags
}
resource "aws_iam_role" "trail" {
  name_prefix = "${var.name}-trail-"
  assume_role_policy = jsonencode({ Version = "2012-10-17", Statement = [{
    Effect    = "Allow", Principal = { Service = "cloudtrail.amazonaws.com" }, Action = "sts:AssumeRole",
    Condition = { StringEquals = { "aws:SourceArn" = local.trail_arn } }
  }] })
  tags = var.tags
}
resource "aws_iam_role_policy" "trail" {
  role = aws_iam_role.trail.id
  policy = jsonencode({ Version = "2012-10-17", Statement = [{
    Effect   = "Allow", Action = ["logs:CreateLogStream", "logs:PutLogEvents"],
    Resource = "${aws_cloudwatch_log_group.trail.arn}:*"
  }] })
}
