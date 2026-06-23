#!/usr/bin/env bash
set -euo pipefail

ROOT="/srv/tyche/projects/limen-ai-edge-case-atlas"
LANES="${1:-16}"
BATCH_SIZE="${2:-24}"
PROVIDER="${HERMES_PROVIDER:-openai-codex}"
MODEL="${HERMES_MODEL:-gpt-5.5}"

cd "$ROOT"
for lane_num in $(seq 1 "$LANES"); do
  lane="$(printf '%02d' "$lane_num")"
  session="limen-case-extraction-lane-${lane}"
  lane_id="lane${lane}"
  if tmux has-session -t "$session" 2>/dev/null; then
    echo "session exists: $session"
    continue
  fi
  tmux new-session -d -s "$session" \
    "cd '$ROOT' && tools/case_extraction_lane.py --lane-id '$lane_id' --batch-size '$BATCH_SIZE' --provider '$PROVIDER' --model '$MODEL' --sleep-empty-seconds 10 --empty-exit-rounds 1"
  echo "started $session batch_size=$BATCH_SIZE"
done
