# Threat Model — Northstar Cloud Security & Operations Platform

## Purpose
This threat model evaluates the simulated Northstar Digital Services environment represented by this portfolio. It is intended to show how security requirements are derived from assets, data flows, trust boundaries, attacker goals, and business impact rather than added as isolated controls.

Northstar is a fictional 750-user remote-first SaaS organization. The threat model assumes a mixed workforce and service environment spanning AWS, Azure/Microsoft 365, and Google Cloud, with Terraform-based infrastructure delivery and centralized operational/security telemetry.

## Security Objectives
The environment is designed around six objectives:

1. Prevent unauthorized access to workforce and cloud identities.
2. Prevent direct public exposure of private workloads and security data.
3. Preserve confidentiality and integrity of logs, audit evidence, and infrastructure state.
4. Detect credential misuse and suspicious authentication behavior quickly.
5. Limit blast radius through least privilege, segmented access, and change controls.
6. Recover critical services and security telemetry within documented recovery objectives.

## Critical Assets
| Asset | Why it matters | Primary security concern |
|---|---|---|
| Workforce identities | Access to SaaS, cloud consoles, email, and administrative functions | Account takeover and privilege misuse |
| Privileged cloud roles | Can alter IAM, networking, logging, and workloads | Privilege escalation and persistence |
| Terraform state | May contain infrastructure metadata and sensitive references | Disclosure, tampering, destructive changes |
| Audit/log storage | Supports detection, forensics, and accountability | Deletion, alteration, or loss of evidence |
| Cloud networks | Control workload reachability and segmentation | Unauthorized ingress/egress |
| CI/CD pipeline | Can alter infrastructure at scale | Supply-chain compromise and malicious deployment |
| Microsoft 365 / collaboration data | Business communications and files | Phishing, token theft, data exfiltration |
| CloudGuardian findings/reports | Security posture evidence | Tampering or disclosure of weaknesses |
| Backup/recovery artifacts | Required to restore service after failure | Deletion, encryption, or unusable recovery data |

## Trust Boundaries
### Boundary 1 — User Device to Identity Provider
Users authenticate from managed or unmanaged endpoints into the identity plane. Risk includes credential theft, session-token replay, impossible travel, password spraying, and MFA fatigue.

### Boundary 2 — Identity Provider to Cloud Control Planes
Federated identities and privileged roles cross from identity services into AWS, Azure, and GCP. Incorrect role mapping or excessive permissions can increase blast radius.

### Boundary 3 — Public Internet to Cloud Networks
Cloud workloads and management endpoints must avoid unnecessary direct exposure. Private subnets, NSGs/security groups, firewall rules, and platform access controls enforce this boundary.

### Boundary 4 — CI/CD to Infrastructure Control Planes
GitHub Actions and Terraform can create or modify infrastructure. Pull-request review, validation, policy scanning, secret scanning, and controlled credentials reduce supply-chain and change risk.

### Boundary 5 — Cloud Services to Central Telemetry
Logs and security events leave workload/control-plane sources and enter centralized audit destinations. Integrity, retention, and availability are critical because response quality depends on trustworthy telemetry.

### Boundary 6 — Operations Personnel to Recovery Systems
Backup, restore, and incident-containment actions often require elevated access. Access must be limited, auditable, and separate from routine user permissions.

## STRIDE Analysis
| Threat | Example in this environment | Impact | Primary mitigations in repository |
|---|---|---|---|
| Spoofing | Stolen workforce credential used from a new geography | Unauthorized cloud/M365 access | MFA, conditional access concepts, anomaly detections, session revocation playbook |
| Tampering | Malicious Terraform change weakens a firewall rule | Exposure or persistence | PR review, Terraform tests, Checkov, TFLint, policy gate, rollback plan |
| Repudiation | Administrator denies making a high-risk change | Weak accountability | Central logging, change records, Git history, incident timeline |
| Information Disclosure | Public storage bucket exposes logs or data | Data loss / regulatory impact | Public-access prevention, private networking, encryption, CloudGuardian checks |
| Denial of Service | Misconfiguration or resource exhaustion makes service unavailable | Customer/business interruption | Monitoring, runbooks, incident process, DR plan, rollback procedures |
| Elevation of Privilege | Wildcard IAM permission allows broader administrative access | Expanded blast radius | Least privilege, RBAC matrix, access reviews, CloudGuardian wildcard detection |

## High-Priority Abuse Cases
### AC-01 — Credential Compromise
**Attack path:** phishing/token theft → successful sign-in → cloud console access → enumeration → privilege attempt → data access.

**Detection evidence:** new geography, unusual source IP, suspicious API usage, authentication anomalies.

**Response:** revoke sessions, disable/reset credential, remove malicious persistence, review IAM changes, rotate exposed secrets, validate affected resources, document blast radius.

### AC-02 — Password Spray
**Attack path:** attacker tests a small set of common passwords across many users.

**Detection evidence:** many failed sign-ins across distinct accounts from a shared source in a short window.

**Response:** block source where appropriate, enforce MFA, inspect successful follow-on authentication, reset affected accounts, review sign-in risk.

### AC-03 — Over-Permissive IAM
**Attack path:** legitimate or compromised account receives wildcard permissions and accesses resources beyond job need.

**Detection evidence:** access review, CloudGuardian wildcard policy finding, unusual privileged API events.

**Response:** replace wildcard actions/resources with scoped roles, remove direct grants, document ownership and approval.

### AC-04 — Public Cloud Storage
**Attack path:** bucket/container becomes public through configuration drift or deployment change.

**Detection evidence:** CloudGuardian finding, IaC policy scan, cloud configuration alert.

**Response:** block public access, validate ACL/policy state, inspect access logs, rotate exposed data/secrets if necessary.

### AC-05 — CI/CD Supply-Chain Change
**Attack path:** malicious commit or compromised developer account alters Terraform or workflow logic.

**Detection evidence:** PR diff, branch protection, policy/test failure, secret scan, unexpected plan output.

**Response:** block merge, revoke compromised token, revert commit, re-run security tests, review recent pipeline executions.

### AC-06 — Destruction of Audit Evidence
**Attack path:** privileged attacker deletes or shortens retention of logs to reduce forensic visibility.

**Detection evidence:** configuration-change audit events and retention drift.

**Response:** restore expected configuration through IaC, preserve remaining logs, investigate privileged activity, increase separation of duties.

## MITRE ATT&CK Mapping
| Technique | Relevance | Portfolio control/evidence |
|---|---|---|
| T1078 Valid Accounts | Compromised identities can access cloud services | credential-compromise detection and playbook |
| T1110.003 Password Spraying | Distributed authentication attack | password-spray detection |
| T1098 Account Manipulation | Attacker may add credentials or role assignments | IAM review and incident containment process |
| T1548 Abuse Elevation Control Mechanism | Excessive roles can enable privilege escalation | least-privilege design and CloudGuardian checks |
| T1530 Data from Cloud Storage | Public/mis-scoped storage can expose data | storage controls and public-access checks |
| T1562.008 Disable or Modify Cloud Logs | Attackers may impair logging | centralized log retention and governance |
| T1588.006 Obtain Capabilities: Vulnerabilities | Relevant to supply-chain/cloud change risk | scanning and controlled delivery pipeline |

## Security Requirements Derived from the Model
- No automatic public IP assignment on AWS private subnets.
- AWS audit storage must block public ACLs/policies, use server-side encryption, and have versioning enabled.
- Azure private subnet must be associated with an NSG containing an explicit internet-inbound deny rule.
- GCP subnet must use VPC flow logging and private Google access.
- GCP audit bucket must enforce uniform bucket-level access and public-access prevention.
- Security log retention must never be configured below 30 days in Terraform modules.
- CI must run format, init/validate, native Terraform tests, TFLint, Checkov, secret scanning, Python tests, and the policy gate before changes are considered releasable.
- High-risk IAM changes require human review and rollback planning.

## Residual Risks
No lab design removes all risk. Remaining risks include compromised endpoints, stolen active sessions, zero-day vulnerabilities, malicious insiders with approved privilege, provider outages, unavailable backups, CI dependency compromise, and human approval mistakes. In a real environment, additional controls would include device compliance, phishing-resistant MFA, PAM/PIM, cloud-native CSPM/SIEM integration, immutable backup tiers, dedicated security accounts/projects/subscriptions, KMS-managed keys, signed artifacts, protected environments, and tested cross-region recovery.

## Review Cadence
Threat modeling should be reviewed after major architecture changes, new identity integrations, changes to CI/CD trust, new internet-facing services, material incidents, or at least quarterly in a production program.
