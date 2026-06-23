#!/usr/bin/env bash
set -euo pipefail

PROJECT_ROOT="${PROJECT_ROOT:-/srv/tyche/projects/limen-ai-edge-case-atlas}"
LOG_DIR="${PROJECT_ROOT}/logs"
BOOTSTRAP_LOG="${LOG_DIR}/limen-runtime-bootstrap.log"
LOCK="${PROJECT_ROOT}/runtime/limen-runtime-bootstrap.lock"
SESSION="limen-runtime-autostart"
PAUSE_FILE="${PROJECT_ROOT}/runtime/PAUSE-limen-obscure-runtime"

mkdir -p "${LOG_DIR}" "${PROJECT_ROOT}/runtime"
cd "${PROJECT_ROOT}"

log() {
  printf '[%s] %s\n' "$(date -u +%FT%TZ)" "$*" | tee -a "${BOOTSTRAP_LOG}"
}

exec 9>"${LOCK}"
if ! flock -n 9; then
  log "bootstrap already running; exit"
  exit 0
fi

STOP_LANES=(
  limen-cpu-miner-health-finance-education
  limen-cpu-miner-identity-provenance
  limen-cpu-miner-legal-research
  limen-cpu-miner-public-sector
  limen-cpu-miner-residual-weird
  limen-cpu-miner-security
)

for lane in "${STOP_LANES[@]}"; do
  : > "/srv/tyche/STOP-${lane}"
  tmux kill-session -t "${lane}" 2>/dev/null || true
done

if [[ -f "${PAUSE_FILE}" ]]; then
  tmux kill-session -t "${SESSION}" 2>/dev/null || true
  log "runtime pause guard present; ${SESSION} stopped/not started"
  log "bootstrap complete (paused)"
  exit 0
fi

if tmux has-session -t "${SESSION}" 2>/dev/null; then
  log "${SESSION} already running"
else
  log "starting ${SESSION}"
  tmux new-session -d -s "${SESSION}" \
    "cd '${PROJECT_ROOT}' && tools/limen_runtime_autostart.py --interval 60 >> logs/limen-runtime-autostart.out 2>&1"
fi

tools/limen_runtime_autostart.py --once >> "${BOOTSTRAP_LOG}" 2>&1 || true
log "bootstrap complete"
