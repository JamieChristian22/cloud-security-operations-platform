variable "name" { type=string }
variable "project_id" { type=string }
variable "region" { type=string }
variable "subnet_cidr" { type=string }
variable "log_retention_days" { type=number default=90 validation { condition=var.log_retention_days>=30 error_message="Retain logs at least 30 days." } }
