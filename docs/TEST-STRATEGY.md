# Validation strategy

| Layer | What it proves | What it does not prove |
|---|---|---|
| Python unit/regression tests | Rules, validation, exception expiry, edge cases, reporting and plan-policy behavior | Live cloud collection completeness or real attacks |
| CLI integration tests | Exit codes and generated outputs across processes | Deployment authorization |
| Terraform fmt | HCL style and parseability | Provider/API validity |
| Terraform validate | Provider-schema and configuration consistency | Permission, quota, network or API behavior |
| Terraform test with mocked providers | Assertions about intended configuration | Successful live provisioning or telemetry delivery |
| Checkov | Static rules within scanned scope and documented exceptions | Complete security/compliance |
| TFLint | Terraform language quality within configured rules | Runtime correctness |
| Gitleaks | Recognizable secret patterns in scanned files | Absence of all sensitive data |
| Live sandbox acceptance | Actual provisioning, permission boundaries and log arrival | Production readiness across all accounts |

## Reproduction

Run `python scripts/automation/run_all.py`. For Terraform, install the recorded CLI version and run `python scripts/iac/validate_terraform.py`. The latter initializes, validates and tests the root and all three modules, saves separate logs and fails if any step fails. Provider downloads require internet access; mocked tests do not require cloud credentials.

Run security tools in an isolated virtual environment with `requirements-security.txt`. Checkov's HCL dependency differs from the optional HCL parser used for structural checks, so avoid mixing those packages into an unrelated application environment.

## Evidence policy

Results are generated from actual commands. Every check has a command, return code and output log. A failed or unavailable stage remains visible. Generated timestamps are the execution host's UTC clock. No live cloud acceptance is implied by offline success. `evidence/validation/README.md` summarizes the packaged run.

## CI acceptance after upload

A maintainer should observe the first hosted run, download its artifacts, fix runner-specific issues if any, and then require the offline, terraform and security jobs in branch protection. Setting up a workflow file alone does not enable required checks. Keep deployment permissions separate from validation permissions.
