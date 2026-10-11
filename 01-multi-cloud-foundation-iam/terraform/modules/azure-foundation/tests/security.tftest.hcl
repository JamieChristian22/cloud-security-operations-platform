mock_provider "azurerm" {
  mock_data "azurerm_client_config" {
    defaults = { subscription_id = "11111111-1111-1111-1111-111111111111" }
  }
}

run "azure_security_baseline" {
  command = plan

  variables {
    name               = "northstar-test"
    location           = "eastus"
    vnet_cidr          = "10.30.0.0/16"
    subnet_cidr        = "10.30.10.0/24"
    log_retention_days = 90
    tags = {
      Environment = "test"
      ManagedBy   = "Terraform"
    }
  }

  assert {
    condition     = contains(azurerm_virtual_network.this.address_space, "10.30.0.0/16")
    error_message = "The Azure VNet must use the approved private address range."
  }

  assert {
    condition     = contains(azurerm_subnet.private.address_prefixes, "10.30.10.0/24")
    error_message = "The private subnet CIDR must remain scoped to the approved range."
  }

  assert {
    condition     = one(azurerm_network_security_group.private.security_rule).direction == "Inbound" && one(azurerm_network_security_group.private.security_rule).access == "Deny" && one(azurerm_network_security_group.private.security_rule).source_address_prefix == "Internet"
    error_message = "The private NSG must explicitly deny inbound internet traffic."
  }

  assert {
    condition     = azurerm_log_analytics_workspace.security.retention_in_days == 90
    error_message = "Log Analytics retention must match the approved security-retention setting."
  }
}

