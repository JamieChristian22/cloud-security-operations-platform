#!/usr/bin/env python3
import argparse,json,re
from pathlib import Path

def main():
    p=argparse.ArgumentParser(); p.add_argument("--repo",required=True); p.add_argument("--output",required=True); a=p.parse_args(); root=Path(a.repo)
    required=["README.md","PROJECT-INDEX.md","PORTFOLIO-EVIDENCE.md","docs/THREAT-MODEL.md","docs/DISASTER-RECOVERY.md","docs/COST-GOVERNANCE.md","01-multi-cloud-foundation-iam","02-cloud-support-reliability-center","03-security-operations-incident-response","04-cloudguardian-security-auditor","05-devsecops-infrastructure-delivery"]
    missing=[x for x in required if not (root/x).exists()]
    terms=['TO'+'DO','FIX'+'ME','TB'+'D']; banned=re.compile(r'\b(?:'+ '|'.join(terms) + r')\b',re.I); markers=[]
    for f in root.rglob("*"):
        if f.is_file() and f.suffix.lower() in {".md",".py",".tf",".hcl",".yml",".yaml",".json",".txt",".csv"}:
            try: text=f.read_text(errors="ignore")
            except Exception: continue
            if banned.search(text): markers.append(str(f.relative_to(root)))
    result={"required_items":len(required),"missing":missing,"unfinished_markers":markers,"status":"PASS" if not missing and not markers else "FAIL"}; Path(a.output).parent.mkdir(parents=True,exist_ok=True); Path(a.output).write_text(json.dumps(result,indent=2)); print(json.dumps(result,indent=2)); return 0 if result["status"]=="PASS" else 1
if __name__=="__main__": raise SystemExit(main())
