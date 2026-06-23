#!/usr/bin/env python3
"""Check LIMEN/ObscureAI runtime sessions without starting mining."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


PROJECT_ROOT = Path("/srv/tyche/projects/limen-ai-edge-case-atlas")
FRONTEND_ROOT = Path("/srv/tyche/local-projects/home-anton-projects/tyche-research-vault")
PAUSE_FILENAME = "PAUSE-limen-obscure-runtime"

REQUIRED_SESSIONS = [
    "limen-runtime-autostart",
    "limen-quiet-monitor",
    "limen-hermes-lane-supervisor",
    "limen-review-candidate-materializer",
    "limen-observatory-refresh",
    "obscure-ai-observatory-refresh",
]

CPU_MINER_SESSIONS = [
    "limen-cpu-miner-health-finance-education",
    "limen-cpu-miner-identity-provenance",
    "limen-cpu-miner-legal-research",
    "limen-cpu-miner-public-sector",
    "limen-cpu-miner-residual-weird",
    "limen-cpu-miner-security",
]

LOG_CHECKS = [
    (PROJECT_ROOT / "logs/limen-runtime-autostart.jsonl", 300),
    (PROJECT_ROOT / "logs/limen-runtime-bootstrap.log", 900),
    (PROJECT_ROOT / "logs/limen-runtime-housekeeping.jsonl", 7200),
    (PROJECT_ROOT / "logs/limen-quiet-monitor.jsonl", 900),
    (PROJECT_ROOT / "logs/limen-hermes-lane-supervisor.log", 900),
    (PROJECT_ROOT / "logs/review-candidate-materializer.log", 900),
    (FRONTEND_ROOT / "logs/limen-observatory-refresh.log", 1200),
    (FRONTEND_ROOT / "logs/obscure-ai-observatory-refresh.log", 1200),
]

LOG_FAILURE_CHECKS = [
    {
        "path": PROJECT_ROOT / "logs/limen-hermes-lane-supervisor.log",
        "patterns": [
            ("hermes_auth_missing", r"not logged into openai codex|run `hermes model` or configure|no credentials", "blocker"),
            ("hermes_auth_error", r"authentication|unauthorized|invalid api key|permission denied", "blocker"),
            ("hermes_quota_backoff", r"\b429\b|usage limit|quota", "warning"),
            ("hermes_traceback", r"traceback|fatal:|command not found|no such file or directory", "blocker"),
        ],
    },
    {
        "path": PROJECT_ROOT / "logs/review-candidate-materializer.log",
        "patterns": [
            ("materializer_runtime_error", r"traceback|fatal:|permission denied|command not found|no such file or directory", "blocker"),
        ],
    },
    {
        "path": FRONTEND_ROOT / "logs/limen-observatory-refresh.log",
        "patterns": [
            ("limen_frontend_build_or_deploy_failed", r"build or validation failed|deploy failed", "blocker"),
            ("limen_frontend_runtime_error", r"traceback|fatal:|permission denied|command not found|no such file or directory", "blocker"),
        ],
    },
    {
        "path": FRONTEND_ROOT / "logs/obscure-ai-observatory-refresh.log",
        "patterns": [
            ("obscure_ai_frontend_build_or_deploy_failed", r"build or validation failed|deploy failed", "blocker"),
            ("obscure_ai_frontend_runtime_error", r"traceback|fatal:|permission denied|command not found|no such file or directory", "blocker"),
        ],
    },
]
LOG_FAILURE_TAIL_LINES = 160


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def tmux_sessions() -> list[str]:
    try:
        proc = subprocess.run(["tmux", "ls"], text=True, capture_output=True, timeout=8)
    except Exception:
        return []
    if proc.returncode != 0:
        return []
    return sorted(line.split(":", 1)[0] for line in proc.stdout.splitlines() if line.strip())


def process_matches() -> list[dict[str, Any]]:
    patterns = ("tyche-limen-cpu-miner", "limen_cpu", "limen-cpu-miner")
    diagnostic_fragments = (
        "limen_runtime_health_check.py",
        "CPU_MINER_HITS",
        "pgrep",
        "grep ",
        "rg ",
        "tmux ls",
        "ps -eo",
    )
    matches: list[dict[str, Any]] = []
    try:
        proc = subprocess.run(["ps", "-eo", "pid,args"], text=True, capture_output=True, timeout=8)
    except Exception:
        return matches
    for line in proc.stdout.splitlines()[1:]:
        line = line.strip()
        if not line:
            continue
        try:
            pid_text, args = line.split(None, 1)
        except ValueError:
            continue
        if any(fragment in args for fragment in diagnostic_fragments):
            continue
        if any(pattern in args for pattern in patterns) and "STOP-limen-cpu-miner" not in args:
            matches.append({"pid": int(pid_text), "args": args[:500]})
    return matches


def log_status(path: Path, max_age_seconds: int) -> dict[str, Any]:
    if not path.exists():
        return {
            "path": str(path),
            "exists": False,
            "age_seconds": None,
            "max_age_seconds": max_age_seconds,
            "fresh": False,
        }
    age = max(0, int(time.time() - path.stat().st_mtime))
    return {
        "path": str(path),
        "exists": True,
        "age_seconds": age,
        "max_age_seconds": max_age_seconds,
        "fresh": age <= max_age_seconds,
    }


def read_tail_lines(path: Path, limit: int) -> list[str]:
    try:
        with path.open("r", encoding="utf-8", errors="replace") as fh:
            lines = fh.readlines()
    except Exception:
        return []
    return [line.rstrip("\n") for line in lines[-limit:]]


def log_failure_issues(project_root: Path, frontend_root: Path) -> list[dict[str, Any]]:
    issues: list[dict[str, Any]] = []
    for check in LOG_FAILURE_CHECKS:
        path = check["path"]
        adjusted = path
        if str(path).startswith(str(PROJECT_ROOT)):
            adjusted = project_root / path.relative_to(PROJECT_ROOT)
        elif str(path).startswith(str(FRONTEND_ROOT)):
            adjusted = frontend_root / path.relative_to(FRONTEND_ROOT)
        if not adjusted.exists():
            continue
        lines = read_tail_lines(adjusted, LOG_FAILURE_TAIL_LINES)
        for code, pattern, severity in check["patterns"]:
            compiled = re.compile(pattern, re.IGNORECASE)
            for line in reversed(lines):
                if compiled.search(line):
                    issues.append(
                        {
                            "code": code,
                            "severity": severity,
                            "path": str(adjusted),
                            "tail_lines_scanned": len(lines),
                            "matched_pattern": pattern,
                            "line": line[-500:],
                            "boundary": "Recent log-tail semantic check; confirms likely active runtime/auth/quota/build failures only.",
                        }
                    )
                    break
    return issues


def crontab_text() -> str:
    try:
        proc = subprocess.run(["crontab", "-l"], text=True, capture_output=True, timeout=8)
    except Exception:
        return ""
    if proc.returncode != 0:
        return ""
    return proc.stdout


def bootstrap_cron_status(project_root: Path) -> dict[str, Any]:
    text = crontab_text()
    bootstrap = str(project_root / "tools" / "limen_runtime_bootstrap.sh")
    lines = [line.strip() for line in text.splitlines() if bootstrap in line]
    return {
        "bootstrap_script": bootstrap,
        "lines": lines,
        "has_reboot": any(line.startswith("@reboot") for line in lines),
        "has_periodic": any(line.startswith("*/5 ") or line.startswith("*/10 ") for line in lines),
    }


def housekeeping_cron_status(project_root: Path) -> dict[str, Any]:
    text = crontab_text()
    housekeeping = str(project_root / "tools" / "limen_runtime_housekeeping.py")
    lines = [line.strip() for line in text.splitlines() if housekeeping in line]
    return {
        "housekeeping_script": housekeeping,
        "lines": lines,
        "has_periodic": bool(lines),
    }


def run_hermes_readiness(project_root: Path) -> dict[str, Any]:
    try:
        proc = subprocess.run(
            [str(project_root / "tools" / "limen_hermes_readiness.py")],
            cwd=project_root,
            text=True,
            capture_output=True,
            timeout=30,
        )
    except Exception as exc:
        return {
            "generated_at_utc": utc_now(),
            "ok": False,
            "blockers": [{"code": "hermes_readiness_check_failed", "message": str(exc)}],
            "warnings": [],
        }
    if not proc.stdout.strip():
        return {
            "generated_at_utc": utc_now(),
            "ok": False,
            "blockers": [
                {
                    "code": "hermes_readiness_check_no_output",
                    "message": proc.stderr.strip() or "limen_hermes_readiness.py produced no output",
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
            "blockers": [{"code": "hermes_readiness_check_unreadable", "message": str(exc)}],
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


def build(project_root: Path, frontend_root: Path, required_sessions: list[str]) -> dict[str, Any]:
    sessions = tmux_sessions()
    session_set = set(sessions)
    blockers: list[dict[str, Any]] = []
    warnings: list[dict[str, Any]] = []
    pause_file = project_root / "runtime" / PAUSE_FILENAME
    paused = pause_file.exists()

    missing_required = sorted(session for session in required_sessions if session not in session_set)
    if missing_required and not paused:
        add_blocker(blockers, "required_tmux_sessions_missing", "Required LIMEN/ObscureAI monitor sessions are missing.", missing_required)
    if paused:
        still_running = sorted(session for session in required_sessions if session in session_set)
        if still_running:
            add_warning(
                warnings,
                "runtime_pause_sessions_still_running",
                "Runtime pause guard is present but some LIMEN/ObscureAI sessions are still running.",
                still_running,
            )

    cpu_sessions = sorted(session for session in sessions if session.startswith("limen-cpu-miner-"))
    if cpu_sessions:
        add_blocker(blockers, "cpu_mining_tmux_sessions_running", "CPU mining tmux sessions are running.", cpu_sessions)

    cpu_processes = process_matches()
    if cpu_processes:
        add_blocker(blockers, "cpu_mining_processes_running", "CPU mining processes are running.", cpu_processes)

    expected_stop_files = [Path("/srv/tyche") / f"STOP-{session}" for session in CPU_MINER_SESSIONS]
    missing_stop_files = [str(path) for path in expected_stop_files if not path.exists()]
    if missing_stop_files:
        add_warning(warnings, "cpu_mining_stop_files_missing", "Some CPU-miner STOP guard files are missing.", missing_stop_files)

    log_checks = []
    for path, max_age in LOG_CHECKS:
        adjusted = path
        if str(path).startswith(str(PROJECT_ROOT)):
            adjusted = project_root / path.relative_to(PROJECT_ROOT)
        elif str(path).startswith(str(FRONTEND_ROOT)):
            adjusted = frontend_root / path.relative_to(FRONTEND_ROOT)
        status = log_status(adjusted, max_age)
        log_checks.append(status)
        if paused:
            continue
        if not status["exists"]:
            add_warning(warnings, "runtime_log_missing", "Runtime heartbeat log is missing.", str(adjusted))
        elif not status["fresh"]:
            add_warning(warnings, "runtime_log_stale", "Runtime heartbeat log is stale.", status)

    log_failure_checks = [] if paused else log_failure_issues(project_root, frontend_root)
    for issue in log_failure_checks:
        if issue.get("severity") == "blocker":
            add_blocker(blockers, issue.get("code", "runtime_log_failure"), "Recent runtime log contains a failure pattern.", issue)
        else:
            add_warning(warnings, issue.get("code", "runtime_log_warning"), "Recent runtime log contains a warning pattern.", issue)

    cron_status = bootstrap_cron_status(project_root)
    if not cron_status["has_reboot"] and not paused:
        add_blocker(blockers, "runtime_bootstrap_reboot_cron_missing", "LIMEN runtime bootstrap @reboot cron entry is missing.", cron_status)
    if not cron_status["has_periodic"] and not paused:
        add_blocker(blockers, "runtime_bootstrap_periodic_cron_missing", "LIMEN runtime periodic bootstrap cron entry is missing.", cron_status)
    housekeeping_cron = housekeeping_cron_status(project_root)
    if not housekeeping_cron["has_periodic"] and not paused:
        add_blocker(
            blockers,
            "runtime_housekeeping_cron_missing",
            "LIMEN runtime housekeeping cron entry is missing.",
            housekeeping_cron,
        )

    hermes_readiness = (
        {
            "ok": True,
            "generated_at_utc": utc_now(),
            "paused": True,
            "backlog": {},
            "supervisor": {},
            "lanes": {},
            "hermes": {},
            "infos": [
                {
                    "code": "runtime_paused",
                    "message": "LIMEN/ObscureAI runtime pause guard is present; Hermes lane readiness is not checked while paused.",
                }
            ],
        }
        if paused
        else run_hermes_readiness(project_root)
    )
    for blocker in hermes_readiness.get("blockers", []) if isinstance(hermes_readiness, dict) else []:
        if isinstance(blocker, dict):
            add_blocker(blockers, blocker.get("code", "hermes_readiness_blocker"), "Hermes readiness check found a blocker.", blocker)
    for warning in hermes_readiness.get("warnings", []) if isinstance(hermes_readiness, dict) else []:
        if isinstance(warning, dict):
            add_warning(warnings, warning.get("code", "hermes_readiness_warning"), "Hermes readiness check found a warning.", warning)

    return {
        "generated_at_utc": utc_now(),
        "ok": not blockers,
        "paused": paused,
        "pause_file": str(pause_file),
        "blockers": blockers,
        "warnings": warnings,
        "sessions": sessions,
        "required_sessions": required_sessions,
        "missing_required_sessions": missing_required,
        "cpu_mining_sessions": cpu_sessions,
        "cpu_mining_processes": cpu_processes,
        "cpu_mining_stop_files_present": len(expected_stop_files) - len(missing_stop_files),
        "cpu_mining_stop_files_expected": len(expected_stop_files),
        "log_checks": log_checks,
        "log_failure_checks": log_failure_checks,
        "autonomy": {
            "bootstrap_cron": cron_status,
            "housekeeping_cron": housekeeping_cron,
        },
        "hermes_readiness": {
            "ok": hermes_readiness.get("ok"),
            "generated_at_utc": hermes_readiness.get("generated_at_utc"),
            "backlog": hermes_readiness.get("backlog", {}),
            "supervisor": hermes_readiness.get("supervisor", {}),
            "lanes": hermes_readiness.get("lanes", {}),
            "hermes": {
                "binary": (hermes_readiness.get("hermes", {}) or {}).get("binary", {}),
                "config": (hermes_readiness.get("hermes", {}) or {}).get("config", {}),
                "auth": (hermes_readiness.get("hermes", {}) or {}).get("auth", {}),
            },
            "infos": hermes_readiness.get("infos", []),
        },
        "boundary": "Runtime session/heartbeat/log-tail check only; it does not start mining, Hermes lanes, processing, or deploys.",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--project-root", default=str(PROJECT_ROOT))
    parser.add_argument("--frontend-root", default=str(FRONTEND_ROOT))
    parser.add_argument("--required-session", action="append", default=[])
    parser.add_argument("--pretty", action="store_true")
    args = parser.parse_args()
    required = args.required_session or REQUIRED_SESSIONS
    payload = build(Path(args.project_root), Path(args.frontend_root), required)
    print(json.dumps(payload, ensure_ascii=False, indent=2 if args.pretty else None, sort_keys=True))
    return 0 if payload["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
