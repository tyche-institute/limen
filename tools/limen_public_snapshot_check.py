#!/usr/bin/env python3
"""Compare local LIMEN/ObscureAI snapshots with production JSON."""

from __future__ import annotations

import argparse
import json
import subprocess
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


DEFAULT_FRONTEND_ROOT = Path("/srv/tyche/local-projects/home-anton-projects/tyche-research-vault")
DEFAULT_PROJECT_ROOT = Path("/srv/tyche/projects/limen-ai-edge-case-atlas")
LIMEN_URL = "https://limen-observatory.pages.dev/data/limen-snapshot.json"
OBSCURE_URL = "https://obscure-ai.eatf.eu/data/cases.json"


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def read_json(path: Path) -> dict[str, Any]:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return {}


def fetch_json(url: str, timeout: int) -> tuple[dict[str, Any], str]:
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 LIMEN public snapshot verifier"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as response:
            return json.load(response), response.geturl()
    except Exception as exc:
        return {}, f"fetch failed: {exc}"


def get_path(data: dict[str, Any], *parts: str) -> Any:
    value: Any = data
    for part in parts:
        if not isinstance(value, dict):
            return None
        value = value.get(part)
    return value


def limen_metrics(data: dict[str, Any]) -> dict[str, Any]:
    packet = data.get("reviewed_core_promotion_packet", {}) if isinstance(data.get("reviewed_core_promotion_packet", {}), dict) else {}
    triage = data.get("review_triage", {}) if isinstance(data.get("review_triage", {}), dict) else {}
    bulk = data.get("bulk_review", {}) if isinstance(data.get("bulk_review", {}), dict) else {}
    bulk_tasks = bulk.get("tasks", {}) if isinstance(bulk.get("tasks", {}), dict) else {}

    def bulk_missing(name: str) -> Any:
        task = bulk_tasks.get(name, {}) if isinstance(bulk_tasks.get(name, {}), dict) else {}
        return task.get("missing_queue_ids")

    return {
        "generated_at_utc": data.get("generated_at_utc", ""),
        "review_candidate_rows": triage.get("materialized_review_candidates"),
        "first_pass_reviewed_rows": triage.get("first_pass_reviewed_candidates"),
        "direct_source_queue_rows": triage.get("direct_source_review_queue_rows"),
        "direct_source_missing_rows": triage.get("source_review_queue_missing"),
        "bulk_current_output_clean": bulk.get("current_output_clean"),
        "bulk_parent_source_missing_rows": bulk_missing("parent_source_extraction"),
        "bulk_translation_missing_rows": bulk_missing("bulk_translation_review"),
        "bulk_translation_parent_source_missing_rows": bulk_missing("translation_parent_source_extraction"),
        "promotion_packet_rows": packet.get("packet_rows"),
        "case_autoreview_rows": packet.get("case_autoreview_rows"),
        "case_autoreview_paid_token_required_rows": packet.get("case_autoreview_paid_token_required_rows"),
        "case_autoreview_human_acceptance_required_rows": packet.get("case_autoreview_human_acceptance_required_rows"),
        "case_final_promoted_to_obscure_ai": packet.get("case_final_promoted_to_obscure_ai"),
    }


def obscure_metrics(data: dict[str, Any]) -> dict[str, Any]:
    pipeline = data.get("limen_pipeline", {}) if isinstance(data.get("limen_pipeline", {}), dict) else {}

    def nested_missing(name: str) -> Any:
        task = pipeline.get(name, {}) if isinstance(pipeline.get(name, {}), dict) else {}
        return task.get("missing_rows")

    return {
        "generated_at_utc": data.get("generated_at_utc", ""),
        "count": data.get("count"),
        "review_candidate_rows": pipeline.get("review_candidate_rows"),
        "direct_source_queue_rows": pipeline.get("direct_source_queue_rows"),
        "direct_source_missing_rows": pipeline.get("direct_source_missing_rows"),
        "bulk_current_output_clean": pipeline.get("bulk_current_output_clean"),
        "bulk_parent_source_missing_rows": nested_missing("bulk_parent_source"),
        "bulk_translation_missing_rows": nested_missing("bulk_translation"),
        "bulk_translation_parent_source_missing_rows": nested_missing("bulk_translation_parent_source"),
        "promotion_packet_rows": pipeline.get("promotion_packet_rows"),
        "case_autoreview_rows": pipeline.get("case_autoreview_rows"),
        "case_autoreview_paid_token_required_rows": pipeline.get("case_autoreview_paid_token_required_rows"),
        "case_autoreview_human_acceptance_required_rows": pipeline.get("case_autoreview_human_acceptance_required_rows"),
        "case_final_obscure_ai_promoted_rows": pipeline.get("case_final_obscure_ai_promoted_rows"),
    }


def compare(
    name: str, local: dict[str, Any], live: dict[str, Any], other_label: str = "production"
) -> tuple[list[dict[str, Any]], list[dict[str, Any]], list[dict[str, Any]]]:
    blockers: list[dict[str, Any]] = []
    warnings: list[dict[str, Any]] = []
    infos: list[dict[str, Any]] = []
    if not live:
        blockers.append({"code": f"{name}_{other_label}_unavailable", "message": f"{name} {other_label} JSON could not be fetched."})
        return blockers, warnings, infos
    if not local:
        warnings.append({"code": f"{name}_local_snapshot_missing", "message": f"{name} local snapshot is missing; {other_label} fetch succeeded."})
        return blockers, warnings, infos
    for key, local_value in sorted(local.items()):
        live_value = live.get(key)
        if local_value != live_value:
            if key == "generated_at_utc":
                infos.append(
                    {
                        "code": f"{name}_{other_label}_timestamp_drift",
                        "message": f"{name} {other_label} timestamp differs from local snapshot, but counters are checked separately.",
                        "field": key,
                        "local": local_value,
                        "live": live_value,
                    }
                )
                continue
            blockers.append(
                {
                    "code": f"{name}_{other_label}_mismatch",
                    "message": f"{name} {other_label} field differs from local snapshot.",
                    "field": key,
                    "local": local_value,
                    "live": live_value,
                }
            )
    return blockers, warnings, infos


def compact_status(project_root: Path, timeout: int) -> dict[str, Any]:
    script = project_root / "tools" / "limen_compact_status.py"
    try:
        proc = subprocess.run([str(script)], text=True, capture_output=True, timeout=timeout)
    except Exception:
        return {}
    if proc.returncode != 0:
        return {}
    try:
        return json.loads(proc.stdout)
    except Exception:
        return {}


def project_limen_metrics(status: dict[str, Any]) -> dict[str, Any]:
    review = status.get("review", {}) if isinstance(status.get("review", {}), dict) else {}
    bulk = status.get("bulk", {}) if isinstance(status.get("bulk", {}), dict) else {}
    bulk_tasks = bulk.get("tasks", {}) if isinstance(bulk.get("tasks", {}), dict) else {}
    promotion = status.get("promotion", {}) if isinstance(status.get("promotion", {}), dict) else {}
    case_hardening = status.get("case_hardening", {}) if isinstance(status.get("case_hardening", {}), dict) else {}
    case_autoreview = status.get("case_autoreview", {}) if isinstance(status.get("case_autoreview", {}), dict) else {}
    def bulk_missing(name: str) -> Any:
        task = bulk_tasks.get(name, {}) if isinstance(bulk_tasks.get(name, {}), dict) else {}
        return task.get("missing_rows")

    return {
        "review_candidate_rows": review.get("candidate_rows"),
        "first_pass_reviewed_rows": review.get("first_pass_reviewed_rows"),
        "direct_source_queue_rows": review.get("direct_source_queue_rows"),
        "direct_source_missing_rows": review.get("direct_source_missing_rows"),
        "bulk_current_output_clean": bulk.get("current_output_clean"),
        "bulk_parent_source_missing_rows": bulk_missing("parent_source_extraction"),
        "bulk_translation_missing_rows": bulk_missing("bulk_translation_review"),
        "bulk_translation_parent_source_missing_rows": bulk_missing("translation_parent_source_extraction"),
        "promotion_packet_rows": promotion.get("packet_rows"),
        "case_autoreview_rows": case_autoreview.get("rows"),
        "case_autoreview_paid_token_required_rows": case_autoreview.get("paid_token_required_rows"),
        "case_autoreview_human_acceptance_required_rows": case_autoreview.get("human_acceptance_required_rows"),
        "case_final_promoted_to_obscure_ai": case_hardening.get("final_obscure_ai_promoted_rows"),
    }


def project_obscure_metrics(status: dict[str, Any], local_obscure: dict[str, Any]) -> dict[str, Any]:
    review = status.get("review", {}) if isinstance(status.get("review", {}), dict) else {}
    bulk = status.get("bulk", {}) if isinstance(status.get("bulk", {}), dict) else {}
    bulk_tasks = bulk.get("tasks", {}) if isinstance(bulk.get("tasks", {}), dict) else {}
    promotion = status.get("promotion", {}) if isinstance(status.get("promotion", {}), dict) else {}
    case_hardening = status.get("case_hardening", {}) if isinstance(status.get("case_hardening", {}), dict) else {}
    case_autoreview = status.get("case_autoreview", {}) if isinstance(status.get("case_autoreview", {}), dict) else {}
    def bulk_missing(name: str) -> Any:
        task = bulk_tasks.get(name, {}) if isinstance(bulk_tasks.get(name, {}), dict) else {}
        return task.get("missing_rows")

    return {
        "count": local_obscure.get("count"),
        "review_candidate_rows": review.get("candidate_rows"),
        "direct_source_queue_rows": review.get("direct_source_queue_rows"),
        "direct_source_missing_rows": review.get("direct_source_missing_rows"),
        "bulk_current_output_clean": bulk.get("current_output_clean"),
        "bulk_parent_source_missing_rows": bulk_missing("parent_source_extraction"),
        "bulk_translation_missing_rows": bulk_missing("bulk_translation_review"),
        "bulk_translation_parent_source_missing_rows": bulk_missing("translation_parent_source_extraction"),
        "promotion_packet_rows": promotion.get("packet_rows"),
        "case_autoreview_rows": case_autoreview.get("rows"),
        "case_autoreview_paid_token_required_rows": case_autoreview.get("paid_token_required_rows"),
        "case_autoreview_human_acceptance_required_rows": case_autoreview.get("human_acceptance_required_rows"),
        "case_final_obscure_ai_promoted_rows": case_hardening.get("final_obscure_ai_promoted_rows"),
    }


def only_keys(data: dict[str, Any], keys: dict[str, Any]) -> dict[str, Any]:
    return {key: data.get(key) for key in keys}


def build(frontend_root: Path, project_root: Path, timeout: int) -> dict[str, Any]:
    local_limen = limen_metrics(read_json(frontend_root / "sites/limen-observatory/data/limen-snapshot.json"))
    local_obscure = obscure_metrics(read_json(frontend_root / "sites/obscure-ai/data/cases.json"))
    project_status = compact_status(project_root, timeout)
    project_limen = project_limen_metrics(project_status) if project_status else {}
    project_obscure = project_obscure_metrics(project_status, local_obscure) if project_status else {}
    live_limen_raw, live_limen_url = fetch_json(LIMEN_URL, timeout)
    live_obscure_raw, live_obscure_url = fetch_json(OBSCURE_URL, timeout)
    live_limen = limen_metrics(live_limen_raw)
    live_obscure = obscure_metrics(live_obscure_raw)

    blockers: list[dict[str, Any]] = []
    warnings: list[dict[str, Any]] = []
    infos: list[dict[str, Any]] = []
    for name, local, live in (("limen", local_limen, live_limen), ("obscure_ai", local_obscure, live_obscure)):
        new_blockers, new_warnings, new_infos = compare(name, local, live)
        blockers.extend(new_blockers)
        warnings.extend(new_warnings)
        infos.extend(new_infos)
    for name, local, project in (
        ("limen", only_keys(local_limen, project_limen), project_limen),
        ("obscure_ai", only_keys(local_obscure, project_obscure), project_obscure),
    ):
        if project:
            new_blockers, new_warnings, new_infos = compare(name, local, project, other_label="project")
            blockers.extend(new_blockers)
            warnings.extend(new_warnings)
            infos.extend(new_infos)
        else:
            warnings.append({"code": f"{name}_project_status_missing", "message": "Current LIMEN project compact status could not be read."})

    return {
        "generated_at_utc": utc_now(),
        "ok": not blockers,
        "blockers": blockers,
        "warnings": warnings,
        "infos": infos,
        "limen": {
            "url": LIMEN_URL,
            "resolved_url": live_limen_url,
            "local": local_limen,
            "live": live_limen,
        },
        "obscure_ai": {
            "url": OBSCURE_URL,
            "resolved_url": live_obscure_url,
            "local": local_obscure,
            "live": live_obscure,
        },
        "project": {
            "root": str(project_root),
            "limen": project_limen,
            "obscure_ai": project_obscure,
        },
        "boundary": "Production JSON availability plus local frontend freshness versus current LIMEN compact counters; not a content-quality or completeness claim.",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--frontend-root", default=str(DEFAULT_FRONTEND_ROOT))
    parser.add_argument("--project-root", default=str(DEFAULT_PROJECT_ROOT))
    parser.add_argument("--timeout", type=int, default=30)
    parser.add_argument("--pretty", action="store_true")
    args = parser.parse_args()
    payload = build(Path(args.frontend_root), Path(args.project_root), args.timeout)
    print(json.dumps(payload, ensure_ascii=False, indent=2 if args.pretty else None, sort_keys=True))
    return 0 if payload["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
