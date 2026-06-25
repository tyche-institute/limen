#!/usr/bin/env python3
import csv
import sys
from pathlib import Path

crosswalk_path = Path('/srv/tyche/projects/limen-ai-edge-case-atlas/results/crosswalks/legal-normative-crosswalk-v0.1.tsv')

if not crosswalk_path.is_file():
    print("Crosswalk file not found", file=sys.stderr)
    sys.exit(1)

with crosswalk_path.open('r', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter='\\t')
    rows = list(reader)

header = rows[0] if rows else []
print(f"Header columns: {len(header)}")
print(f"Total rows (including header): {len(rows)}")
# Print a sample of the first few rows
for i, row in enumerate(rows[:5]):
    print(f"Row {i}: {row}")