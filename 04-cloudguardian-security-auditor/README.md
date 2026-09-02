# Project 04 — CloudGuardian Security Auditor

CloudGuardian is an original, dependency-free Python CLI that evaluates normalized multi-cloud/identity inventory data and produces prioritized findings with JSON, CSV, and HTML reports.

## Detection Coverage
- workforce identities missing MFA;
- dormant enabled accounts and dormant privileged identities;
- stale long-lived access keys;
- wildcard administrative permissions;
- public storage;
- internet-exposed SSH/RDP;
- missing `Environment` / `Owner` metadata.

## Run
```bash
python src/cloudguardian.py --input sample_data/environment.json --out reports/generated
```

To use the tool as a CI-style gate:
```bash
python src/cloudguardian.py --input sample_data/environment.json --out reports/generated --fail-on high
```
A non-zero exit is expected when high/critical findings exist.

## Included Sample
The intentionally insecure sample produces **8 findings** so each detection path is demonstrable. The data spans Entra ID-style identities plus AWS/Azure/GCP-tagged resources. It is synthetic and contains no live credentials.

## Reporting
Each finding records severity, control, provider, resource, evidence, remediation, and a high-level control mapping. The risk score is intentionally transparent: Critical=25, High=15, Medium=7, Low=2, capped at 100. It is a portfolio heuristic—not a standard such as CVSS.

## Tests
`pytest tests -q` validates clean-state behavior, MFA, public storage, public SSH, wildcard permissions, and score capping.

## Design Limitation
CloudGuardian consumes normalized inventory rather than calling provider APIs. That makes the portfolio safe/reproducible but means a production implementation would require authenticated collectors, pagination, rate-limit handling, provider-specific schemas, exception workflows, and secure secrets management.
