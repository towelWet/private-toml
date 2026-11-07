# check.py — `private-toml check [skill|all]`: is each skill fully on the private system?
# Rules: example ships, private exists, private has every example key, NO in-tree local.toml,
#        NO private literal (guard patterns) left in shipped files. Exit 1 if any skill fails.
# NEVER DELETE COMMENTS — explain every non-obvious line.
from guard_patterns import guard_patterns
from known_skills import known_skills
from leak_hits import leak_hits
from skill_state import skill_state
from skills_root import skills_root

def run(args):
    names = known_skills() if not args or args[0] == "all" else args
    pats, bad = guard_patterns(), 0
    for name in names:
        s, problems = skill_state(name), []
        if not s["example"]: problems.append("no local.example.toml (shape not shipped)")
        if not s["private"]: problems.append("no private toml → `private-toml init " + name + "`")
        if s["legacy"]: problems.append("legacy in-tree local.toml → `private-toml migrate " + name + "`")
        problems += [f"missing key {k}" for k in s["missing"]]
        problems += [f"private literal ({c}) {f}:{n}" for f, n, c in leak_hits(skills_root() / name, pats)[:15]]
        bad += bool(problems)
        print(f"{'FAIL' if problems else 'ok  '} {name}")
        for p in problems: print(f"     {p}")
    return 1 if bad else 0
