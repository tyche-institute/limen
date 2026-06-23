#!/usr/bin/env bash
set -euo pipefail

PROJECT_ROOT="/srv/tyche/projects/limen-ai-edge-case-atlas"
REVIEW_ROOT="${PROJECT_ROOT}/results/review-candidates"
QUEUE="${REVIEW_ROOT}/direct-source-review-queue.tsv"
TARGET_ROOT="${REVIEW_ROOT}/source-review-drain-targets"
LOG_DIR="${PROJECT_ROOT}/logs/source-review-lanes"
LANES="${1:-16}"
BATCH_SIZE="${2:-100}"
PROVIDER="${HERMES_PROVIDER:-openai-codex}"
MODEL="${HERMES_MODEL:-gpt-5.5}"
STAMP="$(date -u +%Y%m%dT%H%M%SZ)"
TARGET="${TARGET_ROOT}/${STAMP}-direct-source-review-queue.tsv"

mkdir -p "${TARGET_ROOT}" "${LOG_DIR}"
cp "${QUEUE}" "${TARGET}"
printf '%s\n' "${TARGET}" > "${TARGET_ROOT}/current-target.txt"

for lane_num in $(seq 1 "${LANES}"); do
  lane="$(printf '%02d' "${lane_num}")"
  session="limen-source-review-lane-${lane}"
  lane_id="lane${lane}"
  log_path="${LOG_DIR}/${session}.log"
  if tmux has-session -t "${session}" 2>/dev/null; then
    printf 'already_running\t%s\n' "${session}"
    continue
  fi
  tmux new-session -d -s "${session}" \
    "${PROJECT_ROOT}/tools/source_review_lane.py --lane-id ${lane_id} --queue ${TARGET} --batch-size ${BATCH_SIZE} --provider ${PROVIDER} --model ${MODEL} >> ${log_path} 2>&1"
  printf 'started\t%s\t%s\n' "${session}" "${TARGET}"
done
