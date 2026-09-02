# Automation Control Catalog

This document maps the repository's executable controls to the operational risks they address. The purpose is to show not only that scripts exist, but why each one matters in a cloud operations and security program.

## Control catalog

| Control | Risk addressed | Evidence source | Automated action | Operational response |
|---|---|---|---|---|
| IAM MFA review | account takeover through weak authentication | synthetic identity inventory | flags active users without MFA | enforce MFA; block privileged access until remediated |
| Dormant account review | unused identities retaining access | last-login age | identifies stale active accounts | validate owner and disable unnecessary access |
| Credential-age review | long-lived keys increasing exposure window | access-key age | flags credentials older than policy threshold | rotate/revoke and prefer short-lived credentials |
| Public exposure check | accidental internet exposure | normalized resource inventory | identifies resources marked public | remove public access or document approved exception |
| Encryption-at-rest check | unauthorized data disclosure | encryption state | flags unencrypted resources | enable provider-managed or customer-managed encryption |
| Audit logging check | insufficient forensic visibility | logging state | flags disabled logging | enable centralized service/access logging |
| Recovery check | inability to restore business data | backup/versioning state | flags missing recovery protection | enable backup/versioning based on criticality |
| Cost threshold review | spend growth without owner review | monthly estimates | flags high-cost resources and missing cost tags | right-size, schedule, reserve, or assign ownership |
| DR backup/RPO review | backups not meeting business recovery objectives | backup age and RPO | compares backup freshness to RPO | investigate failed backup jobs and run protected backup |
| DR restore-test review | backups existing but being unusable | days since restore test | flags stale critical-service tests | perform and document restore validation |
| Credential-compromise detection | suspicious authentication or credential use | synthetic security events | runs detection logic and asserts alert generation | revoke sessions, disable credentials, scope impact |
| Password-spray detection | distributed password guessing | synthetic sign-in events | identifies repeated failures across identities | block source, investigate targets, strengthen authentication |
| Impossible-travel detection | implausible session geography | synthetic sign-in events | correlates distant sign-ins over short intervals | challenge/revoke session and investigate account |
| DevSecOps policy gate | insecure infrastructure reaching deployment | proposed-change JSON | blocks public admin ports, public storage, wildcard admin actions | revise change before approval |
| Terraform source guard | high-risk IaC patterns | Terraform files | scans broad CIDRs and possible hard-coded secrets; optionally runs Terraform CLI checks | review findings before merge |
| Portfolio completeness | incomplete evidence or unfinished artifacts | repository tree | checks required artifacts and unfinished markers | correct repository before publishing |

## Control philosophy

The automation follows a **detect → explain → remediate → validate** model. Scripts do not silently change infrastructure. They surface findings with enough evidence for a human operator to decide whether the condition is expected, risky, or requires an exception.

That choice is intentional: production operations often separate detection from mutation so that high-impact security or infrastructure changes remain auditable and approval-driven.

## Evidence and reproducibility

The default datasets in `scripts/sample_data/` are deterministic. This makes the behavior reproducible for a reviewer and suitable for CI. The data includes both compliant and intentionally risky conditions so that detection logic can demonstrate positive findings instead of only returning an empty report.

The repository's central validation command is:

```bash
python3 scripts/automation/run_all.py
```

Its machine-readable summary is written to `scripts/reports/automation_summary.json`.
