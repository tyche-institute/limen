#!/usr/bin/env python3
"""Read-only Hermes/Codex readiness check for LIMEN review lanes.

This intentionally does not run `hermes model` or call a model because Hermes
requires an interactive terminal for that command. It checks local config,
credential presence, supervisor freshness, lane backlog, and recent supervisor
failure markers without exposing secrets.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

try:
    import yaml
except Exception:  # pragma: no cover - fallback is only for stripped envs.
    yaml = None


PROJECT_ROOT = Path("/srv/tyche/projects/limen-ai-edge-case-atlas")
HERMES_HOME = Path("/home/anton/.hermes")
OUT = PROJECT_ROOT / "runtime" / "limen-hermes-readiness-latest.json"
SUPERVISOR_LOG = PROJECT_ROOT / "logs" / "limen-hermes-lane-supervisor.log"
SUPERVISOR_SESSION = "limen-hermes-lane-supervisor"
LANE_PREFIXES = (
    "limen-source-review-lane-",
    "limen-url-hardening-lane-",
    "limen-translation-review-lane-",
    "limen-bulk-source-lane-",
    "limen-bulk-translation-lane-",
    "limen-bulk-translation-source-lane-",
    "limen-case-extraction-lane-",
)


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def parse_utc(value: str) -> datetime | None:
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00"))
    except Exception:
        return None


def age_seconds(value: str | None) -> int | None:
    if not value:
        return None
    dt = parse_utc(value)
    if not dt:
        return None
    return max(0, int((datetime.now(timezone.utc) - dt).total_seconds()))


def read_json(path: Path) -> dict[str, Any]:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return {}


def read_yaml(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    text = path.read_text(encoding="utf-8", errors="replace")
    if yaml is not None:
        try:
            data = yaml.safe_load(text)
            return data if isinstance(data, dict) else {}
        except Exception:
            pass
    model: dict[str, str] = {}
    in_model = False
    for line in text.splitlines():
        if re.match(r"^model:\s*$", line):
            in_model = True
            continue
        if in_model and line and not line.startswith(" "):
            in_model = False
        if in_model:
            match = re.match(r"\s+([a-zA-Z0-9_-]+):\s*(.+)\s*$", line)
            if match:
                model[match.group(1)] = match.group(2).strip("'\"")
    return {"model": model}


def iv(value: Any) -> int:
    try:
        return int(value or 0)
    except Exception:
        return 0


def run(cmd: list[str], timeout: int = 10) -> tuple[int | None, str, str]:
    try:
        proc = subprocess.run(cmd, text=True, capture_output=True, timeout=timeout)
    except Exception as exc:
        return None, "", str(exc)
    return proc.returncode, proc.stdout.strip(), proc.stderr.strip()


def tmux_sessions() -> list[str]:
    code, stdout, _ = run(["tmux", "ls"], timeout=5)
    if code != 0:
        return []
    return [line.split(":", 1)[0] for line in stdout.splitlines() if ":" in line]


def hermes_binary_status() -> dict[str, Any]:
    path = shutil.which("hermes")
    payload: dict[str, Any] = {"path": path, "exists": bool(path), "version": ""}
    if path:
        code, stdout, stderr = run(["hermes", "--version"], timeout=10)
        payload.update(
            {
                "version_returncode": code,
                "version": (stdout or stderr).splitlines()[0] if (stdout or stderr) else "",
            }
        )
    return payload


def config_status(hermes_home: Path) -> dict[str, Any]:
    config_path = hermes_home / "config.yaml"
    config = read_yaml(config_path)
    model = config.get("model", {}) if isinstance(config.get("model"), dict) else {}
    fallback = config.get("fallback_providers", []) if isinstance(config.get("fallback_providers"), list) else []
    fallback_has_codex = any(
        isinstance(item, dict) and item.get("provider") == "openai-codex" for item in fallback
    )
    return {
        "path": str(config_path),
        "exists": config_path.exists(),
        "default_provider": model.get("provider", ""),
        "default_model": model.get("default", ""),
        "fallback_has_openai_codex": fallback_has_codex,
    }


def auth_status(hermes_home: Path) -> dict[str, Any]:
    auth_path = hermes_home / "auth.json"
    auth = read_json(auth_path)
    provider = (auth.get("providers", {}) or {}).get("openai-codex", {})
    tokens = provider.get("tokens", {}) if isinstance(provider, dict) else {}
    return {
        "path": str(auth_path),
        "exists": auth_path.exists(),
        "openai_codex_provider_present": bool(provider),
        "openai_codex_auth_mode": provider.get("auth_mode", "") if isinstance(provider, dict) else "",
        "openai_codex_last_refresh": provider.get("last_refresh", "") if isinstance(provider, dict) else "",
        "openai_codex_has_access_token": bool(tokens.get("access_token")),
        "openai_codex_has_refresh_token": bool(tokens.get("refresh_token")),
        "openai_codex_has_account_id": bool(tokens.get("account_id")),
    }


def compact_backlog(project_root: Path) -> dict[str, Any]:
    compact = read_json(project_root / "runtime" / "limen-compact-status-latest.json")
    if not compact:
        compact = read_json(project_root / "runtime" / "limen-case-review-no-tokens-compact-latest.json")
    if not compact:
        code, stdout, _ = run([str(project_root / "tools" / "limen_compact_status.py")], timeout=60)
        if code == 0:
            try:
                compact = json.loads(stdout)
            except Exception:
                compact = {}

    bulk = compact.get("bulk", {}) if isinstance(compact.get("bulk"), dict) else {}
    bulk_tasks = bulk.get("tasks", {}) if isinstance(bulk.get("tasks"), dict) else {}
    bulk_missing = sum(iv(task.get("missing_rows")) for task in bulk_tasks.values() if isinstance(task, dict))
    direct_missing = iv(((compact.get("review") or {}) if isinstance(compact.get("review"), dict) else {}).get("direct_source_missing_rows"))
    hardening = compact.get("hardening", {}) if isinstance(compact.get("hardening"), dict) else {}
    hardening_url_missing = iv(((hardening.get("url") or {}) if isinstance(hardening.get("url"), dict) else {}).get("missing_rows"))
    hardening_translation_missing = iv(
        ((hardening.get("translation") or {}) if isinstance(hardening.get("translation"), dict) else {}).get("missing_rows")
    )
    case_missing = iv(((compact.get("case_extraction") or {}) if isinstance(compact.get("case_extraction"), dict) else {}).get("missing_rows"))
    total = direct_missing + hardening_url_missing + hardening_translation_missing + bulk_missing + case_missing
    return {
        "direct_source_missing_rows": direct_missing,
        "hardening_url_missing_rows": hardening_url_missing,
        "hardening_translation_missing_rows": hardening_translation_missing,
        "bulk_missing_rows": bulk_missing,
        "case_extraction_missing_rows": case_missing,
        "hermes_review_backlog_rows": total,
    }


def supervisor_status(log_path: Path, sessions: list[str], max_age: int) -> dict[str, Any]:
    payload: dict[str, Any] = {
        "session": SUPERVISOR_SESSION,
        "session_present": SUPERVISOR_SESSION in sessions,
        "log_path": str(log_path),
        "log_exists": log_path.exists(),
        "log_age_seconds": None,
        "fresh": False,
        "latest_cycle_start_utc": "",
        "latest_cycle_complete_utc": "",
        "latest_direct_source_backlog": None,
        "recent_failure_lines": [],
        "recent_quota_lines": [],
    }
    if not log_path.exists():
        return payload
    payload["log_age_seconds"] = max(0, int(datetime.now(timezone.utc).timestamp() - log_path.stat().st_mtime))
    payload["fresh"] = payload["log_age_seconds"] <= max_age
    # Supervisor cycles can emit large JSON rollups; keep enough tail to include
    # the latest cycle start, backlog line, and completion marker together.
    lines = log_path.read_text(encoding="utf-8", errors="replace").splitlines()[-5000:]
    latest_start_index = -1
    stamp_re = re.compile(r"^\[(?P<stamp>[0-9T:\-]+Z)\]\s+(?P<msg>.*)$")
    for idx, line in enumerate(lines):
        match = stamp_re.match(line)
        if not match:
            continue
        msg = match.group("msg")
        stamp = match.group("stamp")
        if msg.startswith("cycle start"):
            payload["latest_cycle_start_utc"] = stamp
            latest_start_index = idx
        if msg.startswith("cycle complete"):
            payload["latest_cycle_complete_utc"] = stamp
        backlog_match = re.search(r"direct-source backlog=([0-9]+)", msg)
        if backlog_match:
            payload["latest_direct_source_backlog"] = int(backlog_match.group(1))

    recent_lines = lines[latest_start_index:] if latest_start_index >= 0 else lines[-120:]
    failure_lines = []
    quota_lines = []
    for line in recent_lines:
        lower = line.lower()
        if re.match(r"^\[[0-9T:\-]+Z\].*\bfailed\b", lower) or any(
            marker in lower
            for marker in (
                "not logged into openai codex",
                "authentication",
                "unauthorized",
                "invalid api key",
                "command not found",
                "traceback",
                "no such file or directory",
            )
        ):
            failure_lines.append(line[-300:])
        if "quota" in lower or "usage limit" in lower or re.search(r"\b429\b", lower):
            quota_lines.append(line[-300:])
    payload["recent_failure_lines"] = failure_lines[:10]
    payload["recent_quota_lines"] = quota_lines[:10]
    payload["cycle_complete_age_seconds"] = age_seconds(payload["latest_cycle_complete_utc"])
    return payload


def active_lane_status(sessions: list[str]) -> dict[str, Any]:
    by_prefix = {
        prefix.rstrip("-"): [name for name in sessions if name.startswith(prefix)]
        for prefix in LANE_PREFIXES
    }
    return {
        "active_lane_sessions": sum(len(items) for items in by_prefix.values()),
        "by_prefix": {prefix: len(items) for prefix, items in by_prefix.items()},
    }


def build(project_root: Path, hermes_home: Path, max_log_age: int) -> dict[str, Any]:
    blockers: list[dict[str, Any]] = []
    warnings: list[dict[str, Any]] = []
    infos: list[dict[str, Any]] = []

    binary = hermes_binary_status()
    config = config_status(hermes_home)
    auth = auth_status(hermes_home)
    sessions = tmux_sessions()
    supervisor = supervisor_status(project_root / "logs" / "limen-hermes-lane-supervisor.log", sessions, max_log_age)
    lanes = active_lane_status(sessions)
    backlog = compact_backlog(project_root)

    if not binary["exists"]:
        blockers.append({"code": "hermes_binary_missing", "message": "hermes is not on PATH."})
    if not config["exists"]:
        blockers.append({"code": "hermes_config_missing", "message": "~/.hermes/config.yaml is missing."})
    if not auth["exists"] or not auth["openai_codex_provider_present"]:
        blockers.append({"code": "openai_codex_auth_missing", "message": "Hermes OpenAI Codex credentials are missing."})
    elif not (auth["openai_codex_has_access_token"] and auth["openai_codex_has_refresh_token"]):
        blockers.append({"code": "openai_codex_tokens_incomplete", "message": "Hermes OpenAI Codex token set is incomplete."})
    if config.get("default_provider") != "openai-codex":
        infos.append(
            {
                "code": "hermes_default_provider_not_codex",
                "message": "LIMEN lane launchers pass --provider openai-codex explicitly; global default differs.",
                "value": config.get("default_provider"),
            }
        )
    if not supervisor["session_present"]:
        blockers.append({"code": "hermes_supervisor_missing", "message": "limen-hermes-lane-supervisor tmux session is missing."})
    if not supervisor["fresh"]:
        blockers.append(
            {
                "code": "hermes_supervisor_log_stale",
                "message": "Hermes lane supervisor heartbeat log is stale.",
                "value": supervisor.get("log_age_seconds"),
            }
        )
    complete_age = supervisor.get("cycle_complete_age_seconds")
    if complete_age is not None and complete_age > max_log_age:
        blockers.append(
            {
                "code": "hermes_supervisor_cycle_stale",
                "message": "Hermes lane supervisor has not completed a recent cycle.",
                "value": complete_age,
            }
        )
    if supervisor["recent_failure_lines"]:
        blockers.append(
            {
                "code": "hermes_supervisor_recent_failure",
                "message": "Recent supervisor cycle contains failure markers.",
                "sample": supervisor["recent_failure_lines"][:3],
            }
        )
    if supervisor["recent_quota_lines"]:
        warnings.append(
            {
                "code": "hermes_supervisor_recent_quota",
                "message": "Recent supervisor cycle contains quota/backoff markers.",
                "sample": supervisor["recent_quota_lines"][:3],
            }
        )
    if backlog["hermes_review_backlog_rows"] and lanes["active_lane_sessions"] == 0:
        warnings.append(
            {
                "code": "hermes_backlog_no_active_lane_sessions",
                "message": "Hermes backlog exists but no lane sessions are currently active.",
                "value": backlog["hermes_review_backlog_rows"],
            }
        )

    return {
        "generated_at_utc": utc_now(),
        "ok": not blockers,
        "blockers": blockers,
        "warnings": warnings,
        "infos": infos,
        "hermes": {
            "binary": binary,
            "config": config,
            "auth": auth,
        },
        "supervisor": supervisor,
        "lanes": lanes,
        "backlog": backlog,
        "throughput_defaults": {
            "source_lanes": 48,
            "source_batch_size": 160,
            "hardening_lanes": 2,
            "bulk_source_lanes": 32,
            "bulk_translation_lanes": 32,
            "bulk_translation_source_lanes": 24,
            "case_extraction_lanes": 8,
            "case_extraction_batch_size": 16,
        },
        "boundary": "Read-only readiness check; does not call models, launch lanes, mine data, process queues, or deploy.",
    }


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    tmp.replace(path)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--project-root", default=str(PROJECT_ROOT))
    parser.add_argument("--hermes-home", default=str(HERMES_HOME))
    parser.add_argument("--out", default=str(OUT))
    parser.add_argument("--max-log-age", type=int, default=300)
    parser.add_argument("--pretty", action="store_true")
    args = parser.parse_args()

    payload = build(Path(args.project_root), Path(args.hermes_home), args.max_log_age)
    write_json(Path(args.out), payload)
    print(json.dumps(payload, ensure_ascii=False, indent=2 if args.pretty else None, sort_keys=True))
    return 0 if payload["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
