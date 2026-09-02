# CloudGuardian Remediation Walkthrough

The insecure sample is intentionally scanned first, then a remediated version demonstrates closure of each finding.

| Finding | Remediation represented in `environment-remediated.json` |
|---|---|
| Missing MFA | MFA set to true for enabled workforce identities |
| Dormant privileged account | account disabled pending owner review |
| Stale access key | old key marked inactive; short-lived credential model recommended |
| Wildcard permissions | replaced `*` with task-scoped read actions |
| Public storage | public access disabled |
| Public SSH | source restricted to approved internal management range |
| Missing owner tag | ownership metadata added |

Run both datasets and compare the generated reports. The remediated sample should return **0 findings / risk score 0**. This before/after evidence is stronger than a scanner that only reports problems.
