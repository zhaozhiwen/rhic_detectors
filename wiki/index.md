---
title: index — RHIC detectors
type: index
updated: 2026-11-10
---

# index — RHIC detectors

*Read this first on every query. LLM-maintained catalog of all wiki pages.*

Literature study of the RHIC detectors listed on the SoLID wiki *RHIC detectors* page (https://solid.jlab.org/wiki/index.php?title=RHIC_detectors); so far STAR only. The wiki uses a **three-layer architecture**:

1. **Thematic wiki pages** in `wiki/synthesis/` — cross-cutting syntheses per detector system and topic (below). No per-paper pages. The `wiki/` root holds this `index.md`, `list.md` (flat raw-source inventory) and `log.md` (activity log).
2. **Per-source notes** `raw/<slug>-note.md` — the bridge layer: bibliographic data, key numbers, caveats; links up to thematic pages and down to the full source. Thematic pages cite these notes by wikilink, never the full source directly.
3. **Full sources** `raw/<slug>.md` — full-content paraphrase of each paper, talk, email or status sheet, with equations, numbers and tables reproduced exactly and figure descriptions.

Conventions: [note] = derived or interpretive, not stated in a source; "Zhiwen, personal communication, 2026-11-09" = stated by Zhiwen, not in any source. Source counts (N) are raw/ sources.

## Thematic wiki pages (in `wiki/synthesis/`)

### Overview / Status
- [[rhic-detector-status]] — October 2026 STAR availability sheet (all detectors) + remaining trays: BTOF 112/120 (≈2.4 m × 21 cm), MTD 61/122 (≈90 × 55 cm), with geometric cross-checks of tray size, area and channel counts. (8 sources)

### Detectors
- [[star-barrel-tof]] — STAR barrel TOF: 120 trays × 32 MRPCs × 6 pads (3.5 × 6.1 cm²; 3.3 cm wide in a 2006 design paper, unresolved), 23 040 channels, 5 × 220 µm gaps, NINO/HPTDC, design budget ≤ 100 ps, stop 74–82 ps; pad/√12 resolution and inferred pad orientation; tray size; USTC prototype history; 112 trays remain. (8 sources)
- [[star-mtd]] — STAR MTD: long-strip MRPC types A/B/C, final type B (12 strips 87 × 3.8 cm, ~100 ps, 1–2 cm), 45% coverage at |η| < 0.5, 122 trays (61 remain); muon ID (prompt fraction 6–10%, LR ε 0.81); seven cross-paper discrepancies; design takeaways. (6 sources)
- [[star-bemc]] — STAR BEMC: |η| ≤ 1, 120 modules / 4800 towers, Pb/scint ≈ 20 X₀ (≈ 0.7 λ_I), gas SMD, front face r = 223.5 cm; design resolution ≈ 14%/√E ⊕ 1.5%; links to TOF and MTD absorber. (4 sources)
- [[star-eemc]] — STAR EEMC: 1.086 ≤ η ≤ 2.00, 720 towers, 21.4 X₀, scintillator-strip SMD (6864 strips), pre/postshower; requirement ≤ 16%/√E + 2%; in situ, no readout. (3 sources)
- [[star-fcs]] — STAR Forward Calorimeter System: as-built PHENIX-shashlik ECal (1496 towers, 18 X₀) + Fe/scint HCal (520 towers, 4.45 λ) at ≈ 7 m, 2.5 < η < 4; status, Run-22 triggers; 2014 W/ScFi + Pb HCal prototype was a different design; open discrepancies. (5 sources)

### Technology
- [[mrpc-technology]] — MRPC position resolution (two-end timing along strips; pitch/√12 derivation, why x², 2D pads), rate capability vs electrode type (float glass < ~500 Hz/cm² … ceramic ~500 kHz/cm²), no photosensor, BTOF vs MTD readout electronics; external sources. (7 sources)
- [[pi-mu-separation-calorimetry]] — π/μ separation with a hadron calorimeter: discriminants, punch-through vs decay in flight, NA62/ATLAS/ePIC/second-EIC-detector cases, STAR MTD cross-check; external references. (4 sources)

### Systems
- [[star-daq-trigger]] — BTOF readout chain TINO → TDIG → TCPU → THUB → DDL into STAR DAQ, with board internals, HPTDC 24.41 ps arithmetic, TPMD start side and timing budget; MTD Level-0 trigger inputs and dimuon trigger; MTD DAQ path not stated; further reading (Landgraf 2003, Bieser 2003, 2013 DAQ talk). (6 sources)
- [[star-magnet-absorber]] — STAR flux-return backlegs: 30 bars at 12°, 6.85 m, ≈ 61 cm thick × 57 cm wide at r = 363 cm, 1.2 / −1.26 T; absorber budget steel ≈ 3.6 λ_I + BEMC ≈ 0.7 λ_I vs papers' "about 5"; multiple scattering 10 cm / 100 ps at 2 GeV/c. (5 sources)

### Open questions
- [[open-questions]] — Open issues 9, 11–16 (strip signal speed, MTD 56% coverage, Run-12 z resolution, TOF construction details, MTD DAQ path, FCS discrepancies, TOF pad/glass dimensions 3.3 vs 3.5 cm) with next steps; unverified from-memory items; scope gap. (10 sources)

## Navigation
- [[list]] — flat inventory of all raw sources (14), with route and ingest date.
- [[log]] — append-only activity log, newest first.
