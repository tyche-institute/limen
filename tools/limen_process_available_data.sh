#!/usr/bin/env bash
set -euo pipefail

PROJECT_ROOT="${PROJECT_ROOT:-/srv/tyche/projects/limen-ai-edge-case-atlas}"
FRONTEND_ROOT="${FRONTEND_ROOT:-/srv/tyche/local-projects/home-anton-projects/tyche-research-vault}"
SOURCE_LANES="${LIMEN_SOURCE_LANES:-48}"
SOURCE_BATCH_SIZE="${LIMEN_SOURCE_BATCH_SIZE:-160}"
SOURCE_WAIT_SECONDS="${LIMEN_SOURCE_WAIT_SECONDS:-900}"
STOP_MINING=0
DEPLOY_FRONTENDS=0
STAMP="$(date -u +%Y%m%dT%H%M%SZ)"
LOG="${PROJECT_ROOT}/logs/limen-process-available-data-${STAMP}.log"

usage() {
  cat <<'EOF'
usage: limen_process_available_data.sh [--stop-mining] [--deploy-frontends]

Runs the quiet LIMEN processing pipeline against already available data and
prints one compact status JSON. Detailed command output is written to logs.
EOF
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --stop-mining) STOP_MINING=1 ;;
    --deploy-frontends) DEPLOY_FRONTENDS=1 ;;
    -h|--help) usage; exit 0 ;;
    *) echo "unknown arg: $1" >&2; usage >&2; exit 2 ;;
  esac
  shift
done

cd "${PROJECT_ROOT}"
mkdir -p "$(dirname "${LOG}")" "${PROJECT_ROOT}/runtime"

log() {
  printf '[%s] %s\n' "$(date -u +%FT%TZ)" "$*" | tee -a "${LOG}" >&2
}

run_logged() {
  log "run: $*"
  "$@" >> "${LOG}" 2>&1
}

LOCK="${PROJECT_ROOT}/runtime/limen-process-available-data.lock"
exec 9>"${LOCK}"
if ! flock -n 9; then
  log "another limen_process_available_data.sh run is active; leaving data untouched"
  tools/limen_compact_status.py
  exit 0
fi

json_field() {
  local path="$1"
  local field="$2"
  python3 - "$path" "$field" <<'PY'
import json
import sys
path, field = sys.argv[1:3]
try:
    data = json.load(open(path, encoding="utf-8"))
except Exception:
    print(0)
    raise SystemExit
value = data
for part in field.split("."):
    value = value.get(part) if isinstance(value, dict) else None
print(value if isinstance(value, int) else 0)
PY
}

stop_mining() {
  for lane in \
    limen-cpu-miner-health-finance-education \
    limen-cpu-miner-identity-provenance \
    limen-cpu-miner-legal-research \
    limen-cpu-miner-public-sector \
    limen-cpu-miner-residual-weird \
    limen-cpu-miner-security; do
    : > "/srv/tyche/STOP-${lane}"
    tmux kill-session -t "${lane}" 2>/dev/null || true
  done
}

direct_missing() {
  python3 - <<'PY'
import json
try:
    data = json.load(open("results/review-candidates/bulk-source-review-routing-status.json", encoding="utf-8"))
except Exception:
    print(0)
    raise SystemExit
print(int(data.get("current_queue_missing_rows") or 0))
PY
}

drain_direct_source_if_needed() {
  run_logged python3 tools/build_bulk_source_review_routing.py
  local missing
  missing="$(direct_missing)"
  if [[ "${missing}" =~ ^[0-9]+$ && "${missing}" -gt 0 ]]; then
    local lanes="${SOURCE_LANES}"
    if [[ "${missing}" -lt "${lanes}" ]]; then
      lanes="${missing}"
    fi
    log "direct-source missing=${missing}; launching lanes=${lanes}"
    run_logged tools/launch_source_review_lanes.sh "${lanes}" "${SOURCE_BATCH_SIZE}"
    local waited=0
    while [[ "${waited}" -lt "${SOURCE_WAIT_SECONDS}" ]]; do
      sleep 20
      waited=$((waited + 20))
      run_logged python3 tools/build_bulk_source_review_routing.py
      missing="$(direct_missing)"
      log "direct-source missing=${missing} waited=${waited}s"
      if [[ "${missing}" == "0" ]]; then
        break
      fi
    done
  fi
}

deploy_frontends() {
  (
    cd "${FRONTEND_ROOT}"
    run_logged python3 scripts/build_limen_observatory_snapshot.py
    run_logged python3 -m json.tool sites/limen-observatory/data/limen-snapshot.json
    run_logged node --check sites/limen-observatory/app.js
    run_logged npx wrangler pages deploy sites/limen-observatory --project-name limen-observatory --branch main
    run_logged python3 scripts/build_obscure_ai_dataset.py
    run_logged python3 -m json.tool sites/obscure-ai/data/cases.json
    run_logged node --check sites/obscure-ai/app.js
    run_logged npx wrangler pages deploy sites/obscure-ai --project-name obscure-ai --branch main
  )
}

log "process available data start log=${LOG}"
if [[ "${STOP_MINING}" == "1" ]]; then
  log "stopping LIMEN CPU mining"
  stop_mining
fi

run_logged python3 tools/materialize_review_candidates.py
run_logged python3 tools/review_all_candidates.py
drain_direct_source_if_needed
run_logged python3 tools/build_bulk_named_source_autoresolve.py
run_logged python3 tools/prepare_bulk_review_queues.py
run_logged python3 tools/build_bulk_review_rollup.py
run_logged python3 tools/prepare_hardening_review_queues.py
run_logged python3 tools/hardening_local_autoresolve.py --task all
run_logged python3 tools/build_hardening_review_rollup.py
run_logged python3 tools/build_source_review_promotion_hardening.py
run_logged python3 tools/build_source_review_completion_ledger.py
run_logged python3 tools/build_translation_hold_board.py
run_logged python3 tools/prepare_bulk_translation_parent_source_queue.py
run_logged python3 tools/build_bulk_review_rollup.py
run_logged python3 tools/build_reviewed_core_promotion_packet.py
run_logged python3 tools/build_reviewed_core_source_surface_disposition.py
run_logged python3 tools/build_case_extraction_rollup.py
run_logged python3 tools/build_reviewed_core_case_hardening_review.py
run_logged python3 tools/build_case_review_autorecommendations.py

if [[ "${DEPLOY_FRONTENDS}" == "1" ]]; then
  log "deploying frontends"
  deploy_frontends
fi

log "process available data complete"
tools/limen_compact_status.py
