# Post-Incident Report — IR-2026-004
**Summary:** A simulated long-lived developer cloud key was exposed and used from an unfamiliar source for reconnaissance. The key was disabled within 10 minutes of the first suspicious event.

**Impact:** Lab-account metadata was enumerated. Sample evidence shows no successful IAM modification, object write/delete, or data download by the suspicious source.

**Root cause:** Secret-handling failure plus missing automated secret detection.

**What worked:** Audit events were available; least privilege denied role enumeration; the detection combined new-source and discovery behavior; containment was direct and documented.

**What failed:** Long-lived credentials were permitted and code review alone did not catch the secret.

**Corrective actions:** CI secret scan; short-lived credential preference; 90-day maximum lab key age; quarterly access review; detection test added to repository; incident playbook updated.

**Owner / due dates:** Security Engineering owns CI secret scanning before next release; IAM owner reviews long-lived credentials within 7 days; Cloud Ops validates alert routing within 3 days.
