output "resource_group_name" { value=azurerm_resource_group.this.name }
output "subnet_id" { value=azurerm_subnet.private.id }
output "log_analytics_workspace_id" { value=azurerm_log_analytics_workspace.security.id }
