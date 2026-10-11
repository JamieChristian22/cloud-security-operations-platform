import pytest
from csop.detections import impossible_travel,password_spray,credential_recon,normalize

def event(minute=0,user='a',result='success',ip='203.0.113.10',**kwargs):
 return dict(timestamp=f'2026-01-01T00:{minute:02}:00Z',user=user,result=result,source_ip=ip,**kwargs)

def spray():return [event(i,user=u,result='failure') for i,u in enumerate('abc')]

def test_travel_sorts_events():
 a=event(0,latitude=40.7,longitude=-74);b=event(10,latitude=52.5,longitude=13.4)
 assert len(impossible_travel([b,a]))==1

def test_travel_same_city_no_alert():
 assert impossible_travel([event(0,latitude=40.7,longitude=-74),event(10,latitude=40.71,longitude=-74)])==[]

def test_travel_ignores_failures():
 assert impossible_travel([event(0,latitude=40.7,longitude=-74),event(10,result='failure',latitude=52.5,longitude=13.4)])==[]

def test_travel_trusted_network_suppression():
 assert impossible_travel([event(0,latitude=40.7,longitude=-74,trusted_network=True),event(10,latitude=52.5,longitude=13.4)])==[]

def test_travel_missing_geo_is_not_invented():
 assert impossible_travel([event(0),event(10)])==[]

def test_simultaneous_far_away_signins():
 alerts=impossible_travel([event(0,latitude=40.7,longitude=-74),event(0,latitude=52.5,longitude=13.4)])
 assert len(alerts)==1 and alerts[0]['speed_kmh'] is None

def test_spray_then_success():
 alerts=password_spray(list(reversed(spray()+[event(4,user='b')])))
 assert alerts[0]['severity']=='high' and alerts[0]['subsequent_success_users']==['b']

def test_earlier_success_does_not_escalate():
 events=[event(0)]+[event(i+1,user=u,result='failure') for i,u in enumerate('abc')]
 assert password_spray(events)[0]['severity']=='medium'

def test_unrelated_account_success_does_not_escalate():
 assert password_spray(spray()+[event(4,user='d')])[0]['severity']=='medium'

def test_success_outside_window():
 assert password_spray(spray()+[event(20)])[0]['severity']=='medium'

def test_spray_does_not_span_unlimited_time():
 assert password_spray([event(i*20,user=u,result='failure') for i,u in enumerate('abc')])==[]

def test_one_user_bruteforce_not_spray():
 assert password_spray([event(i,result='failure') for i in range(5)])==[]

def test_duplicate_events_deduplicated():
 events=spray();assert len(normalize(events+events))==3
 assert len(password_spray(events+events))==1

@pytest.mark.parametrize('change',[{'timestamp':'2026-01-01T00:00:00'},{'source_ip':'bad'},{'result':'unknown'},{'latitude':100,'longitude':0},{'trusted_network':'yes'}])
def test_invalid_event_rejected(change):
 e=event();e.update(change)
 with pytest.raises(ValueError):normalize([e])

def test_recon_threshold():
 events=[event(i,action=action) for i,action in enumerate(['ListBuckets','ListRoles','DescribeInstances'])]
 assert len(credential_recon(events))==1
 assert credential_recon(events[:2])==[]

def test_recon_is_per_identity():
 events=[event(i,user=str(i),action=action) for i,action in enumerate(['ListBuckets','ListRoles','DescribeInstances'])]
 assert credential_recon(events)==[]
