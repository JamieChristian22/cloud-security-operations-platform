"""Gate normalized proposed inventory, using the same controls as CloudGuardian."""
import json,sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[2]/'src'))
from csop.audit import scan,gate

def main():
 try:
  data=json.loads(Path(sys.argv[1]).read_text());findings=scan(data)
 except (ValueError,OSError,IndexError) as e:
  print('INPUT ERROR:',e);return 2
 for f in findings:print(f"{f['severity']}: {f['control_id']} {f['resource']} {f['evidence']}")
 failed=gate(findings,'high');print('FAIL' if failed else 'PASS')
 return 1 if failed else 0
if __name__=='__main__':raise SystemExit(main())
