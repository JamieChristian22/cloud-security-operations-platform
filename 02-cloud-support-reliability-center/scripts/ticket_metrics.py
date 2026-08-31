import csv
from collections import Counter, defaultdict
from pathlib import Path
DATA = Path(__file__).resolve().parents[1] / "data" / "tickets.csv"
rows=list(csv.DictReader(DATA.open()))
for r in rows: r['resolution_hours']=float(r['resolution_hours'])
closed=len(rows)
avg=sum(r['resolution_hours'] for r in rows)/closed
sla=sum(r['sla_met'].lower()=='yes' for r in rows)
priority=Counter(r['priority'] for r in rows)
category=Counter(r['category'] for r in rows)
causes=Counter(r['root_cause'] for r in rows)
byprio=defaultdict(list)
for r in rows: byprio[r['priority']].append(r['resolution_hours'])
print('CLOUD SUPPORT & RELIABILITY KPI REPORT')
print('='*43)
print(f'Tickets resolved: {closed}/{closed}')
print(f'Average resolution time: {avg:.2f} hours')
print(f'SLA attainment: {(sla/closed)*100:.1f}%')
print('Priority breakdown: ' + ', '.join(f'{k}={priority[k]}' for k in sorted(priority)))
print('Average resolution by priority: ' + ', '.join(f'{k}={sum(v)/len(v):.2f}h' for k,v in sorted(byprio.items())))
print('\nTop categories:')
for k,v in category.most_common(8): print(f'  {k}: {v}')
print('\nRepeat root causes / themes:')
for k,v in causes.most_common():
    if v > 1: print(f'  {k}: {v}')
if not any(v>1 for v in causes.values()): print('  No exact duplicate root-cause labels; review broader control themes in RCA-TRENDS.md')
