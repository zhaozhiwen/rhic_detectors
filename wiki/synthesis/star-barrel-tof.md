---
title: STAR Barrel Time-of-Flight (BTOF)
tags: [experiment, detector, technology, status]
sources: [shao2002-mrpc-beam-test.md, shao2002-mrpc-beam-test-note.md, wu2007-star-barrel-tof.md, wu2007-star-barrel-tof-note.md, llope2012-star-mrpc-systems.md, llope2012-star-mrpc-systems-note.md, ruan2009-mtd-concept.md, ruan2009-mtd-concept-note.md, yang2014-mtd-cosmic-calibration.md, yang2014-mtd-cosmic-calibration-note.md, beddo2003-bemc.md, beddo2003-bemc-note.md, star2026-detector-status.md, star2026-detector-status-note.md, schambach2006-star-tof-electronics.md, schambach2006-star-tof-electronics-note.md]
updated: 2026-11-10
---

# STAR Barrel Time-of-Flight (BTOF)

MRPC-based barrel TOF of STAR: 120 trays just outside the TPC, 3840 MRPCs, 23 040 pad channels, ≈ 50 m², read by NINO/HPTDC electronics. Main sources: USTC prototype beam test [shao2002-mrpc-beam-test-note](../../raw/shao2002-mrpc-beam-test-note.md), QM2006 proceeding [wu2007-star-barrel-tof-note](../../raw/wu2007-star-barrel-tof-note.md), system overview [llope2012-star-mrpc-systems-note](../../raw/llope2012-star-mrpc-systems-note.md), 2006 electronics design paper (readout chain, MRPC/tray construction, timing budget, cosmic stand) [schambach2006-star-tof-electronics-note](../../raw/schambach2006-star-tof-electronics-note.md). As-built η range from [yang2014-mtd-cosmic-calibration-note](../../raw/yang2014-mtd-cosmic-calibration-note.md). MRPC physics (position resolution, rate, no photosensor) is on [mrpc-technology](mrpc-technology.md); DAQ chain on [star-daq-trigger](star-daq-trigger.md); current hardware on [rhic-detector-status](rhic-detector-status.md).

Conventions: [note] = derived/interpretation, not stated in a source. "Zhiwen, personal communication, 2026-11-09" = stated by Zhiwen, not in any paper.

## Final system (Llope 2012 unless marked)

| Item | Value | Comment |
|---|---|---|
| Trays | 120, two adjacent rings of 60 just outside the TPC | each tray ≈ 0.9 in η, 1/60 of φ (6°); 2006 design: two adjoining shells of 60, each ≈ 1 unit of η; Al box, 50 mil (0.13 cm) walls, welded corners, TINO boards form the lid [schambach2006-star-tof-electronics-note](../../raw/schambach2006-star-tof-electronics-note.md) |
| MRPCs | 32 per tray, "nearly projective" toward the centre of STAR → 3840 | tilt angles not given |
| Pads | 6 per MRPC, one row, **3.5 × 6.1 cm²**, read out from one edge | **contradiction:** [schambach2006-star-tof-electronics-note](../../raw/schambach2006-star-tof-electronics-note.md) prints **3.3 cm × 6.1 cm**; unresolved ([open-questions](open-questions.md) #16). Inter-pad gap, MRPC outer size and pad orientation (z vs φ) not given in either |
| Channels | **23 040** (192 per tray) | ≈ 50 m² active; 49.2 m² from 3.5 × 6.1 cm² pads, 46.4 m² from 3.3 × 6.1 cm [note] |
| η, φ, radius | \|η\| < 0.9 as built [yang2014-mtd-cosmic-calibration-note](../../raw/yang2014-mtd-cosmic-calibration-note.md); 2π; radius ~220 cm [ruan2009-mtd-concept-note](../../raw/ruan2009-mtd-concept-note.md), [yang2014-mtd-cosmic-calibration-note](../../raw/yang2014-mtd-cosmic-calibration-note.md) (not given in Llope 2012) | 2007 design said \|η\| < 1 [wu2007-star-barrel-tof-note](../../raw/wu2007-star-barrel-tof-note.md) (printed "η < 1", a [source issue]) |
| MRPC stack | single stack, 5 × 220 µm gaps; inner glass 0.54 mm float glass; outer glass 1.1 mm with graphite electrodes (10⁵ Ω/□); glass ~10¹³ Ω cm | HV ~14 kV. 2006 design [schambach2006-star-tof-electronics-note](../../raw/schambach2006-star-tof-electronics-note.md): 14 kV, outer glass **0.7 mm**, inner **0.55 mm**, 0.22 mm nylon fishing-line spacers, graphite tape 10⁵ Ω, pads 0.35 mm Mylar from the outer electrodes, gap count not given. Outer glass 0.7 vs 1.1 mm unresolved (#16) |
| Gas | 95% R-134a + 5% isobutane | same in the 2006 design, atmospheric pressure [schambach2006-star-tof-electronics-note](../../raw/schambach2006-star-tof-electronics-note.md); 2002 beam test used 90/5/5 with SF₆ [shao2002-mrpc-beam-test-note](../../raw/shao2002-mrpc-beam-test-note.md) |
| Signal | ~25 fC per hit, read directly by NINO (no photosensor) | dark rate ~1 Hz/cm² (~20 Hz/pad) |
| Electronics | TINO (3 NINO per 4 MRPCs) → TDIG (3 HPTDC, 40 MHz, 24.4 ps LSB, ToT) → TCPU (tray multiplicity to L0) → 4 THUB → DAQ | ~100 W per tray, water-cooled; per tray 8 TINO + 8 TDIG (24 ch each) + 1 TCPU, 2 data cables (96 pads each); THUBs on the magnet steel, 30 or 31 TCPUs each; HPTDC bin 24.41 ps [schambach2006-star-tof-electronics-note](../../raw/schambach2006-star-tof-electronics-note.md); details on [star-daq-trigger](star-daq-trigger.md) |
| Calibration | HPTDC INL, per-channel offsets vs start, ToT slewing | no hit-position-in-pad correction listed |
| Timing budget (2006 design) | total ≤ 100 ps after corrections = 50 ps VPD start ⊕ 30 ps corrections ⊕ stop < 80 ps | MRPC pure stop 50–70 ps with near-final prototype electronics [schambach2006-star-tof-electronics-note](../../raw/schambach2006-star-tof-electronics-note.md); √(100² − 50² − 30²) ≈ 81 ps [note] |
| Cosmic test stand (2006) | 80–110 ps overall, module to module; Fig. 3 example σ = 85.39 ± 1.96 ps | width of one module minus the mean of the others, not unfolded; ≈ 74 ps per module if 4 equal modules [note] [schambach2006-star-tof-electronics-note](../../raw/schambach2006-star-tof-electronics-note.md) |
| Timing in STAR | stop 74–82 ps for final trays; total 87 ps (Au+Au 200, start 30 ps), 111–112 ps (p+p 200, start 81–83 ps) | start, stop, total agree in quadrature to ~2 ps [note] |
| Test beam | > 95% efficiency, stop < 75 ps at 200 Hz/cm² (RHIC-II design rate) | occupancy ~12% in central Au+Au |
| Installation | 94 trays before Run 9 ("three-quarters"; abstract says "∼70 %", a [source issue]) | 94/120 = 78% [note] |

[wu2007-star-barrel-tof-note](../../raw/wu2007-star-barrel-tof-note.md) gives no construction details (no gaps, glass, pads or electronics); its hardware content is gas, HV, timing and the TOFr tray coverage.

## Position resolution: pads, √12 and inferred orientation

A pad tells only which pad fired, so σ ≈ pad size/√12 = **1.01 cm × 1.76 cm** [note] (2D combined 2.03 cm); with the 3.3 cm width of [schambach2006-star-tof-electronics-note](../../raw/schambach2006-star-tof-electronics-note.md), 3.3/√12 ≈ **0.95 cm** across [note]. Derivation of √12 and the 2D case: [mrpc-technology](mrpc-technology.md). The TPC track supplies the position at the TOF radius; the pad is used only to match a track to a hit. Small pads keep occupancy ≈ 12% in central Au+Au, so a pad rarely sees two particles [llope2012-star-mrpc-systems-note](../../raw/llope2012-star-mrpc-systems-note.md).

- Lower bounds: the final inter-pad gap is not given, so 1.01/1.76 cm assume pad size, not pitch [note].
- **Pad orientation (inferred)** [note]: six 3.5 cm pads = 21 cm (Llope 2012), which fits the 21 cm tray width (Zhiwen, personal communication, 2026-11-09) and the 22–23 cm arc per 6°; six 6.1 cm pads (36.6 cm) would not, and 32 × 36.6 cm would far exceed the tray length. The 3.3 cm width printed in [schambach2006-star-tof-electronics-note](../../raw/schambach2006-star-tof-electronics-note.md) gives 6 × 3.3 = 19.8 cm, which also fits only with the short side along φ, so the inference holds for either value (which width is right is unresolved, [open-questions](open-questions.md) #16). So pads are **3.5 (or 3.3) cm in φ (rφ) and 6.1 cm along z**; each MRPC's 6.1 cm side lies along z, consistent with ≈ 7.1–7.5 cm pitch for 32 nearly projective (tilted) MRPCs. Resolution ≈ **1.0 cm (0.95 cm if 3.3 cm) in rφ, 1.8 cm in z**. Not stated in any paper ([open-questions](open-questions.md) #13).

## Tray size

No paper gives the tray's physical dimensions ([schambach2006-star-tof-electronics-note](../../raw/schambach2006-star-tof-electronics-note.md) gives only the 50 mil Al wall). Stated values and derivations [note]:

| Quantity | Stated | Derived [note] |
|---|---|---|
| φ per tray | π/30 = 6° (TOFr, [wu2007-star-barrel-tof-note](../../raw/wu2007-star-barrel-tof-note.md)); 1/60 of 2π ([llope2012-star-mrpc-systems-note](../../raw/llope2012-star-mrpc-systems-note.md)) | arc 22.0 cm at R = 210 cm, 23.0 cm at 220 cm |
| η per tray | −1 < η < 0 (TOFr, R = 210 cm); ≈ 0.9 units (final) | length along z: 247 cm (η 0–1 at 210 cm); 226 cm (η 0–0.9 at 220 cm) |
| Radius | 210 cm (TOFr tray); ~220 cm (barrel, [ruan2009-mtd-concept-note](../../raw/ruan2009-mtd-concept-note.md), [yang2014-mtd-cosmic-calibration-note](../../raw/yang2014-mtd-cosmic-calibration-note.md)) | — |
| MRPCs per tray | 28 (TOFr); 32 (final) | pitch along z: 247/28 ≈ 8.8 cm; 226/32 ≈ 7.1 cm |
| Trays | 120, two rings of 60 | 60 × 6° = 360° per ring ✓ |
| Electronics per tray | 8 TINO, 8 TDIG, 1 TCPU, 192 channels, ~100 W, water-cooled (also [schambach2006-star-tof-electronics-note](../../raw/schambach2006-star-tof-electronics-note.md)) | 8 × 4 = 32 MRPCs ✓ |

**Tray size (Zhiwen, personal communication, 2026-11-09):** 120 trays, each ≈ **2.4 m long × 21 cm wide**. Checks [note]:
- 21 cm at R ≈ 210–220 cm subtends 5.5–5.7°, just under 6° per tray → room between neighbours ✓.
- 2.4 m lies between the derived 226 cm (η 0–0.9 at 220 cm) and 247 cm (η 0–1 at 210 cm) ✓.
- 32 MRPCs in 2.4 m → one per ≈ 7.5 cm along z ✓.
- 120 × 2.4 × 0.21 m ≈ 60 m² tray footprint vs ≈ 49 m² of pads.
- Outer limit: BEMC front face at r = 223.5 cm [beddo2003-bemc-note](../../raw/beddo2003-bemc-note.md); both systems use 60 × 6° in φ ([star-bemc](star-bemc.md)).

## Prototype history

| Stage | Pads | Stack | Timing | Source |
|---|---|---|---|---|
| USTC 6-gap prototype (CERN PS T10, 2001) | 2 × 6 pads, 3.1 × 3.0 cm², 3 mm gap | 6 × 250 µm (0.2–0.3 mm), 0.70 mm inner / 1.2 mm outer "Shanghai glass" (2.57 / 1.8 × 10¹³ Ω cm) | ~65 ps, > 97% for 15.5–17 kV | [shao2002-mrpc-beam-test-note](../../raw/shao2002-mrpc-beam-test-note.md) |
| USTC 10-gap prototype | same pads | 2 × 5 × 220 µm | 54 ps at 23.5 kV (abstract: < 55 ps) | [shao2002-mrpc-beam-test-note](../../raw/shao2002-mrpc-beam-test-note.md) |
| TOFr (Run 3), TOFr′ (Run 4) | — | final design from 2001 | stop 80–89 ps (CAMAC, long cables) | [llope2012-star-mrpc-systems-note](../../raw/llope2012-star-mrpc-systems-note.md) |
| TOFr5 (Runs 5–6) | — | — | stop 75–94 ps (on-board HPTDC) | [llope2012-star-mrpc-systems-note](../../raw/llope2012-star-mrpc-systems-note.md) |
| TOFr tray geometry | — | 28 MRPCs | π/30 in φ, −1 < η < 0, R = 210 cm | [wu2007-star-barrel-tof-note](../../raw/wu2007-star-barrel-tof-note.md) |

- Prototype pads (2 × 6, ≈ 3 × 3 cm) differ from the final layout (1 × 6, 3.5 × 6.1 cm, or 3.3 cm wide per [schambach2006-star-tof-electronics-note](../../raw/schambach2006-star-tof-electronics-note.md)); the final stack has 5 thinner gaps.
- A full-scale prototype tray with successive prototype electronics had been in STAR since the 2003 run [schambach2006-star-tof-electronics-note](../../raw/schambach2006-star-tof-electronics-note.md).
- In the 3 mm gaps between prototype pads, efficiency fell to ≈ 80% and timing to ≥ 100 ps [shao2002-mrpc-beam-test-note](../../raw/shao2002-mrpc-beam-test-note.md).
- Why MRPC: a PMT-scintillator TOF would need ≈ 25 000 fast PMTs for 64 m² (cost, magnetic field) [shao2002-mrpc-beam-test-note](../../raw/shao2002-mrpc-beam-test-note.md); see [mrpc-technology](mrpc-technology.md).
- PID reach with TOFr (200 GeV d+Au): π/K to p_T ~ 1.6 GeV/c, p/meson to ~ 3.0 GeV/c [wu2007-star-barrel-tof-note](../../raw/wu2007-star-barrel-tof-note.md).

## Availability

| Built | Remaining | Status | Source |
|---|---|---|---|
| 120 trays | **112 trays** | in situ, no readout | Zhiwen, personal communication, 2026-11-09; matches "All except 8 trays" in [star2026-detector-status-note](../../raw/star2026-detector-status-note.md) (October 2026) ✓ |

112 trays ≈ 56 m² of tray, ≈ 46 m² of pads, 21 504 channels [note]. Details: [rhic-detector-status](rhic-detector-status.md).

## Related
[mrpc-technology](mrpc-technology.md) · [star-mtd](star-mtd.md) · [star-daq-trigger](star-daq-trigger.md) · [star-bemc](star-bemc.md) · [rhic-detector-status](rhic-detector-status.md) · [open-questions](open-questions.md)
