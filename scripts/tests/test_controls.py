import json, importlib.util
from pathlib import Path
ROOT=Path(__file__).parents[1]
def load(rel,name):
    spec=importlib.util.spec_from_file_location(name,ROOT/rel); m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m

def test_iam_review_detects_mfa_and_stale_key():
    m=load("iam/access_review.py","iam"); users=json.loads((ROOT/"sample_data/iam_users.json").read_text()); f=m.review(users); assert any(x["control"]=="MFA" for x in f); assert any(x["control"]=="Credential age" for x in f)
def test_security_baseline_detects_public_resource():
    m=load("security/baseline_audit.py","baseline"); r=json.loads((ROOT/"sample_data/resources.json").read_text()); f=m.audit(r); assert any(x["control"]=="Public exposure" for x in f)
def test_finops_total_under_budget():
    m=load("finops/cost_guardrails.py","finops"); r=json.loads((ROOT/"sample_data/resources.json").read_text()); x=m.evaluate(r,400); assert x["status"]=="OK"; assert x["monthly_estimate"]>0
def test_dr_critical_services_have_backups():
    m=load("dr/readiness_check.py","dr"); a=json.loads((ROOT/"sample_data/dr_assets.json").read_text()); x=m.check(a); assert not any(f["severity"]=="CRITICAL" and f["service"] in {"identity-platform","security-log-archive"} for f in x["findings"])
