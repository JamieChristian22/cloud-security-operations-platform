# Packaged validation results

Source revision before upgrade: `ef0e1524917892710a9f35e779b6c154e40d5576`.

| Check | Result | Evidence |
|---|---|---|
| Python regression tests | 98 passed | python-junit.xml and scripts/reports/automation_summary.json |
| Offline workflow | 11/11 checks passed on supplied fixtures | scripts/reports/automation_summary.json |
| Terraform formatting | Passed | terraform-fmt.txt |
| Checkov 3.2.495 | 101 passed, 0 failed, 7 resource-scoped lab exceptions | checkov.json and docs/SCANNER-EXCEPTIONS.md |
| Gitleaks 8.24.2 | No findings in scanned current files | gitleaks.json and gitleaks.txt |
| Terraform provider validation / mocked tests | Blocked by runtime Unix-socket prohibition | terraform-environment.txt and terraform-validate.txt |
| TFLint 0.55.1 | Blocked by plugin runtime in this environment | tflint.txt |
| Live cloud deployment, live collection and SIEM replay | Not performed | See docs/DEPLOYMENT-GUIDE.md |
| Hosted GitHub Actions | Workflow supplied; not executed here | .github/workflows/ci.yml |

Commands and versions are recorded in command-results.json. Generated timestamps come from the execution host. The unit tests and scanner results do not establish cloud deployment success. A check marked blocked is not counted as passed.

Checkov exceptions cover SNS fanout, an unattached reusable workload group, S3 notifications/access logging/replication, GCP access logging and irreversible retention lock. Each is scoped and explained; none is a production risk approval.

To rerun: install development dependencies and run `python scripts/automation/run_all.py`. In a supported Terraform environment run `python scripts/iac/validate_terraform.py`, then run the scanner commands from CI. Review hosted run artifacts after uploading the extracted project.
