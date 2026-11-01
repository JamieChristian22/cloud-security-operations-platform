# CloudGuardian Interactive Demo

[Open the self-contained findings explorer](../demo/cloudguardian.html) by opening the HTML file locally in a modern browser. No server, credentials, backend, or internet connection is required.

The explorer embeds the `04-cloudguardian-security-auditor/reports/generated/report.json` **synthetic** assessment snapshot and provides keyword, cloud-provider, and severity filters. Only the view changes; the tool does not modify cloud resources or run live scans. The risk score is the report's lab heuristic.

## Reviewer walkthrough

1. Open `demo/cloudguardian.html`; confirm the eight initial findings shown in the supplied fixture.
2. Select `High` severity and confirm the filtering and visible count.
3. Search `MFA` to inspect identity findings, then choose **Reset**.
4. Compare the control, evidence and remediation for a critical finding.
5. Review the source [CloudGuardian CLI](../04-cloudguardian-security-auditor/src/cloudguardian.py) and [demonstration script](DEMO-GUIDE.md) for the runnable control checks.

## Data integrity

The Python test `tests/test_demo_snapshot.py` asserts that the embedded dataset matches the current committed JSON snapshot. Regenerate the embedded payload if you change the source fixture. Treat any UI illustration as supporting evidence, not a production verification.
