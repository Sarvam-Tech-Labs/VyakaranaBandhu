#!/bin/bash
# usage: clone.sh owner/repo [dest-name]   (unauthenticated, shallow, credential helpers disabled)
OUT=/workspaces/codespaces-blank/sandhi_work/external_data/raw
repo="$1"; name="${2:-$(echo $repo | sed 's,/,__,')}"
dest="$OUT/$name"
if [ -d "$dest" ]; then echo "EXISTS $dest"; exit 0; fi
GIT_TERMINAL_PROMPT=0 GIT_ASKPASS=/bin/true git -c credential.helper= -c core.askPass=/bin/true clone --depth 1 --quiet "https://github.com/$repo.git" "$dest" 2>&1 | tail -3
if [ -d "$dest/.git" ]; then (cd "$dest" && echo "OK $repo commit=$(git rev-parse HEAD) size=$(du -sh . | cut -f1)"); else echo "FAIL $repo"; fi
