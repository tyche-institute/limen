#!/usr/bin/env python3
"""Close the promotion packet as public/core disposition accounting.

This stage does not promote anything. It explains every reviewed-core promotion
packet row as either an already represented duplicate, a closed non-case source
surface, or a cluster that still needs case extraction/hardening before it can
ever become reviewed-core / ObscureAI material.
"""

from __future__ import annotations

import csv
import json
import re
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path


PROJECT_ROOT = Path("/srv/tyche/projects/limen-ai-edge-case-atlas")
REVIEW_ROOT = PROJECT_ROOT / "results" / "review-candidates"
PACKET = REVIEW_ROOT / "reviewed-core-promotion-packet-v0.1.tsv"
OUT = REVIEW_ROOT / "reviewed-core-source-surface-disposition-v0.1.tsv"
QUEUE = REVIEW_ROOT / "reviewed-core-case-extraction-queue-v0.1.tsv"
STATUS = REVIEW_ROOT / "reviewed-core-source-surface-disposition-status.json"
SUMMARY = REVIEW_ROOT / "reviewed-core-source-surface-disposition-summary-v0.1.md"
DASHBOARD_COPY = PROJECT_ROOT / "results" / "dashboard" / "reviewed-core-source-surface-disposition.tsv"
QUEUE_DASHBOARD_COPY = PROJECT_ROOT / "results" / "dashboard" / "reviewed-core-case-extraction-queue.tsv"

FIELDS = [
    "source_cluster_key",
    "packet_rows",
    "signal_ids",
    "source_lanes",
    "source_host",
    "source_url_or_locator",
    "source_name",
    "queries",
    "representative_title_or_snippet",
    "public_disposition",
    "completion_status",
    "destination",
    "rationale",
    "required_before_reviewed_core",
    "required_before_obscure_ai",
    "boundary",
]

CASE_HINTS = [
    "complaint",
    "enforcement",
    "fine",
    "penalty",
    "sanction",
    "ruling",
    "judgment",
    "lawsuit",
    "charge",
    "indictment",
    "settlement",
    "breach",
    "incident",
    "deepfake",
    "robocall",
    "fraud",
    "scam",
    "cve-",
    "vulnerability",
    "exploit",
    "leak",
    "bias",
    "discrimination",
]

SURFACE_HINTS = [
    "source-surface",
    "source surface",
    "source posture",
    "context only",
    "source-context",
    "locator only",
    "register",
    "registry",
    "framework",
    "policy",
    "strategy",
    "guidance",
    "roadmap",
    "procurement",
    "tender",
    "patent",
    "doi",
    "crossref",
    "openalex",
    "no case",
    "no incident",
    "no legal",
    "no compliance",
    "no safety",
    "no prevalence",
    "no deployment",
]

SCHOLARLY_HOSTS = {
    "doi.org",
    "api.crossref.org",
    "api.openalex.org",
    "semanticscholar.org",
    "link.springer.com",
    "arxiv.org",
}

PATENT_HOSTS = {
    "patents.google.com",
    "ops.epo.org",
    "patentscope.wipo.int",
    "uspto.gov",
}

REGISTER_HOST_FRAGMENTS = [
    "algoritmes.overheid.nl",
    "ai.hel.fi",
    "aesia.digital.gob.es",
    "1823.gov.hk",
]

POLICY_HOST_FRAGMENTS = [
    "eur-lex.europa.eu",
    "gov.uk",
    "gov.br",
    "digdir.no",
    "cnie.ma",
    "ict.go.ke",
    "congressonacional.leg.br",
    "w3.org",
]

VENDOR_OR_DOC_HINTS = [
    "docs.",
    "github.com",
    "gitlab.com",
    "haptik.ai",
    "bland.ai",
    "limbic.ai",
    "evolvtechnology.com",
    "manus.im",
]

AUTHORITY_HINTS = [
    "court",
    "tribunal",
    "corte",
    "garante",
    "ftc",
    "fcc",
    "sec",
    "ico",
    "cnil",
    "commission",
    "authority",
    "regulator",
]


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def clean(value: str, limit: int = 700) -> str:
    return re.sub(r"\s+", " ", value or "").strip().replace("\t", " ")[:limit].rstrip()


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


def count_hits(text: str, hints: list[str]) -> int:
    return sum(1 for hint in hints if hint in text)


def any_fragment(host: str, fragments: list[str]) -> bool:
    return any(fragment in host for fragment in fragments)


def unique_join(values: list[str], limit: int = 16) -> str:
    seen: list[str] = []
    for value in values:
        value = clean(value, 240)
        if value and value not in seen:
            seen.append(value)
    return "; ".join(seen[:limit])


def representative(rows: list[dict[str, str]]) -> dict[str, str]:
    return sorted(
        rows,
        key=lambda row: (
            0 if row.get("normalized_source_url") else 1,
            0 if row.get("source_host") else 1,
            row.get("source_lane", ""),
            row.get("packet_id", ""),
        ),
    )[0]


def classify(rows: list[dict[str, str]]) -> tuple[str, str, str, str, str, str, str]:
    rep = representative(rows)
    text = " ".join(
        clean(row.get(key, ""), 900)
        for row in rows
        for key in [
            "source_host",
            "source_name",
            "queries",
            "title_or_snippet",
            "claim_ceiling",
            "next_action",
            "required_before_reviewed_core",
            "required_before_obscure_ai",
        ]
    ).lower()
    host = clean(rep.get("source_host", ""), 240).lower()
    source_url = clean(rep.get("source_url_or_locator", ""), 500).lower()
    case_hits = count_hits(text, CASE_HINTS)
    surface_hits = count_hits(text, SURFACE_HINTS)
    authority_hits = count_hits(f"{text} {host}", AUTHORITY_HINTS)

    if any(row.get("dedupe_status") == "exact_reviewed_core_url_match" for row in rows):
        return (
            "duplicate_existing_reviewed_core",
            "closed_duplicate",
            "reviewed_core_lineage_only",
            "Already represented by an exact reviewed-core URL match; keep only as lineage/dedupe evidence.",
            "Do not promote duplicate rows.",
            "Do not add duplicate rows to ObscureAI.",
            "closed",
        )

    if host in SCHOLARLY_HOSTS or "doi.org/" in source_url:
        return (
            "noncase_scholarly_or_index_surface",
            "closed_noncase_source_surface",
            "source_family_accounting",
            "Scholarly/index source surface, useful for traceability but not a case-level AI edge-case record.",
            "A concrete event/entity claim and direct source would be required before reviewed-core consideration.",
            "Not ObscureAI material without a reviewed case-level claim ceiling.",
            "closed",
        )

    if host in PATENT_HOSTS or "patent" in text:
        return (
            "noncase_patent_or_ip_surface",
            "closed_noncase_source_surface",
            "source_family_accounting",
            "Patent/IP surface, useful for topology/source-family work but not an incident or authority finding.",
            "A separate concrete public event or authority record would be required.",
            "Not ObscureAI material without an evidence-tiered case record.",
            "closed",
        )

    if any_fragment(host, REGISTER_HOST_FRAGMENTS) or "algorithm register" in text or "ai register" in text:
        return (
            "noncase_register_or_transparency_surface",
            "closed_noncase_source_surface",
            "source_family_accounting",
            "Register/transparency surface; it may inventory systems, but the current row is not a harm/finding/event.",
            "Extract a specific authority action or concrete edge-case event before reviewed-core consideration.",
            "Not ObscureAI material until converted into a bounded case-level record.",
            "closed",
        )

    if any_fragment(host, POLICY_HOST_FRAGMENTS) or any(token in text for token in ["policy", "strategy", "guidance", "gdpr", "eur-lex"]):
        return (
            "noncase_policy_or_law_surface",
            "closed_noncase_source_surface",
            "source_family_accounting",
            "Policy/legal-text surface; it supports context, not an incident/finding by itself.",
            "A concrete source passage, event/entity and claim ceiling would be required.",
            "Not ObscureAI material without a reviewed case-level claim.",
            "closed",
        )

    if any(fragment in host for fragment in VENDOR_OR_DOC_HINTS) or any(fragment in source_url for fragment in VENDOR_OR_DOC_HINTS):
        return (
            "noncase_vendor_docs_or_product_surface",
            "closed_noncase_source_surface",
            "source_family_accounting",
            "Vendor/doc/product source surface; current row does not establish a public edge-case event or authority finding.",
            "Only promote if a separate concrete incident/finding is extracted and deduped.",
            "Not ObscureAI material without reviewed-core acceptance.",
            "closed",
        )

    if case_hits >= 2 and authority_hits >= 1 and surface_hits == 0:
        return (
            "case_extraction_candidate",
            "needs_case_extraction_review",
            "case_extraction_queue",
            "Case and authority hints are present without source-surface blockers; route to manual/Hermes case extraction before hardening.",
            "Extract exact source text/date/event/entity, dedupe against reviewed core, and write a strict claim ceiling.",
            "Reviewed-core acceptance and human claim-ceiling review required before ObscureAI.",
            "open",
        )

    return (
        "noncase_source_surface_context_only",
        "closed_noncase_source_surface",
        "source_family_accounting",
        "Current cluster remains source-surface/context rather than a case-level record.",
        "A concrete public event/finding and direct source passage would be required before reviewed-core consideration.",
        "Not ObscureAI material without case hardening and reviewed-core acceptance.",
        "closed",
    )


def build() -> dict[str, object]:
    packet_rows = read_tsv(PACKET)
    clusters: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in packet_rows:
        key = row.get("source_cluster_key") or row.get("packet_id") or "missing"
        clusters[key].append(row)

    rows: list[dict[str, str]] = []
    queue_rows: list[dict[str, str]] = []
    represented_packet_rows = 0

    for key, members in sorted(clusters.items()):
        represented_packet_rows += len(members)
        rep = representative(members)
        disposition, status, destination, rationale, before_core, before_obscure, queue_state = classify(members)
        row = {
            "source_cluster_key": key,
            "packet_rows": str(len(members)),
            "signal_ids": unique_join([m.get("signal_id", "") for m in members], 24),
            "source_lanes": unique_join([m.get("source_lane", "") for m in members], 16),
            "source_host": rep.get("source_host", ""),
            "source_url_or_locator": rep.get("source_url_or_locator", ""),
            "source_name": rep.get("source_name", ""),
            "queries": unique_join([m.get("queries", "") for m in members], 16),
            "representative_title_or_snippet": clean(rep.get("title_or_snippet", ""), 700),
            "public_disposition": disposition,
            "completion_status": status,
            "destination": destination,
            "rationale": rationale,
            "required_before_reviewed_core": before_core,
            "required_before_obscure_ai": before_obscure,
            "boundary": "Disposition accounting only; no reviewed-core promotion or ObscureAI addition occurred.",
        }
        rows.append(row)
        if queue_state == "open":
            queue_rows.append(row)

    rows.sort(key=lambda row: (row["completion_status"], row["public_disposition"], row["source_host"], row["source_cluster_key"]))
    queue_rows.sort(key=lambda row: (row["source_host"], row["source_cluster_key"]))
    write_tsv(OUT, rows)
    write_tsv(DASHBOARD_COPY, rows[:300])
    write_tsv(QUEUE, queue_rows)
    write_tsv(QUEUE_DASHBOARD_COPY, queue_rows[:300])

    completion_counts = Counter(row["completion_status"] for row in rows)
    disposition_counts = Counter(row["public_disposition"] for row in rows)
    destination_counts = Counter(row["destination"] for row in rows)
    row_completion_counts = Counter()
    row_disposition_counts = Counter()
    for row in rows:
        n = int(row["packet_rows"])
        row_completion_counts[row["completion_status"]] += n
        row_disposition_counts[row["public_disposition"]] += n

    status = {
        "generated_at_utc": utc_now(),
        "input": str(PACKET),
        "output": str(OUT),
        "case_extraction_queue": str(QUEUE),
        "dashboard_copy": str(DASHBOARD_COPY),
        "case_extraction_dashboard_copy": str(QUEUE_DASHBOARD_COPY),
        "packet_rows": len(packet_rows),
        "packet_rows_represented": represented_packet_rows,
        "source_clusters": len(rows),
        "case_extraction_candidate_clusters": len(queue_rows),
        "case_extraction_candidate_rows": sum(int(row["packet_rows"]) for row in queue_rows),
        "closed_clusters": completion_counts.get("closed_duplicate", 0) + completion_counts.get("closed_noncase_source_surface", 0),
        "closed_packet_rows": row_completion_counts.get("closed_duplicate", 0) + row_completion_counts.get("closed_noncase_source_surface", 0),
        "completion_status_counts": dict(sorted(completion_counts.items())),
        "completion_status_packet_row_counts": dict(sorted(row_completion_counts.items())),
        "public_disposition_counts": dict(sorted(disposition_counts.items())),
        "public_disposition_packet_row_counts": dict(sorted(row_disposition_counts.items())),
        "destination_counts": dict(sorted(destination_counts.items())),
        "top_hosts": dict(Counter(row["source_host"] or "(local/locator)" for row in rows).most_common(20)),
        "obscure_ai_ready_now": 0,
        "boundary": "Disposition accounting only; no reviewed-core promotion or ObscureAI addition occurred.",
    }
    STATUS.write_text(json.dumps(status, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    SUMMARY.write_text(
        "\n".join(
            [
                "# LIMEN reviewed-core source-surface disposition",
                "",
                f"- Generated: `{status['generated_at_utc']}`",
                f"- Packet rows represented: `{status['packet_rows_represented']} / {status['packet_rows']}`",
                f"- Source clusters: `{status['source_clusters']}`",
                f"- Closed clusters: `{status['closed_clusters']}`",
                f"- Closed packet rows: `{status['closed_packet_rows']}`",
                f"- Case-extraction candidate clusters: `{status['case_extraction_candidate_clusters']}`",
                f"- Case-extraction candidate rows: `{status['case_extraction_candidate_rows']}`",
                f"- Dispositions: `{json.dumps(status['public_disposition_counts'], sort_keys=True)}`",
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
