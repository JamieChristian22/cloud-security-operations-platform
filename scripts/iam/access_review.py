#!/usr/bin/env python3
import argparse, json, csv
from pathlib import Path


def review(users):
    findings = []
    for u in users:
        if u["status"] == "active" and not u["mfa"]:
            findings.append({"severity":"HIGH","user":u["user"],"control":"MFA","finding":"Active account without MFA","remediation":"Require MFA before continued access."})
        if u["status"] == "active" and u["last_login_days"] > 60:
            findings.append({"severity":"MEDIUM","user":u["user"],"control":"Dormant account","finding":f"No login for {u['last_login_days']} days","remediation":"Confirm business need; disable or remove unused access."})
        if u["access_key_age_days"] > 90:
            findings.append({"severity":"HIGH","user":u["user"],"control":"Credential age","finding":f"Access key age is {u['access_key_age_days']} days","remediation":"Rotate the access key and document owner validation."})
        if u["privileged"] and not u["mfa"]:
            findings.append({"severity":"CRITICAL","user":u["user"],"control":"Privileged MFA","finding":"Privileged account lacks MFA","remediation":"Block privileged access until phishing-resistant MFA is enrolled."})
    return findings


def main():
    p=argparse.ArgumentParser(description="Perform an IAM access review against a JSON inventory.")
    p.add_argument("--input", default=str(Path(__file__).parents[1]/"sample_data/iam_users.json"))
    p.add_argument("--output", default=str(Path(__file__).parents[1]/"reports/iam_access_review.json"))
    args=p.parse_args()
    users=json.loads(Path(args.input).read_text())
    findings=review(users)
    result={"users_reviewed":len(users),"findings":findings,"finding_count":len(findings),"status":"PASS" if not any(f["severity"] in {"CRITICAL","HIGH"} for f in findings) else "REVIEW_REQUIRED"}
    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    Path(args.output).write_text(json.dumps(result,indent=2))
    print(json.dumps(result,indent=2))
    return 0

if __name__=="__main__": raise SystemExit(main())
