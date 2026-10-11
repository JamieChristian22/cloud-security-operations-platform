variable "name" {
  type = string
}
variable "vpc_cidr" {
  type = string
}
variable "private_subnets" {
  type = map(object({
    cidr = string,
    az   = string
  }))
}
variable "tags" {
  type = map(string)
  default = {
  }
}
variable "log_retention_days" {
  type    = number
  default = 90
  validation {
    condition     = var.log_retention_days >= 30 && var.log_retention_days <= 365
    error_message = "Retain security logs between 30 and 365 days."
  }
}

