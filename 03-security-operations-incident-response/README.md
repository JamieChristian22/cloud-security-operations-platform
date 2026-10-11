# Security Operations & Incident Response

Three Python detections correlate synthetic identity/cloud events. The incident package contains timeline, IOC register, response playbook and post-incident analysis. SIEM queries provide adaptation examples.

## Review path

Start at [detections/](detections/), then read the [project index](../PROJECT-INDEX.md), [evidence statement](../PORTFOLIO-EVIDENCE.md) and [demo guide](../docs/DEMO-GUIDE.md).

## Implementation boundary

The shared engine is `../src/csop/detections.py`. Run scripts with `--assert-alert` for positive lab fixtures. Geography alone does not establish compromise; validate enrichment and competing explanations.

## Validation

From the repository root:

```bash
python scripts/automation/run_all.py
python -m pytest -q
```

Infrastructure validation is separate: `python scripts/iac/validate_terraform.py`.

## Operational handoff

Document the source scope, accountable owner, expected result, observed evidence and rollback before a live change. Follow [operations standards](../docs/OPERATIONS-STANDARD.md) and the [deployment guide](../docs/DEPLOYMENT-GUIDE.md). All production-like processes here are lab demonstrations until separately accepted in a real environment.
