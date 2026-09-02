# 🤖 Project 04 — CloudGuardian Security Auditor

![Python](https://img.shields.io/badge/Python-Security_Automation-3776AB?logo=python\&logoColor=white)
![Cloud Security](https://img.shields.io/badge/Cloud-Security-success)
![IAM](https://img.shields.io/badge/IAM-Security-blue)
![Security Audit](https://img.shields.io/badge/Security-Auditing-critical)
![Automation](https://img.shields.io/badge/Security-Automation-blueviolet)
![JSON](https://img.shields.io/badge/Output-JSON-yellow)
![CSV](https://img.shields.io/badge/Output-CSV-blue)
![HTML](https://img.shields.io/badge/Output-HTML-E34F26?logo=html5\&logoColor=white)
![Tests](https://img.shields.io/badge/Automated_Tests-Passing-brightgreen)
![Status](https://img.shields.io/badge/Project-Complete-brightgreen)
![Portfolio](https://img.shields.io/badge/Portfolio-Job_Ready-success)

> **CloudGuardian is a Python-based cloud security auditing and posture-assessment tool that evaluates identity, permissions, credentials, storage, network exposure, encryption, and resource-governance controls and converts technical findings into actionable remediation reports.**

---

## 🎯 Overview

**CloudGuardian** was built to answer a practical cloud-security question:

> **How can a cloud operations or security team identify high-risk configuration weaknesses before they become incidents?**

Instead of manually reviewing every identity, credential, policy, storage resource, network rule, and governance setting, CloudGuardian provides a repeatable auditing workflow.

The tool evaluates structured cloud-security inventory data against defined security controls and produces prioritized findings.

CloudGuardian focuses on:

* 🔑 MFA coverage
* 👑 Privileged identities
* 💤 Dormant accounts
* ⏳ Stale credentials
* ⚠️ Excessive permissions
* 🔓 Public storage
* 🌐 Exposed management ports
* 🔐 Encryption
* 🏷️ Resource governance
* 📊 Security scoring
* 🛠️ Remediation guidance
* 📄 Machine-readable and human-readable reporting

The project demonstrates the transition from:

**Manual Security Review → Automated Control Evaluation → Risk Prioritization → Remediation → Validation**

> ⚠️ **Environment Notice:** CloudGuardian operates against synthetic/local portfolio datasets included with this project. Findings and security scores represent the simulated environment and do not represent a production organization or employer environment.

---

# 🏢 Business Scenario

Northstar Digital Services operates cloud resources across multiple environments.

As cloud adoption grows, manually reviewing every resource becomes increasingly difficult.

Security teams need answers to questions such as:

* 🔑 Which privileged identities are missing MFA?
* 💤 Which accounts are dormant?
* ⏳ Which credentials are stale?
* ⚠️ Which identities have excessive permissions?
* 🔓 Is any storage publicly accessible?
* 🌐 Are administrative ports exposed?
* 🔐 Are resources encrypted?
* 🏷️ Are resources missing required ownership metadata?
* 🚨 Which findings require immediate remediation?
* 📈 Is security posture improving after remediation?

CloudGuardian automates these checks and converts raw configuration data into prioritized security findings.

---

# 🎯 Project Objectives

CloudGuardian demonstrates:

1. 🐍 **Python security automation**
2. ☁️ **Cloud security posture assessment**
3. 🔐 **Identity-security auditing**
4. 👑 **Privileged-access review**
5. 🔑 **MFA validation**
6. 💤 **Dormant-account detection**
7. ⏳ **Credential-age analysis**
8. ⚠️ **Permission-risk identification**
9. 🔓 **Public-resource detection**
10. 🌐 **Network-exposure analysis**
11. 🔐 **Encryption validation**
12. 🏷️ **Resource-governance validation**
13. 🚦 **Finding severity classification**
14. 📊 **Security scoring**
15. 🛠️ **Remediation recommendations**
16. 📄 **JSON, CSV, and HTML reporting**
17. 🧪 **Automated testing**
18. ♻️ **Post-remediation validation**

---

# 🧠 Why CloudGuardian Exists

Cloud environments generate enormous amounts of configuration data.

Raw inventory alone does not answer:

> **What is actually risky?**

CloudGuardian applies security logic to configuration data.

```text
Cloud Inventory
      ↓
Normalize Data
      ↓
Evaluate Controls
      ↓
Identify Findings
      ↓
Assign Severity
      ↓
Calculate Risk
      ↓
Recommend Remediation
      ↓
Generate Reports
      ↓
Remediate
      ↓
Re-Scan
      ↓
Validate Improvement
```

The goal is not simply to identify configuration differences.

The goal is to identify **security-relevant conditions that require action**.

---

# 🔍 Security Controls

## 🔑 MFA Coverage

![MFA](https://img.shields.io/badge/Control-MFA-success)

CloudGuardian evaluates whether identities—particularly privileged identities—have MFA enabled.

### Risk

A privileged account without MFA creates a substantially larger risk if the password is compromised.

### Example Finding

```text
HIGH — Privileged identity missing MFA
Identity: cloud-admin
Risk: Password compromise could provide privileged cloud access.
Remediation: Require MFA before privileged access is permitted.
```

---

# 👑 Privileged Identity Review

CloudGuardian identifies privileged identities and evaluates them against stronger security expectations.

Checks include:

* 🔑 MFA
* ⏳ Credential age
* 💤 Dormancy
* ⚠️ Permission scope
* 👤 Ownership

Privileged accounts receive greater scrutiny because compromise can produce a larger blast radius.

---

# 💤 Dormant Accounts

![Dormant Accounts](https://img.shields.io/badge/Control-Dormant_Accounts-blue)

Accounts that remain enabled but unused can create unnecessary attack surface.

CloudGuardian identifies identities whose activity exceeds the configured dormancy threshold.

### Security Principle

> **Access that is no longer needed should not remain available indefinitely.**

---

# ⏳ Stale Credentials

![Credentials](https://img.shields.io/badge/Control-Credential_Age-orange)

Long-lived credentials increase exposure.

CloudGuardian evaluates credential age and identifies keys requiring rotation or retirement.

### Recommended Response

* 🔄 Rotate required credentials
* 🗑️ Remove unused credentials
* 🔐 Prefer temporary credentials
* 📊 Monitor credential usage

---

# ⚠️ Excessive Permissions

![Least Privilege](https://img.shields.io/badge/Control-Least_Privilege-success)

CloudGuardian identifies permission patterns that violate least-privilege expectations.

Examples include:

```text
*
*:* 
Administrator-level access
Broad wildcard permissions
Unnecessary privileged roles
```

### Security Question

> **Does this identity have more access than its job function requires?**

The objective is not merely to remove permissions.

It is to reduce **blast radius** while preserving legitimate operational capability.

---

# 🔓 Public Storage

![Storage Security](https://img.shields.io/badge/Control-Storage_Exposure-red)

CloudGuardian evaluates storage resources for public exposure.

Potential findings include:

* 🌍 Public bucket/container
* 🔓 Anonymous access
* ⚠️ Missing access restriction
* 🏷️ Missing ownership information

### Risk

Public storage can expose sensitive information or unintentionally make internal resources available externally.

---

# 🌐 Network Exposure

![Network Security](https://img.shields.io/badge/Control-Network_Exposure-critical)

CloudGuardian evaluates network rules for risky administrative exposure.

High-risk examples include:

```text
0.0.0.0/0 → TCP/22
0.0.0.0/0 → TCP/3389
```

These represent unrestricted Internet access to administrative services such as:

* 🐧 SSH
* 🪟 RDP

### Preferred Controls

* 🔒 Restricted source ranges
* 🔐 VPN
* 🧱 Bastion access
* 🪪 Identity-aware access
* 🚫 No unnecessary public administration

---

# 🔐 Encryption Validation

CloudGuardian checks whether supported resources meet expected encryption requirements.

The control asks:

> **Is sensitive data protected at rest according to the defined security baseline?**

Resources that fail the expected encryption policy are surfaced for remediation.

---

# 🏷️ Resource Governance

![Governance](https://img.shields.io/badge/Control-Resource_Governance-blue)

Security also requires knowing who owns a resource.

CloudGuardian validates required metadata such as:

* `environment`
* `owner`
* `application`
* `cost-center`
* `managed-by`

Missing metadata can make:

* 🚨 Incident response slower
* 💰 Cost attribution harder
* 🔍 Security investigations more difficult
* 🤖 Automation unreliable
* 📋 Governance inconsistent

---

# 🚦 Finding Severity

CloudGuardian prioritizes findings by operational risk.

| Severity        | Meaning                                       | Example                                               |
| --------------- | --------------------------------------------- | ----------------------------------------------------- |
| 🔴 **Critical** | Immediate high-impact exposure                | Public administrative access with privileged exposure |
| 🟠 **High**     | Serious weakness requiring prompt remediation | Privileged identity without MFA                       |
| 🟡 **Medium**   | Security weakness requiring correction        | Stale credential                                      |
| 🔵 **Low**      | Governance or hygiene issue                   | Missing metadata                                      |

Severity helps teams answer:

> **What should we fix first?**

---

# 📊 Security Score

![Security Score](https://img.shields.io/badge/Security-Posture_Scoring-blueviolet)

CloudGuardian converts findings into an overall posture score.

A simplified conceptual model:

```text
Starting Score: 100

Critical Finding → largest deduction
High Finding     → significant deduction
Medium Finding   → moderate deduction
Low Finding      → smaller deduction

Final Score = Security Posture Score
```

The score is intended as a **prioritization and comparison mechanism**, not a substitute for professional risk analysis.

Its greatest value appears when comparing:

**Before Remediation → After Remediation**

---

# 🖥️ Example CloudGuardian Assessment

```text
CLOUDGUARDIAN
Cloud Security Assessment
==================================================

IDENTITY SECURITY
--------------------------------------------------
Privileged identities reviewed
MFA coverage evaluated
Dormant identities checked
Credential age evaluated
Permission scope analyzed

CLOUD SECURITY
--------------------------------------------------
Storage exposure checked
Network exposure checked
Encryption controls evaluated
Resource governance validated

FINDINGS
--------------------------------------------------
Critical / High / Medium / Low findings prioritized

OUTPUT
--------------------------------------------------
JSON report generated
CSV findings generated
HTML assessment generated

NEXT STEP
--------------------------------------------------
Review findings → Remediate → Re-run assessment
```

> 📌 Actual results are generated from the included simulated datasets and should be interpreted only within the portfolio environment.

---

# 🔄 Remediation Workflow

CloudGuardian is designed to support a complete remediation lifecycle.

```text
🔍 Scan
   ↓
🚨 Identify Finding
   ↓
🚦 Assign Severity
   ↓
🧠 Determine Risk
   ↓
🛠️ Recommend Remediation
   ↓
🔧 Apply Fix
   ↓
🔁 Re-Scan
   ↓
✅ Validate
```

This is important because finding vulnerabilities without validating remediation leaves the security lifecycle incomplete.

---

# ♻️ Before & After Validation

The project includes insecure and remediated datasets to demonstrate the effect of security improvements.

### Before Remediation

CloudGuardian identifies intentionally planted weaknesses.

Examples may include:

* 🔑 MFA gaps
* 💤 Dormant privileged access
* ⏳ Stale credentials
* ⚠️ Excessive permissions
* 🔓 Public storage
* 🌐 Administrative exposure
* 🔐 Encryption gaps
* 🏷️ Governance issues

### Remediation

Security controls are corrected.

### After Remediation

CloudGuardian is executed again.

Expected outcome:

```text
Initial Environment
      ↓
Security Findings
      ↓
Remediation
      ↓
Re-Scan
      ↓
Reduced Findings
      ↓
Improved Security Posture
```

This demonstrates **security validation**, not just security detection.

---

# 📄 Reporting

![JSON](https://img.shields.io/badge/Report-JSON-yellow)
![CSV](https://img.shields.io/badge/Report-CSV-blue)
![HTML](https://img.shields.io/badge/Report-HTML-E34F26?logo=html5\&logoColor=white)

CloudGuardian produces multiple report formats because different consumers need different outputs.

## 🧾 JSON

Useful for:

* APIs
* Automation
* SIEM ingestion
* Future integrations
* Machine processing

## 📊 CSV

Useful for:

* Analyst review
* Spreadsheet analysis
* Finding tracking
* Governance workflows

## 🌐 HTML

Useful for:

* Human-readable assessment
* Security review
* Portfolio presentation
* Management reporting

---

# 🐍 Python Engineering

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python\&logoColor=white)
![Automation](https://img.shields.io/badge/Engineering-Automation-success)
![Testing](https://img.shields.io/badge/Testing-Automated-brightgreen)

CloudGuardian demonstrates Python beyond simple scripting.

The project includes concepts such as:

* 📥 Data ingestion
* 🔄 Normalization
* 🧠 Control logic
* 🚨 Finding generation
* 🚦 Severity classification
* 📊 Scoring
* 🛠️ Remediation mapping
* 📄 Report generation
* 🧪 Automated validation

The tool separates **security logic from reporting**, making it easier to extend.

---

# 🧪 Testing Strategy

Security automation must be testable.

CloudGuardian includes automated tests that verify expected findings against controlled datasets.

Testing answers questions such as:

* Does a missing-MFA condition trigger?
* Does stale credential logic behave correctly?
* Are wildcard permissions detected?
* Is public storage identified?
* Are exposed management ports detected?
* Does a remediated environment produce fewer findings?

This reduces the risk of assuming a security control works simply because the script executes successfully.

---

# 🛡️ Security Engineering Principles

## 1️⃣ Least Privilege

Grant only the access required.

## 2️⃣ Strong Authentication

Privileged access requires stronger identity controls.

## 3️⃣ Minimize Persistent Credentials

Prefer temporary access where practical.

## 4️⃣ Private by Default

Resources should not be publicly accessible unless explicitly required.

## 5️⃣ Encrypt Sensitive Resources

Data protection should be part of the baseline.

## 6️⃣ Establish Ownership

Every important resource should have an accountable owner.

## 7️⃣ Automate Repeatable Controls

Controls that can be evaluated consistently should not depend entirely on manual review.

## 8️⃣ Validate Remediation

A finding is not truly resolved until the environment is reassessed.

---

# 🔗 Relationship to Project 03

Project 03 demonstrated **reactive security operations**:

`Attack Signal → Detection → Investigation → Containment → Recovery`

CloudGuardian adds **proactive security operations**:

`Configuration → Assessment → Finding → Remediation → Validation`

Together they demonstrate two sides of cloud security:

### 🚨 Reactive

Respond effectively when suspicious activity occurs.

### 🛡️ Proactive

Identify weaknesses before attackers exploit them.

---

# 🧰 Skills Demonstrated

![Python](https://img.shields.io/badge/Python-Security_Tooling-3776AB?logo=python\&logoColor=white)
![Cloud Security](https://img.shields.io/badge/Cloud-Security-success)
![IAM](https://img.shields.io/badge/IAM-Least_Privilege-blue)
![Automation](https://img.shields.io/badge/Security-Automation-blueviolet)
![Network Security](https://img.shields.io/badge/Network-Security-critical)
![Governance](https://img.shields.io/badge/Cloud-Governance-orange)

### 🐍 Python

Security Automation • Data Processing • Control Logic • Reporting • Testing

### 🔐 Identity Security

MFA • Privileged Accounts • Dormant Accounts • Credential Age • Permissions

### ☁️ Cloud Security

Storage Exposure • Network Exposure • Encryption • Configuration Assessment

### 🛡️ Security Engineering

Least Privilege • Risk Prioritization • Security Baselines • Remediation Validation

### 📊 Governance

Security Scoring • Resource Ownership • Finding Tracking • Reporting

---

# 🧠 Key Engineering Decisions

## 1️⃣ Findings Must Be Actionable

CloudGuardian does not simply say:

> “Configuration failed.”

A useful finding should explain:

**What is wrong → Why it matters → How severe it is → What should be done**

---

## 2️⃣ Privileged Identities Receive Greater Scrutiny

Not every identity creates equal risk.

**Why?**

A compromised privileged account can produce a substantially larger blast radius than a restricted read-only identity.

---

## 3️⃣ Security Checks Are Deterministic

Given the same dataset and policy configuration, CloudGuardian should produce consistent results.

**Why?**

Repeatability is essential for automation, testing, and remediation validation.

---

## 4️⃣ Reports Support Multiple Audiences

Machine-readable and human-readable reports are both produced.

**Why?**

Security tooling may need to support:

* Engineers
* Analysts
* Automation
* Governance
* Management

---

## 5️⃣ Remediation Is Revalidated

The project includes a post-remediation assessment.

**Why?**

Security work should prove that the fix changed the security state.

---

# ⚖️ Key Engineering Tradeoff

The central design tradeoff is:

> **Detection coverage ↔ False-positive risk**

A security auditor could flag every unusual configuration.

But excessive low-quality findings create noise and reduce analyst trust.

CloudGuardian therefore focuses on security conditions with clear operational meaning:

* Missing MFA
* Dormant access
* Stale credentials
* Excessive permissions
* Public resources
* Exposed administrative services
* Missing encryption
* Missing governance metadata

The objective is not to produce the largest number of findings.

The objective is to produce **findings worth investigating**.

---

# 🚀 Running CloudGuardian

From the Project 04 directory:

```bash
python3 cloudguardian.py
```

Run the automated tests:

```bash
python3 -m unittest discover tests
```

Review the generated reports after execution.

> Exact commands should match the filenames and directory structure included in this project.

---

# 💼 Interview Discussion

> **“I built CloudGuardian, a Python-based cloud security auditing tool that evaluates identity and infrastructure configuration against a defined security baseline. It checks areas such as MFA, privileged identities, dormant accounts, stale credentials, excessive permissions, public storage, exposed administrative ports, encryption, and resource governance. The tool converts those checks into prioritized findings with remediation guidance and generates JSON, CSV, and HTML reports. I also created insecure and remediated datasets so I could test the full lifecycle—detect the weaknesses, apply remediation, run the assessment again, and verify that the security posture improved. The main engineering challenge was balancing useful detection coverage with false-positive risk so that findings remained actionable.”**

---

# 📂 Repository Structure

```text
04-cloudguardian-security-auditor/
│
├── 🐍 cloudguardian.py
│
├── 📂 data/
│   ├── insecure environment data
│   └── remediated environment data
│
├── 📄 reports/
│   ├── JSON output
│   ├── CSV output
│   └── HTML output
│
├── 🧪 tests/
│   └── automated CloudGuardian tests
│
└── 📄 README.md
```

---

# 🏆 Project Outcome

CloudGuardian demonstrates how repetitive cloud-security review can be transformed into **repeatable security engineering**.

Instead of manually reviewing every resource independently, the workflow becomes:

* 📥 Collect configuration data
* 🔄 Normalize the environment
* 🔍 Evaluate security controls
* 🚨 Identify weaknesses
* 🚦 Prioritize risk
* 🛠️ Recommend remediation
* 📄 Generate reports
* 🔧 Apply fixes
* 🔁 Re-run the assessment
* ✅ Validate improvement

The result is a security workflow that is:

**Repeatable • Testable • Auditable • Actionable • Automatable**

CloudGuardian also serves as the bridge between the portfolio's security-operations work and its DevSecOps work.

Instead of waiting for security weaknesses to become incidents, security controls can increasingly be evaluated **before infrastructure changes reach production-like environments.**

---

## ➡️ Next Project

### ♾️ Project 05 — DevSecOps Infrastructure Delivery

The final project moves security earlier into the infrastructure lifecycle by integrating Terraform validation, security scanning, secret detection, policy enforcement, testing, and controlled CI/CD delivery.
