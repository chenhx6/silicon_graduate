#!/usr/bin/env bash
set -euo pipefail

script_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd -P)"
wiki_root="$(cd -- "$script_dir/../.." && pwd -P)"

exec python3 "$script_dir/run_daily_learning_at.py" --root "$wiki_root" "$@"
