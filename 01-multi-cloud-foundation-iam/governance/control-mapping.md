# Control Mapping

This mapping explains how the lab design translates security principles into technical and operational evidence.

| Control objective | Lab implementation | Evidence |
|---|---|---|
| Strong authentication | MFA required for workforce identities | RBAC matrix + validation checklist |
| Least privilege | Group/role based permissions; no routine direct user grants | `governance/rbac-matrix.csv` |
| Privileged separation | Dedicated admin personas separated from cloud operations | Project README role model |
| Joiner/Mover/Leaver governance | Approval, group mapping, access removal, validation | `runbooks/joiner-mover-leaver.md` |
| Periodic recertification | Quarterly reviewer/owner/exception process | `governance/access-review.md` |
| Network exposure reduction | No direct public SSH/RDP; segmented workloads | Terraform + security checklist |
| Auditability | Central log destination and Git-reviewed changes | architecture + CI/CD project |
| Ownership | Required Environment/Owner tags | Terraform locals + CloudGuardian |
