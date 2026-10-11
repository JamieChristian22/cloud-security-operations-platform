# Indicator and evidence register

All IPs and identities are synthetic. Documentation addresses do not identify real attackers.

| Indicator | Context | Evidence | Interpretation |
|---|---|---|---|
| 203.0.113.77 | API discovery source | API-002 through API-006 | Investigate principal and approved automation; not a malicious-IP verdict |
| dev-jlee | API exercise identity | events.jsonl | Verify owner and credential/session provenance |
| 203.0.113.90 | Sign-in failure/success source | SIGNIN-003 through SIGNIN-006 | Password-spray fixture, separate date from API case |
| alex@northstar.example | Geographic anomaly identity | SIGNIN-001 and SIGNIN-002 | Investigate device/session/VPN context |

Disposition in this repository: retained as synthetic evidence. No real blocking, account suspension, notification or credential revocation was performed.
