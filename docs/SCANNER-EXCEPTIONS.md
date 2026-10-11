# Static scanner exceptions

These are explicit, resource-scoped **lab design decisions**, not production risk approvals. They remain visible as skipped checks in Checkov output. Review every exception before live deployment and replace it with the required control or a formally approved risk record. No benchmark compliance is claimed.

| Reference | Check | Reason and acceptance condition |
|---|---|---|
| LAB-001 | CKV_AWS_252 | CloudWatch log integration is the demonstrated path; SNS fanout is an environment-specific integration. |
| LAB-002 | CKV2_AWS_5 | reusable foundation has no workload instances; attach the group during workload deployment. |
| LAB-003 | CKV2_AWS_62 | event-driven object processing is outside this audit archive lab; live delivery monitoring is required. |
| LAB-004 | CKV_AWS_18 | separate S3 server-access logging destination is deferred; live access-monitoring design is an acceptance requirement. |
| LAB-005 | CKV_AWS_144 | cross-region replication is an explicit DR design decision with cost and key-policy implications. |
| LAB-006 | CKV_GCP_62 | separate bucket usage/access-log destination is deferred; project data-access audit logging is configured. |
| LAB-007 | CKV2_GCP_4 | retention configured but irreversible Bucket Lock intentionally requires separate owner approval. |

Owner role: repository maintainer. Review trigger: any deployment, architectural change or quarterly portfolio review. The owner role is a responsibility designation, not evidence of organizational sign-off. No global soft-fail is used. New unexcepted failures block the configured scan.

Production acceptance must address event delivery/alerting, archive access monitoring, approved replication strategy and retention immutability. A single-region lab cannot substantiate regional disaster recovery. The standalone workload security group must be attached and its effective reachability tested when a workload is added.
