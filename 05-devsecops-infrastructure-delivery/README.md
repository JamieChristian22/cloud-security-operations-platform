# Project 05 — DevSecOps Infrastructure Delivery

## Problem
Infrastructure changes can introduce public storage, exposed management ports, wildcard administrative permissions, invalid Terraform, or undocumented operational risk. This project treats security and change quality as **pre-merge controls**.

## Active Pipeline
The executable workflow is at the repository root: `.github/workflows/ci.yml`. GitHub only executes workflows from that root location.

Pipeline stages:
1. support analytics execution;
2. three security detection scripts;
3. policy-as-code validation;
4. CloudGuardian unit tests;
5. Terraform format;
6. Terraform init without backend;
7. Terraform validate;
8. human review/approval for any real production-like deployment.

## Security Gate
`policy/policy_check.py` rejects normalized proposed changes that contain:
- public protected storage;
- SSH/RDP exposed to `0.0.0.0/0`;
- wildcard administrative actions.

## Change Management Evidence
`changes/CHG-2026-017.md` shows a risky public-storage proposal being rejected, corrected, retested, and documented rather than bypassing the guardrail.

## Operational Controls
- `docs/release-checklist.md` — pre-release evidence checklist.
- `docs/rollback-plan.md` — rollback/recovery strategy.
- `docs/pull-request-template.md` — reviewer prompts.

## Interview Story
The core principle is that a pipeline should not merely report insecurity after release. It should stop known unsafe patterns **before deployment**, preserve review evidence, and keep rollback possible.
