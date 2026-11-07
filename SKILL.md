---
name: private-toml
description: >-
  One private-config system for every skill that ships to GitHub. Real values (paths, handles,
  hashes, aliases) live OUTSIDE the repo in $CLAUDE_DIR/private/<skill>.toml; the repo ships only
  local.example.toml (same keys, placeholder values). CLI lists, checks, inits and migrates skills.
  Use on /private-toml, "private toml", "move secrets out of the skill", before publishing a skill.
triggers: ["/private-toml", "private toml", "private config", "local.example.toml"]
---

# /private-toml

Real private values never live inside a skill folder, so no publish exclude list can forget them.

| File | Where | Ships to GitHub |
|---|---|---|
| `local.example.toml` | inside the skill | yes — keys + `<placeholder>` values |
| `<skill>.toml` | `$CLAUDE_DIR/private/` (default `~/.claude/private/`) | never |

Code finds the private file through `$CLAUDE_DIR` (or a skill-specific env override) — never a
hardcoded home path.

## Commands

| Command | Does |
|---|---|
| `private-toml list` | every skill in the system: example? private? legacy in-tree `local.toml`? missing keys |
| `private-toml check [skill\|all]` | fails on: no example, no private file, missing keys, legacy `local.toml`, private literal in shipped files |
| `private-toml init <skill>` | create the private file from the example (never overwrites) |
| `private-toml migrate <skill>` | legacy `local.toml` → private file + generated example (never overwrites; legacy file left for you to remove) |
| `private-toml path <skill>` | print the private path (for scripts) |

Drop a file in `commands/` = new command (hot-loaded). `lib/` = one function per file.

## Leak scan

`check` reads forbidden regexes from the private publish guard
(`$CLAUDE_DIR/github-publish-guard/patterns.toml`, `[paths]` + `[identity]`) and scans the files a
publish would ship (honours `.github-publish.toml` `excludes` and `allow`). No guard file → no scan.

## Adopting it in a skill

1. Write `local.example.toml` (or `private-toml migrate <skill>` from an old `local.toml`).
2. Point readers at `$CLAUDE_DIR/private/<skill>.toml`.
3. `private-toml init <skill>` on a new machine, fill the placeholders.
4. `private-toml check <skill>` must say `ok` before publishing.
