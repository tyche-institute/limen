#!/usr/bin/env python3
"""Compute raw agreement for the LIMEN second-coder worksheet."""

from __future__ import annotations

import csv
import sys
from pathlib import Path


FIELDS = [
    "evidence_tier_code",
    "source_family_code",
    "primary_category_code",
    "claim_ceiling_code",
]


def read_tsv(path: Path) -> dict[str, dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as f:
        return {row["public_id"]: row for row in csv.DictReader(f, delimiter="\t")}


def main() -> int:
    here = Path(__file__).resolve().parent
    key_path = here / "first-coder-answer-key.tsv"
    worksheet_path = Path(sys.argv[1]) if len(sys.argv) > 1 else here / "second-coder-worksheet.tsv"
    key = read_tsv(key_path)
    worksheet = read_tsv(worksheet_path)
    rows = [pid for pid in key if pid in worksheet]
    if not rows:
        print("No overlapping public_id rows found.")
        return 1
    print("field\tcoded_rows\tagreements\traw_agreement")
    for field in FIELDS:
        coded = []
        for pid in rows:
            second = worksheet[pid].get(field, "").strip()
            first = key[pid].get(field, "").strip()
            if second:
                coded.append((first, second))
        agreements = sum(1 for first, second in coded if first == second)
        rate = agreements / len(coded) if coded else 0
        print(f"{field}\t{len(coded)}\t{agreements}\t{rate:.3f}")
    print()
    print("disagreements")
    print("public_id\tfield\tfirst_coder\tsecond_coder")
    for pid in rows:
        for field in FIELDS:
            second = worksheet[pid].get(field, "").strip()
            first = key[pid].get(field, "").strip()
            if second and first != second:
                print(f"{pid}\t{field}\t{first}\t{second}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
