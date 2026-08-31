# Project 03 — Security Operations & Incident Response

## Primary Incident
A simulated developer access key is exposed in a public-code scenario. Within minutes, a new source performs cloud discovery actions. The exercise tests alerting, triage, evidence preservation, containment, scope analysis, recovery, and preventive control design.

## Severity
**SEV-2 / High** — confirmed simulated credential compromise with limited lab-account activity. No customer data exists in this project and no real exfiltration is represented.

## Response Timeline
| Time UTC | Action |
|---|---|
| 14:02 | simulated key disclosure |
| 14:08 | new-source discovery calls |
| 14:10 | detection triggers |
| 14:14 | analyst validates ownership |
| 14:18 | credential disabled |
| 14:24 | scope / peer activity review |
| 14:33 | least-privilege remediation |
| 14:46 | approved access recovery validated |
| 15:15 | preventive actions approved |

## Detection Engineering
Three runnable detections are included:
- `credential-compromise.py` — new-source discovery burst after leaked-key scenario.
- `impossible_travel.py` — two countries for one user within 30 minutes in normalized sign-in data.
- `password_spray.py` — one source fails across multiple users and then succeeds.

The detections intentionally operate on local synthetic JSONL evidence so reviewers can run them without cloud credentials.

## Investigation Artifacts
- `timeline.csv` — normalized incident chronology.
- `IOC-REGISTER.md` — synthetic indicators/evidence and disposition.
- `evidence/` — audit and sign-in events.
- `playbooks/compromised-cloud-credential.md` — containment/recovery procedure.
- `post-incident-report.md` — executive/technical PIR.
- `LESSONS-LEARNED.md` — gaps and corrective actions.

## Interview Story
The strongest lesson is preventive: a fast response is valuable, but **short-lived credentials + least privilege + CI secret scanning + anomaly detection** reduce the probability and blast radius of the incident in the first place.
