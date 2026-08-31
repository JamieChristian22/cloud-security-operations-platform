# Multi-Cloud Foundation Design

## Account / Subscription / Project Strategy
- **AWS:** separate conceptual accounts for shared services, security/logging, development, and production.
- **Azure:** management-group style separation with dedicated subscriptions/resource groups by workload and environment.
- **GCP:** organization/folder/project hierarchy separating shared security services from application projects.

## Identity Strategy
The workforce authenticates through a centralized identity provider. Long-lived local cloud users are avoided for normal human access. Group membership maps users to cloud roles; privileged operations require separate administrative roles and stronger approval/monitoring.

## Network Strategy
Application workloads use private subnets where practical. Internet-facing services terminate at approved load-balancing/reverse-proxy layers. Management ports are not broadly exposed. Flow/activity logs support troubleshooting and security review.

## Logging Strategy
Administrative activity, authentication events, network telemetry, and high-value workload events are forwarded to a centralized conceptual security/operations logging plane. Detection logic in Project 03 consumes normalized event data representing that telemetry.

## Failure Domains
A cloud provider outage should not automatically imply total identity or business failure. The design separates identity, workload, logging, and deployment concerns so that incidents can be isolated and recovered using documented runbooks.
