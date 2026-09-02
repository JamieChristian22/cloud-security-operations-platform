# Repository Review Guide

The portfolio is intentionally organized so a technical reviewer can evaluate it quickly without screenshots or a recorded demo.

## Ten-minute technical review

1. Read the root `README.md` for the business scenario and architecture.
2. Open `01-multi-cloud-foundation-iam/terraform/` to review modular AWS, Azure, and GCP infrastructure plus native Terraform tests.
3. Review any two incidents under `02-cloud-support-reliability-center/tickets/` and compare them with the operational runbooks.
4. Inspect the detection code and evidence under `03-security-operations-incident-response/`.
5. Read `04-cloudguardian-security-auditor/src/cloudguardian.py`, then compare the insecure and remediated reports.
6. Review `.github/workflows/ci.yml` and the security gate under `05-devsecops-infrastructure-delivery/policy/`.
7. Run `python3 scripts/automation/run_all.py` to reproduce the offline checks.

## Role-specific review paths

### Cloud Support / Operations
Focus on Project 02, support metrics, runbooks, RCA trends, Project 01 networking/IAM, and the DR plan.

### Cloud Administrator / Cloud Engineer
Focus on Project 01 Terraform modules, environment separation, state strategy, testing, CI, networking, tagging, and operating standards.

### IAM Analyst
Focus on the RBAC matrix, access review, joiner-mover-leaver runbook, IAM automation, least privilege controls, and identity-related incident response.

### SOC / Security Analyst
Focus on Project 03 detections and timeline, CloudGuardian findings, the threat model, IOC register, containment playbook, and post-incident report.

### DevOps / Platform
Focus on Terraform modules/tests, GitHub Actions, TFLint, Checkov, Gitleaks, policy-as-code, rollback planning, and change-management controls.

## Claims and evidence

All company names, identities, incidents, tickets, metrics, and logs are simulated. The portfolio's value comes from the engineering process and inspectable artifacts, not from claiming that lab work was employer production experience.
