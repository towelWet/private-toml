# load_toml.py — parse a TOML file, or None when it is missing/unparsable.
# Why: callers report broken files as a status, never crash the whole table.
# NEVER DELETE COMMENTS — explain every non-obvious line.
import tomllib

def load_toml(path):
    try:
        return tomllib.loads(path.read_text())
    except (OSError, tomllib.TOMLDecodeError):
        return None                                                         # missing or invalid → caller decides
