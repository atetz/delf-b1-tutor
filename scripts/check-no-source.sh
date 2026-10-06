#!/usr/bin/env bash
# Blocks commits that would add restricted or commercial source material.
# Generic checks live here; titles, authors and publishers to block go in the gitignored
# file .source-patterns (one extended regex per line), so the list itself stays private.
set -euo pipefail
root=$(git rev-parse --show-toplevel)
files=$(git diff --cached --name-only --diff-filter=ACM)
[ -z "$files" ] && exit 0
fail=0

if echo "$files" | grep -Ei '\.(pdf|epub|mp3|m4a|wav|ogg|mp4)$|(^|/)learner/'; then
  echo "✗ Staged file type or path that must stay private (see above)."; fail=1
fi

patterns='(^|[^[:alnum:]])p\. ?[0-9]+|pages? [0-9]+ ?[-–] ?[0-9]+|réservé aux (correcteurs|examinateurs)'
if [ -f "$root/.source-patterns" ]; then
  extra=$(grep -v '^\s*#' "$root/.source-patterns" | grep -v '^\s*$' | paste -sd'|' -)
  [ -n "$extra" ] && patterns="$patterns|$extra"
fi

for f in $files; do
  case "$f" in scripts/check-no-source.sh|docs/*) continue;; esac
  if git show ":$f" | grep -EinH --label="$f" "$patterns"; then fail=1; fi
done

if [ $fail -ne 0 ]; then
  echo "✗ Possible source reference above. Rewrite in your own words or remove it."; exit 1
fi
