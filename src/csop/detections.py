"""Offline event detections with explicit windows and evidence identifiers."""
import hashlib
import ipaddress
import math
from datetime import timedelta
from .audit import utc


def normalize(events):
    seen, result = set(), []
    for index, original in enumerate(events):
        event = dict(original)
        for field in ('timestamp','user','source_ip','result'):
            if not isinstance(event.get(field),str) or not event[field].strip():
                raise ValueError(f'event {index}: missing {field}')
        event['_time'] = utc(event['timestamp'])
        ipaddress.ip_address(event['source_ip'])
        if event['result'] not in ('success','failure'):
            raise ValueError('result must be success or failure')
        for key, limit in [('latitude',90),('longitude',180)]:
            if key in event and (type(event[key]) not in (float,int) or not -limit <= event[key] <= limit):
                raise ValueError(f'invalid {key}')
        if ('latitude' in event) != ('longitude' in event):
            raise ValueError('latitude and longitude must be supplied together')
        if 'trusted_network' in event and type(event['trusted_network']) is not bool:
            raise ValueError('trusted_network must be boolean')
        event['event_id'] = event.get('event_id') or hashlib.sha256(
            repr(sorted(original.items())).encode()).hexdigest()[:16]
        if event['event_id'] not in seen:
            result.append(event)
            seen.add(event['event_id'])
    return sorted(result, key=lambda e: (e['_time'], e['event_id']))


def distance_km(a,b):
    lat1,lat2 = map(math.radians,(a['latitude'],b['latitude']))
    dlat = lat2-lat1
    dlon = math.radians(b['longitude']-a['longitude'])
    h = math.sin(dlat/2)**2 + math.cos(lat1)*math.cos(lat2)*math.sin(dlon/2)**2
    return 6371 * 2 * math.asin(math.sqrt(min(1,h)))


def impossible_travel(events, speed_kmh=900, minimum_km=500):
    previous, alerts = {}, []
    for event in normalize(events):
        if event['result'] != 'success' or 'latitude' not in event:
            continue
        before = previous.get(event['user'])
        previous[event['user']] = event
        if not before:
            continue
        if event.get('trusted_network') or before.get('trusted_network'):
            continue
        km = distance_km(before,event)
        hours = (event['_time']-before['_time']).total_seconds()/3600
        speed = km/hours if hours > 0 else None
        if km >= minimum_km and (speed is None or speed > speed_kmh):
            alerts.append(dict(rule_id='DET-001',severity='high',user=event['user'],
                distance_km=round(km,1), elapsed_minutes=round(hours*60,2),
                speed_kmh=round(speed,1) if speed is not None else None,
                reason='Geographic distance exceeds plausible travel speed',
                event_ids=[before['event_id'],event['event_id']], mitre='T1078'))
    return alerts


def password_spray(events, window_minutes=10, threshold=3, success_minutes=10):
    if window_minutes <= 0 or threshold < 2 or success_minutes <= 0:
        raise ValueError('positive windows and threshold >= 2 required')
    events = normalize(events)
    windows, emitted, alerts = {}, {}, []
    for event in events:
        if event['result'] != 'failure':
            continue
        ip, now = event['source_ip'], event['_time']
        recent = [e for e in windows.get(ip,[]) if now-e['_time'] <= timedelta(minutes=window_minutes)]
        recent.append(event)
        windows[ip] = recent
        users = {e['user'] for e in recent}
        if len(users) < threshold or (ip in emitted and now-emitted[ip] <= timedelta(minutes=window_minutes)):
            continue
        successes = [e for e in events if e['source_ip']==ip and e['user'] in users and
            e['result']=='success' and now < e['_time'] <= now+timedelta(minutes=success_minutes)]
        alerts.append(dict(rule_id='DET-002',severity='high' if successes else 'medium',
            source_ip=ip, failed_users=sorted(users), window_minutes=window_minutes,
            subsequent_success_users=sorted({e['user'] for e in successes}),
            event_ids=[e['event_id'] for e in recent+successes], mitre='T1110.003'))
        emitted[ip] = now
    return alerts


def credential_recon(events, window_minutes=10, threshold=3):
    """Correlate distinct reconnaissance APIs; this is a signal, not proof of theft."""
    apis={'GetCallerIdentity','ListBuckets','ListRoles','DescribeInstances'}
    groups, alerts, emitted = {}, [], {}
    for e in normalize(events):
        if e.get('action') not in apis:
            continue
        key=(e['user'],e['source_ip'])
        recent=[x for x in groups.get(key,[]) if e['_time']-x['_time']<=timedelta(minutes=window_minutes)]
        recent.append(e); groups[key]=recent
        if len({x['action'] for x in recent})>=threshold and (
            key not in emitted or e['_time']-emitted[key]>timedelta(minutes=window_minutes)):
            alerts.append(dict(rule_id='DET-003',severity='medium',user=e['user'],source_ip=e['source_ip'],
                actions=sorted({x['action'] for x in recent}),event_ids=[x['event_id'] for x in recent],
                reason='Burst of distinct discovery APIs; verify approved automation',mitre='T1526'))
            emitted[key]=e['_time']
    return alerts
