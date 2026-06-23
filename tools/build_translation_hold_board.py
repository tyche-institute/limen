#!/usr/bin/env python3
"""Build an explicit board for translation-sensitive LIMEN review holds.

This board does not translate, promote, or fact-claim the rows. It makes the
human-translation backlog observable so the public snapshot can show the full
review state without treating machine-translated or cross-project artifacts as
reviewed cases.
"""

from __future__ import annotations

import csv
import json
import re
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path


PROJECT_ROOT = Path("/srv/tyche/projects/limen-ai-edge-case-atlas")
REVIEW_ROOT = PROJECT_ROOT / "results" / "review-candidates"
INPUT = REVIEW_ROOT / "full-first-pass-review.tsv"
OUT = REVIEW_ROOT / "translation-held-review-board-v0.1.tsv"
TOP_OUT = REVIEW_ROOT / "translation-held-review-top50-v0.1.tsv"
STATUS = REVIEW_ROOT / "translation-held-review-status.json"
SUMMARY = REVIEW_ROOT / "translation-held-review-summary-v0.1.md"
DASHBOARD_COPY = PROJECT_ROOT / "results" / "dashboard" / "translation-held-review-board.tsv"

URL_RE = re.compile(r"https?://[^\s,\"'<>]+", re.I)
SELF_ECHO_SOURCE_MARKERS = [
    "/limen-ai-edge-case-atlas/results/dashboard/",
    "/limen-ai-edge-case-atlas/results/review-candidates/",
]

FIELDS = [
    "row_id",
    "signal_id",
    "translation_hold_class",
    "review_priority",
    "shards",
    "queries",
    "language_hint",
    "source_path_family",
    "source_url",
    "source_path",
    "source_line",
    "title_or_snippet",
    "claim_ceiling",
    "next_action",
    "forbidden_overread",
]

LANGUAGE_HINTS = [
    ("japanese", ["japanese", "japan", r"[\u3040-\u30ff]"]),
    ("korean", ["korean", "korea", r"[\uac00-\ud7af]"]),
    ("chinese", ["chinese", "china", r"[\u4e00-\u9fff]"]),
    ("arabic", ["arabic", r"[\u0600-\u06ff]"]),
    ("russian", ["russian", "russia", r"[\u0400-\u04ff]"]),
    ("spanish", ["spanish", "espanol"]),
    ("french", ["french", "france", "francais"]),
    ("german", ["german", "deutsch"]),
    ("estonian", ["estonian", "estonia"]),
    ("finnish", ["finnish", "finland"]),
    ("norwegian", ["norwegian", "norway"]),
    ("dutch", ["dutch", "netherlands"]),
    ("italian", ["italian", "italy"]),
    ("portuguese", ["portuguese", "brazil", "portugal"]),
]


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def clean_cell(value: str, limit: int | None = None) -> str:
    text = re.sub(r"\s+", " ", value or "").strip().replace("\t", " ")
    if limit is not None:
        return text[:limit].rstrip()
    return text


def read_tsv(path: Path) -> list[dict[str, str]]:
    try:
        with path.open("r", encoding="utf-8", errors="replace", newline="") as fh:
            return [{k: v or "" for k, v in row.items() if k is not None} for row in csv.DictReader(fh, delimiter="\t")]
    except Exception:
        return []


def first_url(*values: str) -> str:
    for value in values:
        match = URL_RE.search(value or "")
        if match:
            return match.group(0).rstrip(").,;]`")
    return ""


def path_family(path_value: str) -> str:
    path = path_value or ""
    lowered = path.lower()
    if "/limen-ai-edge-case-atlas/results/multilingual/" in lowered:
        return "limen_multilingual_results"
    if "/limen-ai-edge-case-atlas/" in lowered:
        return "limen_project"
    if "/tyche-thesis-atlas-factory/" in lowered:
        return "thesis_atlas_factory"
    if "/eu-agent-atlas" in lowered:
        return "eu_agent_atlas"
    if "/global-agent-atlas" in lowered:
        return "global_agent_atlas"
    if "/gaia/" in lowered or "/atlas/" in lowered:
        return "cross_project_atlas_or_gaia"
    if "/srv/tyche/projects/" in lowered:
        return "other_tyche_project"
    if "/corpus/" in lowered:
        return "corpus_artifact"
    parts = [part for part in Path(path).parts if part not in {"", "/"}]
    if len(parts) >= 3:
        return "/".join(parts[:3])
    return path[:80] or "unknown_path"


def language_hint(text: str) -> str:
    lowered = text.lower()
    hits: list[str] = []
    for label, needles in LANGUAGE_HINTS:
        for needle in needles:
            if needle.startswith("["):
                if re.search(needle, text):
                    hits.append(label)
                    break
            elif needle in lowered:
                hits.append(label)
                break
    return ";".join(dict.fromkeys(hits)) or "language_not_resolved"


def hold_class(row: dict[str, str]) -> str:
    text = " ".join([row.get("snippet", ""), row.get("source_path", ""), row.get("queries", "")]).lower()
    path = row.get("source_path", "").lower()
    if "/limen-ai-edge-case-atlas/results/multilingual/" in path or "multilingual-weird-case" in path:
        return "existing_multilingual_package_row"
    if any(token in path for token in ["tyche-thesis-atlas-factory", "/gaia/", "/atlas/", "eu-agent-atlas", "global-agent-atlas"]):
        return "cross_project_language_artifact"
    if any(token in text for token in ["machine translation", "auto translation", "auto-translation", "translated gloss", "translation_status"]):
        return "registry_auto_translation"
    if any(
        token in text
        for token in [
            "official",
            "regulator",
            "authority",
            "ministry",
            "court",
            "tribunal",
            "gazette",
            "register",
            "registry",
            "procurement",
            "public sector",
            "government",
        ]
    ):
        return "foreign_language_official_or_public_surface"
    return "translation_sensitive_lead"


def is_self_echo_source(row: dict[str, str]) -> bool:
    path = row.get("source_path", "").lower()
    return any(marker in path for marker in SELF_ECHO_SOURCE_MARKERS)


def priority_rank(priority: str) -> int:
    if priority.startswith("P1"):
        return 0
    if priority.startswith("P2"):
        return 1
    return 2


def build() -> dict[str, object]:
    source_candidates = [row for row in read_tsv(INPUT) if row.get("first_pass_verdict") == "hold_needs_human_translation"]
    source_rows = [row for row in source_candidates if not is_self_echo_source(row)]
    self_echo_rows = len(source_candidates) - len(source_rows)
    out_rows: list[dict[str, str]] = []
    for index, row in enumerate(source_rows, start=1):
        text = " ".join([row.get("snippet", ""), row.get("source_path", ""), row.get("queries", ""), row.get("review_reason", "")])
        out_rows.append(
            {
                "row_id": f"TH-{index:05d}",
                "signal_id": row.get("signal_id", ""),
                "translation_hold_class": hold_class(row),
                "review_priority": row.get("review_priority", ""),
                "shards": row.get("shards", ""),
                "queries": row.get("queries", ""),
                "language_hint": language_hint(text),
                "source_path_family": path_family(row.get("source_path", "")),
                "source_url": first_url(row.get("snippet", ""), row.get("source_path", "")),
                "source_path": row.get("source_path", ""),
                "source_line": row.get("source_line", ""),
                "title_or_snippet": clean_cell(row.get("snippet", ""), 420),
                "claim_ceiling": clean_cell(row.get("claim_ceiling", ""), 260),
                "next_action": clean_cell(row.get("next_action", ""), 260),
                "forbidden_overread": "Do not promote, translate by guess, infer legality, or count as reviewed-core until human translation/source review is complete.",
            }
        )

    out_rows.sort(key=lambda row: (priority_rank(row["review_priority"]), row["translation_hold_class"], row["shards"], row["signal_id"]))

    OUT.parent.mkdir(parents=True, exist_ok=True)
    DASHBOARD_COPY.parent.mkdir(parents=True, exist_ok=True)
    for path, rows in [(OUT, out_rows), (TOP_OUT, out_rows[:50]), (DASHBOARD_COPY, out_rows[:200])]:
        with path.open("w", encoding="utf-8", newline="") as fh:
            writer = csv.DictWriter(fh, fieldnames=FIELDS, delimiter="\t", extrasaction="ignore")
            writer.writeheader()
            writer.writerows(rows)

    class_counts = Counter(row["translation_hold_class"] for row in out_rows)
    priority_counts = Counter(row["review_priority"] for row in out_rows)
    shard_counts = Counter(row["shards"] or "unknown_shard" for row in out_rows)
    language_counts = Counter()
    for row in out_rows:
        for lang in row["language_hint"].split(";"):
            language_counts[lang or "language_not_resolved"] += 1
    path_family_counts = Counter(row["source_path_family"] for row in out_rows)
    with_url = sum(1 for row in out_rows if row["source_url"])
    status = {
        "generated_at_utc": utc_now(),
        "input": str(INPUT),
        "output": str(OUT),
        "top_output": str(TOP_OUT),
        "dashboard_copy": str(DASHBOARD_COPY),
        "translation_hold_rows": len(out_rows),
        "self_echo_rows_excluded": self_echo_rows,
        "with_named_url_rows": with_url,
        "without_named_url_rows": len(out_rows) - with_url,
        "translation_hold_class_counts": dict(class_counts),
        "review_priority_counts": dict(priority_counts),
        "shard_counts": dict(shard_counts),
        "language_hint_counts": dict(language_counts),
        "source_path_family_counts": dict(path_family_counts.most_common(20)),
        "boundary": "Translation hold only; rows need human translation-aware source review before promotion, factual claims, legal claims, or reviewed-core inclusion.",
    }
    STATUS.write_text(json.dumps(status, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    SUMMARY.write_text(
        "\n".join(
            [
                "# LIMEN translation-held review board",
                "",
                f"- Generated: {status['generated_at_utc']}",
                f"- Translation-held rows: {status['translation_hold_rows']}",
                f"- Self-echo rows excluded: {status['self_echo_rows_excluded']}",
                f"- Rows with named URLs: {status['with_named_url_rows']}",
                f"- Rows without named URLs: {status['without_named_url_rows']}",
                f"- Class counts: {json.dumps(status['translation_hold_class_counts'], sort_keys=True)}",
                f"- Priority counts: {json.dumps(status['review_priority_counts'], sort_keys=True)}",
                "",
                status["boundary"],
                "",
            ]
        ),
        encoding="utf-8",
    )
    return status


def main() -> int:
    status = build()
    print(json.dumps(status, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
