import importlib.util
from pathlib import Path
MODULE=Path(__file__).resolve().parents[1]/'src'/'cloudguardian.py'
spec=importlib.util.spec_from_file_location('cloudguardian',MODULE); cg=importlib.util.module_from_spec(spec); spec.loader.exec_module(cg)
def base(): return {'users':[],'keys':[],'policies':[],'storage':[],'firewall_rules':[],'resources':[]}
def test_clean_environment_has_no_findings(): assert cg.scan(base()) == []
def test_missing_mfa_is_high():
 d=base(); d['users']=[{'name':'u','enabled':True,'mfa':False,'days_inactive':0}]
 assert cg.scan(d)[0]['severity']=='High'
def test_public_storage_is_critical():
 d=base(); d['storage']=[{'name':'b','public':True}]
 assert cg.scan(d)[0]['severity']=='Critical'
def test_public_ssh_is_critical():
 d=base(); d['firewall_rules']=[{'name':'ssh','source':'0.0.0.0/0','port':22}]
 assert cg.scan(d)[0]['control']=='Management exposure'
def test_wildcard_policy_is_critical():
 d=base(); d['policies']=[{'name':'admin','actions':['*']}]
 assert cg.scan(d)[0]['severity']=='Critical'
def test_risk_score_is_capped(tmp_path):
 d=base(); d['storage']=[{'name':str(i),'public':True} for i in range(6)]
 fs=cg.scan(d); assert cg.write_reports(fs,tmp_path)==100
