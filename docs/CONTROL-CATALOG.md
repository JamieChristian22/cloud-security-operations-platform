# Security control catalog

| ID | Control and threshold | Severity | Evidence | Response and verification |
|---|---|---|---|---|
| CG-001 | Enabled workforce user lacks MFA | High | enabled=true, mfa=false | Validate identity owner, enroll approved MFA, confirm sign-in policy and retest |
| CG-002 | Enabled account inactive ≥45 days | Medium; High if privileged | days_inactive, privileged | Confirm business need, remove unneeded access; verify access review record |
| CG-003 | Active key older than 90 days | High | age_days, active | Identify workload, rotate safely, revoke old key, verify service continuity |
| CG-004 | Allowed action contains * or ? | Critical for *, High for partial wildcard | normalized actions | Derive required actions/resources from workload evidence and test allow/deny paths |
| CG-005 | Storage marked public | Critical | effective public flag | Block public access; verify approved consumers still work; exception requires owner and expiry |
| CG-006 | World CIDR reaches SSH/RDP within a TCP/all range | Critical | source and inclusive ports | Remove exposure; validate approved private admin path and denied outside path |
| CG-007 | Owner or Environment absent/blank | Low | tags | Identify owner; populate metadata; rerun allocation report |
| CG-008 | Storage encryption disabled | High | encrypted=false | Enable effective encryption, validate key policy and read/write behavior |

## Governance interpretation

These controls support identity/access, data protection, monitoring and configuration-management objectives. Mapping is educational and does not demonstrate conformance with any entire CIS benchmark or NIST framework. Avoid claiming certification from a passed scan.

## Severity and scoring

Weights: Critical=25, High=15, Medium=7, Low=2. Open risk is the sum capped at 100. Counts and individual evidence are more useful than the capped score when environments differ in size. Accepted risk stays visible but does not contribute to the open score. Unknown input is a validation error, not a low-risk result.

## Review ownership

Cloud operations owns inventory accuracy; security owns control logic and exceptions; service owners validate business impact; release reviewers approve infrastructure changes. In this solo portfolio these are simulated responsibilities, not invented employees or sign-offs.

## False positives and scope

A public website asset bucket may be intentional. A service-wide read action may be approved for an auditor. A private source may still be unsafe in an untrusted connected network. Review findings with network paths, data classification and identity context. Record the decision and expiration rather than deleting evidence.
