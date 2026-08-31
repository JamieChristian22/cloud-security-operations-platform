# Changelog

All notable portfolio changes are documented here. Versions describe the evolution of this simulated lab repository, not releases to a production employer environment.

## [2.2.0] - 2026-08-31
### Added
- Native `terraform test` suites for the root configuration and all three cloud foundation modules.
- Security assertions covering private subnet behavior, public-access blocking, versioning, encryption, Azure inbound-deny controls, Google Cloud public-access prevention, and VPC flow logging.
- `docs/THREAT-MODEL.md` with assets, trust boundaries, STRIDE analysis, MITRE ATT&CK mapping, abuse cases, controls, and residual risks.
- `docs/COST-GOVERNANCE.md` with tagging, budgets, ownership, anomaly handling, right-sizing, retention, and teardown standards.
- `docs/DISASTER-RECOVERY.md` with tiered RTO/RPO objectives, backup controls, recovery sequencing, tabletop scenario, failover decision criteria, and validation steps.
- Terraform tests added to the repository-level CI security gate.

### Changed
- Root README and evidence map now surface threat modeling, disaster recovery, cost governance, and IaC test coverage.
- IaC validation guidance now distinguishes static validation, native Terraform tests, security scanning, and authenticated deployment testing.

## [2.1.0] - 2026-08-31
### Added
- Reusable AWS, Azure, and GCP Terraform modules.
- Development and production variable examples.
- TFLint, Checkov, and Gitleaks validation controls.
- IaC operating model, review checklist, rollback plan, release checklist, and change record.

## [2.0.0] - 2026-08-31
### Added
- 40 completed cloud-support incidents and 8 operational runbooks.
- Three runnable security detections and a complete credential-compromise incident package.
- CloudGuardian security auditing tool, unit tests, remediation workflow, and generated reports.
- Repository-level GitHub Actions validation workflow.
- Recruiter quick-start, portfolio evidence map, executive case study, and career materials.

## [1.0.0] - 2026-08-31
### Added
- Initial five-project Cloud Security & Operations Platform structure.
- Multi-cloud IAM, support, security operations, automation, and DevSecOps project foundations.
