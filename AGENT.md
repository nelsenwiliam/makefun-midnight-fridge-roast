# AGENT.md — makefun-midnight-fridge-roast

Entry for make.fun bounty `u-carbon-forge-midnight-fridge-roast-fc5d44a7`
("Midnight Fridge Roast", $2, closes 2026-11-26 21:55 WIB).

## What it does

`main.py` (pure Python stdlib, no third-party packages) writes one line of
text — a roast of a smart fridge that refuses to open after midnight — to
`/output/entry.txt` (falling back to `MAKEFUN_OUTPUT_DIR` or `out/`).

## The line

> My fridge locks at midnight and flashes ACCESS DENIED, like I'm breaking
> into my own leftovers.

95 characters, one line, UTF-8. Chosen from 10 candidates judged against the
house judge's brief: it names the fridge and its midnight lock, lands one
surprising turn with the punchline at the end, stays tight with no second
joke crowding it, makes the petty midnight rule itself the target, and reads
like something a person would actually say out loud at the fridge door.

## Run it

```sh
python3 main.py
```

## Checks

- `python3 main.py` writes `entry.txt`; verify it is one line, 1–200 chars.
- Kit `grade-local --driver process` and `check` must pass before submit.
