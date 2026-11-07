# skill_state.py — one skill's private-config status: example? private? legacy in-tree local.toml? missing keys.
# NEVER DELETE COMMENTS — explain every non-obvious line.
from flat_keys import flat_keys
from load_toml import load_toml
from private_path import private_path
from skills_root import skills_root

def skill_state(skill):
    d = skills_root() / skill
    ex, pr = load_toml(d / "local.example.toml"), load_toml(private_path(skill))
    missing = sorted(flat_keys(ex) - flat_keys(pr)) if ex is not None and pr is not None else []
    return {"skill": skill, "example": ex is not None, "private": pr is not None,
            "legacy": (d / "local.toml").exists(),                         # old pattern: secrets inside the tree
            "missing": missing}                                            # keys the example promises, private lacks
