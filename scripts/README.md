# Automation entry points

| Command | Purpose |
|---|---|
| `python scripts/automation/run_all.py` | Run all offline fixture checks, reports and regression tests |
| `python -m pytest -q` | Run the complete Python test suite |
| `python scripts/iac/validate_terraform.py` | Format/init/validate/mock-test the root and three provider modules |
| `python scripts/iac/plan_policy.py --help` | Evaluate saved Terraform JSON with explicit coverage |
| `python scripts/collectors/aws_security_groups.py --help` | Normalize AWS CLI export or collect read-only regional security groups |
| `python scripts/automation/portfolio_validate.py --repo . --output reports/local/structure.json` | Validate required delivery files and local Markdown links |

The standalone IAM, baseline, FinOps and DR scripts are retained illustrative controls over their own fixture formats. CloudGuardian is the primary normalized security gate. Successful execution of an illustrative report script does not mean its findings are resolved. Review report status and findings separately.

Install `requirements-dev.txt` in a virtual environment for offline tests. Optional live, read-only AWS collection uses `requirements-collectors.txt`. Optional Checkov scans use `requirements-security.txt` in a separate virtual environment; TFLint and Gitleaks are native tools downloaded with SHA256 checks by `scripts/automation/install_ci_tools.py`. Terraform requires network access for provider initialization. Never commit live state, plans, raw credentials or unredacted customer evidence.
