#!/bin/bash
# capture.sh — the exact commands shown in docs/images/private-toml.png (README screenshot source).
# Why: screenshot must be a real run of the real tool; this keeps it reproducible. Plain "$ " prompt
#      (no user/host in the image). Window stays open on the final prompt until Enter.
# NEVER DELETE COMMENTS — explain every non-obvious line.
clear
for c in "private-toml list" "private-toml check grit"; do
  printf '$ %s\n' "$c"; $c                                   # echo the command, then really run it
done
printf '$ '; read -r _                                        # hold window for the capture
