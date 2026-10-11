# Playbook · Suspected cloud credential compromise

## Trigger and ownership

A credible credential exposure, anomalous session or discovery/data-access correlation starts triage. Assign an incident lead and IAM/workload contacts. Determine whether the affected identity is human, service, emergency or shared. Record account, region, key/session identifier, application and business dependencies.

## Preserve and scope

Export relevant audit/sign-in records with UTC timestamps and event IDs. Hash the exports and retain originals in a restricted evidence location. Identify successful and failed actions, resources touched, privilege changes, new credentials and persistence indicators. Confirm logging coverage and missing periods before making a negative-impact claim.

## Decide containment

If exposure is confirmed or credible impact warrants emergency action, use the authorized incident procedure to revoke/disable the affected key or session. Coordinate dependent workloads where time permits. Review alternate credentials, role sessions and downstream tokens; disabling one key may not end every existing session. Restrict a network path only after assessing shared infrastructure impact.

## Eradicate and recover

Remove exposed material from current code/configuration, rotate affected secrets, and review repository history privately as appropriate. Prefer workload federation or short-lived sessions. Correct permission scope and trust. Verify the old credential fails and the replacement workload path succeeds. Confirm audit events continue to arrive.

## Close with evidence

Record actual containment time, evidence used, access tests, residual uncertainty, communication and owner-assigned follow-ups. Do not calculate response metrics from authored timestamps. For this portfolio use the clearly labeled synthetic timeline and report.

## Escalation triggers

Escalate immediately for privileged access, persistence, sensitive-data access, unclear blast radius, compromised logging or cross-account movement. Preserve the evidence before destructive remediation when practical, without delaying necessary containment of active harm.
