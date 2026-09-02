# Runbook — DNS Resolution Failure

1. Compare expected hostname/IP against inventory.
2. Query configured resolver with `nslookup`/`dig`.
3. Check authoritative record, TTL, private-zone association, and search suffix.
4. Test direct IP only to isolate DNS from application health.
5. Correct the record/zone link, wait for appropriate cache behavior, retest.
