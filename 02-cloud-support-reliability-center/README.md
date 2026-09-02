# Project 02 — Cloud Support & Reliability Center

## Scenario
A simulated cloud support queue receives identity, networking, compute, storage, monitoring, Linux, Microsoft 365, Google Cloud, Terraform, backup, security, and CI/CD incidents. The goal is service restoration **plus** evidence-backed RCA and prevention.

## Operating Model
- **P1:** widespread outage/security-critical — 15-minute response target.
- **P2:** major degradation/multiple users — 30-minute response target.
- **P3:** single-user or limited impact — 4-business-hour response target.
- **P4:** request/how-to — 1-business-day response target.

## Evidence
- `tickets/` contains **40 resolved incidents** with impact, evidence, commands, RCA, fix, validation, prevention, and customer communication.
- `data/tickets.csv` is the source dataset.
- `scripts/ticket_metrics.py` computes closure rate, average resolution time, SLA attainment, priority distribution, category distribution, and repeat causes.
- `RCA-TRENDS.md` groups incidents into broader systemic themes.
- `runbooks/` contains eight reusable operational procedures.

## Troubleshooting Method
1. Confirm scope and business impact.
2. Separate authentication, authorization, DNS, network, compute, storage, and application layers.
3. Form the smallest testable hypothesis.
4. Gather evidence before making a change.
5. Apply the least-risk remediation.
6. Validate from the user/service perspective.
7. Record root cause, prevention, and communication.

## Interview Story
The value of the queue is not ticket volume. It shows a repeatable diagnostic approach and demonstrates how operational lessons become runbooks, monitoring changes, access controls, and automated policy checks.
