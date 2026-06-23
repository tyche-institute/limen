#!/usr/bin/env python3
"""Cheap URL/locator extraction for bulk source-review routing rows."""

from __future__ import annotations

import csv
import json
import re
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path


PROJECT_ROOT = Path("/srv/tyche/projects/limen-ai-edge-case-atlas")
REVIEW_ROOT = PROJECT_ROOT / "results" / "review-candidates"
ROUTING = REVIEW_ROOT / "bulk-source-review-routing-v0.1.tsv"
OUT = REVIEW_ROOT / "bulk-named-source-autoresolve-v0.1.tsv"
UNRESOLVED = REVIEW_ROOT / "bulk-named-source-unresolved-queue-v0.1.tsv"
STATUS = REVIEW_ROOT / "bulk-named-source-autoresolve-status.json"
DASHBOARD_COPY = PROJECT_ROOT / "results" / "dashboard" / "bulk-named-source-autoresolve.tsv"

URL_RE = re.compile(r"https?://[^\s,\"'<>]+", re.I)

FIELDS = [
    "signal_id",
    "autoresolve_status",
    "extracted_source_url",
    "evidence_location",
    "source_review_role",
    "review_priority",
    "shards",
    "queries",
    "source_path",
    "source_line",
    "reason",
    "claim_ceiling",
    "next_action",
]


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", errors="replace", newline="") as fh:
        return [{k: v or "" for k, v in row.items() if k is not None} for row in csv.DictReader(fh, delimiter="\t")]


def write_tsv(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=FIELDS, delimiter="\t", extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def first_url(*values: str) -> str:
    for value in values:
        match = URL_RE.search(value or "")
        if match:
            return match.group(0).rstrip(").,;]`")
    return ""


def nearby_context(path_value: str, line_value: str, radius: int = 8) -> tuple[str, str]:
    try:
        path = Path(path_value)
        line_no = int(line_value or "0")
        if not path.exists() or line_no <= 0 or path.stat().st_size > 80_000_000:
            return "", ""
        start = max(1, line_no - radius)
        end = line_no + radius
        parts: list[str] = []
        with path.open("r", encoding="utf-8", errors="replace") as fh:
            for index, line in enumerate(fh, start=1):
                if index > end:
                    break
                if index >= start:
                    parts.append(line.rstrip("\n"))
        return "\n".join(parts), f"{path}:{start}-{end}"
    except Exception:
        return "", ""


def resolve(row: dict[str, str]) -> tuple[str, str, str]:
    direct = first_url(row.get("reason", ""), row.get("claim_ceiling", ""), row.get("next_action", ""), row.get("source_path", ""))
    if direct:
        return "url_found_in_review_metadata", direct, "bulk-source-review-routing"
    context, location = nearby_context(row.get("source_path", ""), row.get("source_line", ""))
    url = first_url(context)
    if url:
        return "url_found_near_source_line", url, location
    return "unresolved_needs_parent_source_extraction", "", location or row.get("source_path", "")


def build() -> dict[str, object]:
    source_rows = [row for row in read_tsv(ROUTING) if row.get("bulk_route") == "next_named_source_extraction"]
    out_rows: list[dict[str, str]] = []
    for row in source_rows:
        status, url, location = resolve(row)
        out_rows.append(
            {
                "signal_id": row.get("signal_id", ""),
                "autoresolve_status": status,
                "extracted_source_url": url,
                "evidence_location": location,
                "source_review_role": row.get("source_review_role", ""),
                "review_priority": row.get("review_priority", ""),
                "shards": row.get("shards", ""),
                "queries": row.get("queries", ""),
                "source_path": row.get("source_path", ""),
                "source_line": row.get("source_line", ""),
                "reason": row.get("reason", ""),
                "claim_ceiling": row.get("claim_ceiling", ""),
                "next_action": row.get("next_action", ""),
            }
        )
    out_rows.sort(key=lambda row: (row["autoresolve_status"], row["review_priority"], row["signal_id"]))
    unresolved = [row for row in out_rows if row["autoresolve_status"] == "unresolved_needs_parent_source_extraction"]
    write_tsv(OUT, out_rows)
    write_tsv(UNRESOLVED, unresolved)
    write_tsv(DASHBOARD_COPY, out_rows[:250])

    counts = Counter(row["autoresolve_status"] for row in out_rows)
    status = {
        "generated_at_utc": utc_now(),
        "input": str(ROUTING),
        "output": str(OUT),
        "unresolved_queue": str(UNRESOLVED),
        "dashboard_copy": str(DASHBOARD_COPY),
        "input_rows": len(source_rows),
        "resolved_rows": len(out_rows) - len(unresolved),
        "unresolved_rows": len(unresolved),
        "autoresolve_status_counts": dict(sorted(counts.items())),
        "boundary": "Deterministic URL/locator extraction only; no reviewed-core promotion, factual claim, legal finding, safety finding, compliance finding, prevalence, or ranking.",
    }
    STATUS.write_text(json.dumps(status, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(status, indent=2, sort_keys=True))
    return status


def main() -> int:
    build()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
