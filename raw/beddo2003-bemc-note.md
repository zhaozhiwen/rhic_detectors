---
title: "Beddo 2003 — The STAR Barrel Electromagnetic Calorimeter (curated notes)"
type: raw-note
source_type: paper
companion: beddo2003-bemc.md
authors: "M. Beddo et al. (102 authors; ANL, BNL, JINR, IUCF, IHEP Protvino, LBNL, MSU, Penn State, Rice, UCLA, Wayne State; corresponding author T.M. Cormier)"
journal: "Nucl. Instrum. Meth. A 499 (2003) 725–739 (RHIC special issue)"
doi: "10.1016/S0168-9002(02)01970-8"
arxiv: none
notes_updated: 2026-11-09
ingested_version: "Publisher version of record, read 2026-11-09 via Route 1 (ScienceDirect HTML in Chrome); formulas, cross-talk limits and Table 1 from the publisher PDF (15 pages) because the HTML drops square roots"
earlier_version: []
later_version: []
published_version: "Nucl. Instrum. Meth. A 499 (2003) 725–739 -- this is the ingested version"
version_facts: "RHIC special issue 'The Relativistic Heavy Ion Collider Project: RHIC and its Detectors' (eds. M. Harrison, T. Ludlam, S. Ozaki), dated 1 March 2003 (© 2002). INSPIRE 608096 (author_count 102) has no arXiv e-print number; direct arXiv query refused by network. Design-stage paper: describes staged installation starting with ~25% for the 2001 run."
versions_checked: 2026-11-09
---

# Beddo 2003 — Curated Notes

> **Full source:** [[beddo2003-bemc]] · Companion notes to [[beddo2003-bemc]] (full source; a full-content paraphrase).
> **DOI:** https://doi.org/10.1016/S0168-9002(02)01970-8 · arXiv: none

## Bibliographic

- **Title:** The STAR Barrel Electromagnetic Calorimeter
- **Authors:** M. Beddo et al., 102 authors (author list from PDF p. 1); corresponding author T.M. Cormier (Wayne State).
- **Journal:** Nucl. Instrum. Meth. A 499 (2003) 725–739, RHIC special issue; immediately precedes the EEMC paper ([[star2003-eemc-note]], pp. 740–750).

## What kind of paper

Design/construction NIM paper for the STAR BEMC: mechanics, optics, SMD, preshower, electronics/trigger role, plus a simulated e/h-discrimination study. No measured in-situ tower energy resolution.

## Abstract (paraphrased)

Describes the design, construction and performance of the STAR Barrel Electromagnetic Calorimeter.

## Key numbers

**Coverage and segmentation**
- |η| ≤ 1.0, 2π; inside the aluminum solenoid coil; front face ≈220 cm (Fig. 4: r = 2235 mm). Area > 60 m².
- 120 modules (60 φ × 2 η), each 6° (~0.1 rad) × 1.0 in η, ≈26 cm wide × 293 cm long; active depth 23.5 cm + ≈6.6 cm structural plates (≈1.9 cm in front).
- 40 towers/module (2 φ × 20 η), 0.05 × 0.05 → 4800 projective towers (~10 × 10 cm² at η = 0).
- Fig. 4: front width 228.16 mm, back width 259.92 mm, module height 302.99 mm, top of linear-bearing track r = 2629.99 mm.

**Stack and depth**
- 20 × 5 mm Pb; 21 Kuraray SCSN81 scintillator layers (19 × 5 mm + 2 × 6 mm preshower). Depth ~20 X₀ at η = 0; EM showers contained up to 60 GeV.
- Compression: 30 straps + bolts/Belleville washers; mean ≈15 psi.
- **[note]** L3-derived: Pb/Sc alone ≈18.1 X₀; ≈0.57 λ_I of Pb, ≈0.7 λ_I with scintillator; ≈1.0 X₀ of material in front at η = 0.

**Optics**
- Megatiles: 40 tiles per layer, σ-groove WLS fibre; isolation by 95% cut + SiO₂-loaded epoxy; cross-talk < ½% (black line on uncut surface). 840 tile shapes per module (420 + mirrors); router ~200 in./min.
- Edges painted Bicron BC620; white bond paper between layers.
- WLS: Kuraray Y11 (200 ppm) S-type, 0.83 mm, mirrored end; 2.1 m clear cable Kuraray 0.9 mm; 1.0 mm in decoder boxes; 21 tiles → one PMT per tower; Lucite mixer 2″ × 0.5″ × 0.5″.
- PMT: Electron Tube 9125B, ≈30 mm, 11 dynodes, ≈23 mm photocathode, peak QE ~25%; accepted mean QE 13.3% (s.d. 1.3%); none < 10% at 490 nm; dark current < 5 nA at gain 2 × 10⁵; non-linearity < 2% at 20 mA.
- Base: Cockcroft–Walton, PFM/PWM HV, divider 2:1:1:1:1:1:1:1:2:3:4:3, ADUC812-type 8051 microcontroller (12-bit DAC/ADC); ripple 0.05% at 1000 V (1 μA); noise ≪ 0.15 pC (1 LSB); limit −1520 V; setpoint 0.6 V, accuracy 0.3%. RS485 control, 12-bit address (4096), one repeater per box of 80 PMTs, LabView.
- Light yield: 3 photoelectrons per mip per layer; ideal σ_E/E ≈ 14%/√E ⊕ 1.5%.
- QA: tile transverse uniformity < 5% RMS; tower longitudinal uniformity < 10% RMS; adjacent-tile cross-talk < ½%. Measured tile-yield RMS 8.1% (160 tiles, modules 8 and 12).

**SMD (Table 1 and text)**

| Parameter | Value |
|---|---|
| Depth | ~5 X₀ at η = 0 (≈5.6 X₀ incl. material in front; 4.6 → 7.1 X₀ calorimeter-only, η 0 → 1) |
| Position in stack | between Pb5 and Sc6 (Fig. 4) |
| Type | double-sided Al extrusion, 5.9 mm channels along η, two wire planes; 30 cells/side, 60 anode wires |
| Wires | 50 μm gold-plated tungsten; wires 1.0 in η long |
| Gas / gain | 90% Ar / 10% CO₂; ≈3000 |
| Thickness | 20.6 mm (cathode to cathode) |
| Signal length | 110 ns |
| η strips | 1.46 (1.54) cm width (pitch) for |η| < 0.5; 1.88 (1.96) cm for |η| > 0.5; 0.1 rad in φ |
| φ strips | 1.33 (1.49) cm; 0.1 in η long |
| Strips | 300/module (150 η + 150 φ); 36 000 total; 120 ganged wire channels |
| Occupancy | ≈1% (p+p); > 5 to ≈25% (Au+Au, threshold-dependent) |

- 1200 areas of 0.1 × 0.1 with 15 η + 15 φ strips; 120 possible shower-max trigger signals (1.0 × 0.1).
- Signals < ≈7 fC/mip; coil ripple up to 400 V; dynamic range ≈1:1000; FEE at η = 1 end; SCA + 80:1 multiplexing; TPC-type amplifier ASIC; uniformity ±14% before calibration; cross-talk ≤ 1%.
- AGS test beam 0.5–5 GeV: linear; back-plane ionization ~10% lower; σ/E(front) = 12% + 86%/√E (back 3–4% worse); σ_front = 2.4 mm + 5.6 mm/√E, σ_back = 3.2 mm + 5.8 mm/√E (E in GeV; linear sums as printed).

**Preshower**
- Layers 1–2 (6 mm), two WLS fibres per groove (20% less light each); one pair to tower sum, other pair to one MAPMT pixel; 300 sixteen-pixel MAPMTs for 4800 pairs.
- Electrons: ≈63% shower before layer 1, ≈84% by middle of preshower; hadrons ≈3% and ≈6%. Mip in PSD ≈8 photoelectrons (two layers).

**Electronics and trigger**
- Towers: gated integrators + 12-bit flash ADCs every crossing, digital pipeline, dead-timeless level-0; token-addressable memory in tower data collector.
- Trigger primitives: 300 tower sums (0.2 × 0.2 patches) + 300 high-tower values, 6 bits each, to level-0 within 700 ns; level-0 to TPC within ~1 μs (~10 crossings).
- SMD: 10-bit digitizers, 80:1 mux; data at level-2 in ~200 μs.

**e/h discrimination (simulation)**
- Range 0.5–5 GeV; eight variables (E/p, E_SMD(η), E_SMD(φ), Δη, Δφ, σ_η, σ_φ, E_PSD); seven-node neural network on GSTAR, π⁺/e⁺ at 0.5, 1.0, 2.0, 5.0 GeV/c; ~1000 e, ~5000 hadrons; 3 pe per MeV.
- Central Au+Au underlying event: 140 MeV/tower mean, 170 MeV s.d.; J/ψ electron threshold 1.5 GeV where σ_E/E = 12% (~180 MeV) degrades to 17%; at 3 GeV 9% → 10%.
- Fig. 10 (read off plot, ≈ (ε_e, h)): (0.90, 5.2) at 0.5 GeV/c; (0.93, 23) at 1.0 GeV/c; (0.91, 92) at 2.0 GeV/c; (0.88, 460) at 5.0 GeV/c. h rises steeply with energy at fixed ε_e.

## Methods / setup

- Engineering description of module mechanics and optics; component QA (tile scans, PMT acceptance tests, cosmic/test-beam light yield); 1998 EMC test-beam data and AGS SMD test beam; GSTAR/GEANT simulation with TPC momentum smearing for the e/h neural-network study.

## What the paper does not give

- Measured tower energy resolution (only the ideal estimate and the 12% at 1.5 GeV used in §8); in-situ absolute calibration method.
- Radiation dose, ageing (scintillator, fibre, gas), PMT rate limits.
- Magnet coil thickness, backleg geometry (Fig. 1 has no dimensions).

## Source issues and caveats

- **[source issue]** Fig. 4: 69.85 + 24.99 = 94.84 mm, but the same span is printed 91.99 mm; the drawing scale says "24.99mm" is the wrong label (≈22.7 mm measured).
- **[source issue]** §8 cites "Fig. 2" for the network output; it is Fig. 9.
- HTML drops every √ and renders "½%" as "12%"; the PDF was used for all formulas and Table 1.
- Text "≈220 cm" vs Fig. 4 r = 2235 mm (rounding). Fig. 4 called "end view" in text, "side view" in caption (it is r–φ).
- Hadron interaction "before layer 1" counts one Pb layer, but Fig. 4 shows no Pb in front of Sc1 (L3 note; minor).
- Fig. 6 bar heights sum to 157, not 160; binned RMS 7.6% vs quoted 8.1%.
- SMD formulas are linear sums, not quadrature, as printed.
- "Frecuency" (Fig. 6) and "Gev" (Fig. 9) typos; "proceed" for "precede".
- Route caveat: Route 1 HTML has no MathML in the body; PDF text layer maps symbols oddly (μ→m, ±→7, η→Z) — rendered pages used. Figure readings approximate.

## Relevance

Defines the BEMC geometry that bounds the barrel TOF from outside (front face r = 2235 mm) and forms the first part of the MTD hadron absorber (≈0.7 λ_I, an L3 **[note]** estimate); also STAR's main level-0 high-p_T/electron trigger detector and the reference for SMD/preshower-based e/h and π⁰/γ separation.

## Related

- Synthesis: [[star-bemc]] · [[star-eemc]] · [[star-daq-trigger]] · [[star-magnet-absorber]] · [[pi-mu-separation-calorimetry]] · [[star-barrel-tof]] · [[star-mtd]] · [[open-questions]]
- Notes: [[star2003-eemc-note]] (companion endcap paper) · [[llope2012-star-mrpc-systems-note]] (MTD absorber "≈6 interaction lengths" incl. BEMC) · [[ruan2009-mtd-concept-note]]
