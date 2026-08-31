# Playbook — Compromised Cloud Credential
## Triage
Confirm credential owner, first/last suspicious use, source, actions, affected resources, and whether privileged or data-access actions succeeded.
## Contain
Disable/revoke credential immediately; revoke sessions where applicable; apply temporary restrictive policy if identity must remain available; preserve logs.
## Investigate
Search identity, storage, compute, IAM, network, and audit activity for the compromise window. Distinguish enumeration from successful modification or exfiltration.
## Recover
Issue approved replacement only after the endpoint/account is trusted, restore least-privilege access, and validate workloads.
## Prevent
Prefer federation/short-lived credentials, secret scanning, MFA, permission boundaries, key-age alerts, and anomalous-source detection.
