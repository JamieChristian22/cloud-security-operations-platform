variable "environment" { type=string default="dev" validation { condition=contains(["dev","stage","prod"],var.environment) error_message="environment must be dev, stage, or prod." } }
variable "aws_region" { type=string default="us-east-1" }
variable "azure_location" { type=string default="eastus" }
variable "gcp_project_id" { type=string description="GCP project ID. Supply through TF_VAR_gcp_project_id or tfvars; never commit secrets." }
variable "gcp_region" { type=string default="us-east1" }
variable "log_retention_days" { type=number default=90 validation { condition=var.log_retention_days>=30 && var.log_retention_days<=3650 error_message="log_retention_days must be 30-3650." } }
