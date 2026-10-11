# Backup restore chooses expired snapshot

**Evidence class: synthetic tabletop exercise.** The commands below are a proposed investigation sequence. The observations are authored examples, not captured cloud execution output. Related ticket: [INC-020](../tickets/INC-020.md).

## Impact and initial scope

The documented restore procedure references a snapshot outside retention. Assign a case owner, confirm environment and start time, and determine whether other users/services are affected before changing configuration. Escalate immediately if there is evidence of active compromise or critical data loss.

## Competing hypotheses

Primary scenario cause: **Stale snapshot identifier in the runbook**. Alternatives: Missing permissions; corrupt backup; incompatible target. Do not accept the primary cause solely because it appears in this exercise. Gather evidence that distinguishes it from alternatives.

## Investigation commands or console checks

```text
List available recovery points and creation times using the provider backup console/API.
Select a disposable isolated restore destination and verify key access.
```

Shell variables represent account-specific values confirmed by the operator. They are not credentials supplied by this repository. Use read-only collection first and store sensitive output outside Git.

## Illustrative evidence and reasoning

Illustrative backup job succeeded, but the runbook references an expired identifier. A newer approved recovery point exists.

This supports the stated root cause within the tabletop scenario. In a live incident, attach timestamped output, correlation IDs and source context; record contradictory evidence instead of discarding it.

## Minimum approved correction

Update selection logic to identify eligible recovery points by service, age and integrity rather than a permanent hard-coded ID. Restore to an isolated target.

Record change owner, approval, affected resources, expected completion time and stop conditions. Separate emergency containment from permanent correction.

## Positive and negative verification

Recovered file hash matches the known fixture; application opens it; measured restore time and recovery point are recorded.

Record expected and observed results separately. Observe a representative monitoring interval and obtain service-owner confirmation before closure.

## Rollback and escalation

Delete only the approved disposable restore target after evidence review; preserve original backups and application data.

If the discriminating test disproves the primary cause, preserve the evidence and test the next hypothesis. Escalate with exact error, timestamps, scope, actions already attempted and their results.

## Prevention and closure

Preventive control: **Quarterly restore drill and recovery-point freshness check**. Acceptance: the recurrence scenario fails safely or generates the expected alert, while the legitimate user path remains functional.

Draft closure message: “The affected path has been restored and verified. We identified the configuration condition that caused the issue, applied the approved correction, and recorded a preventive follow-up. We will monitor for recurrence during the agreed observation period.”

Related runbook: [backup-restore-validation](../runbooks/backup-restore-validation.md).
