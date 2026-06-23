#!/usr/bin/env python3
"""Close obvious LIMEN hardening-review rows from local metadata only."""

from __future__ import annotations

import argparse
import csv
import html
import json
import re
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urljoin, urlparse


PROJECT_ROOT = Path("/srv/tyche/projects/limen-ai-edge-case-atlas")
REVIEW_ROOT = PROJECT_ROOT / "results" / "review-candidates"
QUEUE_ROOT = REVIEW_ROOT / "hardening-review-queues"
BATCH_ROOT = REVIEW_ROOT / "hardening-review-batches"
ROLLUP = REVIEW_ROOT / "hardening-review-rollup-status.json"

URL_QUEUE = QUEUE_ROOT / "named-url-extraction-queue.tsv"
TRANSLATION_QUEUE = QUEUE_ROOT / "translation-source-review-queue.tsv"

URL_FIELDS = [
    "row_id",
    "signal_id",
    "url_extraction_verdict",
    "extracted_source_url",
    "source_name",
    "evidence_location",
    "reason",
    "claim_ceiling",
    "next_action",
]

TRANSLATION_FIELDS = [
    "row_id",
    "signal_id",
    "translation_review_verdict",
    "language_reviewed",
    "source_url_or_locator",
    "source_name",
    "reason",
    "claim_ceiling",
    "next_action",
]


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def stamp() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", errors="replace", newline="") as fh:
        return [{k: v or "" for k, v in row.items() if k is not None} for row in csv.DictReader(fh, delimiter="\t")]


def write_tsv(path: Path, rows: list[dict[str, str]], fields: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, delimiter="\t", fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def write_json(path: Path, payload: dict[str, object]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def clean(value: str) -> str:
    return (value or "").replace("\t", " ").replace("\r", " ").replace("\n", " ").strip()


def missing_ids(task: str) -> set[str]:
    data = json.loads(ROLLUP.read_text(encoding="utf-8"))
    return set(data.get("tasks", {}).get(task, {}).get("missing_row_ids", []))


def full_missing_ids(queue: Path, batch_subdir: str, result_file: str) -> set[str]:
    queue_ids = {row.get("row_id", "") for row in read_tsv(queue) if row.get("row_id", "")}
    done: set[str] = set()
    for result_path in (BATCH_ROOT / batch_subdir).glob(f"*/{result_file}"):
        try:
            done.update(row.get("row_id", "") for row in read_tsv(result_path) if row.get("row_id", ""))
        except Exception:
            continue
    return queue_ids - done


def first_http(*values: str) -> str:
    for value in values:
        match = re.search(r"https?://[^\s<>'\")]+", value or "")
        if match:
            return match.group(0).rstrip(".,;]")
    return ""


def file_context(path: Path, line_number: str, radius: int = 30) -> str:
    try:
        line = int(line_number)
    except Exception:
        line = 0
    try:
        lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
    except Exception:
        return ""
    if line <= 0:
        return "\n".join(lines[:80])
    start = max(0, line - radius - 1)
    end = min(len(lines), line + radius)
    return "\n".join(lines[start:end])


def html_metadata(path: Path) -> tuple[str, str]:
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except Exception:
        return "", ""
    url = ""
    for pattern in [
        r'<link[^>]+rel=["\']canonical["\'][^>]+href=["\']([^"\']+)["\']',
        r'<meta[^>]+property=["\']og:url["\'][^>]+content=["\']([^"\']+)["\']',
        r'"@id"\s*:\s*"([^"]+)"',
    ]:
        match = re.search(pattern, text, flags=re.IGNORECASE)
        if match:
            candidate = html.unescape(match.group(1)).replace("\\/", "/")
            if candidate.startswith(("http://", "https://")):
                url = candidate
                break
    source_name = ""
    site_match = re.search(r'<meta[^>]+property=["\']og:site_name["\'][^>]+content=["\']([^"\']+)["\']', text, flags=re.IGNORECASE)
    if site_match:
        source_name = clean(html.unescape(site_match.group(1)))
    elif url:
        source_name = urlparse(url).netloc
    return url, source_name


def href_from_context(context: str) -> str:
    match = re.search(r'href=["\']([^"\']+)["\']', context or "", flags=re.IGNORECASE)
    return html.unescape(match.group(1)) if match else ""


def resolve_url_row(row: dict[str, str]) -> dict[str, str]:
    source_path = Path(row.get("source_path", ""))
    snippet = row.get("title_or_snippet", "")
    context = file_context(source_path, row.get("source_line", "")) if source_path.exists() else ""
    direct = first_http(snippet, row.get("source_review_reason", ""), context)
    canonical, source_name = html_metadata(source_path) if source_path.suffix.lower() in {".html", ".htm"} else ("", "")
    href = href_from_context(snippet) or href_from_context(context)
    extracted = direct
    reason = "explicit http(s) URL recovered from local row/context"
    if not extracted and canonical:
        if href.startswith(("http://", "https://")):
            extracted = href
            reason = "local HTML context exposes explicit href"
        elif href.startswith("/") or href.startswith("./") or href.startswith("../"):
            extracted = urljoin(canonical, href)
            reason = "local HTML exposes canonical URL plus relative href"
        else:
            extracted = canonical
            reason = "local HTML exposes canonical/og URL"
    if extracted:
        return {
            "row_id": row["row_id"],
            "signal_id": row.get("signal_id", ""),
            "url_extraction_verdict": "url_extracted",
            "extracted_source_url": clean(extracted),
            "source_name": clean(source_name or urlparse(extracted).netloc),
            "evidence_location": f"{row.get('source_path', '')}:{row.get('source_line', '')}",
            "reason": reason,
            "claim_ceiling": clean(row.get("claim_ceiling", "source-surface only")) or "source-surface only",
            "next_action": "source_surface_review_only_no_case_promotion",
        }
    wrapper_paths = ("/reports/", "/config/", "/corpus/", "/data/seeds/", "/program/")
    verdict = "wrapper_needs_parent_source" if any(part in row.get("source_path", "") for part in wrapper_paths) else "source_path_is_snapshot_only"
    return {
        "row_id": row["row_id"],
        "signal_id": row.get("signal_id", ""),
        "url_extraction_verdict": verdict,
        "extracted_source_url": "",
        "source_name": "",
        "evidence_location": f"{row.get('source_path', '')}:{row.get('source_line', '')}",
        "reason": "local row is a wrapper/cache lead; no explicit original public URL recovered locally",
        "claim_ceiling": clean(row.get("claim_ceiling", "source-surface only")) or "source-surface only",
        "next_action": "parent_source_extraction_or_hold",
    }


def resolve_translation_row(row: dict[str, str]) -> dict[str, str]:
    family = row.get("source_path_family", "")
    source_path = row.get("source_path", "")
    hold_class = row.get("translation_hold_class", "")
    source_url = row.get("source_url", "")
    cross_project = (
        hold_class == "cross_project_language_artifact"
        or family in {"cross_project_atlas_or_gaia", "global_agent_atlas", "other_tyche_project", "srv/tyche/pallas"}
        or "/gaia/" in source_path
        or "/pallas/" in source_path
    )
    if cross_project:
        verdict = "cross_project_duplicate"
        reason = "local metadata identifies a derived cross-project language artifact"
        next_action = "route_upstream_or_deduplicate"
    elif source_url:
        verdict = "translation_source_reviewed"
        reason = "local row includes source URL/locator and translation-aware context for bounded source-surface review"
        next_action = "source_surface_review_only_no_case_promotion"
    elif hold_class == "registry_auto_translation":
        verdict = "machine_translation_hold"
        reason = "registry-derived translated summary lacks enough original-language source context"
        next_action = "hold_until_original_language_source"
    else:
        verdict = "needs_original_language_source"
        reason = "plausible foreign-language lead but original-language source URL is missing locally"
        next_action = "recover_original_language_source"
    locator = source_url or f"{source_path}:{row.get('source_line', '')}"
    return {
        "row_id": row["row_id"],
        "signal_id": row.get("signal_id", ""),
        "translation_review_verdict": verdict,
        "language_reviewed": clean(row.get("language_hint", "language_not_resolved")) or "language_not_resolved",
        "source_url_or_locator": clean(locator),
        "source_name": clean(urlparse(source_url).netloc if source_url else family),
        "reason": reason,
        "claim_ceiling": clean(row.get("claim_ceiling", "translation/source-surface only")) or "translation/source-surface only",
        "next_action": next_action,
    }


def write_batch(task: str, queue_rows: list[dict[str, str]], result_rows: list[dict[str, str]], fields: list[str], result_file: str) -> None:
    batch_dir = BATCH_ROOT / task / f"{stamp()}-local-autoresolve"
    batch_dir.mkdir(parents=True, exist_ok=True)
    write_tsv(batch_dir / "input.tsv", queue_rows, list(queue_rows[0].keys()) if queue_rows else [])
    write_tsv(batch_dir / result_file, result_rows, fields)
    verdict_field = "url_extraction_verdict" if task == "named-url-extraction" else "translation_review_verdict"
    counts = Counter(row.get(verdict_field, "") for row in result_rows)
    (batch_dir / f"{task}-summary.md").write_text(
        "\n".join(
            [
                f"# {task} local autoresolve",
                "",
                f"- Batch: `{batch_dir.name}`",
                f"- Rows reviewed: `{len(result_rows)}`",
                f"- Verdict counts: `{json.dumps(dict(sorted(counts.items())), sort_keys=True)}`",
                "- Boundary: local metadata/source-surface hardening only; no incident truth or reviewed-core promotion.",
                "- Next smallest move: rerun hardening rollup and downstream promotion-safety builders.",
                "",
            ]
        ),
        encoding="utf-8",
    )
    write_json(
        batch_dir / "manifest.json",
        {
            "batch_id": batch_dir.name,
            "task": task,
            "status": "complete",
            "created_at_utc": utc_now(),
            "started_at_utc": utc_now(),
            "completed_at_utc": utc_now(),
            "updated_at_utc": utc_now(),
            "input": str(batch_dir / "input.tsv"),
            "input_rows": len(queue_rows),
            "local_autoresolve": True,
            "verdict_counts": dict(sorted(counts.items())),
        },
    )
    print(json.dumps({"task": task, "batch": str(batch_dir), "rows": len(result_rows), "verdict_counts": dict(sorted(counts.items()))}, sort_keys=True))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--task", choices=["all", "url", "translation"], default="all")
    args = parser.parse_args()

    if args.task in {"all", "url"}:
        ids = full_missing_ids(URL_QUEUE, "named-url-extraction", "named-url-extraction-results.tsv") or missing_ids("named-url-extraction")
        rows = [row for row in read_tsv(URL_QUEUE) if row.get("row_id") in ids]
        if rows:
            write_batch("named-url-extraction", rows, [resolve_url_row(row) for row in rows], URL_FIELDS, "named-url-extraction-results.tsv")
        else:
            print(json.dumps({"task": "named-url-extraction", "rows": 0}))

    if args.task in {"all", "translation"}:
        ids = full_missing_ids(TRANSLATION_QUEUE, "translation-source-review", "translation-source-review-results.tsv") or missing_ids("translation-source-review")
        rows = [row for row in read_tsv(TRANSLATION_QUEUE) if row.get("row_id") in ids]
        if rows:
            write_batch("translation-source-review", rows, [resolve_translation_row(row) for row in rows], TRANSLATION_FIELDS, "translation-source-review-results.tsv")
        else:
            print(json.dumps({"task": "translation-source-review", "rows": 0}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
