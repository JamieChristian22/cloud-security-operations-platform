# Operations and incident-record standard

Each case must distinguish observations from hypotheses. A command listed without output is a suggested procedure, not execution evidence. Synthetic examples must be labeled at the top of the case.

## Required record

1. Scope: affected service, environment, user path, start time and business impact.
2. Triage: severity, owner, escalation trigger and immediate safe containment.
3. Hypotheses: competing causes and one discriminating test for each.
4. Evidence: UTC timestamp, source, exact error, sanitized command/output and collection context.
5. Decision: why the chosen cause explains observations and alternatives do not.
6. Change: minimum approved correction, blast radius, owner and rollback trigger.
7. Verification: positive user-path test, negative security test and monitoring observation.
8. Closure: user communication, follow-up control, owner and acceptance criterion.

## Severity example

P1: widespread critical unavailability or active high-impact compromise; immediate escalation.
P2: material degradation, limited critical impact or credible security incident.
P3: localized issue with workaround and no active security impact.
P4: planned hygiene, request or improvement.

These are lab definitions. Actual severity and SLA depend on organizational contracts. Do not infer SLA compliance solely from resolution hours when timestamps, business calendars and priority policies are absent.

## Evidence handling

Use UTC timestamps, original event IDs and hashes of exported files. Preserve originals read-only and redact copies for public sharing. Record collector, source system, time, hash and transformation. Do not publish live access keys, tokens, customer data, private account IDs or sensitive network details.

## Communications

Initial: describe observed impact, ownership and next update time. Update: explain what is known, current mitigation and uncertainty. Closure: describe restored behavior, verification and follow-up without disclosing exploitable internal details. All communication examples in this portfolio are drafts, not messages sent to customers.
