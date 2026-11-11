# rhic_detectors — Schema

Read this file at the start of every session in this repo. It is the single rule set for this wiki (adapted from the user's wiki_paper schema; this repo is self-contained and depends on nothing outside it).

## Purpose and scope

An LLM-maintained Obsidian knowledge base for a literature study of RHIC detectors: so far the STAR barrel time-of-flight (BTOF), Muon Telescope Detector (MTD), Barrel and Endcap Electromagnetic Calorimeters (BEMC, EEMC), Forward Calorimeter System (FCS), DAQ/trigger, and the magnet / return-iron absorber. **Scope = the detectors listed on the SoLID wiki page [RHIC detectors](https://solid.jlab.org/wiki/index.php?title=RHIC_detectors).** Listed entries not yet covered are ingest candidates; track them in `wiki/synthesis/open-questions.md`. Reading notes and syntheses only; SoLID simulation or reuse assessment is out of scope unless the user asks. Domain: experimental nuclear/particle-physics instrumentation.

The repo is **public** on GitHub as `zhaozhiwen/rhic_detectors`, pushed by the user. Everything committed is world-readable: see "Public repo and git".

## Three-layer architecture

```
wiki/                         ← navigation only: index.md, list.md, log.md
  └─ synthesis/<topic>.md     ← Layer 1: thematic pages (detectors, systems, technologies, status)
                │  links down to raw/<slug>-note.md
                ▼
raw/<slug>-note.md            ← Layer 2: per-source curated note (bridge)
                │  companion: <slug>.md + a link to it in the body
                ▼
raw/<slug>.md                 ← Layer 3: full-content paraphrase of the source
```

**Layer 1 — `wiki/synthesis/`.** Cross-cutting pages, each drawing on several sources. No per-source pages (a source's own write-up is its note). The `wiki/` root holds only `index.md`, `list.md`, `log.md`. Multi-source composites with no single companion may be named `<topic>-synthesis.md` with frontmatter `type: synthesis` and `compiled_from:`.

**Layer 2 — `raw/<slug>-note.md`.** Frontmatter `type: raw-note`, `companion: <slug>.md` (or `companion: none` for note-only sources), `source_type:` (same value as the companion), and **links for readers**: `doi:` and/or `arxiv:` and `journal:` (venue, volume, pages, year) for papers, `url:` for anything else with a public address. PDFs and figures are not in the repo, so these links are how a GitHub reader reaches the original. Body: "Companion notes to [<slug>](<slug>.md) (full source).", bibliography, the abstract **paraphrased** (never verbatim — public repo), key numbers, motivations, method, caveats, the SoLID angle, and a "Related" block at the bottom (`[<topic>](../wiki/synthesis/<topic>.md)` up, `[<other-slug>-note](<other-slug>-note.md)` across). The note **holds all metadata that can go stale**: `earlier_version:` / `later_version:` (each `<slug> (<what/when>) -- ingested` or `-- not ingested`), `version_facts:`, `versions_checked: <date>`. Update these in every note that names a newly ingested source.

**Layer 3 — `raw/<slug>.md`: full-content paraphrase** (user decision, 2026-11-09; applies to every source and every new ingest). Every section of the source, in order; **every number, unit, equation, table cell and reference reproduced exactly**; prose and figure captions paraphrased in our own words. It is NOT a verbatim transcription. Frontmatter `type: raw-source`, `captured_as: full-content paraphrase`, `source_type: paper | email | status-sheet | talk-slides`, `captured_via:` (route + evidence), `captured_date:`, `figures:`, `vision_model:`, plus `doi:`/`arxiv:`/`url:`. Equations keep the source's own numbers as `\tag{N}`. Our additions are tagged **[note]**, suspected errors in the source **[source issue]** (state what is printed and what is meant; never silently correct). Short quotations only where the exact wording matters (e.g. a "first" claim), in quote marks. Immutable once written: it carries only capture-time facts — never `earlier_version`/`later_version` or "not ingested"/"later version exists" status (lint `version_metadata_in_full_source`).

**Linking rules.** All cross-references are **relative Markdown links** with the slug as link text, e.g. `[star-mtd](../wiki/synthesis/star-mtd.md)` from a file in `raw/` — never Obsidian `[[wikilinks]]`, which GitHub shows as plain text (user decision, 2026-11-11; lint `wikilink_syntax`, `unresolved_link`). Paths are relative to the linking file: from `raw/` → `../wiki/synthesis/<page>.md`, `<slug>-note.md`; from `wiki/synthesis/` → `../../raw/<slug>-note.md`, `<page>.md`; from `wiki/` → `synthesis/<page>.md`, `../raw/<slug>.md`. Never put links in YAML frontmatter. Thematic pages link down to `<slug>-note.md`. Notes link up to thematic pages and down to the companion `<slug>.md` (lint `note_companion_not_linked`). Notes cite other sources via `<other-slug>-note.md`, never `<other-slug>.md`. Full sources are leaves (no links to other wiki pages). In Obsidian set Settings → Files & Links: "Use [[Wikilinks]]" off, "New link format" = relative path.

**Citing the user.** Facts the user states in chat (e.g. tray dimensions he knows from the hardware) are cited as "Zhiwen, personal communication, <YYYY-MM-DD>" — on the synthesis page where used, and in the log entry. They are never presented as coming from a paper.

## Directory layout

Repo root = wiki root = Obsidian vault (also browsable on GitHub: all links are relative Markdown links).

```
rhic_detectors/
├── README.md              GitHub overview
├── CLAUDE.md              this schema
├── llm-wiki.md            Karpathy's LLM-wiki pattern
├── .gitignore  .gitattributes
├── agents/                master copies of subagent definitions (wiki-fetch.md, wiki-vision.md)
├── scripts/               lint.py, ingest_clean.py, CLAUDE.md (usage)
├── raw/
│   ├── <slug>.md          Layer 3
│   ├── <slug>-note.md     Layer 2
│   └── assets/<slug>/     source.pdf, figN.png, originals (.docx, slides) — LOCAL ONLY, git-ignored
├── wiki/
│   ├── index.md  list.md  log.md
│   └── synthesis/*.md     Layer 1 (flat, no subfolders)
└── _to_delete/            quarantine for files to be removed (git-ignored; the user deletes it)
```

- `wiki/index.md` — thematic reading path: `wiki/synthesis/` pages grouped by page type. Does not list raw sources.
- `wiki/list.md` — flat inventory of every raw source (format below); lint requires every `raw/<slug>.md` to be linked there (`raw_source_missing_from_list`).
- `wiki/log.md` — append-only session log.
- Nothing else at the root without asking the user. Scratch files (page renders, contact sheets, OCR output, HTML dumps, converted drafts) live **outside the repo** (cloud container scratch / `/tmp`, or device `$HOME` outside `mnt/`), never in `raw/` or `raw/assets/`.

## Tooling

Scripts run from the repo root: `python3 scripts/lint.py`, `python3 scripts/ingest_clean.py …`. See [scripts/CLAUDE.md](scripts/CLAUDE.md). `pandoc`, `pdftotext`, `pdfimages`, `pdffonts` are available in the Cowork Linux sandbox; ingests are driven from there.

## Public repo and git

- **Not published: paper PDFs and figure images** (user decision, 2026-11-09). `raw/assets/` and `*.pdf` are git-ignored and stay on the user's machine. Figure embeds `![…](assets/<slug>/figN.png)` render in local Obsidian; on GitHub they show as broken images — expected; readers follow the DOI/arXiv links in the note. Never move a figure or PDF out of `raw/assets/` to get it rendered on GitHub.
- **Copyright:** Layer 3 is a paraphrase, the Layer 2 abstract is paraphrased; numbers, equations, tables and references are facts and are kept exact.
- **Non-paper sources are published** (user decision): an email from a STAR collaborator, an internal STAR detector-status sheet, internal STAR talk slides. Record `source_type:` (`email | status-sheet | talk-slides | paper`) in both the Layer 3 and the Layer 2 frontmatter. The originals (.docx, slide PDF, sheet PDF) stay in `raw/assets/<slug>/`, local only. Do not copy personal contact details (email addresses, phone numbers) out of emails or internal documents; ask the user before publishing anything an internal source marks as restricted.
- **arXiv copies are not kept where a publisher version exists** (user decision): no arXiv PDF or arXiv-based full text in `raw/assets/` once the publisher version is captured; the arXiv id is still recorded as a link in the note.
- **The user runs git himself, from native Windows.** Claude never runs `git commit/push/pull/rebase/reset/checkout`, never changes remotes or repo visibility, and leaves changes uncommitted, telling the user what changed. (The Cowork device shell cannot `unlink`, so git there litters `tmp_obj_*` / `.lock` files and aborts.)

## Concurrency & data safety

- Never let two sessions or agents write the same file at once: OneDrive sync conflicts silently truncate file tails (files end mid-word). Parallel agents get disjoint file lists. Lint's `suspicious_tail` catches truncation — run it after every write batch; whitelist a genuine case with a trailing `<!-- lint: tail-ok -->`.
- The device shell and the Windows-side file tools can see different states of this OneDrive folder. Write each file through ONE interface per task. Edit in place (python read-modify-write or `sed -i`), never by re-typing a file from tool output, which can be truncated. After committing a file from the cloud container to the device, md5-compare the device copy with the intended one; to re-commit an edited file, commit it under a new staged file name (a re-used `stagedPath` can resend the earlier upload).
- **Never delete.** Move unwanted files to `_to_delete/` and tell the user. A file that refuses to move ("Permission denied" while siblings work) is usually held open by another program: leave it, note it in the log, move on.

## raw/ file types and naming

1. `<slug>.md` — Layer 3 full-content paraphrase (`type: raw-source`).
2. `<slug>-note.md` — Layer 2 note (`type: raw-note`). If only an abstract or stub is available, write only the note (`companion: none`) and leave `<slug>.md` absent until the full source is captured. Never mix the two roles in one file. Very long reviews and tertiary sources (web pages, Wikipedia) usually stay note-only.
3. Multi-source composites go in `wiki/synthesis/`, not `raw/`.

**Slugs** — lowercase, hyphen-separated, no spaces:
- Papers: `<firstauthor><year>-<topic>`, year = publication year of the captured (journal) version. E.g. `wu2007-star-barrel-tof`, `beddo2003-bemc`, `huang2016-mtd-muon-id`.
- **Collaboration-name rule:** when the author list is fully alphabetical (the first author is arbitrary), use the collaboration: `<collaboration><year>-<topic>`, e.g. `star2003-eemc` (STAR EEMC NIM paper, alphabetical list). When named lead authors precede an alphabetical block, keep the first author. Check the actual author list; record first author and collaboration in frontmatter `authors:` either way.
- Non-papers: talk slides `<speaker><year>-<topic>-talk` (`gagliardi2022-star-forward-upgrade-talk`); emails `<sender><year>-<topic>-email` (`ruan2026-fcs-specs-email`); documents with no named author use the issuing body: `<org><year>-<topic>` (`star2026-detector-status`). Proposals / TDRs: `<collaboration-or-id><year>-<topic>-<proposal|tdr>`.
- **Detector tags:** the topic part names the detector with a fixed tag so files sort and grep by subsystem: `barrel-tof` / `tof`, `mtd`, `bemc`, `eemc`, `fcs`, `mrpc`, `forward-upgrade`, `daq`, `trigger`, `magnet`, `detector-status`; add new tags (e.g. `epd`, `vpd`, `etof`, `sphenix-…`) when a new subsystem enters scope and list them here. Prefix `star-` where the topic would otherwise be ambiguous.

## Reading a source — which route

**Network reality (this folder, 2026-11):** the user's Chrome via the `claude-in-chrome` tools is the **only** route to publishers (it carries the JLab institutional access). The cloud container and the device shell have no network to arXiv, doi.org or publishers; WebFetch/WebSearch are good for metadata checks at most. Never use the built-in browser pane for ingests. For a fresh tab: `tabs_context_mcp{createIfEmpty:true}`; never reuse the user's own tabs; close yours when done.

Try routes in order 1 → 2 → 3. Record the route actually taken in `captured_via:` and in the log entry. **On any problem, ask the user** — never silently work around it or fall back to the next route. CAPTCHAs and other human-only gates: ask the user to clear them in his Chrome, then continue in a new tab (the cookies carry over); note it in the frontmatter and log.

- **Route 1 — publisher HTML (try first).** Open the article's full-text HTML in the user's Chrome, save the figures at full resolution, extract text and math from the DOM (MathJax `script[type="math/tex"]`, MathML `<math>`, or rendered unicode — varies by publisher; verify large transfers with a SHA-256 hash), write the Layer 3 paraphrase with figures embedded, then download the PDF as backup and **take every formula and table from the PDF** where the HTML is lossy (below). Pay special attention to math:
  - Check `window.MathJax.version`. **MathJax v4 lazy pages:** call `window.MathJax.startup.document.lazyTypesetAll()`; on a large page fire it **once, bare, without `await`, in its own tool call**, and poll the rendered count in a later call (awaiting or looping it can stall or hang the tab; recover with a full `navigate()` reload — not `location.reload()` — then reinstall extraction helpers). If that stalls, an incremental scroll sweep (~0.8 viewport steps, `lazyTypesetAll()` at each step).
  - **MathJax v3** (no `lazyTypesetAll`): `resize_window` to a very tall viewport (~9999 px), then a few fractional-scroll passes; reset the viewport afterwards. Holdouts are often hidden nav-menu duplicates, not content.
- **Route 2 — arXiv HTML (fallback; only if no publisher HTML).** ar5iv, or arXiv-native `/html/<id>`; same steps as Route 1. Techniques: replace each LaTeXML `<math>` by a placeholder holding its `<annotation encoding="application/x-tex">` TeX before pandoc and restore after (pandoc's MathML parsing injects "OPEN"/"CLOSE" text and escapes `$`); convert `<object data="X.svg">` to `<img>` (pandoc drops `<object>`) and rasterize SVGs; a `<figure>` may hold several panels — use `re.findall`, and compare distinct image basenames with the number downloaded; inside pipe tables write `\lvert`/`\rvert` instead of `|`; strip nested `<span>` tags open/close independently. If a publisher version exists, the arXiv copy is used only to read from — it is not kept (see Public repo).
- **Route 3 — PDF (last resort, only with the user's OK).** A transcription subagent reads the PDF pages (vision) and writes the paraphrase; the main side cross-checks it against the text layer. **Check the text layer first:** `pdffonts` showing `Type 3` fonts with `uni: no` means extractors return garbage → build an OCR layer (`ocrmypdf --force-ocr -l eng --sidecar source_ocr.txt …`, kept outside the repo). Symbol-font glyphs (Ξ, Λ, Ω, √, ±) are often dropped by `pdftotext`: the rendered page decides.

**Lessons learned in this folder (2026-11):**
- **ScienceDirect may serve only the abstract + PDF** (no HTML body) for older and proceedings articles → Route 1 is unavailable; ask, then Route 2 (if an arXiv HTML exists) or Route 3.
- **ScienceDirect HTML can drop `√` signs and table cells** → on every ScienceDirect Route 1 ingest, take formulas and tables from the PDF and say so in `captured_via`.
- ScienceDirect "View PDF" is a redirect page: `navigate()` the tab to it, let it resolve to `pdf.sciencedirectassets.com/…` (signed, ~5 min), then fetch+blob from that tab. **Chrome blocks repeated scripted downloads from `pdf.sciencedirectassets.com`** → stop; the user saves the PDF by hand; copy (do not move) it from Downloads into `raw/assets/<slug>/source.pdf`.
- **IOP (J. Phys. G, J. Phys. Conf. Ser.) and EPJ Web of Conferences proceedings usually have no HTML full text** (only abstract + PDF) → Route 3 after asking.
- **Talk slides are Route 3 with every slide viewed** as a rendered image (not just the text layer): slide plots, tables and annotations carry content the text layer lacks; one section per slide (`### Slide N — <title>`).
- **Emails / .docx:** convert the text (pandoc or python-docx); tab-aligned blocks become tables; check arithmetic in a **[note]** section; the original file goes to `raw/assets/<slug>/`.
- **Number check:** after writing Layer 3 from a PDF source, run a script that pulls every number from the body and looks it up in the PDF text layer; inspect each miss against the page image.
- Keep scratch renders outside the repo.

**Downloads (all routes):** only via `fetch(url).then(r=>r.blob())` + `URL.createObjectURL` + a programmatic `<a download>` click — never a native Save-As dialog (it blocks the user's computer). Files land in the user's Downloads folder; reconcile them promptly by byte size against the returned `blob.size` (temporary `.tmp` names can be garbage-collected after ~45 min), copy them into `raw/assets/<slug>/`, and list leftovers for the user (never delete them).

**Vision pass on every figure is the DEFAULT, on all routes** (skip only if the user asks for a captions-only ingest; then `figures: <N> (captions-only, vision pass deferred by user request)` and nothing in the note may be read off a figure). A separate vision subagent reads each image, checks it against its caption (publisher endpoints have served swapped figures), and writes a description block (plot type, axes with units and lin/log, key features, takeaway) below the figure line in `raw/<slug>.md`; the main agent then reads the finished file. Record `vision_model: <model> (<agent type>, effort <level>), <YYYY-MM-DD>` in the Layer 3 frontmatter and the log (lint `missing_vision_model`). Finally the PDF is kept as local backup in `raw/assets/<slug>/source.pdf`.

**Figures from a PDF:** never crop by guessed pixel coordinates. Embedded rasters with labels inside → `pdfimages -png`. Vector plots → bbox from PyMuPDF drawing/image rects paired with the caption position, render from a Ghostscript 300-DPI page render (`gs -r300 -sDEVICE=png16m -dGraphicsAlphaBits=4 -dTextAlphaBits=4`; PyMuPDF/poppler draw hairlines pale), check text bleed **by position** against `page.get_text("blocks")`, check every panel is inside the crop, then one contact sheet of crops beside their pages. Re-crop only flagged figures; if a heuristic change re-runs a whole document, diff every crop against the previous run.

**PDF page links:** in notes and synthesis, page references may link to the local PDF page — `p. [55](assets/<slug>/source.pdf#page=55)` from `raw/`, `../../raw/assets/<slug>/source.pdf#page=55` from `wiki/synthesis/` (opens at the page in Obsidian; dead on GitHub, so always also give the page number in text).

## Wiki page conventions

Every page in `wiki/` has YAML frontmatter:

```yaml
---
title: <page title>
tags: [<one or more of the vocabulary below>]
sources: [raw/ filenames this page draws from, e.g. wu2007-star-barrel-tof-note.md]
updated: YYYY-MM-DD
---
```

**Tag vocabulary:** shared `experiment`, `theory`, `measurement`, `overview`; domain tags `detector`, `status`, `technology`. Add a new tag only with the user's OK and list it here.

Pages are dense and LLM-readable — no filler. Every number carries its source (a link to `<slug>-note.md`, section or page); where sources disagree, give both values with sources and say which supersedes which (or that it is unresolved). Relative Markdown links for cross-references (see Linking rules); an entity or concept mentioned on several pages gets its own page.

## Page types

- **Overview** — high-level map of a topic (e.g. the STAR detector layout).
- **Detector** — one per detector subsystem (`star-barrel-tof`, `star-mtd`, `star-bemc`, `star-eemc`, `star-fcs`). Suggested sections: role and coverage; geometry and construction; technology; readout and electronics; performance (resolution, efficiency, calibration — numbers with sources); current status; discrepancies between sources; open questions.
- **System** — shared infrastructure serving several detectors (`star-daq-trigger`, `star-magnet-absorber`).
- **Technology** — a technique across detectors (`mrpc-technology`, `pi-mu-separation-calorimetry`).
- **Status** — present state of hardware (in situ / removed / shipped, channels live) (`rhic-detector-status`); dated, with the source of each claim.
- **Measurement** — a specific performance dataset (beam test, cosmic test, in-run calibration) with numbers, uncertainties and conditions.
- **Entity** — collaborations, facilities, people — only when referenced from several pages.
- `open-questions.md` — the tracker: unresolved discrepancies, facts no ingested source states, and uncovered SoLID-wiki entries, each with the next source to check.

## index.md format

Grouped by page type. Each entry: `- [page](synthesis/page.md) — one-line summary (N sources)`. Read `index.md` first on every query.

## list.md format

One `## Raw sources` table, one row per `raw/<slug>.md`, added on every ingest:

```
| Slug | Full source | Note | Route | Ingested |
|---|---|---|---|---|
| <slug> | [<slug>](../raw/<slug>.md) — Authors, *Title*, venue (or: email / talk slides / status sheet) | [<slug>-note](../raw/<slug>-note.md) | Route N (short reason) | YYYY-MM-DD |
```

Keep the Route cell short; the forensic detail belongs in `captured_via` and the log.

## log.md format

Each entry starts `## [YYYY-MM-DD] <type> | <title>`; types `ingest`, `query`, `lint`, `tooling`, `assets`, `schema`. List files added/updated, the route, the vision model, user decisions and any personal-communication facts.

```
## [2026-11-09] ingest | Beddo et al. 2003, STAR BEMC
- Added: raw/beddo2003-bemc.md, raw/beddo2003-bemc-note.md
- Updated: wiki/synthesis/star-bemc.md, wiki/list.md, wiki/index.md
```

## Ingest workflow

### Agent roles

The main session **decides and reviews**; subagents do the bulk work (bulky page text stays out of the main context, and the wiki files — not the chat — carry the context a writer needs).

| Agent | Model | Does |
|---|---|---|
| Main session | the user's selection (usually Opus) | duplicate/scope check against the SoLID wiki list, route decision, all questions to the user, review of each subagent's report and diffs, spot-check of at least one number per changed page against the source |
| Fetch | `subagent_type: wiki-fetch` (Sonnet, effort medium) | browser driving in the user's Chrome, text/math extraction, pandoc + cleanup, figure/PDF/HTML downloads, figure crops, staging/committing assets; returns paths + short report |
| Vision | `subagent_type: wiki-vision` (Opus, effort high) | figure data-integrity check + descriptions |
| Transcription (Route 3) | `general-purpose`, `model: opus`, one per ~20-page chunk | reads PDF pages / slides and writes the Layer 3 paraphrase (sections, every number/equation/table exact, captions, references) |
| Writer | `general-purpose`, `model: opus` | verifies the fetch/transcription output (equation tags, figure/image count, references, number check vs text layer, no leftover HTML/placeholders), then writes the note, synthesis updates, cross-references, `list`/`index`/`log`, runs lint, reports changed files |

**Agent definitions** live in `agents/` (`wiki-fetch.md`, `wiki-vision.md`) and carry model, effort and standing rules. At the start of an ingest session check that `~/.claude/agents/` has both; if not, copy them there and tell the user a session restart is needed; until then use `general-purpose` with the same `model:` and paste the definition's rules into the brief. Edit the copies in `agents/`, not the installed ones.

Rules: the fetch agent **never works around a problem** — it cannot ask the user, so it stops and reports (no publisher HTML, paywall, CAPTCHA, download block, truncation, count mismatch, stalled browser after one fresh-tab retry). Every fetch brief states the browser rules (user's Chrome only; fetch+Blob downloads; close all tabs and reopen once on an extension stall). Verification is independent of production: the writer, not the producer, checks the output before building on it; the main session then reviews.

### Route 2 pipeline (from the repo root; scratch outside the repo)

```
# HTML saved through the user's Chrome → $SCRATCH/<slug>.html ; figures → raw/assets/<slug>/
sandbox$ pandoc -f html -t gfm --wrap=none --atx-headers $SCRATCH/<slug>.html -o $SCRATCH/<slug>.raw.md
sandbox$ python3 scripts/ingest_clean.py <arxiv_id> <slug> $SCRATCH/<slug>.raw.md $SCRATCH/<slug>.clean.md
# paraphrase into raw/<slug>.md (numbers/equations/tables exact), prepend frontmatter
# >>> vision subagent on every figure (required) <<<
# writer subagent: note, synthesis, list/index/log
sandbox$ python3 scripts/lint.py
```

Route 1 has no fixed pipeline (publisher markup varies); same vision, verification and lint requirements.

### Route 3 in practice

1. Confirm there is no HTML (publisher, arXiv) and get the user's OK.
2. Fetch: PDF through the user's Chrome; `pdfinfo` / `pdffonts` to judge the text layer; figures by the PDF-figure method above; OCR layer if the text layer is unusable.
3. Page map (sections, figures, tables, references → PDF pages) before transcription, so chunks and any user-approved skips are exact.
4. Chunked transcription in parallel (~20 pages per Opus subagent), one shared rules brief: full-content paraphrase, `<!-- p. N -->` page markers, source equation numbers as `\tag{N}`, pipe tables, figure image + paraphrased caption, `[UNCERTAIN: …]`, **[source issue]**.
5. Mechanical join check: equation tags continuous, every figure/table/reference number present, a page marker for every page.
6. Vision pass in batches of ~10 with the captions; re-crop anything flagged as cut or bled, then re-describe.
7. Writer verifies (number check against the text layer, tables against page images), then writes note, synthesis, list/index/log, lint.
8. Main-session review: diffs plus one number per changed page against the page image.

User-approved skips of long low-value appendices are fine if listed by caption with page references and stated in the frontmatter.

### After the source is in (checklist, no exceptions)

1. `wiki/list.md` row; `wiki/index.md` if a page or its source count changes.
2. Update every affected synthesis page: add what the source contributes and revise every line it makes stale (open questions, superseded numbers, comparison tables, status).
3. Cross-references in the most-affected sibling notes; version-chain fields of every note naming the new source.
4. Staleness sweep: `grep -rn -i "not yet ingested\|not ingested\|being ingested" raw/*-note.md wiki/synthesis/` and fix every hit about a source now in `raw/` (lint `stale_ingest_status`; a line about a genuinely external document may carry `<!-- lint: status-ok -->`).
5. `wiki/synthesis/open-questions.md`: close what the source answers, add what it raises.
6. Append the `wiki/log.md` entry.
7. `python3 scripts/lint.py` — must be CLEAN.

A source may touch 5–15 pages. Prefer updating pages over creating new ones. When new data contradicts an existing claim, update the page and state the contradiction and which source supersedes which.

## Query workflow

1. Read `wiki/index.md`; 2. read the relevant pages; 3. answer with citations to wiki pages and notes; 4. if the answer is substantial and reusable, offer to file it as a synthesis page (follow-up Q&A that is not about one source belongs in a synthesis page, with sources).

## Drafting workflow (talks, proposals, papers citing this literature)

- Numbers and claims in a draft trace to **Layer 3 only** (`raw/<slug>.md`: the source's own numbers, tables, equations). Notes, synthesis pages and figure **Description** blocks are LLM interpretation: use them to find things, never to cite. Because Layer 3 prose is paraphrased, check any wording-sensitive claim against the original PDF.
- Figure-derived numbers are second-class: verify on the image in `raw/assets/<slug>/` and state them approximately, or leave them out.
- "First"/priority claims only in the source's own words.
- Sources without a Layer 3 file are unverified: list them for external checking.
- Before circulating a draft, run a source-trace pass (each number/claim → text-supported / table-supported / figure-verified / personal communication / not locally verifiable / contradicted) and save it next to the draft. Drafts live outside this repo.

## Lint workflow

**Structural lint** (run first, must pass): `python3 scripts/lint.py` from the repo root. Scans `raw/*.md`, `wiki/synthesis/*.md`, `wiki/index.md`, `wiki/list.md`, `wiki/log.md` only (not the root files, `agents/`, `scripts/` or `_to_delete/`). Checks: no `[[wikilinks]]`, relative Markdown link resolution, image existence (skipped for `assets/` paths when `raw/assets/` is absent, e.g. a fresh GitHub clone), raw frontmatter presence and `type:`, `source_type:` and `captured_as:` on Layer 3, `vision_model`, note companion fields and companion link, full↔note pairing, `list.md` coverage, version metadata out of Layer 3, stale "not ingested" status, tail truncation. Exit 0 = clean.

**Full review** (user preference): ask first; then two independent subagents, told that whoever finds the most serious issues wins; merge their findings, deduplicated and verified, into one report.

**Manual semantic lint:** contradictions between pages; superseded claims (e.g. prototype vs as-built numbers, design vs current status); orphan pages; concepts lacking a page; missing cross-references; data gaps; anachronistic terminology; verbatim passages that slipped into Layer 3 or a note abstract (public repo); personal-communication facts presented as paper facts.
