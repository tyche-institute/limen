#!/usr/bin/env bash
# limen_runtime_bootstrap.sh
# -----------------------------------------------------------------------------
# LIMEN AI edge-case atlas — funnel ADVANCER (staging only).
#
# Purpose
#   Re-animate the dead cron entry that is supposed to keep the LIMEN evidence
#   funnel moving. It chains the EXISTING pipeline scripts in scripts/ in the
#   intended order:
#
#       mining (external, NOT started here)
#         -> direct-source verify        (verify_candidate_signals.py)
#         -> extract edge cases          (extract_edge_cases.py)
#         -> confidence / scoring        (run_confidence_scoring.py / confidence_scoring.py)
#         -> adjudication STAGING        (refresh draft-adjudication + promotion-packet snapshot)
#         -> dashboard aggregates        (dashboard_agg.py)
#
#   It STAGES results so candidates move toward reviewed-core, and writes a
#   staging-status.json snapshot of the current funnel counts. It deliberately
#   stops at the human-controlled boundary.
#
# HARD BOUNDARIES (do not remove — they define what this script is allowed to do)
#   * NEVER promotes anything into reviewed-core or ObscureAI. Final adjudication
#     stays a human-controlled copy step (see status JSONs in review-candidates/).
#   * NEVER deploys anything public. NO wrangler, NO `pages deploy`, NO git push,
#     NO Zenodo. Public sites are built+deployed by humans / the sanitiser.
#   * NEVER starts CPU-mining sessions or any tmux/process. It only runs the
#     deterministic, no-LLM staging scripts that already exist.
#   * no sudo. Runs entirely as the invoking user against project paths.
#
# Safety / hygiene
#   * idempotent + single-flight: a lock dir prevents overlapping cron runs
#     (cron fires every 5 min; a long run will be skipped, not stacked).
#   * honours /srv/tyche/STOP (global) and a project STOP file.
#   * each stage is best-effort: a missing input or a failing prototype script
#     is logged and skipped; it never aborts the whole chain or the cron.
#   * all output to logs/ ; staging artifacts to runtime/ and a stamped snapshot.
# -----------------------------------------------------------------------------

set -u -o pipefail

# ----- paths -----------------------------------------------------------------
PROJECT_DIR="/srv/tyche/projects/limen-ai-edge-case-atlas"
SCRIPTS_DIR="${PROJECT_DIR}/scripts"
RUNTIME_DIR="${PROJECT_DIR}/runtime"
LOG_DIR="${PROJECT_DIR}/logs"
RESULTS_DIR="${PROJECT_DIR}/results"
REVIEW_DIR="${RESULTS_DIR}/review-candidates"
DATA_DIR="${PROJECT_DIR}/data"

LOCK_DIR="${RUNTIME_DIR}/.bootstrap.lock"
LOG_FILE="${LOG_DIR}/limen-runtime-bootstrap.log"

# STOP files: global fleet stop + project-local stop.
GLOBAL_STOP="/srv/tyche/STOP-limen-runtime"
GLOBAL_STOP_ALL="/srv/tyche/STOP"
PROJECT_STOP="${PROJECT_DIR}/STOP"
PROJECT_STOP_RUNTIME="${PROJECT_DIR}/STOP-runtime"

# Prefer the project venv python; fall back to system python3.
if [ -x "${PROJECT_DIR}/venv/bin/python" ]; then
  PY="${PROJECT_DIR}/venv/bin/python"
elif [ -x "${SCRIPTS_DIR}/venv/bin/python" ]; then
  PY="${SCRIPTS_DIR}/venv/bin/python"
else
  PY="$(command -v python3 || command -v python || echo python3)"
fi

RUN_TS="$(date -u +%Y%m%dT%H%M%SZ)"
SNAP_DIR="${RUNTIME_DIR}/staging/${RUN_TS}"

mkdir -p "${RUNTIME_DIR}" "${LOG_DIR}" >/dev/null 2>&1 || true

log() {
  printf '%s [bootstrap] %s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)" "$*" >> "${LOG_FILE}"
}

# ----- STOP guards -----------------------------------------------------------
for stop in "${GLOBAL_STOP}" "${GLOBAL_STOP_ALL}" "${PROJECT_STOP}" "${PROJECT_STOP_RUNTIME}"; do
  if [ -e "${stop}" ]; then
    log "STOP file present (${stop}); exiting without action."
    exit 0
  fi
done

# ----- single-flight lock (idempotent, no overlap) ---------------------------
if ! mkdir "${LOCK_DIR}" 2>/dev/null; then
  # Stale-lock recovery: if the lock is older than 60 min, assume a dead run.
  if [ -d "${LOCK_DIR}" ]; then
    lock_age=$(( $(date +%s) - $(stat -c %Y "${LOCK_DIR}" 2>/dev/null || echo 0) ))
    if [ "${lock_age}" -gt 3600 ]; then
      log "Stale lock (${lock_age}s); reclaiming."
      rm -rf "${LOCK_DIR}" 2>/dev/null || true
      mkdir "${LOCK_DIR}" 2>/dev/null || { log "Could not reclaim lock; exiting."; exit 0; }
    else
      log "Another bootstrap run holds the lock (age ${lock_age}s); skipping this tick."
      exit 0
    fi
  fi
fi
# Always release the lock on exit.
cleanup() { rm -rf "${LOCK_DIR}" 2>/dev/null || true; }
trap cleanup EXIT INT TERM

mkdir -p "${SNAP_DIR}" >/dev/null 2>&1 || true
log "=== run ${RUN_TS} start (py=${PY}) ==="

# Stage runner: never lets one stage kill the chain.
#   run_stage <human-label> <command...>
run_stage() {
  local label="$1"; shift
  log "stage[${label}] begin: $*"
  if "$@" >>"${LOG_FILE}" 2>&1; then
    log "stage[${label}] ok"
    return 0
  else
    local rc=$?
    log "stage[${label}] non-zero exit (${rc}); continuing chain"
    return 0
  fi
}

# Existence helper.
have() { [ -e "$1" ]; }

# =============================================================================
# STAGE 1 — direct-source verify
#   verify_candidate_signals.py compares mined candidate signals against the
#   direct-source review queue / authority targets. It is a read-only reporter;
#   we capture its output as a staging artifact. It uses repo-relative paths,
#   so we run it from PROJECT_DIR and only if its inputs exist.
# =============================================================================
VERIFY_SCRIPT="${SCRIPTS_DIR}/verify_candidate_signals.py"
if have "${VERIFY_SCRIPT}"; then
  (
    cd "${PROJECT_DIR}" || exit 0
    run_stage "verify" "${PY}" "${VERIFY_SCRIPT}"
  ) >"${SNAP_DIR}/01-verify-candidate-signals.out" 2>&1 || true
  log "stage[verify] artifact -> ${SNAP_DIR}/01-verify-candidate-signals.out"
else
  log "stage[verify] script missing (${VERIFY_SCRIPT}); skipped"
fi

# =============================================================================
# STAGE 2 — extract edge cases
#   extract_edge_cases.py walks a crawl dir for *.jsonl and filters records
#   into a candidate output. We only run it when there is an input dir to walk
#   AND it would have somewhere to write; output goes to the staging snapshot
#   (never overwrites a curated funnel file).
# =============================================================================
EXTRACT_SCRIPT="${SCRIPTS_DIR}/extract_edge_cases.py"
EXTRACT_INPUT=""
for cand in "${DATA_DIR}/processed" "${PROJECT_DIR}/fetches" "${DATA_DIR}/cases"; do
  if have "${cand}"; then EXTRACT_INPUT="${cand}"; break; fi
done
if have "${EXTRACT_SCRIPT}" && [ -n "${EXTRACT_INPUT}" ]; then
  run_stage "extract" "${PY}" "${EXTRACT_SCRIPT}" "${EXTRACT_INPUT}" \
    -o "${SNAP_DIR}/02-extracted-edge-cases.jsonl"
  log "stage[extract] input=${EXTRACT_INPUT} -> ${SNAP_DIR}/02-extracted-edge-cases.jsonl"
else
  log "stage[extract] skipped (script or input dir absent; input='${EXTRACT_INPUT}')"
fi

# =============================================================================
# STAGE 3 — confidence / scoring
#   run_confidence_scoring.py and confidence_scoring.py compute composite
#   confidence over clusters. The prototype scripts carry hardcoded input
#   paths; we run them only when those inputs are actually present, so a run on
#   a machine without a given boost shard is a clean skip, not a crash.
# =============================================================================
CONF_RUN="${SCRIPTS_DIR}/run_confidence_scoring.py"
CONF_CORE="${SCRIPTS_DIR}/confidence_scoring.py"
BOOST011="${RESULTS_DIR}/boost/limen-boost-011"
if have "${CONF_RUN}" && have "${BOOST011}/duplicate-clusters.json" \
   && have "${BOOST011}/taxonomy-delta.json"; then
  run_stage "confidence-run" "${PY}" "${CONF_RUN}"
  if have "${BOOST011}/confidence_scores.json"; then
    cp -f "${BOOST011}/confidence_scores.json" \
      "${SNAP_DIR}/03-confidence_scores.json" 2>/dev/null || true
  fi
elif have "${CONF_CORE}"; then
  log "stage[confidence] boost-011 cluster inputs absent; scorer left idle (no usable input)"
else
  log "stage[confidence] scripts/inputs absent; skipped"
fi

# =============================================================================
# STAGE 4 — adjudication STAGING (the heart of "advance toward reviewed-core")
#   We DO NOT write into reviewed-core or ObscureAI. We refresh a *draft*
#   adjudication snapshot from the existing hardening-review + autoreview
#   ledgers, and recompute funnel readiness counts. Anyone reading the snapshot
#   sees which candidates are "ready_for_human_acceptance" without anything
#   being promoted automatically.
#
#   Sources (already produced by the funnel, read-only here):
#     reviewed-core-case-hardening-review-v0.1.tsv      (verdicts)
#     reviewed-core-case-autoreview-v0.1.tsv            (deterministic draft recs)
#     reviewed-core-case-final-adjudication-draft-v0.1.tsv (current draft ledger)
#     reviewed-core-promotion-packet-status.json        (packet readiness)
# =============================================================================
ADJ_DRAFT="${REVIEW_DIR}/reviewed-core-case-final-adjudication-draft-v0.1.tsv"
AUTOREVIEW="${REVIEW_DIR}/reviewed-core-case-autoreview-v0.1.tsv"
HARDENING="${REVIEW_DIR}/reviewed-core-case-hardening-review-v0.1.tsv"
PACKET_STATUS="${REVIEW_DIR}/reviewed-core-promotion-packet-status.json"
HARDENING_STATUS="${REVIEW_DIR}/reviewed-core-case-hardening-review-status.json"

# Copy the current draft-stage ledgers into the snapshot (staging, never promote).
for f in "${ADJ_DRAFT}" "${AUTOREVIEW}" "${HARDENING}"; do
  if have "${f}"; then
    cp -f "${f}" "${SNAP_DIR}/04-$(basename "${f}")" 2>/dev/null || true
  fi
done
log "stage[adjudication] draft ledgers snapshotted (no promotion performed)"

# Recompute funnel readiness from the existing status JSONs and emit a single
# staging-status.json. Pure stdlib python; never touches reviewed-core.
"${PY}" - "$RUN_TS" "$PACKET_STATUS" "$HARDENING_STATUS" "$SNAP_DIR" "$RUNTIME_DIR" <<'PYEOF' >>"${LOG_FILE}" 2>&1 || log "stage[adjudication] status synth had a non-zero exit; continuing"
import json, os, sys

run_ts, packet_status, hardening_status, snap_dir, runtime_dir = sys.argv[1:6]

def load(p):
    try:
        with open(p) as fh:
            return json.load(fh)
    except Exception:
        return {}

pkt = load(packet_status)
hrd = load(hardening_status)

snapshot = {
    "generated_at_utc": run_ts,
    "stage": "staging_only",
    "boundary": ("Staging advancer: refreshes draft adjudication + funnel counts only. "
                 "No reviewed-core promotion, no ObscureAI addition, no public deploy. "
                 "Final adjudication is a human-controlled copy step."),
    "funnel": {
        "promotion_packet_rows": pkt.get("packet_rows"),
        "unique_signal_ids": pkt.get("unique_signal_ids"),
        "unique_source_clusters": pkt.get("unique_source_clusters"),
        "reviewed_core_ready_now": pkt.get("reviewed_core_ready_now"),
        "obscure_ai_ready_now": pkt.get("obscure_ai_ready_now"),
        "reviewed_core_ready_for_human_acceptance_pre_adjudication":
            hrd.get("reviewed_core_ready_for_human_acceptance_pre_adjudication"),
        "case_hardening_review_rows": hrd.get("case_hardening_review_rows"),
        "hardening_verdict_counts": hrd.get("hardening_verdict_counts"),
        "case_final_decision_counts": hrd.get("case_final_decision_counts"),
    },
    "next_human_action": ("Review candidates flagged ready_for_human_acceptance and, if accepted, "
                          "copy them into reviewed-core-case-final-adjudication-v0.1.tsv by hand; "
                          "then rebuild cases.json and deploy via the human sanitiser path."),
}

# Snapshot copy (immutable, stamped) + a stable 'latest' pointer in runtime/.
for dest in (os.path.join(snap_dir, "staging-status.json"),
             os.path.join(runtime_dir, "staging-status.latest.json")):
    try:
        with open(dest, "w") as fh:
            json.dump(snapshot, fh, indent=2)
        print("[adjudication] wrote", dest)
    except Exception as e:  # pragma: no cover
        print("[adjudication] could not write", dest, ":", e)
PYEOF
log "stage[adjudication] staging-status snapshot refreshed"

# =============================================================================
# STAGE 5 — dashboard aggregates (local JSON only; no deploy)
#   dashboard_agg.py emits api/dashboard/aggregates.json from local ledgers.
#   This is a local build artifact; publishing it is a separate human step.
#   Run only when its primary input ledger exists.
# =============================================================================
DASH_AGG="${SCRIPTS_DIR}/dashboard_agg.py"
SRC_LEDGER="${PROJECT_DIR}/sources/source-family-ledger.tsv"
if have "${DASH_AGG}" && have "${SRC_LEDGER}"; then
  (
    cd "${PROJECT_DIR}" || exit 0
    run_stage "dashboard-agg" "${PY}" "${DASH_AGG}"
  )
else
  log "stage[dashboard-agg] script or source ledger absent; skipped (no deploy attempted)"
fi

# ----- retention: keep the staging snapshots from ballooning ------------------
# Defensive local prune (housekeeping.py is the authoritative capper). Keep the
# 24 most recent stamped snapshots; drop older ones.
if [ -d "${RUNTIME_DIR}/staging" ]; then
  ls -1dt "${RUNTIME_DIR}/staging"/*/ 2>/dev/null | tail -n +25 | while read -r old; do
    rm -rf "${old}" 2>/dev/null || true
  done
fi

log "=== run ${RUN_TS} done -> snapshot ${SNAP_DIR} ==="
exit 0
