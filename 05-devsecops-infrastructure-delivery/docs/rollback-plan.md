# Rollback and recovery procedure

1. Define the trigger before change: user-path regression, unexpected permissions, missing telemetry or breached error threshold.
2. Stop further rollout and preserve the failed plan, sanitized errors and relevant logs.
3. Identify the previous known-good code/configuration and inspect a new plan. A Git revert does not automatically restore data or infrastructure safely.
4. Review state drift, resource replacements and key/retention dependencies. Do not restore an old state file over a changed environment without reconciliation.
5. Apply the approved corrective plan or execute the service-specific recovery procedure through the authorized owner.
6. Recheck positive functionality, negative security access and telemetry delivery. Keep the incident open until those pass.
7. Preserve audit stores, backups and keys throughout recovery. Destruction protections are intentional stop conditions.

For data loss, restore into an isolated target first, verify hashes and service behavior, then approve cutover. Record measured RTO/RPO; the repository's design targets are not measured recovery results.
