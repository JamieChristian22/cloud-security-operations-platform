import json
from pathlib import Path
p=Path(__file__).resolve().parents[1]/'evidence'/'signin_events.jsonl'
events=[json.loads(x) for x in p.read_text().splitlines() if x.strip()]
by={}
alerts=[]
for e in events:
    prev=by.get(e['user'])
    if prev and e['minutes_since_previous'] <= 30 and e['country'] != prev['country']:
        alerts.append({'severity':'high','user':e['user'],'reason':'country changed within 30 minutes','from':prev['country'],'to':e['country']})
    by[e['user']]=e
print(json.dumps(alerts,indent=2))
raise SystemExit(0 if alerts else 1)
