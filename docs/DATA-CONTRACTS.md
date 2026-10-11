# Data contracts and input quality

## Inventory v2

CloudGuardian requires all six arrays: `users`, `keys`, `policies`, `storage`, `firewall_rules`, `resources`. An empty array means the supplied scope contains no records for that section; it does not prove the cloud has none. A collector must describe uncollected domains in metadata.

| Array | Required fields | Rules |
|---|---|---|
| users | name, enabled, mfa, days_inactive | Booleans are real JSON booleans; days are nonnegative integers |
| keys | id, active, age_days | Active means usable in the represented snapshot |
| policies | name, actions | Nonempty action strings; these are normalized allowed actions, not raw IAM JSON |
| storage | name, public, encrypted | Collect effective values; do not default an unknown value to false |
| firewall_rules | name, source; port OR from_port/to_port | Valid IPv4/IPv6 CIDR; inclusive integer range; protocol tcp/udp/all |
| resources | id, tags | String tag keys/values; Owner and Environment assessed for nonempty content |

`provider` should identify the source platform. Duplicate identities within a section/provider fail validation. Optional `metadata` records collection time, covered accounts/regions and excluded sources. The AWS collector deliberately covers only security-group CIDR ingress and tags.

The normalized policy contract does not model explicit deny, condition keys, permissions boundaries, SCPs, resource policies or cross-account trust. Its wildcard finding is a review signal, not a complete effective-permissions decision.

## Events

JSONL records contain timestamp (ISO 8601 with timezone), user, source_ip, result (`success` or `failure`), and preferably event_id. Travel records need latitude and longitude; the engine does not invent coordinates. Reconnaissance records add action. Optional trusted_network is a boolean applied by trusted enrichment, not by an untrusted source event.

Invalid coordinates, IPs or timestamps fail the batch with exit code 2. A production stream should quarantine individual bad records with counters; this lab intentionally fails visibly instead of silently dropping them. Duplicate event IDs are collapsed. Conflicting reuse of an event ID must be prevented upstream.

## Exceptions

Each exception includes exact finding_id, accountable owner, reason, ticket, and timezone-aware expires_at. It applies to one current finding. Expired, duplicate and unknown finding IDs fail. Accepted risk remains in the report; it is excluded from the blocking gate and open-risk score. Protect the exception file with code review; a JSON file is not an approval system.

## Exit codes

CloudGuardian and policy CLIs use 0 for successful processing/passing gate, 1 for a breached gate or unmet explicit lab expectation, and 2 for invalid input or execution setup. Detection CLIs return 0 for valid processing even with no alerts; `--assert-alert` is used only to verify a known-positive fixture.

## Reports

JSON contains schema_version, findings, open_count, severity/control/provider/status summary, scope, and a bounded heuristic score. Stable IDs hash control/provider/resource. CSV escapes spreadsheet formula prefixes. HTML escapes all finding text. Neither report should contain credentials or unredacted production identity data when committed publicly.
