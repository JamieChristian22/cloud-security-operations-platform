import copy
from datetime import datetime,timezone
import pytest
from csop.audit import scan,apply_exceptions,gate
from csop.inventory import SECTIONS

@pytest.fixture
def inventory():return {k:[] for k in SECTIONS}

@pytest.mark.parametrize('section',SECTIONS)
def test_missing_section_is_error(inventory,section):
 del inventory[section]
 with pytest.raises(ValueError):scan(inventory)

@pytest.mark.parametrize('source,start,end,expected',[
 ('0.0.0.0/0',22,22,True),('::/0',1,65535,True),('::/0',3389,3389,True),
 ('10.0.0.0/8',22,22,False),('0.0.0.0/0',443,443,False),('0.0.0.0/0',20,25,True)])
def test_management_ranges(inventory,source,start,end,expected):
 inventory['firewall_rules']=[dict(name='rule',source=source,from_port=start,to_port=end)]
 assert bool(scan(inventory))==expected

@pytest.mark.parametrize('action,severity',[('*','Critical'),('s3:*','High'),('iam:Get*','High'),('s3:GetObject',None)])
def test_wildcard_actions(inventory,action,severity):
 inventory['policies']=[dict(name='policy',actions=[action])]
 findings=scan(inventory)
 assert (findings[0]['severity'] if findings else None)==severity

@pytest.mark.parametrize('days,expected',[(89,False),(90,False),(91,True)])
def test_key_boundary(inventory,days,expected):
 inventory['keys']=[dict(id='key',active=True,age_days=days)]
 assert bool(scan(inventory))==expected

@pytest.mark.parametrize('days,expected',[(44,False),(45,True),(46,True)])
def test_inactivity_boundary(inventory,days,expected):
 inventory['users']=[dict(name='u',enabled=True,mfa=True,days_inactive=days)]
 assert bool(scan(inventory))==expected

def test_disabled_identity_not_flagged(inventory):
 inventory['users']=[dict(name='u',enabled=False,mfa=False,days_inactive=90)]
 assert scan(inventory)==[]

def test_missing_encryption_not_clean(inventory):
 inventory['storage']=[dict(name='bucket',public=False)]
 with pytest.raises(ValueError):scan(inventory)

def test_encryption_control(inventory):
 inventory['storage']=[dict(name='bucket',public=False,encrypted=False)]
 assert scan(inventory)[0]['control_id']=='CG-008'

@pytest.mark.parametrize('field,value',[('enabled','false'),('days_inactive',-1),('mfa',1)])
def test_bad_user_values(inventory,field,value):
 u=dict(name='u',enabled=True,mfa=True,days_inactive=0);u[field]=value
 inventory['users']=[u]
 with pytest.raises(ValueError):scan(inventory)

def test_empty_tags_flagged(inventory):
 inventory['resources']=[dict(id='vm',tags={'Owner':' ','Environment':'dev'})]
 assert scan(inventory)[0]['control_id']=='CG-007'

def test_duplicate_resource_rejected(inventory):
 inventory['storage']=[dict(name='b',public=True,encrypted=True)]*2
 with pytest.raises(ValueError):scan(inventory)

@pytest.mark.parametrize('source', ['garbage','10.0.0.0/999'])
def test_bad_cidr_rejected(inventory,source):
 inventory['firewall_rules']=[dict(name='fw',source=source,port=22)]
 with pytest.raises(ValueError):scan(inventory)

def test_exception_visibility_and_gate(inventory):
 inventory['storage']=[dict(name='b',public=True,encrypted=True)]
 findings=scan(inventory);now=datetime(2026,1,1,tzinfo=timezone.utc)
 exception=dict(finding_id=findings[0]['id'],owner='security-owner',reason='Documented lab exception',ticket='RISK-001',expires_at='2026-01-02T00:00:00Z')
 result=apply_exceptions(findings,[exception],now)
 assert result[0]['status']=='accepted_risk' and not gate(result,'high')
 assert findings[0]['status']=='open' and gate(findings,'high')
 exception['expires_at']='2025-12-31T00:00:00Z'
 with pytest.raises(ValueError):apply_exceptions(findings,[exception],now)

def test_fingerprints_stable(inventory):
 inventory['storage']=[dict(name='a',public=True,encrypted=True),dict(name='b',public=True,encrypted=True)]
 first=scan(inventory);inventory['storage'].reverse()
 assert scan(inventory)==first
