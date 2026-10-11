# Runbook · Private web service unreachable

## Trigger and scope

A load balancer reports unhealthy targets while the application is healthy locally. Confirm the exact affected identity, resource and environment. Record the first observed failure and last known good state in UTC. Assign severity according to business impact, not the error string alone.

## Prerequisites

Read-only access to logs/configuration, approved support scope and a place to retain sanitized evidence. A remediation action requires the responsible owner's authorization. Verify the current cloud identity before using a CLI.

## Ordered diagnosis

1. Capture the exact error and correlation/request ID; reproduce once through the affected user path.
2. Check recent identity, network, application and policy changes in the relevant time range.
3. Consider application failure; listener error; route/acl issue.
4. Run the discriminating checks below and compare expected and observed state.
5. Document why the chosen cause explains the observations before modifying anything.

```text
curl -I https://service.lab.example
aws elbv2 describe-target-health --target-group-arn "$TARGET_GROUP_ARN"
aws ec2 describe-security-groups --group-ids "$WORKLOAD_SG"
```

## Decision branch

If evidence matches **security-group path omits approved https**, use the scoped correction below. If it does not, preserve the output, test the next hypothesis, and escalate with the evidence packet. Avoid simultaneous changes to identity, network and application configuration; they obscure causal verification.

## Approved correction

Add HTTPS ingress from the verified load-balancer security group through Terraform review. Do not expose management ports or change unrelated routes.

## Verification and closure

Target becomes healthy; approved HTTPS succeeds; an outside source cannot reach private management ports. Record timestamps, expected/actual result, owner confirmation and the observation window. Do not close merely because a command returned success.

## Rollback

Revert only the new ingress if scope is broader than intended or health remains unstable; investigate next hypothesis.

## Prevention

Ingress review and health-check smoke test. Keep the regression check and runbook version linked to the incident. Review the linked [tabletop exercise](../case-studies/02-private-service-unreachable.md) for an illustrative decision sequence.
