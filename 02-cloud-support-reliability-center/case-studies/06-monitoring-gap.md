# Monitoring dimension mismatch

**Evidence class: synthetic tabletop exercise.** The commands below are a proposed investigation sequence. The observations are authored examples, not captured cloud execution output. Related ticket: [INC-007](../tickets/INC-007.md).

## Impact and initial scope

A simulated CPU threshold breach produces no alert. Assign a case owner, confirm environment and start time, and determine whether other users/services are affected before changing configuration. Escalate immediately if there is evidence of active compromise or critical data loss.

## Competing hypotheses

Primary scenario cause: **Alarm points at the wrong resource dimension**. Alternatives: Missing metric; insufficient evaluation periods; action disabled. Do not accept the primary cause solely because it appears in this exercise. Gather evidence that distinguishes it from alternatives.

## Investigation commands or console checks

```text
Inspect metric namespace, resource dimensions, statistic, period, threshold and missing-data behavior.
Compare the alarm dimension with the current resource ID.
```

Shell variables represent account-specific values confirmed by the operator. They are not credentials supplied by this repository. Use read-only collection first and store sensitive output outside Git.

## Illustrative evidence and reasoning

Illustrative metric is present for vm-app-02; alarm selects vm-app-01; notification destination is enabled.

This supports the stated root cause within the tabletop scenario. In a live incident, attach timestamped output, correlation IDs and source context; record contradictory evidence instead of discarding it.

## Minimum approved correction

Correct the resource dimension through configuration review and use a controlled metric/test event to exercise the route.

Record change owner, approval, affected resources, expected completion time and stop conditions. Separate emergency containment from permanent correction.

## Positive and negative verification

Alarm transitions as expected, notification arrives at the approved test destination, and recovery notification is observed.

Record expected and observed results separately. Observe a representative monitoring interval and obtain service-owner confirmation before closure.

## Rollback and escalation

Restore the previous definition if unrelated services are targeted; suppress the test-only alert according to the maintenance procedure.

If the discriminating test disproves the primary cause, preserve the evidence and test the next hypothesis. Escalate with exact error, timestamps, scope, actions already attempted and their results.

## Prevention and closure

Preventive control: **Alert route test and resource-dimension validation**. Acceptance: the recurrence scenario fails safely or generates the expected alert, while the legitimate user path remains functional.

Draft closure message: “The affected path has been restored and verified. We identified the configuration condition that caused the issue, applied the approved correction, and recorded a preventive follow-up. We will monitor for recurrence during the agreed observation period.”

Related runbook: [cloud-monitoring-alert](../runbooks/cloud-monitoring-alert.md).
