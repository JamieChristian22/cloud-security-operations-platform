variable "audit_reader_principal_arns" {
  type        = set(string)
  default     = []
  description = "Approved existing role ARNs allowed to assume the scoped audit reader. Empty creates no reader."
  validation {
    condition     = alltrue([for arn in var.audit_reader_principal_arns : can(regex("^arn:aws[a-z-]*:iam::[0-9]{12}:role/[A-Za-z0-9+=,.@_/-]+$", arn))])
    error_message = "Supply explicit IAM role ARNs; wildcard and account-root trust are not allowed."
  }
}
resource "aws_iam_role" "audit_reader" {
  count                = length(var.audit_reader_principal_arns) > 0 ? 1 : 0
  name_prefix          = "${var.name}-audit-reader-"
  max_session_duration = 3600
  assume_role_policy = jsonencode({ Version = "2012-10-17", Statement = [{
    Effect = "Allow", Principal = { AWS = sort(tolist(var.audit_reader_principal_arns)) }, Action = "sts:AssumeRole"
  }] })
  tags = var.tags
}
resource "aws_iam_role_policy" "audit_reader" {
  count = length(var.audit_reader_principal_arns) > 0 ? 1 : 0
  role  = aws_iam_role.audit_reader[0].id
  policy = jsonencode({ Version = "2012-10-17", Statement = [
    { Effect = "Allow", Action = ["s3:ListBucket"], Resource = aws_s3_bucket.audit.arn },
    { Effect = "Allow", Action = ["s3:GetObject"], Resource = "${aws_s3_bucket.audit.arn}/AWSLogs/*" },
    { Effect = "Allow", Action = ["kms:Decrypt"], Resource = aws_kms_key.audit.arn }
  ] })
}
