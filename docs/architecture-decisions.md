# Architecture Decision Records

## ADR-001 — Centralized identity first
**Decision:** Use Entra ID as the conceptual workforce identity provider and federate access to cloud platforms.  
**Reason:** Central lifecycle controls, MFA enforcement, simpler offboarding, and fewer unmanaged credentials.  
**Tradeoff:** Identity-provider outage becomes high impact, so break-glass access and monitoring are required.

## ADR-002 — Infrastructure as code
**Decision:** Terraform is the source of truth for reproducible infrastructure examples.  
**Reason:** Peer review, drift reduction, repeatability, and auditability.  
**Tradeoff:** State and secrets require separate production-grade controls not emulated in this portfolio.

## ADR-003 — No real secrets in Git
All examples use placeholders only for credential values; code is designed to run against sample data by default. `.gitignore` excludes state, environment files, keys, and generated reports.
