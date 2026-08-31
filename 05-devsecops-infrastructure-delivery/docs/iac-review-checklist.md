# IaC Pull Request Review Checklist

- [ ] `terraform fmt -recursive -check` passes.
- [ ] `terraform init -backend=false` and `terraform validate` pass.
- [ ] TFLint reports no blocking issues.
- [ ] Checkov reports no blocking IaC findings or an exception is documented.
- [ ] Secret scan passes; no keys, tokens, state, plans, or real tfvars are committed.
- [ ] Network exposure is justified and least-privilege.
- [ ] Storage public access, encryption and versioning are explicitly controlled.
- [ ] Logging/retention requirements are represented.
- [ ] Inputs/outputs and module boundaries remain understandable.
- [ ] Change record describes risk, validation, blast radius and rollback.
- [ ] Any live apply requires protected-environment approval.
