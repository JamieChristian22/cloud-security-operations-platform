# Cloud Cost Governance & FinOps Operating Standard

## Purpose
Cost governance is part of operational reliability. Unowned or poorly tagged resources increase waste, weaken incident ownership, and make secure teardown harder. This standard defines how the simulated Northstar environment would control cloud spend across AWS, Azure, and GCP.

## Governance Principles
1. Every billable resource has an accountable owner.
2. Environment and business purpose are visible through standard metadata.
3. Budgets and anomalies are reviewed before they become material overruns.
4. Non-production resources are intentionally short-lived where possible.
5. Logging/security retention is optimized without weakening required controls.
6. Cost reductions must not bypass security, resilience, or audit requirements.

## Required Tags / Labels
The Terraform root already establishes a shared metadata baseline:

| Key | Example | Purpose |
|---|---|---|
| `Project` | `cloud-security-operations-platform` | Workload grouping |
| `Environment` | `dev`, `stage`, `prod` | Lifecycle and risk classification |
| `ManagedBy` | `Terraform` | Ownership of configuration changes |
| `DataClass` | `Internal` | Data handling context |
| `Owner` | `cloud-operations` | Operational accountability |
| `CostCenter` | `LAB-001` | Chargeback/showback grouping |

In production, additional labels would include application/service, business unit, criticality, backup policy, and expiration date for temporary resources.

## Budget Model
### Development / Lab
- **Monthly target:** $25–$50 per sandbox, depending on services enabled.
- **Alert thresholds:** 50%, 80%, and 100% of monthly target.
- **Action at 80%:** identify top contributors, stop unused compute, confirm logging/storage growth.
- **Action at 100%:** freeze non-essential resource creation until owner review.

### Production Example
A real organization would define workload-specific budgets from historical baseline and forecast. Security, backup, logging, and availability requirements must be explicitly represented so teams do not reduce required controls solely to hit a cost target.

## Cost Anomaly Workflow
1. Detect unexpected daily or weekly spend increase.
2. Confirm whether the increase corresponds to approved deployment/change activity.
3. Identify account/subscription/project, service, region, and owner.
4. Compare usage, unit price, and resource count to the previous baseline.
5. Check common causes: runaway compute, log ingestion spike, storage growth, data egress, abandoned snapshots/disks, duplicated environments.
6. Contain obvious waste if safe to do so.
7. Document root cause and expected recurring cost.
8. Update budget or architecture only after owner/security review.

## Resource Lifecycle Standards
### Compute
- Stop or schedule non-production VMs/instances when not needed.
- Prefer right-sized instance families based on measured CPU/memory patterns.
- Remove orphaned instances after ownership validation.

### Storage
- Apply lifecycle policies for audit/log data based on required retention.
- Remove unattached disks after recovery-window review.
- Expire temporary exports and build artifacts.
- Preserve backups needed to meet RPO/RTO requirements.

### Networking
- Review unnecessary public IPs, NAT gateways, load balancers, and high-volume egress.
- Data-transfer architecture should be evaluated before moving large datasets across clouds/regions.

### Logging and Security
- Retain enough telemetry for incident response and compliance objectives.
- Filter known-noise sources before ingestion where operationally safe.
- Use tiered retention/archival instead of deleting valuable security evidence prematurely.

## Environment Teardown Checklist
Before deleting a lab or non-production environment:
1. Confirm no production dependency references the environment.
2. Export required logs/reports.
3. Preserve configuration/state evidence needed for troubleshooting or audit.
4. Confirm backup retention obligations.
5. Run `terraform plan -destroy` and review the complete impact.
6. Require owner approval for shared resources.
7. Destroy through Terraform rather than manual console deletion where possible.
8. Reconcile provider consoles for orphaned resources.
9. Confirm residual storage, IPs, snapshots, keys, and monitoring resources are removed or intentionally retained.

## Monthly FinOps Review
| Review area | Question | Action if unhealthy |
|---|---|---|
| Ownership | Are resources tagged and attributable? | quarantine or assign owner |
| Idle capacity | Are resources unused for 7–30 days? | stop/right-size/remove |
| Storage growth | Is growth expected and retained intentionally? | lifecycle/archive/clean up |
| Logging | Are high-volume sources valuable? | tune collection without losing required evidence |
| Network egress | Has cross-region/cloud transfer increased? | redesign path or caching strategy |
| Budget variance | Is actual spend within forecast? | investigate and reforecast |
| Commitment usage | Are reserved/committed resources actually used? | rebalance commitment strategy |

## Security Guardrail
Cost optimization is not an authorization to weaken MFA, logging, encryption, backups, network segmentation, public-access controls, vulnerability scanning, or incident-response evidence collection.
