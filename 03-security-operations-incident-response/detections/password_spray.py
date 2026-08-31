import json
from collections import defaultdict
from pathlib import Path
p=Path(__file__).resolve().parents[1]/'evidence'/'signin_events.jsonl'
events=[json.loads(x) for x in p.read_text().splitlines() if x.strip()]
failed=defaultdict(set); successes=[]
for e in events:
    if e['result']=='failure': failed[e['source_ip']].add(e['user'])
    elif e['result']=='success': successes.append(e)
alerts=[]
for ip,users in failed.items():
    if len(users)>=3:
        hit=[s for s in successes if s['source_ip']==ip]
        alerts.append({'severity':'high' if hit else 'medium','source_ip':ip,'failed_users':sorted(users),'subsequent_success_users':[x['user'] for x in hit]})
print(json.dumps(alerts,indent=2))
raise SystemExit(0 if alerts else 1)
