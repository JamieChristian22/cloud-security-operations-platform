# Detection engineering specification

## DET-001 · Geographic travel anomaly

For each user, compare consecutive successful sign-ins with coordinates after UTC sorting and duplicate removal. Alert when distance is at least 500 km and implied speed exceeds 900 km/h. Simultaneous distant sign-ins also alert with no numeric speed. Records without coordinates are not evaluated for travel.

Approved trusted-network enrichment suppresses pairs involving that network. Enrichment is part of the trusted processing boundary. VPN egress, mobile networks, inaccurate geolocation, shared accounts and noninteractive token activity are common explanations. A high alert is a triage priority, not a verdict of compromise.

Evidence: both event IDs, distance, elapsed minutes, user and implied speed. Analyst checks device, application, MFA, session/token activity, user confirmation and other identity signals before containment.

## DET-002 · Password spray

For each source IP, count distinct failed users inside a rolling ten-minute window. Three users meet the demonstration threshold. Correlate a successful sign-in only if it belongs to an attacked user, follows the threshold event, and occurs within ten minutes. Repeated alerts for the same source are suppressed for one window.

A source with failures against one identity is not this rule's spray pattern. Distributed spraying across many IPs is outside the rule's scope. Test thresholds with approved replay data; production thresholds depend on authentication volumes, proxy topology and expected failures.

Evidence: failure event IDs, attacked users, source, window and any subsequent success IDs. Investigate source ownership and authentication result codes; contain the affected identity/session when justified, then review peer accounts.

## DET-003 · Cloud discovery burst

Three distinct discovery APIs from one user/source in ten minutes produce a medium signal. The API set is GetCallerIdentity, ListBuckets, ListRoles and DescribeInstances. Successful and denied attempts both reveal activity. Approved inventory tools can generate this pattern, so verify the principal, schedule and source before escalation.

This rule demonstrates discovery correlation. It cannot establish credential theft by itself. Pair with key age, anomalous source, privilege change, data access and user confirmation.

## Testing and tuning

`tests/test_detections.py` covers chronology, benign travel, failures, trusted networks, missing geography, simultaneous events, duplicate input, one-user brute force, out-of-window events, earlier/unrelated successes, invalid records and per-user/source isolation.

Before live activation: validate schema mappings, evaluate an approved historical window, label true/false positives, choose thresholds, identify escalation owner, run in monitoring mode, and document acceptance. Measure alerts/day, confirmed incidents, analyst time, late events and enrichment failures. Do not publish synthetic precision/recall as a production metric.

## SIEM examples

The queries under `03-security-operations-incident-response/siem/` are integration starting points. Their data-source assumptions are documented in the files. They have not been executed against a live Sentinel or Splunk environment. The Python engine is the reference implementation for the offline fixtures.
