"""Collect read-only EC2 ingress rules for one explicit region. No auto-discovery."""
import argparse,json,sys
from datetime import datetime,timezone
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[2]/'src'))
from csop.inventory import SECTIONS,validate


def normalize_groups(groups):
    data={section:[] for section in SECTIONS}
    for group in groups:
        group_id=group['GroupId']
        data['resources'].append(dict(id=group_id,provider='aws',tags={t['Key']:t['Value'] for t in group.get('Tags',[])}))
        for index,permission in enumerate(group.get('IpPermissions',[])):
            protocol=str(permission['IpProtocol'])
            if protocol not in ('tcp','6','-1'):continue
            start,end=(0,65535) if protocol=='-1' else (permission['FromPort'],permission['ToPort'])
            sources=[r['CidrIp'] for r in permission.get('IpRanges',[])]+[r['CidrIpv6'] for r in permission.get('Ipv6Ranges',[])]
            for source in sources:
                data['firewall_rules'].append(dict(name=f'{group_id}:{index}:{source}',source=source,from_port=start,to_port=end,protocol='all' if protocol=='-1' else 'tcp',provider='aws'))
    validate(data)
    return data


def main():
    p=argparse.ArgumentParser(description=__doc__)
    source=p.add_mutually_exclusive_group(required=True)
    source.add_argument('--snapshot',help='AWS CLI describe-security-groups JSON export')
    source.add_argument('--region',help='Explicit AWS region for a live read-only collection')
    p.add_argument('--profile');p.add_argument('--output',required=True);a=p.parse_args()
    try:
        if a.snapshot:
            payload=json.loads(Path(a.snapshot).read_text());groups=payload['SecurityGroups'];scope={'source':'snapshot','file':Path(a.snapshot).name}
        else:
            import boto3
            from botocore.config import Config
            session=boto3.Session(profile_name=a.profile,region_name=a.region)
            config=Config(retries={'max_attempts':5,'mode':'standard'},connect_timeout=10,read_timeout=30)
            identity=session.client('sts',config=config).get_caller_identity()
            ec2=session.client('ec2',config=config)
            groups=[g for page in ec2.get_paginator('describe_security_groups').paginate() for g in page['SecurityGroups']]
            scope={'source':'live-read-only','region':a.region,'account':identity['Account']}
        result=normalize_groups(groups)
        result['metadata']={'collected_at':datetime.now(timezone.utc).isoformat(),'scope':scope,
            'covered':['EC2 TCP/all-protocol CIDR ingress','security-group ownership tags'],
            'not_collected':['IAM','S3','Azure','GCP','prefix lists','referenced security groups','NACLs','routes','effective end-to-end reachability']}
        output=Path(a.output);output.parent.mkdir(parents=True,exist_ok=True);output.write_text(json.dumps(result,indent=2)+'\n')
        print(f'Collected {len(groups)} security groups to {output}')
        return 0
    except Exception as exc:
        print(f'COLLECTION FAILED: {type(exc).__name__}: {exc}',file=sys.stderr);return 2
if __name__=='__main__':raise SystemExit(main())
