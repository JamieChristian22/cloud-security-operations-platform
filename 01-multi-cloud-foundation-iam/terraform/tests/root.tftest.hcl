mock_provider "aws" {}
mock_provider "azurerm" {}
mock_provider "google" {}

run "secure_dev_configuration" {
  command = plan

  variables {
    environment        = "dev"
    aws_region         = "us-east-1"
    azure_location     = "eastus"
    gcp_project_id     = "northstar-secops-test"
    gcp_region         = "us-east1"
    log_retention_days = 90
  }

  assert {
    condition     = var.log_retention_days >= 30
    error_message = "Security log retention must remain at or above 30 days."
  }

  assert {
    condition     = local.common_tags.ManagedBy == "Terraform"
    error_message = "All resources must identify Terraform as the management source."
  }

  assert {
    condition     = local.common_tags.Environment == "dev"
    error_message = "Environment tagging must match the selected deployment environment."
  }

  assert {
    condition     = local.common_tags.Owner == "cloud-operations"
    error_message = "Operational ownership tag must remain defined."
  }
}

run "secure_prod_configuration" {
  command = plan

  variables {
    environment        = "prod"
    aws_region         = "us-east-1"
    azure_location     = "eastus"
    gcp_project_id     = "northstar-secops-prod-test"
    gcp_region         = "us-east1"
    log_retention_days = 365
  }

  assert {
    condition     = local.common_tags.Environment == "prod"
    error_message = "Production plans must carry the prod environment tag."
  }

  assert {
    condition     = var.log_retention_days == 365
    error_message = "The production test expects one-year security-log retention."
  }
}
