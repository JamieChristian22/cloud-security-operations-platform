"""Strict validation of normalized inventory. Missing evidence is never clean."""
import ipaddress

SECTIONS = ('users', 'keys', 'policies', 'storage', 'firewall_rules', 'resources')
REQUIRED = {
    'users': {'name': str, 'enabled': bool, 'mfa': bool, 'days_inactive': int},
    'keys': {'id': str, 'active': bool, 'age_days': int},
    'policies': {'name': str, 'actions': list},
    'storage': {'name': str, 'public': bool, 'encrypted': bool},
    'firewall_rules': {'name': str, 'source': str},
    'resources': {'id': str, 'tags': dict},
}


def port_range(rule):
    if 'port' in rule:
        start = end = rule['port']
    else:
        start, end = rule.get('from_port'), rule.get('to_port')
    if type(start) is not int or type(end) is not int or not 0 <= start <= end <= 65535:
        raise ValueError('port or inclusive from_port/to_port must be integers in 0..65535')
    return start, end


def validate(data):
    if not isinstance(data, dict):
        raise ValueError('inventory must be an object')
    for section in SECTIONS:
        if section not in data or not isinstance(data[section], list):
            raise ValueError(f'{section}: required array missing or invalid')
        ids = set()
        for index, item in enumerate(data[section]):
            label = f'{section}[{index}]'
            if not isinstance(item, dict):
                raise ValueError(f'{label}: expected object')
            for key, kind in REQUIRED[section].items():
                value = item.get(key)
                if type(value) is not kind or (kind is str and not value.strip()):
                    raise ValueError(f'{label}.{key}: expected nonempty {kind.__name__}')
            for field in ('days_inactive', 'age_days'):
                if field in item and item[field] < 0:
                    raise ValueError(f'{label}.{field}: cannot be negative')
            identity = (item.get('provider', 'unspecified'), item.get('id', item.get('name')))
            if identity in ids:
                raise ValueError(f'{label}: duplicate provider/resource identity')
            ids.add(identity)
            if 'provider' in item and (not isinstance(item['provider'], str) or not item['provider'].strip()):
                raise ValueError(f'{label}.provider: expected nonempty string')
            if 'privileged' in item and type(item['privileged']) is not bool:
                raise ValueError(f'{label}.privileged: expected boolean')
            if section == 'policies':
                if not item['actions'] or any(not isinstance(a, str) or not a.strip() for a in item['actions']):
                    raise ValueError(f'{label}.actions: nonempty string array required')
            if section == 'firewall_rules':
                ipaddress.ip_network(item['source'], strict=False)
                port_range(item)
                if item.get('protocol', 'tcp') not in ('tcp', 'udp', 'all'):
                    raise ValueError(f'{label}.protocol: tcp, udp or all required')
            if section == 'resources' and any(not isinstance(k, str) or not isinstance(v, str) for k,v in item['tags'].items()):
                raise ValueError(f'{label}.tags: string values required')
    return data
