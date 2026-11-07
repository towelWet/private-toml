# init.py — `private-toml init <skill>`: create $CLAUDE_DIR/private/<skill>.toml from the shipped example.
# Why: fresh machine / new skill: start from the shape, then fill real values. Never overwrites.
# NEVER DELETE COMMENTS — explain every non-obvious line.
from private_path import private_path
from skills_root import skills_root

def run(args):
    if not args: return print("usage: private-toml init <skill>") or 2
    ex, dst = skills_root() / args[0] / "local.example.toml", private_path(args[0])
    if dst.exists(): return print(f"exists, untouched: {dst}") or 0         # never clobber real values
    if not ex.exists(): return print(f"no {ex} — write the example first") or 1
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_text(ex.read_text()); print(f"created {dst} — replace every <placeholder>")
    return 0
