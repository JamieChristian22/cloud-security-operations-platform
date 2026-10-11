variable "name" {
  type = string
}
variable "location" {
  type = string
}
variable "vnet_cidr" {
  type = string
}
variable "subnet_cidr" {
  type = string
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
    error_message = "Retain logs between 30 and 365 days."
  }
}

