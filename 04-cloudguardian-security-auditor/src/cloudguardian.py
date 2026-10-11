"""CloudGuardian CLI. Assess normalized inventory; never mutate cloud resources."""
import argparse
import csv
import html
import json
import sys
from collections import Counter
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[2]/'src'))
from csop.audit import scan, apply_exceptions, gate, WEIGHTS


def summarize(findings):
    return {f'by_{key}':dict(Counter(f[key] for f in findings)) for key in ('severity','control','provider','status')}


def write_reports(findings,out,metadata=None):
    out.mkdir(parents=True,exist_ok=True)
    open_findings=[f for f in findings if f['status']=='open']
    risk=min(100,sum(WEIGHTS[f['severity']] for f in open_findings))
    payload=dict(schema_version='2.0',risk_score=risk,finding_count=len(findings),
        open_count=len(open_findings),summary=summarize(findings),findings=findings,
        scope='Supplied normalized inventory only; score is a lab heuristic',inventory_metadata=metadata or {})
    (out/'report.json').write_text(json.dumps(payload,indent=2)+'\n')
    fields=['id','control_id','severity','status','control','provider','resource','evidence','remediation']
    def safe_cell(value):
        value=str(value)
        return "'"+value if value.startswith(('=','+','-','@','\t','\r','\n')) else value
    with (out/'report.csv').open('w',newline='') as fh:
        writer=csv.DictWriter(fh,fieldnames=fields);writer.writeheader()
        writer.writerows({k:safe_cell(f[k]) for k in fields} for f in findings)
    rows=''.join('<tr>'+''.join('<td>'+html.escape(str(f[k]))+'</td>' for k in fields)+'</tr>' for f in findings)
    headings=''.join('<th>'+k.replace('_',' ').title()+'</th>' for k in fields)
    doc=f'''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>CloudGuardian assessment</title>
<style>body{{font:15px system-ui;margin:0;background:#eef3f9;color:#13243a}}header{{padding:36px;background:#11243c;color:white}}main{{padding:28px;overflow:auto}}table{{border-collapse:collapse;background:white;width:100%}}th,td{{padding:12px;border-bottom:1px solid #d8e1ec;text-align:left;vertical-align:top}}th{{background:#dce9f4}}.metric{{font-size:28px}}footer{{padding:24px}}</style>
<header><p>CLOUD SECURITY & OPERATIONS PLATFORM</p><h1>CloudGuardian assessment</h1><p class="metric">{len(open_findings)} open findings · {len(findings)-len(open_findings)} accepted risks · {risk}/100 heuristic score</p><p>Assessment of supplied inventory. A zero score does not establish compliance or complete cloud coverage.</p></header><main><table><thead><tr>{headings}</tr></thead><tbody>{rows}</tbody></table></main><footer>Accepted risks remain visible. Verify evidence provenance and collection scope before remediation.</footer></html>'''
    (out/'report.html').write_text(doc)
    return risk


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--input',required=True);p.add_argument('--out',required=True)
    p.add_argument('--exceptions');p.add_argument('--fail-on',choices=['none','critical','high','medium','low'],default='none')
    a=p.parse_args()
    try:
        data=json.loads(Path(a.input).read_text())
        findings=scan(data)
        if a.exceptions:
            findings=apply_exceptions(findings,json.loads(Path(a.exceptions).read_text()))
        score=write_reports(findings,Path(a.out),data.get("metadata"))
    except (ValueError,OSError,TypeError) as exc:
        print(f'INPUT ERROR: {exc}',file=sys.stderr);return 2
    print(json.dumps(dict(findings=len(findings),risk_score=score,gate='FAIL' if gate(findings,a.fail_on) else 'PASS')))
    return 1 if gate(findings,a.fail_on) else 0

if __name__=='__main__':raise SystemExit(main())
