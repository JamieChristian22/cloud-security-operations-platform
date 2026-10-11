# CloudGuardian Security Auditor

Eight inventory controls produce JSON, CSV and HTML reports with stable IDs, open-risk scoring and expiry-aware exceptions. Strict validation prevents missing or malformed security fields from silently passing.

## Review path

Start at [src/cloudguardian.py](src/cloudguardian.py), then read the [project index](../PROJECT-INDEX.md), [evidence statement](../PORTFOLIO-EVIDENCE.md) and [demo guide](../docs/DEMO-GUIDE.md).

## Implementation boundary

The paired input files demonstrate insecure and remediated snapshots. The AWS collector covers only security-group ingress/tags; full Azure/GCP collection is not implemented. See data contracts, control catalog, tests and report scope.

## Validation

From the repository root:

```bash
python scripts/automation/run_all.py
python -m pytest -q
```

Infrastructure validation is separate: `python scripts/iac/validate_terraform.py`.

## Operational handoff

Document the source scope, accountable owner, expected result, observed evidence and rollback before a live change. Follow [operations standards](../docs/OPERATIONS-STANDARD.md) and the [deployment guide](../docs/DEPLOYMENT-GUIDE.md). All production-like processes here are lab demonstrations until separately accepted in a real environment.
