# Ten-minute reproducible demonstration

## 1. Establish the evidence boundary (one minute)

Explain that this is a synthetic lab with executable tools. Show the evidence statement and source revision. State that Terraform tests are mocked and cloud acceptance is a separate step.

## 2. Reproduce validation (two minutes)

```bash
python scripts/automation/run_all.py
python -m pytest -q
```

Open the suite report and identify the deliberately insecure fixture findings. Test success means the controls detected expected conditions.

## 3. Assess and remediate (three minutes)

```bash
python 04-cloudguardian-security-auditor/src/cloudguardian.py --input 04-cloudguardian-security-auditor/sample_data/environment.json --out reports/local/before --fail-on high
python 04-cloudguardian-security-auditor/src/cloudguardian.py --input 04-cloudguardian-security-auditor/sample_data/environment-remediated.json --out reports/local/after --fail-on high
```

The first command is expected to exit 1. The second should exit 0. Compare JSON/HTML findings and discuss the specific changes. These are paired fixture snapshots; no live resources were changed by this demonstration.

## 4. Explain one detection (two minutes)

```bash
python 03-security-operations-incident-response/detections/password_spray.py --assert-alert
```

Point to source IP, distinct users, event IDs and the later success. Explain why an earlier success or a different user does not escalate the alert. Show the tests for those cases.

## 5. Connect to operations (two minutes)

Open `02-cloud-support-reliability-center/case-studies/01-iam-access-denied.md`. Walk through hypothesis, decisive evidence, scoped correction, positive/negative retest and the preventive control. Then show where CI would catch the same class of mistake.

## Optional collector demonstration

```bash
python scripts/collectors/aws_security_groups.py --snapshot scripts/sample_data/aws_security_groups.json --output reports/local/aws-inventory.json
python 04-cloudguardian-security-auditor/src/cloudguardian.py --input reports/local/aws-inventory.json --out reports/local/aws-audit
```

Explain why empty IAM/S3 arrays in this collector output mean uncollected scope, not a clean identity or storage environment.
