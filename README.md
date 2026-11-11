# rhic_detectors

A literature study of detectors at RHIC (Brookhaven National Laboratory), kept as an LLM-maintained [Obsidian](https://obsidian.md) wiki. So far it covers the STAR barrel time-of-flight (BTOF), Muon Telescope Detector (MTD), Barrel and Endcap Electromagnetic Calorimeters (BEMC, EEMC), Forward Calorimeter System (FCS), DAQ/trigger, and the magnet / return-iron absorber, together with the MRPC technology and the current hardware status.

**Scope:** the detectors listed on the SoLID wiki page [RHIC detectors](https://solid.jlab.org/wiki/index.php?title=RHIC_detectors). Entries there that are not covered yet are tracked in [wiki/synthesis/open-questions.md](wiki/synthesis/open-questions.md).

## The LLM-wiki idea

Instead of re-reading papers for every question (plain RAG), an LLM reads each source once and **writes and maintains** a cross-linked wiki: per-source notes, thematic pages per detector, an index and a log. New sources are merged into existing pages, contradictions are flagged, and the knowledge compounds. The human picks sources and asks questions; the LLM does the bookkeeping. Pattern: [llm-wiki.md](llm-wiki.md). Rules for this repo: [CLAUDE.md](CLAUDE.md).

Three layers:

1. **`wiki/synthesis/`** — thematic pages (one per detector, system or technology), citing the notes below.
2. **`raw/<slug>-note.md`** — one curated note per source: bibliography with DOI/arXiv links, paraphrased abstract, key numbers, caveats.
3. **`raw/<slug>.md`** — a *full-content paraphrase* of each source: every section, with all numbers, equations, tables and references reproduced exactly, and the prose in our own words (not a verbatim copy).

## Structure

```
rhic_detectors/
├── README.md            this file
├── CLAUDE.md            schema: layers, naming, reading routes, workflows (read by the LLM every session)
├── llm-wiki.md          the LLM-wiki pattern (Karpathy)
├── agents/              subagent definitions: wiki-fetch (acquisition), wiki-vision (figure check)
├── scripts/             lint.py (structural checks), ingest_clean.py (arXiv HTML cleanup)
├── raw/
│   ├── <slug>.md        full-content paraphrase of a source
│   ├── <slug>-note.md   curated note on that source
│   └── assets/          PDFs and figures — local only, not in the public repo
└── wiki/
    ├── index.md         start here: thematic reading path
    ├── list.md          inventory of every source
    ├── log.md           chronological record of ingests, queries, lint passes
    └── synthesis/       thematic pages
```

## How to read it

- Start at [wiki/index.md](wiki/index.md), then follow the links into the detector pages and, from there, into the per-source notes.
- [wiki/list.md](wiki/list.md) lists every source with how it was captured.
- **On GitHub:** start at [wiki/index.md](wiki/index.md); all cross-references are relative links and click through. Figures do not show (images and PDFs are not in the repo); follow the DOI links in each note.
- **In Obsidian** (open the repo folder as a vault): links, backlinks, graph view and, on the maintainer's machine, figures all work.

## Coverage

The authoritative source list of each page is its `sources:` frontmatter.

| Detector / topic | Synthesis page | Main sources (slug) |
|---|---|---|
| STAR barrel TOF (BTOF) | [star-barrel-tof](wiki/synthesis/star-barrel-tof.md) | shao2002-mrpc-beam-test, schambach2006-star-tof-electronics, wu2007-star-barrel-tof, llope2012-star-mrpc-systems, star2026-detector-status |
| STAR Muon Telescope Detector (MTD) | [star-mtd](wiki/synthesis/star-mtd.md) | ruan2009-mtd-concept, yang2014-mtd-cosmic-calibration, huang2016-mtd-muon-id, llope2012-star-mrpc-systems, star2026-detector-status |
| STAR Barrel EM Calorimeter (BEMC) | [star-bemc](wiki/synthesis/star-bemc.md) | beddo2003-bemc, star2026-detector-status |
| STAR Endcap EM Calorimeter (EEMC) | [star-eemc](wiki/synthesis/star-eemc.md) | star2003-eemc, star2026-detector-status |
| STAR Forward Calorimeter System (FCS) | [star-fcs](wiki/synthesis/star-fcs.md) | tsai2015-fcs-prototype, gagliardi2022-star-forward-upgrade-talk, wang2024-star-forward-upgrade, ruan2026-fcs-specs-email, star2026-detector-status |
| MRPC technology | [mrpc-technology](wiki/synthesis/mrpc-technology.md) | shao2002-mrpc-beam-test, schambach2006-star-tof-electronics, wu2007-star-barrel-tof, llope2012-star-mrpc-systems, ruan2009-mtd-concept, yang2014-mtd-cosmic-calibration |
| STAR DAQ and trigger | [star-daq-trigger](wiki/synthesis/star-daq-trigger.md) | schambach2006-star-tof-electronics, llope2012-star-mrpc-systems, ruan2009-mtd-concept, beddo2003-bemc, star2003-eemc, gagliardi2022-star-forward-upgrade-talk, wang2024-star-forward-upgrade |
| STAR magnet and absorber | [star-magnet-absorber](wiki/synthesis/star-magnet-absorber.md) | ruan2009-mtd-concept, yang2014-mtd-cosmic-calibration, huang2016-mtd-muon-id, beddo2003-bemc, star2003-eemc |
| π/μ separation with calorimetry | [pi-mu-separation-calorimetry](wiki/synthesis/pi-mu-separation-calorimetry.md) | ruan2009-mtd-concept, huang2016-mtd-muon-id, beddo2003-bemc, tsai2015-fcs-prototype |
| Current hardware status | [rhic-detector-status](wiki/synthesis/rhic-detector-status.md) | star2026-detector-status, ruan2026-fcs-specs-email, wang2024-star-forward-upgrade |
| Open questions and uncovered scope | [open-questions](wiki/synthesis/open-questions.md) | all |

Sources (details, DOIs and capture route in each `raw/<slug>-note.md` and in [wiki/list.md](wiki/list.md)):

| Slug | Source | Type |
|---|---|---|
| shao2002-mrpc-beam-test | M. Shao et al., Nucl. Instrum. Meth. A 492 (2002) 344 | paper |
| beddo2003-bemc | M. Beddo et al., Nucl. Instrum. Meth. A 499 (2003) 725 | paper |
| star2003-eemc | C.E. Allgower et al. (STAR), Nucl. Instrum. Meth. A 499 (2003) 740 | paper |
| schambach2006-star-tof-electronics | J. Schambach et al., 2006 IEEE NSS Conf. Rec. vol. 1, 485 | paper |
| wu2007-star-barrel-tof | J. Wu, M. Xu, J. Phys. G 34 (2007) S729 | paper |
| ruan2009-mtd-concept | L. Ruan et al., J. Phys. G 36 (2009) 095001 | paper |
| llope2012-star-mrpc-systems | W.J. Llope, Nucl. Instrum. Meth. A 661 (2012) S110 | paper |
| yang2014-mtd-cosmic-calibration | C. Yang et al., Nucl. Instrum. Meth. A 762 (2014) 1 | paper |
| tsai2015-fcs-prototype | O.D. Tsai et al., J. Phys. Conf. Ser. 587 (2015) 012053 | paper |
| huang2016-mtd-muon-id | T.C. Huang et al., Nucl. Instrum. Meth. A 833 (2016) 88 | paper |
| gagliardi2022-star-forward-upgrade-talk | C. Gagliardi, *The STAR Forward Upgrade*, STAR talk, 2022 | talk slides |
| wang2024-star-forward-upgrade | Z. Wang, EPJ Web Conf. 296 (2024) 16003 | paper |
| ruan2026-fcs-specs-email | L. Ruan, FCS ECal/HCal construction specs, email, 2026-10-29 | email |
| star2026-detector-status | STAR detector status as of October 2026 (one-page sheet) | status sheet |

## What is not in this repo

- **Paper PDFs and figure images.** They are not ours to redistribute, so `raw/assets/` is git-ignored and stays on the maintainer's machine. Figure embeds in `raw/<slug>.md` therefore show as broken images on GitHub; every figure keeps its caption and a description, and the DOI/arXiv links in each note lead to the original.
- **Full sources (`raw/<slug>.md`, Layer 3).** Kept on the maintainer's machine only (git-ignored since 2026-11-11). The published notes (`raw/<slug>-note.md`) carry the key numbers, caveats and links to the original via DOI/arXiv; their "full source" links do not resolve on GitHub.
- Facts stated by the maintainer that no source contains are cited as "Zhiwen, personal communication, <date>".

## Working with it

With an LLM agent (e.g. Claude Code) opened in this folder, which reads [CLAUDE.md](CLAUDE.md) first:

- **Ingest:** "Ingest `<DOI / arXiv id / file>` into the wiki: Layer 3 full-content paraphrase, note, synthesis updates, list/index/log, lint."
- **Query:** "Using the wiki, compare the time resolution of the BTOF and MTD MRPCs, with sources."
- **Lint:** "Health-check the wiki: run `python3 scripts/lint.py`, then flag contradictions, stale claims, orphan pages and missing cross-references."
- **File back:** "That comparison is useful — save it as a synthesis page."

Structural check, from the repo root: `python3 scripts/lint.py` (Python 3, stdlib only; image checks are skipped when `raw/assets/` is absent).

## Credits

Built with Claude, following Karpathy's LLM-wiki pattern ([llm-wiki.md](llm-wiki.md)).
