# scripts/

Utility scripts for the rhic_detectors wiki. Run them from the **repo root** (the folder holding `raw/` and `wiki/`), e.g. `python3 scripts/lint.py`.

## Conventions

- **Python 3 only** (no shell scripts in this directory; shell can call them)
- **stdlib only** — no `pip install` requirements
- **One concern per script** — no monolithic CLIs with subcommands
- **Top-of-file docstring** with usage example; the file should be self-documenting
- **Exit 0 = success, non-zero = something needs attention** (`lint.py` follows this)
- **Run from the repo root** — scripts assume `cwd` is the repo root so relative paths like `raw/`, `wiki/synthesis/` resolve correctly
- **No scratch output inside the repo** — temporary files go to `/tmp` or another folder outside it

## Environment

The ingest pipeline assumes a Linux environment with `pandoc` available (the Claude Cowork sandbox has `/usr/bin/pandoc` 2.9.2.1). The repo lives on OneDrive (Windows side); scripts read/write the OneDrive mount from the sandbox.

If running locally on Windows: `lint.py` works anywhere with Python 3; `ingest_clean.py` works anywhere with Python 3 *after* pandoc has produced the input file. The pandoc step itself needs either WSL or `winget install JohnMacFarlane.Pandoc`. The current convention is to drive ingests from the sandbox.

## Current scripts

| Script | Purpose | Usage |
|---|---|---|
| `lint.py` | No `[[wikilinks]]`, relative Markdown link resolution, image existence (skipped when the git-ignored `raw/assets/` is absent), raw frontmatter (presence, `type`, `source_type`, `captured_as`, `vision_model`), companion + full↔note pairing, `list.md` coverage, version metadata out of full sources, stale "not ingested" status, tail truncation — across `raw/*.md` and `wiki/` only | `python3 scripts/lint.py` |
| `ingest_clean.py` | Pandoc-converted ar5iv / arXiv HTML → wiki-ready GFM markdown body (Route 2). Strips ar5iv UI, fixes image paths, converts math, collapses equation tables, etc. The output is the input to the Layer 3 paraphrase, not the Layer 3 file itself | `python3 scripts/ingest_clean.py <arxiv_id> <slug> [<input.html.md>] [<output.md>]` |

## When to add a new script

A workflow you've done by hand 3+ times AND the inline version is ≥10 lines of Python ("automate anything done 3 times").

## When NOT to add a script

- One-off cleanups specific to a single source
- Tasks the model can do faster ad hoc
- Anything that needs human judgment per call

## Adding a script

1. Write it as `scripts/<name>.py`
2. Add a row to the table above
3. Test by running it from the repo root
4. Log the addition in `wiki/log.md` (type `tooling`)
