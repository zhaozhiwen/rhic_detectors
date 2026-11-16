---
title: STAR detector availability after RHIC operations (October 2026)
tags: [status, overview, detector]
sources: [star2026-detector-status.md, star2026-detector-status-note.md, llope2012-star-mrpc-systems.md, llope2012-star-mrpc-systems-note.md, wu2007-star-barrel-tof.md, wu2007-star-barrel-tof-note.md, ruan2009-mtd-concept.md, ruan2009-mtd-concept-note.md, yang2014-mtd-cosmic-calibration.md, yang2014-mtd-cosmic-calibration-note.md, huang2016-mtd-muon-id.md, huang2016-mtd-muon-id-note.md, beddo2003-bemc.md, beddo2003-bemc-note.md, schambach2006-star-tof-electronics.md, schambach2006-star-tof-electronics-note.md, kajimoto2009-star-tof-thesis.md, kajimoto2009-star-tof-thesis-note.md]
updated: 2026-11-16
---

# STAR detector availability after RHIC operations (October 2026)

Entry point for "what STAR hardware is left". Primary source: the one-page sheet "STAR Detector status as of October 2026" (author not given; PDF created 2026-10-22) [star2026-detector-status-note](../../raw/star2026-detector-status-note.md). Remaining tray counts and tray sizes: Zhiwen, personal communication, 2026-11-09. Scope of the wiki: the RHIC detectors listed on the SoLID wiki *RHIC detectors* page (https://solid.jlab.org/wiki/index.php?title=RHIC_detectors); only STAR systems have been read so far.

## Status sheet (October 2026)

| Group | Detector | Availability | Status | Wiki page |
|---|---|---|---|---|
| Trigger | BBC | — | Disposed | — |
| Trigger | VPD | All | Radiation surveyed and stored | [mrpc-technology](mrpc-technology.md) (start time) |
| Trigger | EPD | All | Dismounted, packed, ready to be returned to Ohio | — |
| Very forward | ZDC | All | In situ | — |
| Very forward | ZDC SMD | All | Radiation surveyed and stored | — |
| Very forward | Roman pots | All | Last used in 2017; stored | — |
| Forward | Forward EMCal | All | In situ | [star-fcs](star-fcs.md) |
| Forward | Forward HCal | All | In situ | [star-fcs](star-fcs.md) |
| Forward | sTGC | All | Dismounted | [star-forward-tracking](star-forward-tracking.md) |
| — | Endcap EMCal | All | In situ; no readout | [star-eemc](star-eemc.md) |
| — | Endcap TOF | All | Dismounted, packed, ready to be returned to Germany | — |
| — | FST | One of two halves (3 layers) | Dismounted | [star-forward-tracking](star-forward-tracking.md) |
| Central | TPC | All | In situ | — |
| Central | Barrel TOF | All except 8 trays | In situ; no readout | [star-barrel-tof](star-barrel-tof.md) |
| Central | MTD | Half | In situ; no readout | [star-mtd](star-mtd.md) |
| Central | Barrel EMCal | All | In situ; no readout | [star-bemc](star-bemc.md) |

## Remaining BTOF and MTD trays (Zhiwen, personal communication, 2026-11-09)

| System | Built | Tray size | Remaining | Consistency with the sheet |
|---|---|---|---|---|
| Barrel TOF | 120 trays (126 built incl. 6 spares) | ≈ 2.4 m × 21 cm (as built 241.3 × 21.6 × 8.9 cm [kajimoto2009-star-tof-thesis-note](../../raw/kajimoto2009-star-tof-thesis-note.md)) | **112 trays** | "All except 8 trays" ✓ |
| MTD | 122 trays | ≈ 90 × 55 cm | **61 trays** | "Half" ✓ |

## BTOF installation history (2007–2010) [kajimoto2009-star-tof-thesis-note](../../raw/kajimoto2009-star-tof-thesis-note.md)

| Date | Trays | Note |
|---|---|---|
| Production (to August 7, 2009) | 126 assembled at UT (120 + 6 spares), 122 with production electronics | A–C and 121–123 on a prototype aluminium body |
| Oct 2007 – Jul 2009 | 125 shipped to BNL in 5 shipments | Tray 6 shipped twice |
| Run 8 (2008) | 5 trays (4.2 %), positions 76–80 | 2 dead channels of 960 |
| Run 9 (2009) | 94 installed (78 %), 86 active (71.7 %) | positions 1–12, 15–41, 44–72, 75–78, 97–101, 104–120; 13, 14, 42, 43, 73, 74, 102, 103 blocked by TPC supports |
| Before Run 10 | all 120 | planned in the thesis; done per [llope2012-star-mrpc-systems-note](../../raw/llope2012-star-mrpc-systems-note.md) |

[note] The 8 positions left empty in 2009 and the 8 trays missing in October 2026 have the same count only; no source connects them, and which 8 trays are gone in 2026 is not recorded.

## Geometric checks [note]

**BTOF** (paper values from [llope2012-star-mrpc-systems-note](../../raw/llope2012-star-mrpc-systems-note.md), [wu2007-star-barrel-tof-note](../../raw/wu2007-star-barrel-tof-note.md); radius ~220 cm from [ruan2009-mtd-concept-note](../../raw/ruan2009-mtd-concept-note.md), [yang2014-mtd-cosmic-calibration-note](../../raw/yang2014-mtd-cosmic-calibration-note.md)):
- 120 trays = two rings of 60 × 6° ✓. 21 cm at R ≈ 210–220 cm subtends 5.5–5.7° < 6° ✓.
- 2.4 m length lies between 226 cm (η 0–0.9 at 220 cm) and 247 cm (η 0–1 at 210 cm) ✓; 32 MRPCs → ≈ 7.5 cm per MRPC along z ✓.
- Pad row across the tray (stated in [kajimoto2009-star-tof-thesis-note](../../raw/kajimoto2009-star-tof-thesis-note.md)): pads ≈ 3.5 cm pitch (3.15 cm copper + 0.3 cm gap) in φ, 6.1 cm along z; six pads span 20.4 cm on a 21.0 cm board in a 21.6 cm tray ([star-barrel-tof](star-barrel-tof.md); [open-questions](open-questions.md) #16 closed). The pad areas below use Llope's 3.5 × 6.1 cm² (≈ pitch × length).
- Full system: 120 × 2.4 × 0.21 m ≈ 60 m² tray footprint; 49.2 m² of pads; 23 040 channels.
- **112 trays**: ≈ 56 m² of tray, ≈ 46 m² of pads (112 × 32 × 6 × 21.35 cm²), 21 504 channels (112 × 192).
- BEMC front face at r = 223.5 cm bounds the TOF trays [beddo2003-bemc-note](../../raw/beddo2003-bemc-note.md).

**MTD** (paper values from [llope2012-star-mrpc-systems-note](../../raw/llope2012-star-mrpc-systems-note.md), [yang2014-mtd-cosmic-calibration-note](../../raw/yang2014-mtd-cosmic-calibration-note.md), [huang2016-mtd-muon-id-note](../../raw/huang2016-mtd-muon-id-note.md)):
- One tray holds one WMRPC (91.5 × 58 × 3 cm³ outer; type B 87 × 52 cm²) → 90 × 55 cm fits ✓.
- 122 modules: 1464 strips, 2928 channels; strip area 122 × 87 × 45.6 cm² = 48.4 m² = **45.5%** of the \|η\| < 0.5 band at 403 cm (≈ 106 m²) ✓ the quoted ~45%.
- Count consistent with ≈ 120 implied by Yang 2014 ("12 modules = 10%") and 117 planned in Llope 2012.
- Tray footprint 122 × 0.90 × 0.55 m ≈ 60 m².
- **61 trays**: ≈ 30 m² of tray, ≈ 24.2 m² of strips, 1464 channels (two ends per strip).

Which 61 MTD trays and which 8 BTOF trays are gone is not recorded in any source here.

## Related
[star-barrel-tof](star-barrel-tof.md) · [star-mtd](star-mtd.md) · [star-bemc](star-bemc.md) · [star-eemc](star-eemc.md) · [star-fcs](star-fcs.md) · [star-forward-tracking](star-forward-tracking.md) · [open-questions](open-questions.md)
