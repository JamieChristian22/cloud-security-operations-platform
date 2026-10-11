# Cloud Support & Reliability Center

Forty synthetic incidents cover IAM, networking, Linux, M365, monitoring, backup and delivery. Eight detailed runbooks and case-study packets show a repeatable investigation process. Python analytics summarize the supplied fixture.

## Review path

Start at [case-studies/](case-studies/), then read the [project index](../PROJECT-INDEX.md), [evidence statement](../PORTFOLIO-EVIDENCE.md) and [demo guide](../docs/DEMO-GUIDE.md).

## Implementation boundary

The resolution times and SLA flags are simulated. Case-study command outputs are labeled illustrative evidence, not cloud console captures. Start with the IAM or DNS case and discuss why each test changes the diagnosis.

## Validation

From the repository root:

```bash
python scripts/automation/run_all.py
python -m pytest -q
```

Infrastructure validation is separate: `python scripts/iac/validate_terraform.py`.

## Operational handoff

Document the source scope, accountable owner, expected result, observed evidence and rollback before a live change. Follow [operations standards](../docs/OPERATIONS-STANDARD.md) and the [deployment guide](../docs/DEPLOYMENT-GUIDE.md). All production-like processes here are lab demonstrations until separately accepted in a real environment.
