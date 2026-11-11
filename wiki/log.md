# log

Append-only record of wiki activity. Format: `## [YYYY-MM-DD] <type> | <title>` (types: ingest, query, lint, tooling, assets). Newest first. Entries before the 2026-11-09 restructure were converted from the History section of the old README; old file names are given with their new slugs.

---

## [2026-11-11] tooling | Repo and folder renamed to rhic_detectors
- GitHub repo is `zhaozhiwen/rhic_detectors` (plural); the local folder was renamed from `rhic_detector` to `rhic_detectors` to match. README, CLAUDE.md, agents/ and scripts/ updated. Earlier log entries keep the old name.
- Git: the repo root is now this folder (the clone's `.git` was moved up from a nested checkout).

## [2026-11-10] ingest | Schambach et al. 2006, STAR TOF readout electronics (IEEE NSS)
- Added: raw/schambach2006-star-tof-electronics.md (Layer 3), raw/schambach2006-star-tof-electronics-note.md (Layer 2). J. Schambach et al., *STAR Time of Flight Readout Electronics, DAQ, and Cosmic Ray Test Stand*, 2006 IEEE NSS Conf. Rec. vol. 1, 485–488, doi:10.1109/NSSMIC.2006.356203.
- Route 1: IEEE Xplore full-text HTML in the user's Chrome (institutional access); text and MathJax TeX from the DOM, references from the Xplore list; every number and the formula checked against `pdftotext -layout` of the publisher PDF (HTML and PDF agree). Chrome first blocked repeated downloads from ieeexplore.ieee.org until the user allowed automatic downloads for the site. PDF backup kept locally in `raw/assets/schambach2006-star-tof-electronics/source.pdf`. Figures (3) cropped from 300-dpi PDF renders because the HTML "large" GIFs are only ~380 px wide.
- Vision: claude-opus-5-5 (general-purpose subagent, model opus), 2026-11-10, all 3 figures.
- Updated: [[star-barrel-tof]] (MRPC/tray construction numbers, electronics counts, 2006 timing budget, cosmic stand 80–110 ps, pad-size contradiction in the table and the pad-orientation inference), [[star-daq-trigger]] (board internals, HPTDC 40 → 320 MHz / 32-tap DLL / 4-tap RC → 24.41 ps, buffers, TCPU cabling, THUB clock and SIU/RORC/Myrinet link, TPMD start side, timing budget; MTD path unchanged), [[mrpc-technology]] (NINO features, HPTDC bin arithmetic, glass thicknesses, cosmic difference width vs single-module resolution; "six" → "seven" STAR MRPC papers), [[rhic-detector-status]] (pad-width caveat), [[open-questions]], [[list]], [[index]]; Related blocks of [[llope2012-star-mrpc-systems-note]] and [[wu2007-star-barrel-tof-note]].
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
- **Layer 1** synthesis pages created from `summary.md`, `qa_mrpc.md`, `qa_hcal.md` and the README (Status, Open issues): [[star-barrel-tof]], [[star-mtd]], [[star-bemc]], [[star-eemc]], [[star-fcs]], [[mrpc-technology]], [[star-daq-trigger]], [[star-magnet-absorber]], [[pi-mu-separation-calorimetry]], [[rhic-detector-status]], [[open-questions]]; plus [[index]], [[list]] and this log. Old file references replaced by wikilinks; Zhiwen's statements tagged "Zhiwen, personal communication, 2026-11-09".
- **Not published:** `raw/assets/` (publisher PDFs, figures) stays local. arXiv PDFs dropped where a publisher version exists.
- **Dropped:** the web page build (`site/`: build script, template, generated HTML).
- **Pending:** old files (`README.md`, `summary.md`, `qa_mrpc.md`, `qa_hcal.md`, `site/`) moved to `_to_delete/`, kept until the user confirms deletion.

## [2026-11-09] ingest | Beddo et al. 2003, STAR BEMC (NIM A 499, 725)
- Added: raw/beddo2003-bemc.md (old `2003_beddo_bemc_design.md`), Route 1 (ScienceDirect HTML; formulas and Table 1 from the PDF, where the HTML drops √). Subagent workflow (reader + figure pass + number check against the PDF).
- Updated: BEMC/EEMC section of the cross-paper summary (now [[star-bemc]]); the MTD "≈ 5 interaction lengths" discrepancy now uses the BEMC's ≈ 0.7 λ_I ([[star-magnet-absorber]]). Added to the web page.

## [2026-11-09] ingest | Allgower et al. 2003, STAR EEMC (NIM A 499, 740)
- Added: raw/star2003-eemc.md (old `2003_allgower_eemc_design.md`), Route 1 (ScienceDirect HTML; Table 1 rebuilt from the PDF). Same workflow.
- Updated: BEMC/EEMC section of the summary (now [[star-eemc]]). Added to the web page.

## [2026-11-09] query | Remaining BTOF and MTD trays
- Zhiwen stated the remaining hardware: Barrel TOF 112 of 120 trays, MTD 61 of 122 trays. Both agree with the October 2026 status sheet ("All except 8 trays", "Half"). Derived: 112 trays ≈ 56 m² tray, ≈ 46 m² pads, 21 504 channels; 61 trays ≈ 30 m² tray, ≈ 24.2 m² strips, 1464 channels.
- Now in: [[rhic-detector-status]], [[star-barrel-tof]], [[star-mtd]].

## [2026-11-09] query | BTOF and MTD tray sizes
- Zhiwen stated: BTOF 120 trays of ≈ 2.4 m × 21 cm; MTD 122 trays of ≈ 90 × 55 cm. All geometric cross-checks pass (MTD strip area 48.4 m² = 45.5% of the |η| < 0.5 band; 21 cm tray fits six 3.5 cm pads).
- Now in: [[star-barrel-tof]], [[star-mtd]], [[rhic-detector-status]].

## [2026-11-06] ingest | Gagliardi 2022, STAR Forward Upgrade talk
- Added: raw/gagliardi2022-star-forward-upgrade-talk.md (old `2022_gagliardi_fcs_forward_upgrade_talk.md`), talk slides (PDF) from Zhiwen's Downloads; not peer-reviewed. Left off the web page (internal collaboration talk).
- Updated: FCS section of the summary (now [[star-fcs]]); open issue 15 added ([[open-questions]]).

## [2026-11-06] ingest | Wang 2024, STAR forward detector upgrade (EPJ Web Conf. 296, 16003)
- Added: raw/wang2024-star-forward-upgrade.md (old `2024_wang_fcs_forward_upgrade.md`), Route 3 (PDF; no HTML full text, no arXiv). Added to the web page under "Papers: FCS".
- Updated: FCS section of the summary (now [[star-fcs]]).

## [2026-11-06] ingest | Tsai et al. 2015, FCS prototype (J. Phys. Conf. Ser. 587, 012053)
- Added: raw/tsai2015-fcs-prototype.md (old `2015_tsai_fcs_prototype.md`), Route 3 (PDF). The 2014 prototype, not the as-built FCS. Added to the web page under "Papers: FCS".
- Updated: FCS section of the summary (now [[star-fcs]]).

## [2026-11-06] query | Further reading on STAR DAQ and trigger
- Added to Q6: Landgraf 2003, Bieser 2003, Landgraf 2013 DAQ talk (indico 246374/542866) and the free STAR NIM DAQ PDF. Open issue 14 added (MTD DAQ path not stated in the papers).
- Now in: [[star-daq-trigger]], [[open-questions]].

## [2026-11-06] query | BTOF and MTD data acquisition chain (Q6)
- BTOF chain TINO → TDIG → TCPU → THUB → DDL from Llope 2012; MTD path into STAR DAQ marked as not stated in any paper.
- Now in: [[star-daq-trigger]].

## [2026-11-06] tooling | SoLID wiki *RHIC detectors* link
- Link https://solid.jlab.org/wiki/index.php?title=RHIC_detectors added to the README and the web page (header button, index legend, About); page republished. The SoLID wiki was reachable again.

## [2026-11-06] tooling | Notes published as a private claude.ai page "RHIC Detector Notes"
- Contents: About, summary, qa_mrpc, qa_hcal and the paper notes, with an Ask Claude function. Comments were enabled and removed the same day at Zhiwen's request. Build script saved in `site/` (pandoc 2.9 needed a `\tag` workaround on the Cowork VM). Dropped in the 2026-11-09 restructure.

## [2026-11-06] query | BTOF pads, √12 derivation, photosensor, readout electronics (Q1 addendum, Q3–Q5)
- Q1: why the variance integral is over x² (quadrature addition, Gaussian RMS). Q3: BTOF pad position resolution = pad size/√12 (1.01 × 1.76 cm), 2D derivation, inferred pad orientation (3.5 cm in φ, 6.1 cm along z). Q4: no photosensor (≈ 25 fC directly into NINO). Q5: BTOF vs MTD readout electronics.
- BTOF tray size (stated vs derived) and the inferred pad orientation added to the summary.
- Now in: [[mrpc-technology]], [[star-barrel-tof]].

## [2026-11-06] tooling | README reorganized
- Layout listed `pdf/`, `figures/` and `STAR_Detector_Status.pdf`; per-paper workflow moved into Rules; history condensed.

## [2026-11-06] ingest | Llope 2012, Multigap RPCs in STAR (NIM A 661, S110)
- Added: raw/llope2012-star-mrpc-systems.md (old `2012_llope_tof_system.md`), Route 1 (ScienceDirect HTML), checked against the publisher PDF.
- Updated: BTOF section of the summary rewritten (now [[star-barrel-tof]]); MTD area updated with the 117-WMRPC plan ([[star-mtd]]).

## [2026-11-06] ingest | Shao et al. 2002, MRPC beam test (NIM A 492, 344)
- Added: raw/shao2002-mrpc-beam-test.md (old `2002_shao_tof_mrpc.md`), Route 3 (PDF; ScienceDirect served no HTML body; no arXiv); figures cropped from the PDF.
- Updated: BTOF prototype history (now [[star-barrel-tof]]).

## [2026-11-05] query | MTD and BTOF coverage and size tables
- Derived as-built MTD module count (≈ 120 from "12 modules = 10%"), strip area and coverage consistency (44.8% vs quoted 45%); 2009 plan inconsistency (56% vs ≈ 75% bar faces).
- Now in: [[star-mtd]], [[open-questions]] #11.

## [2026-11-05] lint | Q&A files checked against the re-read notes
- `qa_mrpc.md` and `qa_hcal.md` checked against the new notes; nothing contradicted. `qa_hcal.md` gained §4.5 (STAR MTD cross-check), now in [[pi-mu-separation-calorimetry]].

## [2026-11-05] query | π/μ separation with a hadron calorimeter
- Compiled from external sources (NA62, ATLAS TileCal, ePIC, second EIC detector). Now [[pi-mu-separation-calorimetry]].

## [2026-11-05] query | MRPC position resolution (√12) and rate capability (Q1, Q2)
- Q1: two-end timing along the strip, pitch/√12 across; type A 0.84 cm vs 0.9–1.1 measured, type B 1.27 vs 1.6–1.9. Q2: rate capability by electrode type, with external sources; none of the STAR papers measures a rate limit.
- Now in: [[mrpc-technology]].

## [2026-11-05] ingest | Four STAR TOF/MTD papers re-read with the subagent workflow
- Added: raw/wu2007-star-barrel-tof.md (Route 3, PDF), raw/ruan2009-mtd-concept.md (Route 2, arXiv HTML; checked against the publisher PDF; Fig. 1 from the publisher PDF), raw/yang2014-mtd-cosmic-calibration.md (Route 1, ScienceDirect HTML), raw/huang2016-mtd-muon-id.md (Route 2; ScienceDirect served no HTML body). PDFs and figures saved; the 2016 publisher PDF saved by hand (Chrome blocked a repeated scripted download; old open issue 10 closed).
- Cross-paper summary rewritten from the verified notes; old open issues 1–8 closed. Old `*_v1.md` notes deleted at Zhiwen's request.
- Prior history: before 2026-11-05 the MTD papers 2009, 2014, 2016 had been read in a claude.ai chat via ar5iv (no figures, no PDFs, self-check only); those notes were replaced.

## [2026-11-05] ingest | STAR detector status sheet, October 2026
- Added: `STAR_Detector_Status.pdf` (one page, author not given, created 2026-10-22), listed in the Sources table; now raw/star2026-detector-status.md. Relevant: Barrel TOF "All except 8 trays", MTD "Half", both in situ, no readout; VPD radiation-surveyed and stored; Forward EMCal/HCal in situ; Endcap TOF packed for return to Germany. Now in [[rhic-detector-status]].

## [2026-11-05] ingest | Lijuan Ruan email, FCS ECal/HCal construction specs (2026-10-29)
- Added: `email_lijuan.docx` converted to `email_lijuan.md` (verbatim text, table restored, arithmetic checks; stack-depth unit typo corrected to 377.3 mm); now raw/ruan2026-fcs-specs-email.md. Route: email (docx).

## [2026-11-05] tooling | Scope widened to all RHIC detectors on the SoLID wiki
- Folder kept flat. solid.jlab.org returned Cloudflare 522, so the detector list could not be refreshed. `mrpc.md` and `hcal.md` from the chat renamed `qa_mrpc.md` and `qa_hcal.md`.
