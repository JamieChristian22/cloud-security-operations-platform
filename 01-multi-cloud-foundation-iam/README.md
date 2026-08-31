# Project 01 — Multi-Cloud Foundation & IAM

## Executive Summary
Northstar Digital Services needs one consistent access and infrastructure baseline across AWS, Azure, and GCP. This project demonstrates how cloud foundations, identity governance, network segmentation, ownership, and change control fit together before applications are deployed.

## Business Requirements
- Support 750 simulated users across Engineering, IT, Security, Finance, Sales, and Support.
- Human access uses groups/roles rather than routine direct permissions.
- Privileged administration is separated from day-to-day workload operations.
- MFA is mandatory for workforce identities.
- Production write access is limited to approved operational roles.
- Public management access is prohibited by default.
- Resources require environment and owner metadata.
- Security/administrative logs are part of the target architecture.
- Infrastructure changes are reviewed in Git before deployment.

## Role Model
| Persona | AWS | Azure | GCP | Guardrail |
|---|---|---|---|---|
| Help Desk | identity read + approved reset workflow | Helpdesk Administrator | viewer | no infrastructure write |
| Cloud Ops | scoped operations role | Contributor on ops RG | compute operator | no org-wide IAM admin |
| Security Analyst | security audit/read | Security Reader | security reviewer | investigation only |
| IAM Admin | scoped identity administration | Privileged Role Administrator | IAM admin scoped | separate admin identity |
| Developer | app-specific role | app RG contributor | project developer | no production IAM |

## Technical Design
The Terraform examples create a private-first network foundation in all three clouds. They intentionally avoid broad public management ingress. The lab demonstrates provider structure and policy intent without claiming live production deployment.

## Governance Deliverables
- `governance/rbac-matrix.csv` — entitlement design by persona.
- `governance/access-review.md` — quarterly recertification process.
- `governance/control-mapping.md` — control objective → lab evidence mapping.
- `runbooks/joiner-mover-leaver.md` — approved lifecycle workflow.
- `validation/security-checklist.md` — pre-deployment review.
- `architecture/multi-cloud-design.md` — account, network, identity, logging, and failure-domain decisions.

## Interview Story
The key tradeoff is **operational capability without uncontrolled privilege**. Cloud Ops can recover workloads, IAM Admin can manage identity, and Security can investigate, but no single normal role is intended to silently administer everything. This reduces blast radius and improves auditability.
