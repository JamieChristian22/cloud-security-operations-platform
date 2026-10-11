# Runbook · Monitoring dimension mismatch

## Trigger and scope

A simulated CPU threshold breach produces no alert. Confirm the exact affected identity, resource and environment. Record the first observed failure and last known good state in UTC. Assign severity according to business impact, not the error string alone.

## Prerequisites

Read-only access to logs/configuration, approved support scope and a place to retain sanitized evidence. A remediation action requires the responsible owner's authorization. Verify the current cloud identity before using a CLI.

## Ordered diagnosis

1. Capture the exact error and correlation/request ID; reproduce once through the affected user path.
2. Check recent identity, network, application and policy changes in the relevant time range.
3. Consider missing metric; insufficient evaluation periods; action disabled.
4. Run the discriminating checks below and compare expected and observed state.
5. Document why the chosen cause explains the observations before modifying anything.

```text
Inspect metric namespace, resource dimensions, statistic, period, threshold and missing-data behavior.
Compare the alarm dimension with the current resource ID.
```

## Decision branch

If evidence matches **alarm points at the wrong resource dimension**, use the scoped correction below. If it does not, preserve the output, test the next hypothesis, and escalate with the evidence packet. Avoid simultaneous changes to identity, network and application configuration; they obscure causal verification.

## Approved correction

Correct the resource dimension through configuration review and use a controlled metric/test event to exercise the route.

## Verification and closure

Alarm transitions as expected, notification arrives at the approved test destination, and recovery notification is observed. Record timestamps, expected/actual result, owner confirmation and the observation window. Do not close merely because a command returned success.

## Rollback

Restore the previous definition if unrelated services are targeted; suppress the test-only alert according to the maintenance procedure.

## Prevention

Alert route test and resource-dimension validation. Keep the regression check and runbook version linked to the incident. Review the linked [tabletop exercise](../case-studies/06-monitoring-gap.md) for an illustrative decision sequence.
