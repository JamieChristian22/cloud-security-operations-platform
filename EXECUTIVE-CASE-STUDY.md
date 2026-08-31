# Executive Case Study — Northstar Digital Services

## Situation
Northstar Digital Services is a fictional 750-user SaaS company with a remote workforce and services distributed across AWS, Azure/Microsoft 365, and Google Cloud. Growth created five operational risks: inconsistent identity access, recurring support incidents, weak incident-response repeatability, limited automated security review, and infrastructure changes that could bypass engineering controls.

## Objective
Create a cohesive cloud operations and security operating model that demonstrates how a small technical team could standardize access, improve troubleshooting, detect identity threats, automate configuration review, and control infrastructure changes.

## Approach
The portfolio separates the problem into five connected projects. Project 01 establishes cloud and IAM foundations. Project 02 formalizes support and RCA. Project 03 handles detection and incident response. Project 04 automates security assessment with CloudGuardian. Project 05 places security and quality gates around Terraform delivery.

## Operational Outcomes in the Lab
The support dataset contains 40 resolved simulated incidents and allows KPI calculation directly from source data. Security detections identify the planted credential-compromise, impossible-travel, and password-spray scenarios. CloudGuardian reports eight intentional findings in the insecure sample environment and zero in the remediated sample. The IaC workflow adds automated checks before infrastructure changes are considered deployable.

## Risk Reduction Logic
The design reduces standing privilege through role-based access, reduces configuration drift through Terraform and documented state practices, reduces repeat incidents through runbooks and RCA, reduces identity-threat dwell time through detections and playbooks, and reduces insecure deployment risk through automated CI security gates.

## Limitations
This is a lab portfolio, not a claim of production operations. The company, users, events, tickets, and impact are simulated. Cloud-provider credentials and Terraform state are intentionally absent. The portfolio demonstrates engineering process, technical reasoning, code, and documentation using inspectable artifacts.
