#!/usr/bin/env python3
"""Build a promotion-hardening board from source-reviewed LIMEN candidates.

This does not promote anything into reviewed core. It separates concrete
source-surface rows that may support a future case-hardening pass from rows
that are useful only as source-family / registry / policy anchors.
"""

from __future__ import annotations

import csv
import json
import re
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse


PROJECT_ROOT = Path("/srv/tyche/projects/limen-ai-edge-case-atlas")
REVIEW_ROOT = PROJECT_ROOT / "results" / "review-candidates"
BATCH_ROOT = REVIEW_ROOT / "source-review-batches"
OUT = REVIEW_ROOT / "source-reviewed-promotion-hardening-v0.1.tsv"
TOP_OUT = REVIEW_ROOT / "source-reviewed-promotion-hardening-top50-v0.1.tsv"
SUMMARY = REVIEW_ROOT / "source-reviewed-promotion-hardening-summary-v0.1.md"
STATUS = REVIEW_ROOT / "source-reviewed-promotion-hardening-status.json"
DASHBOARD_COPY = PROJECT_ROOT / "results" / "dashboard" / "source-reviewed-promotion-hardening.tsv"
URL_EXTRACTION_RESULTS = REVIEW_ROOT / "named-url-extraction-results-v0.1.tsv"
SOURCE_LEDGER = PROJECT_ROOT / "sources" / "authoritative-source-ledger.tsv"
AUTHORITATIVE_CASES = PROJECT_ROOT / "data" / "cases" / "authoritative-candidates.jsonl"
SECURITY_ROOT = PROJECT_ROOT / "results" / "security"
REVIEWED_CORE_TABLES = [
    SECURITY_ROOT / "security-agentic-watch-v0.1.tsv",
    SECURITY_ROOT / "limen-reviewed-core-extension-v0.1.tsv",
    SECURITY_ROOT / "limen-reviewed-core-web-verified-v0.1.tsv",
    *sorted(SECURITY_ROOT.glob("limen-reviewed-core-web-verified-batch*-v0.1.tsv")),
]

URL_RE = re.compile(r"https?://[^\s,\"'<>]+", re.I)
SOURCE_ID_RE = re.compile(r"\bSRC-AUTH-\d{4}\b")
CASE_ID_RE = re.compile(r"\bLIMEN-\d{6}\b")

CASE_SIGNAL_HINTS = [
    "incident",
    "breach",
    "exploit",
    "vulnerab",
    "deepfake",
    "voice clone",
    "hallucinat",
    "fabricat",
    "misleading",
    "scam",
    "fraud",
    "bias",
    "discriminat",
    "complaint",
    "enforcement",
    "fine",
    "penalt",
    "sanction",
    "ban",
    "reprimand",
    "investigat",
    "lawsuit",
    "charged",
    "indict",
    "ruling",
    "settlement",
    "csam",
    "harassment",
    "privacy violation",
]

SPECIFIC_CASE_HINTS = [
    "notice of apparent liability",
    "consent decree",
    "final order",
    "forfeiture order",
    "settlement",
    "fine",
    "fined",
    "penalt",
    "sanction",
    "lawsuit",
    "indict",
    "charged",
    "complaint",
    "breach",
    "exploit",
    "cve-",
    "deepfake",
    "voice clone",
    "robocall",
    "hallucinat",
    "fabricat",
    "false",
    "misleading",
    "fraud",
    "scam",
    "discriminat",
]

AUTHORITY_HINTS = [
    ".gov",
    ".europa.eu",
    "court",
    "tribunal",
    "commission",
    "regulator",
    "authority",
    "agency",
    "ministry",
    "police",
    "prosecutor",
    "sec",
    "ftc",
    "fcc",
    "ico",
    "cnil",
    "garante",
    "datatilsynet",
    "cve",
    "advisory",
]

SURFACE_ONLY_HINTS = [
    "algorithm register",
    "ai register",
    "open data",
    "data portal",
    "public tenders",
    "procurement",
    "sandbox",
    "policy",
    "strategy",
    "guidance",
    "manual",
    "statute",
    "provisions",
    "data protection act",
    "official gazette search",
    "search:",
    "register page",
    "regulator page",
    "legal page",
    "reporting page",
    "incident reporting",
    "incident report form",
    "incident management",
    "notification",
    "risk assessment",
    "complaint resolution",
    "citizen support",
    "consumer support",
    "workshop",
    "coalition",
    "frontier ai vulnerability gap",
    "positive_regulator_capacity",
    "data protection authority capacity",
    "official_data_protection_authority",
    "false_positive_check",
    "search produced unrelated",
    "digital government",
    "standards",
    "specification",
]

LOW_VALUE_HOSTS = {
    "raw.githubusercontent.com",
    "github.com",
    "doi.org",
    "link.springer.com",
}

FIELDS = [
    "row_id",
    "signal_id",
    "promotion_gate",
    "promotion_priority",
    "promotion_resolution",
    "linked_reviewed_case_id",
    "linked_source_id",
    "linked_source_role",
    "hardening_score",
    "dedupe_key",
    "duplicate_url_count",
    "source_url",
    "url_recovery_status",
    "url_recovery_source",
    "source_host",
    "source_surface_class",
    "source_review_role",
    "review_priority",
    "shards",
    "queries",
    "source_path",
    "source_line",
    "title_or_snippet",
    "source_review_reason",
    "claim_ceiling",
    "next_action",
    "required_hardening_step",
    "forbidden_overread",
]


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def read_tsv(path: Path) -> list[dict[str, str]]:
    try:
        with path.open("r", encoding="utf-8", newline="") as fh:
            return [{k: v or "" for k, v in row.items() if k is not None} for row in csv.DictReader(fh, delimiter="\t")]
    except Exception:
        return []


def clean_cell(value: str, limit: int | None = None) -> str:
    text = re.sub(r"\s+", " ", value or "").strip()
    text = text.replace("\t", " ")
    if limit is not None:
        text = text[:limit].rstrip()
    return text


def first_url(*values: str) -> str:
    for value in values:
        match = URL_RE.search(value or "")
        if match:
            return match.group(0).rstrip(").,;]`")
    return ""


URL_FIELD_PRIORITY = [
    "url",
    "source_url",
    "primary_source_url",
    "seed_url",
    "retrieval_url",
    "reader_target_url",
    "original_url",
    "source_reference",
]


def context_line(path_value: str, line_value: str) -> str:
    try:
        path = Path(path_value)
        line_no = int(line_value or "0")
        if line_no <= 0 or not path.exists() or path.stat().st_size > 50_000_000:
            return ""
        with path.open("r", encoding="utf-8", errors="replace", newline="") as fh:
            for index, line in enumerate(fh, start=1):
                if index == line_no:
                    return line.rstrip("\n")
    except Exception:
        return ""
    return ""


def recover_url_from_context(path_value: str, line_value: str) -> tuple[str, str]:
    line = context_line(path_value, line_value)
    if not line:
        return "", "not_attempted"

    try:
        obj = json.loads(line)
        if isinstance(obj, dict):
            for key in URL_FIELD_PRIORITY:
                value = obj.get(key)
                if isinstance(value, str):
                    url = first_url(value)
                    if url:
                        return url, f"json_field:{key}"
            for key, value in obj.items():
                if isinstance(value, str) and ("url" in key.lower() or "source" in key.lower()):
                    url = first_url(value)
                    if url:
                        return url, f"json_field:{key}"
    except Exception:
        pass

    try:
        dialect = csv.Sniffer().sniff(line[:4096])
        cells = next(csv.reader([line], dialect))
        for cell in cells:
            url = first_url(cell)
            if url:
                return url, "delimited_cell"
    except Exception:
        pass

    url = first_url(line)
    if url:
        return url, "line_regex"
    return "", "line_checked_no_url"


def host_for(url: str) -> str:
    if not url:
        return ""
    host = urlparse(url).netloc.lower()
    return host[4:] if host.startswith("www.") else host


def normalize_text_key(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", value.lower()).strip()


def normalize_url(value: str) -> str:
    return (value or "").rstrip("/").lower()


def count_hints(text: str, hints: list[str]) -> int:
    low = text.lower()
    total = 0
    for hint in hints:
        needle = hint.lower()
        if needle.startswith(".") or " " in needle or len(needle) > 4:
            total += int(needle in low)
            continue
        total += int(re.search(rf"\b{re.escape(needle)}\b", low) is not None)
    return total


def read_jsonl(path: Path) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    try:
        with path.open("r", encoding="utf-8") as fh:
            for line in fh:
                line = line.strip()
                if not line:
                    continue
                rows.append(json.loads(line))
    except Exception:
        return []
    return rows


def reviewed_core_index() -> dict[str, dict[str, str]]:
    case_id_to_case: dict[str, str] = {}
    source_id_to_case: dict[str, str] = {}
    title_to_case: dict[str, str] = {}
    for path in REVIEWED_CORE_TABLES:
        for row in read_tsv(path):
            case_id = row.get("case_id", "")
            if not case_id:
                continue
            case_id_to_case[case_id] = case_id
            title = normalize_text_key(row.get("title", ""))
            if title:
                title_to_case[title] = case_id
            for source_id in SOURCE_ID_RE.findall(row.get("primary_source_id", "")):
                source_id_to_case[source_id] = case_id

    auth_case_title = {
        str(row.get("case_id", "")): normalize_text_key(str(row.get("title", "")))
        for row in read_jsonl(AUTHORITATIVE_CASES)
    }
    auth_case_to_reviewed: dict[str, str] = {}
    for auth_case_id, title in auth_case_title.items():
        if title and title in title_to_case:
            auth_case_to_reviewed[auth_case_id] = title_to_case[title]

    return {
        "case_id_to_case": case_id_to_case,
        "source_id_to_case": source_id_to_case,
        "auth_case_to_reviewed": auth_case_to_reviewed,
    }


def url_extraction_index() -> dict[str, dict[str, str]]:
    rows: dict[str, dict[str, str]] = {}
    for row in read_tsv(URL_EXTRACTION_RESULTS):
        if row.get("url_extraction_verdict") != "url_extracted":
            continue
        url = first_url(row.get("extracted_source_url", ""))
        signal_id = row.get("signal_id", "")
        if signal_id and url:
            row = dict(row)
            row["extracted_source_url"] = url
            rows[signal_id] = row
    return rows


def source_lineage_index() -> tuple[dict[str, dict[str, str]], dict[str, dict[str, str]]]:
    by_source_id: dict[str, dict[str, str]] = {}
    by_url: dict[str, dict[str, str]] = {}
    for row in read_tsv(SOURCE_LEDGER):
        source_id = row.get("source_id", "")
        source_url = row.get("source_url", "")
        if source_id:
            by_source_id[source_id] = row
        if source_url:
            by_url[normalize_url(source_url)] = row
    return by_source_id, by_url


def resolve_reviewed_core_lineage(
    row: dict[str, str],
    source_by_id: dict[str, dict[str, str]],
    source_by_url: dict[str, dict[str, str]],
    reviewed_index: dict[str, dict[str, str]],
) -> dict[str, str]:
    source_row: dict[str, str] = {}
    joined = " ".join(
        [
            row.get("title_or_snippet", ""),
            row.get("source_review_reason", ""),
            row.get("source_path", ""),
            row.get("source_url", ""),
        ]
    )
    for source_id in SOURCE_ID_RE.findall(joined):
        source_row = source_by_id.get(source_id, {})
        if source_row:
            break
    if not source_row and row.get("source_url"):
        source_row = source_by_url.get(normalize_url(row["source_url"]), {})
    if not source_row:
        for case_id in CASE_ID_RE.findall(joined):
            reviewed_case_id = (
                reviewed_index["case_id_to_case"].get(case_id)
                or reviewed_index["auth_case_to_reviewed"].get(case_id)
                or ""
            )
            if reviewed_case_id:
                return {
                    "linked_reviewed_case_id": reviewed_case_id,
                    "linked_source_id": "",
                    "linked_source_role": "",
                }
    if not source_row:
        return {}

    source_id = source_row.get("source_id", "")
    source_case_id = source_row.get("case_id", "")
    reviewed_case_id = (
        reviewed_index["source_id_to_case"].get(source_id)
        or reviewed_index["auth_case_to_reviewed"].get(source_case_id)
        or ""
    )
    if not reviewed_case_id:
        return {}
    return {
        "linked_reviewed_case_id": reviewed_case_id,
        "linked_source_id": source_id,
        "linked_source_role": source_row.get("source_type", ""),
    }


def source_surface_class(text: str, url: str, role: str) -> str:
    low = f"{text} {url} {role}".lower()
    if "cve" in low or "security advisory" in low or "vulnerability" in low:
        return "security_advisory_or_vulnerability"
    if "court" in low or "tribunal" in low or "ruling" in low or "docket" in low:
        return "court_or_tribunal"
    if any(token in low for token in ["ftc", "fcc", "sec", "ico", "cnil", "garante", "commission", "regulator", "authority"]):
        return "regulator_or_public_authority"
    if "procurement" in low or "tender" in low or "contract" in low:
        return "procurement_or_tender_surface"
    if "algorithm register" in low or "ai register" in low or "register" in low:
        return "register_or_transparency_surface"
    if "sandbox" in low:
        return "sandbox_or_innovation_surface"
    if "policy" in low or "strategy" in low or "guidance" in low:
        return "policy_or_guidance_surface"
    if host_for(url) in LOW_VALUE_HOSTS:
        return "secondary_or_index_surface"
    return "public_source_surface"


def classify_gate(row: dict[str, str]) -> tuple[str, str, int, str]:
    case_text = " ".join(
        [
            row.get("snippet", ""),
            row.get("source_review_role", ""),
            row.get("source_review_reason", ""),
            row.get("source_path", ""),
        ]
    )
    query_text = row.get("queries", "")
    text = f"{case_text} {query_text}"
    url = row["source_url"]
    host = row["source_host"]
    case_score = count_hints(case_text, CASE_SIGNAL_HINTS)
    query_case_score = count_hints(query_text, CASE_SIGNAL_HINTS)
    specific_case_score = count_hints(f"{case_text} {url}", SPECIFIC_CASE_HINTS)
    authority_score = count_hints(f"{text} {url} {host}", AUTHORITY_HINTS)
    surface_only_score = count_hints(text, SURFACE_ONLY_HINTS)
    score = case_score * 3 + specific_case_score * 2 + query_case_score + authority_score * 2 - surface_only_score
    if host in LOW_VALUE_HOSTS:
        score -= 2

    if not url:
        return ("needs_named_url_extraction", "P3", score, "Extract a named public URL before any case hardening.")
    if (surface_only_score >= 1 and specific_case_score == 0) or (surface_only_score >= 2 and specific_case_score <= 1):
        return (
            "source_surface_anchor_only",
            "P2" if authority_score >= 1 else "P3",
            score,
            "Use as source-family, registry, policy, or observability anchor only unless a concrete edge-case claim is later extracted.",
        )
    if specific_case_score >= 2 and case_score >= 2 and authority_score >= 1:
        return (
            "ready_for_human_case_hardening",
            "P0" if score >= 10 else "P1",
            score,
            "Verify exact source text/date, assign or dedupe case id, write claim ceiling and caveat before reviewed-core promotion.",
        )
    if specific_case_score >= 1 and case_score >= 1 and authority_score >= 1:
        return (
            "possible_case_hardening_after_context",
            "P1" if score >= 6 else "P2",
            score,
            "Inspect local/public source context for a concrete AI edge-case claim; keep out of reviewed core until exact claim text is captured.",
        )
    return (
        "source_surface_anchor_only",
        "P2" if authority_score >= 1 else "P3",
        score,
        "Use as source-family, registry, policy, or observability anchor only unless a concrete edge-case claim is later extracted.",
    )


def collect_rows() -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    extracted_urls = url_extraction_index()
    source_by_id, source_by_url = source_lineage_index()
    reviewed_index = reviewed_core_index()
    for result_path in sorted(BATCH_ROOT.glob("*/source-review-results.tsv")):
        input_path = result_path.parent / "source-review-input.tsv"
        meta = {row.get("signal_id", ""): row for row in read_tsv(input_path)}
        for result in read_tsv(result_path):
            if result.get("source_review_verdict") != "source_reviewed_candidate":
                continue
            signal_id = result.get("signal_id", "")
            src = meta.get(signal_id, {})
            source_url = first_url(src.get("snippet", ""), result.get("reason", ""), result.get("source_path", ""))
            recovery_status = "snippet_or_result"
            recovery_source = "source_review_input"
            if not source_url:
                source_url, recovery_status = recover_url_from_context(
                    result.get("source_path", "") or src.get("source_path", ""),
                    src.get("source_line", ""),
                )
                recovery_source = "origin_file_line"
            if not source_url:
                extracted = extracted_urls.get(signal_id, {})
                source_url = first_url(extracted.get("extracted_source_url", ""))
                if source_url:
                    recovery_status = "hardening_review_url_extracted"
                    recovery_source = "named-url-extraction-results-v0.1"
            host = host_for(source_url)
            title = clean_cell(URL_RE.sub("", src.get("snippet", "") or ""), 240) or clean_cell(result.get("source_review_role", ""), 120)
            base = {
                "signal_id": signal_id,
                "source_url": source_url,
                "url_recovery_status": recovery_status,
                "url_recovery_source": recovery_source,
                "source_host": host,
                "source_review_role": clean_cell(result.get("source_review_role", ""), 120),
                "source_review_reason": clean_cell(result.get("reason", ""), 360),
                "claim_ceiling": clean_cell(result.get("claim_ceiling", ""), 360),
                "next_action": clean_cell(result.get("next_action", ""), 240),
                "review_priority": src.get("review_priority", ""),
                "shards": src.get("shards", ""),
                "queries": src.get("queries", ""),
                "source_path": result.get("source_path", "") or src.get("source_path", ""),
                "source_line": src.get("source_line", ""),
                "title_or_snippet": title,
            }
            base["source_surface_class"] = source_surface_class(" ".join(base.values()), source_url, base["source_review_role"])
            gate, priority, score, required_step = classify_gate(base | {"snippet": src.get("snippet", "")})
            resolution = resolve_reviewed_core_lineage(base, source_by_id, source_by_url, reviewed_index)
            promotion_resolution = "open_promotion_hardening"
            linked_reviewed_case_id = ""
            linked_source_id = ""
            linked_source_role = ""
            if resolution:
                gate = "already_reviewed_core_lineage"
                priority = "closed"
                required_step = (
                    f"No reviewed-core promotion needed; this source surface is already linked to "
                    f"{resolution['linked_reviewed_case_id']}. Keep it as source-lineage/dedupe evidence."
                )
                promotion_resolution = "linked_existing_reviewed_core"
                linked_reviewed_case_id = resolution["linked_reviewed_case_id"]
                linked_source_id = resolution["linked_source_id"]
                linked_source_role = resolution["linked_source_role"]
            base.update(
                {
                    "promotion_gate": gate,
                    "promotion_priority": priority,
                    "promotion_resolution": promotion_resolution,
                    "linked_reviewed_case_id": linked_reviewed_case_id,
                    "linked_source_id": linked_source_id,
                    "linked_source_role": linked_source_role,
                    "hardening_score": str(score),
                    "required_hardening_step": required_step,
                    "forbidden_overread": "Do not treat source-surface review as reviewed-core promotion, incident truth, legality, compliance, safety, deployment proof, prevalence, or ranking.",
                }
            )
            base["dedupe_key"] = source_url or f"{base['source_path']}:{base['source_line']}:{signal_id}"
            rows.append(base)
    dup_counts = Counter(row["dedupe_key"] for row in rows)
    for index, row in enumerate(rows, start=1):
        row["row_id"] = f"SRPH-{index:05d}"
        row["duplicate_url_count"] = str(dup_counts[row["dedupe_key"]])
    rows.sort(
        key=lambda row: (
            {"closed": 0, "P0": 1, "P1": 2, "P2": 3, "P3": 4}.get(row["promotion_priority"], 9),
            -int(row["hardening_score"]),
            row["source_host"],
            row["signal_id"],
        )
    )
    for index, row in enumerate(rows, start=1):
        row["row_id"] = f"SRPH-{index:05d}"
    return rows


def write_tsv(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, delimiter="\t", fieldnames=FIELDS, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def main() -> int:
    rows = collect_rows()
    write_tsv(OUT, rows)
    write_tsv(TOP_OUT, rows[:50])
    write_tsv(DASHBOARD_COPY, rows[:200])

    gate_counts = Counter(row["promotion_gate"] for row in rows)
    priority_counts = Counter(row["promotion_priority"] for row in rows)
    class_counts = Counter(row["source_surface_class"] for row in rows)
    host_counts = Counter(row["source_host"] or "no_url" for row in rows)
    url_recovery_counts = Counter(row["url_recovery_status"] for row in rows)
    payload = {
        "generated_at_utc": utc_now(),
        "source_reviewed_candidate_rows": len(rows),
        "unique_dedupe_keys": len({row["dedupe_key"] for row in rows}),
        "promotion_gate_counts": dict(sorted(gate_counts.items())),
        "promotion_priority_counts": dict(sorted(priority_counts.items())),
        "source_surface_class_counts": dict(sorted(class_counts.items())),
        "url_recovery_counts": dict(sorted(url_recovery_counts.items())),
        "url_extraction_results": str(URL_EXTRACTION_RESULTS),
        "named_url_rows": sum(1 for row in rows if row["source_url"]),
        "no_named_url_rows": sum(1 for row in rows if not row["source_url"]),
        "top_hosts": [{"host": host, "count": count} for host, count in host_counts.most_common(20)],
        "output": str(OUT),
        "top_output": str(TOP_OUT),
        "dashboard_copy": str(DASHBOARD_COPY),
        "boundary": "Promotion hardening only; no reviewed-core promotion, incident truth, legal finding, safety finding, compliance finding, prevalence, or ranking.",
    }
    STATUS.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    with SUMMARY.open("w", encoding="utf-8") as fh:
        fh.write("# Source-Reviewed Promotion Hardening\n\n")
        fh.write(f"Generated UTC: {payload['generated_at_utc']}\n\n")
        fh.write("This board starts from `source_reviewed_candidate` rows only. It does not promote rows into reviewed core.\n\n")
        fh.write(f"- Rows: `{len(rows)}`\n")
        fh.write(f"- Unique dedupe keys: `{payload['unique_dedupe_keys']}`\n")
        fh.write(f"- Output: `{OUT}`\n")
        fh.write(f"- Top-50 packet: `{TOP_OUT}`\n")
        fh.write(f"- Dashboard copy: `{DASHBOARD_COPY}`\n\n")
        fh.write("## Promotion Gates\n\n")
        for key, value in sorted(gate_counts.items()):
            fh.write(f"- `{key}`: `{value}`\n")
        fh.write("\n## Priority Counts\n\n")
        for key, value in sorted(priority_counts.items()):
            fh.write(f"- `{key}`: `{value}`\n")
        fh.write("\n## Source Surface Classes\n\n")
        for key, value in sorted(class_counts.items()):
            fh.write(f"- `{key}`: `{value}`\n")
        fh.write("\n## URL Recovery\n\n")
        fh.write(f"- Named URL rows: `{payload['named_url_rows']}`\n")
        fh.write(f"- No named URL rows: `{payload['no_named_url_rows']}`\n")
        for key, value in sorted(url_recovery_counts.items()):
            fh.write(f"- `{key}`: `{value}`\n")
        fh.write("\n## Boundary\n\n")
        fh.write(payload["boundary"] + "\n")
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
