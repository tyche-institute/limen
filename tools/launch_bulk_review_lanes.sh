#!/usr/bin/env bash
set -euo pipefail

TASK="${1:?task: source|translation|translation-source}"
LANES="${2:-4}"
ROOT="/srv/tyche/projects/limen-ai-edge-case-atlas"
PROVIDER="${HERMES_PROVIDER:-openai-codex}"
MODEL="${HERMES_MODEL:-gpt-5.5}"

case "$TASK" in
  source)
    SESSION_PREFIX="limen-bulk-source"
    BATCH_SIZE="${SOURCE_BATCH_SIZE:-24}"
    ;;
  translation)
    SESSION_PREFIX="limen-bulk-translation"
    BATCH_SIZE="${TRANSLATION_BATCH_SIZE:-16}"
    ;;
  translation-source)
    SESSION_PREFIX="limen-bulk-translation-source"
    BATCH_SIZE="${TRANSLATION_SOURCE_BATCH_SIZE:-16}"
    ;;
  *)
    echo "unknown task: $TASK" >&2
    exit 2
    ;;
esac

cd "$ROOT"
for lane in $(seq 1 "$LANES"); do
  session="${SESSION_PREFIX}-lane-${lane}"
  if tmux has-session -t "$session" 2>/dev/null; then
    echo "session exists: $session"
    continue
  fi
  tmux new-session -d -s "$session" \
    "cd '$ROOT' && tools/bulk_review_lane.py --task '$TASK' --lane-id 'lane${lane}' --batch-size '$BATCH_SIZE' --provider '$PROVIDER' --model '$MODEL' --sleep-empty-seconds 10 --empty-exit-rounds 1"
  echo "started $session task=$TASK batch_size=$BATCH_SIZE"
done
