# leak_hits.py — files in a skill tree that contain a private literal (path/identity) → should be in private TOML.
# Why: "uses the private system" is only true if no private value is still hardcoded in shipped files.
#      Skips what never ships: .grit, local.toml, db/, caches, binaries, and the manifest's excludes.
# NEVER DELETE COMMENTS — explain every non-obvious line.
import fnmatch
from load_toml import load_toml
SKIP = {".grit", ".git", "__pycache__", "db", "build", ".build", ".build-tmp", "target", "node_modules",
        "Reference", ".DS_Store"}                                              # = publish gate default excludes

def leak_hits(root, patterns):
    man = load_toml(root / ".github-publish.toml") or {}
    excl = list(man.get("excludes", [])) + ["local.toml", ".github-publish.toml"]
    allow = {a.lower() for a in man.get("allow", [])}                     # e.g. "identity:<public handle>" = public on purpose
    hits = []
    for f in root.rglob("*"):
        rel = f.relative_to(root).as_posix()
        if not f.is_file() or set(f.relative_to(root).parts) & SKIP or f.stat().st_size > 2_000_000:
            continue                                                         # never-shipped or too big to be source
        if any(fnmatch.fnmatch(rel, e) or rel.startswith(e.rstrip("/") + "/") for e in excl):
            continue                                                         # manifest says it never ships
        text = f.read_bytes().decode("latin-1")
        for cat, rx in patterns:
            m = rx.search(text)
            if m and f"{cat}:{m.group(0).lower()}" not in allow:
                hits.append((rel, text.count("\n", 0, m.start()) + 1, cat)); break   # first hit per file is enough
    return hits
