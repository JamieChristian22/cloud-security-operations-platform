output "aws" { value={vpc_id=module.aws_foundation.vpc_id,private_subnet_ids=module.aws_foundation.private_subnet_ids,audit_bucket=module.aws_foundation.audit_bucket} }
output "azure" { value={resource_group=module.azure_foundation.resource_group_name,subnet_id=module.azure_foundation.subnet_id,log_workspace=module.azure_foundation.log_analytics_workspace_id} }
output "gcp" { value={network_id=module.gcp_foundation.network_id,subnetwork_id=module.gcp_foundation.subnetwork_id,audit_bucket=module.gcp_foundation.audit_bucket} }
