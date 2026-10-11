# Runbook · IAM AccessDenied after role change

## Trigger and scope

A developer can authenticate but cannot read the approved artifact prefix. Confirm the exact affected identity, resource and environment. Record the first observed failure and last known good state in UTC. Assign severity according to business impact, not the error string alone.

## Prerequisites

Read-only access to logs/configuration, approved support scope and a place to retain sanitized evidence. A remediation action requires the responsible owner's authorization. Verify the current cloud identity before using a CLI.

## Ordered diagnosis

1. Capture the exact error and correlation/request ID; reproduce once through the affected user path.
2. Check recent identity, network, application and policy changes in the relevant time range.
3. Consider expired session; explicit deny; missing object permission.
4. Run the discriminating checks below and compare expected and observed state.
5. Document why the chosen cause explains the observations before modifying anything.

```text
aws sts get-caller-identity
aws iam simulate-principal-policy --policy-source-arn "$ROLE_ARN" --action-names s3:GetObject --resource-arns "$OBJECT_ARN"
```

## Decision branch

If evidence matches **wrong role mapping**, use the scoped correction below. If it does not, preserve the output, test the next hypothesis, and escalate with the evidence packet. Avoid simultaneous changes to identity, network and application configuration; they obscure causal verification.

## Approved correction

Correct the approved group-to-role mapping, obtain a fresh federated session, and grant only the documented object prefix if the mapped role still lacks it.

## Verification and closure

Approved GetObject succeeds; unrelated prefix and PutObject remain denied. Confirm the caller ARN changed to the approved role. Record timestamps, expected/actual result, owner confirmation and the observation window. Do not close merely because a command returned success.

## Rollback

Revert the mapping if unintended users gain access; revoke the new session and restore the previously approved assignment.

## Prevention

Role-mapping assertion and positive/negative IAM acceptance tests. Keep the regression check and runbook version linked to the incident. Review the linked [tabletop exercise](../case-studies/01-iam-access-denied.md) for an illustrative decision sequence.
