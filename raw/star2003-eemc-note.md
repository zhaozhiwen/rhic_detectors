---
title: "Allgower 2003 — The STAR endcap electromagnetic calorimeter (curated notes)"
type: raw-note
source_type: paper
companion: star2003-eemc.md
authors: "STAR EEMC group: C.E. Allgower et al., 46 authors (alphabetical)"
journal: "Nucl. Instrum. Meth. A 499 (2003) 740–750"
doi: 10.1016/S0168-9002(02)01971-X
arxiv: none
notes_updated: 2026-11-09
ingested_version: "Published journal version via publisher HTML (ScienceDirect, Route 1); Table 1 rebuilt from the publisher PDF; all numbers checked against the publisher PDF (captured 2026-11-09)"
earlier_version: []
later_version: []
published_version: "Nucl. Instrum. Meth. A 499 (2003) 740–750 — this is the ingested version"
version_facts: "RHIC special issue 'The Relativistic Heavy Ion Collider Project: RHIC and its Detectors' (eds. M. Harrison, T. Ludlam, S. Ozaki), dated 1 March 2003 (© 2002 Elsevier). No arXiv e-print in the INSPIRE record (608097); a direct arXiv query was refused by the network."
versions_checked: 2026-11-09
---

# Allgower 2003 — STAR EEMC — curated notes

> **Full source:** [star2003-eemc](star2003-eemc.md) · Companion notes to [star2003-eemc](star2003-eemc.md) (full source; a full-content paraphrase).

Links: DOI <https://doi.org/10.1016/S0168-9002(02)01971-X>

## Bibliographic

- **Title:** The STAR endcap electromagnetic calorimeter
- **Authors:** C.E. Allgower, B.D. Anderson, … A. Zubarev — 46 authors, alphabetical (IUCF, Kent State, MSU, BNL, Argonne, JINR Dubna, Rice, Texas A&M, Penn State). Corresponding author S.E. Vigdor (IUCF).
- **Journal:** Nucl. Instrum. Meth. A 499 (2003) 740–750; doi:10.1016/S0168-9002(02)01971-X; PACS 29.40.Vj; 29.40.Mc; 07.85.+n
- **arXiv:** none

## What kind of paper

Pre-installation design paper in the NIM A RHIC detector issue: requirements (Table 1), tower/optical design, SMD, pre/postshower, front-end and trigger, calibration systems. Performance is mostly simulation plus SLAC test-beam profiles and cosmic light yields; no measured energy resolution.

## Abstract (paraphrased)

The EEMC gives full-azimuth coverage over 1.086 ≤ η ≤ 2.00 for high-pT photons, electrons and EM-decaying mesons. A scintillating-strip shower-maximum detector separates π⁰ from γ, and preshower/postshower layers help separate electrons from hadrons. Its coverage and triggering are central to the polarized p+p spin programme.

## Key numbers

**Geometry and stack**
- 1.086 ≤ η ≤ 2.00, full φ, west poletip; two halves, dividing line 15° from horizontal; front face 2.7 m from the IP.
- 720 projective towers; Δφ = 0.1 (drawing: 6°), Δη = 0.057 to 0.099.
- 23 Pb/stainless-steel absorber layers + 24 scintillator layers. Radiator: 4.57 mm Ca-loaded Pb + 0.5 mm stainless steel each face ≈ 0.85 X₀. Scintillator 4 mm Kuraray SCSN-81.
- Total 21.4 X₀ at normal incidence; ∼1 X₀ of STAR material in front; slightly less than one hadronic interaction length. EM sampling fraction 5.0%. Mass ≈ 25,000 kg (both halves).
- Tie-rods every 30° in φ → 30° modules. Megatiles 6° (12 tiles) or 12° (24 tiles); 30° sector = 2 × 12° + one 6° keystone.

**Tower optics and PMTs**
- WLS: Kuraray Y11 (200 ppm), 0.83 mm, σ-grooves, equal lengths per tower. Clear fibre 0.9 mm to the poletip rear; harness 1 mm, 20–45 cm; optical mixer → one PMT per tower.
- PMT: Electron Tubes 9107B, 12 per 6° box; Cockcroft–Walton bases at 160 V DC; gain 2 × 10⁵, linear ±2% to ≥ 50 mA (∼100 GeV).
- Cosmic MIP per 4 mm tile: 2.3–3.2 photoelectrons.

**SMD**
- At ≈ 5 X₀ (after the 5th radiator). Extruded triangular strips, 7 mm high, 10 mm base, 1.0 mm axial WLS hole; u and v planes; 286 strips per plane per 30° sector (572 per sector); radii 77.7–217 cm; three layers, 36 mm total depth.
- Readout: Hamamatsu R5900-M16 16-anode MAPMTs, 3 boxes × 12 MAPMTs per 30° sector; crosstalk ∼1%. Light yield 0.6 p.e. per mm of strip (MIP).
- Simulated π⁰/γ: 80% π⁰ rejection at 80% γ retention, 10–40 GeV.

**Pre/postshower**
- Scintillator layers 1, 2 (preshower) and last (postshower): 5 mm Bicron BC400, dual WLS fibres, one MAPMT channel per tile.
- Simulated h/e suppression: preshower ≈ 4.5 (5–30 GeV/c); postshower × 2; or SMD/tower ratio × 2. W isolation and away-side cuts: another order of magnitude each. Preshower π⁰/γ extra ≈ 2. γ roughly twice as likely as π⁰ to deposit nothing in these layers.

**Electronics / trigger**
- Towers: BEMC electronics, 12-bit flash ADC every crossing, pipelines; L0 single-tower (high-tower) and multi-tower sums; jets via large E_T + CTB/MWC multiplicity. Full ADC range from MIP to 150 GeV electrons.
- MAPMT: preamp + gated integrator + 12-bit ADC per anode; 192 channels + multiplexer per box of 12 MAPMTs; available at L2, not L0. Level 3 prunes TPC pile-up (up to a few thousand segments per trigger at ∼10³² cm⁻² s⁻¹).

**Table 1 requirements (selected)**
- E per tower ≈ 0.2 GeV (min) to 150 GeV (max); < 10% integral non-linearity ∼1–150 GeV; ≥ 20 X₀ and ≤ 1 hadron interaction length.
- σ_E/E ≤ 16%/√E + 2% (linear sum as written).
- π⁰/γ suppression > 3 for pT ≈ 10–20 GeV/c; h±/e± > 10 for pT ≳ 5 GeV/c; W S/B > 3:1 for pT > 20 GeV/c.
- Tower occupancy < 10% at L_pp = 2 × 10³²; absolute calibration ±2% (±10% online); SMD relative gains ≲ ±10%; < 2% shower loss in cracks; timing < 1 RHIC beam period (110 ns).

**Calibration**
- Tower gain matching ±10% before beam; final ±2% in situ (π⁰, Z⁰ peaks; ρ± cross-check); MAPMT hardware compensation ±20% via ADC gain.
- Systems: 355 nm pulsed UV laser via leaky fibres (α-source-monitored); pulsed LEDs (tower PMTs, one pre/post MAPMT pixel, SMD WLS fibres); 300 μCi ⁶⁰Co rod source.
- Scale chain: cosmics (detector horizontal) → laser for dynamic range → ⁶⁰Co (primary) / cosmics vertical (secondary) to transfer.

**Test beam**
- SLAC FFTB, 12-tower prototype, 5, 10, 20 GeV electrons (1–2 per pulse); Oct 1999 (5 mm D0 strips) and Jan 2001 (final strips). y-plane profile matches GEANT; x-plane slightly broader (unexplained).

## Methods / setup

Design description; PYTHIA + GEANT simulations (π⁰/γ via SMD peak-integral vs sided fit residual; e/h via pre/post and SMD/tower); SLAC FFTB prototype scans; cosmic photoelectron measurements.

## What the paper does not give

- Measured energy resolution (stochastic/constant terms), test-beam resolution numbers.
- Radiation/ageing numbers (only a monitoring requirement).
- Pre/postshower channel count; total SMD strip count (only per sector); SMD strip pitch.
- Thicknesses of front plate/FRL/back plate (needed to reconcile 21.4 X₀).
- The term "jet patch".

## Source issues and caveats

- [source issue] (possible) Ref. [1] Bunce et al., Annu. Rev. Nucl. Part. Sci. 50 printed with year 2002; standard year 2000.
- [note] Δφ "0.1" in the caption vs "Δφ = 6°" on the drawing (0.105 rad): rounded.
- [note] Recomputed layer sum ≈ 20.4 X₀ (≈ 19.9 X₀ with 0.85 per sheet) vs quoted 21.4 X₀; ≈ 1 X₀ unitemised.
- [note] MIP-based sampling estimate 10.3% vs quoted EM 5.0%; rule-of-thumb stochastic term ≈ 17%/√E vs the 16%/√E requirement.
- [note] L_pp in Table 1 has no units (presumably cm⁻² s⁻¹); "110 ns" is a rounded bunch spacing.
- [note] Dates (2001 RHIC run test, summer-2002 lower-half install, upper half a year later) are plans at the time of writing.
- Route caveat: HTML Table 1 lost its cell structure (rebuilt from PDF); PDF text layer maps μ→m and ±→7 (300 μCi and 50 mA confirmed on the rendered page). No arXiv copy exists.

## Relevance

Reference design of the STAR forward EM calorimeter (1.086 ≤ η ≤ 2.00): stack, SMD and pre/postshower layout and the e/h and π⁰/γ strategy. Current status of the EEMC is tracked in [rhic-detector-status](../wiki/synthesis/rhic-detector-status.md).

## Related

- Synthesis: [star-eemc](../wiki/synthesis/star-eemc.md) · [star-bemc](../wiki/synthesis/star-bemc.md) · [star-daq-trigger](../wiki/synthesis/star-daq-trigger.md) · [pi-mu-separation-calorimetry](../wiki/synthesis/pi-mu-separation-calorimetry.md) · [star-fcs](../wiki/synthesis/star-fcs.md) · [rhic-detector-status](../wiki/synthesis/rhic-detector-status.md) · [open-questions](../wiki/synthesis/open-questions.md)
- Other notes: [beddo2003-bemc-note](beddo2003-bemc-note.md) (barrel EMC; **[note]** the companion identifies it as the preceding article in the same issue) · [tsai2015-fcs-prototype-note](tsai2015-fcs-prototype-note.md) · [wang2024-star-forward-upgrade-note](wang2024-star-forward-upgrade-note.md)
