mock_provider "google" {}

run "gcp_security_baseline" {
  command = plan

  variables {
    name               = "northstar-test"
    project_id         = "northstar-secops-test"
    region             = "us-east1"
    subnet_cidr        = "10.40.10.0/24"
    log_retention_days = 90
  }

  assert {
    condition     = google_compute_network.this.auto_create_subnetworks == false
    error_message = "The GCP VPC must not create uncontrolled automatic subnets."
  }

  assert {
    condition     = google_compute_subnetwork.private.private_ip_google_access == true
    error_message = "Private Google access must remain enabled for the private subnet."
  }

  assert {
    condition     = google_compute_subnetwork.private.log_config[0].flow_sampling == 0.5
    error_message = "VPC flow logging must remain enabled at the documented sampling level."
  }

  assert {
    condition     = google_compute_firewall.deny_ssh_internet.direction == "INGRESS" && google_compute_firewall.deny_ssh_internet.source_ranges == ["0.0.0.0/0"] && google_compute_firewall.deny_ssh_internet.deny[0].ports == ["22"]
    error_message = "The baseline firewall must deny internet-originated SSH."
  }

  assert {
    condition     = google_storage_bucket.audit.uniform_bucket_level_access == true && google_storage_bucket.audit.public_access_prevention == "enforced"
    error_message = "GCP audit storage must use uniform access and enforced public-access prevention."
  }

  assert {
    condition     = google_storage_bucket.audit.versioning[0].enabled == true
    error_message = "GCP audit storage versioning must remain enabled."
  }
}
