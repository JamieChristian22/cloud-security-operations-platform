#!/usr/bin/env python3
"""Run the repository's complete offline validation and control suite.

The suite is intentionally credential-free. It evaluates deterministic lab data,
repository evidence, detection logic, policy controls, and unit tests so a reviewer
can reproduce the portfolio's claims without access to a cloud account.
"""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

SCRIPTS_ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = SCRIPTS_ROOT.parent
REPORTS = SCRIPTS_ROOT / "reports"
REPORTS.mkdir(parents=True, exist_ok=True)


def run_python(label: str, script: Path, *args: str) -> dict:
    proc = subprocess.run(
        [sys.executable, str(script), *map(str, args)],
        cwd=REPO_ROOT,
        text=True,
        capture_output=True,
    )
    return {
        "name": label,
        "command": " ".join([sys.executable, str(script), *map(str, args)]),
        "returncode": proc.returncode,
        "status": "PASS" if proc.returncode == 0 else "FAIL",
        "stdout": proc.stdout[-5000:],
        "stderr": proc.stderr[-5000:],
    }


def run_command(label: str, command: list[str]) -> dict:
    proc = subprocess.run(command, cwd=REPO_ROOT, text=True, capture_output=True)
    return {
        "name": label,
        "command": " ".join(command),
        "returncode": proc.returncode,
        "status": "PASS" if proc.returncode == 0 else "FAIL",
        "stdout": proc.stdout[-5000:],
        "stderr": proc.stderr[-5000:],
    }


def main() -> int:
    checks = [
        run_python(
            "IAM access review",
            SCRIPTS_ROOT / "iam/access_review.py",
            "--output",
            REPORTS / "iam_access_review.json",
        ),
        run_python(
            "Cloud security baseline",
            SCRIPTS_ROOT / "security/baseline_audit.py",
            "--output",
            REPORTS / "security_baseline.json",
        ),
        run_python(
            "Cost governance guardrails",
            SCRIPTS_ROOT / "finops/cost_guardrails.py",
            "--output",
            REPORTS / "cost_guardrails.json",
        ),
        run_python(
            "Disaster recovery readiness",
            SCRIPTS_ROOT / "dr/readiness_check.py",
            "--output",
            REPORTS / "dr_readiness.json",
        ),
        run_python(
            "Support ticket analytics",
            SCRIPTS_ROOT / "operations/ticket_metrics.py",
            "--input",
            REPO_ROOT / "02-cloud-support-reliability-center/data/tickets.csv",
            "--output",
            REPORTS / "support_metrics.json",
        ),
        run_python(
            "Security detection suite",
            SCRIPTS_ROOT / "security/run_detections.py",
            "--repo",
            REPO_ROOT,
            "--output",
            REPORTS / "detection_results.json",
        ),
        run_python(
            "DevSecOps policy gate",
            REPO_ROOT / "05-devsecops-infrastructure-delivery/policy/policy_check.py",
            REPO_ROOT / "05-devsecops-infrastructure-delivery/policy/sample_proposed_change.json",
        ),
        run_command(
            "CloudGuardian unit tests",
            [
                sys.executable,
                "-m",
                "pytest",
                "04-cloudguardian-security-auditor/tests",
                "-q",
            ],
        ),
        run_command(
            "Automation control tests",
            [sys.executable, "-m", "pytest", "scripts/tests", "-q"],
        ),
        run_python(
            "Portfolio completeness validation",
            SCRIPTS_ROOT / "automation/portfolio_validate.py",
            "--repo",
            REPO_ROOT,
            "--output",
            REPORTS / "portfolio_validation.json",
        ),
    ]

    passed = sum(c["status"] == "PASS" for c in checks)
    summary = {
        "suite": "Cloud Security & Operations Platform offline validation",
        "repo": str(REPO_ROOT),
        "passed": passed,
        "total": len(checks),
        "status": "PASS" if passed == len(checks) else "FAIL",
        "checks": checks,
    }
    output = REPORTS / "automation_summary.json"
    output.write_text(json.dumps(summary, indent=2))

    print("CLOUD SECURITY & OPERATIONS PLATFORM — VALIDATION SUITE")
    print("=" * 62)
    for check in checks:
        print(f"{check['status']:4}  {check['name']}")
    print("-" * 62)
    print(f"Result: {passed}/{len(checks)} checks passed")
    print(f"Report: {output.relative_to(REPO_ROOT)}")
    return 0 if summary["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
