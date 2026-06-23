#!/usr/bin/env bash
set -euo pipefail

PROJECT_ROOT="${PROJECT_ROOT:-/srv/tyche/projects/limen-ai-edge-case-atlas}"
LOG_DIR="${PROJECT_ROOT}/logs"
SUPERVISOR_LOG="${LOG_DIR}/limen-hermes-lane-supervisor.log"
SLEEP_SECONDS="${LIMEN_SUPERVISOR_SLEEP_SECONDS:-45}"
SOURCE_LANES="${LIMEN_SOURCE_LANES:-48}"
SOURCE_BATCH_SIZE="${LIMEN_SOURCE_BATCH_SIZE:-160}"
HARDENING_LANES="${LIMEN_HARDENING_LANES:-2}"
HARDENING_QUOTA_BACKOFF_SECONDS="${LIMEN_HARDENING_QUOTA_BACKOFF_SECONDS:-300}"
BULK_SOURCE_LANES="${LIMEN_BULK_SOURCE_LANES:-32}"
BULK_TRANSLATION_LANES="${LIMEN_BULK_TRANSLATION_LANES:-32}"
BULK_TRANSLATION_SOURCE_LANES="${LIMEN_BULK_TRANSLATION_SOURCE_LANES:-24}"
CASE_EXTRACTION_LANES="${LIMEN_CASE_EXTRACTION_LANES:-8}"
CASE_EXTRACTION_BATCH_SIZE="${LIMEN_CASE_EXTRACTION_BATCH_SIZE:-16}"

mkdir -p "${LOG_DIR}"
cd "${PROJECT_ROOT}"

log() {
  printf '[%s] %s\n' "$(date -u +%FT%TZ)" "$*" | tee -a "${SUPERVISOR_LOG}"
}

source_backlog() {
  python3 - <<'PY'
import csv
import glob

queue = "results/review-candidates/direct-source-review-queue.tsv"
done = set()
for path in glob.glob("results/review-candidates/source-review-batches/*/source-review-results.tsv"):
    try:
        with open(path, encoding="utf-8", errors="replace", newline="") as fh:
            for row in csv.DictReader(fh, delimiter="\t"):
                if row.get("signal_id"):
                    done.add(row["signal_id"])
    except Exception:
        pass

ids = []
try:
    with open(queue, encoding="utf-8", errors="replace", newline="") as fh:
        for row in csv.DictReader(fh, delimiter="\t"):
            if row.get("signal_id"):
                ids.append(row["signal_id"])
except Exception:
    print(0)
    raise SystemExit

print(len(set(ids) - done))
PY
}

json_bool() {
  local path="$1"
  local expr="$2"
  python3 - "$path" "$expr" <<'PY'
import json
import sys

path, expr = sys.argv[1:3]
try:
    data = json.load(open(path, encoding="utf-8"))
except Exception:
    print("false")
    raise SystemExit
value = data
for part in expr.split("."):
    value = value.get(part) if isinstance(value, dict) else None
print("true" if value is True else "false")
PY
}

hardening_quota_backoff_remaining() {
  local backoff_seconds="$1"
  python3 - "${backoff_seconds}" <<'PY'
import glob
import json
import sys
from datetime import datetime, timezone

backoff = int(sys.argv[1])
now = datetime.now(timezone.utc)
newest = None
for path in glob.glob("results/review-candidates/hardening-review-batches/*/*/manifest.json"):
    try:
        data = json.load(open(path, encoding="utf-8"))
    except Exception:
        continue
    reason = str(data.get("failure_reason") or "")
    if data.get("status") != "failed" or "quota_429" not in reason:
        continue
    stamp = data.get("failed_at_utc") or data.get("updated_at_utc")
    if not stamp:
        continue
    try:
        dt = datetime.fromisoformat(stamp.replace("Z", "+00:00"))
    except Exception:
        continue
    if newest is None or dt > newest:
        newest = dt
if newest is None:
    print(0)
else:
    elapsed = max(0, int((now - newest).total_seconds()))
    print(max(0, backoff - elapsed))
PY
}

while true; do
  if [[ -f /srv/tyche/STOP || -f "${PROJECT_ROOT}/STOP" || -f /srv/tyche/STOP-limen-hermes-lane-supervisor ]]; then
    log "STOP present; sleeping ${SLEEP_SECONDS}s"
    sleep "${SLEEP_SECONDS}"
    continue
  fi

  log "cycle start"

  "${PROJECT_ROOT}/tools/build_bulk_source_review_routing.py" >> "${SUPERVISOR_LOG}" 2>&1 || log "bulk source routing failed"
  "${PROJECT_ROOT}/tools/build_bulk_named_source_autoresolve.py" >> "${SUPERVISOR_LOG}" 2>&1 || log "bulk named-source autoresolve failed"
  "${PROJECT_ROOT}/tools/prepare_bulk_review_queues.py" >> "${SUPERVISOR_LOG}" 2>&1 || log "bulk queue prep failed"
  backlog="$(source_backlog || echo 0)"
  log "direct-source backlog=${backlog}"
  if [[ "${backlog}" =~ ^[0-9]+$ && "${backlog}" -gt 0 ]]; then
    source_lanes_now="${SOURCE_LANES}"
    if [[ "${backlog}" -lt "${source_lanes_now}" ]]; then
      source_lanes_now="${backlog}"
    fi
    log "launching source-review lanes=${source_lanes_now} batch=${SOURCE_BATCH_SIZE}"
    "${PROJECT_ROOT}/tools/launch_source_review_lanes.sh" "${source_lanes_now}" "${SOURCE_BATCH_SIZE}" >> "${SUPERVISOR_LOG}" 2>&1 || log "source lane launch failed"
  fi

  "${PROJECT_ROOT}/tools/build_hardening_review_rollup.py" >> "${SUPERVISOR_LOG}" 2>&1 || log "hardening rollup failed"
  if [[ "$(json_bool "results/review-candidates/hardening-review-rollup-status.json" "all_complete")" != "true" ]]; then
    quota_wait="$(hardening_quota_backoff_remaining "${HARDENING_QUOTA_BACKOFF_SECONDS}" || echo 0)"
    if [[ "${quota_wait}" =~ ^[0-9]+$ && "${quota_wait}" -gt 0 ]]; then
      if [[ -x "${PROJECT_ROOT}/tools/hardening_local_autoresolve.py" ]]; then
        log "hardening quota backoff active; trying local autoresolve before relaunch"
        "${PROJECT_ROOT}/tools/hardening_local_autoresolve.py" --task all >> "${SUPERVISOR_LOG}" 2>&1 || log "hardening local autoresolve failed"
        "${PROJECT_ROOT}/tools/build_hardening_review_rollup.py" >> "${SUPERVISOR_LOG}" 2>&1 || log "hardening rollup after local autoresolve failed"
      fi
      if [[ "$(json_bool "results/review-candidates/hardening-review-rollup-status.json" "all_complete")" == "true" ]]; then
        log "hardening completed during quota backoff"
      else
        log "hardening quota backoff active; waiting ${quota_wait}s before relaunch"
      fi
    else
      log "launching hardening lanes=${HARDENING_LANES}"
      "${PROJECT_ROOT}/tools/launch_hardening_review_lanes.sh" all "${HARDENING_LANES}" >> "${SUPERVISOR_LOG}" 2>&1 || log "hardening lane launch failed"
    fi
  fi

  "${PROJECT_ROOT}/tools/build_bulk_review_rollup.py" >> "${SUPERVISOR_LOG}" 2>&1 || log "bulk rollup failed"
  if [[ "$(json_bool "results/review-candidates/bulk-review-rollup-status.json" "all_queues_complete")" != "true" ]]; then
    log "launching bulk lanes"
    "${PROJECT_ROOT}/tools/launch_bulk_review_lanes.sh" source "${BULK_SOURCE_LANES}" >> "${SUPERVISOR_LOG}" 2>&1 || log "bulk source lane launch failed"
    "${PROJECT_ROOT}/tools/launch_bulk_review_lanes.sh" translation "${BULK_TRANSLATION_LANES}" >> "${SUPERVISOR_LOG}" 2>&1 || log "bulk translation lane launch failed"
    "${PROJECT_ROOT}/tools/launch_bulk_review_lanes.sh" translation-source "${BULK_TRANSLATION_SOURCE_LANES}" >> "${SUPERVISOR_LOG}" 2>&1 || log "bulk translation-source lane launch failed"
  fi
  "${PROJECT_ROOT}/tools/prepare_bulk_translation_parent_source_queue.py" >> "${SUPERVISOR_LOG}" 2>&1 || log "bulk translation-parent queue prep failed"
  "${PROJECT_ROOT}/tools/build_bulk_review_rollup.py" >> "${SUPERVISOR_LOG}" 2>&1 || log "bulk rollup after translation-parent prep failed"
  if [[ "$(json_bool "results/review-candidates/bulk-review-rollup-status.json" "all_queues_complete")" != "true" ]]; then
    log "launching residual bulk lanes"
    "${PROJECT_ROOT}/tools/launch_bulk_review_lanes.sh" source "${BULK_SOURCE_LANES}" >> "${SUPERVISOR_LOG}" 2>&1 || log "residual bulk source lane launch failed"
    "${PROJECT_ROOT}/tools/launch_bulk_review_lanes.sh" translation "${BULK_TRANSLATION_LANES}" >> "${SUPERVISOR_LOG}" 2>&1 || log "residual bulk translation lane launch failed"
    "${PROJECT_ROOT}/tools/launch_bulk_review_lanes.sh" translation-source "${BULK_TRANSLATION_SOURCE_LANES}" >> "${SUPERVISOR_LOG}" 2>&1 || log "residual bulk translation-source lane launch failed"
  fi

  "${PROJECT_ROOT}/tools/build_source_review_promotion_hardening.py" >> "${SUPERVISOR_LOG}" 2>&1 || log "promotion hardening failed"
  "${PROJECT_ROOT}/tools/build_source_review_completion_ledger.py" >> "${SUPERVISOR_LOG}" 2>&1 || log "completion ledger failed"
  "${PROJECT_ROOT}/tools/build_translation_hold_board.py" >> "${SUPERVISOR_LOG}" 2>&1 || log "translation hold board failed"
  "${PROJECT_ROOT}/tools/build_reviewed_core_promotion_packet.py" >> "${SUPERVISOR_LOG}" 2>&1 || log "promotion packet failed"
  "${PROJECT_ROOT}/tools/build_reviewed_core_source_surface_disposition.py" >> "${SUPERVISOR_LOG}" 2>&1 || log "source-surface disposition failed"
  "${PROJECT_ROOT}/tools/build_case_extraction_rollup.py" >> "${SUPERVISOR_LOG}" 2>&1 || log "case extraction rollup failed"
  if [[ "$(json_bool "results/review-candidates/reviewed-core-case-extraction-rollup-status.json" "all_complete")" != "true" ]]; then
    log "launching case-extraction lanes=${CASE_EXTRACTION_LANES} batch=${CASE_EXTRACTION_BATCH_SIZE}"
    "${PROJECT_ROOT}/tools/launch_case_extraction_lanes.sh" "${CASE_EXTRACTION_LANES}" "${CASE_EXTRACTION_BATCH_SIZE}" >> "${SUPERVISOR_LOG}" 2>&1 || log "case extraction lane launch failed"
  fi
  "${PROJECT_ROOT}/tools/build_case_extraction_rollup.py" >> "${SUPERVISOR_LOG}" 2>&1 || log "case extraction rollup after launch failed"
  "${PROJECT_ROOT}/tools/build_reviewed_core_case_hardening_review.py" >> "${SUPERVISOR_LOG}" 2>&1 || log "case hardening review failed"

  log "cycle complete; sleeping ${SLEEP_SECONDS}s"
  sleep "${SLEEP_SECONDS}"
done
