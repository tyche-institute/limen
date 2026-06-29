#!/usr/bin/env python3
"""limen_runtime_housekeeping.py

Cap and rotate LIMEN runtime artifacts so the cron-driven advancer cannot fill
the disk. Invoked from cron as:

    limen_runtime_housekeeping.py --max-mb 32 --keep-mb 8

Behaviour
  * Targets the project's runtime/ staging tree and the rotating *.log /
    *.jsonl runtime logs under logs/.
  * For each managed group: if total size exceeds --max-mb, delete the OLDEST
    entries (whole staging snapshots; oldest rotated log files) until the group
    is at or below --keep-mb. Active append-target logs are truncated-by-tail
    rather than deleted, so the cron keeps writing to a valid file.
  * Honours /srv/tyche/STOP, /srv/tyche/STOP-limen-runtime and project STOP
    files: if any is present, it exits 0 without touching anything.
  * No sudo. Pure stdlib. Idempotent and safe to run every 30 min.

It NEVER touches curated funnel data under results/ or data/ — only runtime/
scratch and rotating logs.
"""

from __future__ import annotations

import argparse
import os
import sys
import time

PROJECT_DIR = "/srv/tyche/projects/limen-ai-edge-case-atlas"
RUNTIME_DIR = os.path.join(PROJECT_DIR, "runtime")
STAGING_DIR = os.path.join(RUNTIME_DIR, "staging")
LOG_DIR = os.path.join(PROJECT_DIR, "logs")

STOP_FILES = [
    "/srv/tyche/STOP",
    "/srv/tyche/STOP-limen-runtime",
    os.path.join(PROJECT_DIR, "STOP"),
    os.path.join(PROJECT_DIR, "STOP-runtime"),
]

# Rotating runtime logs we are allowed to cap. Anything else under logs/ is left
# alone so we never clobber a file another process owns by surprise.
MANAGED_LOG_BASENAMES = {
    "limen-runtime-autostart.jsonl",
    "limen-runtime-bootstrap.cron.log",
    "limen-runtime-housekeeping.cron.log",
    "limen-runtime-bootstrap.log",
    "limen-hermes-lane-supervisor.out",
    "review-candidate-materializer.out",
}

MB = 1024 * 1024


def log(msg: str) -> None:
    print(f"{time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())} [housekeeping] {msg}",
          flush=True)


def stopped() -> bool:
    for s in STOP_FILES:
        if os.path.exists(s):
            log(f"STOP file present ({s}); exiting without action.")
            return True
    return False


def dir_size(path: str) -> int:
    total = 0
    for root, _dirs, files in os.walk(path):
        for name in files:
            fp = os.path.join(root, name)
            try:
                total += os.path.getsize(fp)
            except OSError:
                pass
    return total


def rm_tree(path: str) -> None:
    # stdlib recursive remove without importing shutil-at-top noise.
    for root, dirs, files in os.walk(path, topdown=False):
        for name in files:
            try:
                os.remove(os.path.join(root, name))
            except OSError:
                pass
        for name in dirs:
            try:
                os.rmdir(os.path.join(root, name))
            except OSError:
                pass
    try:
        os.rmdir(path)
    except OSError:
        pass


def cap_staging(max_mb: int, keep_mb: int) -> None:
    """Drop oldest whole staging snapshots until the tree is <= keep_mb."""
    if not os.path.isdir(STAGING_DIR):
        return
    total = dir_size(STAGING_DIR)
    if total <= max_mb * MB:
        log(f"staging within cap ({total // MB} MB <= {max_mb} MB); no prune")
        return

    snaps = []
    for name in os.listdir(STAGING_DIR):
        p = os.path.join(STAGING_DIR, name)
        if os.path.isdir(p):
            try:
                snaps.append((os.path.getmtime(p), p))
            except OSError:
                pass
    snaps.sort()  # oldest first

    keep_bytes = keep_mb * MB
    removed = 0
    for _mtime, p in snaps:
        if total <= keep_bytes:
            break
        sz = dir_size(p)
        rm_tree(p)
        total -= sz
        removed += 1
        log(f"pruned staging snapshot {os.path.basename(p)} ({sz // MB} MB)")
    log(f"staging prune done: removed {removed} snapshot(s); now {total // MB} MB")


def tail_truncate(path: str, keep_bytes: int) -> None:
    """Keep only the last keep_bytes of an active append-target log, preserving
    whole trailing lines and keeping the file in place for the writer."""
    try:
        size = os.path.getsize(path)
    except OSError:
        return
    if size <= keep_bytes:
        return
    try:
        with open(path, "rb") as fh:
            fh.seek(size - keep_bytes)
            tail = fh.read()
        # Drop a partial first line so we don't leave a fragment.
        nl = tail.find(b"\n")
        if 0 <= nl < len(tail) - 1:
            tail = tail[nl + 1:]
        tmp = path + ".hk.tmp"
        with open(tmp, "wb") as fh:
            fh.write(tail)
        os.replace(tmp, path)
        log(f"tail-truncated {os.path.basename(path)} -> {len(tail) // MB} MB")
    except OSError as e:
        log(f"could not truncate {path}: {e}")


def cap_logs(max_mb: int, keep_mb: int) -> None:
    """Cap each managed rotating log individually to keep_mb when it exceeds
    max_mb. These are append-target files, so we tail-truncate in place."""
    if not os.path.isdir(LOG_DIR):
        return
    for base in sorted(MANAGED_LOG_BASENAMES):
        p = os.path.join(LOG_DIR, base)
        if not os.path.isfile(p):
            continue
        try:
            size = os.path.getsize(p)
        except OSError:
            continue
        if size > max_mb * MB:
            tail_truncate(p, keep_mb * MB)
        else:
            log(f"log {base} within cap ({size // MB} MB <= {max_mb} MB)")


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(
        description="Cap/rotate LIMEN runtime artifacts (staging tree + rotating logs).")
    parser.add_argument("--max-mb", type=int, default=32,
                        help="Trigger pruning when a managed group exceeds this size (MB).")
    parser.add_argument("--keep-mb", type=int, default=8,
                        help="Prune down to at most this size (MB).")
    args = parser.parse_args(argv)

    if args.keep_mb > args.max_mb:
        # Defensive: keep must not exceed max.
        args.keep_mb = args.max_mb

    if stopped():
        return 0

    os.makedirs(RUNTIME_DIR, exist_ok=True)
    log(f"start (max-mb={args.max_mb}, keep-mb={args.keep_mb})")
    cap_staging(args.max_mb, args.keep_mb)
    cap_logs(args.max_mb, args.keep_mb)
    log("done")
    return 0


if __name__ == "__main__":
    sys.exit(main())
