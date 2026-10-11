from pathlib import Path
import yaml
ROOT=Path(__file__).resolve().parents[1]

def test_workflow_is_readonly_and_has_real_gates():
 workflow=yaml.safe_load((ROOT/'.github/workflows/ci.yml').read_text())
 assert workflow['permissions']=={'contents':'read'}
 assert set(workflow['jobs'])=={'offline','terraform','security'}
 for job in workflow['jobs'].values():
  for step in job['steps']:
   assert not step.get('continue-on-error',False)
   if 'uses' in step:assert len(step['uses'].split('@')[1])==40

def test_no_cloud_apply_in_ci():
 text=(ROOT/'.github/workflows/ci.yml').read_text()
 assert 'terraform apply' not in text and 'pull_request_target' not in text
