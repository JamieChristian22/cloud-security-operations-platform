import json,sys
from pathlib import Path
d=json.loads(Path(sys.argv[1]).read_text()); errors=[]
for s in d.get('storage',[]):
 if s.get('public'): errors.append(f"Public storage forbidden: {s['name']}")
for r in d.get('firewall_rules',[]):
 if r.get('source')=='0.0.0.0/0' and r.get('port') in (22,3389): errors.append(f"Public management port forbidden: {r['name']}")
for p in d.get('policies',[]):
 if '*' in p.get('actions',[]): errors.append(f"Wildcard admin action forbidden: {p['name']}")
if errors:
 print('\n'.join('FAIL: '+x for x in errors)); raise SystemExit(1)
print('PASS: proposed change satisfies portfolio security gates')
