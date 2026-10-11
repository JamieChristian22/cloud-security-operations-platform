# Remediation walkthrough

Both files are synthetic snapshots. The tool evaluates them; it does not change cloud configuration.

| Finding | Change represented in the remediated fixture | Live verification required |
|---|---|---|
| Missing MFA | Workforce MFA enabled | Approved sign-in policy and enrollment confirmed |
| Dormant privileged identity | Identity disabled | Access denied and owner approval recorded |
| Stale active key | Old key inactive | Old credential fails; replacement workload succeeds |
| Broad permissions | Explicit task actions | Required action allowed; unrelated actions denied |
| Public storage | Public flag disabled | Anonymous access denied; approved consumer works |
| Public SSH | Approved private source | External management denied; private admin path works |
| Missing owner | Owner tag populated | Owner accepts responsibility and allocation reports update |

Encryption is already enabled in both original fixtures; CG-008 is exercised by unit tests. Zero findings in the remediated fixture means no implemented rule fired for the represented scope, not complete compliance.

Use the commands in `../docs/DEMO-GUIDE.md`. Review stable finding IDs to connect a finding with its remediation decision. An exception is not remediation; it remains visible as accepted risk and must expire.
