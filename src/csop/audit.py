"""Deterministic inventory assessment with auditable, expiring exceptions."""
import hashlib
import ipaddress
from datetime import datetime, timezone
from .inventory import validate, port_range

WEIGHTS = {'Critical': 25, 'High': 15, 'Medium': 7, 'Low': 2}
CONTROLS = {
 'CG-001': ('MFA', 'High', 'Require workforce MFA and verify registration.'),
 'CG-002': ('Dormant account', 'Medium', 'Confirm ownership and disable unneeded identities.'),
 'CG-003': ('Credential age', 'High', 'Rotate or revoke; prefer short-lived workload identity.'),
 'CG-004': ('Least privilege', 'Critical', 'Replace unrestricted actions with approved task scope.'),
 'CG-005': ('Public storage', 'Critical', 'Remove public access or obtain a time-limited exception.'),
 'CG-006': ('Management exposure', 'Critical', 'Use managed sessions or approved private access.'),
 'CG-007': ('Tagging', 'Low', 'Populate Environment and Owner with accountable values.'),
 'CG-008': ('Storage encryption', 'High', 'Enable encryption and validate the effective configuration.'),
}


def utc(value):
    dt = datetime.fromisoformat(value.replace('Z', '+00:00'))
    if dt.tzinfo is None:
        raise ValueError('timestamp must include a timezone')
    return dt.astimezone(timezone.utc)


def scan(data):
    validate(data)
    findings = []
    def add(code, item, evidence, severity=None):
        control, default_severity, remediation = CONTROLS[code]
        resource = item.get('id', item.get('name'))
        provider = item.get('provider', 'unspecified')
        fingerprint = hashlib.sha256(f'{code}|{provider}|{resource}'.encode()).hexdigest()[:20]
        findings.append(dict(id=fingerprint, control_id=code, control=control,
            severity=severity or default_severity, provider=provider, resource=resource,
            evidence=evidence, remediation=remediation, status='open',
            mapping='Educational control mapping; see docs/CONTROL-CATALOG.md'))
    for user in data['users']:
        if user['enabled'] and not user['mfa']:
            add('CG-001', user, 'Enabled account has MFA disabled')
        if user['enabled'] and user['days_inactive'] >= 45:
            add('CG-002', user, f"Inactive for {user['days_inactive']} days", 'High' if user.get('privileged') else None)
    for key in data['keys']:
        if key['active'] and key['age_days'] > 90:
            add('CG-003', key, f"Active key age: {key['age_days']} days")
    for policy in data['policies']:
        broad = [a for a in policy['actions'] if '*' in a or '?' in a]
        if broad:
            add('CG-004', policy, 'Wildcard actions: ' + ', '.join(broad), 'Critical' if '*' in broad else 'High')
    for storage in data['storage']:
        if storage['public']:
            add('CG-005', storage, 'Public access enabled')
        if not storage['encrypted']:
            add('CG-008', storage, 'Encryption disabled')
    for rule in data['firewall_rules']:
        network = ipaddress.ip_network(rule['source'], strict=False)
        start, end = port_range(rule)
        ports = [p for p in (22,3389) if start <= p <= end]
        if network.prefixlen == 0 and ports and rule.get('protocol', 'tcp') in ('tcp','all'):
            add('CG-006', rule, f"World exposure {network}; management ports {ports}")
    for resource in data['resources']:
        missing = [tag for tag in ('Environment','Owner') if not resource['tags'].get(tag,'').strip()]
        if missing:
            add('CG-007', resource, 'Missing or empty tags: ' + ', '.join(missing))
    return sorted(findings, key=lambda f: (-WEIGHTS[f['severity']], f['id']))


def apply_exceptions(findings, exceptions, now=None):
    """Keep excepted findings visible. Invalid/expired approvals fail closed."""
    now = now or datetime.now(timezone.utc)
    if not isinstance(exceptions, list):
        raise ValueError('exceptions must be an array')
    indexed = {}
    for approval in exceptions:
        if not isinstance(approval, dict):
            raise ValueError('exception must be an object')
        required = ('finding_id','owner','reason','ticket','expires_at')
        if any(not isinstance(approval.get(k),str) or not approval[k].strip() for k in required):
            raise ValueError('exception requires finding_id, owner, reason, ticket, expires_at')
        if utc(approval['expires_at']) <= now:
            raise ValueError(f"Expired exception: {approval['ticket']}")
        if approval['finding_id'] in indexed:
            raise ValueError('Duplicate exception finding_id')
        indexed[approval['finding_id']] = approval
    result = []
    for finding in findings:
        finding = dict(finding)
        if finding['id'] in indexed:
            finding['status'] = 'accepted_risk'
            finding['exception'] = indexed[finding['id']]
        result.append(finding)
    unknown = set(indexed) - {f['id'] for f in findings}
    if unknown:
        raise ValueError('Exception references a finding absent from this assessment')
    return result


def gate(findings, threshold):
    if threshold == 'none':
        return False
    minimum = WEIGHTS[threshold.capitalize()]
    return any(f['status'] == 'open' and WEIGHTS[f['severity']] >= minimum for f in findings)
