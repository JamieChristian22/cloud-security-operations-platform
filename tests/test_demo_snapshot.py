"""Ensure the offline CloudGuardian explorer exactly matches the checked-in synthetic snapshot."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEMO = ROOT / "demo/cloudguardian.html"
REPORT = ROOT / "04-cloudguardian-security-auditor/reports/generated/report.json"


def test_demo_embeds_exact_current_fixture():
    html = DEMO.read_text(encoding="utf-8")
    match = re.search(
        r'<script id="report-data" type="application/json">(.*?)</script>',
        html,
        re.DOTALL,
    )
    assert match, "Missing structured snapshot payload"
    assert json.loads(match.group(1)) == json.loads(REPORT.read_text(encoding="utf-8"))


def test_demo_has_accessible_filters_and_no_external_assets():
    html = DEMO.read_text(encoding="utf-8")
    for field in ("query", "provider", "severity"):
        assert 'for="' + field + '"' in html
        assert 'id="' + field + '"' in html
    assert 'aria-live="polite"' in html
    assert 'textContent=' in html
    assert not re.search(r'<(?:script|link)[^>]+(?:src|href)="https?://', html)
