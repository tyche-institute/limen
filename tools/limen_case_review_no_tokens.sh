#!/usr/bin/env bash
set -euo pipefail

PROJECT_ROOT="${PROJECT_ROOT:-/srv/tyche/projects/limen-ai-edge-case-atlas}"
FRONTEND_ROOT="${FRONTEND_ROOT:-/srv/tyche/local-projects/home-anton-projects/tyche-research-vault}"
REFRESH_FRONTENDS=0
DEPLOY_FRONTENDS=0
STAMP="$(date -u +%Y%m%dT%H%M%SZ)"
LOG="${PROJECT_ROOT}/logs/limen-case-review-no-tokens-${STAMP}.log"
STATUS_OUT="${PROJECT_ROOT}/runtime/limen-case-review-no-tokens-status-latest.json"
COMPACT_OUT="${PROJECT_ROOT}/runtime/limen-case-review-no-tokens-compact-latest.json"
AUDIT_OUT="${PROJECT_ROOT}/runtime/limen-token-free-review-audit-latest.json"

usage() {
  cat <<'EOF'
usage: limen_case_review_no_tokens.sh [--refresh-frontends] [--deploy-frontends]

Runs deterministic LIMEN case review stages without paid model calls.

This script does not call hermes, codex, openai, claude, or any LLM API. It only
uses local ledgers plus bounded source/source-family rules. Case promotion still
stops at the reviewed-core/ObscureAI human-acceptance boundary.
EOF
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --refresh-frontends) REFRESH_FRONTENDS=1 ;;
    --deploy-frontends) REFRESH_FRONTENDS=1; DEPLOY_FRONTENDS=1 ;;
    -h|--help) usage; exit 0 ;;
    *) echo "unknown arg: $1" >&2; usage >&2; exit 2 ;;
  esac
  shift
done

cd "${PROJECT_ROOT}"
mkdir -p "$(dirname "${LOG}")" "$(dirname "${STATUS_OUT}")"

log() {
  printf '[%s] %s\n' "$(date -u +%FT%TZ)" "$*" | tee -a "${LOG}" >&2
}

run_logged() {
  log "run: $*"
  "$@" >> "${LOG}" 2>&1
}

LOCK="${PROJECT_ROOT}/runtime/limen-case-review-no-tokens.lock"
exec 9>"${LOCK}"
if ! flock -n 9; then
  log "another token-free case-review run is active; leaving data untouched"
  python3 tools/limen_compact_status.py > "${COMPACT_OUT}"
  python3 - "${COMPACT_OUT}" "${STATUS_OUT}" <<'PY'
import json
import sys
from datetime import datetime, timezone

compact_path, status_path = sys.argv[1:3]
status = json.load(open(compact_path, encoding="utf-8"))
case_autoreview = status.get("case_autoreview") or {}
payload = {
    "generated_at_utc": datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
    "ok": False,
    "blocked_by_lock": True,
    "case_hardening": status.get("case_hardening") or {},
    "case_autoreview": case_autoreview,
    "compact_status_path": compact_path,
}
open(status_path, "w", encoding="utf-8").write(json.dumps(payload, ensure_ascii=False, sort_keys=True) + "\n")
print(json.dumps(payload, ensure_ascii=False, sort_keys=True))
PY
  exit 0
fi

refresh_frontends() {
  (
    cd "${FRONTEND_ROOT}"
    run_logged python3 scripts/build_limen_observatory_snapshot.py
    run_logged python3 -m json.tool sites/limen-observatory/data/limen-snapshot.json
    run_logged node --check sites/limen-observatory/app.js
    run_logged python3 scripts/build_obscure_ai_dataset.py
    run_logged python3 -m json.tool sites/obscure-ai/data/cases.json
    run_logged node --check sites/obscure-ai/app.js
    if [[ "${DEPLOY_FRONTENDS}" == "1" ]]; then
      run_logged npx wrangler pages deploy sites/limen-observatory --project-name limen-observatory --branch main
      run_logged npx wrangler pages deploy sites/obscure-ai --project-name obscure-ai --branch main
    fi
  )
}

log "token-free case review start log=${LOG}"
run_logged python3 tools/build_reviewed_core_case_hardening_review.py
run_logged python3 tools/build_case_review_autorecommendations.py
run_logged python3 tools/limen_token_free_review_audit.py --out "${AUDIT_OUT}"

if [[ "${REFRESH_FRONTENDS}" == "1" ]]; then
  log "refreshing frontend datasets deploy=${DEPLOY_FRONTENDS}"
  refresh_frontends
fi

python3 tools/limen_compact_status.py > "${COMPACT_OUT}"

python3 - "${COMPACT_OUT}" "${STATUS_OUT}" "${AUDIT_OUT}" <<'PY'
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

compact_path = Path(sys.argv[1])
status_path = Path(sys.argv[2])
audit_path = Path(sys.argv[3])
status = json.loads(compact_path.read_text(encoding="utf-8"))
try:
    audit = json.loads(audit_path.read_text(encoding="utf-8"))
except Exception:
    audit = {}
case_hardening = status.get("case_hardening") or {}
case_autoreview = status.get("case_autoreview") or {}
payload = {
    "generated_at_utc": datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
    "ok": (
        case_autoreview.get("paid_token_required_rows", 0) == 0
        and case_autoreview.get("human_acceptance_required_rows", 0) == 0
    ),
    "blocked_by_lock": False,
    "case_hardening": case_hardening,
    "case_autoreview": case_autoreview,
    "token_free_review_audit": {
        "ok": audit.get("ok"),
        "generated_at_utc": audit.get("generated_at_utc"),
        "current_paid_token_required_rows": audit.get("current_paid_token_required_rows"),
        "current_human_required_rows": audit.get("current_human_required_rows"),
        "current_missing_review_rows": audit.get("current_missing_review_rows"),
        "path": str(audit_path),
    },
    "compact_status_path": str(compact_path),
    "status_path": str(status_path),
}
status_path.write_text(json.dumps(payload, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps(payload, ensure_ascii=False, sort_keys=True))
PY

log "token-free case review complete"
