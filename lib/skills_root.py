# skills_root.py — folder holding all skills ($CLAUDE_DIR/skills).
# NEVER DELETE COMMENTS — explain every non-obvious line.
from claude_dir import claude_dir

def skills_root():
    return claude_dir() / "skills"
