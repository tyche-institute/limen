#!/usr/bin/env python3
"""Build a bounded reviewed-core / ObscureAI promotion packet.

This script does not promote anything. It gathers the source-linked outputs
from the first direct-source and bulk follow-up layers, deduplicates them
against the existing reviewed core, and assigns a conservative posture for
human case hardening.
"""

from __future__ import annotations

import csv
import hashlib
import json
import re
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlsplit, urlunsplit


PROJECT_ROOT = Path("/srv/tyche/projects/limen-ai-edge-case-atlas")
REVIEW_ROOT = PROJECT_ROOT / "results" / "review-candidates"
SECURITY_ROOT = PROJECT_ROOT / "results" / "security"

HARDENING = REVIEW_ROOT / "source-reviewed-promotion-hardening-v0.1.tsv"
TRANSLATION_RESULTS = REVIEW_ROOT / "translation-source-review-results-v0.1.tsv"
TRANSLATION_BOARD = REVIEW_ROOT / "translation-held-review-board-v0.1.tsv"
BULK_PARENT_RESULTS = REVIEW_ROOT / "bulk-parent-source-extraction-results-v0.1.tsv"
BULK_NAMED_SOURCE_AUTORESOLVE = REVIEW_ROOT / "bulk-named-source-autoresolve-v0.1.tsv"
BULK_TRANSLATION_RESULTS = REVIEW_ROOT / "bulk-translation-review-results-v0.1.tsv"
BULK_TRANSLATION_PARENT_RESULTS = REVIEW_ROOT / "bulk-translation-parent-source-extraction-results-v0.1.tsv"
ROUTING_STATUS = REVIEW_ROOT / "bulk-source-review-routing-status.json"

OUT = REVIEW_ROOT / "reviewed-core-promotion-packet-v0.1.tsv"
SUMMARY = REVIEW_ROOT / "reviewed-core-promotion-packet-summary-v0.1.md"
STATUS = REVIEW_ROOT / "reviewed-core-promotion-packet-status.json"
DASHBOARD_COPY = PROJECT_ROOT / "results" / "dashboard" / "reviewed-core-promotion-packet.tsv"
CASE_QUEUE = REVIEW_ROOT / "reviewed-core-case-hardening-queue-v0.1.tsv"
CASE_QUEUE_DASHBOARD_COPY = PROJECT_ROOT / "results" / "dashboard" / "reviewed-core-case-hardening-queue.tsv"

CORE_TABLES = [
    SECURITY_ROOT / "security-agentic-watch-v0.1.tsv",
    SECURITY_ROOT / "limen-reviewed-core-extension-v0.1.tsv",
    SECURITY_ROOT / "limen-reviewed-core-web-verified-v0.1.tsv",
    *sorted(SECURITY_ROOT.glob("limen-reviewed-core-web-verified-batch*-v0.1.tsv")),
]

FIELDS = [
    "packet_id",
    "source_lane",
    "signal_id",
    "queue_id",
    "review_status",
    "promotion_readiness",
    "reviewed_core_posture",
    "obscure_ai_posture",
    "dedupe_status",
    "source_cluster_key",
    "cluster_size",
    "source_url_or_locator",
    "normalized_source_url",
    "source_host",
    "source_name",
    "language_reviewed",
    "review_priority",
    "shards",
    "queries",
    "hardening_gate",
    "hardening_priority",
    "source_path",
    "source_line",
    "title_or_snippet",
    "claim_ceiling",
    "next_action",
    "required_before_reviewed_core",
    "required_before_obscure_ai",
    "forbidden_overread",
]

CASE_QUEUE_FIELDS = [
    "cluster_id",
    "source_cluster_key",
    "candidate_packet_rows",
    "signal_ids",
    "source_lanes",
    "source_url_or_locator",
    "normalized_source_url",
    "source_host",
    "source_name",
    "queries",
    "case_hardening_status",
    "case_claim_ceiling_candidate",
    "required_before_reviewed_core",
    "required_before_obscure_ai",
    "boundary",
]

CASE_HINTS = [
    "incident",
    "breach",
    "exploit",
    "vulnerab",
    "deepfake",
    "synthetic media",
    "complaint",
    "enforcement",
    "fine",
    "penalt",
    "sanction",
    "ruling",
    "judgment",
    "lawsuit",
    "fraud",
    "scam",
    "impersonat",
    "hallucinat",
    "fabricat",
    "cve-",
    "sues",
    "orders",
    "ban",
    "leak",
]

SURFACE_HINTS = [
    "source posture only",
    "source-surface",
    "source surface",
    "context only",
    "source-context",
    "strategy",
    "sandbox",
    "register",
    "registry",
    "framework",
    "portal",
    "index",
    "guidance",
    "policy",
    "roadmap",
    "procurement",
    "no legal",
    "no compliance",
    "no safety",
    "no prevalence",
    "no ranking",
    "no reviewed-core",
    "no incident",
    "no operational",
    "no deployment",
    "no case",
    "parent-source",
    "wrapper",
]

READY_BLOCKERS = [
    "no legal",
    "no compliance",
    "no safety",
    "no prevalence",
    "no reviewed-core",
    "no incident",
    "no deployment",
    "no case",
    "source posture only",
    "source-surface",
    "context only",
    "source-context",
]


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def read_json(path: Path, default: object) -> object:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return default


def read_tsv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8", errors="replace", newline="") as fh:
        return [{k: v or "" for k, v in row.items() if k is not None} for row in csv.DictReader(fh, delimiter="\t")]


def write_tsv(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=FIELDS, delimiter="\t", extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def write_tsv_with_fields(path: Path, rows: list[dict[str, str]], fields: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fields, delimiter="\t", extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def clean(value: str, limit: int = 520) -> str:
    return re.sub(r"\s+", " ", value or "").strip().replace("\t", " ")[:limit].rstrip()


def extract_urls(value: str) -> list[str]:
    urls = []
    for match in re.findall(r"https?://[^\s;|]+", value or ""):
        urls.append(match.rstrip(".,)]}\"'"))
    return urls


def normalize_url(value: str) -> str:
    urls = extract_urls(value)
    if not urls:
        return ""
    raw = urls[0]
    try:
        parsed = urlsplit(raw)
    except Exception:
        return clean(raw.lower().rstrip("/"), 500)
    host = parsed.netloc.lower()
    if host.startswith("www."):
        host = host[4:]
    path = re.sub(r"/+", "/", parsed.path or "").rstrip("/")
    query = parsed.query
    scheme = parsed.scheme.lower()
    if scheme in {"http", "https"}:
        scheme = "https"
    return urlunsplit((scheme, host, path, query, ""))


def source_host(value: str) -> str:
    url = normalize_url(value)
    if not url:
        return ""
    try:
        return urlsplit(url).netloc.lower()
    except Exception:
        return ""


def stable_cluster_key(url_or_locator: str, source_name: str, fallback: str) -> str:
    normalized = normalize_url(url_or_locator)
    if normalized:
        return normalized
    locator = clean(url_or_locator, 500).lower()
    if locator:
        return locator
    name = clean(source_name, 240).lower()
    if name:
        return "name:" + name
    return "missing:" + hashlib.sha1(clean(fallback, 500).encode("utf-8", errors="ignore")).hexdigest()[:16]


def text_blob(row: dict[str, str]) -> str:
    return " ".join(
        clean(row.get(key, ""), 1000)
        for key in [
            "source_name",
            "source_url_or_locator",
            "extracted_source_url",
            "reason",
            "claim_ceiling",
            "next_action",
            "title_or_snippet",
            "queries",
            "source_path",
            "source_review_reason",
            "required_hardening_step",
        ]
    ).lower()


def count_hits(text: str, hints: list[str]) -> int:
    return sum(1 for hint in hints if hint in text)


def core_url_index() -> dict[str, dict[str, str]]:
    index: dict[str, dict[str, str]] = {}
    for path in CORE_TABLES:
        for row in read_tsv(path):
            normalized = normalize_url(row.get("primary_source_url", ""))
            if not normalized:
                continue
            index[normalized] = {
                "case_id": row.get("case_id", ""),
                "title": clean(row.get("title", ""), 240),
                "source_table": str(path.relative_to(PROJECT_ROOT)),
            }
    return index


def classify(row: dict[str, str], core_urls: dict[str, dict[str, str]]) -> tuple[str, str, str, str, str, str]:
    text = text_blob(row)
    normalized = normalize_url(row.get("source_url_or_locator", "") or row.get("extracted_source_url", ""))
    surface_hits = count_hits(text, SURFACE_HINTS)
    case_hits = count_hits(text, CASE_HINTS)
    has_ready_blocker = any(blocker in text for blocker in READY_BLOCKERS)

    if normalized and normalized in core_urls:
        case = core_urls[normalized]
        return (
            "duplicate_existing_reviewed_core",
            "do_not_promote_duplicate",
            "do_not_add_duplicate",
            "exact_reviewed_core_url_match",
            f"Already represented by {case['case_id']}: {case['title']}",
            "Do not add to ObscureAI; preserve as source-lineage/dedupe evidence only.",
        )

    if not normalized and not clean(row.get("source_url_or_locator", "")):
        return (
            "blocked_no_public_source_url",
            "blocked_before_reviewed_core",
            "not_obscure_ai_ready_no_source_url",
            "no_public_url_or_locator",
            "Resolve a public source URL/locator, then rerun dedupe and case hardening.",
            "Do not add to ObscureAI without a direct public source URL and case-level claim ceiling.",
        )

    if case_hits >= 2 and not has_ready_blocker and surface_hits == 0:
        return (
            "possible_case_needs_human_case_hardening",
            "case_candidate_not_promoted",
            "possible_obscure_ai_case_needs_human_claim_ceiling",
            "not_in_reviewed_core_exact_url",
            "Verify exact source text/date, extract the case-level factual claim, dedupe by entity/event, then write a strict claim ceiling.",
            "Only add after human source-text verification, dedupe, chronology, category fit, and claim-ceiling review.",
        )

    if case_hits >= 1 and "court ai" in text:
        return (
            "legal_or_court_source_needs_human_case_hardening",
            "case_candidate_not_promoted",
            "possible_obscure_ai_case_needs_human_claim_ceiling",
            "not_in_reviewed_core_exact_url",
            "Human legal/source review required before any case statement; keep the current row as source surface only.",
            "Do not add until the legal holding/event claim is manually bounded and deduped.",
        )

    return (
        "source_surface_or_context_only",
        "keep_out_of_reviewed_core_for_now",
        "not_obscure_ai_case_source_surface",
        "not_in_reviewed_core_exact_url",
        "Keep as LIMEN source-surface/context unless a concrete edge-case event is extracted and human-hardened.",
        "Do not add to ObscureAI; current row is source-surface/context rather than a case-level record.",
    )


def packet_row(
    *,
    source_lane: str,
    row: dict[str, str],
    review_status: str,
    source_url_or_locator: str,
    source_name: str,
    title_or_snippet: str,
    language_reviewed: str = "",
    hardening_gate: str = "",
    hardening_priority: str = "",
    core_urls: dict[str, dict[str, str]],
) -> dict[str, str]:
    base = {
        "source_lane": source_lane,
        "signal_id": row.get("signal_id", ""),
        "queue_id": row.get("queue_id", ""),
        "review_status": review_status,
        "source_url_or_locator": clean(source_url_or_locator, 700),
        "normalized_source_url": normalize_url(source_url_or_locator),
        "source_host": source_host(source_url_or_locator),
        "source_name": clean(source_name, 240),
        "language_reviewed": clean(language_reviewed, 120),
        "review_priority": clean(row.get("review_priority", ""), 120),
        "shards": clean(row.get("shards", ""), 120),
        "queries": clean(row.get("queries", ""), 180),
        "hardening_gate": clean(hardening_gate, 120),
        "hardening_priority": clean(hardening_priority, 80),
        "source_path": clean(row.get("source_path", ""), 500),
        "source_line": clean(row.get("source_line", ""), 80),
        "title_or_snippet": clean(title_or_snippet, 520),
        "claim_ceiling": clean(row.get("claim_ceiling", ""), 360),
        "next_action": clean(row.get("next_action", "") or row.get("required_hardening_step", ""), 360),
        "forbidden_overread": "Packet row only; no reviewed-core promotion, ObscureAI addition, incident truth, legal finding, safety finding, compliance finding, prevalence, or ranking claim.",
    }
    base["source_cluster_key"] = stable_cluster_key(
        base["source_url_or_locator"],
        base["source_name"],
        " ".join([base["signal_id"], base["title_or_snippet"], base["source_path"]]),
    )
    (
        base["promotion_readiness"],
        base["reviewed_core_posture"],
        base["obscure_ai_posture"],
        base["dedupe_status"],
        base["required_before_reviewed_core"],
        base["required_before_obscure_ai"],
    ) = classify(base | row, core_urls)
    return base


def build_rows(core_urls: dict[str, dict[str, str]]) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    translation_board = {row.get("signal_id", ""): row for row in read_tsv(TRANSLATION_BOARD)}

    for row in read_tsv(TRANSLATION_RESULTS):
        if row.get("translation_review_verdict") != "translation_source_reviewed":
            continue
        board = translation_board.get(row.get("signal_id", ""), {})
        rows.append(
            packet_row(
                source_lane="hardening_translation_source_review",
                row=row,
                review_status="translation_source_reviewed",
                source_url_or_locator=row.get("source_url_or_locator", ""),
                source_name=row.get("source_name", ""),
                language_reviewed=row.get("language_reviewed", ""),
                title_or_snippet=board.get("title_or_snippet", "") or row.get("reason", ""),
                core_urls=core_urls,
            )
        )

    for row in read_tsv(HARDENING):
        if row.get("promotion_priority") not in {"P0", "P1"}:
            continue
        rows.append(
            packet_row(
                source_lane="source_review_promotion_hardening",
                row=row,
                review_status=row.get("promotion_gate", ""),
                source_url_or_locator=row.get("source_url", ""),
                source_name=row.get("source_host", ""),
                hardening_gate=row.get("promotion_gate", ""),
                hardening_priority=row.get("promotion_priority", ""),
                title_or_snippet=row.get("title_or_snippet", ""),
                core_urls=core_urls,
            )
        )

    for row in read_tsv(BULK_PARENT_RESULTS):
        if row.get("bulk_source_verdict") != "source_url_extracted":
            continue
        rows.append(
            packet_row(
                source_lane="bulk_parent_source_extraction",
                row=row,
                review_status="source_url_extracted",
                source_url_or_locator=row.get("extracted_source_url", ""),
                source_name=row.get("source_name", ""),
                title_or_snippet=row.get("reason", ""),
                core_urls=core_urls,
            )
        )

    for row in read_tsv(BULK_NAMED_SOURCE_AUTORESOLVE):
        if not row.get("autoresolve_status", "").startswith("url_found"):
            continue
        source_url = row.get("extracted_source_url", "")
        rows.append(
            packet_row(
                source_lane="bulk_named_source_autoresolve",
                row=row,
                review_status=row.get("autoresolve_status", ""),
                source_url_or_locator=source_url,
                source_name=source_host(source_url),
                title_or_snippet=row.get("reason", ""),
                core_urls=core_urls,
            )
        )

    for row in read_tsv(BULK_TRANSLATION_RESULTS):
        if row.get("bulk_translation_verdict") != "translation_source_reviewed":
            continue
        rows.append(
            packet_row(
                source_lane="bulk_translation_source_review",
                row=row,
                review_status="translation_source_reviewed",
                source_url_or_locator=row.get("source_url_or_locator", ""),
                source_name=row.get("source_name", ""),
                language_reviewed=row.get("language_reviewed", ""),
                title_or_snippet=row.get("reason", ""),
                core_urls=core_urls,
            )
        )

    for row in read_tsv(BULK_TRANSLATION_PARENT_RESULTS):
        if row.get("bulk_source_verdict") != "source_url_extracted":
            continue
        rows.append(
            packet_row(
                source_lane="bulk_translation_parent_source_extraction",
                row=row,
                review_status="source_url_extracted",
                source_url_or_locator=row.get("extracted_source_url", ""),
                source_name=row.get("source_name", ""),
                title_or_snippet=row.get("reason", ""),
                core_urls=core_urls,
            )
        )
    return rows


def unique_join(values: list[str], limit: int = 12) -> str:
    seen = []
    for value in values:
        text = clean(value, 300)
        if text and text not in seen:
            seen.append(text)
    return "; ".join(seen[:limit])


def build_case_queue(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    clusters: dict[str, list[dict[str, str]]] = {}
    for row in rows:
        if not row.get("obscure_ai_posture", "").startswith("possible_obscure_ai_case"):
            continue
        clusters.setdefault(row["source_cluster_key"], []).append(row)

    out_rows: list[dict[str, str]] = []
    for index, (cluster_key, members) in enumerate(sorted(clusters.items()), start=1):
        rep = sorted(
            members,
            key=lambda row: (
                0 if row.get("normalized_source_url") else 1,
                row.get("source_lane", ""),
                row.get("packet_id", ""),
            ),
        )[0]
        out_rows.append(
            {
                "cluster_id": f"RCCQ-{index:05d}",
                "source_cluster_key": cluster_key,
                "candidate_packet_rows": str(len(members)),
                "signal_ids": unique_join([row.get("signal_id", "") for row in members], 20),
                "source_lanes": unique_join([row.get("source_lane", "") for row in members], 20),
                "source_url_or_locator": rep.get("source_url_or_locator", ""),
                "normalized_source_url": rep.get("normalized_source_url", ""),
                "source_host": rep.get("source_host", ""),
                "source_name": rep.get("source_name", ""),
                "queries": unique_join([row.get("queries", "") for row in members], 20),
                "case_hardening_status": "needs_human_legal_or_source_review_before_promotion",
                "case_claim_ceiling_candidate": "Official/public source candidate only; no legal holding, due-process finding, incident truth, deployment, compliance, safety, prevalence, or ranking claim until manually hardened.",
                "required_before_reviewed_core": "Read the original source, extract exact date/title/holding or event language, dedupe against reviewed core by event/entity/source, then write a case-level claim ceiling.",
                "required_before_obscure_ai": "Only add after reviewed-core acceptance and human claim-ceiling review; current cluster is not ObscureAI-ready.",
                "boundary": "Case-hardening queue only; no reviewed-core promotion or ObscureAI addition occurred.",
            }
        )
    return out_rows


def build() -> dict[str, object]:
    core_urls = core_url_index()
    rows = build_rows(core_urls)
    cluster_counts = Counter(row["source_cluster_key"] for row in rows)
    signal_counts = Counter(row["signal_id"] for row in rows if row.get("signal_id"))
    for row in rows:
        row["cluster_size"] = str(cluster_counts[row["source_cluster_key"]])

    rows.sort(
        key=lambda row: (
            row["promotion_readiness"],
            row["obscure_ai_posture"],
            row["source_cluster_key"],
            row["source_lane"],
            row["signal_id"],
        )
    )
    for index, row in enumerate(rows, start=1):
        row["packet_id"] = f"RCPP-{index:05d}"

    write_tsv(OUT, rows)
    write_tsv(DASHBOARD_COPY, rows[:300])
    case_queue_rows = build_case_queue(rows)
    write_tsv_with_fields(CASE_QUEUE, case_queue_rows, CASE_QUEUE_FIELDS)
    write_tsv_with_fields(CASE_QUEUE_DASHBOARD_COPY, case_queue_rows, CASE_QUEUE_FIELDS)

    readiness_counts = Counter(row["promotion_readiness"] for row in rows)
    core_posture_counts = Counter(row["reviewed_core_posture"] for row in rows)
    obscure_posture_counts = Counter(row["obscure_ai_posture"] for row in rows)
    lane_counts = Counter(row["source_lane"] for row in rows)
    dedupe_counts = Counter(row["dedupe_status"] for row in rows)
    routing_status = read_json(ROUTING_STATUS, {})

    reviewed_core_ready_now = core_posture_counts.get("ready_for_reviewed_core", 0)
    obscure_ai_ready_now = obscure_posture_counts.get("ready_for_obscure_ai", 0)
    possible_case_rows = sum(
        count
        for posture, count in obscure_posture_counts.items()
        if posture.startswith("possible_obscure_ai_case")
    )

    status = {
        "generated_at_utc": utc_now(),
        "packet_rows": len(rows),
        "unique_signal_ids": len(signal_counts),
        "duplicate_signal_ids": sum(1 for count in signal_counts.values() if count > 1),
        "unique_source_clusters": len(cluster_counts),
        "multirow_source_clusters": sum(1 for count in cluster_counts.values() if count > 1),
        "reviewed_core_exact_url_index_rows": len(core_urls),
        "source_lane_counts": dict(sorted(lane_counts.items())),
        "promotion_readiness_counts": dict(sorted(readiness_counts.items())),
        "reviewed_core_posture_counts": dict(sorted(core_posture_counts.items())),
        "obscure_ai_posture_counts": dict(sorted(obscure_posture_counts.items())),
        "dedupe_status_counts": dict(sorted(dedupe_counts.items())),
        "possible_case_hardening_rows": possible_case_rows,
        "case_hardening_clusters": len(case_queue_rows),
        "reviewed_core_ready_now": reviewed_core_ready_now,
        "obscure_ai_ready_now": obscure_ai_ready_now,
        "direct_source_queue_rows": int((routing_status or {}).get("current_queue_rows") or 0)
        if isinstance(routing_status, dict)
        else 0,
        "direct_source_queue_reviewed_rows": int((routing_status or {}).get("current_queue_reviewed_rows") or 0)
        if isinstance(routing_status, dict)
        else 0,
        "output": str(OUT),
        "case_hardening_queue": str(CASE_QUEUE),
        "dashboard_copy": str(DASHBOARD_COPY),
        "case_hardening_dashboard_copy": str(CASE_QUEUE_DASHBOARD_COPY),
        "boundary": "Promotion packet only; no reviewed-core or ObscureAI addition has occurred.",
    }
    STATUS.write_text(json.dumps(status, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    SUMMARY.write_text(
        "\n".join(
            [
                "# LIMEN reviewed-core promotion packet",
                "",
                f"- Generated: {status['generated_at_utc']}",
                f"- Packet rows: `{status['packet_rows']}`",
                f"- Unique signal IDs: `{status['unique_signal_ids']}`",
                f"- Unique source clusters: `{status['unique_source_clusters']}`",
                f"- Source lanes: `{json.dumps(status['source_lane_counts'], sort_keys=True)}`",
                f"- Promotion readiness: `{json.dumps(status['promotion_readiness_counts'], sort_keys=True)}`",
                f"- Reviewed-core posture: `{json.dumps(status['reviewed_core_posture_counts'], sort_keys=True)}`",
                f"- ObscureAI posture: `{json.dumps(status['obscure_ai_posture_counts'], sort_keys=True)}`",
                f"- Possible case-hardening rows: `{status['possible_case_hardening_rows']}`",
                f"- Case-hardening clusters: `{status['case_hardening_clusters']}`",
                f"- Reviewed-core ready now: `{status['reviewed_core_ready_now']}`",
                f"- ObscureAI ready now: `{status['obscure_ai_ready_now']}`",
                "",
                status["boundary"],
                "",
            ]
        ),
        encoding="utf-8",
    )
    return status


def main() -> int:
    print(json.dumps(build(), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
