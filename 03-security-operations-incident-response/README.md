# 🛡️ Project 03 — Security Operations & Incident Response

![Security Operations](https://img.shields.io/badge/Security-Operations-critical)
![Incident Response](https://img.shields.io/badge/Incident-Response-red)
![Detection Engineering](https://img.shields.io/badge/Detection-Engineering-blue)
![Python](https://img.shields.io/badge/Python-Detections-3776AB?logo=python\&logoColor=white)
![IAM](https://img.shields.io/badge/IAM-Credential_Security-success)
![Severity](https://img.shields.io/badge/Incident-SEV--2-orange)
![Detections](https://img.shields.io/badge/Detections-3-brightgreen)
![MITRE ATT\&CK](https://img.shields.io/badge/MITRE-ATT%26CK-E34F26)
![Status](https://img.shields.io/badge/Project-Complete-brightgreen)
![Portfolio](https://img.shields.io/badge/Portfolio-Job_Ready-success)

> **Production-inspired Security Operations and Incident Response project demonstrating detection engineering, investigation, evidence preservation, containment, scope analysis, credential remediation, recovery, post-incident review, and preventive security engineering.**

---

## 🎯 Overview

This project simulates a **cloud security incident involving compromised developer credentials**.

A developer access key is exposed through a simulated public-code scenario. Shortly afterward, activity from a previously unseen source begins performing cloud discovery actions.

The Security Operations workflow must determine:

* 🚨 Is the alert legitimate?
* 🔑 Were credentials compromised?
* 👤 Who owns the affected identity?
* 🔍 What activity occurred?
* ☁️ Which resources were accessed?
* 💥 What is the potential blast radius?
* 🛑 How should the threat be contained?
* ♻️ How can legitimate access be restored safely?
* 🛡️ What controls would prevent recurrence?

The exercise follows the complete incident lifecycle:

**Detect → Triage → Investigate → Preserve → Scope → Contain → Eradicate → Recover → Validate → Learn → Prevent**

> ⚠️ **Environment Notice:** All identities, credentials, IP addresses, events, indicators, systems, timelines, and evidence in this project are synthetic and created exclusively for portfolio/lab purposes. No real credential compromise, customer data exposure, or production breach is represented.

---

# 🏢 Business Scenario

Northstar Digital Services operates cloud infrastructure supporting development and operational workloads.

During routine security monitoring, the SOC receives an alert indicating unusual discovery activity associated with a developer credential.

The credential appears to have been exposed through a simulated public-code scenario.

Within minutes, a previously unseen source begins performing discovery actions.

The incident requires coordination across:

* 🛡️ Security Operations
* 🔑 Identity & Access Management
* ☁️ Cloud Operations
* 💻 Development
* 📋 Governance

The response team must contain the incident quickly while preserving enough evidence to understand what happened.

---

# 🚨 Primary Incident

![Incident](https://img.shields.io/badge/Scenario-Credential_Compromise-red)
![Severity](https://img.shields.io/badge/Severity-SEV--2-orange)
![Status](https://img.shields.io/badge/Response-Contained-success)

### Scenario

A simulated developer access key becomes exposed through a public-code scenario.

Within minutes:

`Credential Exposure`

⬇️

`New Source Activity`

⬇️

`Cloud Discovery`

⬇️

`Detection Trigger`

⬇️

`SOC Investigation`

⬇️

`Credential Containment`

⬇️

`Scope Analysis`

⬇️

`Least-Privilege Remediation`

⬇️

`Approved Access Recovery`

⬇️

`Preventive Controls`

---

# 🚦 Incident Severity

## 🟠 SEV-2 / High

The scenario represents a **confirmed simulated credential compromise with limited lab-account activity**.

### Severity Factors

* 🔑 Valid credential involved
* 🌍 Previously unseen source
* 🔎 Cloud discovery activity
* ⚠️ Potential privilege misuse
* ☁️ Cloud-resource exposure potential

### Scope Limitations

* No real customer environment
* No customer data
* No real exfiltration
* No production systems
* No real compromised credentials

This classification allows the project to demonstrate a realistic high-severity response without misrepresenting the lab environment.

---

# 🎯 Project Objectives

This project demonstrates:

1. 🚨 **Security alert triage**
2. 🔎 **Detection engineering**
3. 🧠 **Hypothesis-driven investigation**
4. 📊 **Log and event analysis**
5. 🧾 **Evidence preservation**
6. 🔍 **IOC analysis**
7. ☁️ **Cloud activity investigation**
8. 🔑 **Credential compromise response**
9. 💥 **Blast-radius analysis**
10. 🛑 **Threat containment**
11. 🧹 **Eradication**
12. ♻️ **Secure recovery**
13. ✅ **Post-recovery validation**
14. 📋 **Incident documentation**
15. 🧠 **Lessons learned**
16. 🛡️ **Preventive control design**

---

# ⏱️ Incident Response Timeline

| Time UTC  | Incident Activity                          |
| --------- | ------------------------------------------ |
| **14:02** | 🔑 Simulated developer key disclosure      |
| **14:08** | 🌍 New-source cloud discovery calls        |
| **14:10** | 🚨 Detection triggers                      |
| **14:14** | 👤 Analyst validates credential ownership  |
| **14:18** | 🛑 Compromised credential disabled         |
| **14:24** | 🔍 Scope and peer activity reviewed        |
| **14:33** | 🔐 Least-privilege remediation implemented |
| **14:46** | ✅ Approved access recovery validated       |
| **15:15** | 🛡️ Preventive actions approved            |

📊 Full normalized chronology:

`timeline.csv`

---

# 🔎 Detection Engineering

![Python](https://img.shields.io/badge/Python-Detection_Engineering-3776AB?logo=python\&logoColor=white)
![Detections](https://img.shields.io/badge/Runnable_Detections-3-brightgreen)
![Evidence](https://img.shields.io/badge/Evidence-Synthetic_JSONL-blue)

The project contains **three runnable Python detections**.

These detections operate against local synthetic evidence, allowing reviewers to evaluate the detection logic without requiring cloud credentials.

---

## 🔑 Detection 01 — Credential Compromise

`detections/credential-compromise.py`

### Detection Goal

Identify suspicious cloud discovery activity from a previously unseen source following a leaked-key scenario.

### Detection Logic

The detection looks for behavioral indicators including:

* 🌍 New source activity
* 🔑 Credential use
* 🔎 Discovery actions
* ⏱️ Activity burst
* 👤 Identity association

### Security Question

> **Is a legitimate credential suddenly being used in a way that differs from its expected behavior?**

---

## 🌍 Detection 02 — Impossible Travel

`detections/impossible_travel.py`

### Detection Goal

Identify geographically inconsistent authentication behavior.

The detection evaluates normalized sign-in activity for:

* 👤 Same user
* 🌎 Different countries
* ⏱️ Authentication events within 30 minutes

### Security Question

> **Could the same identity realistically have authenticated from both locations within the observed timeframe?**

---

## 🔐 Detection 03 — Password Spray

`detections/password_spray.py`

### Detection Goal

Identify one source attempting authentication across multiple accounts before eventually succeeding.

Detection indicators include:

* 🌍 Common source
* ❌ Multiple failed authentications
* 👥 Multiple targeted identities
* ✅ Subsequent successful authentication

### Security Question

> **Is one source systematically testing credentials across multiple accounts?**

---

# 📊 Detection Philosophy

The project emphasizes **behavior and context**, not simply isolated events.

A single failed login may be normal.

A single discovery call may be legitimate.

A new IP address may be harmless.

Risk increases when multiple signals combine.

```text
New Source
    +
Valid Credential
    +
Discovery Activity
    +
Unexpected Behavior
    =
Higher-Confidence Security Signal
```

This reduces reliance on simplistic single-event alerting.

---

# 🔍 Investigation Workflow

The investigation follows a structured process.

## 1️⃣ Validate the Alert

Determine:

* Did the detection execute correctly?
* Is the activity expected?
* Does the source belong to an approved system?
* Is the affected identity legitimate?

---

## 2️⃣ Identify the Principal

Determine:

* 👤 Identity owner
* 🔑 Credential involved
* 🏢 Expected role
* ☁️ Expected cloud access
* 🕐 Normal usage pattern

---

## 3️⃣ Build the Timeline

Events are normalized chronologically.

This helps determine:

* What happened first?
* What occurred after credential exposure?
* When was the alert generated?
* How quickly was containment performed?
* Was activity observed after containment?

---

## 4️⃣ Determine Scope

The investigation evaluates:

* ☁️ Resources accessed
* 🔐 Permissions available
* 👥 Other identities affected
* 🔑 Additional credentials
* 🌐 Source activity
* 📊 Administrative events

The objective is to determine the **blast radius**, not merely confirm that the credential was compromised.

---

## 5️⃣ Preserve Evidence

Relevant evidence is retained before unnecessary changes are made.

This supports:

* Investigation
* Timeline reconstruction
* Root-cause analysis
* Post-incident reporting
* Detection improvement

---

# 🧾 Investigation Evidence

![Evidence](https://img.shields.io/badge/Investigation-Evidence_Preserved-blue)
![IOC](https://img.shields.io/badge/IOC-Register-orange)
![Timeline](https://img.shields.io/badge/Timeline-Normalized-success)

The repository includes several investigation artifacts.

| Artifact                                       | Purpose                                 |
| ---------------------------------------------- | --------------------------------------- |
| 📊 `timeline.csv`                              | Normalized incident chronology          |
| 🚩 `IOC-REGISTER.md`                           | Synthetic indicators and disposition    |
| 📂 `evidence/`                                 | Audit and authentication events         |
| 📖 `playbooks/compromised-cloud-credential.md` | Containment and recovery procedure      |
| 📋 `post-incident-report.md`                   | Executive and technical incident report |
| 🧠 `LESSONS-LEARNED.md`                        | Gaps, findings, and corrective actions  |

---

# 🚩 Indicator Management

Indicators are documented in:

`IOC-REGISTER.md`

The register provides a structured location for recording:

* 🌍 Source indicators
* 👤 Identity context
* 🔑 Credential relationships
* 📊 Associated events
* 🔍 Investigation status
* ✅ Disposition

The objective is to prevent investigation evidence from becoming disconnected across multiple files.

---

# 🛑 Containment

Once the credential compromise is validated, the priority becomes stopping unauthorized access.

### Containment Actions

1. 🔑 Disable affected credential
2. 🔌 Revoke active access where applicable
3. 🔍 Review recent identity activity
4. 👥 Review related identities
5. ☁️ Identify affected resources
6. 📊 Preserve relevant logs
7. 🚨 Monitor for continued activity

### Containment Principle

> **Stop the threat while preserving enough evidence to understand the incident.**

---

# 🧹 Eradication

Containment stops immediate activity.

Eradication addresses the conditions that allowed the incident to occur.

Actions include:

* 🗑️ Remove compromised credential
* 🔐 Correct excessive permissions
* 🔑 Replace approved credentials where required
* 🔍 Review related secrets
* 📋 Validate IAM assignments
* 🛡️ Correct security-control gaps

The goal is to prevent the environment from returning to the same vulnerable state.

---

# ♻️ Recovery

Recovery restores legitimate operational access safely.

The process follows:

`Contain`

⬇️

`Remediate`

⬇️

`Reauthorize`

⬇️

`Validate`

⬇️

`Monitor`

Legitimate access is not restored simply by creating another credential.

The replacement access must follow:

* 🔐 Least privilege
* 👤 Correct ownership
* ⏳ Appropriate lifetime
* 📋 Approved scope
* 📊 Monitoring

---

# ✅ Recovery Validation

Recovery is considered successful only after validation confirms:

* ❌ Compromised credential no longer works
* 👤 Approved identity access functions
* 🔐 Permissions match intended role
* ☁️ Required cloud operations succeed
* 🚫 Unauthorized operations fail
* 📊 Monitoring remains active
* 🚨 No continued suspicious activity is observed

---

# 📖 Incident Response Playbook

![Playbook](https://img.shields.io/badge/IR-Playbook-blue)
![Credential Response](https://img.shields.io/badge/Scenario-Cloud_Credential-orange)

The reusable response procedure is documented in:

`playbooks/compromised-cloud-credential.md`

The playbook follows:

**Trigger → Validate → Scope → Contain → Eradicate → Recover → Validate → Escalate → Document**

This converts one simulated incident into reusable operational knowledge.

---

# 📋 Post-Incident Report

`post-incident-report.md`

The post-incident report provides both:

### 👔 Executive Perspective

* What happened?
* What was the impact?
* Was the incident contained?
* What is being done to prevent recurrence?

### 🧑‍💻 Technical Perspective

* Detection
* Timeline
* Evidence
* Root cause
* Scope
* Containment
* Remediation
* Recovery
* Corrective actions

This demonstrates the ability to communicate the same incident to both technical and nontechnical stakeholders.

---

# 🧠 Lessons Learned

`LESSONS-LEARNED.md`

Incident response does not end when access is restored.

The lessons-learned process evaluates:

* What worked?
* What delayed response?
* Which controls failed?
* Which controls reduced impact?
* Which detection opportunities were missed?
* What should be automated?
* What should be prevented entirely?

---

# 🛡️ Preventive Security Engineering

The strongest outcome of incident response is preventing the next incident.

The project emphasizes several preventive controls.

### 🔑 Short-Lived Credentials

Reduce dependence on persistent access keys.

### 🔐 Least Privilege

Limit what a compromised identity can access.

### 🔎 Secret Scanning

Detect exposed credentials before they become operational incidents.

### 🚨 Behavioral Detection

Identify unusual credential activity.

### 👑 Privileged Access Separation

Prevent standard developer credentials from automatically providing broad administrative authority.

### 📊 Continuous Monitoring

Ensure suspicious activity remains visible after remediation.

---

# 🔄 Incident Response Lifecycle

```text
                     🚨 Detection
                          │
                          ▼
                       🎫 Triage
                          │
                          ▼
                    🔍 Investigation
                          │
                          ▼
                   🧾 Preserve Evidence
                          │
                          ▼
                     💥 Scope Impact
                          │
                          ▼
                     🛑 Containment
                          │
                          ▼
                     🧹 Eradication
                          │
                          ▼
                       ♻️ Recovery
                          │
                          ▼
                     ✅ Validation
                          │
                          ▼
                 📋 Post-Incident Review
                          │
                          ▼
                  🧠 Lessons Learned
                          │
                          ▼
                 🛡️ Preventive Controls
```

---

# 🧰 Skills Demonstrated

![Python](https://img.shields.io/badge/Python-Security_Automation-3776AB?logo=python\&logoColor=white)
![Cloud Security](https://img.shields.io/badge/Cloud-Security-success)
![IAM](https://img.shields.io/badge/Identity-IAM-blue)
![Incident Response](https://img.shields.io/badge/Incident-Response-red)
![Detection Engineering](https://img.shields.io/badge/Detection-Engineering-blueviolet)
![MITRE ATT\&CK](https://img.shields.io/badge/MITRE-ATT%26CK-E34F26)
![SOC](https://img.shields.io/badge/SOC-Operations-critical)

### 🛡️ Security Operations

Alert Triage • Investigation • Evidence Analysis • IOC Management • Incident Documentation

### 🚨 Incident Response

Detection • Containment • Eradication • Recovery • Validation • Post-Incident Review

### 🔎 Detection Engineering

Python • Behavioral Detection • Credential Abuse • Impossible Travel • Password Spray

### 🔐 Identity Security

IAM • Credential Security • Least Privilege • Privileged Access • Access Remediation

### ☁️ Cloud Security

Cloud Audit Events • Identity Activity • Discovery Behavior • Blast-Radius Analysis

### 📋 Governance

Incident Timeline • IOC Register • Playbooks • PIR • Lessons Learned • Corrective Actions

---

# 📂 Project Evidence

| Evidence                                       | Demonstrates                       |
| ---------------------------------------------- | ---------------------------------- |
| 🐍 `detections/credential-compromise.py`       | Cloud credential-abuse detection   |
| 🌍 `detections/impossible_travel.py`           | Authentication anomaly detection   |
| 🔐 `detections/password_spray.py`              | Password-spray detection           |
| 📂 `evidence/`                                 | Synthetic investigation evidence   |
| 📊 `timeline.csv`                              | Incident chronology                |
| 🚩 `IOC-REGISTER.md`                           | Indicator tracking and disposition |
| 📖 `playbooks/compromised-cloud-credential.md` | Reusable IR procedure              |
| 📋 `post-incident-report.md`                   | Executive and technical reporting  |
| 🧠 `LESSONS-LEARNED.md`                        | Corrective actions and improvement |

---

# 🧠 Key Security Decisions

## 1️⃣ Contain the Credential Before Rebuilding Access

The affected credential is disabled before normal access is restored.

**Why?**

Creating replacement access without removing compromised access could leave the attacker active.

---

## 2️⃣ Preserve Evidence Before Unnecessary Changes

Logs and relevant events are retained during investigation.

**Why?**

Aggressive remediation can destroy evidence required to determine root cause and blast radius.

---

## 3️⃣ Investigate Scope, Not Just the Alert

The response evaluates related resources, identities, permissions, and events.

**Why?**

Confirming credential compromise does not answer what the credential actually allowed an attacker to do.

---

## 4️⃣ Restore Least-Privilege Access

Recovery does not simply recreate the previous credential configuration.

**Why?**

An incident is an opportunity to correct excessive permissions rather than reproduce them.

---

## 5️⃣ Convert Incidents Into Preventive Controls

The final stage produces improvements such as secret scanning, anomaly detection, credential changes, and IAM hardening.

**Why?**

A mature security program should become more difficult to compromise after every incident.

---

# ⚖️ Key Engineering Tradeoff

The central incident-response tradeoff is:

> **Speed of containment ↔ Evidence preservation**

Security teams need to stop malicious activity quickly.

However, immediately changing everything can destroy evidence needed to understand:

* Initial access
* Attacker activity
* Scope
* Root cause
* Potential persistence

The response therefore prioritizes:

**Preserve critical evidence → Disable compromised access → Determine scope → Remediate → Recover**

This balances operational urgency with investigation quality.

---

# 💼 Interview Discussion

> **“I built a simulated Security Operations and Incident Response exercise around a compromised cloud developer credential. A synthetic access key was exposed in a public-code scenario and then used from a new source for cloud discovery activity. I created Python detections for credential compromise, impossible travel, and password spraying, normalized the incident timeline, maintained an IOC register, investigated the affected identity and potential blast radius, contained the credential, corrected permissions, restored approved least-privilege access, and documented the response through a reusable playbook and post-incident report. The biggest lesson was that fast containment is important, but controls such as short-lived credentials, least privilege, secret scanning, and behavioral detection can reduce both the probability and impact of credential compromise.”**

---

# 📂 Repository Structure

```text
03-security-operations-incident-response/
│
├── 🔎 detections/
│   ├── credential-compromise.py
│   ├── impossible_travel.py
│   └── password_spray.py
│
├── 🧾 evidence/
│   └── synthetic audit and sign-in evidence
│
├── 📖 playbooks/
│   └── compromised-cloud-credential.md
│
├── 🚩 IOC-REGISTER.md
├── 🧠 LESSONS-LEARNED.md
├── 📋 post-incident-report.md
├── 📊 timeline.csv
└── 📄 README.md
```

---

# 🏆 Project Outcome

This project demonstrates a complete security-operations workflow where an alert does not end at detection.

The incident progresses through:

* 🚨 Detection
* 🎫 Triage
* 🔍 Investigation
* 🧾 Evidence preservation
* 💥 Scope analysis
* 🛑 Containment
* 🧹 Eradication
* ♻️ Recovery
* ✅ Validation
* 📋 Post-incident review
* 🧠 Lessons learned
* 🛡️ Preventive security engineering

The most important outcome is not simply that the simulated compromised credential was disabled.

The environment becomes **more resilient after the incident than it was before it.**

---

## ➡️ Next Project

### 🤖 Project 04 — CloudGuardian Security Auditor

The next project moves from reactive security operations into proactive security automation by using Python to identify cloud and identity security weaknesses before they become incidents.
