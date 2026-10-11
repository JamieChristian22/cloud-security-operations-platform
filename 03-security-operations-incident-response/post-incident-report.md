# Post-incident review · IR-2026-004

**Synthetic exercise.** No real credential was exposed or revoked. The API-event fixture is dated August 20, 2026. The sign-in fixture is a separate August 31 exercise and is not merged into this incident timeline.

## Evidence-supported narrative

At 14:01 UTC the fixture records an ordinary object read by dev-jlee from 198.51.100.24. At 14:08:10 the same identity appears from 203.0.113.77 and issues GetCallerIdentity, followed by ListBuckets, a denied ListRoles, and DescribeInstances. Three distinct discovery APIs within ten minutes meet DET-003. This is a reconnaissance signal requiring review, not proof that a credential was stolen.

At 14:19:01 a later ListBuckets from that source is denied. The fixture does not include a key-deactivation API, so denial alone cannot establish that revocation occurred. The tabletop playbook describes how an analyst would contain confirmed compromise.

## Impact assessment

The supplied records show discovery requests and one successful object read from the earlier source. They do not establish complete activity coverage, sensitive-data access, persistence or exfiltration. “No exfiltration observed in the provided sample” is narrower than “no exfiltration occurred.”

## Root-cause hypothesis

The exercise hypothesis is exposed long-lived credentials. Confirmation requires key/session identity, credential provenance, ownership confirmation and a review of where the credential was stored. The six-record fixture alone does not prove the exposure mechanism.

## Response decision

Preserve evidence and validate the principal. If compromise is confirmed, revoke or disable the affected credential using approved emergency access, assess active sessions and dependent workloads, and verify the old credential fails. Do not rely on repository deletion alone to invalidate a secret.

## Corrective actions and acceptance

| Action | Responsible role | Acceptance evidence |
|---|---|---|
| Rotate/revoke affected credential | IAM owner | Old credential denied; replacement workload path succeeds |
| Preserve incident artifacts | Incident analyst | Export manifest and hashes; restricted originals retained |
| Replace routine long-lived use | Workload owner | Tested federated/short-lived identity flow |
| Add code secret scanning | Delivery owner | Seeded test fixture detected; clean commit passes |
| Tune discovery rule | Detection owner | Known-positive replay alerts; approved inventory activity reviewed |
| Review privilege | Service and IAM owners | Explicit read/write tests at required resource scope |

These roles and acceptance steps are part of the exercise. No organizational approval or completed production remediation is asserted.
