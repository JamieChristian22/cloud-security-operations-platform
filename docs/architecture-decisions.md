# Architecture decisions

## ADR-001 · Shared normalized security engine

Decision: use one Python engine for inventory assessment and the normalized policy gate. This prevents threshold drift between a report and a blocking control. Collection is separate and must publish its scope. A normalized record does not capture every cloud-specific semantic; effective IAM/network analysis remains outside this engine.

## ADR-002 · Terraform root plus independently testable modules

Decision: preserve the multi-cloud learning root while testing each provider module independently. This supports code review without credentials. Organizational deployment should split state by cloud/environment to reduce shared blast radius and credential coupling.

## ADR-003 · Explicit evidence levels

Decision: label unit-tested, mocked, synthetic and live evidence separately. Cached reports never prove a live deployment. CI YAML demonstrates a delivery design until a hosted run is observed. This improves the credibility of interview claims.

## ADR-004 · Protected audit retention

Decision: prevent routine destruction of audit stores and KMS keys and disable forced bucket deletion. Retention is configurable within supported bounds. Immutable retention locks and cross-region replication are deferred to explicit organizational design because they affect cost, deletion and recovery obligations.

## ADR-005 · Focused policy plus broad static scanning

Decision: implement understandable Python plan checks and run Checkov separately. Report uncovered resource types. Unknown values fail review for supported types. This trades convenience for visible uncertainty and avoids presenting a small custom policy as complete infrastructure security.

## ADR-006 · Manual deployment boundary

Decision: CI runs validation and uploads artifacts, with read-only repository permissions. It never applies infrastructure. Deployment identity, account targeting and approvals are established separately. The portfolio can therefore be exercised safely without giving the test workflow cloud credentials.
