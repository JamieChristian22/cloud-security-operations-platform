# Multi-Cloud Infrastructure as Code

Production-inspired Terraform for a simulated Northstar environment. The root composition calls reusable AWS, Azure, and GCP modules rather than defining every resource in one file.

## What this demonstrates
- Reusable multi-cloud modules with typed inputs and outputs.
- Private network foundations in three clouds.
- Security-by-default controls: public-access prevention, encryption, versioning, NSG/firewall restrictions, VPC flow logs, centralized security logging, and retention policies.
- Environment-specific tfvars examples without committed credentials.
- CI quality gates for formatting, initialization, validation, native `terraform test`, TFLint, Checkov, and secret scanning.
- Explicit state/backend guidance and change/rollback documentation.

## Safe validation
```bash
terraform fmt -recursive -check
terraform init -backend=false
terraform validate
terraform test
terraform -chdir=modules/aws-foundation test
terraform -chdir=modules/azure-foundation test
terraform -chdir=modules/gcp-foundation test
```
Native Terraform tests use mock providers to verify planned security properties without cloud credentials. Static security checks are also executed in GitHub Actions. Live deployment requires authenticated cloud sandboxes and may incur charges. No claim is made that this lab configuration has been deployed to a production employer environment.

## Structure
`modules/` contains reusable provider-specific foundations. `environments/` contains non-secret examples. Root files compose the modules. `tests/` contains root governance assertions, and each provider module has its own `tests/security.tftest.hcl` security contract. State files, `.terraform/`, plans, and real tfvars are excluded from Git.
