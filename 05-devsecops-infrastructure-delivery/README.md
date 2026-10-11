# DevSecOps Infrastructure Delivery

Repository CI validates Python behavior, Terraform root/modules, static security and secret patterns. A focused Terraform JSON plan gate reports unsupported resource coverage. Release and rollback records connect code review to operational decisions.

## Review path

Start at [../.github/workflows/ci.yml](../.github/workflows/ci.yml), then read the [project index](../PROJECT-INDEX.md), [evidence statement](../PORTFOLIO-EVIDENCE.md) and [demo guide](../docs/DEMO-GUIDE.md).

## Implementation boundary

The workflow does not deploy. Hosted execution must be verified after upload. Checkov exceptions are explicit lab tradeoffs, not proof that every benchmark passes. Plan artifacts can contain sensitive data.

## Validation

From the repository root:

```bash
python scripts/automation/run_all.py
python -m pytest -q
```

Infrastructure validation is separate: `python scripts/iac/validate_terraform.py`.

## Operational handoff

Document the source scope, accountable owner, expected result, observed evidence and rollback before a live change. Follow [operations standards](../docs/OPERATIONS-STANDARD.md) and the [deployment guide](../docs/DEPLOYMENT-GUIDE.md). All production-like processes here are lab demonstrations until separately accepted in a real environment.
