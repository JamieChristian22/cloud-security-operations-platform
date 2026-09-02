# Indicator / Evidence Register

All values are synthetic and reserved for documentation examples.

| Type | Value | Why it mattered | Disposition |
|---|---|---|---|
| Source IP | `203.0.113.77` | New source associated with discovery burst | blocked in lab logic / retained as evidence |
| Identity | `dev-lab` | Owner of simulated leaked key | key disabled; permissions reviewed |
| Actions | `ListBuckets`, `ListRoles` | Discovery pattern inconsistent with normal workflow | detection condition |
| Time window | 14:08–14:10 UTC | Burst shortly after simulated disclosure | used for timeline correlation |

`203.0.113.0/24` is documentation address space; no claim is made about a real attacker.
