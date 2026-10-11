# Sandbox deployment and live acceptance

## Scope and prerequisites

The repository includes a multi-cloud root for learning and independent modules for isolated review. Use dedicated sandbox accounts/projects/subscriptions. Confirm ownership, billing limits, enabled APIs, permitted regions and a cleanup plan. Audit retention and KMS protection intentionally make deletion harder. This document does not assert that a deployment has happened.

Terraform version and providers are recorded in configuration/lockfiles. Use federated CLI sessions or workload identity; keep credentials out of tfvars, code and screenshots. A subscription-level Azure diagnostic setting requires appropriate subscription permissions. GCP audit configuration is authoritative for the configured service; review existing audit settings before use.

## Local validation first

```bash
python scripts/automation/run_all.py
python scripts/iac/validate_terraform.py
```

The offline workflow does not run apply. After all local checks pass, review provider identity using your cloud CLI and verify the target account independently.

## State and environment design

Default state is local for the lab. It may contain sensitive identifiers and must not enter Git. For team use, configure an approved remote backend with encryption, access logging, versioning and locking. The supplied `backend.hcl.example` is an example of parameters, not an active backend. Add a backend declaration appropriate to your organization and migrate state only after backing it up and coordinating exclusive access.

Separate state by cloud and environment before production use. The single root couples lifecycle and credentials across providers. Keep IAM deployment privileges separate from application deployment and read-only assessment.

## Plan and review

Set GCP project ID and cloud CLI credentials explicitly. Audit reader variables default empty; supply only verified existing principals. Check environment-specific retention and resource names. Do not use the synthetic project IDs from tests as real deployment targets.

```bash
cd 01-multi-cloud-foundation-iam/terraform
terraform init
terraform plan -out=reviewed.tfplan
terraform show -json reviewed.tfplan > reviewed-plan.json
```

Run the focused plan policy from the repository root:

```bash
python scripts/iac/plan_policy.py --input 01-multi-cloud-foundation-iam/terraform/reviewed-plan.json --output reports/local/plan-policy.json
```

Review uncovered resource types, unknown values, Checkov results, permissions, replacements, deletions and costs. Treat plan JSON as sensitive; do not commit real plans. Apply only the reviewed plan after the accountable owner approves it. This package provides no automatic apply workflow.

## Live acceptance checklist

| Test | Action | Required evidence |
|---|---|---|
| Identity | Assume authorized audit-reader role; attempt an unauthorized write | Sanitized allowed read and denied write, principal and scope |
| AWS audit | Perform benign management read; verify CloudTrail file and CloudWatch event | Timestamp, event ID, trail status, delivery delay |
| AWS network | Generate approved lab traffic and verify flow log delivery | Interface/VPC scope, ACCEPT/REJECT record and destination |
| Azure logging | Make an approved resource-group change | Activity event arrives in selected Log Analytics workspace |
| GCP logging | Perform approved data read in a test resource | Audit event arrives in configured sink destination |
| Storage | Verify public access is blocked and authorized encrypted access works | Effective configuration and access result |
| Detection | Replay approved benign and suspicious events in a test workspace | Rule version, expected/actual alerts and false-positive notes |
| Recovery | Restore a disposable object/configuration from a known version | Hash match, elapsed time, measured recovery point |
| Cost | Review post-test resources and projected retention charges | Owner-approved budget and cleanup inventory |

## Recovery and cleanup

Keep audit evidence and Terraform state. Before deleting anything, export resource inventory, verify that no shared dependency exists, and inspect the destroy plan. `prevent_destroy` will stop deletion of protected audit stores and KMS keys; do not remove it casually. Retention can continue to prevent object deletion even after Terraform configuration changes. A real retention lock can be irreversible; the lab does not enable it by default.

KMS keys, CloudWatch ingestion/retention, Azure Log Analytics, GCP data-access logs and storage can incur charges. Cost documents are governance examples, not pricing quotes. Measure actual sandbox usage and confirm current provider pricing before deployment.
