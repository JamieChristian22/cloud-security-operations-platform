# Infrastructure Release Checklist

- [ ] Change has a linked business/technical reason.
- [ ] Terraform is formatted and validated.
- [ ] Policy gate passes.
- [ ] CloudGuardian tests pass.
- [ ] Security-sensitive changes have a second reviewer.
- [ ] Blast radius and dependencies are documented.
- [ ] Rollback/recovery procedure is written before production-like apply.
- [ ] No credentials, tokens, or state files are committed.
- [ ] Post-change validation checks are defined.
- [ ] Change record is updated with result and lessons learned.
