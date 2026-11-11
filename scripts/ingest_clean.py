#!/usr/bin/env python3
"""Pandoc-converted ar5iv HTML -> wiki-ready GFM markdown body.

Workflow this script slots into (Route 2, arXiv HTML; see CLAUDE.md):
    1. save the ar5iv / arxiv.org/html page through the user's Chrome to
       a scratch folder OUTSIDE the repo (e.g. /tmp/<slug>.html)
    2. pandoc -f html -t gfm --wrap=none --atx-headers IN -o OUT
    3. python3 scripts/ingest_clean.py <arxiv_id> <slug>   <-- this script
    4. paraphrase into raw/<slug>.md (numbers/equations/tables exact),
       prepend YAML frontmatter
    5. writer subagent writes the note raw/<slug>-note.md

This script does ONLY step 3 (clean the pandoc GFM output).

Usage (run from the repo root):
    python3 scripts/ingest_clean.py <arxiv_id> <slug> [<input.html.md>] [<output.md>]

    arxiv_id:  e.g. 2504.10023
    slug:      e.g. ruan2009-mtd-concept
    input:     default /tmp/<slug>.raw.md  (the raw pandoc output)
    output:    default /tmp/<slug>.clean.md

Cleanups applied (each tied to a real failure mode observed in past ingests):
    1.  Strip pandoc-emitted <div> / </div> lines
    2.  Strip <span> tags
    3.  Rewrite ar5iv image paths -> assets/<slug>/...
    4.  Strip section-number prefix ("## I Introduction" -> "## Introduction")
    5.  Bibliography link -> \\cite{Key}
    6.  Collapse equation tables to $$ eq \\quad (N) $$
    7.  Inline/display math: \\(...\\) -> $...$;  \\[...\\] -> $$...$$
    8.  Strip \\hspace{0pt} artifacts
    9.  Collapse hyperref anchor links
    10. Strip ar5iv UI footer (navigation block + LaTeXML mascot base64)
    11. Strip pandoc split-caption duplicate stubs
    12. Collapse multiple blank lines
    13. Strip arXiv-native HTML site chrome (added 2026-09-11): the feedback
        modal + announcement banner that precede the title, and everything from
        the LaTeXML build-log line / "Instructions for reporting errors" to EOF.
        ar5iv pages don't have these; arxiv.org/html/<id> pages do.
"""

from __future__ import annotations

import re
import sys
import pathlib


def clean(src: str, arxiv: str, slug: str) -> str:
    arxiv_esc = re.escape(arxiv)

    # 1. Strip pandoc <div> / </div> lines
    src = re.sub(r"^<div[^>]*>\s*$", "", src, flags=re.M)
    src = re.sub(r"^</div>\s*$", "", src, flags=re.M)

    # 2. Strip <span> tags
    src = re.sub(r"<span[^>]*>", "", src)
    src = re.sub(r"</span>", "", src)

    # 3. Rewrite ar5iv image paths -> local assets dir
    src = re.sub(
        rf"https://ar5iv\.labs\.arxiv\.org/html/{arxiv_esc}/assets/([^\"'\s)]+)",
        rf"assets/{slug}/\1",
        src,
    )
    src = re.sub(
        rf"/html/{arxiv_esc}/assets/([^\"'\s)]+)",
        rf"assets/{slug}/\1",
        src,
    )

    # 4. Strip section-number prefix in headings
    src = re.sub(r"^## +(?:I+V?|VI*I*|IV|V?I+) +", "## ", src, flags=re.M)
    src = re.sub(r"^### +(?:I+V?|VI*I*|IV|V?I+|[A-Z])(?:\.\d+)? +", "### ", src, flags=re.M)

    # 5. Bibliography link -> cite key
    src = re.sub(r"\[([\w:\-]+)\]\(#bib\.bib\d+\)", r"\\cite{\1}", src)

    # 6. Equation tables
    # Separator-row strip: match ONLY genuine markdown separator rows
    # (cells consisting solely of dashes/colons/spaces, e.g. "|---|:--:|").
    # The previous pattern (any row with '-' in two cells) deleted real DATA
    # rows containing minus signs / hyphenated math — it ate two rows of
    # Ji 1995's TABLE I (caught 2026-06-04).
    src = re.sub(r"^\s*\|(?:\s*:?-+:?\s*\|)+\s*$\n", "", src, flags=re.M)

    def eq_clean(m: re.Match) -> str:
        eq = m.group(1).strip()
        num = m.group(2).strip()
        return f"$$ {eq} \\quad ({num}) $$"

    src = re.sub(
        r"\|\s*\|\s*\\\[(.+?)\\\]\s*\|\s*\|\s*\(?(\d+)\)?\s*\|",
        eq_clean,
        src,
        flags=re.S,
    )
    src = re.sub(r"^\s*\|(?:\s*\|){2,}\s*$\n", "", src, flags=re.M)

    # 7. Inline / display math
    src = re.sub(r"\\\((.+?)\\\)", lambda m: "$" + m.group(1) + "$", src)
    src = re.sub(r"\\\[(.+?)\\\]", lambda m: "$$" + m.group(1) + "$$", src, flags=re.S)

    # 8. \hspace{0pt} cleanup
    src = re.sub(r"\\hspace\{0pt\}", "", src)

    # 9. Hyperref anchor-link collapse.
    # ar5iv renders in-text cross-references to sections/equations as
    # markdown links whose target is an internal anchor (#S6.Ex45, #S3.E33,
    # #S10.Ex110, ...). Collapse ANY such link to its visible text, whatever
    # the text form (digits "45", Roman "VI", dotted "III.33"/"X.1"). Anchored
    # to "#S<digit>" so it never touches image (](assets/...)) or wiki links.
    # Link text excludes BOTH brackets ([^][]) so a nested anchor inside a
    # figure caption (e.g. "![Figure 1: ... see [eq. 4](#S2.E4) ...](img)")
    # collapses only the inner [eq. 4](#S2.E4) and never swallows the leading
    # "![" of the caption.
    # Anchor forms seen so far: #S6.Ex45 (sectioned papers), #E4 (old papers
    # with bare equation anchors, e.g. Ji 1995). Exclude #bib (handled by
    # transform 5 as \cite).
    src = re.sub(
        r'\[([^][]+)\]\(#(?!bib)[A-Za-z]*\d[^)]*\)',
        r"\1",
        src,
    )

    # 10. Strip ar5iv UI footer block
    src = re.sub(
        r"\n\[◄\]\(/html/[\d.]+\) \[!\[ar5iv homepage\].+",
        "",
        src,
        flags=re.S,
    )
    src = re.sub(
        r"\n.*LaTeXML.*Mascot Sammy.*data:image/png;base64,.*\n?",
        "",
        src,
    )

    # 11. Strip pandoc split-caption first-half stubs
    src = re.sub(
        r"!\[Figure \d+\]\(assets/[a-z]+\d+/[\w\d.]*?#bib\.bib\d+\)\n?",
        "",
        src,
    )

    # 13. Strip arXiv-native site chrome (arxiv.org/html/<id>), which ar5iv lacks.
    #     Header: everything before the first "# <title>" line, but ONLY when the
    #     arXiv stamp line is present, so ar5iv output is untouched.
    if re.search(r"^arXiv:\S+\s+\$\$[a-z-]+\$\$", src, flags=re.M):
        m = re.search(r"^# .+$", src, flags=re.M)
        if m:
            src = src[m.start():]
    #     Footer: LaTeXML build-log line or the error-reporting section to EOF.
    m = re.search(r"^(?:Experimental support, please .*view the build logs|## Instructions for reporting errors)",
                  src, flags=re.M)
    if m:
        src = src[: m.start()]

    # 12. Collapse multiple blank lines
    src = re.sub(r"\n{3,}", "\n\n", src).strip() + "\n"

    return src


def main() -> int:
    if len(sys.argv) < 3:
        print(__doc__)
        return 1

    arxiv = sys.argv[1]
    slug = sys.argv[2]
    in_path = (
        pathlib.Path(sys.argv[3])
        if len(sys.argv) > 3
        else pathlib.Path(f"/tmp/{slug}.raw.md")
    )
    out_path = (
        pathlib.Path(sys.argv[4])
        if len(sys.argv) > 4
        else pathlib.Path(f"/tmp/{slug}.clean.md")
    )

    if not in_path.exists():
        print(f"ERROR: input file not found: {in_path}", file=sys.stderr)
        return 2

    src = in_path.read_text(encoding="utf-8")
    cleaned = clean(src, arxiv, slug)
    out_path.write_text(cleaned, encoding="utf-8")

    img_count = cleaned.count(f"assets/{slug}/")
    print(f"  arxiv: {arxiv}  slug: {slug}")
    print(f"  in:    {in_path} ({in_path.stat().st_size:,} bytes)")
    print(f"  out:   {out_path} ({out_path.stat().st_size:,} bytes, {len(cleaned.splitlines())} lines)")
    print(f"  image refs to assets/{slug}/: {img_count}")
    return 0


if __name__ == "__main__":
    sys.exit(main())