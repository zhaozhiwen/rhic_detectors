# log

Append-only record of wiki activity. Format: `## [YYYY-MM-DD] <type> | <title>` (types: ingest, query, lint, tooling, assets). Newest first. Entries before the 2026-11-09 restructure were converted from the History section of the old README; old file names are given with their new slugs.

---

## [2026-11-16] ingest | STAR Forward Upgrade proposal (Nov 2018 review version)
- Added: raw/star2018-forward-upgrade-proposal.md (Layer 3), raw/star2018-forward-upgrade-proposal-note.md (Layer 2), new synthesis page [star-forward-tracking](synthesis/star-forward-tracking.md). The STAR Collaboration, *The STAR Forward Calorimeter System and Forward Tracking System*, proposal, November 2018 (review version), 84 pp.; `source_type: proposal`. Public copy with the same file name: https://drupal.star.bnl.gov/STAR/files/Proposal.ForwardUpgrade.Nov_.2018.Review.pdf.
- Route 3 (PDF only): local copy supplied by the repo author (Word-made PDF, clean text layer; printed page = PDF page); local backup `raw/assets/star2018-forward-upgrade-proposal/source.pdf` and `source.txt`. Later related STAR documents (STAR Note SN0648 "… beyond BES-II"; ForwardUpgrade.v20.pdf) are recorded in the note as not ingested; version relation unverified.
- Scope (user-approved): Ch. 1, 3, 4, 5 and the bibliography (141 entries) in full; Ch. 2 (physics case) summarised by section with Tables 2-1 and 2-2 in full and its 39 figures by caption only; table of contents skipped.
- Transcription: 4 opus transcription subagents from 100-dpi page renders plus the text layer. Figures (57 in Ch. 3–5) cropped from 300-dpi Ghostscript renders by ink-region detection with text lines whitened; problem crops re-cut by hand; checked on contact sheets.
- Vision: claude-opus-5-5 (general-purpose subagent, model opus), 2026-11-16; 57 figures described; Fig. 4-19 (a table stored as an image) transcribed in the vision pass.
- Writer verification: Tables 2-1, 2-2, 3-1, 5-1 present (the source has no Table 1-x; Table 5-1 is the silicon dose table, not an sTGC table); every number in the body text of Ch. 3–5 found in the text layer (misses only inside figure descriptions and [note] lines); about 40 numbers spot-checked on the page renders pp. 53, 54, 56, 66, 73, 75, 76, 77 (1496/15552/520 towers, 2.6 m × 2 m, HCal 20 / 3.1 / 3 mm, 38 layers, 4.5 λ, 5 mm pins, FEE 180 GeV / 14-bit 0–70 V / 800 µA / < 150 Ω / < 1 mV / 0–66 mV/°C / +80 V / 0–410 and 0–614 µA, 16 FEE per bus, trigger 64 bits / 107 ns / 34 links / 74 + 3 boards / 20 + 8 + 4, IST DAQ 864/288 APV / 6 modules / 24 APV / 24 m / 37.532 MHz / 2.125 Gbps / 0.3 W, Table 5-1 all cells, NIEL 1–7×10¹², sTGC 50 μm / 1.8 / 1.4 mm / 2900 V / 100 μm / 1.5 mm / 3.2 mm / 55–45% / 40 modules / $200K / 24000 channels / 2900 → 2600 V) — all match.
- Updated: [star-fcs](synthesis/star-fcs.md) (new design-stage section and design-vs-as-built table: front-face ECal readout, 38-layer HCal, sampling fractions, FEE/bias specs, SiPM radiation study, DEP counts, simulated trigger efficiencies; 2014 test-beam cross-check; open points rewritten), [star-daq-trigger](synthesis/star-daq-trigger.md) (retitled "STAR DAQ and trigger paths (BTOF, MTD, forward upgrade)"; new section: DEP/ADC and DEP/IO, three-layer FCS trigger, Run 17 prototype, FST readout via the IST DAQ and ALICE DDL, sTGC TPC-readout plan vs as-built VMM), [open-questions](synthesis/open-questions.md), [rhic-detector-status](synthesis/rhic-detector-status.md) (sTGC and FST rows now link to star-forward-tracking), [list](list.md), [index](index.md). Cross-references and version fields: [wang2024-star-forward-upgrade-note](../raw/wang2024-star-forward-upgrade-note.md), [gagliardi2022-star-forward-upgrade-talk-note](../raw/gagliardi2022-star-forward-upgrade-talk-note.md) (earlier_version: the proposal, a separate document), [tsai2015-fcs-prototype-note](../raw/tsai2015-fcs-prototype-note.md) (later_version: the proposal), [ruan2026-fcs-specs-email-note](../raw/ruan2026-fcs-specs-email-note.md) (version_facts); readout-end caveats in all four notes updated; `notes_updated` / `versions_checked` 2026-11-16.
- Main findings: the 2018 design already has 1496 PHENIX ECal + 520 HCal towers and the as-built sampling fractions (0.20, 0.0145), but a 38-layer HCal (as built 36 + back plate) and an EM resolution printed both ~8% and ~10%/√E; ECal readout on the front face by design; no ECal tower length or depth given (only the PHENIX calorimeter paper cited); 74 DEP/ADC = as-built 2 × (24 + 9) calorimeter boards + 8 preshower boards [note]; SiPM Run-17 degradation explained by junction heating, new HPK S14160-015P keeps it at ≈ 1%; FTS design FST z = 139.9/163.2/186.5 cm and sTGC 273–363 cm with square modules and TPC (ALTRO) readout, changed by construction to FST 152–179 cm and pentagonal sTGC modules with VMM readout at 300–360 cm.
- Source issues recorded: ~8% vs ~10%/√E; broken "Section 0" references; figure references one number low in §4.5; 3.2.1 Fig. 3-6 vs 3-4; 24 m vs "120 feet"; "between 15 kg"; FTS/FST naming; 500 GeV luminosity 1 vs 1.1 fb⁻¹; several typos (FSC, FANL, ALTAS, "Newton's low").
- Open questions: #15 narrowed (readout end probably resolved in favour of the front face; ECal length and λ still open, next source the PHENIX calorimeter NIM A 499 (2003) 521); added #24 (FCS HCal layer count 38 vs 36) and #25 (FTS as-built geometry and design changes).

## [2026-11-16] ingest | Kajimoto 2009 PhD thesis, STAR barrel TOF (UT Austin)
- Added: raw/kajimoto2009-star-tof-thesis.md (Layer 3), raw/kajimoto2009-star-tof-thesis-note.md (Layer 2). K. Kajimoto, *A Large Area Time of Flight Detector for the STAR Experiment at RHIC*, PhD dissertation, The University of Texas at Austin, December 2009 (supervisor G. Hoffmann); `source_type: thesis`.
- Route 3 (PDF only): open-access PDF from Texas ScholarWorks (no HTML or arXiv version), fetched in the user's Chrome; 197 pages, printed page = PDF page − 13. Local backup `raw/assets/kajimoto2009-star-tof-thesis/source.pdf` and `source.txt` (text layer). Embedded pages of other documents leak hidden text into the text layer, so the rendered pages decided.
- Scope (user-approved): Ch. 3–7 in full; Ch. 1–2 summarised by section except §2.2.4 (CTB), §2.2.7 (pVPD) and §2.2.10 (Trigger) in full; Appendices 1–2 by caption with a short summary; Appendix 3 (acronyms) and the bibliography in full.
- Transcription: chunked, by 8 opus transcription subagents from 100-dpi page renders plus the text layer. Figures (104) cropped by caption position from 300-dpi Ghostscript page renders, landscape pages rotated upright, checked on contact sheets.
- Vision: claude-opus-5-5 (general-purpose subagent, model opus), 2026-11-16; 89 figures described (Figs. 2.1–6.6), 15 appendix figures by caption only.
- Writer verification: equation tags 1.1, 3.1–3.3, 4.1–4.11, 5.1–5.2 continuous; Tables 1.1, 4.1–4.7, 5.1, 6.1–6.7 present; page markers for every printed page i–iv, 1–184; about 30 numbers spot-checked against page renders (§3.1 tray box, Fig. 3.4 dimensions incl. a 300-dpi zoom of the short-edge axis, Tables 4.1, 4.2, 4.6, 4.7, 5.1, 6.1, 6.2, 6.6, Eqs. 4.1–4.2, Ch. 6 intro, §6.3, §7.1) — all match; every number in the note found in Layer 3.
- Updated: [star-barrel-tof](synthesis/star-barrel-tof.md) (tray box, module size, pad layout and stated orientation, glass, gap-count conflict, board history, UT cosmic results, new sections on production/QA, Run 8/9 commissioning and the CTB), [star-daq-trigger](synthesis/star-daq-trigger.md) (as-built boards and history, five networks, THUB-NW clock tree, DAQ receiver, TOF controller, Run-9 operations, STAR trigger section), [mrpc-technology](synthesis/mrpc-technology.md) (new section 5: cosmic-test analysis, noise rates, threshold scans; pad table; glass/gap row; VPD; "seven" → "eight" STAR MRPC sources), [rhic-detector-status](synthesis/rhic-detector-status.md) (BTOF installation history 2007–2010, 126 built, pad bullet), [open-questions](synthesis/open-questions.md), [list](list.md), [index](index.md). Cross-references: [schambach2006-star-tof-electronics-note](../raw/schambach2006-star-tof-electronics-note.md) (pad/glass caveats updated, version_facts), [llope2012-star-mrpc-systems-note](../raw/llope2012-star-mrpc-systems-note.md), [wu2007-star-barrel-tof-note](../raw/wu2007-star-barrel-tof-note.md) (`notes_updated: 2026-11-16`).
- Main findings: tray box 95" × 8.5" × 3.5" (241.3 × 21.6 × 8.9 cm); MRPC module 212.0 × 94.0 × 17.9 mm (measured 211.94 × 94.04 × 18.21 mm); pads 3.15 cm with 0.3 cm interval (pitch 3.45 cm), row perpendicular to the tray's long side; glass 1.1/0.54 mm (agrees with Llope 2012, against Schambach 2006's 0.7/0.55 mm); 5 inner + 2 outer plates ⇒ 6 gaps (Llope 2012 says five); 126 trays built (120 + 6 spares), 125 shipped; tray noise mean 7.37 Hz at 2500 mV, 101 of 24192 channels (0.417 %) above 50 Hz; tray-stand cosmic mean 238.6 ps without slewing correction; Run 8: 5 trays, 2 of 960 channels dead; Run 9: 94 installed, 86 active, 9 (or 10) dead channels; threshold scans led to a 1200 mV beam test.
- Source issues recorded (Layer 3 and note): Eq. 3.3 γ² placement; Eq. 4.2 pad area in mm; HPTDCs per TDIG 3 vs 4; CAT-5 vs CAT-6; Table 6.1 shipment 4 count; dead-channel totals (16152, 0.55 %, 9 vs 10) and live-channel averages above 192; several run numbers with wrong digit counts.
- Open questions: #16 (pad width and glass) closed; #13 partly answered (tray box, module size, inter-pad gap, pad orientation; tilt angles and tray radius still missing); #9 count updated to eight sources; added #21 (gap count 5 vs 6), #22 (Run-9 dead-channel count and live-channel arithmetic), #23 (VPD distance 5 / 5.4 / 5.6 m).

## [2026-11-11] lint | Layer 3 audit and figure re-description (option A)
- Scope: 9 Layer 3 full sources audited (beddo2003-bemc, wu2007-star-barrel-tof, wang2024-star-forward-upgrade, shao2002-mrpc-beam-test, ruan2009-mtd-concept, llope2012-star-mrpc-systems, star2003-eemc, yang2014-mtd-cosmic-calibration, tsai2015-fcs-prototype) by 3 report-only Opus verifiers; fixes applied by 3 separate Opus writers. The Gagliardi 2022 talk was not audited (can be added later).
- Figures: new vision descriptions for 10 papers (78 figures) by 4 Opus vision subagents; `vision_model` recorded in each Layer 3 frontmatter (claude-opus-5-5, general-purpose subagent, 2026-11-11).
- Text-layer extracts: `raw/assets/<slug>/source.txt` (`pdftotext -layout`, local only) made for the five PDF-only sources (shao2002, wu2007, tsai2015, wang2024, gagliardi2022 talk).
- Route re-check: wang2024 (EPJ WoC) and tsai2015 (IOP) still PDF only; ruan2009 IOPscience abstract + PDF only; huang2016 ScienceDirect now serves the HTML body → **re-captured via Route 1** (ScienceDirect HTML; formulas and Table 1 checked against the publisher PDF; publisher high-resolution figures), captured_date 2026-11-11. No number or statement changed against the earlier Route 2 (arXiv v3 HTML) capture, which is quarantined in `_to_delete/huang2016-old/`.
- ruan2009: text aligned to the publisher J. Phys. G PDF (captured_via updated; PACS codes were arXiv-only); Fig. 1 replaced by a correct 300-dpi publisher-PDF cut (the old image had inverted colours; quarantined in `_to_delete/ruan2009-old/`).
- Layer 3 stays a full-content paraphrase. Near-verbatim passages were found in every audited file and re-paraphrased. Layer 3 files are local only (git-ignored since 2026-11-11); only notes and synthesis pages are published.
- Content moved out of Layer 3: tsai2015 old "Checks (d)" (2014 prototype vs as-built FCS, drawn from a later source) → a labelled cross-source comparison in [tsai2015-fcs-prototype-note](../raw/tsai2015-fcs-prototype-note.md); eemc October 2026 status → cited from [star2026-detector-status-note](../raw/star2026-detector-status-note.md) in [star2003-eemc-note](../raw/star2003-eemc-note.md); yang2014 15–18 cm/ns signal-speed sentence removed (not in the paper; stays a from-memory item in open question #9).
- Main corrections carried into notes/synthesis: eemc SMD depth in cm not checkable from the paper (≈ 12–15 cm estimate withdrawn); eemc §6 "π⁰ and Z⁰" tagged [source issue] (η⁰ meant); ruan2009 strip width 25 mm with inter-strip gap not given (span ≥ 150 mm), Fe dE/dx 11.8–12.6 MeV/cm, 2160/540 = 4 strips no longer called an internal inconsistency, rejection 50–100 ⇒ 1–2% acceptance vs "< 1%"; shao2002 Fig. 10 "about 55 ps" closer to the raw 57.7 ps (jitter included); wang2024 ±60 cm ΔX side peaks only approximately half an HCal half (≈ 65 cm); wu2007 85 ps ambiguity retagged [note]; llope2012 "50 m²" (no "~" printed); yang2014 affiliation as printed (Variable Energy Cyclotron Centre, West Bengal); tsai2015 printed forms "S10931-025p" and "SENSL SiPMTs", Giessen/dates and 25 µm pitch tagged [note], e/h above 10 GeV ≈ 0.915–0.945, Pb(Sb) density ≈ 11.0 g/cm³ (≈ 3.7 λ_I), photostatistics a quarter or a fifth of the variance; huang2016 new figure findings (Fig. 1 inset χ²/ndf 53.0/37.0; "Counts/Bin" behaves like counts per GeV/c² [note]; Fig. 3 has no ΔToF panel and legend says "linear extrapolation" [source issue]; Fig. 6 data plateaus ≈ 0.67/0.72 vs text "about 80%" [note]).
- Updated notes: huang2016, ruan2009, tsai2015, star2003-eemc, yang2014, shao2002, wang2024, wu2007, llope2012 (`notes_updated: 2026-11-11`; `versions_checked` 2026-11-11 for huang2016, ruan2009, tsai2015, wang2024). Synthesis: [star-mtd](synthesis/star-mtd.md), [star-eemc](synthesis/star-eemc.md), [star-fcs](synthesis/star-fcs.md), [star-barrel-tof](synthesis/star-barrel-tof.md), [pi-mu-separation-calorimetry](synthesis/pi-mu-separation-calorimetry.md), [open-questions](synthesis/open-questions.md) (#9 and #11 updated; #17 EEMC SMD depth, #18 MTD muon-ID data plateaus, #19 2009 prototype strip gap, #20 2009 hadron rejection added). [list](list.md) (huang2016 → Route 1, 2026-11-11; ruan2009 alignment noted), [index](index.md).

## [2026-11-11] tooling | Wikilinks converted to relative Markdown links
- Why: GitHub shows Obsidian `[[wikilinks]]` as plain text, so cross-references did not work on the repo's web page.
- 598 links in 36 files (raw/, wiki/, wiki/synthesis/) converted by a one-off script to `[slug](relative/path.md)`; none unresolved. Text in code spans and YAML frontmatter untouched.
- `scripts/lint.py`: new checks `wikilink_syntax` (any `[[…]]` left) and `unresolved_link`; companion and `list.md` checks now follow Markdown links (`note_companion_not_linked`). Tested on a scratch copy with deliberately broken links.
- CLAUDE.md linking rules, README ("how to read it") and scripts/CLAUDE.md updated. Obsidian setting to match: Files & Links → `Use [[Wikilinks]]` off, "New link format" = relative path.

## [2026-11-11] tooling | Repo and folder renamed to rhic_detectors
- GitHub repo is `zhaozhiwen/rhic_detectors` (plural); the local folder was renamed from `rhic_detector` to `rhic_detectors` to match. README, CLAUDE.md, agents/ and scripts/ updated. Earlier log entries keep the old name.
- Git: the repo root is now this folder (the clone's `.git` was moved up from a nested checkout).

## [2026-11-10] ingest | Schambach et al. 2006, STAR TOF readout electronics (IEEE NSS)
- Added: raw/schambach2006-star-tof-electronics.md (Layer 3), raw/schambach2006-star-tof-electronics-note.md (Layer 2). J. Schambach et al., *STAR Time of Flight Readout Electronics, DAQ, and Cosmic Ray Test Stand*, 2006 IEEE NSS Conf. Rec. vol. 1, 485–488, doi:10.1109/NSSMIC.2006.356203.
- Route 1: IEEE Xplore full-text HTML in the user's Chrome (institutional access); text and MathJax TeX from the DOM, references from the Xplore list; every number and the formula checked against `pdftotext -layout` of the publisher PDF (HTML and PDF agree). Chrome first blocked repeated downloads from ieeexplore.ieee.org until the user allowed automatic downloads for the site. PDF backup kept locally in `raw/assets/schambach2006-star-tof-electronics/source.pdf`. Figures (3) cropped from 300-dpi PDF renders because the HTML "large" GIFs are only ~380 px wide.
- Vision: claude-opus-5-5 (general-purpose subagent, model opus), 2026-11-10, all 3 figures.
- Updated: [star-barrel-tof](synthesis/star-barrel-tof.md) (MRPC/tray construction numbers, electronics counts, 2006 timing budget, cosmic stand 80–110 ps, pad-size contradiction in the table and the pad-orientation inference), [star-daq-trigger](synthesis/star-daq-trigger.md) (board internals, HPTDC 40 → 320 MHz / 32-tap DLL / 4-tap RC → 24.41 ps, buffers, TCPU cabling, THUB clock and SIU/RORC/Myrinet link, TPMD start side, timing budget; MTD path unchanged), [mrpc-technology](synthesis/mrpc-technology.md) (NINO features, HPTDC bin arithmetic, glass thicknesses, cosmic difference width vs single-module resolution; "six" → "seven" STAR MRPC papers), [rhic-detector-status](synthesis/rhic-detector-status.md) (pad-width caveat), [open-questions](synthesis/open-questions.md), [list](list.md), [index](index.md); Related blocks of [llope2012-star-mrpc-systems-note](../raw/llope2012-star-mrpc-systems-note.md) and [wu2007-star-barrel-tof-note](../raw/wu2007-star-barrel-tof-note.md).
- Discrepancy: pad printed 3.3 cm × 6.1 cm here vs 3.5 × 6.1 cm² in Llope 2012; also outer/inner glass 0.7/0.55 mm vs 1.1/0.54 mm. Not resolved; both values given. The pad-orientation inference (short side along φ) holds for either width (19.8 or 21 cm across a ≈ 21 cm tray); σ across 0.95 vs 1.01 cm.
- Open questions: #16 added (TOF pad and glass dimensions); #13 next step now carries the TOF proposal URL from this paper's ref. [1] (no #13 item closed: the paper gives no MRPC outer size, inter-pad gap, tilt angles or tray dimensions); #9 count updated to seven papers. The from-memory MTD items (THUB/DDL sharing, QT boards, "MINO") are not addressed by this 2006 paper and stay unverified.

## [2026-11-09] tooling | Restructure into an LLM wiki for the public repo zhaozhiwen/rhic_detector
- **Layout:** three-layer LLM wiki (Karpathy pattern): `wiki/` (index, list, log + `synthesis/`), `raw/<slug>-note.md` (Layer 2), `raw/<slug>.md` (Layer 3).
- **Slugs renamed (old → new):**
  - `2002_shao_tof_mrpc.md` → `shao2002-mrpc-beam-test`
  - `2003_beddo_bemc_design.md` → `beddo2003-bemc`
  - `2003_allgower_eemc_design.md` → `star2003-eemc`
  - `2007_wu_tof_barrel.md` → `wu2007-star-barrel-tof`
  - `2009_ruan_mtd_design.md` → `ruan2009-mtd-concept`
  - `2012_llope_tof_system.md` → `llope2012-star-mrpc-systems`
  - `2014_yang_mtd_cosmic_performance.md` → `yang2014-mtd-cosmic-calibration`
  - `2015_tsai_fcs_prototype.md` → `tsai2015-fcs-prototype`
  - `2016_huang_mtd_muon_id.md` → `huang2016-mtd-muon-id`
  - `2022_gagliardi_fcs_forward_upgrade_talk.md` → `gagliardi2022-star-forward-upgrade-talk`
  - `2024_wang_fcs_forward_upgrade.md` → `wang2024-star-forward-upgrade`
  - `email_lijuan.docx` / `email_lijuan.md` → `ruan2026-fcs-specs-email`
  - `STAR_Detector_Status.pdf` → `star2026-detector-status` (new Layer-3 file from the PDF)
- **Layer 3** (`raw/<slug>.md`) = the full-content paraphrase notes (equations, numbers and tables exact; figure descriptions), with PDFs and figures under `raw/assets/<slug>/`.
- **Layer 2** notes `raw/<slug>-note.md` added for all 13 sources.
- **Layer 1** synthesis pages created from `summary.md`, `qa_mrpc.md`, `qa_hcal.md` and the README (Status, Open issues): [star-barrel-tof](synthesis/star-barrel-tof.md), [star-mtd](synthesis/star-mtd.md), [star-bemc](synthesis/star-bemc.md), [star-eemc](synthesis/star-eemc.md), [star-fcs](synthesis/star-fcs.md), [mrpc-technology](synthesis/mrpc-technology.md), [star-daq-trigger](synthesis/star-daq-trigger.md), [star-magnet-absorber](synthesis/star-magnet-absorber.md), [pi-mu-separation-calorimetry](synthesis/pi-mu-separation-calorimetry.md), [rhic-detector-status](synthesis/rhic-detector-status.md), [open-questions](synthesis/open-questions.md); plus [index](index.md), [list](list.md) and this log. Old file references replaced by wikilinks; Zhiwen's statements tagged "Zhiwen, personal communication, 2026-11-09".
- **Not published:** `raw/assets/` (publisher PDFs, figures) stays local. arXiv PDFs dropped where a publisher version exists.
- **Dropped:** the web page build (`site/`: build script, template, generated HTML).
- **Pending:** old files (`README.md`, `summary.md`, `qa_mrpc.md`, `qa_hcal.md`, `site/`) moved to `_to_delete/`, kept until the user confirms deletion.

## [2026-11-09] ingest | Beddo et al. 2003, STAR BEMC (NIM A 499, 725)
- Added: raw/beddo2003-bemc.md (old `2003_beddo_bemc_design.md`), Route 1 (ScienceDirect HTML; formulas and Table 1 from the PDF, where the HTML drops √). Subagent workflow (reader + figure pass + number check against the PDF).
- Updated: BEMC/EEMC section of the cross-paper summary (now [star-bemc](synthesis/star-bemc.md)); the MTD "≈ 5 interaction lengths" discrepancy now uses the BEMC's ≈ 0.7 λ_I ([star-magnet-absorber](synthesis/star-magnet-absorber.md)). Added to the web page.

## [2026-11-09] ingest | Allgower et al. 2003, STAR EEMC (NIM A 499, 740)
- Added: raw/star2003-eemc.md (old `2003_allgower_eemc_design.md`), Route 1 (ScienceDirect HTML; Table 1 rebuilt from the PDF). Same workflow.
- Updated: BEMC/EEMC section of the summary (now [star-eemc](synthesis/star-eemc.md)). Added to the web page.

## [2026-11-09] query | Remaining BTOF and MTD trays
- Zhiwen stated the remaining hardware: Barrel TOF 112 of 120 trays, MTD 61 of 122 trays. Both agree with the October 2026 status sheet ("All except 8 trays", "Half"). Derived: 112 trays ≈ 56 m² tray, ≈ 46 m² pads, 21 504 channels; 61 trays ≈ 30 m² tray, ≈ 24.2 m² strips, 1464 channels.
- Now in: [rhic-detector-status](synthesis/rhic-detector-status.md), [star-barrel-tof](synthesis/star-barrel-tof.md), [star-mtd](synthesis/star-mtd.md).

## [2026-11-09] query | BTOF and MTD tray sizes
- Zhiwen stated: BTOF 120 trays of ≈ 2.4 m × 21 cm; MTD 122 trays of ≈ 90 × 55 cm. All geometric cross-checks pass (MTD strip area 48.4 m² = 45.5% of the |η| < 0.5 band; 21 cm tray fits six 3.5 cm pads).
- Now in: [star-barrel-tof](synthesis/star-barrel-tof.md), [star-mtd](synthesis/star-mtd.md), [rhic-detector-status](synthesis/rhic-detector-status.md).

## [2026-11-06] ingest | Gagliardi 2022, STAR Forward Upgrade talk
- Added: raw/gagliardi2022-star-forward-upgrade-talk.md (old `2022_gagliardi_fcs_forward_upgrade_talk.md`), talk slides (PDF) from Zhiwen's Downloads; not peer-reviewed. Left off the web page (internal collaboration talk).
- Updated: FCS section of the summary (now [star-fcs](synthesis/star-fcs.md)); open issue 15 added ([open-questions](synthesis/open-questions.md)).

## [2026-11-06] ingest | Wang 2024, STAR forward detector upgrade (EPJ Web Conf. 296, 16003)
- Added: raw/wang2024-star-forward-upgrade.md (old `2024_wang_fcs_forward_upgrade.md`), Route 3 (PDF; no HTML full text, no arXiv). Added to the web page under "Papers: FCS".
- Updated: FCS section of the summary (now [star-fcs](synthesis/star-fcs.md)).

## [2026-11-06] ingest | Tsai et al. 2015, FCS prototype (J. Phys. Conf. Ser. 587, 012053)
- Added: raw/tsai2015-fcs-prototype.md (old `2015_tsai_fcs_prototype.md`), Route 3 (PDF). The 2014 prototype, not the as-built FCS. Added to the web page under "Papers: FCS".
- Updated: FCS section of the summary (now [star-fcs](synthesis/star-fcs.md)).

## [2026-11-06] query | Further reading on STAR DAQ and trigger
- Added to Q6: Landgraf 2003, Bieser 2003, Landgraf 2013 DAQ talk (indico 246374/542866) and the free STAR NIM DAQ PDF. Open issue 14 added (MTD DAQ path not stated in the papers).
- Now in: [star-daq-trigger](synthesis/star-daq-trigger.md), [open-questions](synthesis/open-questions.md).

## [2026-11-06] query | BTOF and MTD data acquisition chain (Q6)
- BTOF chain TINO → TDIG → TCPU → THUB → DDL from Llope 2012; MTD path into STAR DAQ marked as not stated in any paper.
- Now in: [star-daq-trigger](synthesis/star-daq-trigger.md).

## [2026-11-06] tooling | SoLID wiki *RHIC detectors* link
- Link https://solid.jlab.org/wiki/index.php?title=RHIC_detectors added to the README and the web page (header button, index legend, About); page republished. The SoLID wiki was reachable again.

## [2026-11-06] tooling | Notes published as a private claude.ai page "RHIC Detector Notes"
- Contents: About, summary, qa_mrpc, qa_hcal and the paper notes, with an Ask Claude function. Comments were enabled and removed the same day at Zhiwen's request. Build script saved in `site/` (pandoc 2.9 needed a `\tag` workaround on the Cowork VM). Dropped in the 2026-11-09 restructure.

## [2026-11-06] query | BTOF pads, √12 derivation, photosensor, readout electronics (Q1 addendum, Q3–Q5)
- Q1: why the variance integral is over x² (quadrature addition, Gaussian RMS). Q3: BTOF pad position resolution = pad size/√12 (1.01 × 1.76 cm), 2D derivation, inferred pad orientation (3.5 cm in φ, 6.1 cm along z). Q4: no photosensor (≈ 25 fC directly into NINO). Q5: BTOF vs MTD readout electronics.
- BTOF tray size (stated vs derived) and the inferred pad orientation added to the summary.
- Now in: [mrpc-technology](synthesis/mrpc-technology.md), [star-barrel-tof](synthesis/star-barrel-tof.md).

## [2026-11-06] tooling | README reorganized
- Layout listed `pdf/`, `figures/` and `STAR_Detector_Status.pdf`; per-paper workflow moved into Rules; history condensed.

## [2026-11-06] ingest | Llope 2012, Multigap RPCs in STAR (NIM A 661, S110)
- Added: raw/llope2012-star-mrpc-systems.md (old `2012_llope_tof_system.md`), Route 1 (ScienceDirect HTML), checked against the publisher PDF.
- Updated: BTOF section of the summary rewritten (now [star-barrel-tof](synthesis/star-barrel-tof.md)); MTD area updated with the 117-WMRPC plan ([star-mtd](synthesis/star-mtd.md)).

## [2026-11-06] ingest | Shao et al. 2002, MRPC beam test (NIM A 492, 344)
- Added: raw/shao2002-mrpc-beam-test.md (old `2002_shao_tof_mrpc.md`), Route 3 (PDF; ScienceDirect served no HTML body; no arXiv); figures cropped from the PDF.
- Updated: BTOF prototype history (now [star-barrel-tof](synthesis/star-barrel-tof.md)).

## [2026-11-05] query | MTD and BTOF coverage and size tables
- Derived as-built MTD module count (≈ 120 from "12 modules = 10%"), strip area and coverage consistency (44.8% vs quoted 45%); 2009 plan inconsistency (56% vs ≈ 75% bar faces).
- Now in: [star-mtd](synthesis/star-mtd.md), [open-questions](synthesis/open-questions.md) #11.

## [2026-11-05] lint | Q&A files checked against the re-read notes
- `qa_mrpc.md` and `qa_hcal.md` checked against the new notes; nothing contradicted. `qa_hcal.md` gained §4.5 (STAR MTD cross-check), now in [pi-mu-separation-calorimetry](synthesis/pi-mu-separation-calorimetry.md).

## [2026-11-05] query | π/μ separation with a hadron calorimeter
- Compiled from external sources (NA62, ATLAS TileCal, ePIC, second EIC detector). Now [pi-mu-separation-calorimetry](synthesis/pi-mu-separation-calorimetry.md).

## [2026-11-05] query | MRPC position resolution (√12) and rate capability (Q1, Q2)
- Q1: two-end timing along the strip, pitch/√12 across; type A 0.84 cm vs 0.9–1.1 measured, type B 1.27 vs 1.6–1.9. Q2: rate capability by electrode type, with external sources; none of the STAR papers measures a rate limit.
- Now in: [mrpc-technology](synthesis/mrpc-technology.md).

## [2026-11-05] ingest | Four STAR TOF/MTD papers re-read with the subagent workflow
- Added: raw/wu2007-star-barrel-tof.md (Route 3, PDF), raw/ruan2009-mtd-concept.md (Route 2, arXiv HTML; checked against the publisher PDF; Fig. 1 from the publisher PDF), raw/yang2014-mtd-cosmic-calibration.md (Route 1, ScienceDirect HTML), raw/huang2016-mtd-muon-id.md (Route 2; ScienceDirect served no HTML body). PDFs and figures saved; the 2016 publisher PDF saved by hand (Chrome blocked a repeated scripted download; old open issue 10 closed).
- Cross-paper summary rewritten from the verified notes; old open issues 1–8 closed. Old `*_v1.md` notes deleted at Zhiwen's request.
- Prior history: before 2026-11-05 the MTD papers 2009, 2014, 2016 had been read in a claude.ai chat via ar5iv (no figures, no PDFs, self-check only); those notes were replaced.

## [2026-11-05] ingest | STAR detector status sheet, October 2026
- Added: `STAR_Detector_Status.pdf` (one page, author not given, created 2026-10-22), listed in the Sources table; now raw/star2026-detector-status.md. Relevant: Barrel TOF "All except 8 trays", MTD "Half", both in situ, no readout; VPD radiation-surveyed and stored; Forward EMCal/HCal in situ; Endcap TOF packed for return to Germany. Now in [rhic-detector-status](synthesis/rhic-detector-status.md).

## [2026-11-05] ingest | Lijuan Ruan email, FCS ECal/HCal construction specs (2026-10-29)
- Added: `email_lijuan.docx` converted to `email_lijuan.md` (verbatim text, table restored, arithmetic checks; stack-depth unit typo corrected to 377.3 mm); now raw/ruan2026-fcs-specs-email.md. Route: email (docx).

## [2026-11-05] tooling | Scope widened to all RHIC detectors on the SoLID wiki
- Folder kept flat. solid.jlab.org returned Cloudflare 522, so the detector list could not be refreshed. `mrpc.md` and `hcal.md` from the chat renamed `qa_mrpc.md` and `qa_hcal.md`.
