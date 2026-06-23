#!/usr/bin/env bash
set -euo pipefail

PROJECT_ROOT="/srv/tyche/projects/limen-ai-edge-case-atlas"
LOG_DIR="${PROJECT_ROOT}/logs/hardening-review-lanes"
TASK="${1:-all}"
LANES="${2:-16}"
URL_BATCH_SIZE="${URL_BATCH_SIZE:-15}"
TRANSLATION_BATCH_SIZE="${TRANSLATION_BATCH_SIZE:-32}"
PROVIDER="${HERMES_PROVIDER:-openai-codex}"
MODEL="${HERMES_MODEL:-gpt-5.5}"

mkdir -p "${LOG_DIR}"
"${PROJECT_ROOT}/tools/prepare_hardening_review_queues.py"

launch_task() {
  local task="$1"
  local prefix="$2"
  local batch_size="$3"
  for lane_num in $(seq 1 "${LANES}"); do
    local lane="$(printf '%02d' "${lane_num}")"
    local session="${prefix}-${lane}"
    local lane_id="lane${lane}"
    local log_path="${LOG_DIR}/${session}.log"
    if tmux has-session -t "${session}" 2>/dev/null; then
      printf 'already_running\t%s\n' "${session}"
      continue
    fi
    tmux new-session -d -s "${session}" \
      "${PROJECT_ROOT}/tools/hardening_review_lane.py --task ${task} --lane-id ${lane_id} --batch-size ${batch_size} --provider ${PROVIDER} --model ${MODEL} >> ${log_path} 2>&1"
    printf 'started\t%s\t%s\tbatch_size=%s\n' "${session}" "${task}" "${batch_size}"
  done
}

case "${TASK}" in
  all)
    launch_task url limen-url-hardening-lane "${URL_BATCH_SIZE}"
    launch_task translation limen-translation-review-lane "${TRANSLATION_BATCH_SIZE}"
    ;;
  url)
    launch_task url limen-url-hardening-lane "${URL_BATCH_SIZE}"
    ;;
  translation)
    launch_task translation limen-translation-review-lane "${TRANSLATION_BATCH_SIZE}"
    ;;
  *)
    echo "usage: $0 [all|url|translation] [lanes]" >&2
    exit 2
    ;;
esac
