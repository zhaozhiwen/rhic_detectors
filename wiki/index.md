---
title: index — RHIC detectors
type: index
updated: 2026-11-16
---

# index — RHIC detectors

*Read this first on every query. LLM-maintained catalog of all wiki pages.*

Literature study of the RHIC detectors listed on the SoLID wiki *RHIC detectors* page (https://solid.jlab.org/wiki/index.php?title=RHIC_detectors); so far STAR only. The wiki uses a **three-layer architecture**:

1. **Thematic wiki pages** in `wiki/synthesis/` — cross-cutting syntheses per detector system and topic (below). No per-paper pages. The `wiki/` root holds this `index.md`, `list.md` (flat raw-source inventory) and `log.md` (activity log).
2. **Per-source notes** `raw/<slug>-note.md` — the bridge layer: bibliographic data, key numbers, caveats; links up to thematic pages and down to the full source. Thematic pages cite these notes by relative Markdown link, never the full source directly.
3. **Full sources** `raw/<slug>.md` — full-content paraphrase of each paper, talk, email or status sheet, with equations, numbers and tables reproduced exactly and figure descriptions.

Conventions: [note] = derived or interpretive, not stated in a source; "Zhiwen, personal communication, 2026-11-09" = stated by Zhiwen, not in any source. Source counts (N) are raw/ sources.

## Thematic wiki pages (in `wiki/synthesis/`)

### Overview / Status
- [rhic-detector-status](synthesis/rhic-detector-status.md) — October 2026 STAR availability sheet (all detectors) + remaining trays: BTOF 112/120 (≈2.4 m × 21 cm), MTD 61/122 (≈90 × 55 cm), with geometric cross-checks of tray size, area and channel counts; BTOF installation history 2007–2010 (126 built, Run 8 5 trays, Run 9 94/86). (9 sources)

### Detectors
- [star-barrel-tof](synthesis/star-barrel-tof.md) — STAR barrel TOF: 120 trays (241.3 × 21.6 × 8.9 cm) × 32 MRPCs (212 × 94 × 17.9 mm) × 6 pads (3.15 cm + 0.3 cm gap ≈ 3.5 cm pitch × 6.1 cm, row across the tray), 23 040 channels, 220 µm gaps (5 or 6, open), glass 1.1/0.54 mm, NINO/HPTDC, design budget ≤ 100 ps, stop 74–82 ps; pad/√12 resolution; UT production and QA, Run 8/9 commissioning and dead channels; CTB it replaced; USTC prototype history; 112 trays remain. (9 sources)
- [star-mtd](synthesis/star-mtd.md) — STAR MTD: long-strip MRPC types A/B/C, final type B (12 strips 87 × 3.8 cm, ~100 ps, 1–2 cm), 45% coverage at |η| < 0.5, 122 trays (61 remain); muon ID (prompt fraction 6–10%, LR ε 0.81); seven cross-paper discrepancies; design takeaways. (6 sources)
- [star-bemc](synthesis/star-bemc.md) — STAR BEMC: |η| ≤ 1, 120 modules / 4800 towers, Pb/scint ≈ 20 X₀ (≈ 0.7 λ_I), gas SMD, front face r = 223.5 cm; design resolution ≈ 14%/√E ⊕ 1.5%; links to TOF and MTD absorber. (4 sources)
- [star-eemc](synthesis/star-eemc.md) — STAR EEMC: 1.086 ≤ η ≤ 2.00, 720 towers, 21.4 X₀, scintillator-strip SMD (6864 strips), pre/postshower; requirement ≤ 16%/√E + 2%; in situ, no readout. (3 sources)
- [star-fcs](synthesis/star-fcs.md) — STAR Forward Calorimeter System: as-built PHENIX-shashlik ECal (1496 towers, 18 X₀) + Fe/scint HCal (520 towers, 4.45 λ) at ≈ 7 m, 2.5 < η < 4; 2018 design proposal (front-face ECal readout, 38-layer HCal, FEE/bias specs, SiPM radiation study, 74 DEP/ADC) vs as built; status, Run-22 triggers; 2014 W/ScFi + Pb HCal prototype was a different design; open discrepancies. (6 sources)
- [star-forward-tracking](synthesis/star-forward-tracking.md) — STAR Forward Tracking System: 3 Si mini-strip disks (FST, APV25 + IST DAQ) + 4 sTGC planes (FTT); 2018 design (z = 139.9–186.5 / 273–363 cm, square modules, TPC readout) vs as built (152–179 / 300–360 cm, pentagonal modules, VMM readout); simulated performance, reconstruction, Run 22, dismounted by October 2026. (4 sources)

### Technology
- [mrpc-technology](synthesis/mrpc-technology.md) — MRPC position resolution (two-end timing along strips; pitch/√12 derivation, why x², 2D pads), rate capability vs electrode type (float glass < ~500 Hz/cm² … ceramic ~500 kHz/cm²), no photosensor, BTOF vs MTD readout electronics; STAR TOF cosmic-test methods (MaxTOT, iterative slewing, correlation), noise rates and threshold scans; external sources. (8 sources)
- [pi-mu-separation-calorimetry](synthesis/pi-mu-separation-calorimetry.md) — π/μ separation with a hadron calorimeter: discriminants, punch-through vs decay in flight, NA62/ATLAS/ePIC/second-EIC-detector cases, STAR MTD cross-check; external references. (4 sources)

### Systems
- [star-daq-trigger](synthesis/star-daq-trigger.md) — DAQ and trigger paths. BTOF readout chain TINO → TDIG → TCPU → THUB → DDL into STAR DAQ, with board internals and history (TFEE → TAMP → TINO, TFEEb → TPMT → TPMD, TMIT → THUB), HPTDC 24.41 ps arithmetic, five networks and the THUB-NW clock tree, DAQ receiver and TOF controller, Run-9 operations, STAR trigger levels, TPMD start side and timing budget; MTD Level-0 trigger inputs and dimuon trigger; MTD DAQ path not stated; forward upgrade: FCS DEP/ADC + DEP/IO three-layer trigger (2018 design), FST readout via the IST DAQ and DDL, sTGC readout plan (TPC ALTRO) vs as-built VMM; further reading (Landgraf 2003, Bieser 2003, 2013 DAQ talk). (8 sources)
- [star-magnet-absorber](synthesis/star-magnet-absorber.md) — STAR flux-return backlegs: 30 bars at 12°, 6.85 m, ≈ 61 cm thick × 57 cm wide at r = 363 cm, 1.2 / −1.26 T; absorber budget steel ≈ 3.6 λ_I + BEMC ≈ 0.7 λ_I vs papers' "about 5"; multiple scattering 10 cm / 100 ps at 2 GeV/c. (5 sources)

### Open questions
- [open-questions](synthesis/open-questions.md) — Open issues 9, 11–15, 17–25 (strip signal speed, MTD 56% coverage, Run-12 z resolution, TOF tilt angles and tray radius, MTD DAQ path, FCS discrepancies (readout end probably resolved; ECal length/λ open), EEMC SMD depth, MTD muon-ID data plateaus, 2009 MTD strip gap and hadron rejection, TOF gap count 5 vs 6, Run-9 dead-channel count, VPD distance, FCS HCal layer count, FTS as-built geometry) with next steps; #16 (TOF pad/glass) closed 2026-11-16; unverified from-memory items; scope gap. (13 sources)

## Navigation
- [list](list.md) — flat inventory of all raw sources (16), with route and ingest date.
- [log](log.md) — append-only activity log, newest first.
