# known_skills.py — skills that take part in the private system (example, private file, or legacy local.toml).
# NEVER DELETE COMMENTS — explain every non-obvious line.
from claude_dir import claude_dir
from skills_root import skills_root

def known_skills():
    root = skills_root()
    names = {p.parent.name for p in root.glob("*/local.example.toml")}     # shape shipped in repo
    names |= {p.parent.name for p in root.glob("*/local.toml")}            # legacy, needs migrate
    names |= {p.stem for p in (claude_dir() / "private").glob("*.toml")}    # private values already present
    return sorted(n for n in names if (root / n).is_dir() and not (root / n).is_symlink())   # aliases (x → x-viewer) count once
