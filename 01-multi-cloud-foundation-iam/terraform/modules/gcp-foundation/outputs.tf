output "network_id" { value=google_compute_network.this.id }
output "subnetwork_id" { value=google_compute_subnetwork.private.id }
output "audit_bucket" { value=google_storage_bucket.audit.name }
