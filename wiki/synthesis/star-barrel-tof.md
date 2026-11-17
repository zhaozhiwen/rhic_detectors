---
title: STAR Barrel Time-of-Flight (BTOF)
tags: [experiment, detector, technology, status]
sources: [shao2002-mrpc-beam-test.md, shao2002-mrpc-beam-test-note.md, wu2007-star-barrel-tof.md, wu2007-star-barrel-tof-note.md, llope2012-star-mrpc-systems.md, llope2012-star-mrpc-systems-note.md, ruan2009-mtd-concept.md, ruan2009-mtd-concept-note.md, yang2014-mtd-cosmic-calibration.md, yang2014-mtd-cosmic-calibration-note.md, beddo2003-bemc.md, beddo2003-bemc-note.md, star2026-detector-status.md, star2026-detector-status-note.md, schambach2006-star-tof-electronics.md, schambach2006-star-tof-electronics-note.md, kajimoto2009-star-tof-thesis.md, kajimoto2009-star-tof-thesis-note.md]
updated: 2026-11-17
---

# STAR Barrel Time-of-Flight (BTOF)

MRPC-based barrel TOF of STAR: 120 trays just outside the TPC, 3840 MRPCs, 23 040 pad channels, 50 m² (Llope 2012), read by NINO/HPTDC electronics. Main sources: USTC prototype beam test [shao2002-mrpc-beam-test-note](../../raw/shao2002-mrpc-beam-test-note.md), QM2006 proceeding [wu2007-star-barrel-tof-note](../../raw/wu2007-star-barrel-tof-note.md), system overview [llope2012-star-mrpc-systems-note](../../raw/llope2012-star-mrpc-systems-note.md), 2006 electronics design paper (readout chain, MRPC/tray construction, timing budget, cosmic stand) [schambach2006-star-tof-electronics-note](../../raw/schambach2006-star-tof-electronics-note.md), 2009 UT Austin PhD thesis on the construction (tray and MRPC dimensions, module and tray QA, board history, production statistics, Run 8/9 commissioning) [kajimoto2009-star-tof-thesis-note](../../raw/kajimoto2009-star-tof-thesis-note.md). As-built η range from [yang2014-mtd-cosmic-calibration-note](../../raw/yang2014-mtd-cosmic-calibration-note.md). MRPC physics (position resolution, rate, no photosensor) is on [mrpc-technology](mrpc-technology.md); DAQ chain on [star-daq-trigger](star-daq-trigger.md); current hardware on [rhic-detector-status](rhic-detector-status.md).

Conventions: [note] = derived/interpretation, not stated in a source. "Zhiwen, personal communication, 2026-11-09" = stated by Zhiwen, not in any paper.

## Final system (Llope 2012 unless marked)

| Item | Value | Comment |
|---|---|---|
| Trays | 120, two adjacent rings of 60 just outside the TPC | each tray ≈ 0.9 in η, 1/60 of φ (6°); 2006 design: two adjoining shells of 60, each ≈ 1 unit of η; Al box, 50 mil (0.13 cm) walls, welded corners, TINO boards form the lid [schambach2006-star-tof-electronics-note](../../raw/schambach2006-star-tof-electronics-note.md); as-built box **95" (241.3 cm) × 8.5" (21.6 cm) × 3.5" (8.9 cm)**, gas-tight with flowing R134a, 32 MRPCs inside and 17 boards outside, one unit of η per tray (−1 < η < 0 or 0 < η < 1) [kajimoto2009-star-tof-thesis-note](../../raw/kajimoto2009-star-tof-thesis-note.md) |
| MRPCs | 32 per tray, "nearly projective" toward the centre of STAR → 3840 | tilt angles not given; module outer size **212.0 × 94.0 × 17.9 mm** nominal (tolerance ±0.5, ±0.5, ±1.0 mm), measured mean 211.94 × 94.04 × 18.21 mm; built at Tsinghua and USTC [kajimoto2009-star-tof-thesis-note](../../raw/kajimoto2009-star-tof-thesis-note.md) |
| Pads | 6 per MRPC, one row, **3.5 × 6.1 cm²**, read out from one edge | [kajimoto2009-star-tof-thesis-note](../../raw/kajimoto2009-star-tof-thesis-note.md) (Fig. 3.4, reproduced from the 2004 TOF proposal): **pad width 3.15 cm, pad interval 0.3 cm** (pitch 3.45 cm [note]); its Eq. 4.2 uses 6.1 × 3.1 (printed in mm, a [source issue]); the pad row runs across the tray (§5.3.2). Llope's 3.5 cm matches the 3.45 cm pitch to rounding [note]; the **3.3 cm** of [schambach2006-star-tof-electronics-note](../../raw/schambach2006-star-tof-electronics-note.md) matches neither and is unexplained ([open-questions](open-questions.md) #16, closed 2026-11-16) |
| Channels | **23 040** (192 per tray) | 50 m² active (Llope 2012; no "≈" printed); 49.2 m² from 3.5 × 6.1 cm² pads, 46.4 m² from 3.3 × 6.1 cm, 44.3 m² from 3.15 × 6.1 cm [note] |
| η, φ, radius | \|η\| < 0.9 as built [yang2014-mtd-cosmic-calibration-note](../../raw/yang2014-mtd-cosmic-calibration-note.md); 2π; radius ~220 cm [ruan2009-mtd-concept-note](../../raw/ruan2009-mtd-concept-note.md), [yang2014-mtd-cosmic-calibration-note](../../raw/yang2014-mtd-cosmic-calibration-note.md) (not given in Llope 2012) | 2007 design said \|η\| < 1 [wu2007-star-barrel-tof-note](../../raw/wu2007-star-barrel-tof-note.md) (printed "η < 1", a [source issue]) |
| MRPC stack | single stack, 5 × 220 µm gaps (6 per [kajimoto2009-star-tof-thesis-note](../../raw/kajimoto2009-star-tof-thesis-note.md), #21); inner glass 0.54 mm float glass; outer glass 1.1 mm with graphite electrodes (10⁵ Ω/□); glass ~10¹³ Ω cm | HV ~14 kV. 2006 design [schambach2006-star-tof-electronics-note](../../raw/schambach2006-star-tof-electronics-note.md): 14 kV, outer glass **0.7 mm**, inner **0.55 mm**, 0.22 mm nylon fishing-line spacers, graphite tape 10⁵ Ω, pads 0.35 mm Mylar from the outer electrodes, gap count not given. [kajimoto2009-star-tof-thesis-note](../../raw/kajimoto2009-star-tof-thesis-note.md) (Fig. 3.4 from the 2004 proposal): outer glass 1.1 mm, inner 0.54 mm, 220 µm gaps, 0.35 mm Mylar, 1.5 mm PCB, 4 mm honeycomb ⇒ glass agrees with Llope 2012, the 2006 values 0.7/0.55 mm stand alone (#16 closed). **Gap count:** thesis stack of 5 inner + 2 outer glass plates ⇒ 6 gaps [note] vs "five gaps" in Llope 2012 (open, [open-questions](open-questions.md) #21) |
| Gas | 95% R-134a + 5% isobutane | same in the 2006 design, atmospheric pressure [schambach2006-star-tof-electronics-note](../../raw/schambach2006-star-tof-electronics-note.md); 2002 beam test used 90/5/5 with SF₆ [shao2002-mrpc-beam-test-note](../../raw/shao2002-mrpc-beam-test-note.md) |
| Signal | ~25 fC per hit, read directly by NINO (no photosensor) | dark rate ~1 Hz/cm² (~20 Hz/pad) |
| Electronics | TINO (3 NINO per 4 MRPCs) → TDIG (3 HPTDC, 40 MHz, 24.4 ps LSB, ToT) → TCPU (tray multiplicity to L0) → 4 THUB → DAQ | ~100 W per tray, water-cooled; per tray 8 TINO + 8 TDIG (24 ch each) + 1 TCPU, 2 data cables (96 pads each); THUBs on the magnet steel, 30 or 31 TCPUs each; HPTDC bin 24.41 ps [schambach2006-star-tof-electronics-note](../../raw/schambach2006-star-tof-electronics-note.md); board history TFEE → TAMP → TINO, TFEEb → TPMT → TPMD, TMIT → THUB [kajimoto2009-star-tof-thesis-note](../../raw/kajimoto2009-star-tof-thesis-note.md); details on [star-daq-trigger](star-daq-trigger.md) |
| Calibration | HPTDC INL, per-channel offsets vs start, ToT slewing | no hit-position-in-pad correction listed |
| Timing budget (2006 design) | total ≤ 100 ps after corrections = 50 ps VPD start ⊕ 30 ps corrections ⊕ stop < 80 ps | MRPC pure stop 50–70 ps with near-final prototype electronics [schambach2006-star-tof-electronics-note](../../raw/schambach2006-star-tof-electronics-note.md); √(100² − 50² − 30²) ≈ 81 ps [note] |
| Cosmic test stand (2006) | 80–110 ps overall, module to module; Fig. 3 example σ = 85.39 ± 1.96 ps | width of one module minus the mean of the others, not unfolded; ≈ 74 ps per module if 4 equal modules [note] [schambach2006-star-tof-electronics-note](../../raw/schambach2006-star-tof-electronics-note.md) |
| Cosmic tests at UT (2003–2009) | 2003 small box: 86 ps (pad 4) and 90 ps (pad 2) per pad after slewing correction; 2007 "submarine": module TM0320 74.4 ps over all pads (pads 65.1–94.2 ps); tray stands: mean 238.6 ps over 120 trays without slewing correction | widths are differences against the other pads in the stack, not unfolded; tray widths also include the large vertical spacing of the trays [kajimoto2009-star-tof-thesis-note](../../raw/kajimoto2009-star-tof-thesis-note.md); methods on [mrpc-technology](mrpc-technology.md) |
| Timing in STAR | stop 74–82 ps for final trays; total 87 ps (Au+Au 200, start 30 ps), 111–112 ps (p+p 200, start 81–83 ps) | start, stop, total agree in quadrature to ~2 ps [note] |
| Test beam | > 95% efficiency, stop < 75 ps at 200 Hz/cm² (RHIC-II design rate) | occupancy ~12% in central Au+Au |
| Installation | 94 trays before Run 9 ("three-quarters"; abstract says "∼70 %", a [source issue]) | 94/120 = 78% [note]. [kajimoto2009-star-tof-thesis-note](../../raw/kajimoto2009-star-tof-thesis-note.md): Run 8 5 trays (positions 76–80); Run 9 94 installed (78 %), 86 active (71.7 %); details below |

[wu2007-star-barrel-tof-note](../../raw/wu2007-star-barrel-tof-note.md) gives no construction details (no gaps, glass, pads or electronics); its hardware content is gas, HV, timing and the TOFr tray coverage.

## Position resolution: pads, √12 and orientation

A pad tells only which pad fired, so σ ≈ pad size/√12 = **1.01 cm × 1.76 cm** for 3.5 × 6.1 cm² [note] (2D combined 2.03 cm). With the thesis layout [kajimoto2009-star-tof-thesis-note](../../raw/kajimoto2009-star-tof-thesis-note.md) (3.15 cm pads, 0.3 cm interval): pitch 3.45/√12 ≈ **1.00 cm**, pad 3.15/√12 ≈ 0.91 cm across [note]; the 3.3 cm of [schambach2006-star-tof-electronics-note](../../raw/schambach2006-star-tof-electronics-note.md) would give 0.95 cm. Derivation of √12 and the 2D case: [mrpc-technology](mrpc-technology.md). The TPC track supplies the position at the TOF radius; the pad is used only to match a track to a hit. Small pads keep occupancy ≈ 12% in central Au+Au, so a pad rarely sees two particles [llope2012-star-mrpc-systems-note](../../raw/llope2012-star-mrpc-systems-note.md).

- Pad vs pitch: across the pads the gap is 0.3 cm (2004-proposal drawing in the thesis), so Llope's 3.5 cm ≈ the 3.45 cm pitch and 1.0 cm is a pitch-based value; along z no gap applies (one pad per module in z) [note] and 6.1 cm is the length used in the thesis Eq. 4.2; the Fig. 3.4 axis puts the pad copper at 1.1–7.4 cm (6.3 cm) along the module's 9.4 cm short side [note, figure-read].
- **Pad orientation (stated):** [kajimoto2009-star-tof-thesis-note](../../raw/kajimoto2009-star-tof-thesis-note.md) §5.3.2: the 6 pads of each module are aligned perpendicular to the tray's long side, so the row of pads runs across the tray. With a 21.0 cm board (212 mm module) inside the 21.6 cm wide tray, the **3.15 cm (pitch 3.45 cm) side lies along φ and the ≈ 6.1 cm side along z** [note]. This confirms the earlier inference from the tray width (21 cm, Zhiwen, personal communication, 2026-11-09): six 6.1 cm pads (36.6 cm) could not fit across, and 32 modules at ≈ 7.5 cm pitch along z fit 2.4 m. Resolution ≈ **1.0 cm in rφ, 1.8 cm in z** [note]. MRPC tilt angles are still not given in any source ([open-questions](open-questions.md) #13).

## Tray size

As built ([kajimoto2009-star-tof-thesis-note](../../raw/kajimoto2009-star-tof-thesis-note.md) §3.1): tray box **95" (241.3 cm) long × 8.5" (21.6 cm) wide × 3.5" (8.9 cm) high**, almost the CTB tray shape; [schambach2006-star-tof-electronics-note](../../raw/schambach2006-star-tof-electronics-note.md) adds the 50 mil Al wall. Other stated values and derivations [note]:

| Quantity | Stated | Derived [note] |
|---|---|---|
| φ per tray | π/30 = 6° (TOFr, [wu2007-star-barrel-tof-note](../../raw/wu2007-star-barrel-tof-note.md)); 1/60 of 2π ([llope2012-star-mrpc-systems-note](../../raw/llope2012-star-mrpc-systems-note.md)) | arc 22.0 cm at R = 210 cm, 23.0 cm at 220 cm |
| η per tray | −1 < η < 0 (TOFr, R = 210 cm); ≈ 0.9 units (final) | length along z: 247 cm (η 0–1 at 210 cm); 226 cm (η 0–0.9 at 220 cm) |
| Radius | 210 cm (TOFr tray); ~220 cm (barrel, [ruan2009-mtd-concept-note](../../raw/ruan2009-mtd-concept-note.md), [yang2014-mtd-cosmic-calibration-note](../../raw/yang2014-mtd-cosmic-calibration-note.md)) | — |
| MRPCs per tray | 28 (TOFr); 32 (final) | pitch along z: 247/28 ≈ 8.8 cm; 226/32 ≈ 7.1 cm |
| Trays | 120, two rings of 60 | 60 × 6° = 360° per ring ✓ |
| Electronics per tray | 8 TINO, 8 TDIG, 1 TCPU, 192 channels, ~100 W, water-cooled (also [schambach2006-star-tof-electronics-note](../../raw/schambach2006-star-tof-electronics-note.md)) | 8 × 4 = 32 MRPCs ✓ |

**Tray size (Zhiwen, personal communication, 2026-11-09):** 120 trays, each ≈ **2.4 m long × 21 cm wide** — agrees with the thesis box, 241.3 × 21.6 cm [kajimoto2009-star-tof-thesis-note](../../raw/kajimoto2009-star-tof-thesis-note.md). Checks [note]:
- 21 cm at R ≈ 210–220 cm subtends 5.5–5.7°, just under 6° per tray → room between neighbours ✓.
- 2.4 m lies between the derived 226 cm (η 0–0.9 at 220 cm) and 247 cm (η 0–1 at 210 cm) ✓.
- 32 MRPCs in 2.4 m → one per ≈ 7.5 cm along z ✓.
- 120 × 2.4 × 0.21 m ≈ 60 m² tray footprint vs ≈ 49 m² of pads.
- Outer limit: BEMC front face at r = 223.5 cm [beddo2003-bemc-note](../../raw/beddo2003-bemc-note.md); both systems use 60 × 6° in φ ([star-bemc](star-bemc.md)).

## Material budget (radiation lengths) [note]

No source quotes an X₀ for the MRPC or the tray. The numbers below are **our estimate** (2026-11-17) from the published layer stack ([kajimoto2009-star-tof-thesis-note](../../raw/kajimoto2009-star-tof-thesis-note.md), Fig. 3.4; glass thicknesses also in [llope2012-star-mrpc-systems-note](../../raw/llope2012-star-mrpc-systems-note.md)) with standard radiation lengths; treat them as ±~1% X₀.

| Layer (one MRPC module) | Thickness | X₀ used | % X₀ |
|---|---|---|---|
| Glass: 2 outer × 1.1 mm + 5 inner × 0.54 mm | 4.9 mm | ≈ 10.6 cm (soda-lime float glass, estimated from composition) | 4.6 |
| Readout PCBs (FR4): 2 × 1.5 mm | 3.0 mm | 19.4 cm (G10) | 1.5 |
| Copper pads (thickness not given; 35 µm/board, ~60% coverage assumed) | ~0.04–0.07 mm | 1.44 cm | 0.3–0.5 |
| Mylar: 2 × 0.35 mm | 0.7 mm | 28.5 cm | 0.25 |
| Honeycomb: 2 × 4 mm (Nomex-type, ~0.05 g/cm³ assumed) | 8 mm | — | ~0.1 |
| Gas gaps 6 × 0.22 mm, graphite tape | 1.3 mm | — | ~0 |
| **MRPC module total** | **17.9 mm** | | **≈ 7** |

- The layers add up to 17.9 mm, the module thickness specified and measured in UT QA ([kajimoto2009-star-tof-thesis-note](../../raw/kajimoto2009-star-tof-thesis-note.md), Table 4.1), so the stack is complete.
- Glass dominates (about two-thirds of the module's X₀).
- **Comparison:** 5 cm of plastic scintillator (PVT, X₀ ≈ 42.5 cm) is ≈ 11.8% X₀; one MRPC module ≈ 0.6 of that, i.e. the material of ≈ 3 cm of plastic.
- **Whole tray (rough):** add the 50 mil (1.27 mm) aluminium floor ≈ 1.4% X₀ and the 1/8" FR4 TINO lid ≈ 1.6% X₀ ([schambach2006-star-tof-electronics-note](../../raw/schambach2006-star-tof-electronics-note.md)), plus TDIG boards, cooling loop and cables (not quantified) → roughly ≥ 10% X₀ for material in front of the BEMC.
- **Angle:** the MRPCs are tilted to be nearly projective, so the module is crossed close to normal incidence; the flat tray floor and lid are crossed at 1/sin θ (≈ 1.5× at |η| = 1).
- Unknowns that move the total by a few tenths of a percent: copper thickness, honeycomb type, exact glass composition. A STAR GEANT geometry file or a TOF material note would settle them ([open-questions](open-questions.md)).

## Prototype history

| Stage | Pads | Stack | Timing | Source |
|---|---|---|---|---|
| USTC 6-gap prototype (CERN PS T10, 2001) | 2 × 6 pads, 3.1 × 3.0 cm², 3 mm gap | 6 × 250 µm (0.2–0.3 mm), 0.70 mm inner / 1.2 mm outer "Shanghai glass" (2.57 / 1.8 × 10¹³ Ω cm) | ~65 ps, > 97% for 15.5–17 kV | [shao2002-mrpc-beam-test-note](../../raw/shao2002-mrpc-beam-test-note.md) |
| USTC 10-gap prototype | same pads | 2 × 5 × 220 µm | 54 ps at 23.5 kV (abstract: < 55 ps) | [shao2002-mrpc-beam-test-note](../../raw/shao2002-mrpc-beam-test-note.md) |
| TOFr (Run 3), TOFr′ (Run 4) | — | final design from 2001 | stop 80–89 ps (CAMAC, long cables) | [llope2012-star-mrpc-systems-note](../../raw/llope2012-star-mrpc-systems-note.md) |
| TOFr5 (Runs 5–6) | — | — | stop 75–94 ps (on-board HPTDC) | [llope2012-star-mrpc-systems-note](../../raw/llope2012-star-mrpc-systems-note.md) |
| TOFr tray geometry | — | 28 MRPCs | π/30 in φ, −1 < η < 0, R = 210 cm | [wu2007-star-barrel-tof-note](../../raw/wu2007-star-barrel-tof-note.md) |

- Prototype pads (2 × 6, ≈ 3 × 3 cm) differ from the final layout (1 × 6, 3.15 cm pads at 3.45 cm pitch × 6.1 cm, [kajimoto2009-star-tof-thesis-note](../../raw/kajimoto2009-star-tof-thesis-note.md); 3.5 × 6.1 cm in Llope 2012); the final stack has thinner 220 µm gaps (5 per Llope 2012, 6 per the thesis, #21).
- A full-scale prototype tray with successive prototype electronics had been in STAR since the 2003 run [schambach2006-star-tof-electronics-note](../../raw/schambach2006-star-tof-electronics-note.md); prototype trays were tested at the AGS and at RHIC from 2001, TOFr read by a 6-channel TFEE prototype [kajimoto2009-star-tof-thesis-note](../../raw/kajimoto2009-star-tof-thesis-note.md).
- In the 3 mm gaps between prototype pads, efficiency fell to ≈ 80% and timing to ≥ 100 ps [shao2002-mrpc-beam-test-note](../../raw/shao2002-mrpc-beam-test-note.md).
- Why MRPC: a PMT-scintillator TOF would need ≈ 25 000 fast PMTs for 64 m² (cost, magnetic field) [shao2002-mrpc-beam-test-note](../../raw/shao2002-mrpc-beam-test-note.md); see [mrpc-technology](mrpc-technology.md).
- PID reach with TOFr (200 GeV d+Au): π/K to p_T ~ 1.6 GeV/c, p/meson to ~ 3.0 GeV/c [wu2007-star-barrel-tof-note](../../raw/wu2007-star-barrel-tof-note.md).

## Production and QA (UT Austin, 2006–2009) [kajimoto2009-star-tof-thesis-note](../../raw/kajimoto2009-star-tof-thesis-note.md)

All production trays were assembled and tested at UT Austin; MRPCs from Tsinghua (TM) and USTC (UM), TINO from Rice, TDIG/TCPU from Blue Sky Electronics (TDIG INL tables made at Rice), Al tray boxes from Oaks Precision Fabricating (126 sets).

| Step | Numbers |
|---|---|
| MRPC size check (summer 2006; TM001-090, UM001-040) | spec 212.0 × 94.0 × 17.9 mm; measured 211.94 (σ 0.101) × 94.04 (σ 0.062) × 18.21 (σ 0.141) mm; later batches with jigs |
| Signal-cable test | 12 twisted pairs per module into a 34-pin connector; PIC16F913 + MAX306 tester (Dec 2006 – Jan 2007) |
| MRPC HV test | 682 modules (July 16 – October 11, 2007), 3 could not hold HV (TM0101, TM0107, TM0151) |
| MRPC cosmic stands | "small" box (2003–04), "big" box (2004 – Oct 2007; about 197 modules, > 6000 h), "submarine" (32 modules, CTB-tray trigger) |
| Tray assembly | 10-step checklist; DC430 sealant cured ~1 week; cooling loop clamped between TINO and TDIG at 4.5 inch-pounds |
| Leak tests | cooling loop N₂ 200 psi under water, 2 h; tray gas pressure stable ≥ 1 day, freon sniffer silent |
| Tray noise | 126 trays = 24192 channels at 2500 mV; mean 7.37 Hz (Fig. 5.13); spec 50 Hz; 101 channels (0.417 %) above, in 10 trays; peripheral pads noisier; HV and cable mistakes found on trays 8 and 22 |
| Tray cosmics | 120 of 126 trays (A, 1–5 untested); mean 238.6 ps per channel without slewing correction; first 12 trays unreliable |
| Final check at BNL (WAH) | noise rates and HV currents on a 30-tray stand |

## Commissioning: Runs 8 and 9 [kajimoto2009-star-tof-thesis-note](../../raw/kajimoto2009-star-tof-thesis-note.md)

| | Run 8 (2008) | Run 9 (Jan 16 – Jul 4, 2009) |
|---|---|---|
| Trays | 5 (4.2 %), positions 76–80 | 94 installed (78 %), 86 active (71.7 %) |
| Positions | 76–80 | 1–12, 15–41, 44–72, 75–78, 97–101, 104–120; 13, 14, 42, 43, 73, 74, 102, 103 blocked by TPC support structures |
| Dead channels | 2 of 960 | 9 (Table 6.6: 6 on position 4, 1 each on 10, 60, 76) or 10 of 16,512 (§7.1); printed totals inconsistent (see note) |
| Live channels per tray | requirement > 175, met by every tray; printed averages 195.60 / 195.88 exceed 192, presumably 191.60 / 191.88 [note] | |

- Non-working Run-9 trays and causes: positions 38, 39 (no LV connection), 52 (HV cables not mated), 75 (bad TCPU), 47, 68, 112, 118 (low rates; 112 and 118 missing the positive HV connection); position 46 noisy.
- The dead channel on tray SN 4 (module 28, pad 6) was dead in both runs.
- Threshold: Day-50 scan 500–2500 mV; most trays flat, some diverge at 500–600 mV; STAR TOF decided to test 1200 mV in beam (default in tests 2500 mV). Details on [mrpc-technology](mrpc-technology.md).
- After Run 9: trays 77, 117, 120 back to UT; 4, 58, 64 re-fitted; all 120 trays scheduled before Run 10; [llope2012-star-mrpc-systems-note](../../raw/llope2012-star-mrpc-systems-note.md) reports the complete set of 120 installed before Run 10 and the same Run 8 (5 trays) / Run 9 (94 trays) history; it also names the MAXIM 3760 → NINO change, matching the thesis TFEE → TINO history.

## The CTB it replaced

The TOF trays occupy the Central Trigger Barrel positions: CTB = 240 plastic scintillators with PMTs in 120 trays, each one unit of η × 6° in φ, −1 ≤ η ≤ 1, used for charged multiplicity in the trigger; production CTB trays were aluminium without a cooling loop; position numbering from STAR TOF Note 229 [kajimoto2009-star-tof-thesis-note](../../raw/kajimoto2009-star-tof-thesis-note.md). The TOF tray multiplicity to Level-0 takes over that trigger role ([star-daq-trigger](star-daq-trigger.md)).

## Availability

| Built | Remaining | Status | Source |
|---|---|---|---|
| 120 trays (126 assembled incl. 6 spares, 125 shipped to BNL [kajimoto2009-star-tof-thesis-note](../../raw/kajimoto2009-star-tof-thesis-note.md)) | **112 trays** | in situ, no readout | Zhiwen, personal communication, 2026-11-09; matches "All except 8 trays" in [star2026-detector-status-note](../../raw/star2026-detector-status-note.md) (October 2026) ✓ |

112 trays ≈ 56 m² of tray, ≈ 46 m² of pads, 21 504 channels [note]. Details: [rhic-detector-status](rhic-detector-status.md).

## Related
[mrpc-technology](mrpc-technology.md) · [star-mtd](star-mtd.md) · [star-daq-trigger](star-daq-trigger.md) · [star-bemc](star-bemc.md) · [rhic-detector-status](rhic-detector-status.md) · [open-questions](open-questions.md)
