# Runbook · M365 sign-in blocked by location policy

## Trigger and scope

A known user cannot sign in from an approved remote location. Confirm the exact affected identity, resource and environment. Record the first observed failure and last known good state in UTC. Assign severity according to business impact, not the error string alone.

## Prerequisites

Read-only access to logs/configuration, approved support scope and a place to retain sanitized evidence. A remediation action requires the responsible owner's authorization. Verify the current cloud identity before using a CLI.

## Ordered diagnosis

1. Capture the exact error and correlation/request ID; reproduce once through the affected user path.
2. Check recent identity, network, application and policy changes in the relevant time range.
3. Consider wrong password; disabled account; device compliance failure.
4. Run the discriminating checks below and compare expected and observed state.
5. Document why the chosen cause explains the observations before modifying anything.

```text
Review Entra sign-in logs: correlation ID, conditional-access result, device, risk and client IP.
Compare named-location membership with the approved network record.
```

## Decision branch

If evidence matches **conditional access location classification**, use the scoped correction below. If it does not, preserve the output, test the next hypothesis, and escalate with the evidence packet. Avoid simultaneous changes to identity, network and application configuration; they obscure causal verification.

## Approved correction

Validate the user and source using approved identity checks. Correct the named-location record or obtain a narrowly scoped, expiring exception. Preserve MFA.

## Verification and closure

Approved user/device succeeds with required MFA; unapproved source remains blocked; exception has an owner and expiry. Record timestamps, expected/actual result, owner confirmation and the observation window. Do not close merely because a command returned success.

## Rollback

Revert the location change and revoke the exception if unexpected identities become eligible.

## Prevention

Named-location review and break-glass exception audit. Keep the regression check and runbook version linked to the incident. Review the linked [tabletop exercise](../case-studies/03-identity-signin.md) for an illustrative decision sequence.
