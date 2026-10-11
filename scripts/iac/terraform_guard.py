"""Compatibility entry point for real Terraform validation; no regex security verdict."""
from pathlib import Path
import argparse,subprocess,sys

def main():
 p=argparse.ArgumentParser();p.add_argument('--root',required=True);p.add_argument('--output',required=True);a=p.parse_args()
 expected=Path(__file__).resolve().parents[2]/'01-multi-cloud-foundation-iam/terraform'
 if Path(a.root).resolve()!=expected:raise SystemExit('This compatibility command validates the repository Terraform root only')
 return subprocess.call([sys.executable,str(Path(__file__).with_name('validate_terraform.py')),'--output',str(Path(a.output).parent/'terraform')])
if __name__=='__main__':raise SystemExit(main())
