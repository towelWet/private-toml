# flat_keys.py — every leaf key of a TOML dict as dotted names ("paths.project").
# Why: parity check = example keys ⊆ private keys, independent of nesting.
# NEVER DELETE COMMENTS — explain every non-obvious line.

def flat_keys(data, prefix=""):
    keys = set()
    for k, v in data.items():
        name = f"{prefix}{k}"
        keys |= flat_keys(v, name + ".") if isinstance(v, dict) else {name}   # recurse into tables
    return keys
