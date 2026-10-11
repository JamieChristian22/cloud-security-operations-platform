"""Focused policy over Terraform show -json plans. Report explicit coverage."""
import json
import ipaddress

SUPPORTED = {
 'aws_security_group','aws_vpc_security_group_ingress_rule',
 'aws_s3_bucket_public_access_block','aws_s3_bucket','aws_iam_policy','aws_iam_role_policy',
 'azurerm_network_security_rule','azurerm_network_security_group',
 'google_compute_firewall','google_storage_bucket',
}

SECURITY_FIELDS = {
 'aws_security_group': ('ingress',),
 'aws_vpc_security_group_ingress_rule': ('cidr_ipv4','cidr_ipv6','ip_protocol','from_port','to_port'),
 'aws_s3_bucket_public_access_block': ('block_public_acls','block_public_policy','ignore_public_acls','restrict_public_buckets'),
 'aws_s3_bucket': ('force_destroy',),
 'aws_iam_policy': ('policy',), 'aws_iam_role_policy': ('policy',),
 'azurerm_network_security_group': ('security_rule',),
 'azurerm_network_security_rule': ('direction','access','protocol','source_address_prefix','source_address_prefixes','destination_port_range','destination_port_ranges'),
 'google_compute_firewall': ('direction','disabled','source_ranges','allow'),
 'google_storage_bucket': ('force_destroy','uniform_bucket_level_access','public_access_prevention'),
}

def contains_unknown(value):
    if isinstance(value,dict):return any(contains_unknown(v) for v in value.values())
    if isinstance(value,list):return any(contains_unknown(v) for v in value)
    return value is True

def public(source):
    if source in ('*','Internet','Any'):return True
    try:return ipaddress.ip_network(source,strict=False).prefixlen==0
    except (ValueError,TypeError):return False

def management(start,end):
    return any(int(start)<=p<=int(end) for p in (22,3389))

def azure_ports(rule):
    ranges=rule.get('destination_port_ranges') or [rule.get('destination_port_range')]
    for item in ranges:
        if item=='*':return True
        if not isinstance(item,str):raise ValueError('missing Azure destination port range')
        pieces=item.split('-');start=int(pieces[0]);end=int(pieces[-1])
        if management(start,end):return True
    return False

def evaluate(plan):
    if not isinstance(plan,dict) or 'format_version' not in plan or not isinstance(plan.get('resource_changes'),list):
        raise ValueError('Expected terraform show -json with resource_changes array')
    if plan.get('errored') is True or plan.get('complete') is False:
        raise ValueError('Errored or incomplete plans cannot pass')
    violations=[]; reviewed=[];uncovered=[]
    for resource in plan['resource_changes']:
        kind=resource.get('type');address=resource.get('address','unknown')
        change=resource.get('change',{});actions=change.get('actions',[])
        if actions==['delete'] or resource.get('mode')=='data':continue
        if kind not in SUPPORTED:
            uncovered.append(dict(address=address,type=kind));continue
        reviewed.append(address)
        def flag(reason):violations.append(dict(address=address,reason=reason))
        unknown = change.get('after_unknown',{})
        if any(contains_unknown(unknown.get(field,False)) for field in SECURITY_FIELDS[kind]):
            flag('Unresolved planned values require review; cannot assert safety');continue
        after=change.get('after')
        if not isinstance(after,dict):flag('Missing planned resource state');continue
        try:
            if kind=='aws_s3_bucket_public_access_block':
                if not all(after.get(k) is True for k in ('block_public_acls','block_public_policy','ignore_public_acls','restrict_public_buckets')):flag('S3 public-access block incomplete')
            elif kind=='aws_s3_bucket':
                if after.get('force_destroy') is True:flag('Audit/data bucket force_destroy enabled')
            elif kind=='google_storage_bucket':
                if after.get('public_access_prevention')!='enforced' or after.get('uniform_bucket_level_access') is not True:flag('GCS public access protections incomplete')
                if after.get('force_destroy') is True:flag('GCS force_destroy enabled')
            elif kind in ('aws_iam_policy','aws_iam_role_policy'):
                document=json.loads(after['policy']) if isinstance(after.get('policy'),str) else after.get('policy')
                if not isinstance(document,dict):raise ValueError('invalid IAM policy JSON')
                statements=document.get('Statement',[])
                if isinstance(statements,dict):statements=[statements]
                for statement in statements:
                    if statement.get('Effect')!='Allow':continue
                    if 'NotAction' in statement:flag('Allow NotAction requires explicit security review')
                    actions=statement.get('Action',[])
                    if isinstance(actions,str):actions=[actions]
                    if any('*' in x or '?' in x for x in actions):flag('Wildcard Allow action')
            elif kind in ('aws_security_group','aws_vpc_security_group_ingress_rule'):
                rules=after.get('ingress',[]) if kind=='aws_security_group' else [after]
                for rule in rules:
                    sources=rule.get('cidr_blocks',[])+rule.get('ipv6_cidr_blocks',[])+[rule.get('cidr_ipv4'),rule.get('cidr_ipv6')]
                    protocol=str(rule.get('protocol',rule.get('ip_protocol')))
                    if any(public(x) for x in sources) and (protocol=='-1' or protocol in ('tcp','6') and management(rule['from_port'],rule['to_port'])):flag('Public management ingress')
            elif kind in ('azurerm_network_security_rule','azurerm_network_security_group'):
                rules=after.get('security_rule',[]) if kind.endswith('_group') else [after]
                for rule in rules:
                    sources=rule.get('source_address_prefixes') or [rule.get('source_address_prefix')]
                    if rule.get('direction')=='Inbound' and rule.get('access')=='Allow' and rule.get('protocol') in ('*','Tcp','tcp') and any(public(x) for x in sources) and azure_ports(rule):flag('Public Azure management ingress')
            elif kind=='google_compute_firewall':
                if after.get('direction','INGRESS')=='INGRESS' and not after.get('disabled',False) and any(public(x) for x in after.get('source_ranges',[])):
                    for allow in after.get('allow',[]):
                        if allow.get('protocol')=='all':flag('Public all-protocol ingress')
                        elif allow.get('protocol') in ('tcp','6'):
                            ports=allow.get('ports',[])
                            if not ports or any(management(*(int(p.split('-')[0]),int(p.split('-')[-1]))) for p in ports):flag('Public GCP management ingress')
        except (KeyError,ValueError,TypeError) as exc:
            flag('Unsupported or malformed security fields: '+str(exc))
    return dict(status='FAIL' if violations else 'PASS',reviewed=reviewed,uncovered=uncovered,violations=violations,
        scope='Focused structural checks; uncovered resource types need other scanners and human review')
