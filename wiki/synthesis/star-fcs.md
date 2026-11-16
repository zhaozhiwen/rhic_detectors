---
title: STAR Forward Calorimeter System (FCS)
tags: [experiment, detector, status]
sources: [tsai2015-fcs-prototype.md, tsai2015-fcs-prototype-note.md, wang2024-star-forward-upgrade.md, wang2024-star-forward-upgrade-note.md, gagliardi2022-star-forward-upgrade-talk.md, gagliardi2022-star-forward-upgrade-talk-note.md, ruan2026-fcs-specs-email.md, ruan2026-fcs-specs-email-note.md, star2026-detector-status.md, star2026-detector-status-note.md, star2018-forward-upgrade-proposal.md, star2018-forward-upgrade-proposal-note.md]
updated: 2026-11-16
---

# STAR Forward Calorimeter System (FCS)

Forward ECal (re-used PHENIX Pb/scintillator shashlik) + HCal (Fe/scintillator) at ≈ 7 m from the IP, 2.5 < η < 4, SiPM readout; part of the STAR Forward Upgrade together with the Forward Tracking System (Si tracker + sTGC; see [star-forward-tracking](star-forward-tracking.md)). Sources: the November 2018 STAR design proposal (not peer-reviewed; design values) [star2018-forward-upgrade-proposal-note](../../raw/star2018-forward-upgrade-proposal-note.md), QM2023 proceedings [wang2024-star-forward-upgrade-note](../../raw/wang2024-star-forward-upgrade-note.md), STAR Juniors talk Feb 2022 (not peer-reviewed) [gagliardi2022-star-forward-upgrade-talk-note](../../raw/gagliardi2022-star-forward-upgrade-talk-note.md), construction specs by email from L. Ruan [ruan2026-fcs-specs-email-note](../../raw/ruan2026-fcs-specs-email-note.md), and the 2014 prototype [tsai2015-fcs-prototype-note](../../raw/tsai2015-fcs-prototype-note.md), which was a **different design**.

## As built (Wang 2024, Gagliardi 2022, email)

| Item              | ECal                                                                                                                                              | HCal                                                                 |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------- |
| Technology        | re-used PHENIX Pb/scintillator shashlik, WLS fibres (36 per tower)                                                                                | Fe/scintillator sampling, 3 mm WLS plate down one side of each tower |
| Layers            | 66 × 4 mm scint (each wrapped 2 × 0.12 mm paper) + 65 × 1.5 mm Pb (email; talk: 66 cells); pitch 5.74 mm                                          | 36 × (20 mm steel + 3 mm scint), pitch 23.4 mm, + 10 mm back plate (2018 design: 38 layers, 3.1 mm gaps) |
| Tower face        | 5.542 cm (email); 5.52 cm (talk)                                                                                                                  | 9.99 cm (email); 10 cm (talk)                                        |
| Tower length      | **37.73 cm (email) vs 33 cm (talk)**                                                                                                              | 84.24 cm (+ 1 cm back plate)                                         |
| Depth             | 18.1 X₀ (email), 18 X₀ (talk); **0.93 λ (email) vs 0.85 λ (talk)**; ≈ 0.90 λ recomputed [note]                                                    | 41 X₀, 4.45 λ (email); ≈ 4.5 λ (talk); ECal + HCal ≈ 5.4 λ           |
| Other             | effective X₀ 2.06 cm; Molière radius 5.6 cm; sampling fraction 0.20                                                                               | effective λ 18.9 cm; sampling fraction 0.0145 (same value in the 2018 simulation) |
| Towers            | 1496 (2 halves × 22 × 34)                                                                                                                         | 520 (2 × 13 × 20)                                                    |
| Readout           | SiPM ("on the front face" per Wang; email: fibres read "at the back"; 2018 design: front face, see below); 24 DEP boards per half; new ADC/trigger electronics developed with EIC R&D | SiPM; 9 DEP boards per half                                          |
| Position          | ECal front z = 710.16 cm, HCal front z = 782.63 cm (email); two movable halves (North/South)                                                      |                                                                      |
| Coverage          | 2.5 < η < 4 (paper, talk; design physics range); ≈ 2.2 < η < 4.3 geometric (email)                                                                |                                                                      |
| Design resolution | ~10%/√E (pp, pA), ~20%/√E (AA) (talk; 2018 Table 3-1); the 2018 text also prints ~8%/√E (Ch. 1, §4.1)                                            | ~50%/√E + 10% (talk; 2018 proposal)                                  |

## Status and performance
- Installed during 2020 (talk) / completed 2021 (Wang); commissioned in Run 21; in the trigger and data taking in Run 22 (p+p 510 GeV) and Run 23 (Au+Au 200 GeV).
- ECal calibrated from the π⁰ mass, iterated per channel; within 10% of the π⁰ mass after two iterations [wang2024-star-forward-upgrade-note](../../raw/wang2024-star-forward-upgrade-note.md). HCal MIP calibration still in progress at QM2023.
- **No measured energy resolution** for either calorimeter in these sources; only design goals.
- SiPM radiation damage tracked through leakage current in LED runs; gain loss compensated by regular bias and attenuator adjustments; worst near the beam pipe (Wang 2024 and its talk slides).
- Run-22 FCS triggers: jet patches, di-jets, Drell–Yan (fcsDY ≈ 446 Hz recorded, ≈ 20% of the DAQ bandwidth) and J/ψ (fcsJPsi) [gagliardi2022-star-forward-upgrade-talk-note](../../raw/gagliardi2022-star-forward-upgrade-talk-note.md).
- October 2026: Forward EMCal and Forward HCal "All", in situ; sTGC dismounted; FST one of two halves (3 layers) dismounted [star2026-detector-status-note](../../raw/star2026-detector-status-note.md) ([rhic-detector-status](rhic-detector-status.md)).

## Design stage: the 2018 proposal [star2018-forward-upgrade-proposal-note](../../raw/star2018-forward-upgrade-proposal-note.md)

STAR's November 2018 review proposal fixes the design that was built: 1496 of the 15552 PHENIX ECal towers plus 520 Fe/scintillator HCal towers, ≈ 2.6 m × 2 m, SiPMs and one common front end, re-use of the Forward Preshower Detector (2.5 < η < 4, in STAR since 2015). The redesign from the 2014 concept (below) was driven by cost: the PHENIX ECal became free after 2016 and meets the resolution goal, at the price of giving up compensation; with a non-compensating EM section a lead HCal brings no benefit, so the absorber became iron.

| Item | 2018 design | As built (for comparison) |
|---|---|---|
| ECal | re-used PHENIX towers; no length, X₀ or λ given (cites the PHENIX calorimeter paper, NIM A499 (2003) 521) | 5.542 cm, 37.73 cm (email) / 33 cm (talk), 18 X₀ |
| ECal readout | mounted on the **front face** so no significant dead space opens between ECal and HCal; FEE (4 towers) bolted to the module front, pogo pins to SiPM carrier boards glued to a light-guide block at the end of each tower's fibre bundle | "on the front face" (Wang 2024); "read out at the back" (email) |
| HCal | 38 layers of 20 mm Fe + 3 mm scintillator in 3.1 mm gaps, ≈ 4.5 λ; 3 mm EJ-280 WLS plate per tower read at the downstream end; uniformity filter (within 10%) | 36 layers, pitch 23.4 mm, + 10 mm back plate, 4.45 λ (email) |
| Sampling fraction (simulation) | ECal 0.20, HCal 0.0145 | same (email) |
| Weight, mounting | ECal ≈ 10 t on the FMS rails and rollers; HCal ≈ 40 t on new rails over the west-wall cavity | two movable halves (talk, email) |
| FEE | ECal board 4 towers, HCal board 2 towers; full scale 180 GeV, ≈ 5x gain for cosmics; bias 0–70 V (14-bit), limit ≈ 800 µA, noise < 1 mV; temperature compensation 0 to +66 mV/°C (12-bit); current monitor 16-bit, 0–410 µA (HCal 0–614 µA); I²C, up to 16 FEE per bus | not described in the as-built sources |
| SiPM | Run 17: up to 10% response loss per 510 GeV run from a breakdown-voltage shift (≈ 100 µA → ≈ 0.6 °C heating → ≈ 10%); HPK S14160-015P after ≈ 7×10¹⁰ n/cm²: ≈ 1% per run, ≈ 40 mV/C vs ≈ 60 mV/C; $8.9 each for 10k units | type not given in the as-built sources; LED leakage-current monitoring and regular bias/attenuator adjustment (Wang 2024) |
| Digitizers / trigger | 74 DEP/ADC + 3 DEP/IO; 3-layer trigger, ≤ 1.35 µs ([star-daq-trigger](star-daq-trigger.md)) | 24 ECal + 9 HCal DEP per half (email) |
| Simulated trigger | photons 99% → 96% at 80 GeV (threshold 80% of E); π⁻ 74% at 10 GeV (60%) | Run 22 fcsDY, fcsJPsi, jet-patch triggers (talk) |

[note] The proposal's 74 DEP/ADC equals the email's 2 × (24 + 9) = 66 calorimeter boards plus 2 × 4 = 8 preshower boards; its trigger layer 2 takes only 20 ECal + 8 HCal boards per half. The HCal layer count (38 → 36 + back plate) and pitch (23.1 → 23.4 mm) changed between design and construction; no source says why.

## The 2014 prototype was a different design (Tsai 2015)

| | 2014 prototype | As built |
|---|---|---|
| ECal | W powder + scintillating fibres (SPACal), 2.5 × 2.5 × 17 cm, 23 X₀, 9600 towers proposed | Pb/Sc shashlik (PHENIX), 5.5 cm, 18 X₀, 1496 towers |
| HCal | Pb (4% Sb) 10 mm × 63 + 2.5 mm scint, 10 × 10 × 81 cm, 4 λ (≈ 3.8 recomputed for pure Pb, ≈ 3.7 with the Pb(Sb) density ≈ 11.0 g/cm³ [note]), Pb:Sc = 4:1, built to be compensating; 600 towers proposed | steel 20 mm × 36 + 3 mm scint, 84 cm, 4.45 λ, not compensating; 520 towers |
| Light collection | WLS plate between HCal towers; light guides to MPPCs in the ECal | WLS plate per HCal tower (carried over); WLS fibres in the ECal |
| Test beam (FNAL 2014) | electrons (11 ± 0.7)%/√E + (0.7 ± 0.2)%; hadrons (58 ± 4)%/√E + (1.5 ± 1.5)% (EM + HCal, weighted, linear sum); e/h "close to 0.95" above 10 GeV after EM weighting (Fig. 8 points ≈ 0.915–0.945 [note]) | not measured in these sources |

The 2018 proposal (§4.5) repeats the same 2014 test-beam results (Fig. 4-9 legends: hadrons (0.58 ± 0.04)/√E + 0.015 ± 0.015, electrons (0.11 ± 0.007)/√E + 0.007 ± 0.002) and adds that the hadron resolution was ≈ 15% worse than MC at 10 GeV [star2018-forward-upgrade-proposal-note](../../raw/star2018-forward-upgrade-proposal-note.md). The prototype's W/ScFi calorimetry went on to EIC R&D; the HCal's WLS-plate side readout and SiPM readout survived into the built FCS [note].

## Open points ([open-questions](open-questions.md) #15, #24)
1. ECal tower length 33 cm (talk) vs 37.73 cm (email stack arithmetic: 66 × 4.24 + 65 × 1.50 mm); depth 0.85 vs 0.93 λ (≈ 0.90 recomputed). **Not settled by the 2018 proposal**, which gives no ECal length or depth and only cites the PHENIX calorimeter paper (Aphecetche et al., NIM A499 (2003) 521) — that paper is the next source.
2. Which end the SiPMs read: the 2018 design puts the ECal readout on the front face (FEE on the module front, light guide at the end of each fibre bundle), agreeing with Wang 2024 "front face". [note] The email's "read out at the back" is compatible if it refers to the module's own fibre-readout end, turned to face the IP in STAR; no source says so explicitly. Treated as probably resolved (front face), pending an as-built statement.
3. No HCal or combined resolution measured in STAR in any of these sources; the proposal's numbers are the 2014 prototype and simulations.
4. HCal layer count: 38 (2018 design) vs 36 + 10 mm back plate (email); reason not given.

## Related
[star-forward-tracking](star-forward-tracking.md) · [star-daq-trigger](star-daq-trigger.md) · [star-eemc](star-eemc.md) · [pi-mu-separation-calorimetry](pi-mu-separation-calorimetry.md) · [rhic-detector-status](rhic-detector-status.md) · [open-questions](open-questions.md)
