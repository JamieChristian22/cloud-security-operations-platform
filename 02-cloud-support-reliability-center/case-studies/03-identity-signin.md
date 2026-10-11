# M365 sign-in blocked by location policy

**Evidence class: synthetic tabletop exercise.** The commands below are a proposed investigation sequence. The observations are authored examples, not captured cloud execution output. Related ticket: [INC-003](../tickets/INC-003.md).

## Impact and initial scope

A known user cannot sign in from an approved remote location. Assign a case owner, confirm environment and start time, and determine whether other users/services are affected before changing configuration. Escalate immediately if there is evidence of active compromise or critical data loss.

## Competing hypotheses

Primary scenario cause: **Conditional Access location classification**. Alternatives: Wrong password; disabled account; device compliance failure. Do not accept the primary cause solely because it appears in this exercise. Gather evidence that distinguishes it from alternatives.

## Investigation commands or console checks

```text
Review Entra sign-in logs: correlation ID, conditional-access result, device, risk and client IP.
Compare named-location membership with the approved network record.
```

Shell variables represent account-specific values confirmed by the operator. They are not credentials supplied by this repository. Use read-only collection first and store sensitive output outside Git.

## Illustrative evidence and reasoning

Illustrative sign-in result: credential accepted, named-location condition failed, device compliant.

This supports the stated root cause within the tabletop scenario. In a live incident, attach timestamped output, correlation IDs and source context; record contradictory evidence instead of discarding it.

## Minimum approved correction

Validate the user and source using approved identity checks. Correct the named-location record or obtain a narrowly scoped, expiring exception. Preserve MFA.

Record change owner, approval, affected resources, expected completion time and stop conditions. Separate emergency containment from permanent correction.

## Positive and negative verification

Approved user/device succeeds with required MFA; unapproved source remains blocked; exception has an owner and expiry.

Record expected and observed results separately. Observe a representative monitoring interval and obtain service-owner confirmation before closure.

## Rollback and escalation

Revert the location change and revoke the exception if unexpected identities become eligible.

If the discriminating test disproves the primary cause, preserve the evidence and test the next hypothesis. Escalate with exact error, timestamps, scope, actions already attempted and their results.

## Prevention and closure

Preventive control: **Named-location review and break-glass exception audit**. Acceptance: the recurrence scenario fails safely or generates the expected alert, while the legitimate user path remains functional.

Draft closure message: “The affected path has been restored and verified. We identified the configuration condition that caused the issue, applied the approved correction, and recorded a preventive follow-up. We will monitor for recurrence during the agreed observation period.”

Related runbook: [m365-signin](../runbooks/m365-signin.md).
