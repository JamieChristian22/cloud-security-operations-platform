# Runbook — Unreachable Cloud Service

1. Confirm scope: one user, one region, one target, or all users.
2. Resolve DNS (`nslookup`/`dig`) and verify expected endpoint.
3. Test TCP/TLS (`curl -vk`, `nc -vz` where permitted).
4. Check load balancer/target health.
5. Review security groups/NSGs/firewall rules and routes.
6. Test application locally on target.
7. Apply smallest safe fix, retest externally, record RCA.

**Do not** open broad management ports as a shortcut.
