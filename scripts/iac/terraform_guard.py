#!/usr/bin/env python3
import argparse,json,re,shutil,subprocess
from pathlib import Path

def scan_files(root):
    findings=[]; tf=list(root.rglob("*.tf"))
    rules=[("HIGH",re.compile(r'0\.0\.0\.0/0'),"Broad IPv4 CIDR detected; confirm exposure is intentional."),("HIGH",re.compile(r'::/0'),"Broad IPv6 CIDR detected; confirm exposure is intentional."),("HIGH",re.compile(r'(?i)password\s*=\s*"[^$]'),"Possible plaintext password assignment."),("HIGH",re.compile(r'(?i)(secret|access_key)\s*=\s*"[A-Za-z0-9]'),"Possible hard-coded secret." )]
    for f in tf:
        text=f.read_text(errors="ignore")
        for sev,pat,msg in rules:
            for m in pat.finditer(text):
                findings.append({"severity":sev,"file":str(f.relative_to(root)),"line":text[:m.start()].count("\n")+1,"finding":msg})
    return tf,findings

def run(cmd,cwd):
    p=subprocess.run(cmd,cwd=cwd,text=True,capture_output=True); return {"command":" ".join(cmd),"returncode":p.returncode,"stdout":p.stdout[-4000:],"stderr":p.stderr[-4000:]}

def main():
    p=argparse.ArgumentParser(); p.add_argument("--root",required=True); p.add_argument("--output",required=True); a=p.parse_args(); root=Path(a.root); tf,findings=scan_files(root); checks=[]
    if shutil.which("terraform"):
        checks.append(run(["terraform","fmt","-check","-recursive"],root))
        checks.append(run(["terraform","init","-backend=false","-input=false"],root))
        checks.append(run(["terraform","validate"],root))
    result={"terraform_files":len(tf),"static_findings":findings,"terraform_cli_available":bool(shutil.which("terraform")),"cli_checks":checks,"status":"PASS" if not findings and all(c["returncode"]==0 for c in checks) else "REVIEW_REQUIRED"}
    Path(a.output).parent.mkdir(parents=True,exist_ok=True); Path(a.output).write_text(json.dumps(result,indent=2)); print(json.dumps(result,indent=2))
if __name__=="__main__": main()
