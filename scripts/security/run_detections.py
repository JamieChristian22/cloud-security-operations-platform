#!/usr/bin/env python3
import argparse,json,subprocess,sys
from pathlib import Path

def main():
    p=argparse.ArgumentParser(); p.add_argument("--repo",required=True); p.add_argument("--output",required=True); a=p.parse_args(); repo=Path(a.repo)
    det=repo/"03-security-operations-incident-response/detections"; results=[]
    for script in ["credential-compromise.py","password_spray.py","impossible_travel.py"]:
        path=det/script; proc=subprocess.run([sys.executable,str(path)],cwd=repo,text=True,capture_output=True)
        results.append({"script":script,"returncode":proc.returncode,"status":"PASS" if proc.returncode==0 else "FAIL","stdout":proc.stdout.strip(),"stderr":proc.stderr.strip()})
    overall="PASS" if all(r["returncode"]==0 for r in results) else "FAIL"
    out={"overall":overall,"detections":results}; Path(a.output).parent.mkdir(parents=True,exist_ok=True); Path(a.output).write_text(json.dumps(out,indent=2)); print(json.dumps(out,indent=2)); return 0 if overall=="PASS" else 1
if __name__=="__main__": raise SystemExit(main())
