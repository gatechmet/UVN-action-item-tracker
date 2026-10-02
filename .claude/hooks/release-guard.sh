#!/usr/bin/env bash
# Blocks git commit/push when the release is not a fresh shared-folder build of tracker.html.
cmd=$(python3 -c 'import json,sys;print(json.load(sys.stdin).get("tool_input",{}).get("command",""))' 2>/dev/null)
case "$cmd" in *"git commit"*|*"git push"*) ;; *) exit 0;; esac
root=$(git rev-parse --show-toplevel 2>/dev/null) || exit 0
[ -f "$root/shared-drive-demo/build/build.py" ] || exit 0
if ! out=$(python3 "$root/shared-drive-demo/build/build.py" --check 2>&1); then
  printf 'Blocked: the shared-folder release is out of step.\n%s\nEdit tracker.html, run python3 shared-drive-demo/build/build.py, then commit. See CLAUDE.md.\n' "$out" >&2
  exit 2
fi
exit 0
