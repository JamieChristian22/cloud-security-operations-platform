resource "google_project_iam_audit_config" "all_services" {
  project = var.project_id
  service = "allServices"
  audit_log_config { log_type = "ADMIN_READ" }
  audit_log_config { log_type = "DATA_READ" }
  audit_log_config { log_type = "DATA_WRITE" }
}
resource "google_compute_firewall" "deny_management_ipv6" {
  name      = "${var.name}-deny-management-ipv6"
  network   = google_compute_network.this.name
  direction = "INGRESS"
  priority  = 1000
  deny {
    protocol = "tcp"
    ports    = ["22", "3389"]
  }
  source_ranges = ["::/0"]
}
variable "audit_reader_members" {
  type        = set(string)
  default     = []
  description = "Explicit group: or serviceAccount: principals allowed to read the audit bucket."
  validation {
    condition     = alltrue([for member in var.audit_reader_members : can(regex("^(group|serviceAccount):[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+$", member))])
    error_message = "Use explicit group or service account members; public principals are forbidden."
  }
}
resource "google_storage_bucket_iam_member" "audit_reader" {
  for_each = var.audit_reader_members
  bucket   = google_storage_bucket.audit.name
  role     = "roles/storage.objectViewer"
  member   = each.value
}
