---
title: STAR Barrel Electromagnetic Calorimeter (BEMC)
tags: [experiment, detector, status]
sources: [beddo2003-bemc.md, beddo2003-bemc-note.md, star2003-eemc.md, star2003-eemc-note.md, yang2014-mtd-cosmic-calibration.md, yang2014-mtd-cosmic-calibration-note.md, star2026-detector-status.md, star2026-detector-status-note.md]
updated: 2026-11-09
---

# STAR Barrel Electromagnetic Calorimeter (BEMC)

Pb/scintillator sampling calorimeter at \|η\| ≤ 1 inside the solenoid coil, with a gas shower-maximum detector (SMD) and preshower. Source: design paper [beddo2003-bemc-note](../../raw/beddo2003-bemc-note.md) (NIM A 499 (2003) 725, RHIC special issue). It gives design and test-beam numbers only; **no measured in-situ tower resolution**. Endcap counterpart: [star-eemc](star-eemc.md).

| Item | Value |
|---|---|
| Coverage | \|η\| ≤ 1, 2π, inside the solenoid coil |
| Segmentation | 120 modules (60 φ × 2 η), each 6° × 1.0 in η; 4800 towers of 0.05 × 0.05 (40 per module) |
| Radius / size | front face r = 2235 mm (text "≈ 220 cm"), back-plate top 2538 mm (302.99 mm module height), rail top 2629.99 mm (Fig. 4); module ≈ 26 cm wide × 293 cm long; front/back width 228.16 / 259.92 mm |
| Stack | 20 × 5 mm Pb; 19 × 5 mm + 2 × 6 mm SCSN81 scintillator; active depth 23.5 cm |
| Depth | ≈ 20 X₀ at η = 0 (stated); ≈ 18.1 X₀ from Pb + scintillator [note]; ≈ 0.57 λ_I of Pb, ≈ 0.7 λ_I with scintillator [note] |
| Shower-max detector | gas (Ar/CO₂) wire chamber after the 5th Pb layer (≈ 5 X₀; ≈ 5.6 X₀ incl. material in front): 36 000 strips; 150 + 150 strips per module |
| Preshower | first two scintillator layers; 4800 channels on 16-pixel MAPMTs |
| Light path | WLS fibre → clear fibre → light mixer → one PMT per tower (ETI 9125B), outside the magnet steel |
| Electronics | 12-bit flash ADCs every crossing; Level-0 high-tower and 300 patch sums within 700 ns |
| Resolution | design ≈ 14%/√E ⊕ 1.5%; SMD test beam σ/E = 12% + 86%/√E (the HTML drops the √; formulas from the PDF) |
| Installation | staged: first ≈ 25% for the 2001 run, then ≈ 25% per year |
| Status (Oct 2026) | "All", in situ, no readout [star2026-detector-status-note](../../raw/star2026-detector-status-note.md) |

## Geometry checks [note]
- 120 × 40 = 4800 towers ✓; 60 × 6° = 360° ✓.
- Each module is ≈ 6 mm narrower than its 6° sector (234.0 mm at 2235 mm, 265.8 mm at 2538 mm) → room between neighbours.
- η = 1 at z = r sinh 1 = 262.7 cm (front) to 298.3 cm (back) → 293 cm module length fits a projective η = 1 end ≈.

## Links to other systems [note]
- **Barrel TOF**: BEMC front face (r = 223.5 cm) is the outer limit for the TOF trays (~220 cm); both use 60 × 6° in φ ([star-barrel-tof](star-barrel-tof.md)).
- **MTD absorber**: the BEMC (≈ 0.7 λ_I) and the 30 magnet flux-return bars (counted in Beddo Fig. 1, 12° spacing) are the hadron absorber in front of the MTD ([star-magnet-absorber](star-magnet-absorber.md)). BEMC fibres and PMT boxes run out between the bars; the MTD trays sit on the BEMC PMT boxes at ~400 cm [yang2014-mtd-cosmic-calibration-note](../../raw/yang2014-mtd-cosmic-calibration-note.md) ([star-mtd](star-mtd.md)).
- **EEMC** reuses the BEMC tower electronics ([star-eemc](star-eemc.md)).

## Related
[star-eemc](star-eemc.md) · [star-magnet-absorber](star-magnet-absorber.md) · [star-barrel-tof](star-barrel-tof.md) · [star-mtd](star-mtd.md) · [rhic-detector-status](rhic-detector-status.md)
