# Runbook · Backup restore chooses expired snapshot

## Trigger and scope

The documented restore procedure references a snapshot outside retention. Confirm the exact affected identity, resource and environment. Record the first observed failure and last known good state in UTC. Assign severity according to business impact, not the error string alone.

## Prerequisites

Read-only access to logs/configuration, approved support scope and a place to retain sanitized evidence. A remediation action requires the responsible owner's authorization. Verify the current cloud identity before using a CLI.

## Ordered diagnosis

1. Capture the exact error and correlation/request ID; reproduce once through the affected user path.
2. Check recent identity, network, application and policy changes in the relevant time range.
3. Consider missing permissions; corrupt backup; incompatible target.
4. Run the discriminating checks below and compare expected and observed state.
5. Document why the chosen cause explains the observations before modifying anything.

```text
List available recovery points and creation times using the provider backup console/API.
Select a disposable isolated restore destination and verify key access.
```

## Decision branch

If evidence matches **stale snapshot identifier in the runbook**, use the scoped correction below. If it does not, preserve the output, test the next hypothesis, and escalate with the evidence packet. Avoid simultaneous changes to identity, network and application configuration; they obscure causal verification.

## Approved correction

Update selection logic to identify eligible recovery points by service, age and integrity rather than a permanent hard-coded ID. Restore to an isolated target.

## Verification and closure

Recovered file hash matches the known fixture; application opens it; measured restore time and recovery point are recorded. Record timestamps, expected/actual result, owner confirmation and the observation window. Do not close merely because a command returned success.

## Rollback

Delete only the approved disposable restore target after evidence review; preserve original backups and application data.

## Prevention

Quarterly restore drill and recovery-point freshness check. Keep the regression check and runbook version linked to the incident. Review the linked [tabletop exercise](../case-studies/07-backup-restore.md) for an illustrative decision sequence.
