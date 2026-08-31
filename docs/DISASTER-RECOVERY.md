# Disaster Recovery & Service Restoration Plan

## Purpose
This plan defines how the simulated Northstar environment would restore critical cloud operations after a major outage, destructive change, provider incident, ransomware event, or loss of administrative access. It complements incident response: incident response contains and investigates the event; disaster recovery restores business capability to an acceptable level.

## Recovery Objectives
| Service tier | Example capabilities | Target RTO | Target RPO |
|---|---|---:|---:|
| Tier 0 | Identity, privileged access, DNS, core network control, security logging | 1 hour | 15 minutes |
| Tier 1 | Customer-facing application/API, authentication dependencies, critical databases | 4 hours | 1 hour |
| Tier 2 | Internal collaboration, analytics, non-critical integrations | 8 hours | 4 hours |
| Tier 3 | Development/test and non-critical reporting | 24 hours | 24 hours |

These are simulated planning targets. A production organization would validate them against business impact analysis and contractual obligations.

## Recovery Design Principles
- Identity recovery precedes most application recovery because administrators need trustworthy access.
- Infrastructure should be recreated through version-controlled Terraform where practical.
- Terraform state and provider credentials require protected, recoverable storage separate from ordinary workloads.
- Logs and forensic evidence must be preserved before destructive cleanup.
- Backups are only considered valid if restore procedures are tested.
- Recovery prioritizes minimum viable service first, then full performance and secondary features.

## Backup Standard
### Terraform / Configuration
- Git repository is the authoritative IaC source.
- Remote Terraform state should use provider-supported locking/versioning where available.
- State access should be restricted to deployment identities and recovery administrators.
- State backups/version history must be protected from routine deletion permissions.

### Cloud Data
- Critical structured data: point-in-time recovery or scheduled snapshots aligned with RPO.
- Object data: versioning plus lifecycle controls appropriate to business retention.
- Security logs: centralized retention with restricted deletion and separate ownership where possible.
- Microsoft 365/SaaS data: recovery strategy should account for native retention and third-party backup requirements based on risk.

## Disaster Scenarios
### Scenario A — Destructive Terraform Change
**Trigger:** approved or compromised pipeline removes critical networking or service resources.

**Recovery sequence:**
1. Stop additional pipeline execution.
2. Preserve run logs and the exact Terraform plan/commit.
3. Revert to last-known-good commit.
4. Verify remote state consistency and locking.
5. Generate a recovery plan.
6. Restore Tier 0 networking/identity dependencies first.
7. Restore Tier 1 services.
8. Validate monitoring, logging, DNS, and security controls.
9. Conduct post-incident review before reopening routine deployments.

### Scenario B — Credential/Identity Compromise
**Trigger:** privileged account or deployment credential is compromised.

**Recovery sequence:**
1. Use break-glass identity governed outside the compromised session.
2. Revoke active sessions/tokens and disable affected credentials.
3. Rotate deployment secrets and cloud access keys.
4. Inspect role assignments, federation, service principals, IAM policies, API keys, and persistence.
5. Restore expected IAM configuration from reviewed source of truth.
6. Re-enable production access in phases after validation.

### Scenario C — Regional Cloud Service Outage
**Trigger:** provider region degrades or becomes unavailable.

**Decision factors:** outage duration estimate, Tier 0/Tier 1 dependency impact, replication freshness, data consistency, DNS failover readiness, recovery cost, and risk of failback.

**Recovery sequence:** validate secondary-region dependencies → restore/scale minimum viable service → update routing/DNS → validate application health → monitor data consistency → communicate service status → plan controlled failback.

### Scenario D — Ransomware / Destructive Data Event
**Trigger:** mass encryption/deletion or compromised administrator destroys cloud/SaaS data.

**Recovery sequence:** isolate attacker access → preserve evidence → identify clean recovery point → validate backup integrity → restore identity controls → restore critical data into isolated environment → malware/security validation → reconnect production services → monitor for reinfection/persistence.

## Recovery Runbook
### Phase 1 — Declare and Stabilize
- Assign incident commander and recovery lead.
- Record start time, affected services, business impact, and current evidence.
- Stop automated deployments if they may worsen the event.
- Protect logs, snapshots, and forensic artifacts.

### Phase 2 — Restore Administrative Control
- Validate break-glass identities.
- Enforce MFA and rotate compromised credentials.
- Confirm access to DNS, networking, state storage, backups, and logging.

### Phase 3 — Restore Tier 0
- Identity/federation.
- Core networking and routing.
- DNS and certificate dependencies.
- Centralized security/operations telemetry.

### Phase 4 — Restore Tier 1
- Data stores and customer-facing workloads.
- Application secrets/configuration.
- Health checks and ingress paths.

### Phase 5 — Validate
- Authentication and authorization work as expected.
- No unintended public exposure exists.
- Logging and alerting are active.
- Data recovery point is within accepted RPO.
- Service restoration is within or explained against RTO.
- CloudGuardian/security posture checks are rerun.
- Terraform plan shows no unexplained drift.

### Phase 6 — Resume and Improve
- Re-enable pipelines gradually.
- Communicate recovery completion.
- Capture final timeline and data-loss estimate.
- Create corrective actions with owners/dates.

## Tabletop Exercise — Compromised Pipeline + Regional Failure
### Situation
At 09:10, a compromised developer token is used to merge a Terraform change that removes an Azure network control. At 09:18, the primary region experiences a service disruption. Authentication remains available, but customer traffic is failing and the team cannot assume the environment state is trustworthy.

### Expected Team Actions
1. Freeze CI/CD and invalidate the compromised token.
2. Identify the last trusted commit and state version.
3. Review cloud audit logs for additional malicious changes.
4. Use break-glass administrative access.
5. Decide whether recovery in the primary region is safe or secondary-region activation is required.
6. Restore Tier 0 network/security controls from reviewed IaC.
7. Restore Tier 1 service and validate data consistency.
8. Confirm logging and detections are functioning before normal deployment resumes.

### Success Criteria
- Incident commander and recovery lead identified within 15 minutes.
- Compromised token revoked within 20 minutes.
- Trusted infrastructure version identified within 30 minutes.
- Tier 0 control plane recovered within the 1-hour target.
- Tier 1 customer service recovered within the 4-hour target.
- No unexplained privileged roles or public exposures remain after recovery.

## DR Test Evidence Template
For each recovery test record:
- Date and scenario.
- Systems in scope.
- Recovery point used.
- Actual RPO achieved.
- Actual RTO achieved.
- Validation evidence.
- Gaps discovered.
- Corrective action owner and due date.

A production program should exercise Tier 0 and Tier 1 recovery at least semi-annually and after material architectural changes.
