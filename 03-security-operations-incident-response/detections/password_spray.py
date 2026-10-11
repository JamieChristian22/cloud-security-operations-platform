"""Run a detection against JSONL; --assert-alert is a lab expectation check."""
import argparse,json,sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[2]/'src'))
from csop.detections import password_spray
def main():
 p=argparse.ArgumentParser();p.add_argument('--input',default=str(Path(__file__).resolve().parents[1]/'evidence'/'signin_events.jsonl'));p.add_argument('--assert-alert',action='store_true');a=p.parse_args()
 try:
  events=[json.loads(x) for x in Path(a.input).read_text().splitlines() if x.strip()]
  alerts=password_spray(events)
 except (ValueError,OSError,TypeError) as e:
  print(str(e),file=sys.stderr);return 2
 print(json.dumps(alerts,indent=2));return 1 if a.assert_alert and not alerts else 0
if __name__=='__main__':raise SystemExit(main())
