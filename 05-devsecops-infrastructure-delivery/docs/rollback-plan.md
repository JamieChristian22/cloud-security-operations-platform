# Rollback / Recovery Strategy

1. Stop if the plan shows unexpected replacement or broad permission expansion.
2. Preserve the failed plan/log output as change evidence.
3. Revert the source change through Git rather than editing cloud state manually where possible.
4. Re-run format, validation, policy tests, and unit tests.
5. For stateful resources, prefer restore/recovery procedures over destructive recreation.
6. Validate user/service health after rollback.
7. Record whether rollback succeeded, what data/state was affected, and what guardrail should change.

This portfolio does not automatically deploy to production accounts and stores no cloud credentials.
