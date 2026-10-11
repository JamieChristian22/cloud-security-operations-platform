"""Analyze explicitly labeled synthetic ticket data without inventing status/SLA."""
import argparse,csv,json,math
from pathlib import Path
from collections import Counter,defaultdict
from statistics import median

def analyze(rows):
    count=len(rows);ids=set();durations=[];by_priority=defaultdict(list);resolved=0;sla_known=[]
    for row in rows:
        for field in ('id','status','priority','resolution_hours','sla_met'):
            if field not in row:raise ValueError(f'Missing column: {field}')
        if not row['id'] or row['id'] in ids:raise ValueError('Ticket IDs must be nonempty and unique')
        ids.add(row['id'])
        status=row['status'].lower()
        if status not in ('resolved','open','in_progress'):raise ValueError('Unknown ticket status')
        priority=row['priority']
        if priority not in ('P1','P2','P3','P4'):raise ValueError('Unknown ticket priority')
        if status=='resolved':
            hours=float(row['resolution_hours'])
            if not math.isfinite(hours) or hours<0:raise ValueError('Resolution hours must be finite and nonnegative')
            resolved+=1;durations.append(hours);by_priority[priority].append(hours)
        sla=row['sla_met'].lower()
        if sla not in ('yes','no','unknown',''):raise ValueError('SLA must be yes, no or unknown')
        if sla in ('yes','no'):sla_known.append(sla=='yes')
    return dict(scope='Synthetic ticket fixture; SLA flags are supplied, not independently recomputed',
        ticket_count=count,resolved_count=resolved,
        resolution_rate_percent=round(resolved/count*100,1) if count else None,
        average_resolution_hours=round(sum(durations)/len(durations),2) if durations else None,
        median_resolution_hours=median(durations) if durations else None,
        sla_known_count=len(sla_known),sla_unknown_count=count-len(sla_known),
        sla_attainment_percent=round(sum(sla_known)/len(sla_known)*100,1) if sla_known else None,
        priority_distribution=dict(Counter(row['priority'] for row in rows)),
        category_distribution=dict(Counter(row.get('category','Unknown') for row in rows)),
        average_resolution_by_priority={p:round(sum(v)/len(v),2) for p,v in sorted(by_priority.items())})

def main():
    p=argparse.ArgumentParser();p.add_argument('--input',required=True);p.add_argument('--output',required=True);a=p.parse_args()
    try:
        with open(a.input,newline='') as f:result=analyze(list(csv.DictReader(f)))
    except (ValueError,OSError) as exc:print('INPUT ERROR:',exc);return 2
    out=Path(a.output);out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2));return 0
if __name__=='__main__':raise SystemExit(main())
