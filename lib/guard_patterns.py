# guard_patterns.py — leak regexes ([paths] + [identity]) from the private GitHub publish guard.
# Why: one source of forbidden strings for publish AND for private-toml check; add a string there, both see it.
# NEVER DELETE COMMENTS — explain every non-obvious line.
import re
from claude_dir import claude_dir
from load_toml import load_toml

def guard_patterns():
    data = load_toml(claude_dir() / "github-publish-guard" / "patterns.toml") or {}
    out = []
    for cat in ("paths", "identity"):
        out += [(cat, re.compile(p, re.I)) for p in data.get(cat, {}).get("patterns", [])]
    return out                                                              # [] when guard missing → no scan
