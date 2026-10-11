"""Initialize, validate and mock-test every Terraform root; never apply."""
import argparse,json,shutil,subprocess
from datetime import datetime,timezone
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]

def main():
 p=argparse.ArgumentParser();p.add_argument('--terraform',default='terraform');p.add_argument('--output',default=str(ROOT/'evidence/validation/terraform'));a=p.parse_args()
 binary=shutil.which(a.terraform)
 if not binary:print('Terraform CLI not found');return 2
 base=ROOT/'01-multi-cloud-foundation-iam/terraform';out=Path(a.output);out.mkdir(parents=True,exist_ok=True)
 results=[]
 for folder in [base,*sorted((base/'modules').iterdir())]:
  if not folder.is_dir():continue
  name='root' if folder==base else folder.name
  for stage,args in [('fmt',['fmt','-check','-recursive']),('init',['init','-backend=false','-input=false','-no-color']),('validate',['validate','-no-color']),('test',['test','-no-color'])]:
   command=[binary,f'-chdir={folder}',*args]
   try:
    proc=subprocess.run(command,text=True,capture_output=True,timeout=600)
    output=proc.stdout+proc.stderr;rc=proc.returncode
   except subprocess.TimeoutExpired:
    output='Timed out after 600 seconds';rc=124
   (out/f'{name}-{stage}.txt').write_text(output)
   results.append(dict(module=name,stage=stage,returncode=rc,log=f'{name}-{stage}.txt'))
   print(name,stage,'PASS' if rc==0 else 'FAIL',flush=True)
   if rc:break
 summary=dict(timestamp=datetime.now(timezone.utc).isoformat(),scope='Provider validation and mock tests; no live deployment',results=results,status='PASS' if len(results)==16 and all(x['returncode']==0 for x in results) else 'FAIL')
 (out/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
 return 0 if summary['status']=='PASS' else 1
if __name__=='__main__':raise SystemExit(main())
