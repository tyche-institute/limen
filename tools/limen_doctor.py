#!/usr/bin/env python3
"""Compact LIMEN/ObscureAI operational doctor.

Runs existing read-only verifiers and writes one low-token status JSON.
"""

from __future__ import annotations

import argparse
import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


PROJECT_ROOT = Path("/srv/tyche/projects/limen-ai-edge-case-atlas")
FRONTEND_ROOT = Path("/srv/tyche/local-projects/home-anton-projects/tyche-research-vault")
LATEST = PROJECT_ROOT / "runtime" / "limen-doctor-status-latest.json"


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def iv(value: Any) -> int:
    try:
        return int(value or 0)
    except Exception:
        return 0


def run_json(cmd: list[str], cwd: Path, timeout: int) -> tuple[dict[str, Any], dict[str, Any] | None]:
    try:
        proc = subprocess.run(cmd, cwd=cwd, text=True, capture_output=True, timeout=timeout)
    except Exception as exc:
        return {}, {"cmd": cmd, "error": str(exc), "returncode": None}
    if proc.returncode != 0:
        return {}, {
            "cmd": cmd,
            "returncode": proc.returncode,
            "stderr": proc.stderr.strip()[-1000:],
            "stdout": proc.stdout.strip()[-1000:],
        }
    try:
        return json.loads(proc.stdout), None
    except Exception as exc:
        return {}, {"cmd": cmd, "error": str(exc), "stdout": proc.stdout.strip()[-1000:]}


def read_json(path: Path) -> dict[str, Any]:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return {}


def compact_counts(status: dict[str, Any]) -> dict[str, Any]:
    review = status.get("review", {}) if isinstance(status.get("review", {}), dict) else {}
    bulk = status.get("bulk", {}) if isinstance(status.get("bulk", {}), dict) else {}
    promotion = status.get("promotion", {}) if isinstance(status.get("promotion", {}), dict) else {}
    case_autoreview = status.get("case_autoreview", {}) if isinstance(status.get("case_autoreview", {}), dict) else {}
    case_extraction = status.get("case_extraction", {}) if isinstance(status.get("case_extraction", {}), dict) else {}
    hardening = status.get("hardening", {}) if isinstance(status.get("hardening", {}), dict) else {}
    bulk_tasks = bulk.get("tasks", {}) if isinstance(bulk.get("tasks", {}), dict) else {}
    return {
        "review_candidates": iv(review.get("candidate_rows")),
        "first_pass_reviewed": iv(review.get("first_pass_reviewed_rows")),
        "direct_source_queue": iv(review.get("direct_source_queue_rows")),
        "direct_source_missing": iv(review.get("direct_source_missing_rows")),
        "bulk_clean": bool(bulk.get("current_output_clean")),
        "bulk_missing": sum(iv(task.get("missing_rows")) for task in bulk_tasks.values() if isinstance(task, dict)),
        "hardening_clean": bool(hardening.get("current_output_clean")),
        "case_extraction_clean": bool(case_extraction.get("current_output_clean")),
        "case_extraction_missing": iv(case_extraction.get("missing_rows")),
        "promotion_packet_rows": iv(promotion.get("packet_rows")),
        "promotion_source_clusters": iv(promotion.get("source_clusters")),
        "obscure_ai_ready_now": iv(promotion.get("obscure_ai_ready_now")),
        "case_autoreview_rows": iv(case_autoreview.get("rows")),
        "case_autoreview_paid_token_rows": iv(case_autoreview.get("paid_token_required_rows")),
        "case_autoreview_human_acceptance_rows": iv(case_autoreview.get("human_acceptance_required_rows")),
    }


def merge_public_counts(counts: dict[str, Any], public: dict[str, Any]) -> None:
    if not isinstance(public, dict) or not public:
        return

    obscure = public.get("obscure_ai", {}) if isinstance(public.get("obscure_ai", {}), dict) else {}
    project = public.get("project", {}) if isinstance(public.get("project", {}), dict) else {}
    project_obscure = project.get("obscure_ai", {}) if isinstance(project.get("obscure_ai", {}), dict) else {}

    local_obscure = obscure.get("local", {}) if isinstance(obscure.get("local", {}), dict) else {}
    live_obscure = obscure.get("live", {}) if isinstance(obscure.get("live", {}), dict) else {}
    counts["obscure_ai_local_case_rows"] = iv(local_obscure.get("count"))
    counts["obscure_ai_live_case_rows"] = iv(live_obscure.get("count"))
    counts["obscure_ai_project_case_rows"] = iv(project_obscure.get("count"))


def build(project_root: Path, frontend_root: Path) -> dict[str, Any]:
    errors: list[dict[str, Any]] = []
    compact, error = run_json([str(project_root / "tools" / "limen_compact_status.py")], project_root, 60)
    if error:
        errors.append({"check": "compact_status", **error})
    public, error = run_json(
        [
            str(project_root / "tools" / "limen_public_snapshot_check.py"),
            "--frontend-root",
            str(frontend_root),
            "--project-root",
            str(project_root),
        ],
        project_root,
        90,
    )
    if error:
        errors.append({"check": "public_snapshot", **error})
    runtime, error = run_json(
        [
            str(project_root / "tools" / "limen_runtime_health_check.py"),
            "--project-root",
            str(project_root),
            "--frontend-root",
            str(frontend_root),
        ],
        project_root,
        30,
    )
    if error:
        errors.append({"check": "runtime_health", **error})
    token_free_audit, error = run_json(
        [str(project_root / "tools" / "limen_token_free_review_audit.py")],
        project_root,
        30,
    )
    if error:
        errors.append({"check": "token_free_review_audit", **error})
    no_token = read_json(project_root / "runtime" / "limen-case-review-no-tokens-status-latest.json")

    blockers: list[dict[str, Any]] = []
    warnings: list[dict[str, Any]] = []
    for name, payload in (("public", public), ("runtime", runtime)):
        for blocker in payload.get("blockers", []) if isinstance(payload, dict) else []:
            if isinstance(blocker, dict):
                blockers.append({"source": name, **blocker})
        for warning in payload.get("warnings", []) if isinstance(payload, dict) else []:
            if isinstance(warning, dict):
                warnings.append({"source": name, **warning})
    if errors:
        blockers.extend({"source": error.pop("check", "doctor"), **error} for error in errors)

    counts = compact_counts(compact)
    merge_public_counts(counts, public)
    if counts.get("case_autoreview_paid_token_rows"):
        warnings.append({"source": "case_autoreview", "code": "paid_tokens_needed"})
    if token_free_audit.get("current_paid_token_required_rows"):
        warnings.append(
            {
                "source": "token_free_review_audit",
                "code": "paid_token_review_rows",
                "rows": token_free_audit.get("current_paid_token_required_rows"),
            }
        )
    if no_token and not no_token.get("ok", False):
        warnings.append({"source": "no_token_case_review", "code": "not_ok"})

    return {
        "generated_at_utc": utc_now(),
        "ok": not blockers,
        "blockers": blockers,
        "warnings": warnings,
        "counts": counts,
        "runtime": {
            "ok": runtime.get("ok"),
            "required_sessions": runtime.get("required_sessions", []),
            "missing_required_sessions": runtime.get("missing_required_sessions", []),
            "cpu_mining_sessions": runtime.get("cpu_mining_sessions", []),
            "cpu_mining_processes": runtime.get("cpu_mining_processes", []),
            "log_failure_checks": runtime.get("log_failure_checks", []),
            "hermes_readiness": runtime.get("hermes_readiness", {}),
        },
        "public": {
            "ok": public.get("ok"),
            "infos": public.get("infos", []),
        },
        "no_token_case_review": {
            "ok": no_token.get("ok"),
            "generated_at_utc": no_token.get("generated_at_utc"),
            "case_autoreview": no_token.get("case_autoreview", {}),
        },
        "token_free_review_audit": {
            "ok": token_free_audit.get("ok"),
            "generated_at_utc": token_free_audit.get("generated_at_utc"),
            "current_paid_token_required_rows": token_free_audit.get("current_paid_token_required_rows"),
            "current_human_required_rows": token_free_audit.get("current_human_required_rows"),
            "current_missing_review_rows": token_free_audit.get("current_missing_review_rows"),
            "incomplete_layers": token_free_audit.get("incomplete_layers", []),
        },
        "boundary": "Read-only verifier aggregation; does not start mining, process queues, call models, or deploy.",
    }


def write_json(path: Path, payload: dict[str, Any], pretty: bool) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(payload, ensure_ascii=False, indent=2 if pretty else None, sort_keys=True) + "\n", encoding="utf-8")
    tmp.replace(path)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--project-root", default=str(PROJECT_ROOT))
    parser.add_argument("--frontend-root", default=str(FRONTEND_ROOT))
    parser.add_argument("--out", default=str(LATEST))
    parser.add_argument("--pretty", action="store_true")
    args = parser.parse_args()
    payload = build(Path(args.project_root), Path(args.frontend_root))
    write_json(Path(args.out), payload, pretty=True)
    print(json.dumps(payload, ensure_ascii=False, indent=2 if args.pretty else None, sort_keys=True))
    return 0 if payload["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
