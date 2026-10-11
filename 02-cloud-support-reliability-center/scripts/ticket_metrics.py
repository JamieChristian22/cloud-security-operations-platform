"""Compatibility entry point for the shared synthetic ticket analytics."""
import subprocess,sys
from pathlib import Path
root=Path(__file__).resolve().parents[2]
raise SystemExit(subprocess.call([sys.executable,str(root/'scripts/operations/ticket_metrics.py'),'--input',str(root/'02-cloud-support-reliability-center/data/tickets.csv'),'--output',str(root/'scripts/reports/support_metrics.json')]))
