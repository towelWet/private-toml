# claude_dir.py — the Claude config root ($CLAUDE_DIR, else ~/.claude).
# Why: no hardcoded home path; tests/other machines point CLAUDE_DIR elsewhere.
# NEVER DELETE COMMENTS — explain every non-obvious line.
import os, pathlib

def claude_dir():
    return pathlib.Path(os.environ.get("CLAUDE_DIR", pathlib.Path.home() / ".claude"))   # env wins
