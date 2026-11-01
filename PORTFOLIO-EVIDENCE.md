# Cloud Security & Operations Platform — Evidence Map

This index links claimed portfolio capabilities to inspectable code, fixtures, tests and reports. All exercises use synthetic data unless stated otherwise. Neither the evidence files nor passing offline checks establish live AWS, Azure or GCP deployment.

| Capability | Implementation | Validation / evidence |
|---|---|---|
| Identity and access review | [IAM access review](scripts/iam/access_review.py) | [IAM sample inventory](scripts/sample_data/iam_users.json) |
| Secure infrastructure configuration | [Terraform root](01-multi-cloud-foundation-iam/terraform/) | [Mock Terraform tests](01-multi-cloud-foundation-iam/terraform/tests/root.tftest.hcl) |
| Service-desk incident metrics | [Ticket metrics](scripts/operations/ticket_metrics.py) | [Synthetic tickets](02-cloud-support-reliability-center/data/tickets.csv) |
| Authentication threat detection | [Detection engine](src/csop/detections.py) | [Detection unit tests](tests/test_detections.py) |
| Configuration security assessment | [CloudGuardian](04-cloudguardian-security-auditor/src/cloudguardian.py) | [Insecure findings](04-cloudguardian-security-auditor/reports/generated/report.json) and [remediated sample](04-cloudguardian-security-auditor/reports/remediated/report.json) |
| Security policy checks | [Plan policy engine](src/csop/plan_policy.py) | [Policy tests](tests/test_plan_policy.py) |
| Full offline regression | [Validation orchestrator](scripts/automation/run_all.py) | [Test strategy](docs/TEST-STRATEGY.md) |
| Hosted build checks | [GitHub Actions CI workflow](.github/workflows/ci.yml) | Review the actual pull-request checks; presence of this file does not establish a passed hosted run |

## Reproduce the results

```bash
python -m pip install -r requirements-dev.txt
python scripts/automation/run_all.py
```

The suite writes an aggregate result to `scripts/reports/automation_summary.json`. Verify the current workflow execution before treating reports stored in the repository as current. [Demonstration guide](docs/DEMO-GUIDE.md) explains a ten-minute walkthrough.
