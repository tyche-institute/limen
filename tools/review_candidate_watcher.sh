#!/usr/bin/env bash
set -euo pipefail

PROJECT_ROOT="/srv/tyche/projects/limen-ai-edge-case-atlas"
LOG_DIR="${PROJECT_ROOT}/logs"
SLEEP_SECONDS="${LIMEN_REVIEW_CANDIDATE_WATCHER_SLEEP_SECONDS:-120}"
mkdir -p "${LOG_DIR}"

while true; do
  "${PROJECT_ROOT}/tools/materialize_review_candidates.py" --no-journal >> "${LOG_DIR}/review-candidate-materializer.log" 2>&1
  "${PROJECT_ROOT}/tools/review_all_candidates.py" --no-journal >> "${LOG_DIR}/review-candidate-reviewer.log" 2>&1
  sleep "${SLEEP_SECONDS}"
done
