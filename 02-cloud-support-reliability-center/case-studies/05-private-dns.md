# Private endpoint resolves to public address

**Evidence class: synthetic tabletop exercise.** The commands below are a proposed investigation sequence. The observations are authored examples, not captured cloud execution output. Related ticket: [INC-021](../tickets/INC-021.md).

## Impact and initial scope

A private endpoint consumer fails despite correct endpoint and application health. Assign a case owner, confirm environment and start time, and determine whether other users/services are affected before changing configuration. Escalate immediately if there is evidence of active compromise or critical data loss.

## Competing hypotheses

Primary scenario cause: **Private DNS zone link missing**. Alternatives: Client cache; wrong resolver; missing record. Do not accept the primary cause solely because it appears in this exercise. Gather evidence that distinguishes it from alternatives.

## Investigation commands or console checks

```text
nslookup service.lab.example
nslookup service.lab.example "$APPROVED_DNS_SERVER"
Review private zone VNet links and endpoint DNS configuration.
```

Shell variables represent account-specific values confirmed by the operator. They are not credentials supplied by this repository. Use read-only collection first and store sensitive output outside Git.

## Illustrative evidence and reasoning

Illustrative result: corporate resolver returns the public answer; expected private record exists in a zone not linked to the client VNet.

This supports the stated root cause within the tabletop scenario. In a live incident, attach timestamped output, correlation IDs and source context; record contradictory evidence instead of discarding it.

## Minimum approved correction

Link the approved VNet to the existing private DNS zone through reviewed configuration. Change only the required resolver path.

Record change owner, approval, affected resources, expected completion time and stop conditions. Separate emergency containment from permanent correction.

## Positive and negative verification

Approved resolver returns the expected private address; TLS hostname validation succeeds; unrelated zones still resolve.

Record expected and observed results separately. Observe a representative monitoring interval and obtain service-owner confirmation before closure.

## Rollback and escalation

Remove only the new zone link if it creates a naming conflict; restore the approved resolver association.

If the discriminating test disproves the primary cause, preserve the evidence and test the next hypothesis. Escalate with exact error, timestamps, scope, actions already attempted and their results.

## Prevention and closure

Preventive control: **DNS resolution acceptance test after endpoint changes**. Acceptance: the recurrence scenario fails safely or generates the expected alert, while the legitimate user path remains functional.

Draft closure message: “The affected path has been restored and verified. We identified the configuration condition that caused the issue, applied the approved correction, and recorded a preventive follow-up. We will monitor for recurrence during the agreed observation period.”

Related runbook: [dns-resolution-failure](../runbooks/dns-resolution-failure.md).
