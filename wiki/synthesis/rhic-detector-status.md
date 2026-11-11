---
title: STAR detector availability after RHIC operations (October 2026)
tags: [status, overview, detector]
sources: [star2026-detector-status.md, star2026-detector-status-note.md, llope2012-star-mrpc-systems.md, llope2012-star-mrpc-systems-note.md, wu2007-star-barrel-tof.md, wu2007-star-barrel-tof-note.md, ruan2009-mtd-concept.md, ruan2009-mtd-concept-note.md, yang2014-mtd-cosmic-calibration.md, yang2014-mtd-cosmic-calibration-note.md, huang2016-mtd-muon-id.md, huang2016-mtd-muon-id-note.md, beddo2003-bemc.md, beddo2003-bemc-note.md, schambach2006-star-tof-electronics.md, schambach2006-star-tof-electronics-note.md]
updated: 2026-11-10
---

# STAR detector availability after RHIC operations (October 2026)

Entry point for "what STAR hardware is left". Primary source: the one-page sheet "STAR Detector status as of October 2026" (author not given; PDF created 2026-10-22) [[star2026-detector-status-note]]. Remaining tray counts and tray sizes: Zhiwen, personal communication, 2026-11-09. Scope of the wiki: the RHIC detectors listed on the SoLID wiki *RHIC detectors* page (https://solid.jlab.org/wiki/index.php?title=RHIC_detectors); only STAR systems have been read so far.

## Status sheet (October 2026)

| Group | Detector | Availability | Status | Wiki page |
|---|---|---|---|---|
| Trigger | BBC | — | Disposed | — |
| Trigger | VPD | All | Radiation surveyed and stored | [[mrpc-technology]] (start time) |
| Trigger | EPD | All | Dismounted, packed, ready to be returned to Ohio | — |
| Very forward | ZDC | All | In situ | — |
| Very forward | ZDC SMD | All | Radiation surveyed and stored | — |
| Very forward | Roman pots | All | Last used in 2017; stored | — |
| Forward | Forward EMCal | All | In situ | [[star-fcs]] |
| Forward | Forward HCal | All | In situ | [[star-fcs]] |
| Forward | sTGC | All | Dismounted | [[star-fcs]] (Forward Tracking System) |
| — | Endcap EMCal | All | In situ; no readout | [[star-eemc]] |
| — | Endcap TOF | All | Dismounted, packed, ready to be returned to Germany | — |
| — | FST | One of two halves (3 layers) | Dismounted | — |
| Central | TPC | All | In situ | — |
| Central | Barrel TOF | All except 8 trays | In situ; no readout | [[star-barrel-tof]] |
| Central | MTD | Half | In situ; no readout | [[star-mtd]] |
| Central | Barrel EMCal | All | In situ; no readout | [[star-bemc]] |

## Remaining BTOF and MTD trays (Zhiwen, personal communication, 2026-11-09)

| System | Built | Tray size | Remaining | Consistency with the sheet |
|---|---|---|---|---|
| Barrel TOF | 120 trays | ≈ 2.4 m × 21 cm | **112 trays** | "All except 8 trays" ✓ |
| MTD | 122 trays | ≈ 90 × 55 cm | **61 trays** | "Half" ✓ |

## Geometric checks [note]

**BTOF** (paper values from [[llope2012-star-mrpc-systems-note]], [[wu2007-star-barrel-tof-note]]; radius ~220 cm from [[ruan2009-mtd-concept-note]], [[yang2014-mtd-cosmic-calibration-note]]):
- 120 trays = two rings of 60 × 6° ✓. 21 cm at R ≈ 210–220 cm subtends 5.5–5.7° < 6° ✓.
- 2.4 m length lies between 226 cm (η 0–0.9 at 220 cm) and 247 cm (η 0–1 at 210 cm) ✓; 32 MRPCs → ≈ 7.5 cm per MRPC along z ✓.
- Six 3.5 cm pads (21 cm) fit across the tray ⇒ pads 3.5 cm in φ, 6.1 cm along z (inferred; [[star-barrel-tof]]). [[schambach2006-star-tof-electronics-note]] prints a 3.3 cm pad width (six = 19.8 cm): same orientation; 3.3 vs 3.5 cm unresolved ([[open-questions]] #16); the pad areas below use 3.5 cm.
- Full system: 120 × 2.4 × 0.21 m ≈ 60 m² tray footprint; 49.2 m² of pads; 23 040 channels.
- **112 trays**: ≈ 56 m² of tray, ≈ 46 m² of pads (112 × 32 × 6 × 21.35 cm²), 21 504 channels (112 × 192).
- BEMC front face at r = 223.5 cm bounds the TOF trays [[beddo2003-bemc-note]].

**MTD** (paper values from [[llope2012-star-mrpc-systems-note]], [[yang2014-mtd-cosmic-calibration-note]], [[huang2016-mtd-muon-id-note]]):
- One tray holds one WMRPC (91.5 × 58 × 3 cm³ outer; type B 87 × 52 cm²) → 90 × 55 cm fits ✓.
- 122 modules: 1464 strips, 2928 channels; strip area 122 × 87 × 45.6 cm² = 48.4 m² = **45.5%** of the \|η\| < 0.5 band at 403 cm (≈ 106 m²) ✓ the quoted ~45%.
- Count consistent with ≈ 120 implied by Yang 2014 ("12 modules = 10%") and 117 planned in Llope 2012.
- Tray footprint 122 × 0.90 × 0.55 m ≈ 60 m².
- **61 trays**: ≈ 30 m² of tray, ≈ 24.2 m² of strips, 1464 channels (two ends per strip).

Which 61 MTD trays and which 8 BTOF trays are gone is not recorded in any source here.

## Related
[[star-barrel-tof]] · [[star-mtd]] · [[star-bemc]] · [[star-eemc]] · [[star-fcs]] · [[open-questions]]
