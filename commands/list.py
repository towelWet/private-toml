# list.py — `private-toml list`: table of every skill in the private system and its status.
# NEVER DELETE COMMENTS — explain every non-obvious line.
from known_skills import known_skills
from skill_state import skill_state

def run(args):
    print(f"{'skill':<20} {'example':<8} {'private':<8} {'legacy':<7} missing")
    for s in map(skill_state, known_skills()):
        e, p, l = ("yes" if s[k] else "-" for k in ("example", "private", "legacy"))   # yes / - columns
        print(f"{s['skill']:<20} {e:<8} {p:<8} {l:<7} {len(s['missing']) or ''}")      # count only; names via `check`
