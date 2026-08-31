# Native Terraform Tests

The portfolio uses Terraform's native testing framework to verify security expectations before authenticated deployment.

## Test Layers
- `tests/root.tftest.hcl` validates root-level environment and governance assumptions.
- `modules/aws-foundation/tests/security.tftest.hcl` validates private subnet behavior, audit-storage public-access blocking, versioning, encryption, and retention.
- `modules/azure-foundation/tests/security.tftest.hcl` validates private address ranges, inbound internet denial, and logging retention.
- `modules/gcp-foundation/tests/security.tftest.hcl` validates custom-network behavior, private Google access, VPC flow logging, internet SSH denial, storage access controls, and versioning.

## CI Commands
```bash
terraform -chdir=01-multi-cloud-foundation-iam/terraform test
terraform -chdir=01-multi-cloud-foundation-iam/terraform/modules/aws-foundation test
terraform -chdir=01-multi-cloud-foundation-iam/terraform/modules/azure-foundation test
terraform -chdir=01-multi-cloud-foundation-iam/terraform/modules/gcp-foundation test
```

Mock providers are used so the unit-style plans do not require live AWS, Azure, or GCP credentials. These tests do not claim that a real deployment has occurred. Authenticated integration tests and post-deployment validation would still be required before production release.
