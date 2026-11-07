# migrate.py — `private-toml migrate <skill>`: legacy in-tree local.toml → private toml + shipped example.
# Steps: copy real values to $CLAUDE_DIR/private/<skill>.toml (never overwrite), write local.example.toml
#        with placeholders (never overwrite). The legacy file is LEFT in place (no move/trash without user
#        approval); code readers must be switched by hand, then the user trashes it.
# NEVER DELETE COMMENTS — explain every non-obvious line.
from placeholder_line import placeholder_line
from private_path import private_path
from skills_root import skills_root

def run(args):
    if not args: return print("usage: private-toml migrate <skill>") or 2
    d = skills_root() / args[0]; src, dst, ex = d / "local.toml", private_path(args[0]), d / "local.example.toml"
    if not src.exists(): return print(f"no legacy {src}") or 1
    dst.parent.mkdir(parents=True, exist_ok=True)
    print(f"private: {'exists, untouched' if dst.exists() else 'created'} {dst}")
    if not dst.exists(): dst.write_text(src.read_text())                    # real values leave the tree
    print(f"example: {'exists, untouched' if ex.exists() else 'created'} {ex}")
    if not ex.exists(): ex.write_text("\n".join(map(placeholder_line, src.read_text().split("\n"))))
    print(f"next: point readers at private path, then trash {src} (your approval)")
    return 0
