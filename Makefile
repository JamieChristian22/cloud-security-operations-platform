PYTHON ?= python3
TF_ROOT = 01-multi-cloud-foundation-iam/terraform
.PHONY: setup validate tests support detections cloudguardian policy terraform-static clean
setup:
	$(PYTHON) -m pip install -r requirements-dev.txt
validate:
	$(PYTHON) scripts/automation/run_all.py
tests:
	$(PYTHON) -m pytest -q
support:
	$(PYTHON) scripts/operations/ticket_metrics.py --input 02-cloud-support-reliability-center/data/tickets.csv --output scripts/reports/support_metrics.json
detections:
	$(PYTHON) scripts/security/run_detections.py --repo . --output scripts/reports/detection_results.json
cloudguardian:
	$(PYTHON) 04-cloudguardian-security-auditor/src/cloudguardian.py --input 04-cloudguardian-security-auditor/sample_data/environment.json --out 04-cloudguardian-security-auditor/reports/generated
policy:
	$(PYTHON) 05-devsecops-infrastructure-delivery/policy/policy_check.py 05-devsecops-infrastructure-delivery/policy/sample_proposed_change.json
terraform-static:
	terraform -chdir=$(TF_ROOT) fmt -check -recursive
	terraform -chdir=$(TF_ROOT) init -backend=false -input=false
	terraform -chdir=$(TF_ROOT) validate
	terraform -chdir=$(TF_ROOT) test
clean:
	$(PYTHON) scripts/automation/clean.py
