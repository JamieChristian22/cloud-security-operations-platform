# Multi-Cloud Infrastructure as Code

Production-inspired Terraform for a simulated Northstar environment. The root composition calls reusable AWS, Azure, and GCP modules rather than defining every resource in one file.

## What this demonstrates
- Reusable multi-cloud modules with typed inputs and outputs.
- Private network foundations in three clouds.
- Security-by-default controls: public-access prevention, encryption, versioning, NSG/firewall restrictions, VPC flow logs, centralized security logging, and retention policies.
- Environment-specific tfvars examples without committed credentials.
- CI quality gates for formatting, initialization, validation, native `terraform test`, TFLint, Checkov, and secret scanning.
- Explicit state/backend guidance and change/rollback documentation.

## Validation

From the repository root:

```bash
python scripts/iac/validate_terraform.py
```

This initializes and validates the root and every provider module before running mocked tests. It never applies cloud resources. Provider plugins need a supported local runtime and internet access for initial download. The packaged evidence records that provider execution was blocked by this generation environment's socket restriction; no Terraform test pass is claimed here.

The GitHub Actions workflow is configured to execute these stages after upload. Live deployment requires authenticated sandboxes, permission/cost review and telemetry acceptance. See the root deployment guide for state and retention considerations.

## Structure
`modules/` contains reusable provider-specific foundations. `environments/` contains non-secret examples. Root files compose the modules. `tests/` contains root governance assertions, and each provider module has its own `tests/security.tftest.hcl` security contract. State files, `.terraform/`, plans, and real tfvars are excluded from Git.

