# Lessons Learned

## What Worked
- New-source discovery behavior was detectable from normalized audit events.
- Key ownership could be identified quickly.
- Containment prioritized credential deactivation before broader changes.
- The investigation retained denied/successful activity as useful evidence.

## Gaps Found
- Long-lived access keys created avoidable exposure.
- Secret scanning should happen before merge/publish.
- Privileged discovery permissions were broader than required for the developer workflow.

## Corrective Actions
1. Prefer federated/short-lived credentials for human access.
2. Add secret-scanning and policy checks in CI.
3. Review developer role permissions quarterly.
4. Alert on new-source discovery bursts and password-spray patterns.
5. Perform credential-compromise tabletop exercises twice per year in the simulated operating model.
