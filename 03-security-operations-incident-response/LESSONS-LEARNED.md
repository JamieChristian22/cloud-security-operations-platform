# Lessons from the synthetic incident

1. Detection output is a lead. Discovery API correlation alone cannot prove credential theft.
2. Match the incident narrative to the actual event IDs and dates; separate independent fixtures.
3. A denied follow-up call does not prove key revocation without the corresponding control evidence.
4. Preserve source coverage limitations when discussing data loss or exfiltration.
5. Test credential replacement and old-key denial separately.
6. Convert the failure mode into a regression test and a delivery or identity control.

The upgrade applies these lessons by aligning the timeline and incident report with the supplied API records and adding deterministic detection tests.
