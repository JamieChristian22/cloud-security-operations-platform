#!/usr/bin/env python3
import argparse,json
from pathlib import Path

def check(assets):
    findings=[]
    for a in assets:
        if a["tier"] in {"critical","important"} and not a["backup_enabled"]:
            findings.append({"severity":"CRITICAL","service":a["service"],"finding":"Required backup is disabled","remediation":"Enable policy-backed backup immediately."})
        if a["backup_enabled"] and a["last_backup_hours"] > max(a["rpo_hours"]*2,4):
            findings.append({"severity":"HIGH","service":a["service"],"finding":f"Last backup was {a['last_backup_hours']}h ago; RPO is {a['rpo_hours']}h","remediation":"Investigate backup job health and run an on-demand protected backup."})
        if a["tier"]=="critical" and a["restore_test_days"]>30:
            findings.append({"severity":"HIGH","service":a["service"],"finding":f"Restore test is {a['restore_test_days']} days old","remediation":"Run and document a restore test within the 30-day critical-service cadence."})
        if a["tier"]=="critical" and not a["replicated"]:
            findings.append({"severity":"HIGH","service":a["service"],"finding":"Critical service lacks replication","remediation":"Add independent replica or cross-region recovery path."})
    return {"services_reviewed":len(assets),"findings":findings,"status":"READY" if not any(f["severity"] in {"CRITICAL","HIGH"} for f in findings) else "ACTION_REQUIRED"}

def main():
    root=Path(__file__).parents[1]; p=argparse.ArgumentParser(); p.add_argument("--input",default=str(root/"sample_data/dr_assets.json")); p.add_argument("--output",default=str(root/"reports/dr_readiness.json")); a=p.parse_args(); result=check(json.loads(Path(a.input).read_text())); Path(a.output).parent.mkdir(parents=True,exist_ok=True); Path(a.output).write_text(json.dumps(result,indent=2)); print(json.dumps(result,indent=2))
if __name__=="__main__": main()
