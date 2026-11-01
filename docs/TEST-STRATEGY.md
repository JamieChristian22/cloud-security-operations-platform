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

Run Checkov in an isolated virtual environment using `requirements-security.txt`. The pinned binary URLs and SHA256 checks for TFLint and Gitleaks are in `scripts/automation/tool-downloads.json` and installed by `scripts/automation/install_ci_tools.py` on supported Linux AMD64 machines. Scanner exceptions must remain visible and do not constitute production risk approval.

## Evidence policy

Results are generated from actual commands. Every check has a command, return code and output log. A failed or unavailable stage remains visible. Generated timestamps are the execution host's UTC clock. No live cloud acceptance is implied by offline success. `evidence/validation/README.md` summarizes the packaged run.

## CI acceptance after upload

The feature-branch `.github/workflows/ci.yml` defines three jobs named `offline`, `terraform`, and `security`, with read-only repository permissions, pinned actions, offline fixture testing, Terraform mocked validation, and secrets/IaC scanning. A maintainer must inspect the actual hosted run and its artifacts, fix runner-specific failures, then configure required checks/branch protection. A workflow file alone does not establish successful CI or deploy infrastructure.
