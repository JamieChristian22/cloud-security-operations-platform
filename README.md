# ☁️🛡️ Cloud Security & Operations Platform

![AWS](https://img.shields.io/badge/AWS-Cloud-232F3E?logo=amazonwebservices\&logoColor=white)
![Azure](https://img.shields.io/badge/Microsoft_Azure-Cloud-0078D4?logo=microsoftazure\&logoColor=white)
![Google Cloud](https://img.shields.io/badge/Google_Cloud-Platform-4285F4?logo=googlecloud\&logoColor=white)
![Terraform](https://img.shields.io/badge/Terraform-IaC-844FBA?logo=terraform\&logoColor=white)
![Python](https://img.shields.io/badge/Python-Automation-3776AB?logo=python\&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-CI%2FCD-2088FF?logo=githubactions\&logoColor=white)
![Cloud Security](https://img.shields.io/badge/Cloud-Security-success)
![IAM](https://img.shields.io/badge/Identity-IAM-blue)
![DevSecOps](https://img.shields.io/badge/DevSecOps-Secure_Delivery-brightgreen)
![Incident Response](https://img.shields.io/badge/Incident-Response-red)
![Status](https://img.shields.io/badge/Portfolio-Complete-brightgreen)

> **Production-inspired multi-cloud engineering portfolio demonstrating how to build, secure, operate, troubleshoot, investigate, automate, and continuously validate cloud environments across AWS, Microsoft Azure, and Google Cloud Platform.**

---

## 🎯 Executive Overview

The **Cloud Security & Operations Platform** is an integrated technical portfolio built around a simulated cloud environment for **Northstar Digital Services**, a fictional 750-user remote-first SaaS organization.

Instead of presenting disconnected labs, this repository models an end-to-end cloud engineering lifecycle:

**☁️ Build → 🔐 Secure → 🛠️ Operate → 🚨 Detect → 🔍 Investigate → 🤖 Automate → ♾️ Deliver Safely**

The platform combines:

* ☁️ AWS, Microsoft Azure, and Google Cloud
* 🏗️ Terraform Infrastructure as Code
* 🔐 IAM, RBAC, MFA, and least privilege
* 🌐 Cloud networking and security controls
* 🛠️ Cloud support and troubleshooting
* 📊 Reliability and operational analytics
* 🚨 Security operations and incident response
* 🔎 Detection engineering
* 🤖 Python security automation
* 🛡️ Cloud security posture assessment
* ♾️ DevSecOps and policy-as-code
* 🔄 GitHub Actions CI/CD
* 🧪 Automated testing and validation
* 💾 Disaster recovery
* 💰 Cost governance
* 📋 Operational documentation and runbooks

> ⚠️ **Portfolio Environment:** Northstar Digital Services, its users, incidents, tickets, credentials, metrics, logs, and infrastructure scenarios are simulated for portfolio/lab purposes. This repository demonstrates technical methodology and engineering practices and does not claim employer production experience or live customer infrastructure.

---

# 🏗️ Platform Architecture

```text
                         👥 Users / Engineers
                                 │
                                 ▼
                    ┌────────────────────────┐
                    │   🔐 Identity & IAM    │
                    │ RBAC • MFA • JML • PAM │
                    └───────────┬────────────┘
                                │
              ┌─────────────────┼─────────────────┐
              │                 │                 │
              ▼                 ▼                 ▼
        🟠 AWS Cloud       🔵 Azure Cloud      🌐 Google Cloud
              │                 │                 │
              └─────────────────┼─────────────────┘
                                │
                                ▼
                    🏗️ Terraform Infrastructure
                                │
                                ▼
                 ┌──────────────────────────────┐
                 │ ☁️ Cloud Operations Layer   │
                 │ Support • Monitoring • RCA  │
                 └──────────────┬───────────────┘
                                │
                 ┌──────────────┴───────────────┐
                 │                              │
                 ▼                              ▼
        🚨 Security Operations          🤖 CloudGuardian
        Detection • IR • IOCs          Security Auditing
                 │                              │
                 └──────────────┬───────────────┘
                                │
                                ▼
                    ♾️ DevSecOps Pipeline
                                │
             ┌──────────────────┼──────────────────┐
             │                  │                  │
             ▼                  ▼                  ▼
        🧪 Testing        🛡️ Security Gates    🔑 Secret Scan
             │                  │                  │
             └──────────────────┼──────────────────┘
                                │
                                ▼
                         👀 Human Review
                                │
                                ▼
                      🚀 Deployment Eligible
```

---

# 🧩 Five Integrated Projects

## ☁️ 01 — Multi-Cloud Foundation & IAM

![AWS](https://img.shields.io/badge/AWS-232F3E?logo=amazonwebservices\&logoColor=white)
![Azure](https://img.shields.io/badge/Azure-0078D4?logo=microsoftazure\&logoColor=white)
![GCP](https://img.shields.io/badge/GCP-4285F4?logo=googlecloud\&logoColor=white)
![Terraform](https://img.shields.io/badge/Terraform-844FBA?logo=terraform\&logoColor=white)
![IAM](https://img.shields.io/badge/IAM-Least_Privilege-success)

**Build the cloud foundation securely.**

Establishes a standardized multi-cloud foundation across AWS, Azure, and GCP with Terraform, IAM governance, private-first networking, logging, role separation, and access lifecycle controls.

### 🔑 Highlights

* Multi-cloud Terraform architecture
* AWS, Azure, and GCP modules
* IAM and RBAC design
* MFA expectations
* Least privilege
* Separation of duties
* Joiner-Mover-Leaver lifecycle
* Quarterly access reviews
* Private-first networking
* Security logging
* Terraform security testing

📂 [`01-multi-cloud-foundation-iam/`](01-multi-cloud-foundation-iam/)

---

## 🛠️ 02 — Cloud Support & Reliability Center

![Cloud Support](https://img.shields.io/badge/Cloud-Support-0078D4)
![Incidents](https://img.shields.io/badge/Resolved_Incidents-40-brightgreen)
![Runbooks](https://img.shields.io/badge/Runbooks-8-blue)
![Python](https://img.shields.io/badge/Python-Analytics-3776AB?logo=python\&logoColor=white)

**Operate, troubleshoot, restore, and improve cloud services.**

Simulates a cloud support queue covering AWS, Azure, GCP, IAM, networking, Linux, Microsoft 365, Terraform, monitoring, backup, security, and CI/CD.

### 🔑 Highlights

* 🎫 40 documented simulated incidents
* 📖 8 operational runbooks
* 🔍 Structured troubleshooting
* 🧩 Root-cause analysis
* 📞 Customer communication
* 📊 SLA tracking
* 🐍 Python ticket analytics
* 🔄 Recurring-incident analysis
* 🛡️ Preventive operational controls

📂 [`02-cloud-support-reliability-center/`](02-cloud-support-reliability-center/)

---

## 🛡️ 03 — Security Operations & Incident Response

![SOC](https://img.shields.io/badge/SOC-Operations-critical)
![Incident Response](https://img.shields.io/badge/Incident-Response-red)
![Python](https://img.shields.io/badge/Python-Detections-3776AB?logo=python\&logoColor=white)
![Detections](https://img.shields.io/badge/Detections-3-brightgreen)

**Detect, investigate, contain, and learn from security incidents.**

Models a simulated **SEV-2 cloud credential-compromise incident** from initial detection through containment, recovery, and post-incident improvement.

### 🔑 Highlights

* Credential-compromise investigation
* Synthetic security evidence
* Normalized incident timeline
* IOC register
* Incident-response playbook
* Post-incident report
* Lessons learned
* Blast-radius analysis
* Credential remediation
* Three Python detections:

  * 🔑 Credential compromise
  * 🌍 Impossible travel
  * 🔐 Password spray

📂 [`03-security-operations-incident-response/`](03-security-operations-incident-response/)

---

## 🤖 04 — CloudGuardian Security Auditor

![Python](https://img.shields.io/badge/Python-Security_Automation-3776AB?logo=python\&logoColor=white)
![Cloud Security](https://img.shields.io/badge/Cloud-Security-success)
![Automation](https://img.shields.io/badge/Security-Automation-blueviolet)
![Testing](https://img.shields.io/badge/Tests-Automated-brightgreen)

**Find cloud-security weaknesses before they become incidents.**

**CloudGuardian** is a Python-based security auditing tool that evaluates normalized cloud inventory against security controls and produces prioritized remediation reports.

### 🔑 Detects

* Missing MFA
* Dormant enabled accounts
* Stale access keys
* Wildcard permissions
* Public storage
* Internet-exposed SSH/RDP
* Missing ownership/environment metadata

### 📊 Outputs

* JSON
* CSV
* HTML
* Risk scoring
* Control summaries
* Remediation guidance

The project also demonstrates:

**Insecure Environment → Detection → Remediation → Re-Scan → Validated Improvement**

📂 [`04-cloudguardian-security-auditor/`](04-cloudguardian-security-auditor/)

---

## ♾️ 05 — DevSecOps Infrastructure Delivery

![Terraform](https://img.shields.io/badge/Terraform-IaC-844FBA?logo=terraform\&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-CI%2FCD-2088FF?logo=githubactions\&logoColor=white)
![Checkov](https://img.shields.io/badge/Checkov-Security-blue)
![TFLint](https://img.shields.io/badge/TFLint-Quality-blueviolet)
![Gitleaks](https://img.shields.io/badge/Gitleaks-Secrets-red)

**Move security into infrastructure delivery.**

Integrates infrastructure validation, security scanning, policy enforcement, automated testing, human review, change management, and rollback planning.

### 🔑 Highlights

* GitHub Actions CI/CD
* Terraform validation
* Terraform tests
* TFLint
* Checkov
* Gitleaks
* Python policy-as-code
* Blocking security gates
* Pull-request review
* Change-management evidence
* Release checklist
* Rollback planning

### 🚫 Policy Gate Blocks

* Public protected storage
* `0.0.0.0/0 → SSH/22`
* `0.0.0.0/0 → RDP/3389`
* Wildcard administrative permissions

📂 [`05-devsecops-infrastructure-delivery/`](05-devsecops-infrastructure-delivery/)

---

# 🔄 End-to-End Engineering Lifecycle

The five projects are intentionally connected.

```text
☁️ PROJECT 01
Build Secure Multi-Cloud Foundation
          │
          ▼
🛠️ PROJECT 02
Operate & Troubleshoot Services
          │
          ▼
🛡️ PROJECT 03
Detect & Respond to Threats
          │
          ▼
🤖 PROJECT 04
Automate Security Assessment
          │
          ▼
♾️ PROJECT 05
Prevent Unsafe Infrastructure Delivery
          │
          ▼
🔄 CONTINUOUS IMPROVEMENT
```

The portfolio therefore tells one engineering story:

> **Build it securely → Operate it reliably → Detect threats → Respond effectively → Automate security → Prevent recurrence.**

---

# ⚙️ Automated Validation

![Python](https://img.shields.io/badge/Python-Automation-3776AB?logo=python\&logoColor=white)
![Tests](https://img.shields.io/badge/Offline_Checks-10-brightgreen)
![CI](https://img.shields.io/badge/CI-GitHub_Actions-2088FF?logo=githubactions\&logoColor=white)

The repository includes a consolidated automation layer under:

```text
scripts/
```

The validation workflow brings multiple parts of the portfolio together.

### Automated Checks

1. 🔐 IAM access review
2. 🛡️ Cloud security baseline
3. 💰 Cost governance guardrails
4. 💾 Disaster-recovery readiness
5. 📊 Support ticket analytics
6. 🚨 Security detection suite
7. ♾️ DevSecOps policy gate
8. 🤖 CloudGuardian unit tests
9. 🧪 Automation control tests
10. 📋 Portfolio completeness validation

---

# 🚀 Quick Start

Install the lightweight development requirements:

```bash
python3 -m pip install -r requirements-dev.txt
```

Run the complete offline validation suite:

```bash
python3 scripts/automation/run_all.py
```

### 🍎 macOS / 🐧 Linux

```bash
bash scripts/run.sh
```

### 🪟 Windows PowerShell

```powershell
./scripts/run.ps1
```

---

# 🧰 Make Commands

```bash
make setup
make validate
make tests
make support
make detections
make cloudguardian
make policy
make terraform-static
make clean
```

These commands provide shorter entry points into common repository validation workflows.

---

# ♾️ CI/CD Security Pipeline

The repository-level workflow is located at:

```text
.github/workflows/ci.yml
```

The pipeline separates validation into two major paths.

### 🐍 Offline Controls

```text
IAM Review
    ↓
Security Baseline
    ↓
Cost Guardrails
    ↓
DR Readiness
    ↓
Support Analytics
    ↓
Security Detections
    ↓
Policy Gate
    ↓
CloudGuardian Tests
    ↓
Automation Tests
    ↓
Portfolio Validation
```

### 🏗️ Terraform Security

```text
terraform fmt
      ↓
terraform init -backend=false
      ↓
terraform validate
      ↓
terraform test
      ↓
TFLint
      ↓
Checkov
      ↓
Gitleaks
```

A failed control prevents the validation workflow from being treated as successful.

---

# 🛡️ Security Engineering Model

The platform uses multiple layers of security rather than relying on one tool.

| Layer                  | Example Controls                                       |
| ---------------------- | ------------------------------------------------------ |
| 🔐 **Identity**        | MFA, RBAC, least privilege, JML                        |
| 🌐 **Network**         | Private-first networking, restricted management access |
| 🏗️ **Infrastructure** | Terraform, validation, testing                         |
| 🔎 **Detection**       | Credential abuse, impossible travel, password spray    |
| 🚨 **Response**        | Containment, eradication, recovery                     |
| 🤖 **Automation**      | CloudGuardian, policy-as-code                          |
| ♾️ **DevSecOps**       | Checkov, TFLint, Gitleaks, CI gates                    |
| 📋 **Governance**      | Access reviews, change records, control mapping        |
| 💾 **Resilience**      | Backup, RTO/RPO, disaster recovery                     |
| 💰 **FinOps**          | Ownership tags, budgets, cost guardrails               |

---

# 📚 Engineering Documentation

The repository includes supporting documentation beyond the five technical projects.

### 🧠 Threat Modeling

`docs/THREAT-MODEL.md`

Covers:

* Assets
* Trust boundaries
* STRIDE
* MITRE ATT&CK mapping
* Abuse cases
* Security requirements
* Residual risk

### 💾 Disaster Recovery

`docs/DISASTER-RECOVERY.md`

Covers:

* RTO
* RPO
* Backup standards
* Recovery sequencing
* Disaster scenarios
* Recovery validation

### 💰 Cost Governance

`docs/COST-GOVERNANCE.md`

Covers:

* Resource ownership
* Required tags
* Budget thresholds
* Cost anomaly workflow
* Resource lifecycle
* Monthly FinOps review

### 🤖 Automation Controls

`docs/AUTOMATION-CONTROLS.md`

Maps executable controls to:

* Risk
* Evidence
* Automated response
* Operational response

### 🧭 Repository Guide

`docs/REPOSITORY-GUIDE.md`

Provides technical-review paths based on role.

---

# 👀 Recruiter / Hiring Manager Quick Review

### ⏱️ Have 2 minutes?

Start with:

**🤖 Project 04 — CloudGuardian Security Auditor**

Then review:

**🛠️ Project 02 — Cloud Support & Reliability Center**

These quickly demonstrate both **technical automation and practical operations**.

### ⏱️ Have 5 minutes?

Review:

1. 🤖 CloudGuardian
2. 🛠️ Cloud Support & Reliability
3. 🏗️ Terraform architecture
4. 🛡️ Security incident response
5. ♾️ DevSecOps pipeline

### ⏱️ Have 10 minutes?

Follow:

`docs/REPOSITORY-GUIDE.md`

for a complete technical review path.

---

# 🎯 Role Alignment

This platform demonstrates skills relevant to roles such as:

| Role                                  | Strongest Evidence         |
| ------------------------------------- | -------------------------- |
| ☁️ **Cloud Support Associate**        | Project 02 + Project 01    |
| 🛠️ **Cloud Operations Analyst**      | Project 02 + automation    |
| 🏗️ **Junior Cloud Engineer**         | Project 01 + Project 05    |
| 🖥️ **Systems / Cloud Administrator** | Project 01 + Project 02    |
| 🔐 **IAM Analyst**                    | Project 01 + CloudGuardian |
| 🛡️ **SOC Analyst**                   | Project 03                 |
| 🚨 **Security Operations Analyst**    | Project 03 + Project 04    |
| ☁️🛡️ **Cloud Security Analyst**      | Projects 01, 03, 04, 05    |
| ♾️ **Junior DevOps / DevSecOps**      | Projects 01 + 05           |

---

# 📊 Portfolio Evidence

| Capability       | Evidence                                      |
| ---------------- | --------------------------------------------- |
| ☁️ Multi-Cloud   | AWS + Azure + GCP architecture                |
| 🏗️ IaC          | Terraform root and reusable modules           |
| 🔐 IAM           | RBAC, JML, access review, least privilege     |
| 🛠️ Support      | 40 simulated resolved incidents               |
| 📖 Operations    | 8 reusable runbooks                           |
| 🚨 Detection     | 3 Python security detections                  |
| 🛡️ IR           | Timeline, IOC register, playbook, PIR         |
| 🤖 Automation    | CloudGuardian security auditor                |
| 🐍 Python        | Security, operations, analytics automation    |
| 🧪 Testing       | Unit, control, and Terraform test definitions |
| ♾️ DevSecOps     | CI/CD + security gates                        |
| 💾 Resilience    | DR and recovery planning                      |
| 💰 Governance    | FinOps and cost controls                      |
| 📚 Documentation | Architecture, runbooks, RCA, governance       |

---

# 💼 Interview Discussion

> **“I built the Cloud Security & Operations Platform as an integrated multi-cloud portfolio rather than a collection of unrelated labs. I started by designing a secure AWS, Azure, and GCP foundation with Terraform and IAM controls. I then built a simulated support center with 40 incident investigations and reusable runbooks, followed by a security-operations scenario with Python detections and a full credential-compromise response. I created CloudGuardian to automate cloud-security assessments, and then integrated infrastructure validation, security scanning, secret detection, policy-as-code, testing, and change controls into a DevSecOps workflow. The main goal was to demonstrate the full lifecycle: build cloud infrastructure securely, operate it reliably, investigate problems, automate repetitive controls, and move those controls earlier into delivery.”**

---

# 🧠 Engineering Principles

The platform follows several consistent principles:

* 🔐 **Least privilege over broad access**
* 🌐 **Private-first infrastructure over unnecessary exposure**
* 🔍 **Evidence before remediation**
* 🛠️ **Minimum safe change over uncontrolled troubleshooting**
* 🏗️ **Infrastructure as Code over unmanaged configuration**
* 🤖 **Automation over repetitive manual review**
* 🧪 **Testing over assumption**
* 🚦 **Blocking controls over ignorable warnings**
* 📋 **Documented decisions over undocumented changes**
* ↩️ **Recoverability over irreversible deployment**
* 🔄 **Continuous improvement over repeated incidents**

---

# 📂 Repository Structure

```text
cloud-security-operations-platform/
│
├── ☁️ 01-multi-cloud-foundation-iam/
│   ├── architecture/
│   ├── governance/
│   ├── runbooks/
│   ├── terraform/
│   └── validation/
│
├── 🛠️ 02-cloud-support-reliability-center/
│   ├── data/
│   ├── runbooks/
│   ├── scripts/
│   └── tickets/
│
├── 🛡️ 03-security-operations-incident-response/
│   ├── detections/
│   ├── evidence/
│   └── playbooks/
│
├── 🤖 04-cloudguardian-security-auditor/
│   ├── data/
│   ├── reports/
│   ├── src/
│   └── tests/
│
├── ♾️ 05-devsecops-infrastructure-delivery/
│   ├── changes/
│   ├── docs/
│   └── policy/
│
├── 📚 docs/
├── 🤖 scripts/
├── ⚙️ .github/workflows/
│
├── 📊 EXECUTIVE-CASE-STUDY.md
├── 🔐 SECURITY.md
├── 🤝 CONTRIBUTING.md
├── 📜 CHANGELOG.md
├── ⚙️ Makefile
└── 📄 README.md
```

---

# 🏆 Platform Outcome

The **Cloud Security & Operations Platform** demonstrates more than the ability to configure individual cloud services.

It demonstrates an operating model where:

* ☁️ Cloud infrastructure is designed systematically
* 🔐 Identity is treated as a security boundary
* 🏗️ Infrastructure is version controlled
* 🛠️ Incidents are investigated methodically
* 📊 Operational performance is measured
* 🚨 Security events are detected and investigated
* 🧾 Evidence is preserved
* 🤖 Repetitive security reviews are automated
* 🧪 Controls are tested
* 🚦 Unsafe changes can be blocked
* 👀 Human judgment remains part of high-impact decisions
* ↩️ Recovery is planned before failure
* 💰 Cost and ownership are governed
* 🔄 Incidents feed continuous improvement

The result is an integrated portfolio spanning:

**☁️ Cloud Engineering • 🔐 IAM • 🛠️ Cloud Operations • 🛡️ Cybersecurity • 🤖 Automation • ♾️ DevSecOps**

---

## 👨‍💻 Author

### Jamie Christian II

**Product & Technology | ☁️ Cloud & IT | 🔐 Cybersecurity | 📊 Data, BI & Business**

GitHub: **JamieChristian22**

---

## 📜 License

This project is available under the repository's included license.

---

# ⭐ Cloud Security & Operations Platform

![AWS](https://img.shields.io/badge/AWS-232F3E?logo=amazonwebservices\&logoColor=white)
![Azure](https://img.shields.io/badge/Azure-0078D4?logo=microsoftazure\&logoColor=white)
![GCP](https://img.shields.io/badge/GCP-4285F4?logo=googlecloud\&logoColor=white)
![Terraform](https://img.shields.io/badge/Terraform-844FBA?logo=terraform\&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?logo=python\&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?logo=githubactions\&logoColor=white)
![Cloud Security](https://img.shields.io/badge/Cloud-Security-success)
![DevSecOps](https://img.shields.io/badge/DevSecOps-Complete-brightgreen)

### **Build it. Secure it. Operate it. Detect it. Automate it. Improve it.**
