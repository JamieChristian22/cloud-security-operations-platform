# CI blocks public storage change

**Evidence class: synthetic tabletop exercise.** The commands below are a proposed investigation sequence. The observations are authored examples, not captured cloud execution output. Related ticket: [INC-018](../tickets/INC-018.md).

## Impact and initial scope

A proposed configuration fails security checks before release. Assign a case owner, confirm environment and start time, and determine whether other users/services are affected before changing configuration. Escalate immediately if there is evidence of active compromise or critical data loss.

## Competing hypotheses

Primary scenario cause: **Storage public-access setting violates policy**. Alternatives: Scanner parsing problem; expired exception; input schema mismatch. Do not accept the primary cause solely because it appears in this exercise. Gather evidence that distinguishes it from alternatives.

## Investigation commands or console checks

```text
python 05-devsecops-infrastructure-delivery/policy/policy_check.py 05-devsecops-infrastructure-delivery/policy/sample_proposed_change.json
Review the failing resource/control in the actual CI artifact.
```

Shell variables represent account-specific values confirmed by the operator. They are not credentials supplied by this repository. Use read-only collection first and store sensitive output outside Git.

## Illustrative evidence and reasoning

Tabletop unsafe variant sets public=true and yields CG-005 with exit code 1. The committed safe fixture is expected to pass.

This supports the stated root cause within the tabletop scenario. In a live incident, attach timestamped output, correlation IDs and source context; record contradictory evidence instead of discarding it.

## Minimum approved correction

Keep the gate enabled. Correct storage access to the approved private design, or seek a documented expiring exception through the designated review path.

Record change owner, approval, affected resources, expected completion time and stop conditions. Separate emergency containment from permanent correction.

## Positive and negative verification

Unsafe regression remains blocked; corrected fixture passes; authorized consumers retain access.

Record expected and observed results separately. Observe a representative monitoring interval and obtain service-owner confirmation before closure.

## Rollback and escalation

Revert the proposed code change if remediation breaks required behavior; do not disable the scanner to release.

If the discriminating test disproves the primary cause, preserve the evidence and test the next hypothesis. Escalate with exact error, timestamps, scope, actions already attempted and their results.

## Prevention and closure

Preventive control: **Regression fixture and required security check**. Acceptance: the recurrence scenario fails safely or generates the expected alert, while the legitimate user path remains functional.

Draft closure message: “The affected path has been restored and verified. We identified the configuration condition that caused the issue, applied the approved correction, and recorded a preventive follow-up. We will monitor for recurrence during the agreed observation period.”

Related runbook: [cicd-failure](../runbooks/cicd-failure.md).
