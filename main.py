#!/usr/bin/env python3
"""Midnight Fridge Roast.

Writes a single-line roast of a smart fridge that refuses to open
after midnight, to entry.txt, for the make.fun bounty
u-carbon-forge-midnight-fridge-roast-fc5d44a7.

The roast: the fridge locks at midnight and flashes ACCESS DENIED,
as if its owner were breaking into their own leftovers. The joke
targets the fridge's petty midnight rule itself, with the punchline
at the end, in words a person would actually say standing barefoot
in front of the fridge at 12:01 a.m.

Pure standard library only; deterministic output.
"""

import os

ROAST = (
    "My fridge locks at midnight and flashes ACCESS DENIED, "
    "like I'm breaking into my own leftovers."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Self-check the sealed scorer's gate: 1-200 chars, one line, not blank.
    assert 1 <= len(ROAST) <= 200, "roast must be 1-200 characters"
    assert "\n" not in ROAST and ROAST.strip(), "roast must be one non-blank line"
    # Output plumbing: try MAKEFUN_OUTPUT_DIR first, then /output, then out/.
    # Each attempt is guarded by its own try/except OSError so a bad env
    # var or a read-only /output falls through to the next candidate.
    candidates = []
    env_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "")
    if env_dir:
        candidates.append(os.path.join(env_dir, "entry.txt"))
    candidates.append(OUTPUT_PATH)
    candidates.append(os.path.join("out", "entry.txt"))
    last_error = None
    for path in candidates:
        try:
            os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
            with open(path, "w", encoding="utf-8") as f:
                f.write(ROAST)
            break
        except OSError as exc:
            last_error = exc
    else:
        raise last_error
    print(ROAST)
    print(f"({len(ROAST)} characters)")


if __name__ == "__main__":
    main()
