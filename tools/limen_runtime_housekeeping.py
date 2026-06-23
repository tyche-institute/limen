#!/usr/bin/env python3
"""Bound LIMEN/ObscureAI runtime log growth without stopping services."""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


PROJECT_ROOT = Path("/srv/tyche/projects/limen-ai-edge-case-atlas")
FRONTEND_ROOT = Path("/srv/tyche/local-projects/home-anton-projects/tyche-research-vault")
HEARTBEAT = PROJECT_ROOT / "logs" / "limen-runtime-housekeeping.jsonl"

LOG_GLOBS = [
    "logs/limen-*.log",
    "logs/limen-*.out",
    "logs/limen-*.jsonl",
    "logs/obscure-ai-*.log",
    "logs/obscure-ai-*.out",
    "logs/review-candidate-*.log",
    "logs/review-candidate-*.out",
    "logs/source-review-lanes/*.log",
    "logs/hardening-review-lanes/*.log",
]


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def iter_logs(project_root: Path, frontend_root: Path) -> list[Path]:
    roots = [project_root, frontend_root]
    paths: set[Path] = set()
    for root in roots:
        for pattern in LOG_GLOBS:
            paths.update(path for path in root.glob(pattern) if path.is_file())
    return sorted(paths)


def trim_file(path: Path, max_bytes: int, keep_bytes: int, dry_run: bool) -> dict[str, Any] | None:
    try:
        size = path.stat().st_size
    except OSError:
        return None
    if size <= max_bytes:
        return None

    keep = max(0, min(keep_bytes, size))
    if dry_run:
        return {"path": str(path), "old_bytes": size, "new_bytes": keep, "dry_run": True}

    with path.open("rb") as handle:
        handle.seek(-keep, 2)
        tail = handle.read()
    marker = (
        f"[{utc_now()}] LIMEN housekeeping trimmed log from {size} bytes; "
        f"preserved last {len(tail)} bytes.\n"
    ).encode("utf-8")
    with path.open("wb") as handle:
        handle.write(marker)
        handle.write(tail)
    new_size = path.stat().st_size
    return {"path": str(path), "old_bytes": size, "new_bytes": new_size, "dry_run": False}


def append_jsonl(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(payload, ensure_ascii=False, sort_keys=True) + "\n")


def run(project_root: Path, frontend_root: Path, max_bytes: int, keep_bytes: int, dry_run: bool) -> dict[str, Any]:
    actions = []
    for path in iter_logs(project_root, frontend_root):
        action = trim_file(path, max_bytes=max_bytes, keep_bytes=keep_bytes, dry_run=dry_run)
        if action:
            actions.append(action)
    return {
        "generated_at_utc": utc_now(),
        "ok": True,
        "dry_run": dry_run,
        "max_bytes": max_bytes,
        "keep_bytes": keep_bytes,
        "trimmed_files": len(actions),
        "actions": actions,
        "boundary": "Runtime log housekeeping only; does not start/stop sessions, process queues, call models, deploy, or mine.",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--project-root", default=str(PROJECT_ROOT))
    parser.add_argument("--frontend-root", default=str(FRONTEND_ROOT))
    parser.add_argument("--max-mb", type=int, default=32)
    parser.add_argument("--keep-mb", type=int, default=8)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--log", default=str(HEARTBEAT))
    parser.add_argument("--pretty", action="store_true")
    args = parser.parse_args()

    payload = run(
        Path(args.project_root),
        Path(args.frontend_root),
        max_bytes=max(1, args.max_mb) * 1024 * 1024,
        keep_bytes=max(1, args.keep_mb) * 1024 * 1024,
        dry_run=args.dry_run,
    )
    append_jsonl(Path(args.log), payload)
    print(json.dumps(payload, ensure_ascii=False, indent=2 if args.pretty else None, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
