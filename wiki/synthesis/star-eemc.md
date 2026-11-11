---
title: STAR Endcap Electromagnetic Calorimeter (EEMC)
tags: [experiment, detector, status]
sources: [star2003-eemc.md, star2003-eemc-note.md, beddo2003-bemc.md, beddo2003-bemc-note.md, star2026-detector-status.md, star2026-detector-status-note.md]
updated: 2026-11-09
---

# STAR Endcap Electromagnetic Calorimeter (EEMC)

Pb/scintillator sampling calorimeter on the west poletip, 1.086 ≤ η ≤ 2.00, with a scintillator-strip shower-maximum detector (SMD), preshower and postshower layers. Source: design paper by Allgower et al. [[star2003-eemc-note]] (NIM A 499 (2003) 740, RHIC special issue, the article after the BEMC paper). Design numbers only; **no measured in-situ resolution**. Barrel counterpart: [[star-bemc]].

| Item | Value |
|---|---|
| Coverage | 1.086 ≤ η ≤ 2.00, 2π; west poletip; front face 2.7 m from the IP |
| Segmentation | 720 towers (60 φ × 12 η), Δφ = 6°, Δη = 0.057–0.099 |
| Structure | two halves; total mass ≈ 25 000 kg (radiators + active elements) |
| Stack | 23 × (4.57 mm Ca-loaded Pb + 2 × 0.5 mm stainless) + 24 × 4 mm SCSN-81 |
| Depth | 21.4 X₀ (stated); ≈ 20.4 X₀ recomputed [note]; just under 1 λ_I |
| Shower-max detector | scintillator triangular strips after the 5th radiator (≈ 5 X₀): u/v planes, 6864 strips; π⁰/γ discrimination |
| Pre/postshower | layers 1, 2 (pre) and last (post), MAPMT readout |
| Light path | WLS fibre → clear fibre → mixer → one PMT per tower (EMI 9107B) on the rear of the poletip |
| Electronics | reuses the BEMC tower electronics; SMD/pre/post via gated integrators; MAPMT data available at Level 2, not Level 0 |
| Resolution | requirement σ_E/E ≤ 16%/√E + 2% |
| Calibration | final ±2% absolute scale in situ (π⁰, Z⁰ peaks) |
| Status (Oct 2026) | "All", in situ, no readout [[star2026-detector-status-note]] |

Notes:
- Table 1 of the paper lost its cell structure in the HTML; the note rebuilt it from the PDF [[star2003-eemc-note]].
- Same 6° φ segmentation (60 sectors) as BEMC and barrel TOF [note].
- The Endcap TOF (a separate, later detector, not covered by any source here) is listed as dismounted and packed for return to Germany ([[rhic-detector-status]]).

## Related
[[star-bemc]] · [[star-fcs]] · [[rhic-detector-status]]
