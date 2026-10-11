data "azurerm_client_config" "current" {}
resource "azurerm_monitor_diagnostic_setting" "subscription_activity" {
  name                       = "${var.name}-activity"
  target_resource_id         = "/subscriptions/${data.azurerm_client_config.current.subscription_id}"
  log_analytics_workspace_id = azurerm_log_analytics_workspace.security.id
  enabled_log { category = "Administrative" }
  enabled_log { category = "Security" }
  enabled_log { category = "Policy" }
  enabled_log { category = "Alert" }
}
variable "audit_reader_object_ids" {
  type        = set(string)
  default     = []
  description = "Existing Entra group/service principal object IDs; read-only access scoped to this resource group."
  validation {
    condition     = alltrue([for id in var.audit_reader_object_ids : can(regex("^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$", id))])
    error_message = "Supply existing Entra object UUIDs."
  }
}
resource "azurerm_role_assignment" "audit_reader" {
  for_each             = var.audit_reader_object_ids
  scope                = azurerm_resource_group.this.id
  role_definition_name = "Reader"
  principal_id         = each.value
}
