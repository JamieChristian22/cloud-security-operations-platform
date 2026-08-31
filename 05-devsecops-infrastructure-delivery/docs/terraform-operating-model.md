# Terraform Operating Model

## Workflow
1. Engineer creates a feature branch and changes a module or environment input.
2. Local preflight: `terraform fmt -recursive`, `terraform init -backend=false`, `terraform validate`.
3. Pull request triggers TFLint, Checkov, secret scanning, policy checks and unit tests.
4. Reviewer evaluates the plan/change record, blast radius, least privilege and rollback path.
5. Production apply would require protected-environment approval and authenticated short-lived credentials. This portfolio intentionally does not auto-apply to live accounts.

## State strategy
Production organizations should use encrypted remote state with locking/versioning and tightly scoped access. State may contain sensitive infrastructure metadata; local state is gitignored. Backend credentials must never be committed.

## Drift and recovery
Run scheduled `terraform plan -detailed-exitcode` in an authenticated environment to identify drift. Investigate drift before reconciliation. Rollback is performed by reverting the reviewed configuration to a known-good commit and applying a reviewed plan; do not edit state manually except under an approved recovery procedure.

## Module standards
Modules expose typed variables and useful outputs, carry standard tags/labels where supported, avoid embedded credentials, apply security defaults, and use validation for policy-critical inputs such as retention.
