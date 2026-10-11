import csv,json,subprocess,sys
from pathlib import Path
import pytest
ROOT=Path(__file__).resolve().parents[1]
CLI=ROOT/'04-cloudguardian-security-auditor/src/cloudguardian.py'
SAMPLE=ROOT/'04-cloudguardian-security-auditor/sample_data'

def run(tmp_path,data,threshold='high'):
 p=tmp_path/'input.json';p.write_text(json.dumps(data))
 proc=subprocess.run([sys.executable,str(CLI),'--input',str(p),'--out',str(tmp_path/'report'),'--fail-on',threshold],text=True,capture_output=True)
 return proc

@pytest.mark.parametrize('name,code',[('environment.json',1),('environment-remediated.json',0)])
def test_fixture_gate(tmp_path,name,code):
 result=run(tmp_path,json.loads((SAMPLE/name).read_text()))
 assert result.returncode==code,result.stderr
 report=json.loads((tmp_path/'report/report.json').read_text())
 assert report['schema_version']=='2.0'

def test_bad_inventory_exit_code(tmp_path):
 assert run(tmp_path,{}).returncode==2
 assert not (tmp_path/'report/report.json').exists()

def test_report_escapes_html_and_csv(tmp_path):
 data={k:[] for k in ('users','keys','policies','storage','firewall_rules','resources')}
 data['storage']=[dict(name='=HYPERLINK("x")<script>alert(1)</script>',public=True,encrypted=True)]
 assert run(tmp_path,data).returncode==1
 html=(tmp_path/'report/report.html').read_text()
 assert '<script>' not in html and '&lt;script&gt;' in html
 with (tmp_path/'report/report.csv').open() as f:row=next(csv.DictReader(f))
 assert row['resource'].startswith("'=")

def test_normalized_policy_rejects_malformed(tmp_path):
 p=tmp_path/'bad.json';p.write_text('{}')
 proc=subprocess.run([sys.executable,str(ROOT/'05-devsecops-infrastructure-delivery/policy/policy_check.py'),str(p)],capture_output=True,text=True)
 assert proc.returncode==2

def test_collector_snapshot_end_to_end(tmp_path):
 out=tmp_path/'inventory.json'
 proc=subprocess.run([sys.executable,str(ROOT/'scripts/collectors/aws_security_groups.py'),'--snapshot',str(ROOT/'scripts/sample_data/aws_security_groups.json'),'--output',str(out)],capture_output=True,text=True)
 assert proc.returncode==0,proc.stderr
 data=json.loads(out.read_text());assert 'IAM' in data['metadata']['not_collected']
 assert run(tmp_path,data).returncode==1
