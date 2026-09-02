#!/usr/bin/env python3
import argparse,csv,json
from pathlib import Path
from collections import Counter

def analyze(rows):
    count=len(rows); resolved=sum(1 for r in rows if r.get("status","resolved").lower()=="resolved")
    durations=[float(r.get("resolution_hours",0) or 0) for r in rows]
    sla=sum(1 for r in rows if str(r.get("sla_met","true")).lower() in {"true","yes","1"})
    sev=Counter(r.get("severity","Unknown") for r in rows)
    return {"ticket_count":count,"resolved_count":resolved,"resolution_rate_percent":round(resolved/count*100,1) if count else 0,"average_resolution_hours":round(sum(durations)/count,2) if count else 0,"sla_attainment_percent":round(sla/count*100,1) if count else 0,"severity_distribution":dict(sev)}

def main():
    p=argparse.ArgumentParser(); p.add_argument("--input",required=True); p.add_argument("--output",required=True); a=p.parse_args(); rows=list(csv.DictReader(open(a.input,newline=""))); result=analyze(rows); Path(a.output).parent.mkdir(parents=True,exist_ok=True); Path(a.output).write_text(json.dumps(result,indent=2)); print(json.dumps(result,indent=2))
if __name__=="__main__": main()
