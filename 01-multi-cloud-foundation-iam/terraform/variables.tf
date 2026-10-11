variable "environment" {
  type    = string
  default = "dev"
  validation {
    condition     = contains(["dev", "stage", "prod"], var.environment)
    error_message = "environment must be dev, stage, or prod."
  }
}
variable "aws_region" {
  type    = string
  default = "us-east-1"
}
variable "azure_location" {
  type    = string
  default = "eastus"
}
variable "gcp_project_id" {
  type        = string
  description = "GCP project ID. Supply through TF_VAR_gcp_project_id or tfvars; never commit secrets."
}
variable "gcp_region" {
  type    = string
  default = "us-east1"
}
variable "log_retention_days" {
  type    = number
  default = 90
  validation {
    condition     = var.log_retention_days >= 30 && var.log_retention_days <= 365
    error_message = "log_retention_days must be 30-365."
  }
}


variable "audit_reader_principal_arns" {
  type        = set(string)
  default     = []
  description = "Explicit pre-existing audit reader principals; see module validation."
}

variable "audit_reader_object_ids" {
  type        = set(string)
  default     = []
  description = "Explicit pre-existing audit reader principals; see module validation."
}

variable "audit_reader_members" {
  type        = set(string)
  default     = []
  description = "Explicit pre-existing audit reader principals; see module validation."
}
