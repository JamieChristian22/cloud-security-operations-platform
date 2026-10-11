# SIEM integration examples

These queries have not been executed against a live SIEM. The KQL example assumes Sentinel SigninLogs and string ResultType. The SPL example assumes an approved normalized_signin sourcetype with user, source_ip and result fields. The SPL query detects spray only; it does not perform subsequent-success correlation.

Both examples use fixed bins. The Python reference uses a rolling window, so alerts near a bin boundary may differ. Validate permissions, field types, ingestion latency, UTC handling, source filtering, false positives and replay results before enabling alerts. No connector credentials or production telemetry are supplied.
