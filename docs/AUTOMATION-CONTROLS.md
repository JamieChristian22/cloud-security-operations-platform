# Automation control map

| Stage | Input | Output | Gate meaning |
|---|---|---|---|
| IAM review | sample_data/iam_users.json | IAM findings | Demonstrates review behavior; report may need remediation |
| Baseline | sample_data/resources.json | Resource findings | Demonstrates public/encryption/logging/tag checks |
| FinOps | sample_data/resources.json | Cost guardrail report | Fixture estimate, not a cloud billing integration |
| DR | sample_data/dr_assets.json | Recovery readiness report | Metadata assessment, not a restore drill |
| Support analytics | Synthetic tickets.csv | Resolution/SLA aggregates | Describes fixture only |
| Detection replay | Synthetic JSONL | Alerts with event IDs | Known-positive expectation, plus benign unit tests |
| Normalized policy | Safe proposed inventory | PASS/FAIL | Blocks open High/Critical findings |
| Python tests | Inputs and edge cases | JUnit and test summary | Software assertions pass |
| CloudGuardian | Paired inventory snapshots | Before/after reports | Remediated fixture passes High threshold |
| Completeness | Repository files | Missing/link report | Required paths and local links exist |
| Infrastructure CI | Terraform and plan artifacts | Validation/scanner reports | Separate provider and security stages |

`run_all.py` aggregates offline stages and exits nonzero if a stage fails. The report distinguishes fixture assessment from real environment state. Its subprocesses are local code; it neither applies infrastructure nor sends messages.
