# IAM AccessDenied after role change

**Evidence class: synthetic tabletop exercise.** The commands below are a proposed investigation sequence. The observations are authored examples, not captured cloud execution output. Related ticket: [INC-001](../tickets/INC-001.md).

## Impact and initial scope

A developer can authenticate but cannot read the approved artifact prefix. Assign a case owner, confirm environment and start time, and determine whether other users/services are affected before changing configuration. Escalate immediately if there is evidence of active compromise or critical data loss.

## Competing hypotheses

Primary scenario cause: **Wrong role mapping**. Alternatives: Expired session; explicit deny; missing object permission. Do not accept the primary cause solely because it appears in this exercise. Gather evidence that distinguishes it from alternatives.

## Investigation commands or console checks

```text
aws sts get-caller-identity
aws iam simulate-principal-policy --policy-source-arn "$ROLE_ARN" --action-names s3:GetObject --resource-arns "$OBJECT_ARN"
```

Shell variables represent account-specific values confirmed by the operator. They are not credentials supplied by this repository. Use read-only collection first and store sensitive output outside Git.

## Illustrative evidence and reasoning

The caller is the old reporting role. Simulation returns implicitDeny for the approved object. No new explicit-deny evidence is present.

This supports the stated root cause within the tabletop scenario. In a live incident, attach timestamped output, correlation IDs and source context; record contradictory evidence instead of discarding it.

## Minimum approved correction

Correct the approved group-to-role mapping, obtain a fresh federated session, and grant only the documented object prefix if the mapped role still lacks it.

Record change owner, approval, affected resources, expected completion time and stop conditions. Separate emergency containment from permanent correction.

## Positive and negative verification

Approved GetObject succeeds; unrelated prefix and PutObject remain denied. Confirm the caller ARN changed to the approved role.

Record expected and observed results separately. Observe a representative monitoring interval and obtain service-owner confirmation before closure.

## Rollback and escalation

Revert the mapping if unintended users gain access; revoke the new session and restore the previously approved assignment.

If the discriminating test disproves the primary cause, preserve the evidence and test the next hypothesis. Escalate with exact error, timestamps, scope, actions already attempted and their results.

## Prevention and closure

Preventive control: **Role-mapping assertion and positive/negative IAM acceptance tests**. Acceptance: the recurrence scenario fails safely or generates the expected alert, while the legitimate user path remains functional.

Draft closure message: “The affected path has been restored and verified. We identified the configuration condition that caused the issue, applied the approved correction, and recorded a preventive follow-up. We will monitor for recurrence during the agreed observation period.”

Related runbook: [iam-access-denied](../runbooks/iam-access-denied.md).
