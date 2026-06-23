#!/usr/bin/env python3
"""Write compact LIMEN status and alerts for low-token monitoring."""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


DEFAULT_ROOT = Path("/srv/tyche/projects/limen-ai-edge-case-atlas")


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def iv(value: Any) -> int:
    try:
        return int(value or 0)
    except Exception:
        return 0


def get_path(data: dict[str, Any], *parts: str, default: Any = None) -> Any:
    value: Any = data
    for part in parts:
        if not isinstance(value, dict):
            return default
        value = value.get(part)
    return default if value is None else value


def write_json_atomic(path: Path, payload: dict[str, Any], *, pretty: bool = True) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2 if pretty else None, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    tmp.replace(path)


def append_jsonl(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(payload, ensure_ascii=False, sort_keys=True) + "\n")


def run_status(project_root: Path) -> dict[str, Any]:
    proc = subprocess.run(
        [str(project_root / "tools" / "limen_compact_status.py")],
        cwd=project_root,
        text=True,
        capture_output=True,
        timeout=60,
    )
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr.strip() or proc.stdout.strip() or "limen_compact_status.py failed")
    return json.loads(proc.stdout)


def run_public_snapshot_check(project_root: Path, frontend_root: Path) -> dict[str, Any]:
    proc = subprocess.run(
        [
            str(project_root / "tools" / "limen_public_snapshot_check.py"),
            "--frontend-root",
            str(frontend_root),
        ],
        cwd=project_root,
        text=True,
        capture_output=True,
        timeout=90,
    )
    if not proc.stdout.strip():
        return {
            "generated_at_utc": utc_now(),
            "ok": False,
            "blockers": [
                {
                    "code": "public_snapshot_check_failed",
                    "message": proc.stderr.strip() or "limen_public_snapshot_check.py produced no output",
                }
            ],
            "warnings": [],
        }
    try:
        return json.loads(proc.stdout)
    except Exception as exc:
        return {
            "generated_at_utc": utc_now(),
            "ok": False,
            "blockers": [{"code": "public_snapshot_check_unreadable", "message": str(exc)}],
            "warnings": [],
        }


def run_runtime_health_check(project_root: Path, frontend_root: Path) -> dict[str, Any]:
    proc = subprocess.run(
        [
            str(project_root / "tools" / "limen_runtime_health_check.py"),
            "--project-root",
            str(project_root),
            "--frontend-root",
            str(frontend_root),
        ],
        cwd=project_root,
        text=True,
        capture_output=True,
        timeout=30,
    )
    if not proc.stdout.strip():
        return {
            "generated_at_utc": utc_now(),
            "ok": False,
            "blockers": [
                {
                    "code": "runtime_health_check_failed",
                    "message": proc.stderr.strip() or "limen_runtime_health_check.py produced no output",
                }
            ],
            "warnings": [],
        }
    try:
        return json.loads(proc.stdout)
    except Exception as exc:
        return {
            "generated_at_utc": utc_now(),
            "ok": False,
            "blockers": [{"code": "runtime_health_check_unreadable", "message": str(exc)}],
            "warnings": [],
        }


def run_token_free_review_audit(project_root: Path) -> dict[str, Any]:
    proc = subprocess.run(
        [str(project_root / "tools" / "limen_token_free_review_audit.py")],
        cwd=project_root,
        text=True,
        capture_output=True,
        timeout=30,
    )
    if not proc.stdout.strip():
        return {
            "generated_at_utc": utc_now(),
            "ok": False,
            "blockers": [
                {
                    "code": "token_free_review_audit_failed",
                    "message": proc.stderr.strip() or "limen_token_free_review_audit.py produced no output",
                }
            ],
            "warnings": [],
        }
    try:
        return json.loads(proc.stdout)
    except Exception as exc:
        return {
            "generated_at_utc": utc_now(),
            "ok": False,
            "blockers": [{"code": "token_free_review_audit_unreadable", "message": str(exc)}],
            "warnings": [],
        }


def add_blocker(blockers: list[dict[str, Any]], code: str, message: str, value: Any = None) -> None:
    item: dict[str, Any] = {"code": code, "message": message}
    if value is not None:
        item["value"] = value
    blockers.append(item)


def add_warning(warnings: list[dict[str, Any]], code: str, message: str, value: Any = None) -> None:
    item: dict[str, Any] = {"code": code, "message": message}
    if value is not None:
        item["value"] = value
    warnings.append(item)


def build_alert(status: dict[str, Any]) -> dict[str, Any]:
    blockers: list[dict[str, Any]] = []
    warnings: list[dict[str, Any]] = []

    mining_sessions = get_path(status, "mining", "running_sessions", default=[]) or []
    if mining_sessions:
        add_blocker(blockers, "cpu_mining_running", "CPU mining is running and should remain stopped.", mining_sessions)

    candidate_rows = iv(get_path(status, "review", "candidate_rows"))
    first_pass_rows = iv(get_path(status, "review", "first_pass_reviewed_rows"))
    if candidate_rows > first_pass_rows:
        add_blocker(
            blockers,
            "first_pass_review_missing",
            "Some review candidates still need first-pass review.",
            candidate_rows - first_pass_rows,
        )

    direct_missing = iv(get_path(status, "review", "direct_source_missing_rows"))
    if direct_missing:
        add_blocker(blockers, "direct_source_missing", "Direct-source review has missing rows.", direct_missing)

    hardening_clean = bool(get_path(status, "hardening", "current_output_clean", default=False))
    hardening_url_missing = iv(get_path(status, "hardening", "url", "missing_rows"))
    hardening_translation_missing = iv(get_path(status, "hardening", "translation", "missing_rows"))
    if hardening_url_missing:
        add_blocker(blockers, "hardening_url_missing", "Named-URL hardening has missing rows.", hardening_url_missing)
    if hardening_translation_missing:
        add_blocker(
            blockers,
            "hardening_translation_missing",
            "Translation-source hardening has missing rows.",
            hardening_translation_missing,
        )
    if not hardening_clean:
        add_blocker(blockers, "hardening_not_clean", "Hardening rollup is not clean.")

    # Historical complete batches can contain rows from superseded queues. The
    # rollup filters them out of current outputs, so alert only on active
    # incompleteness above, not on audit-trail artifacts.

    bulk_clean = bool(get_path(status, "bulk", "current_output_clean", default=False))
    if not bulk_clean:
        add_blocker(blockers, "bulk_not_clean", "Bulk review rollup is not clean.")
    bulk_tasks = get_path(status, "bulk", "tasks", default={}) or {}
    if isinstance(bulk_tasks, dict):
        for name, task in sorted(bulk_tasks.items()):
            if not isinstance(task, dict):
                continue
            missing = iv(task.get("missing_rows"))
            if missing:
                add_blocker(blockers, f"bulk_{name}_missing", f"Bulk task {name} has missing rows.", missing)

    case_clean = bool(get_path(status, "case_extraction", "current_output_clean", default=False))
    case_missing = iv(get_path(status, "case_extraction", "missing_rows"))
    if case_missing:
        add_blocker(blockers, "case_extraction_missing", "Reviewed-core case extraction has missing rows.", case_missing)
    if not case_clean:
        add_blocker(blockers, "case_extraction_not_clean", "Reviewed-core case extraction rollup is not clean.")

    ready_for_human = iv(get_path(status, "case_hardening", "ready_for_human_acceptance"))
    if ready_for_human:
        add_warning(
            warnings,
            "case_hardening_human_acceptance_pending",
            "Some case-hardening rows need human acceptance before promotion.",
            ready_for_human,
        )
    case_paid_token_rows = iv(get_path(status, "case_autoreview", "paid_token_required_rows"))
    case_auto_close_rows = iv(get_path(status, "case_autoreview", "token_free_auto_close_rows"))
    case_auto_promote_rows = iv(get_path(status, "case_autoreview", "token_free_promotion_candidate_rows"))
    if case_paid_token_rows:
        add_warning(
            warnings,
            "case_autoreview_paid_tokens_needed",
            "Case autoreview found rows that still need model-backed reading.",
            case_paid_token_rows,
        )

    packet_rows = iv(get_path(status, "promotion", "packet_rows"))
    source_clusters = iv(get_path(status, "promotion", "source_clusters"))
    obscure_ready = iv(get_path(status, "promotion", "obscure_ai_ready_now"))
    if candidate_rows and not packet_rows:
        add_warning(warnings, "promotion_packet_empty", "Promotion packet is empty despite candidate rows.")

    if blockers:
        next_action = "run tools/limen_process_available_data.sh --deploy-frontends"
    else:
        next_action = "nothing_required"
    if mining_sessions:
        next_action = "run tools/limen_process_available_data.sh --stop-mining --deploy-frontends"

    return {
        "generated_at_utc": utc_now(),
        "ok": not blockers,
        "next_action": next_action,
        "blockers": blockers,
        "warnings": warnings,
        "counts": {
            "candidate_rows": candidate_rows,
            "first_pass_reviewed_rows": first_pass_rows,
            "direct_source_missing_rows": direct_missing,
            "hardening_url_missing_rows": hardening_url_missing,
            "hardening_translation_missing_rows": hardening_translation_missing,
            "bulk_missing_rows": sum(
                iv(task.get("missing_rows"))
                for task in bulk_tasks.values()
                if isinstance(bulk_tasks, dict) and isinstance(task, dict)
            ),
            "case_extraction_missing_rows": case_missing,
            "promotion_packet_rows": packet_rows,
            "promotion_source_clusters": source_clusters,
            "obscure_ai_ready_now": obscure_ready,
            "case_autoreview_paid_token_required_rows": case_paid_token_rows,
            "case_autoreview_token_free_auto_close_rows": case_auto_close_rows,
            "case_autoreview_token_free_promotion_candidate_rows": case_auto_promote_rows,
        },
    }


def merge_token_free_audit(alert: dict[str, Any], audit: dict[str, Any]) -> None:
    if not audit:
        add_blocker(
            alert["blockers"],
            "token_free_review_audit_missing",
            "Token-free review audit did not produce a status payload.",
        )
        alert["ok"] = False
        return

    missing_rows = iv(audit.get("current_missing_review_rows"))
    paid_rows = iv(audit.get("current_paid_token_required_rows"))
    human_rows = iv(audit.get("current_human_required_rows"))
    incomplete_layers = audit.get("incomplete_layers", []) or []

    if missing_rows:
        add_blocker(
            alert["blockers"],
            "token_free_review_missing_rows",
            "Token-free review audit found missing review rows.",
            missing_rows,
        )
    if incomplete_layers:
        add_blocker(
            alert["blockers"],
            "token_free_review_incomplete_layers",
            "Token-free review audit found incomplete layers.",
            incomplete_layers,
        )
    if paid_rows:
        add_warning(
            alert["warnings"],
            "token_free_review_paid_tokens_needed",
            "Some rows cannot be closed by the no-token review path.",
            paid_rows,
        )
    if human_rows:
        add_warning(
            alert["warnings"],
            "token_free_review_human_acceptance_needed",
            "Some rows need human acceptance before promotion.",
            human_rows,
        )

    counts = alert.setdefault("counts", {})
    counts["token_free_paid_token_required_rows"] = paid_rows
    counts["token_free_human_required_rows"] = human_rows
    counts["token_free_missing_review_rows"] = missing_rows
    counts["token_free_incomplete_layers"] = len(incomplete_layers)
    alert["token_free_review_audit"] = {
        "ok": audit.get("ok"),
        "generated_at_utc": audit.get("generated_at_utc"),
        "current_paid_token_required_rows": paid_rows,
        "current_human_required_rows": human_rows,
        "current_missing_review_rows": missing_rows,
        "incomplete_layers": incomplete_layers,
    }
    alert["ok"] = not alert["blockers"]
    if alert["blockers"] and alert.get("next_action") == "nothing_required":
        alert["next_action"] = "run tools/limen_process_available_data.sh --deploy-frontends"


def merge_hermes_readiness(alert: dict[str, Any], runtime_status: dict[str, Any]) -> None:
    readiness = runtime_status.get("hermes_readiness", {}) if isinstance(runtime_status, dict) else {}
    if not isinstance(readiness, dict) or not readiness:
        return

    backlog = readiness.get("backlog", {}) if isinstance(readiness.get("backlog"), dict) else {}
    lanes = readiness.get("lanes", {}) if isinstance(readiness.get("lanes"), dict) else {}
    supervisor = readiness.get("supervisor", {}) if isinstance(readiness.get("supervisor"), dict) else {}
    hermes = readiness.get("hermes", {}) if isinstance(readiness.get("hermes"), dict) else {}
    auth = hermes.get("auth", {}) if isinstance(hermes.get("auth"), dict) else {}
    config = hermes.get("config", {}) if isinstance(hermes.get("config"), dict) else {}

    review_backlog = iv(backlog.get("hermes_review_backlog_rows"))
    active_lanes = iv(lanes.get("active_lane_sessions"))
    supervisor_fresh = bool(supervisor.get("fresh"))
    supervisor_session_present = bool(supervisor.get("session_present"))
    codex_auth_present = bool(
        auth.get("openai_codex_provider_present")
        and auth.get("openai_codex_has_access_token")
        and auth.get("openai_codex_has_refresh_token")
    )

    counts = alert.setdefault("counts", {})
    counts["hermes_review_backlog_rows"] = review_backlog
    counts["hermes_active_lane_sessions"] = active_lanes
    counts["hermes_supervisor_fresh"] = 1 if supervisor_fresh else 0
    counts["hermes_codex_auth_present"] = 1 if codex_auth_present else 0
    counts["hermes_latest_direct_source_backlog"] = iv(supervisor.get("latest_direct_source_backlog"))
    if supervisor.get("cycle_complete_age_seconds") is not None:
        counts["hermes_supervisor_cycle_complete_age_seconds"] = iv(supervisor.get("cycle_complete_age_seconds"))

    alert["hermes_readiness"] = {
        "ok": readiness.get("ok"),
        "generated_at_utc": readiness.get("generated_at_utc"),
        "hermes_review_backlog_rows": review_backlog,
        "active_lane_sessions": active_lanes,
        "supervisor_fresh": supervisor_fresh,
        "supervisor_session_present": supervisor_session_present,
        "latest_cycle_start_utc": supervisor.get("latest_cycle_start_utc", ""),
        "latest_cycle_complete_utc": supervisor.get("latest_cycle_complete_utc", ""),
        "latest_direct_source_backlog": supervisor.get("latest_direct_source_backlog"),
        "openai_codex_auth_present": codex_auth_present,
        "default_provider": config.get("default_provider", ""),
        "fallback_has_openai_codex": bool(config.get("fallback_has_openai_codex")),
    }


def merge_public_snapshot_counts(alert: dict[str, Any], public_status: dict[str, Any]) -> None:
    if not isinstance(public_status, dict) or not public_status:
        return

    counts = alert.setdefault("counts", {})

    obscure_local = get_path(public_status, "obscure_ai", "local", "count")
    obscure_live = get_path(public_status, "obscure_ai", "live", "count")
    obscure_project = get_path(public_status, "project", "obscure_ai", "count")
    limen_live_candidates = get_path(public_status, "limen", "live", "review_candidate_rows")
    limen_live_first_pass = get_path(public_status, "limen", "live", "first_pass_reviewed_rows")

    if obscure_local is not None:
        counts["obscure_ai_local_case_rows"] = iv(obscure_local)
    if obscure_live is not None:
        counts["obscure_ai_live_case_rows"] = iv(obscure_live)
    if obscure_project is not None:
        counts["obscure_ai_project_case_rows"] = iv(obscure_project)
    if limen_live_candidates is not None:
        counts["limen_live_candidate_rows"] = iv(limen_live_candidates)
    if limen_live_first_pass is not None:
        counts["limen_live_first_pass_reviewed_rows"] = iv(limen_live_first_pass)

    alert["public_snapshot"] = {
        "ok": public_status.get("ok"),
        "limen_live_generated_at_utc": get_path(public_status, "limen", "live", "generated_at_utc", default=""),
        "obscure_ai_live_generated_at_utc": get_path(public_status, "obscure_ai", "live", "generated_at_utc", default=""),
        "obscure_ai_live_case_rows": iv(obscure_live),
    }


def process_available_data(project_root: Path, *, deploy_frontends: bool, alert: dict[str, Any], log_path: Path) -> int:
    cmd = [str(project_root / "tools" / "limen_process_available_data.sh")]
    codes = {item.get("code") for item in alert.get("blockers", []) if isinstance(item, dict)}
    if "cpu_mining_running" in codes:
        cmd.append("--stop-mining")
    if deploy_frontends:
        cmd.append("--deploy-frontends")

    append_jsonl(log_path, {"generated_at_utc": utc_now(), "event": "process_start", "cmd": cmd})
    with log_path.open("a", encoding="utf-8") as log:
        log.write(f"[{utc_now()}] run: {' '.join(cmd)}\n")
        proc = subprocess.run(cmd, cwd=project_root, text=True, stdout=log, stderr=subprocess.STDOUT)
    append_jsonl(log_path, {"generated_at_utc": utc_now(), "event": "process_exit", "returncode": proc.returncode})
    return proc.returncode


def monitor_once(args: argparse.Namespace) -> tuple[dict[str, Any], dict[str, Any]]:
    project_root = Path(args.project_root).resolve()
    out_dir = Path(args.out_dir)
    if not out_dir.is_absolute():
        out_dir = project_root / out_dir
    log_path = Path(args.log)
    if not log_path.is_absolute():
        log_path = project_root / log_path
    frontend_root = Path(args.frontend_root).resolve()

    status = run_status(project_root)
    alert = build_alert(status)
    public_status = {}
    runtime_status = {}
    token_free_audit = run_token_free_review_audit(project_root)
    merge_token_free_audit(alert, token_free_audit)

    if args.check_runtime:
        runtime_status = run_runtime_health_check(project_root, frontend_root)
        for blocker in runtime_status.get("blockers", []):
            if isinstance(blocker, dict):
                alert["blockers"].append(blocker)
        for warning in runtime_status.get("warnings", []):
            if isinstance(warning, dict):
                alert["warnings"].append(warning)
        merge_hermes_readiness(alert, runtime_status)
        alert["ok"] = not alert["blockers"]

    if args.check_production:
        public_status = run_public_snapshot_check(project_root, frontend_root)
        merge_public_snapshot_counts(alert, public_status)
        for blocker in public_status.get("blockers", []):
            if isinstance(blocker, dict):
                alert["blockers"].append(blocker)
        for warning in public_status.get("warnings", []):
            if isinstance(warning, dict):
                alert["warnings"].append(warning)
        alert["ok"] = not alert["blockers"]
        if not public_status.get("ok", False):
            alert["next_action"] = "run tools/limen_process_available_data.sh --deploy-frontends"

    if args.process_on_backlog and alert["blockers"]:
        rc = process_available_data(project_root, deploy_frontends=args.deploy_frontends, alert=alert, log_path=log_path)
        status = run_status(project_root)
        alert = build_alert(status)
        token_free_audit = run_token_free_review_audit(project_root)
        merge_token_free_audit(alert, token_free_audit)
        if args.check_runtime:
            runtime_status = run_runtime_health_check(project_root, frontend_root)
            for blocker in runtime_status.get("blockers", []):
                if isinstance(blocker, dict):
                    alert["blockers"].append(blocker)
            for warning in runtime_status.get("warnings", []):
                if isinstance(warning, dict):
                    alert["warnings"].append(warning)
            merge_hermes_readiness(alert, runtime_status)
            alert["ok"] = not alert["blockers"]
        if args.check_production:
            public_status = run_public_snapshot_check(project_root, frontend_root)
            merge_public_snapshot_counts(alert, public_status)
            for blocker in public_status.get("blockers", []):
                if isinstance(blocker, dict):
                    alert["blockers"].append(blocker)
            for warning in public_status.get("warnings", []):
                if isinstance(warning, dict):
                    alert["warnings"].append(warning)
            alert["ok"] = not alert["blockers"]
            if not public_status.get("ok", False):
                alert["next_action"] = "run tools/limen_process_available_data.sh --deploy-frontends"
        alert["last_process_run"] = {"generated_at_utc": utc_now(), "returncode": rc}

    write_json_atomic(out_dir / "limen-compact-status-latest.json", status)
    write_json_atomic(out_dir / "limen-compact-alert-latest.json", alert)
    if args.check_production:
        write_json_atomic(out_dir / "limen-public-snapshot-status-latest.json", public_status)
    if args.check_runtime:
        write_json_atomic(out_dir / "limen-runtime-health-latest.json", runtime_status)
    write_json_atomic(out_dir / "limen-token-free-review-audit-status-latest.json", token_free_audit)
    append_jsonl(log_path, {"generated_at_utc": utc_now(), "event": "monitor", "alert": alert})
    return status, alert


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--project-root", default=os.environ.get("PROJECT_ROOT", str(DEFAULT_ROOT)))
    parser.add_argument(
        "--frontend-root",
        default=os.environ.get("FRONTEND_ROOT", "/srv/tyche/local-projects/home-anton-projects/tyche-research-vault"),
    )
    parser.add_argument("--out-dir", default="runtime")
    parser.add_argument("--log", default="logs/limen-quiet-monitor.jsonl")
    parser.add_argument("--interval", type=int, default=300)
    parser.add_argument("--once", action="store_true")
    parser.add_argument("--max-runs", type=int, default=0, help="0 means unlimited unless --once is set.")
    parser.add_argument("--process-on-backlog", action="store_true")
    parser.add_argument("--deploy-frontends", action="store_true")
    parser.add_argument("--check-production", action="store_true")
    parser.add_argument("--check-runtime", action="store_true")
    parser.add_argument("--pretty", action="store_true")
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    runs = 0
    while True:
        _, alert = monitor_once(args)
        print(json.dumps(alert, ensure_ascii=False, indent=2 if args.pretty else None, sort_keys=True), flush=True)
        runs += 1
        if args.once or (args.max_runs and runs >= args.max_runs):
            return 0 if alert.get("ok") else 1
        time.sleep(max(5, args.interval))


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
