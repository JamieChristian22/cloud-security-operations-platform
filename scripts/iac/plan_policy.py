"""Policy check for saved Terraform JSON. Use --require-full-coverage for strict scope."""
import argparse,json,sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[2]/'src'))
from csop.plan_policy import evaluate

def main():
 p=argparse.ArgumentParser();p.add_argument('--input',required=True);p.add_argument('--output',required=True);p.add_argument('--require-full-coverage',action='store_true');a=p.parse_args()
 try:result=evaluate(json.loads(Path(a.input).read_text()))
 except (ValueError,OSError) as e:print('INPUT ERROR:',e,file=sys.stderr);return 2
 if a.require_full_coverage and result['uncovered']:result['status']='FAIL'
 out=Path(a.output);out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(result,indent=2)+'\n');print(result['status'])
 return 0 if result['status']=='PASS' else 1
if __name__=='__main__':raise SystemExit(main())
