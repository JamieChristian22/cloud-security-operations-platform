import importlib.util
from pathlib import Path
import pytest
path=Path(__file__).resolve().parents[1]/'scripts/collectors/aws_security_groups.py'
spec=importlib.util.spec_from_file_location('collector',path);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)

def test_cli_export_ipv6_and_all_protocols():
 result=m.normalize_groups([{'GroupId':'sg-demo','IpPermissions':[{'IpProtocol':'-1','Ipv6Ranges':[{'CidrIpv6':'::/0'}]}]}])
 assert result['firewall_rules'][0]['to_port']==65535
 assert result['metadata'] if 'metadata' in result else result['firewall_rules'][0]['protocol']=='all'

def test_referenced_groups_are_not_fabricated_as_cidrs():
 result=m.normalize_groups([{'GroupId':'sg-demo','IpPermissions':[{'IpProtocol':'tcp','FromPort':22,'ToPort':22,'UserIdGroupPairs':[{'GroupId':'sg-source'}]}]}])
 assert result['firewall_rules']==[]

def test_invalid_export_fails():
 with pytest.raises(KeyError):m.normalize_groups([{}])
