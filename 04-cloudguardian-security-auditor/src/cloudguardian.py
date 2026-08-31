import argparse, json, csv, html
from collections import Counter
from pathlib import Path
WEIGHTS={'Critical':25,'High':15,'Medium':7,'Low':2}
CONTROL_MAP={
 'MFA':['CIS identity hygiene','NIST PR.AA'],
 'Dormant account':['CIS identity hygiene','NIST PR.AA'],
 'Credential age':['CIS credential management','NIST PR.AA'],
 'Least privilege':['CIS access control','NIST PR.AA'],
 'Public storage':['CIS data protection','NIST PR.DS'],
 'Management exposure':['CIS network security','NIST PR.IR'],
 'Tagging':['Operational governance']
}
def finding(sev,control,res,evidence,remediation,provider='multi-cloud'):
 return {'severity':sev,'control':control,'provider':provider,'resource':res,'evidence':evidence,'remediation':remediation,'mapping':'; '.join(CONTROL_MAP.get(control,[]))}
def scan(d):
 f=[]
 for u in d.get('users',[]):
  provider=u.get('provider','identity')
  if u.get('enabled') and not u.get('mfa'): f.append(finding('High','MFA',u['name'],'Enabled workforce account has MFA=false','Require MFA and verify registration before normal access.',provider))
  if u.get('enabled') and u.get('days_inactive',0)>=45: f.append(finding('High' if u.get('privileged') else 'Medium','Dormant account',u['name'],f"Enabled account inactive {u['days_inactive']} days",'Review owner; disable if no approved business need.',provider))
 for k in d.get('keys',[]):
  if k.get('active') and k.get('age_days',0)>90: f.append(finding('High','Credential age',k['id'],f"Active key age is {k['age_days']} days",'Rotate/revoke and prefer short-lived credentials.',k.get('provider','aws')))
 for p in d.get('policies',[]):
  if '*' in p.get('actions',[]): f.append(finding('Critical','Least privilege',p['name'],'Policy contains wildcard action *','Replace wildcard administration with task-scoped actions/resources.',p.get('provider','multi-cloud')))
 for s in d.get('storage',[]):
  if s.get('public'): f.append(finding('Critical','Public storage',s['name'],'Storage public=true','Block public access unless explicitly approved and documented.',s.get('provider','multi-cloud')))
 for r in d.get('firewall_rules',[]):
  if r.get('source')=='0.0.0.0/0' and r.get('port') in (22,3389): f.append(finding('Critical','Management exposure',r['name'],f"Port {r['port']} exposed to 0.0.0.0/0",'Remove public management access; use managed session/bastion/VPN.',r.get('provider','multi-cloud')))
 for r in d.get('resources',[]):
  missing=[x for x in ('Environment','Owner') if x not in r.get('tags',{})]
  if missing: f.append(finding('Low','Tagging',r['id'],f"Missing tags: {', '.join(missing)}",'Add required ownership/environment tags.',r.get('provider','multi-cloud')))
 return f
def summarize(findings):
 return {'by_severity':dict(Counter(x['severity'] for x in findings)),'by_control':dict(Counter(x['control'] for x in findings)),'by_provider':dict(Counter(x['provider'] for x in findings))}
def write_reports(findings,out):
 out.mkdir(parents=True,exist_ok=True); risk=min(100,sum(WEIGHTS[x['severity']] for x in findings))
 payload={'risk_score':risk,'finding_count':len(findings),'summary':summarize(findings),'findings':findings}
 (out/'report.json').write_text(json.dumps(payload,indent=2))
 fields=['severity','control','provider','resource','evidence','remediation','mapping']
 with (out/'report.csv').open('w',newline='') as fh:
  cw=csv.DictWriter(fh,fieldnames=fields); cw.writeheader(); cw.writerows(findings)
 rows=''.join(f"<tr><td>{html.escape(x['severity'])}</td><td>{html.escape(x['control'])}</td><td>{html.escape(x['provider'])}</td><td>{html.escape(x['resource'])}</td><td>{html.escape(x['evidence'])}</td><td>{html.escape(x['remediation'])}</td><td>{html.escape(x['mapping'])}</td></tr>" for x in findings)
 summary=summarize(findings)
 cards=' '.join(f"<strong>{html.escape(k)}</strong>: {v}" for k,v in sorted(summary['by_severity'].items()))
 doc=f"""<!doctype html><meta charset='utf-8'><title>CloudGuardian Report</title><style>body{{font-family:Arial,sans-serif;max-width:1200px;margin:40px auto;padding:0 20px}}table{{border-collapse:collapse;width:100%}}th,td{{border:1px solid #bbb;padding:8px;vertical-align:top}}th{{background:#eee}}.score{{font-size:28px;font-weight:700}}</style><h1>CloudGuardian Security Assessment</h1><p class='score'>Risk score: {risk}/100</p><p><b>Findings:</b> {len(findings)} &nbsp; {cards}</p><p><i>Lab heuristic only; not an industry-standard risk score.</i></p><table><tr><th>Severity</th><th>Control</th><th>Provider</th><th>Resource</th><th>Evidence</th><th>Remediation</th><th>Mapping</th></tr>{rows}</table>"""
 (out/'report.html').write_text(doc)
 return risk
if __name__=='__main__':
 ap=argparse.ArgumentParser(description='Audit normalized multi-cloud inventory data for common security risks.')
 ap.add_argument('--input',required=True); ap.add_argument('--out',required=True); ap.add_argument('--fail-on',choices=['none','critical','high'],default='none')
 a=ap.parse_args(); data=json.loads(Path(a.input).read_text()); fs=scan(data); risk=write_reports(fs,Path(a.out))
 print('CLOUDGUARDIAN SECURITY ASSESSMENT'); print('='*38); print(f'Findings: {len(fs)}'); print(f'Risk score: {risk}/100')
 for x in fs: print(f"[{x['severity']}] {x['provider']} | {x['control']} — {x['resource']}: {x['evidence']}")
 if a.fail_on=='critical' and any(x['severity']=='Critical' for x in fs): raise SystemExit(2)
 if a.fail_on=='high' and any(x['severity'] in ('Critical','High') for x in fs): raise SystemExit(2)
