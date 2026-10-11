# Upgrade gap closure and acceptance register

| Original gap | Delivered change | Acceptance evidence | Remaining boundary |
|---|---|---|---|
| Missing requirements and Makefile | Pinned development dependencies and supported task commands | Offline suite and unit tests | Dependency updates still need review |
| Missing CI | `.github/workflows/ci.yml`, artifact retention, explicit permissions | YAML/structure validation; locally executed tools where recorded | Hosted run and required branch checks must be enabled after upload |
| Terraform compressed syntax | Reformatted modules and actual provider-schema validation | Terraform logs in evidence directory | Mock results do not prove a real apply |
| Audit destruction risk | `force_destroy=false`, prevent_destroy on protected audit stores/KMS | Configuration tests and inspection | Privileged operators can edit code; provider policy is a separate layer |
| Logging existed mainly as storage | AWS trail/flow logs, Azure subscription diagnostics, GCP audit sink/config | Provider validation and mock tests | Live event arrival and permissions require account testing |
| IAM was mostly documentation | Optional explicit reader principals for AWS/Azure/GCP | Scoped policy definitions and validation | Identity lifecycle/MFA administration remains organization-specific |
| Weak travel detection | Haversine distance, UTC sorting, deduplication, trusted-network suppression | Regression tests | IP-to-location enrichment must be trusted and reviewed |
| Unbounded password-spray counting | Distinct users in rolling windows; subsequent success correlation | Negative, timing and correlation tests | Threshold tuning requires real telemetry |
| Limited auditor | Eight controls, wildcards, IPv6, ranges, expiry-aware exceptions, safe reports | CLI and unit tests | No full IAM-policy or network-reachability solver |
| JSON-only proposed-change gate | Added Terraform JSON plan policy with explicit coverage | Plan fixtures and tests | Unknown values fail for reviewed types; uncovered types require other controls |
| Generic ticket/runbook detail | Eight expanded runbooks and detailed exercise packets | Evidence/decision/retest structure | Synthetic examples are not console transcripts |
| Old generated reports | Regenerated reports plus validation evidence and provenance | Latest suite output | Report time reflects actual execution environment |

The standard is inspectable behavior and honest evidence. A portfolio rating is subjective; this register avoids claiming a guaranteed score or production certification.
