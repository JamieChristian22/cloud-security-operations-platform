# Runbook · Linux application disk pressure

## Trigger and scope

API writes fail as the application filesystem reaches its threshold. Confirm the exact affected identity, resource and environment. Record the first observed failure and last known good state in UTC. Assign severity according to business impact, not the error string alone.

## Prerequisites

Read-only access to logs/configuration, approved support scope and a place to retain sanitized evidence. A remediation action requires the responsible owner's authorization. Verify the current cloud identity before using a CLI.

## Ordered diagnosis

1. Capture the exact error and correlation/request ID; reproduce once through the affected user path.
2. Check recent identity, network, application and policy changes in the relevant time range.
3. Consider inode exhaustion; deleted open file; growing database.
4. Run the discriminating checks below and compare expected and observed state.
5. Document why the chosen cause explains the observations before modifying anything.

```text
df -h
df -i
sudo du -xhd1 /var/log
sudo lsof +L1
```

## Decision branch

If evidence matches **unbounded application logs**, use the scoped correction below. If it does not, preserve the output, test the next hypothesis, and escalate with the evidence packet. Avoid simultaneous changes to identity, network and application configuration; they obscure causal verification.

## Approved correction

Preserve diagnostic log samples. Apply the approved logrotate configuration and service-supported reopen action. Avoid deleting database or active files blindly.

## Verification and closure

Disk utilization falls below the local alert threshold; app writes succeed; rotation runs successfully; logs continue to arrive. Record timestamps, expected/actual result, owner confirmation and the observation window. Do not close merely because a command returned success.

## Rollback

Restore the prior rotation configuration if the application stops logging, and escalate storage recovery if growth continues.

## Prevention

Log retention, rotation check and threshold/window alert. Keep the regression check and runbook version linked to the incident. Review the linked [tabletop exercise](../case-studies/04-linux-disk.md) for an illustrative decision sequence.
