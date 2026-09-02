#!/usr/bin/env python3
import argparse, json
from pathlib import Path


def audit(resources):
    out=[]
    for r in resources:
        if r.get("public"):
            out.append({"severity":"HIGH","resource":r["id"],"control":"Public exposure","evidence":"public=true","remediation":"Remove public exposure unless explicitly required; restrict ingress and document exception."})
        if not r.get("encrypted"):
            out.append({"severity":"HIGH","resource":r["id"],"control":"Encryption at rest","evidence":"encrypted=false","remediation":"Enable provider-managed or customer-managed encryption."})
        if not r.get("logging"):
            out.append({"severity":"MEDIUM","resource":r["id"],"control":"Audit logging","evidence":"logging=false","remediation":"Enable service and access logging with centralized retention."})
        if r.get("type") == "object_storage" and not r.get("backup"):
            out.append({"severity":"MEDIUM","resource":r["id"],"control":"Recovery","evidence":"backup=false","remediation":"Enable versioning or backup according to data criticality."})
        tags=r.get("tags",{})
        missing=[x for x in ("owner","environment","cost_center") if not tags.get(x)]
        if missing:
            out.append({"severity":"LOW","resource":r["id"],"control":"Tag governance","evidence":"Missing: "+", ".join(missing),"remediation":"Apply required ownership, environment, and cost-center tags."})
    return out


def main():
    root=Path(__file__).parents[1]
    p=argparse.ArgumentParser()
    p.add_argument("--input", default=str(root/"sample_data/resources.json")); p.add_argument("--output",default=str(root/"reports/security_baseline.json")); a=p.parse_args()
    resources=json.loads(Path(a.input).read_text()); findings=audit(resources)
    result={"resources_reviewed":len(resources),"findings":findings,"summary":{s:sum(1 for f in findings if f["severity"]==s) for s in ["CRITICAL","HIGH","MEDIUM","LOW"]}}
    Path(a.output).parent.mkdir(parents=True,exist_ok=True); Path(a.output).write_text(json.dumps(result,indent=2)); print(json.dumps(result,indent=2))
if __name__=="__main__": main()
