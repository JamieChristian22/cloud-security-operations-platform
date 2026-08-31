from pathlib import Path
import json
p=Path(__file__).resolve().parents[1]/'evidence'/'events.jsonl'
events=[json.loads(x) for x in p.read_text().splitlines() if x.strip()]
known={'dev-jlee':{'198.51.100.24'}}
discovery={'GetCallerIdentity','ListBuckets','ListRoles','DescribeInstances'}
by={}
for e in events:
    key=(e['user'],e['source']); by.setdefault(key,[]).append(e)
for (user,src), evs in by.items():
    score=0; reasons=[]
    if src not in known.get(user,set()): score+=40; reasons.append('new source')
    d=sum(e['action'] in discovery for e in evs)
    if d>=3: score+=40; reasons.append(f'{d} discovery actions')
    if any(e['result']=='Denied' for e in evs): score+=10; reasons.append('denied probing')
    if score>=60: print(f'HIGH user={user} source={src} score={score} reasons={", ".join(reasons)}')
