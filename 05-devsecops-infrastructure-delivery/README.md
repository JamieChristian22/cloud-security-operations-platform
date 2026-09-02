# ♾️ Project 05 — DevSecOps Infrastructure Delivery

![DevSecOps](https://img.shields.io/badge/DevSecOps-Secure_Delivery-success)
![Terraform](https://img.shields.io/badge/Terraform-IaC-844FBA?logo=terraform\&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-CI%2FCD-2088FF?logo=githubactions\&logoColor=white)
![Python](https://img.shields.io/badge/Python-Policy_as_Code-3776AB?logo=python\&logoColor=white)
![Checkov](https://img.shields.io/badge/Checkov-IaC_Security-blue)
![TFLint](https://img.shields.io/badge/TFLint-Terraform_Quality-blueviolet)
![Gitleaks](https://img.shields.io/badge/Gitleaks-Secret_Scanning-red)
![Policy as Code](https://img.shields.io/badge/Policy_as_Code-Enforced-orange)
![Security Gate](https://img.shields.io/badge/Security_Gate-Blocking-critical)
![Status](https://img.shields.io/badge/Project-Complete-brightgreen)
![Portfolio](https://img.shields.io/badge/Portfolio-Job_Ready-success)

> **Production-inspired DevSecOps infrastructure delivery workflow integrating Terraform validation, policy-as-code, security scanning, secret detection, automated testing, change management, human review, and rollback planning to identify unsafe infrastructure changes before deployment.**

---

## 🎯 Overview

This project demonstrates how **security, infrastructure quality, and operational governance can be integrated directly into the delivery lifecycle**.

Infrastructure changes can introduce serious risks:

* 🔓 Public storage
* 🌐 Internet-exposed management ports
* 👑 Wildcard administrative permissions
* 🔑 Exposed secrets
* 🏗️ Invalid Terraform
* ⚙️ Configuration errors
* 📋 Undocumented changes
* ↩️ Missing rollback plans

Instead of discovering these problems after infrastructure has been released, this project applies security and quality controls **before changes are approved for deployment**.

The operating principle is:

> **Unsafe infrastructure should fail the pipeline—not become tomorrow's incident.**

The workflow follows:

**Code → Validate → Test → Scan → Enforce Policy → Review → Approve → Deploy → Verify → Roll Back if Required**

> ⚠️ **Environment Notice:** This project demonstrates a simulated portfolio/lab DevSecOps workflow. It does not claim deployment to an employer production environment. Production-like deployment remains intentionally subject to human review and approval.

---

# 🏢 Business Scenario

Northstar Digital Services manages cloud infrastructure through Infrastructure as Code.

As engineering teams make infrastructure changes, several risks must be controlled.

A proposed change could accidentally:

* 🌍 Make protected storage public
* 🔓 Expose SSH to the Internet
* 🪟 Expose RDP to the Internet
* 👑 Introduce wildcard administrative permissions
* 🔑 Commit sensitive credentials
* 🏗️ Introduce invalid Terraform
* 🛡️ Violate security baselines
* 📋 Bypass change-management requirements
* ↩️ Remove the ability to recover safely

Manual review alone is not enough.

The delivery process therefore combines:

**Automation + Security Gates + Human Review + Change Evidence + Recovery Planning**

---

# 🎯 Project Objectives

This project demonstrates:

1. ♾️ **DevSecOps delivery practices**
2. 🏗️ **Infrastructure as Code validation**
3. 🔐 **Shift-left security**
4. 🐍 **Python policy-as-code**
5. 🚫 **Blocking security gates**
6. 🔎 **Static infrastructure analysis**
7. 🔑 **Secret scanning**
8. 🧪 **Automated testing**
9. 🔄 **CI/CD orchestration**
10. 📋 **Change management**
11. 👀 **Human review and approval**
12. ↩️ **Rollback planning**
13. 📊 **Evidence preservation**
14. 🛡️ **Preventive security engineering**
15. ☁️ **Cloud infrastructure governance**
16. 🔁 **Continuous validation**

---

# 🧠 DevSecOps Philosophy

Traditional delivery can separate development, operations, and security:

```text
Build
  ↓
Deploy
  ↓
Operate
  ↓
Discover Security Problem
  ↓
Emergency Remediation
```

This project moves security earlier:

```text
Code
  ↓
Validate
  ↓
Test
  ↓
Scan
  ↓
Policy Gate
  ↓
Review
  ↓
Approve
  ↓
Deploy
```

The objective is to make unsafe infrastructure **more difficult to release in the first place**.

---

# 🔄 Active CI/CD Pipeline

![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-Automation-2088FF?logo=githubactions\&logoColor=white)
![CI](https://img.shields.io/badge/CI-Automated-success)
![Security](https://img.shields.io/badge/Security-Integrated-critical)

The executable GitHub Actions workflow is located at:

```text
.github/workflows/ci.yml
```

GitHub executes workflows from the repository-level `.github/workflows/` directory.

Project 05 documents the **delivery and security operating model**, while the root workflow performs the executable repository-wide validation.

---

# 🏗️ Pipeline Architecture

```text
                     👨‍💻 Infrastructure Change
                               │
                               ▼
                         🔀 Git Commit / PR
                               │
                               ▼
                     ┌──────────────────────┐
                     │   ⚙️ CI Pipeline     │
                     └──────────┬───────────┘
                                │
               ┌────────────────┴────────────────┐
               │                                 │
               ▼                                 ▼
       🐍 Offline Controls                🏗️ Terraform Security
               │                                 │
               ▼                                 ▼
       📊 Support Analytics                 terraform fmt
               │                                 │
               ▼                                 ▼
       🔎 Security Detections               terraform init
               │                                 │
               ▼                                 ▼
       🛡️ Policy-as-Code                  terraform validate
               │                                 │
               ▼                                 ▼
       🤖 CloudGuardian Tests             terraform test
               │                                 │
               ▼                                 ▼
       🧪 Automation Tests                    TFLint
               │                                 │
               ▼                                 ▼
       📋 Portfolio Validation                Checkov
                                                 │
                                                 ▼
                                              Gitleaks
                                                 │
                         ┌───────────────────────┴───────────┐
                         │                                   │
                         ▼                                   ▼
                    ❌ Gate Fails                       ✅ Gate Passes
                         │                                   │
                         ▼                                   ▼
                  Change Rejected                     👀 Human Review
                                                             │
                                                             ▼
                                                       ✅ Approval
                                                             │
                                                             ▼
                                                   🚀 Deployment Eligible
```

---

# 🛡️ Security Gate

![Policy](https://img.shields.io/badge/Policy_as_Code-Python-3776AB?logo=python\&logoColor=white)
![Gate](https://img.shields.io/badge/Security_Gate-Enforced-red)

The policy engine is located at:

```text
policy/policy_check.py
```

The policy gate evaluates normalized proposed infrastructure changes before approval.

It rejects known unsafe patterns.

---

## 🔓 Control 01 — Public Protected Storage

### Unsafe Pattern

A protected storage resource is proposed with public access.

```text
Protected Storage
        +
Public Access
        =
❌ REJECT
```

### Risk

Public storage can unintentionally expose:

* Sensitive files
* Logs
* Backups
* Application data
* Internal artifacts

### Required Response

Storage must remain private unless an explicitly approved architecture requires public access.

---

# 🌐 Control 02 — Internet-Exposed SSH

![SSH](https://img.shields.io/badge/SSH-Port_22-critical)

The policy gate rejects:

```text
0.0.0.0/0 → TCP/22
```

### Why?

This exposes SSH administration to the entire Internet.

### Safer Alternatives

* 🔒 Restricted source ranges
* 🔐 VPN
* 🧱 Bastion host
* 🪪 Identity-aware access
* ☁️ Cloud-native session management

---

# 🪟 Control 03 — Internet-Exposed RDP

![RDP](https://img.shields.io/badge/RDP-Port_3389-critical)

The policy gate rejects:

```text
0.0.0.0/0 → TCP/3389
```

### Risk

Broad RDP exposure significantly increases the attack surface of Windows administrative services.

The preferred design limits management access to approved administrative paths.

---

# 👑 Control 04 — Wildcard Administrative Actions

![Least Privilege](https://img.shields.io/badge/IAM-Least_Privilege-success)

The policy gate rejects broad administrative actions such as:

```text
*
*:*
```

### Why?

Wildcard administrative access violates least-privilege principles and increases potential blast radius.

### Preferred Model

```text
Required Action
      +
Required Resource
      +
Required Duration
      =
Scoped Permission
```

---

# 🚦 Policy Decision Model

```text
Proposed Infrastructure Change
            │
            ▼
      🔍 Evaluate Policy
            │
     ┌──────┴──────┐
     │             │
     ▼             ▼
Unsafe Pattern   Compliant
     │             │
     ▼             ▼
 ❌ REJECT       ✅ PASS
     │             │
     ▼             ▼
Remediate       Continue CI
     │
     ▼
Re-Test
```

A security warning that can be ignored is weaker than a control that **prevents the unsafe state from advancing**.

---

# 🧪 Terraform Validation

![Terraform](https://img.shields.io/badge/Terraform-1.8.x-844FBA?logo=terraform\&logoColor=white)
![IaC](https://img.shields.io/badge/IaC-Validated-success)

Terraform changes move through several quality controls.

### `terraform fmt`

Validates formatting consistency.

### `terraform init -backend=false`

Initializes Terraform for validation without connecting to the configured remote backend.

### `terraform validate`

Checks Terraform configuration syntax and internal consistency.

### `terraform test`

Executes defined Terraform tests for expected infrastructure behavior.

These stages answer different questions:

| Stage        | Question                                                   |
| ------------ | ---------------------------------------------------------- |
| 📝 `fmt`     | Is the Terraform consistently formatted?                   |
| ⚙️ `init`    | Can required providers/modules initialize?                 |
| ✅ `validate` | Is the configuration structurally valid?                   |
| 🧪 `test`    | Does defined infrastructure behavior satisfy expectations? |

---

# 🔎 TFLint

![TFLint](https://img.shields.io/badge/TFLint-Static_Analysis-blueviolet)

TFLint adds Terraform-focused static analysis.

It helps identify:

* ⚠️ Invalid or problematic patterns
* 📐 Terraform quality issues
* ☁️ Provider-specific problems
* 🧹 Maintainability concerns

Terraform being syntactically valid does not automatically mean it follows good engineering practices.

---

# 🛡️ Checkov

![Checkov](https://img.shields.io/badge/Checkov-IaC_Security-blue)

Checkov adds Infrastructure-as-Code security analysis.

The goal is to identify security weaknesses before infrastructure is deployed.

Examples include:

* 🔓 Public exposure
* 🔐 Missing security controls
* 🌐 Network weaknesses
* 💾 Storage-security issues
* 📊 Logging gaps
* ⚙️ Insecure configuration

---

# 🔑 Gitleaks

![Gitleaks](https://img.shields.io/badge/Gitleaks-Secret_Detection-red)

Gitleaks scans the repository for potential secrets.

Examples include:

* 🔑 API keys
* 🔐 Access tokens
* ☁️ Cloud credentials
* 🪪 Authentication material

This directly reinforces the lessons from **Project 03**, where credential exposure was the simulated incident trigger.

The DevSecOps objective is:

> **Detect the secret before it becomes an incident-response problem.**

---

# 🤖 CloudGuardian Integration

![CloudGuardian](https://img.shields.io/badge/CloudGuardian-Security_Auditor-blueviolet)
![Tests](https://img.shields.io/badge/CloudGuardian-Unit_Tests-success)

Project 04 introduced CloudGuardian as proactive security automation.

Project 05 incorporates CloudGuardian testing into the broader delivery workflow.

This creates a progression:

```text
Project 03
🚨 Detect security incident
        ↓
Project 04
🤖 Automate security assessment
        ↓
Project 05
♾️ Integrate security into delivery
```

The portfolio therefore moves from **reactive response to proactive prevention**.

---

# 🔎 Detection Integration

The CI workflow also executes the security detection logic developed earlier in the platform.

This helps ensure that detection code remains executable as the repository evolves.

Security engineering is treated as code that should be:

* 🔁 Repeatable
* 🧪 Testable
* 🔀 Version controlled
* 🤖 Automatable

---

# 📊 Support Analytics Integration

Operational analytics from the Cloud Support & Reliability Center are also included in repository-wide validation.

This connects DevSecOps with operations.

The broader principle is:

> **Delivery quality includes operational readiness—not just successful code execution.**

---

# 📋 Change Management

![Change Management](https://img.shields.io/badge/Change-Management-blue)
![Evidence](https://img.shields.io/badge/Change-Evidence-success)

Automated security controls do not eliminate the need for documented change management.

The project includes:

```text
changes/CHG-2026-017.md
```

This change record demonstrates a risky infrastructure proposal being:

**Proposed → Evaluated → Rejected → Corrected → Re-tested → Documented**

The guardrail is not bypassed simply because a change is desired.

---

# 🚨 Example Change Scenario

## Initial Proposal

A protected storage resource is proposed with public access.

```text
Infrastructure Change
        ↓
Public Protected Storage
        ↓
Policy Evaluation
        ↓
❌ FAILED
```

The change is **not approved**.

---

## 🛠️ Remediation

The configuration is corrected so the protected storage resource is no longer public.

```text
Rejected Change
      ↓
Security Finding Reviewed
      ↓
Configuration Corrected
      ↓
Policy Re-Tested
      ↓
✅ PASS
```

---

## 📋 Evidence

The change record preserves:

* What was proposed
* Why it failed
* Which control blocked it
* What was changed
* How it was retested
* Final disposition

This creates an auditable security decision rather than an undocumented fix.

---

# 👀 Human Review

![Review](https://img.shields.io/badge/Human-Review_Required-blue)
![Approval](https://img.shields.io/badge/Production_like-Approval_Required-orange)

Automation is intentionally **not treated as the final authority for production-like deployment**.

Human review remains important for:

* 🏢 Business context
* 💥 Blast radius
* 💰 Cost implications
* 🔄 Migration risk
* 🧩 Architectural tradeoffs
* 📋 Change timing
* ↩️ Recovery readiness

The operating model is:

> **Automate what can be evaluated deterministically. Require human judgment where context matters.**

---

# 📋 Pull Request Review

Reviewer guidance is documented in:

```text
docs/pull-request-template.md
```

Reviewers evaluate questions such as:

* What is changing?
* Why is it required?
* What systems are affected?
* What security controls are involved?
* Has testing passed?
* What is the expected blast radius?
* Is rollback possible?
* Is monitoring available?

This improves consistency across infrastructure reviews.

---

# ✅ Release Readiness

The pre-release evidence checklist is located at:

```text
docs/release-checklist.md
```

A change should not become deployment eligible simply because the code exists.

Release readiness considers:

* 🧪 Validation
* 🛡️ Security scanning
* 🔑 Secret detection
* 🚦 Policy compliance
* 👀 Peer review
* 📊 Monitoring
* 📋 Change documentation
* ↩️ Rollback readiness

---

# ↩️ Rollback & Recovery

![Rollback](https://img.shields.io/badge/Rollback-Planned-success)
![Recovery](https://img.shields.io/badge/Recovery-Validated-blue)

The rollback strategy is documented in:

```text
docs/rollback-plan.md
```

A safe deployment process must answer:

> **What happens if the approved change still causes a problem?**

Rollback planning considers:

* 🔄 Reverting the infrastructure change
* 📦 Restoring known-good configuration
* 💾 Protecting state
* 📊 Monitoring recovery
* 🧪 Validating service restoration
* 🚨 Escalating when rollback is unsafe

---

# 🔄 Secure Delivery Lifecycle

```text
👨‍💻 Engineer
    │
    ▼
📝 Infrastructure Change
    │
    ▼
🔀 Pull Request
    │
    ▼
🧪 Automated Validation
    │
    ├── Terraform
    ├── TFLint
    ├── Checkov
    ├── Gitleaks
    ├── Policy-as-Code
    ├── CloudGuardian Tests
    └── Security Detections
    │
    ▼
🚦 Security Gate
    │
 ┌──┴───┐
 │      │
 ▼      ▼
❌ FAIL  ✅ PASS
 │      │
 ▼      ▼
Fix    👀 Review
 │      │
 └──────┤
        ▼
   📋 Change Approval
        │
        ▼
   🚀 Deployment Eligible
        │
        ▼
   📊 Post-Change Validation
        │
        ▼
   ✅ Healthy?
      ┌─┴─┐
      │   │
     Yes  No
      │   │
      ▼   ▼
   Close ↩️ Rollback
```

---

# 🛡️ Shift-Left Security

![Shift Left](https://img.shields.io/badge/Security-Shift_Left-success)

The central DevSecOps idea demonstrated by this project is **shift-left security**.

Instead of:

```text
Deploy → Discover Weakness → Incident → Emergency Fix
```

The preferred model is:

```text
Code → Detect Weakness → Reject → Correct → Validate → Deploy
```

The earlier a defect is detected, the less opportunity it has to create operational or security impact.

---

# 🔗 Portfolio Integration

Project 05 ties the entire Cloud Security & Operations Platform together.

| Project                                  | Capability                    | Project 05 Integration              |
| ---------------------------------------- | ----------------------------- | ----------------------------------- |
| ☁️ **01 — Multi-Cloud Foundation & IAM** | Terraform, IAM, networking    | IaC validation and security testing |
| 🛠️ **02 — Cloud Support & Reliability** | Troubleshooting and analytics | Operational validation              |
| 🛡️ **03 — Security Operations & IR**    | Detection and response        | Detection code validation           |
| 🤖 **04 — CloudGuardian**                | Security automation           | Automated security tests            |
| ♾️ **05 — DevSecOps Delivery**           | Secure CI/CD                  | Integrates controls into delivery   |

This creates one connected engineering story rather than five unrelated projects.

---

# 🧰 Skills Demonstrated

![Terraform](https://img.shields.io/badge/Terraform-Infrastructure_as_Code-844FBA?logo=terraform\&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-CI%2FCD-2088FF?logo=githubactions\&logoColor=white)
![Python](https://img.shields.io/badge/Python-Automation-3776AB?logo=python\&logoColor=white)
![Checkov](https://img.shields.io/badge/Checkov-Security-blue)
![TFLint](https://img.shields.io/badge/TFLint-Quality-blueviolet)
![Gitleaks](https://img.shields.io/badge/Gitleaks-Secrets-red)
![DevSecOps](https://img.shields.io/badge/DevSecOps-Secure_Delivery-success)

### ♾️ DevSecOps

CI/CD • Shift-Left Security • Security Gates • Secure Infrastructure Delivery

### 🏗️ Infrastructure as Code

Terraform • Validation • Testing • Static Analysis • Configuration Quality

### 🛡️ Security Engineering

Policy-as-Code • IaC Security • Secret Detection • Least Privilege • Preventive Controls

### 🐍 Automation

Python • Automated Validation • Policy Enforcement • Security Testing

### 🔀 CI/CD

GitHub Actions • Pull Requests • Automated Gates • Artifact Validation

### 📋 Operations & Governance

Change Management • Peer Review • Release Readiness • Rollback • Recovery

---

# 📂 Project Evidence

| Evidence                           | Demonstrates                                    |
| ---------------------------------- | ----------------------------------------------- |
| 🐍 `policy/policy_check.py`        | Python policy-as-code enforcement               |
| 🧪 `policy/sample-change.json`     | Testable proposed infrastructure change         |
| 📋 `changes/CHG-2026-017.md`       | Rejected → corrected → retested change evidence |
| ✅ `docs/release-checklist.md`      | Release-readiness controls                      |
| ↩️ `docs/rollback-plan.md`         | Recovery and rollback strategy                  |
| 👀 `docs/pull-request-template.md` | Infrastructure review process                   |
| 🏗️ Root Terraform configuration   | Infrastructure-as-Code implementation           |
| ⚙️ `.github/workflows/ci.yml`      | Executable CI/CD validation workflow            |

---

# 🧠 Key Engineering Decisions

## 1️⃣ Security Controls Block Instead of Warn

Known unsafe infrastructure patterns fail the policy gate.

**Why?**

A warning that can be ignored does not reliably prevent insecure infrastructure.

---

## 2️⃣ Security Runs Before Deployment

Scanning occurs during validation.

**Why?**

Preventing an insecure change is safer and less disruptive than remediating it after deployment.

---

## 3️⃣ Terraform Receives Multiple Layers of Validation

Terraform is evaluated through formatting, validation, testing, linting, and security analysis.

**Why?**

No single tool answers every infrastructure-quality or security question.

---

## 4️⃣ Secrets Are Treated Separately

Gitleaks provides dedicated secret detection.

**Why?**

Infrastructure can be perfectly valid while still containing exposed credentials.

---

## 5️⃣ Automation Does Not Replace Human Judgment

Production-like changes still require human review.

**Why?**

Automated tools cannot fully understand business context, migration risk, timing, or organizational impact.

---

## 6️⃣ Every Change Needs a Recovery Path

Rollback is part of delivery planning.

**Why?**

Even validated changes can produce unexpected operational consequences.

---

# ⚖️ Key Engineering Tradeoff

The central DevSecOps tradeoff is:

> **Delivery speed ↔ Security and operational confidence**

Removing controls can make infrastructure changes move faster.

But that speed may introduce:

* 🔓 Security exposure
* 🚨 Incidents
* ⚙️ Configuration failures
* 🔑 Credential leaks
* 💥 Larger blast radius
* ↩️ Difficult recovery

Adding too many poorly designed controls can also create unnecessary friction.

The objective is therefore not:

> **Maximum number of security checks**

It is:

> **High-value automated controls that stop known dangerous patterns while preserving a practical delivery workflow.**

---

# 💼 Interview Discussion

> **“I built the DevSecOps layer of my Cloud Security & Operations Platform to move security earlier into infrastructure delivery. The workflow uses GitHub Actions to orchestrate repository validation and combines Terraform formatting, initialization, validation and testing with TFLint, Checkov, Gitleaks, Python policy-as-code, CloudGuardian tests, and security detection validation. I created blocking policies for high-risk patterns such as public protected storage, SSH or RDP exposed to the Internet, and wildcard administrative permissions. I also documented a simulated change where an unsafe proposal was rejected, corrected, retested, and then documented rather than bypassing the security control. I kept human review and rollback planning in the process because passing automated checks doesn't eliminate operational risk.”**

---

# 📂 Repository Structure

```text
05-devsecops-infrastructure-delivery/
│
├── 📋 changes/
│   └── CHG-2026-017.md
│
├── 📚 docs/
│   ├── release-checklist.md
│   ├── rollback-plan.md
│   └── pull-request-template.md
│
├── 🛡️ policy/
│   ├── policy_check.py
│   └── sample-change.json
│
└── 📄 README.md

Repository-level integration:

.github/
└── workflows/
    └── ci.yml

01-multi-cloud-foundation-iam/
└── terraform/
    └── multi-cloud Terraform implementation
```

---

# 🏆 Project Outcome

This project completes the **Cloud Security & Operations Platform** by integrating infrastructure, operations, security, automation, and governance into one delivery model.

The complete progression is:

```text
☁️ Build Secure Cloud Foundation
            ↓
🛠️ Operate & Troubleshoot Services
            ↓
🚨 Detect & Respond to Security Incidents
            ↓
🤖 Automate Security Assessment
            ↓
♾️ Embed Security Into Delivery
```

The final operating model ensures that:

* 🏗️ Infrastructure is defined as code
* 🧪 Changes are automatically validated
* 🔍 Security weaknesses are scanned
* 🔑 Secrets are checked
* 🚦 Known dangerous patterns are blocked
* 🤖 Security automation is continuously tested
* 👀 Human review remains part of high-impact decisions
* 📋 Change evidence is preserved
* ↩️ Rollback remains possible
* 🛡️ Security becomes part of engineering rather than a final checklist

The result is a delivery process designed to be:

**Repeatable • Secure • Testable • Auditable • Recoverable • Automated**

---

# 🎓 Final Portfolio Story

Together, the five projects demonstrate an end-to-end cloud engineering lifecycle:

### ☁️ Project 01 — Multi-Cloud Foundation & IAM

**Build the foundation securely.**

### 🛠️ Project 02 — Cloud Support & Reliability Center

**Operate, troubleshoot, and improve it.**

### 🛡️ Project 03 — Security Operations & Incident Response

**Detect and respond when suspicious activity occurs.**

### 🤖 Project 04 — CloudGuardian Security Auditor

**Automate proactive security assessment.**

### ♾️ Project 05 — DevSecOps Infrastructure Delivery

**Move those controls into the delivery pipeline so weaknesses can be stopped before deployment.**

> **The portfolio demonstrates not just how to build cloud infrastructure, but how to secure it, operate it, investigate it, automate it, and continuously improve how it is delivered.**

---

## 🏁 Cloud Security & Operations Platform — Complete

![AWS](https://img.shields.io/badge/AWS-Cloud-232F3E?logo=amazonwebservices\&logoColor=white)
![Azure](https://img.shields.io/badge/Azure-Cloud-0078D4?logo=microsoftazure\&logoColor=white)
![Google Cloud](https://img.shields.io/badge/Google_Cloud-Platform-4285F4?logo=googlecloud\&logoColor=white)
![Terraform](https://img.shields.io/badge/Terraform-IaC-844FBA?logo=terraform\&logoColor=white)
![Python](https://img.shields.io/badge/Python-Automation-3776AB?logo=python\&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-CI%2FCD-2088FF?logo=githubactions\&logoColor=white)
![Security](https://img.shields.io/badge/Cloud-Security-success)
![DevSecOps](https://img.shields.io/badge/DevSecOps-Complete-brightgreen)

**Cloud • Security • Operations • IAM • Automation • DevSecOps**
