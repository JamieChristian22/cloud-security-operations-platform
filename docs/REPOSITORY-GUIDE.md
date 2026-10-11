# Repository guide

Start with `README.md`, `PROJECT-INDEX.md`, and `PORTFOLIO-EVIDENCE.md`. Use `docs/DEMO-GUIDE.md` for the runnable narrative. Validation output is in `evidence/validation/`; operational exercise inputs are in each project folder.

Cloud support reviewers should prioritize the eight `case-studies/` packets and runbooks. Security reviewers should inspect the shared engine, data contract, detection specifications, input/negative tests and evidence boundaries. Cloud engineering reviewers should inspect provider modules, optional reader assignments, protected audit resources and the deployment acceptance guide. Delivery reviewers should inspect CI permissions, scanners, exceptions and plan-policy coverage.

The original broad governance documents are retained as design references. Implemented scope and validation status are authoritative in the v2 evidence and deployment documents; a design objective is not a claim of deployed enforcement.
