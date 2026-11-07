#!/usr/bin/env python3
# private-toml.py — CLI entry: `private-toml <command> [args]`. Discovers commands/*.py (hot-loadable).
# Why: one private-config system for every skill that ships to GitHub: real values live OUTSIDE the
#      repo in $CLAUDE_DIR/private/<skill>.toml; the repo ships only local.example.toml (shape).
# NEVER DELETE COMMENTS — explain every non-obvious line.
# Update comments with the code; do not strip them.
import importlib.util, pathlib, sys

def main():
    here = pathlib.Path(__file__).resolve().parent
    sys.path.insert(0, str(here / "lib"))                                   # lib/ = one function per file
    cmds = {p.stem: p for p in sorted((here / "commands").glob("*.py"))}   # drop a file = new command
    name = sys.argv[1] if len(sys.argv) > 1 else "list"                    # no args → overview table
    if name not in cmds:
        sys.exit(f"unknown command {name!r}; have: {', '.join(cmds)}")
    spec = importlib.util.spec_from_file_location(name, cmds[name]); mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    sys.exit(mod.run(sys.argv[2:]) or 0)                                    # run() returns exit code

if __name__ == "__main__":
    main()
