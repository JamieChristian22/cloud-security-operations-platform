import importlib.util
from pathlib import Path
import pytest
p=Path(__file__).resolve().parents[1]/'scripts/operations/ticket_metrics.py'
spec=importlib.util.spec_from_file_location('ticket_metrics',p);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)

def row(**changes):
 data=dict(id='INC-1',status='resolved',priority='P2',resolution_hours='2',sla_met='yes');data.update(changes);return data

def test_known_fixture_analytics():
 result=m.analyze([row(),row(id='INC-2',priority='P3',resolution_hours='4',sla_met='no')])
 assert result['average_resolution_hours']==3 and result['sla_attainment_percent']==50
 assert result['priority_distribution']=={'P2':1,'P3':1}

def test_unknown_sla_not_assumed_success():
 result=m.analyze([row(sla_met='unknown')]);assert result['sla_attainment_percent'] is None

def test_open_ticket_not_assumed_resolved():
 result=m.analyze([row(status='open',resolution_hours='',sla_met='unknown')])
 assert result['resolved_count']==0 and result['average_resolution_hours'] is None

def test_missing_status_rejected():
 data=row();del data['status']
 with pytest.raises(ValueError):m.analyze([data])

def test_duplicate_ticket_rejected():
 with pytest.raises(ValueError):m.analyze([row(),row()])

@pytest.mark.parametrize('value',['-1','nan','inf'])
def test_invalid_duration_rejected(value):
 with pytest.raises(ValueError):m.analyze([row(resolution_hours=value)])
