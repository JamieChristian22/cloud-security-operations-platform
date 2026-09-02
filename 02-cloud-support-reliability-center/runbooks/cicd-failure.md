# Runbook — CI/CD Pipeline Failure

1. Identify the first failing stage, not the last reported symptom.
2. Reproduce locally when safe.
3. Distinguish syntax/dependency failure from security-policy failure.
4. Do not bypass a security gate to force a release.
5. Fix source/configuration, rerun tests, and document the change.
