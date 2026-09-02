# Runbook — IAM AccessDenied

1. Confirm caller identity/session.
2. Record the exact denied action and resource.
3. Check role/group assignment and effective scope.
4. Review explicit deny/SCP/policy boundaries where applicable.
5. Simulate/evaluate the required action.
6. Add only the minimum approved action/resource scope.
7. Retest and capture audit evidence.

Never resolve an authorization problem by granting blanket administrator access.
