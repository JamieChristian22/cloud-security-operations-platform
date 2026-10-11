"""Remove reproducible Python caches only; never touch state or evidence."""
from pathlib import Path
import shutil
root=Path(__file__).resolve().parents[2]
for folder in list(root.rglob('__pycache__'))+list(root.rglob('.pytest_cache')):
    if folder.is_dir() and '.venv' not in folder.parts:
        shutil.rmtree(folder)
