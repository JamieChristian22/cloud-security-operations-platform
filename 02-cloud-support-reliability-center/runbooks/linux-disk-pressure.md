# Runbook — Linux Disk Pressure

1. `df -h` and `df -i`.
2. Identify top consumers with `du`.
3. Check logs, temp files, deleted-open files, and package/cache growth.
4. Protect service stability before cleanup.
5. Rotate/archive approved data; do not delete unknown files blindly.
6. Validate free space and application health.
7. Add threshold alert and retention/rotation control.
