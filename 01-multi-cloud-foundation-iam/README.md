# Multi-Cloud Foundation & IAM

Terraform modules create private networks, audit destinations and log delivery, with explicit optional audit-reader principals. AWS includes CloudTrail, VPC flow logs, KMS, encrypted storage and restricted default security group. Azure includes private subnet/NSG, Log Analytics and subscription activity diagnostics. GCP includes flow logs, audit configuration, a filtered sink and protected audit storage.

## Review path

Start at [terraform/](terraform/), then read the [project index](../PROJECT-INDEX.md), [evidence statement](../PORTFOLIO-EVIDENCE.md) and [demo guide](../docs/DEMO-GUIDE.md).

## Implementation boundary

Review `terraform/modules/`, module tests, governance records and the deployment guide. Reader lists default empty; organization-specific MFA, lifecycle approvals and access reviews are not automatically provisioned.

## Validation

From the repository root:

```bash
python scripts/automation/run_all.py
python -m pytest -q
```

Infrastructure validation is separate: `python scripts/iac/validate_terraform.py`.

## Operational handoff

Document the source scope, accountable owner, expected result, observed evidence and rollback before a live change. Follow [operations standards](../docs/OPERATIONS-STANDARD.md) and the [deployment guide](../docs/DEPLOYMENT-GUIDE.md). All production-like processes here are lab demonstrations until separately accepted in a real environment.
