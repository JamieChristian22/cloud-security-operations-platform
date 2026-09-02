# ☁️ Project 01 — Multi-Cloud Foundation & IAM

![AWS](https://img.shields.io/badge/AWS-Cloud-232F3E?logo=amazonwebservices&logoColor=white)
![Microsoft Azure](https://img.shields.io/badge/Microsoft_Azure-Cloud-0078D4?logo=microsoftazure&logoColor=white)
![Google Cloud](https://img.shields.io/badge/Google_Cloud-Platform-4285F4?logo=googlecloud&logoColor=white)
![Terraform](https://img.shields.io/badge/Terraform-Infrastructure_as_Code-844FBA?logo=terraform&logoColor=white)
![IAM](https://img.shields.io/badge/IAM-Least_Privilege-success)
![Security](https://img.shields.io/badge/Security-Zero_Trust-blue)
![Status](https://img.shields.io/badge/Project-Complete-brightgreen)
![Portfolio](https://img.shields.io/badge/Portfolio-Job_Ready-success)

> **Secure multi-cloud foundation across AWS, Azure, and Google Cloud with Terraform, IAM, RBAC, Zero Trust principles, network security, access governance, and infrastructure change control.**

---

## 🎯 Overview

This project designs a production-inspired multi-cloud foundation for **Northstar Digital Services**, a simulated 750-user organization operating across **AWS, Microsoft Azure, and Google Cloud Platform**.

The objective is to establish a secure cloud landing-zone foundation before application workloads are deployed. The design focuses on:

- 🔐 Identity governance
- 🪪 Role-Based Access Control (RBAC)
- 🛡️ Least-privilege access
- 🌐 Network segmentation
- 🏗️ Infrastructure as Code
- 📊 Security logging
- 🔄 Identity lifecycle management
- 📋 Operational governance

Rather than treating AWS, Azure, and GCP as isolated environments, this project applies a **consistent security and operations model across all three cloud providers**.

> ⚠️ **Environment Notice:** Northstar Digital Services and all organizational metrics in this repository are simulated for portfolio/lab purposes. This project demonstrates architecture, automation, security, and operational practices and does not represent a production employer environment.

---

## 🏢 Business Scenario

Northstar Digital Services is expanding its cloud footprint across AWS, Azure, and GCP.

Without a standardized cloud foundation, the organization faces several risks:

- 🚨 Excessive user privileges
- 🔓 Inconsistent IAM policies
- 👤 Direct user permissions
- ⚠️ Uncontrolled administrative access
- 🌍 Public management exposure
- 🏷️ Missing ownership metadata
- 📋 Weak access-review processes
- 📊 Inconsistent security logging
- 🔄 Configuration drift
- 🏗️ Unreviewed infrastructure changes

The Cloud Operations and Security teams require a standardized foundation that allows teams to operate cloud resources without granting unnecessary administrative privileges.

---

## 🎯 Project Objectives

This project establishes:

1. ☁️ **Multi-cloud infrastructure foundations**
2. 🔐 **Role-based access control**
3. 🛡️ **Least-privilege IAM**
4. 👑 **Privileged-access separation**
5. 🔑 **MFA requirements**
6. 🌐 **Private-first networking**
7. 🏗️ **Infrastructure-as-Code standards**
8. 📊 **Central security and administrative logging**
9. 🏷️ **Resource ownership and environment tagging**
10. 👥 **Joiner-Mover-Leaver identity processes**
11. 🔍 **Quarterly access certification**
12. 🔀 **Git-based infrastructure change control**
13. ✅ **Pre-deployment security validation**

---

# 🏗️ Architecture

The target environment spans three major cloud platforms.

### 🟠 AWS

- 🌐 VPC architecture
- 🔒 Private subnet strategy
- 👤 IAM roles and policies
- 🧱 Security groups
- 📊 Audit logging
- 🗄️ Secure storage controls
- 🏗️ Terraform-managed infrastructure

### 🔵 Microsoft Azure

- 🌐 Virtual Network architecture
- 🛡️ Network Security Groups
- 🪪 Microsoft Entra ID role separation
- 📦 Resource Group access boundaries
- 📊 Security monitoring
- 🏗️ Terraform-managed infrastructure

### 🔴🟡🟢 Google Cloud Platform

- 🌐 VPC architecture
- 🧱 Firewall policies
- 👤 Project-level IAM
- 🔐 Scoped operational roles
- 📊 Security logging
- 🏗️ Terraform-managed infrastructure

The architecture follows a **private-first design**.

Administrative services are not intentionally exposed directly to the public Internet. Access is controlled through **identity, network boundaries, scoped permissions, and approved operational workflows**.

📖 **Architecture documentation:**  
`architecture/multi-cloud-design.md`

---

# 🔐 Identity & Access Management

IAM is treated as a **security boundary**, not simply an administrative feature.

### Core IAM Principles

- 🛡️ Least privilege
- 👥 Role-based access
- ⚖️ Separation of duties
- 🔑 MFA enforcement
- 👑 Privileged identity separation
- 🚫 No routine direct user permissions
- 🔍 Periodic access certification
- 🔄 Documented identity lifecycle management

---

## 👥 Role Model

| Persona | AWS | Azure | GCP | 🔒 Primary Guardrail |
|---|---|---|---|---|
| 🎧 Help Desk | Identity read + approved reset workflow | Helpdesk Administrator | Viewer | No infrastructure write |
| ☁️ Cloud Operations | Scoped operations role | Contributor on operations RG | Compute operator | No organization-wide IAM administration |
| 🛡️ Security Analyst | Security audit/read | Security Reader | Security reviewer | Investigation/read access |
| 🔑 IAM Administrator | Scoped identity administration | Privileged Role Administrator | Scoped IAM administration | Separate privileged identity |
| 💻 Developer | Application-specific role | Application RG Contributor | Project Developer | No production IAM administration |

This prevents one normal operational identity from silently controlling the entire cloud environment.

---

# ⚖️ Separation of Duties

The design intentionally separates operational responsibilities.

### ☁️ Cloud Operations

**Can:**

- ⚙️ Operate workloads
- 🔎 Investigate infrastructure failures
- ♻️ Restart/recover approved services
- 📊 Review operational telemetry

**Cannot routinely:**

- 🚫 Modify organization-wide IAM
- 🚫 Grant privileged roles
- 🚫 Override security governance

### 🔑 IAM Administrators

**Can:**

- 👥 Manage approved identity workflows
- 🔐 Assign scoped roles
- 🔄 Perform access lifecycle operations

Privileged accounts are not intended for routine daily activity.

### 🛡️ Security Analysts

**Can:**

- 🚨 Investigate alerts
- 📊 Review security telemetry
- 🔍 Audit configurations
- 👤 Review IAM activity

Their standard investigation role does not provide unrestricted infrastructure administration.

### 💻 Developers

Developers receive **application-scoped permissions** without production-wide IAM authority.

---

# 🔄 Joiner-Mover-Leaver Lifecycle

Identity access follows a documented lifecycle.

### 🟢 Joiner

1. 📝 Manager submits approved access request.
2. 👤 User identity is provisioned.
3. 🔑 MFA enrollment is required.
4. 👥 User is assigned approved groups.
5. 🔐 Role membership determines cloud access.
6. 👑 Privileged access requires separate authorization.
7. 📋 Provisioning evidence is recorded.

### 🟡 Mover

1. 🔍 Existing access is reviewed.
2. 🗑️ Unnecessary permissions are removed.
3. 🆕 New role access is approved.
4. 👑 Privileged access is independently reviewed.
5. 📋 Access records are updated.

### 🔴 Leaver

1. 🚫 Sign-in access is disabled.
2. 🔌 Active sessions are revoked.
3. ☁️ Cloud role assignments are removed.
4. 🔑 Credentials and keys are invalidated.
5. 👥 Group memberships are removed.
6. 📦 Owned resources are transferred.
7. ✅ Completion is documented.

📖 **Runbook:** `runbooks/joiner-mover-leaver.md`

---

# 🔍 Access Reviews

Quarterly access reviews validate whether users still require their assigned privileges.

Reviews evaluate:

- 👑 Privileged roles
- 💤 Dormant accounts
- ⏳ Stale access
- ⚠️ Excessive permissions
- 🔄 Role changes
- 👥 Unnecessary group memberships
- ⚖️ Separation-of-duty conflicts

### Review Outcomes

`✅ Approved` → `🔧 Modified` → `❌ Removed` → `🚨 Escalated`

📖 **Documentation:** `governance/access-review.md`

---

# 🏗️ Infrastructure as Code

![Terraform](https://img.shields.io/badge/Terraform-IaC-844FBA?logo=terraform&logoColor=white)
![TFLint](https://img.shields.io/badge/TFLint-Validation-blueviolet)
![Checkov](https://img.shields.io/badge/Checkov-Security_Scanning-blue)
![Gitleaks](https://img.shields.io/badge/Gitleaks-Secret_Scanning-red)

Terraform defines cloud infrastructure consistently across AWS, Azure, and GCP.

### IaC provides:

- ♻️ Repeatability
- 🔀 Version control
- 👀 Peer review
- 📐 Configuration consistency
- 🔐 Security validation
- 📜 Change history
- ↩️ Rollback support
- 🤖 Reduced manual configuration

### 🔄 Infrastructure Delivery Workflow

`Developer Change`

⬇️

`Git Branch`

⬇️

`Pull Request`

⬇️

`terraform fmt`

⬇️

`terraform validate`

⬇️

`TFLint + Checkov + Gitleaks`

⬇️

`terraform plan`

⬇️

`Peer Review`

⬇️

`Approved Deployment`

This reduces uncontrolled console-based infrastructure changes.

---

# 🌐 Network Security

The network design follows a **deny-by-default / private-first philosophy**.

Controls include:

- 🧩 Segmented cloud networks
- 🔒 Restricted management access
- 🧱 Scoped AWS security groups
- 🛡️ Azure NSGs
- 🔥 GCP firewall rules
- ⬇️ Controlled ingress
- ⬆️ Controlled egress
- 🚫 No broad public administrative access
- 📊 Security-relevant activity logging

**Goal:** minimize attack surface while maintaining operational capability.

---

# 📊 Logging & Auditability

Security and administrative logging are incorporated directly into the architecture.

### Important Events

- 🔐 Authentication activity
- 👤 IAM changes
- 👑 Privilege assignments
- 🏗️ Infrastructure changes
- 🌐 Network-security changes
- ⚙️ Administrative actions
- ❌ Failed access attempts

### Logs Support

- 🚨 Security investigations
- 🔎 Root-cause analysis
- 👥 Access reviews
- 🛡️ Incident response
- 📋 Governance validation

---

# 🏷️ Resource Governance

Cloud resources require ownership and environment metadata.

### Example Classification

| Tag | Purpose |
|---|---|
| `environment` | Development, staging, or production classification |
| `owner` | Responsible team or service owner |
| `application` | Associated workload |
| `cost-center` | Cost attribution |
| `managed-by` | IaC/automation ownership |

This improves **resource accountability, cost attribution, incident ownership, automation, inventory management, and governance**.

---

# ✅ Security Validation

Before infrastructure changes are considered ready, validation checks review:

### 🔐 Identity

- MFA expectations
- Privileged access
- Role scope
- Direct permission usage

### 🌐 Networking

- Public exposure
- Management ports
- Firewall scope
- Security-group configuration

### 🏗️ Infrastructure

- Required metadata
- Encryption expectations
- Logging
- Terraform validation

### 📋 Governance

- Ownership
- Change approval
- Access boundaries

📖 **Checklist:** `validation/security-checklist.md`

---

# 📚 Governance Artifacts

| Artifact | Purpose |
|---|---|
| 📊 `governance/rbac-matrix.csv` | Maps personas to approved cloud entitlements |
| 🔍 `governance/access-review.md` | Defines quarterly access certification |
| 🛡️ `governance/control-mapping.md` | Maps control objectives to technical evidence |
| 🔄 `runbooks/joiner-mover-leaver.md` | Documents identity lifecycle operations |
| ✅ `validation/security-checklist.md` | Provides pre-deployment security validation |
| 🏗️ `architecture/multi-cloud-design.md` | Documents architecture and design decisions |

---

# 🧠 Key Security Decisions

### 🔐 1. No Routine Direct Permissions

Access flows through approved groups and roles.

**Why?** Direct permissions become difficult to audit and remove as environments grow.

### 👑 2. Separate Privileged Identities

Administrative access is separated from normal daily activity.

**Why?** Compromising a standard workforce identity should not automatically provide privileged administrative access.

### 🚫 3. Production Write Restrictions

Production modification rights are limited to approved operational roles.

**Why?** This reduces accidental and unauthorized production changes.

### 🌐 4. Private-First Networking

Management services are not broadly exposed to the Internet.

**Why?** Reducing public attack surface lowers infrastructure risk.

### 🔀 5. Git-Reviewed Infrastructure

Infrastructure modifications are version controlled and reviewed.

**Why?** This creates traceability and reduces uncontrolled configuration changes.

---

# 🧰 Skills Demonstrated

![AWS](https://img.shields.io/badge/AWS-232F3E?logo=amazonwebservices&logoColor=white)
![Azure](https://img.shields.io/badge/Azure-0078D4?logo=microsoftazure&logoColor=white)
![GCP](https://img.shields.io/badge/GCP-4285F4?logo=googlecloud&logoColor=white)
![Terraform](https://img.shields.io/badge/Terraform-844FBA?logo=terraform&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?logo=githubactions&logoColor=white)
![Security](https://img.shields.io/badge/Cloud-Security-success)
![IAM](https://img.shields.io/badge/Identity-IAM-blue)
![Zero Trust](https://img.shields.io/badge/Security-Zero_Trust-critical)

### ☁️ Cloud
AWS • Microsoft Azure • Google Cloud Platform • Multi-Cloud Architecture

### 🏗️ Infrastructure
Terraform • Infrastructure as Code • Virtual Networking • Security Groups • NSGs • Firewall Policies

### 🔐 Identity
IAM • Microsoft Entra ID Concepts • RBAC • Least Privilege • MFA • Privileged Access • JML • Access Certification

### 🛡️ Security
Zero Trust Principles • Attack-Surface Reduction • Security Logging • Access Governance • Separation of Duties

### ⚙️ Operations
Git-Based Change Management • Security Validation • Operational Runbooks • Resource Governance • Auditability

---

# ⚖️ Key Engineering Tradeoff

The central design challenge was balancing:

> **Operational capability ↔ Controlled privilege**

Cloud Operations needs enough access to recover workloads.

IAM administrators need enough authority to manage identities.

Security analysts need enough visibility to investigate threats.

Developers need enough access to deliver applications.

Granting all capabilities to one broad administrator role would significantly increase the potential blast radius.

The resulting model intentionally distributes responsibility across scoped roles.

### Result

- 🛡️ Stronger security
- 🔍 Better auditability
- 👤 Clear accountability
- 🔐 Easier access reviews
- 🚨 Better incident investigation
- 👑 Reduced privileged-access exposure

---

# 💼 Interview Discussion

> **“I designed a multi-cloud foundation for a simulated 750-user organization across AWS, Azure, and GCP. I focused on establishing consistent IAM and infrastructure guardrails before workloads were deployed. I separated Cloud Operations, Security, IAM administration, Help Desk, and Developer responsibilities, applied least-privilege principles, documented identity lifecycle and access-review processes, and used Terraform with Git-based change control to make infrastructure changes repeatable and auditable. The main design tradeoff was providing operational teams enough access to recover services without creating broad administrator roles that increased blast radius.”**

---

# 📂 Repository Structure

```text
01-multi-cloud-foundation-iam/
├── 🏗️ architecture/
│   └── multi-cloud-design.md
├── 📋 governance/
│   ├── access-review.md
│   ├── control-mapping.md
│   └── rbac-matrix.csv
├── 📖 runbooks/
│   └── joiner-mover-leaver.md
├── 🏗️ terraform/
│   └── multi-cloud infrastructure definitions
├── ✅ validation/
│   └── security-checklist.md
└── 📄 README.md
