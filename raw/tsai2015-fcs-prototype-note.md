---
title: "Tsai 2015 — Development of a forward calorimeter system for the STAR experiment (curated notes)"
type: raw-note
source_type: paper
companion: tsai2015-fcs-prototype.md
authors: "O.D. Tsai et al. (21 authors; UCLA, BNL, Texas A&M, Penn State, Indiana University CEEM, LBNL)"
journal: "J. Phys.: Conf. Ser. 587 (2015) 012053 — Proceedings of CALOR 2014, Giessen, 6–11 April 2014"
doi: 10.1088/1742-6596/587/1/012053
arxiv: none
notes_updated: 2026-11-09
ingested_version: "IOP publisher PDF (open access, CC-BY 3.0; 11 PDF pages incl. IOP cover page), captured 2026-11-06 via Route 3"
earlier_version: []
later_version: []
published_version: "J. Phys.: Conf. Ser. 587 (2015) 012053 -- this is the ingested version"
version_facts: "Conference proceedings of CALOR 2014. No arXiv version found (title-word and author searches, 2026-11-06). Describes the 2014 FCS prototype and the 2014 proposal, not the as-built FCS."
versions_checked: 2026-11-09
---

# Tsai 2015 — Curated Notes

> **Full source:** [[tsai2015-fcs-prototype]] · Companion notes to [[tsai2015-fcs-prototype]] (full source).
> **DOI:** [10.1088/1742-6596/587/1/012053](https://doi.org/10.1088/1742-6596/587/1/012053) · **PDF:** `assets/tsai2015-fcs-prototype/source.pdf`

## Bibliographic / source

- **Title:** Development of a forward calorimeter system for the STAR experiment
- **Authors:** O.D. Tsai (UCLA, corresponding), E. Aschenauer, W. Christie, L.E. Dunkelberger, S. Fazio, C.A. Gagliardi, S. Heppelmann, H.Z. Huang, W.W. Jacobs, G. Igo, A. Kisilev, K. Landry, X. Liu, M.M. Mondal, Y.X. Pan, M. Sergeeva, N. Shah, E. Sichtermann, S. Trentalange, G. Visser, S. Wissink (21).
- **Published:** J. Phys.: Conf. Ser. 587 (2015) 012053; CALOR 2014 (Giessen, 6–11 April 2014). No arXiv version.

## What kind of source

Peer-reviewed conference proceedings (10 paper pages), no tables, no numbered equations. R&D report: 2014 FCS concept + full-scale prototype test beam at FNAL (March 2014, experiment T1018). Preliminary results; final analysis and exact-geometry MC were still in progress. **Describes a design that was later abandoned for the ECal and changed for the HCal** (see cross-check below).

## Summary (paraphrased)

R&D programme for a compact, compensated, finely segmented Forward Calorimeter System for STAR p+p / p+A running at forward pseudorapidity. EM section: tungsten powder + scintillating fibres (SPACal, "spaghetti"); hadronic section: Pb/scintillator-plate sandwich copied from the ZEUS prototype; both read out by Hamamatsu MPPCs. A 16-channel EM + 16-channel HCal prototype was tested at FNAL with hadrons, electrons and muons at 3–32 GeV, alongside an 18-channel W/ScFi EM prototype for an EIC central barrel.

## Key numbers

**2014 proposal**
- Coverage 2.5–4.5 in η; detects π⁰, photons, electrons, jets, leading hadrons.
- SPACal: 120 × 80 towers (9600), active tower ≈ 2.5 cm × 2.5 cm × 17 cm = 23 X0 (X0,eff 0.74 cm, derived).
- HCal: 30 × 20 towers (600), each 10 cm × 10 cm × 81 cm = 4 interaction lengths (recomputed ≈ 3.8 λ_I, ≈ 113 X0); same transverse area as SPACal (3.0 m × 2.0 m, derived).

**HCal prototype construction**
- Absorber: Pb with 4% Sb, 10 mm plates, white diffuse paint (Sherwin Williams F63WC134); 5 mm steel dowel pins; master plate covers 1.5 rows of towers.
- Scintillator: EJ-212, 2.5 mm in 3.1 mm gaps; 63 absorber + 64 scintillator plates per tower; Pb:scint 4:1 (ZEUS-type).
- Light collection: one 3 mm EJ-280 WLS plate per tower, in the gap between adjacent towers; BC-620 at the far end, aluminised mylar on the back; printed variable-density mylar filter makes collection uniform within 10% along depth (without it, MC resolution ~2× worse above 20 GeV). Unwrapped tiles = Tyvek-wrapped tiles.
- 16-channel prototype assembled at the beam line by 4 people in about 8 hours.

**Readout**
- MPPC S10931-025P (3 × 3 mm², 25 µm pixels): 4 per EM tower, 8 per HCal tower. Geometric efficiency 8.2% (HCal) and ~21% (EM).
- HCal FEE: 90 VDC unregulated input, bias set by two DACs (one with thermistor) → programmable voltage and temperature-compensation slope; 4 SiPMs summed into one BFR92A common-base preamp, input a few Ω (4 SiPMs = 1.3 nF); 4 V peak-to-peak differential output on twisted pair.
- EM FEE: OPA691 summing of 4 MPPCs; one bias for all 16 channels via resistive dividers; **no temperature compensation**; Sylgard 184 (~2 mm) cookie; acrylic truncated-pyramid light guide 25 mm high, 25 × 25 mm² → 13 × 13 mm², MPPC centres 7 mm apart. Non-uniformity up to 20% (bench test).
- Light yield: EM ≈ 400 pixels/GeV (2012 test with PMTs: 2000 p.e./GeV); HCal ≈ 130 pixels/GeV. EIC barrel prototype: 430, 530, 600 pixels/GeV depending on reflectors.

**Test beam (FNAL MT6, March 2014)**
- 3–32 GeV hadrons, electrons, muons; differential Cherenkov for e-ID; XY hodoscope of 4.9 mm rods with SensL SiPMs; ~4 cm upstream scintillator; He-filled beam pipes; two MWPCs.
- HCal at 2.5° and EM at 4° to the beam. LED + pedestal at ~1 Hz: gains stable to better than 1% over a 12-hour shift. Laser gain matching within 1%.
- HCal MIP calibration (8 GeV muon mode, EM removed): ≈ 20% tower-by-tower corrections; ≈ 10% attributed to WLS–MPPC alignment (3 mm active dimensions, ~250 µm misplacement possible).
- Hadrons (EM + HCal, energy-dependent EM weight ≈ 2 → 1.2 between 3 and 20 GeV, flat above): ΔE/E = (0.58 ± 0.04)/√E + 0.015 ± 0.015 (linear sum, read from Fig. 10); 19.2% at 12 GeV (Fig. 8 Gaussian σ 367 / mean 1912); ≈ 15% worse than MC (GEANT4 LHEP) at 10 GeV; nonlinear above 15 GeV (HCal alone linear).
- "e/h" (weighted-sum ratio, effectively e/π) close to 0.95, ≈ constant above 10 GeV; plotted points ≈ 0.87–0.98.
- Electrons: ΔE/E = (0.11 ± 0.007)/√E + 0.007 ± 0.002 with 2012 beam-spread estimates (2.7% below 4 GeV, 2.3% above) unfolded; (0.103 ± 0.005)/√E + 0.017 ± 0.002 with no beam-spread correction. 6.45% at 4 GeV (Fig. 9, 1.4 cm central circle, position-corrected).
- Linearity fits (ADC vs GeV): hadron (157.1 ± 2.4)E + 54.3 ± 22.4; electron (144.5 ± 1.2)E + 40.9 ± 10.9.
- EM position dependence: response falls ≈ 12% (X) / 17% (Y) at 10 mm from tower centre (inferred from fit parameters in the Layer-3 file); impact positions from log weighting, cut-off 3.8.
- EIC barrel W/ScFi prototype (18 channels, 18 X0, wedge towers): stochastic ≈ 9.6–12.1%/√E, constant ≈ 0.3–1.3% at η = 0–0.9 (with the parameter swap below); linearity slopes 160.8 (η = 0) → 169.2 (η = 0.9).

## Methods / setup

W/ScFi SPACal built by forming a fibre matrix, pouring W powder, replacing air with epoxy; 4-tower superblocks; composite with steel-like mechanics. HCal built LEGO-style in situ from plates located by dowel pins; optics carry no load. Test beam: energy scans with LED monitoring; HCal MIP calibration with isolated muons; EM energy corrected for impact position; no leakage corrections.

## What it does not give

- No as-built FCS numbers; no HCal-alone resolution or e/h; no EM-alone resolution separate from the electron curve.
- No W-powder/epoxy density, fibre pitch or EM sampling fraction (deferred to the 2012 reference).
- No radiation dose/fluence numbers (MPPCs called "sufficiently radiation hard" with a citation only); nothing on rates, occupancy or pile-up.

## Source issues and caveats

- **[source issue]** Fig. 12 resolution fit parameters are swapped relative to the caption form p0/√E + p1: only p1/√E + p0 reproduces the plotted points (η = 0, 2 GeV: 0.088 vs 0.116).
- **[source issue]** (minor) HCal tower length quoted 81 cm, but 63 × 10 mm + 64 × 3.1 mm = 828.4 mm (≈ 2% longer).
- HCal geometric efficiency 8.2% cannot be reproduced from the dimensions given (8 × 9 mm² on a 3 mm × 10 cm WLS edge gives 24%).
- Fig. 11 in-figure label spelled "Sintillator Hodoscope" (sic).
- Resolution fits are linear sums, not quadrature; not directly comparable with a/√E ⊕ b.
- Fig. 8 e/h points above 10 GeV sit at ≈ 0.90–0.945, slightly below the text's "close to 0.95"; the 32 GeV electron point also sits ≈ 3% below its linearity line.
- **[note]** Estimated EM pixel saturation ≈ 10% at 32 GeV in one EM tower (57 600 pixels at 400 pixels/GeV), so "almost linear" may be optimistic at the top of the range (estimate in the Layer-3 file, not in the paper).
- All results preliminary.

## FCS cross-check: 2014 prototype vs as-built (from [[ruan2026-fcs-specs-email-note]])

| Item | 2014 prototype / proposal | As-built FCS (email) |
|---|---|---|
| η coverage | 2.5–4.5 | ≈ 2.2–4.3 |
| ECal | W powder + ScFi SPACal, 2.5 × 2.5 cm², 17 cm, 23 X0, 9600 towers proposed | re-used PHENIX Pb/scint shashlik, 5.542 × 5.542 cm², 37.73 cm, 18.1 X0, 0.93 λ, 1496 towers |
| HCal absorber | Pb (4% Sb), 10 mm × 63 | steel, 20 mm × 36 (+10 mm back plate) |
| HCal scintillator | 2.5 mm EJ-212 × 64 | 3.0 mm × 36 |
| HCal tower | 10 × 10 cm², 81 cm, 4 λ_I quoted | 9.99 × 9.99 cm², 84.24 cm, 4.45 λ, 41 X0 |
| HCal towers | 600 proposed | 520 |
| HCal light collection | 3 mm WLS plate per tower | 3 mm WLS plate down one side of each tower (same concept) |
| Total depth | ≈ 4.7 λ_I (derived) | ≈ 5.4 λ |

- What survived: WLS-plate side readout of the HCal, SiPM readout throughout, ~10 cm HCal towers. The compensating Pb:scint ratio and the W/ScFi ECal were dropped; W/ScFi went on to EIC R&D.
- **[note]** In the 2014 test beam the FCS prototype was read out **upstream** of the incoming beam (the EIC prototype downstream), with no performance difference between the two. Relevant to the as-built readout-end question (Wang 2024 "front face" vs email "read out at the back"); see [[open-questions]].

## Relevance

Design history of the [[star-fcs]]: explains the origin of the SiPM readout, WLS-plate HCal light collection and LED/MIP calibration approach; quantifies what a compensating W/ScFi + Pb/scint system achieved before STAR chose re-used PHENIX modules and a steel HCal. HCal muon/MIP calibration is a reference point for [[pi-mu-separation-calorimetry]]. Not a source for as-built FCS parameters.

## Related

- Synthesis: [[star-fcs]] · [[pi-mu-separation-calorimetry]] · [[open-questions]]
- Notes: [[wang2024-star-forward-upgrade-note]] (as-built status 2024) · [[gagliardi2022-star-forward-upgrade-talk-note]] (as-built specs, Run 22) · [[ruan2026-fcs-specs-email-note]] (construction specs) · [[star2026-detector-status-note]] (FCS status October 2026)
