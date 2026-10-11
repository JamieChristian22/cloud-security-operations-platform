# Runbook · Private endpoint resolves to public address

## Trigger and scope

A private endpoint consumer fails despite correct endpoint and application health. Confirm the exact affected identity, resource and environment. Record the first observed failure and last known good state in UTC. Assign severity according to business impact, not the error string alone.

## Prerequisites

Read-only access to logs/configuration, approved support scope and a place to retain sanitized evidence. A remediation action requires the responsible owner's authorization. Verify the current cloud identity before using a CLI.

## Ordered diagnosis

1. Capture the exact error and correlation/request ID; reproduce once through the affected user path.
2. Check recent identity, network, application and policy changes in the relevant time range.
3. Consider client cache; wrong resolver; missing record.
4. Run the discriminating checks below and compare expected and observed state.
5. Document why the chosen cause explains the observations before modifying anything.

```text
nslookup service.lab.example
nslookup service.lab.example "$APPROVED_DNS_SERVER"
Review private zone VNet links and endpoint DNS configuration.
```

## Decision branch

If evidence matches **private dns zone link missing**, use the scoped correction below. If it does not, preserve the output, test the next hypothesis, and escalate with the evidence packet. Avoid simultaneous changes to identity, network and application configuration; they obscure causal verification.

## Approved correction

Link the approved VNet to the existing private DNS zone through reviewed configuration. Change only the required resolver path.

## Verification and closure

Approved resolver returns the expected private address; TLS hostname validation succeeds; unrelated zones still resolve. Record timestamps, expected/actual result, owner confirmation and the observation window. Do not close merely because a command returned success.

## Rollback

Remove only the new zone link if it creates a naming conflict; restore the approved resolver association.

## Prevention

DNS resolution acceptance test after endpoint changes. Keep the regression check and runbook version linked to the incident. Review the linked [tabletop exercise](../case-studies/05-private-dns.md) for an illustrative decision sequence.
