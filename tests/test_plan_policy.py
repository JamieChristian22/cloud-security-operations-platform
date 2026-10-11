import pytest
from csop.plan_policy import evaluate

def plan(kind,after,unknown=None):
 return dict(format_version='1.2',resource_changes=[dict(type=kind,address=kind+'.demo',change=dict(actions=['create'],after=after,after_unknown=unknown or {}))])

def test_ipv6_standalone_ingress_blocks():
 p=plan('aws_vpc_security_group_ingress_rule',dict(cidr_ipv6='::/0',ip_protocol='tcp',from_port=1,to_port=65535))
 assert evaluate(p)['status']=='FAIL'

def test_unknown_policy_fails_closed():
 assert evaluate(plan('aws_iam_policy',{},dict(policy=True)))['status']=='FAIL'

def test_iam_deny_wildcard_is_allowed():
 assert evaluate(plan('aws_iam_policy',dict(policy={'Statement':[{'Effect':'Deny','Action':'*'}]})))['status']=='PASS'

def test_iam_allow_wildcard_blocks():
 assert evaluate(plan('aws_iam_policy',dict(policy={'Statement':{'Effect':'Allow','Action':'s3:*'}})))['status']=='FAIL'

def test_uncovered_visible():
 result=evaluate(plan('example_resource',{}));assert len(result['uncovered'])==1

def test_missing_plan_rejected():
 with pytest.raises(ValueError):evaluate({})

@pytest.mark.parametrize('port',['22','20-30','*','3389'])
def test_azure_port_ranges(port):
 after=dict(direction='Inbound',access='Allow',protocol='Tcp',source_address_prefix='Internet',destination_port_range=port)
 assert evaluate(plan('azurerm_network_security_rule',after))['status']=='FAIL'

def test_gcp_deny_rule_not_flagged():
 assert evaluate(plan('google_compute_firewall',dict(source_ranges=['0.0.0.0/0'],deny=[dict(protocol='tcp',ports=['22'])])))['status']=='PASS'

def test_gcp_allow_all_ports():
 assert evaluate(plan('google_compute_firewall',dict(source_ranges=['::/0'],allow=[dict(protocol='tcp',ports=[])])))['status']=='FAIL'

def test_s3_requires_all_public_blocks():
 assert evaluate(plan('aws_s3_bucket_public_access_block',dict(block_public_acls=True)))['status']=='FAIL'

def test_destroy_disabled():
 assert evaluate(plan('aws_s3_bucket',dict(force_destroy=True)))['status']=='FAIL'

def test_unknown_resource_id_does_not_hide_known_security_settings():
 result=evaluate(plan('aws_s3_bucket',dict(force_destroy=False),dict(id=True,arn=True)))
 assert result['status']=='PASS'
