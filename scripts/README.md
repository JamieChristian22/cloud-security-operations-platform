# Automation & Control Scripts

This directory is the runnable automation layer for the **Cloud Security & Operations Platform**. It turns the repository from a documentation-only portfolio into an inspectable, repeatable lab that can be executed without AWS, Azure, or Google Cloud credentials.

All inputs are synthetic and deterministic. No secrets, tokens, customer data, or employer production data are required.

## What the automation covers

| Area | Script | What it evaluates | Output |
|---|---|---|---|
| IAM governance | `iam/access_review.py` | MFA, dormant accounts, stale credentials, privileged-account controls | `reports/iam_access_review.json` |
| Security posture | `security/baseline_audit.py` | public exposure, encryption, logging, recovery, tagging | `reports/security_baseline.json` |
| Threat detection | `security/run_detections.py` | credential compromise, password spray, impossible travel | `reports/detection_results.json` |
| Cost governance | `finops/cost_guardrails.py` | budget use, high-cost resources, cost-center ownership | `reports/cost_guardrails.json` |
| Disaster recovery | `dr/readiness_check.py` | backups, RPO alignment, restore-test freshness, replication | `reports/dr_readiness.json` |
| Support operations | `operations/ticket_metrics.py` | resolution rate, average resolution time, SLA attainment, severity mix | `reports/support_metrics.json` |
| IaC review | `iac/terraform_guard.py` | Terraform source scanning and optional local CLI checks | user-selected output |
| Repository QA | `automation/portfolio_validate.py` | required artifacts and unfinished-marker detection | `reports/portfolio_validation.json` |
| Full suite | `automation/run_all.py` | orchestrates ten offline checks, including project tests and policy gates | `reports/automation_summary.json` |

## Quick start

From the repository root:

```bash
python3 -m pip install -r requirements-dev.txt
python3 scripts/automation/run_all.py
```

macOS/Linux users can also run:

```bash
bash scripts/run.sh
```

Windows PowerShell users can run:

```powershell
./scripts/run.ps1
```

## Expected behavior

The included datasets deliberately contain some **security and governance findings**. A finding is not the same thing as a failed automation run. The controls are designed to identify and report risks correctly; tests verify that those findings are detected as expected.

The complete orchestration suite returns success only when the scripts execute correctly, the project detections behave as designed, the policy gate passes its approved sample change, the unit tests pass, and repository completeness checks succeed.

## Design principles

1. **Reproducible:** every result comes from committed code and committed synthetic data.
2. **Credential-free:** reviewers can execute the automation locally without cloud accounts.
3. **Explainable:** findings contain severity, evidence, remediation, and control rationale where applicable.
4. **CI-friendly:** scripts return meaningful exit codes and produce machine-readable JSON.
5. **Auditable:** generated reports are preserved as evidence and can be compared after code changes.
6. **Honest:** these scripts model production-style operational controls but do not claim production access or employer experience.
