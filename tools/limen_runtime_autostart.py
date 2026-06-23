#!/usr/bin/env python3
"""Restart required LIMEN/ObscureAI runtime sessions without starting mining."""

from __future__ import annotations

import argparse
import json
import subprocess
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


PROJECT_ROOT = Path("/srv/tyche/projects/limen-ai-edge-case-atlas")
FRONTEND_ROOT = Path("/srv/tyche/local-projects/home-anton-projects/tyche-research-vault")
PAUSE_FILE = PROJECT_ROOT / "runtime" / "PAUSE-limen-obscure-runtime"

SESSION_COMMANDS = {
    "limen-quiet-monitor": {
        "cwd": PROJECT_ROOT,
        "cmd": (
            "cd /srv/tyche/projects/limen-ai-edge-case-atlas && "
            "tools/limen_quiet_monitor.py --interval 300 --process-on-backlog "
            "--deploy-frontends --check-production --check-runtime "
            ">> logs/limen-quiet-monitor.out 2>&1"
        ),
    },
    "limen-hermes-lane-supervisor": {
        "cwd": PROJECT_ROOT,
        "cmd": (
            "cd /srv/tyche/projects/limen-ai-edge-case-atlas && "
            "tools/limen-hermes-lane-supervisor.sh >> logs/limen-hermes-lane-supervisor.out 2>&1"
        ),
    },
    "limen-review-candidate-materializer": {
        "cwd": PROJECT_ROOT,
        "cmd": (
            "cd /srv/tyche/projects/limen-ai-edge-case-atlas && "
            "env LIMEN_REVIEW_CANDIDATE_WATCHER_SLEEP_SECONDS=120 "
            "tools/review_candidate_watcher.sh >> logs/review-candidate-materializer.out 2>&1"
        ),
    },
    "limen-observatory-refresh": {
        "cwd": FRONTEND_ROOT,
        "cmd": (
            "cd /srv/tyche/local-projects/home-anton-projects/tyche-research-vault && "
            "scripts/limen_observatory_refresh.sh >> logs/limen-observatory-refresh.out 2>&1"
        ),
    },
    "obscure-ai-observatory-refresh": {
        "cwd": FRONTEND_ROOT,
        "cmd": (
            "cd /srv/tyche/local-projects/home-anton-projects/tyche-research-vault && "
            "scripts/obscure_ai_observatory_refresh.sh >> logs/obscure-ai-observatory-refresh.out 2>&1"
        ),
    },
}

CPU_MINER_PREFIX = "limen-cpu-miner-"


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def tmux_sessions() -> set[str]:
    try:
        proc = subprocess.run(["tmux", "ls"], text=True, capture_output=True, timeout=8)
    except Exception:
        return set()
    if proc.returncode != 0:
        return set()
    return {line.split(":", 1)[0] for line in proc.stdout.splitlines() if line.strip()}


def stop_files_present() -> bool:
    expected = [
        "health-finance-education",
        "identity-provenance",
        "legal-research",
        "public-sector",
        "residual-weird",
        "security",
    ]
    return all((Path("/srv/tyche") / f"STOP-limen-cpu-miner-{name}").exists() for name in expected)


def start_session(name: str, spec: dict[str, Any], dry_run: bool) -> dict[str, Any]:
    if dry_run:
        return {"session": name, "started": False, "dry_run": True, "cmd": spec["cmd"]}
    proc = subprocess.run(
        ["tmux", "new-session", "-d", "-s", name, spec["cmd"]],
        cwd=spec["cwd"],
        text=True,
        capture_output=True,
        timeout=10,
    )
    return {
        "session": name,
        "started": proc.returncode == 0,
        "returncode": proc.returncode,
        "stdout": proc.stdout.strip(),
        "stderr": proc.stderr.strip(),
    }


def check_once(dry_run: bool) -> dict[str, Any]:
    sessions = tmux_sessions()
    actions: list[dict[str, Any]] = []
    blockers: list[dict[str, Any]] = []

    if PAUSE_FILE.exists():
        return {
            "generated_at_utc": utc_now(),
            "ok": True,
            "paused": True,
            "pause_file": str(PAUSE_FILE),
            "blockers": [],
            "actions": [],
            "known_sessions_checked": sorted(SESSION_COMMANDS),
            "boundary": "Runtime pause guard is present; autostart will not restart LIMEN/ObscureAI sessions.",
        }

    cpu_sessions = sorted(session for session in sessions if session.startswith(CPU_MINER_PREFIX))
    if cpu_sessions:
        blockers.append(
            {
                "code": "cpu_mining_session_present",
                "message": "Autostart refuses to act while CPU mining sessions are present.",
                "sessions": cpu_sessions,
            }
        )
    if not stop_files_present():
        blockers.append(
            {
                "code": "cpu_mining_stop_files_missing",
                "message": "Autostart refuses to act until all CPU-miner STOP files are present.",
            }
        )

    if not blockers:
        for name, spec in SESSION_COMMANDS.items():
            if name in sessions:
                continue
            actions.append(start_session(name, spec, dry_run))

    return {
        "generated_at_utc": utc_now(),
        "ok": not blockers and all(action.get("started") or action.get("dry_run") for action in actions),
        "blockers": blockers,
        "actions": actions,
        "known_sessions_checked": sorted(SESSION_COMMANDS),
        "boundary": "Restarts required LIMEN/ObscureAI runtime sessions only; it never starts CPU mining sessions.",
    }


def append_jsonl(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(payload, ensure_ascii=False, sort_keys=True) + "\n")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--once", action="store_true")
    parser.add_argument("--interval", type=int, default=60)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--log", default=str(PROJECT_ROOT / "logs/limen-runtime-autostart.jsonl"))
    parser.add_argument("--pretty", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    log_path = Path(args.log)
    while True:
        payload = check_once(args.dry_run)
        append_jsonl(log_path, payload)
        print(json.dumps(payload, ensure_ascii=False, indent=2 if args.pretty else None, sort_keys=True), flush=True)
        if args.once:
            return 0 if payload["ok"] else 1
        time.sleep(max(10, args.interval))


if __name__ == "__main__":
    raise SystemExit(main())
