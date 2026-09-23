#!/usr/bin/env bash
set -euo pipefail

ROOT="/workspace/wiki"
MODE="daily-learning"
DAY_INDEX="auto"
MODEL="gpt-6-luna"
REASONING_EFFORT="max"
NO_SEARCH=0
UNTIL=""
MAX_CONTINUATIONS=96

while (($#)); do
  case "$1" in
    --root) ROOT="$2"; shift 2 ;;
    --mode) MODE="$2"; shift 2 ;;
    --day-index) DAY_INDEX="$2"; shift 2 ;;
    --model) MODEL="$2"; shift 2 ;;
    --reasoning-effort) REASONING_EFFORT="$2"; shift 2 ;;
    --no-search) NO_SEARCH=1; shift ;;
    --until) UNTIL="$2"; shift 2 ;;
    --max-continuations) MAX_CONTINUATIONS="$2"; shift 2 ;;
    *) echo "unknown argument: $1" >&2; exit 64 ;;
  esac
done

if [[ "$ROOT" != "/workspace/wiki" ]]; then
  echo "daily-learning schedule requires project root /workspace/wiki" >&2
  exit 65
fi

if [[ "$MODE" == "daily-learning" && -z "$UNTIL" ]]; then
  UNTIL="10:00"
fi

RUN_DATE="$(TZ=Asia/Shanghai date +%F)"
if [[ "$DAY_INDEX" == "auto" ]]; then
  DAY_INDEX="$(python3 - "$ROOT" <<'PY'
import json
import sys
from pathlib import Path
root = Path(sys.argv[1])
state = root / "outputs/learning-milestones/2026-09-one-month-state.json"
data = json.loads(state.read_text(encoding="utf-8")) if state.exists() else {}
print(int(data.get("next_day_index", 1)))
PY
)"
fi

PROMPT_FILE="$ROOT/outputs/learning-daily/prompts/${RUN_DATE}-day-${DAY_INDEX}.md"
mkdir -p "$(dirname "$PROMPT_FILE")"

if [[ ! -s "$PROMPT_FILE" ]]; then
  python3 "$ROOT/system/scripts/run_daily_learning.py" \
    --root "$ROOT" \
    --day-index "$DAY_INDEX" \
    --mode "$MODE" \
    --model "$MODEL" \
    --reasoning-effort "$REASONING_EFFORT" \
    --prepare-prompt "$PROMPT_FILE"
fi

ARGS=(
  --root "$ROOT"
  --day-index "$DAY_INDEX"
  --mode "$MODE"
  --model "$MODEL"
  --reasoning-effort "$REASONING_EFFORT"
  --prompt-file "$PROMPT_FILE"
  --max-continuations "$MAX_CONTINUATIONS"
)
if [[ -n "$UNTIL" ]]; then
  ARGS+=(--until "$UNTIL")
fi
if ((NO_SEARCH)); then
  ARGS+=(--no-search)
fi

exec python3 "$ROOT/system/scripts/run_daily_learning.py" "${ARGS[@]}"
