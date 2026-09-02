#!/usr/bin/env python3
import argparse,json
from pathlib import Path

def evaluate(resources,budget=400.0):
    total=round(sum(float(r.get("monthly_cost",0)) for r in resources),2)
    findings=[]
    for r in resources:
        if r.get("monthly_cost",0)>100:
            findings.append({"severity":"MEDIUM","resource":r["id"],"finding":f"Monthly cost ${r['monthly_cost']:.2f} exceeds $100 review threshold","action":"Review utilization, sizing, schedules, reservations/commitments, and business owner."})
        tags=r.get("tags",{})
        if "cost_center" not in tags:
            findings.append({"severity":"LOW","resource":r["id"],"finding":"Missing cost_center tag","action":"Assign cost-center ownership before production approval."})
    pct=round(total/budget*100,1)
    status="OK" if total<=budget else "BUDGET_EXCEEDED"
    return {"monthly_estimate":total,"budget":budget,"budget_utilization_percent":pct,"status":status,"findings":findings}

def main():
    root=Path(__file__).parents[1]; p=argparse.ArgumentParser(); p.add_argument("--input",default=str(root/"sample_data/resources.json")); p.add_argument("--budget",type=float,default=400.0); p.add_argument("--output",default=str(root/"reports/cost_guardrails.json")); a=p.parse_args()
    result=evaluate(json.loads(Path(a.input).read_text()),a.budget); Path(a.output).parent.mkdir(parents=True,exist_ok=True); Path(a.output).write_text(json.dumps(result,indent=2)); print(json.dumps(result,indent=2))
if __name__=="__main__": main()
