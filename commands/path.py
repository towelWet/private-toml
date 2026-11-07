# path.py — `private-toml path <skill>`: print the private toml path (for shell scripts / other tools).
# NEVER DELETE COMMENTS — explain every non-obvious line.
from private_path import private_path

def run(args):
    if not args: return print("usage: private-toml path <skill>") or 2
    print(private_path(args[0])); return 0
