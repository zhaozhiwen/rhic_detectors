#!/usr/bin/env python3
"""Lint check for the rhic_detectors LLM wiki (raw/ + wiki/ three-layer architecture).

Checks wikilink resolution, image existence, frontmatter validity
(presence, type, source_type, captured_as, vision_model), companion
fields, full<->note pairing, list.md coverage, version metadata kept out
of full sources, stale "not ingested" status, and tail truncation.
Inline-code spans and fenced code blocks are excluded from wikilink/image
checks.

Scans ONLY raw/*.md (not raw/assets/), wiki/synthesis/*.md and
wiki/index.md, list.md, log.md. Root files (README, CLAUDE, llm-wiki),
agents/, scripts/ and _to_delete/ are never scanned.

raw/assets/ (PDFs, figures) is git-ignored and exists only on the
maintainer's machine. If it is absent (e.g. a fresh clone of the public
repo), image refs into assets/ are skipped and counted, not reported.

Run from the repo root (the folder holding raw/ and wiki/):
    python3 scripts/lint.py

Exits 0 if clean, 1 if any issues found, 2 if not run from the repo root.
"""

from __future__ import annotations

import re
import sys
import pathlib
from collections import defaultdict


WIKILINK_RE = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]+)?(?:\|[^\]]+)?\]\]")
IMAGE_RE = re.compile(r"!\[[^\]]*\]\(([^)]+)\)")
INLINE_CODE_RE = re.compile(r"``[^`\n]+``|`[^`\n]+`")
FENCE_RE = re.compile(r"^```")

# Allowed values of the Layer 3 `source_type:` frontmatter field (CLAUDE.md,
# "Public repo and git"). Extend here and in CLAUDE.md together.
SOURCE_TYPES = {"paper", "email", "status-sheet", "talk-slides"}


def strip_code(text):
    """Drop inline-code spans and fenced code blocks."""
    out = []
    in_fence = False
    for line in text.split("\n"):
        if FENCE_RE.match(line):
            in_fence = not in_fence
            out.append("")
            continue
        if in_fence:
            out.append("")
            continue
        out.append(INLINE_CODE_RE.sub("", line))
    return "\n".join(out)


def collect_targets(root):
    raw = root / "raw"
    synth = root / "wiki/synthesis"
    wr = root / "wiki"
    files = list(raw.glob("*.md")) + list(synth.glob("*.md"))
    files += [wr / "index.md", wr / "list.md", wr / "log.md", wr / "CLAUDE.md"]
    return {f.stem: f for f in files if f.exists()}


def lint(root):
    raw = root / "raw"
    slug_set = collect_targets(root)
    issues = defaultdict(list)
    stats = {"files_checked": 0, "wikilinks": 0, "images": 0, "images_skipped": 0}
    # raw/assets/ is git-ignored (public repo): without it, asset image refs
    # cannot be checked, so skip them instead of reporting every figure.
    have_assets = (raw / "assets").is_dir()

    for f in sorted(slug_set.values()):
        stats["files_checked"] += 1
        content = f.read_text(encoding="utf-8")
        scanned = strip_code(content)

        for ln, line in enumerate(scanned.split("\n"), 1):
            for m in WIKILINK_RE.finditer(line):
                slug = m.group(1).strip()
                stats["wikilinks"] += 1
                if slug not in slug_set:
                    issues["unresolved_wikilink"].append(
                        f"{f.relative_to(root)}:{ln} [[{slug}]]"
                    )
            for m in IMAGE_RE.finditer(line):
                path = m.group(1).strip()
                if path.startswith("http") or path.startswith("data:"):
                    continue
                if not have_assets and "assets/" in path:
                    stats["images_skipped"] += 1
                    continue
                stats["images"] += 1
                if not (f.parent / path).resolve().exists():
                    issues["missing_image"].append(
                        f"{f.relative_to(root)}:{ln} {path}"
                    )

        if f.parent.name == "raw" and not content.startswith("---\n"):
            # Every raw file must open with YAML frontmatter (type, companion,
            # source_type, ...); without it none of the checks below can run.
            issues["missing_frontmatter"].append(str(f.relative_to(root)))
        if f.parent.name == "raw" and content.startswith("---\n"):
            end = content.find("\n---\n", 4)
            if end < 0:
                issues["malformed_frontmatter"].append(str(f.relative_to(root)))
                continue
            fm = content[4:end]
            type_m = re.search(r"^type:\s*(\S+)", fm, re.M)
            if not type_m:
                issues["missing_type_field"].append(str(f.relative_to(root)))
            elif type_m.group(1) == "raw-source":
                # Repo rules (2026-11-09): every full source declares what kind
                # of document it is and that it is a full-content paraphrase.
                st_m = re.search(r"^source_type:\s*(\S+)", fm, re.M)
                if not st_m:
                    issues["missing_source_type"].append(str(f.relative_to(root)))
                elif st_m.group(1).strip("\"'") not in SOURCE_TYPES:
                    issues["bad_source_type"].append(
                        f"{f.relative_to(root)}: source_type={st_m.group(1)}")
                if not re.search(r"^captured_as:\s*\S", fm, re.M):
                    issues["missing_captured_as"].append(str(f.relative_to(root)))
                # Record which model wrote the figure descriptions (added 2026-09-22,
                # after finding no record of it for any existing ingest). Enforced only
                # for sources captured on/after that date that contain figures.
                date_m = re.search(r"^captured_date:\s*(\d{4}-\d{2}-\d{2})", fm, re.M)
                if (date_m and date_m.group(1) >= "2026-09-22"
                        and IMAGE_RE.search(content)
                        and not re.search(r"^vision_model:\s*\S", fm, re.M)):
                    issues["missing_vision_model"].append(str(f.relative_to(root)))
            elif type_m.group(1) == "raw-note":
                comp_m = re.search(r"^companion:\s*(\S+)", fm, re.M)
                if not comp_m:
                    issues["note_missing_companion"].append(str(f.relative_to(root)))
                else:
                    comp = comp_m.group(1)
                    if comp != "none" and not (raw / comp).exists():
                        issues["note_bad_companion"].append(
                            f"{f.relative_to(root)}: companion={comp}"
                        )
                    elif comp != "none":
                        # Schema: the body must carry a real [[<slug>]] wikilink
                        # to the companion, not just a plain-text filename.
                        stem = comp[:-3] if comp.endswith(".md") else comp
                        if not re.search(r"\[\[" + re.escape(stem) + r"(\||\]\])", content):
                            issues["note_companion_not_wikilinked"].append(
                                str(f.relative_to(root)))

        # Tail-truncation heuristic (added 2026-06-04 after OneDrive sync
        # conflicts silently chopped file tails mid-word). A healthy md file
        # ends with punctuation / closing bracket / table pipe / math $.
        # Whitelist via a trailing "<!-- lint: tail-ok -->" comment for files
        # whose genuine last line trips the heuristic.
        nonblank = [l.rstrip() for l in content.splitlines() if l.strip()]
        if nonblank:
            last = nonblank[-1]
            if not last.endswith("<!-- lint: tail-ok -->") and re.search(
                r"[A-Za-z,(/—-]$", last
            ) and not last.endswith(("---", "```")):
                issues["suspicious_tail"].append(
                    f"{f.relative_to(root)}: ...{last[-50:]}"
                )

    raw_full = {f.stem for f in raw.glob("*.md") if not f.stem.endswith("-note")}
    raw_note = {f.stem.removesuffix("-note") for f in raw.glob("*.md") if f.stem.endswith("-note")}
    for s in sorted(raw_full - raw_note):
        issues["full_without_note"].append(s)
    orphan = sorted(raw_note - raw_full)
    for slug in list(orphan):
        nf = raw / f"{slug}-note.md"
        if nf.exists() and "companion: none" in nf.read_text(encoding="utf-8"):
            orphan.remove(slug)
    for s in orphan:
        issues["note_without_full"].append(s)

    # Every raw source must be catalogued in wiki/list.md (as a [[slug]] wikilink,
    # the "Full source" column convention) -- added 2026-09-21 after an ingest found
    # the raw-sources table silently missing rows for 5 already-ingested papers
    # despite log.md recording that each ingest updated it. lint.py's wikilink check
    # only validates links that exist, not links that are absent, so this drift went
    # undetected across several sessions. Originally the table lived in wiki/index.md;
    # moved to its own wiki/list.md (2026-09-21) to keep index.md as the thematic
    # reading path and list.md as the flat raw-sources inventory.
    list_md = root / "wiki" / "list.md"
    if list_md.exists():
        list_content = list_md.read_text(encoding="utf-8")
        for s in sorted(raw_full):
            if f"[[{s}]]" not in list_content:
                issues["raw_source_missing_from_list"].append(s)

    # Version-chain / ingest-status checks (added 2026-09-23, user rule): status
    # metadata that goes stale (earlier_version / later_version, "not yet
    # ingested") belongs in the note (Layer 2), never in the immutable full
    # source; and after every ingest, notes and synthesis must not still call
    # an ingested source "not ingested". Always on in this repo.
    stale_re = re.compile(r"not (yet )?ingested|being ingested", re.I)
    for f in sorted(raw.glob("*.md")):
        if f.stem.endswith("-note"):
            continue
        c = f.read_text(encoding="utf-8")
        if c.startswith("---\n"):
            e = c.find("\n---\n", 4)
            if e > 0 and re.search(r"^(earlier|later)_version:", c[4:e], re.M):
                issues["version_metadata_in_full_source"].append(str(f.relative_to(root)))
    targets = sorted(raw.glob("*-note.md")) + sorted((root / "wiki" / "synthesis").glob("*.md"))
    for f in targets:
        for ln, line in enumerate(f.read_text(encoding="utf-8").split("\n"), 1):
            if not stale_re.search(line) or re.search(r"previously", line, re.I):
                continue
            # flag only when an ingested slug is mentioned within 80 characters of
            # the status phrase (a phrase about some other, external document on the
            # same line is fine); silence a deliberate case with <!-- lint: status-ok -->
            if "lint: status-ok" in line:
                continue
            hits = [m.start() for m in stale_re.finditer(line)]
            for s in raw_full:
                pos = [m.start() for m in re.finditer(rf"(?<![\w-]){re.escape(s)}(?:-note)?(?![\w-])", line)]
                if any(abs(p - h) <= 80 + len(s) for p in pos for h in hits):
                    issues["stale_ingest_status"].append(f"{f.relative_to(root)}:{ln} mentions {s}")
                    break

    return issues, stats


def main():
    root = pathlib.Path(".")
    if not (root / "raw").exists() or not (root / "wiki").exists():
        print("ERROR: run from the rhic_detectors repo root (need raw/ and wiki/ subdirs): python3 scripts/lint.py", file=sys.stderr)
        return 2

    raw_full_count = sum(1 for f in (root / "raw").glob("*.md") if not f.stem.endswith("-note"))
    issues, stats = lint(root)

    print(f"=== LINT REPORT - {pathlib.Path('.').resolve().name} ===")
    print()
    print(f"Files checked:    {stats['files_checked']}")
    print(f"Wikilinks total:  {stats['wikilinks']}")
    print(f"Image refs total: {stats['images']}")
    if stats["images_skipped"]:
        print(f"Image refs skipped: {stats['images_skipped']} (raw/assets/ absent: git-ignored, local only)")
    print(f"Raw paper pairs:  {raw_full_count} full files (excluding -note suffix)")
    print()

    total = sum(len(v) for v in issues.values())
    if total == 0:
        print("CLEAN. No issues found.")
        return 0

    print(f"ISSUES: {total}")
    for cat in [
        "unresolved_wikilink", "missing_image", "missing_frontmatter", "malformed_frontmatter",
        "missing_type_field", "missing_source_type", "bad_source_type", "missing_captured_as",
        "note_missing_companion", "note_bad_companion",
        "note_companion_not_wikilinked",
        "full_without_note", "note_without_full", "raw_source_missing_from_list",
        "missing_vision_model", "version_metadata_in_full_source", "stale_ingest_status",
        "suspicious_tail",
    ]:
        if issues[cat]:
            print()
            print(f"[{cat}] {len(issues[cat])}")
            for x in issues[cat][:20]:
                print(f"  {x}")
            if len(issues[cat]) > 20:
                print(f"  ... ({len(issues[cat]) - 20} more)")
    return 1


if __name__ == "__main__":
    sys.exit(main())
