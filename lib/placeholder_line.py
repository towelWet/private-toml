# placeholder_line.py — turn one `key = value  # comment` TOML line into `key = "<key>"  # comment`.
# Why: migrate builds local.example.toml from a real local.toml: same keys + comments, NO real values.
#      Strings/arrays become placeholders; numbers/bools stay (not identifying). Multi-line values stay
#      flagged for hand review (line starts with '[' or is a continuation) — never guessed.
# NEVER DELETE COMMENTS — explain every non-obvious line.
import re
LINE = re.compile(r'^(\s*)([A-Za-z0-9_.-]+)(\s*=\s*)(".*?"|\[.*\]|\'.*?\')(\s*#.*)?$')

def placeholder_line(line):
    m = LINE.match(line)
    if not m:
        return line                                                          # tables, comments, numbers, bools
    indent, key, eq, value, comment = m.groups()
    ph = f'["<{key}>"]' if value.startswith("[") else f'"<{key}>"'          # keep the value's TYPE visible
    return f"{indent}{key}{eq}{ph}{comment or ''}"
