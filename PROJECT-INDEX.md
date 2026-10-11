# Project index

| Track | Main artifacts | What to explain in an interview |
|---|---|---|
| Cloud engineering | `01-multi-cloud-foundation-iam/terraform/` | Address planning, log delivery, service trust, audit retention, state isolation |
| IAM | `terraform/modules/*/` reader roles; `governance/` | Trust versus permissions, human MFA versus workload identity, scoped access and review |
| Support | `02-cloud-support-reliability-center/tickets/` | Hypothesis, discriminating evidence, minimum approved change, verification |
| SOC | `src/csop/detections.py`; incident-response evidence | Thresholds, time windows, false positives, evidence chronology and containment |
| Automation | `src/csop/audit.py`; CloudGuardian CLI | Input quality, deterministic IDs, exceptions, severity, report safety |
| DevSecOps | `.github/workflows/ci.yml`; `src/csop/plan_policy.py` | Failing gates, policy coverage, artifacts, review and deployment separation |

A ten-minute review: read the evidence statement, run the suite, inspect one security test, inspect one detailed support case, inspect the Terraform module, and discuss one documented limitation.
