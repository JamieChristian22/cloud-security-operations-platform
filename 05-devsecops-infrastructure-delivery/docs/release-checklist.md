# Release acceptance

- Reproduce the offline suite and inspect findings, not only exit codes.
- Run Terraform root/module validation and mock tests in a supported environment.
- Review Checkov results and each resource-scoped exception.
- Run TFLint and Gitleaks; review the actual scope of the secret scan.
- Confirm generated evidence matches this revision and no real credentials/state are included.
- Review infrastructure plans for unknown values, uncovered policy types, IAM/trust, deletion, replacement, retention and cost.
- Record accountable reviewer, target environment, approved maintenance window and rollback.
- Verify hosted Actions after upload; require appropriate checks through branch protection.
- Deploy only through separately approved credentials and process, then complete live acceptance.

A completed lab checklist is not an organizational approval. Do not prefill reviewer names or passed live results.
