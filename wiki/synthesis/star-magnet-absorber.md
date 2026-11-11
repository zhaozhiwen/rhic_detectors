---
title: STAR magnet backlegs as the MTD hadron absorber
tags: [detector, experiment]
sources: [ruan2009-mtd-concept.md, ruan2009-mtd-concept-note.md, yang2014-mtd-cosmic-calibration.md, yang2014-mtd-cosmic-calibration-note.md, huang2016-mtd-muon-id.md, huang2016-mtd-muon-id-note.md, llope2012-star-mrpc-systems.md, llope2012-star-mrpc-systems-note.md, beddo2003-bemc.md, beddo2003-bemc-note.md]
updated: 2026-11-09
---

# STAR magnet backlegs as the MTD hadron absorber

The STAR solenoid's flux-return bars ("backlegs") plus the BEMC are the hadron absorber in front of the MTD ([star-mtd](star-mtd.md)). The magnet paper itself (Bergsma et al., NIM A 499 (2003) 633) is **not ingested**; all values below come from the MTD papers and the BEMC paper. Confirm against Bergsma 2003 before simulating.

## Geometry

| Quantity | Value | Source |
|---|---|---|
| Flux return | 30 flux-return bars, four end rings, two pole tips; roughly cylindrical | [ruan2009-mtd-concept-note](../../raw/ruan2009-mtd-concept-note.md), [yang2014-mtd-cosmic-calibration-note](../../raw/yang2014-mtd-cosmic-calibration-note.md) |
| Bar length | 6.85 m | 2009, 2014 |
| Cross-section | trapezoidal | 2009, 2014 |
| Outer radius | 363 cm | 2009, 2014, 2016 |
| Radial thickness | 60 cm (2009 text); 24.000" = 60.96 cm (2009 Fig. 4 CAD, dated Feb. 27, 2007); "57 cm thick" (2014); 61 cm (2016) | [ruan2009-mtd-concept-note](../../raw/ruan2009-mtd-concept-note.md), [yang2014-mtd-cosmic-calibration-note](../../raw/yang2014-mtd-cosmic-calibration-note.md), [huang2016-mtd-muon-id-note](../../raw/huang2016-mtd-muon-id-note.md) |
| Width at outer radius | 57 cm (2009 text); 22.5" ≈ 57.1 cm (2009 Fig. 4) | [ruan2009-mtd-concept-note](../../raw/ruan2009-mtd-concept-note.md) |
| Azimuthal spacing | 30 bars at 12° (2π/30 = 0.209 rad) — bars counted in Beddo Fig. 1: one centred at top and bottom, 7 per quadrant between, gaps on the horizontal [note] | [beddo2003-bemc-note](../../raw/beddo2003-bemc-note.md) |
| Bar-face coverage | 30 × 57 cm / (2π × 363 cm) ≈ 75% of 2π [note] | derived |
| Outside the bars | BEMC PMT/electronics boxes; MTD mounted on them at ~400 cm, field-free | [yang2014-mtd-cosmic-calibration-note](../../raw/yang2014-mtd-cosmic-calibration-note.md) |
| MTD trays | five trays per backleg | [llope2012-star-mrpc-systems-note](../../raw/llope2012-star-mrpc-systems-note.md) |

**Recommended values** [note]: ≈ 61 cm radial thickness, 57 cm width at r = 363 cm. Yang's "57 cm thick" is most likely the width (CAD drawing).

## Magnetic field
- Central (TPC, TOF, BEMC radii): 0.5 T.
- Inside the backleg: 1.2 T [ruan2009-mtd-concept-note](../../raw/ruan2009-mtd-concept-note.md); −1.26 T, opposite in direction to the central field, used in the 2014 track extrapolation [yang2014-mtd-cosmic-calibration-note](../../raw/yang2014-mtd-cosmic-calibration-note.md). BEMC PMT boxes and MTD region field-free.
- Yang 2014 also says t_Steel is derived with the 0.5 T field; the effect on timing is ≪ 1 ps, it matters only for position matching [note].

## Interaction-length budget in front of the MTD

| Material | λ_I | Basis |
|---|---|---|
| Backleg steel, 61 cm Fe | ≈ 3.6 λ_I | 61 / 16.8 cm (λ_I(Fe)) [note]; 57 cm would be ≈ 3.4 λ_I |
| BEMC (100 mm Pb ≈ 0.57 λ_I + 107 mm scintillator, SMD, plates) | ≈ 0.7 λ_I | [note] in [beddo2003-bemc-note](../../raw/beddo2003-bemc-note.md) |
| Sum | **≈ 4.3 λ_I** | + aluminium coil, TOF, TPC material add a little |

Stated in the papers: "each of which amounts to five interaction lengths" (2009, per bar); "about 5 absorption lengths" (2016); "about 6 interaction lengths (BEMC + magnet back-legs)" (Llope 2012). "About 5" is a generous round number for all material in front of the MTD [note]. 61 cm Fe is ≈ 5.9 nuclear collision lengths (10.4 cm), so "absorption lengths" does not match the iron alone either [huang2016-mtd-muon-id-note](../../raw/huang2016-mtd-muon-id-note.md).

## Consequences for muons
- Multiple scattering for 2 GeV/c collision muons (mean p_T of muons reaching the MTD): ≈ 10 cm in position and 100 ps in time at the MTD [yang2014-mtd-cosmic-calibration-note](../../raw/yang2014-mtd-cosmic-calibration-note.md).
- Energy loss: Ruan 2009 quotes ≈ 1.2 GeV for 2 < p_T < 10 GeV/c and attributes it to "multiple scattering" ([source issue]: it is ionization). 60 cm Fe at normal incidence gives ≈ 0.7–0.8 GeV; 1.2 GeV is plausible for the full material on oblique paths [ruan2009-mtd-concept-note](../../raw/ruan2009-mtd-concept-note.md).
- Most charged hadrons stop in the BEMC and backlegs; the few escaping mostly go through the gaps between backlegs [yang2014-mtd-cosmic-calibration-note](../../raw/yang2014-mtd-cosmic-calibration-note.md).
- MTD matching cut Δφ < 0.2 rad ≈ one backleg width (0.209 rad) [note].
- Calorimetric view of absorber-based π/μ separation: [pi-mu-separation-calorimetry](pi-mu-separation-calorimetry.md).

## Related
[star-mtd](star-mtd.md) · [star-bemc](star-bemc.md) · [pi-mu-separation-calorimetry](pi-mu-separation-calorimetry.md) · [open-questions](open-questions.md)
