# Linux application disk pressure

**Evidence class: synthetic tabletop exercise.** The commands below are a proposed investigation sequence. The observations are authored examples, not captured cloud execution output. Related ticket: [INC-004](../tickets/INC-004.md).

## Impact and initial scope

API writes fail as the application filesystem reaches its threshold. Assign a case owner, confirm environment and start time, and determine whether other users/services are affected before changing configuration. Escalate immediately if there is evidence of active compromise or critical data loss.

## Competing hypotheses

Primary scenario cause: **Unbounded application logs**. Alternatives: Inode exhaustion; deleted open file; growing database. Do not accept the primary cause solely because it appears in this exercise. Gather evidence that distinguishes it from alternatives.

## Investigation commands or console checks

```text
df -h
df -i
sudo du -xhd1 /var/log
sudo lsof +L1
```

Shell variables represent account-specific values confirmed by the operator. They are not credentials supplied by this repository. Use read-only collection first and store sensitive output outside Git.

## Illustrative evidence and reasoning

Illustrative outputs: /var at 98%, inodes 12%, application log directory 36 GB, no dominant deleted-open file.

This supports the stated root cause within the tabletop scenario. In a live incident, attach timestamped output, correlation IDs and source context; record contradictory evidence instead of discarding it.

## Minimum approved correction

Preserve diagnostic log samples. Apply the approved logrotate configuration and service-supported reopen action. Avoid deleting database or active files blindly.

Record change owner, approval, affected resources, expected completion time and stop conditions. Separate emergency containment from permanent correction.

## Positive and negative verification

Disk utilization falls below the local alert threshold; app writes succeed; rotation runs successfully; logs continue to arrive.

Record expected and observed results separately. Observe a representative monitoring interval and obtain service-owner confirmation before closure.

## Rollback and escalation

Restore the prior rotation configuration if the application stops logging, and escalate storage recovery if growth continues.

If the discriminating test disproves the primary cause, preserve the evidence and test the next hypothesis. Escalate with exact error, timestamps, scope, actions already attempted and their results.

## Prevention and closure

Preventive control: **Log retention, rotation check and threshold/window alert**. Acceptance: the recurrence scenario fails safely or generates the expected alert, while the legitimate user path remains functional.

Draft closure message: “The affected path has been restored and verified. We identified the configuration condition that caused the issue, applied the approved correction, and recorded a preventive follow-up. We will monitor for recurrence during the agreed observation period.”

Related runbook: [linux-disk-pressure](../runbooks/linux-disk-pressure.md).
