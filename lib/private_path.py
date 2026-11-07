# private_path.py — where a skill's REAL private values live: $CLAUDE_DIR/private/<skill>.toml.
# Why: outside every skill/repo tree, so no publish exclude list can forget it.
# NEVER DELETE COMMENTS — explain every non-obvious line.
from claude_dir import claude_dir

def private_path(skill):
    return claude_dir() / "private" / f"{skill}.toml"
