"""Validate delivery structure and local documentation links."""
import argparse,json,re
from pathlib import Path
from urllib.parse import unquote
REQUIRED=['README.md','PROJECT-INDEX.md','PORTFOLIO-EVIDENCE.md','requirements-dev.txt','Makefile','.github/workflows/ci.yml','src/csop/audit.py','src/csop/detections.py','tests/test_security_engine.py','docs/DEPLOYMENT-GUIDE.md','docs/CONTROL-CATALOG.md']
EXCLUDED={'.terraform','.venv','__pycache__','.pytest_cache','.git','.ci-tools'}

def check(root):
 missing=[x for x in REQUIRED if not (root/x).is_file()];broken=[]
 for path in root.rglob('*.md'):
  if any(x in EXCLUDED for x in path.relative_to(root).parts):continue
  for target in re.findall(r'\]\(([^)]+)\)',path.read_text()):
   if target.startswith(('http:','https:','mailto:','#')):continue
   target=unquote(target.split('#')[0])
   if target and not (path.parent/target).exists():broken.append(dict(file=str(path.relative_to(root)),target=target))
 return dict(required_items=len(REQUIRED),missing=missing,broken_local_links=broken,status='PASS' if not missing and not broken else 'FAIL')

def main():
 p=argparse.ArgumentParser();p.add_argument('--repo',required=True);p.add_argument('--output',required=True);a=p.parse_args();result=check(Path(a.repo))
 out=Path(a.output);out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2));return 0 if result['status']=='PASS' else 1
if __name__=='__main__':raise SystemExit(main())
