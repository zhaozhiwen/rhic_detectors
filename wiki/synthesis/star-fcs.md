---
title: STAR Forward Calorimeter System (FCS)
tags: [experiment, detector, status]
sources: [tsai2015-fcs-prototype.md, tsai2015-fcs-prototype-note.md, wang2024-star-forward-upgrade.md, wang2024-star-forward-upgrade-note.md, gagliardi2022-star-forward-upgrade-talk.md, gagliardi2022-star-forward-upgrade-talk-note.md, ruan2026-fcs-specs-email.md, ruan2026-fcs-specs-email-note.md, star2026-detector-status.md, star2026-detector-status-note.md]
updated: 2026-11-11
---

# STAR Forward Calorimeter System (FCS)

Forward ECal (re-used PHENIX Pb/scintillator shashlik) + HCal (Fe/scintillator) at ≈ 7 m from the IP, 2.5 < η < 4, SiPM readout; part of the STAR Forward Upgrade together with the Forward Tracking System (Si tracker + sTGC). Sources: QM2023 proceedings [wang2024-star-forward-upgrade-note](../../raw/wang2024-star-forward-upgrade-note.md), STAR Juniors talk Feb 2022 (not peer-reviewed) [gagliardi2022-star-forward-upgrade-talk-note](../../raw/gagliardi2022-star-forward-upgrade-talk-note.md), construction specs by email from L. Ruan [ruan2026-fcs-specs-email-note](../../raw/ruan2026-fcs-specs-email-note.md), and the 2014 prototype [tsai2015-fcs-prototype-note](../../raw/tsai2015-fcs-prototype-note.md), which was a **different design**.

## As built (Wang 2024, Gagliardi 2022, email)

| Item | ECal | HCal |
|---|---|---|
| Technology | re-used PHENIX Pb/scintillator shashlik, WLS fibres (36 per tower) | Fe/scintillator sampling, 3 mm WLS plate down one side of each tower |
| Layers | 66 × 4 mm scint (each wrapped 2 × 0.12 mm paper) + 65 × 1.5 mm Pb (email; talk: 66 cells); pitch 5.74 mm | 36 × (20 mm steel + 3 mm scint), pitch 23.4 mm, + 10 mm back plate |
| Tower face | 5.542 cm (email); 5.52 cm (talk) | 9.99 cm (email); 10 cm (talk) |
| Tower length | **37.73 cm (email) vs 33 cm (talk)** | 84.24 cm (+ 1 cm back plate) |
| Depth | 18.1 X₀ (email), 18 X₀ (talk); **0.93 λ (email) vs 0.85 λ (talk)**; ≈ 0.90 λ recomputed [note] | 41 X₀, 4.45 λ (email); ≈ 4.5 λ (talk); ECal + HCal ≈ 5.4 λ |
| Other | effective X₀ 2.06 cm; Molière radius 5.6 cm; sampling fraction 0.20 | effective λ 18.9 cm; sampling fraction 0.0145 |
| Towers | 1496 (2 halves × 22 × 34) | 520 (2 × 13 × 20) |
| Readout | SiPM ("on the front face" per Wang; email: fibres read "at the back"); 24 DEP boards per half; new ADC/trigger electronics developed with EIC R&D | SiPM; 9 DEP boards per half |
| Position | ECal front z = 710.16 cm, HCal front z = 782.63 cm (email); two movable halves (North/South) | |
| Coverage | 2.5 < η < 4 (paper, talk; design physics range); ≈ 2.2 < η < 4.3 geometric (email) | |
| Design resolution | ~10%/√E (pp, pA), ~20%/√E (AA) (talk) | ~50%/√E + 10% (talk) |

## Status and performance
- Installed during 2020 (talk) / completed 2021 (Wang); commissioned in Run 21; in the trigger and data taking in Run 22 (p+p 510 GeV) and Run 23 (Au+Au 200 GeV).
- ECal calibrated from the π⁰ mass, iterated per channel; within 10% of the π⁰ mass after two iterations [wang2024-star-forward-upgrade-note](../../raw/wang2024-star-forward-upgrade-note.md). HCal MIP calibration still in progress at QM2023.
- **No measured energy resolution** for either calorimeter in these sources; only design goals.
- SiPM radiation damage tracked through leakage current in LED runs; gain loss compensated by regular bias and attenuator adjustments; worst near the beam pipe (Wang 2024 and its talk slides).
- Run-22 FCS triggers: jet patches, di-jets, Drell–Yan (fcsDY ≈ 446 Hz recorded, ≈ 20% of the DAQ bandwidth) and J/ψ (fcsJPsi) [gagliardi2022-star-forward-upgrade-talk-note](../../raw/gagliardi2022-star-forward-upgrade-talk-note.md).
- October 2026: Forward EMCal and Forward HCal "All", in situ; sTGC dismounted; FST one of two halves (3 layers) dismounted [star2026-detector-status-note](../../raw/star2026-detector-status-note.md) ([rhic-detector-status](rhic-detector-status.md)).

## The 2014 prototype was a different design (Tsai 2015)

| | 2014 prototype | As built |
|---|---|---|
| ECal | W powder + scintillating fibres (SPACal), 2.5 × 2.5 × 17 cm, 23 X₀, 9600 towers proposed | Pb/Sc shashlik (PHENIX), 5.5 cm, 18 X₀, 1496 towers |
| HCal | Pb (4% Sb) 10 mm × 63 + 2.5 mm scint, 10 × 10 × 81 cm, 4 λ (≈ 3.8 recomputed for pure Pb, ≈ 3.7 with the Pb(Sb) density ≈ 11.0 g/cm³ [note]), Pb:Sc = 4:1, built to be compensating; 600 towers proposed | steel 20 mm × 36 + 3 mm scint, 84 cm, 4.45 λ, not compensating; 520 towers |
| Light collection | WLS plate between HCal towers; light guides to MPPCs in the ECal | WLS plate per HCal tower (carried over); WLS fibres in the ECal |
| Test beam (FNAL 2014) | electrons (11 ± 0.7)%/√E + (0.7 ± 0.2)%; hadrons (58 ± 4)%/√E + (1.5 ± 1.5)% (EM + HCal, weighted, linear sum); e/h "close to 0.95" above 10 GeV after EM weighting (Fig. 8 points ≈ 0.915–0.945 [note]) | not measured in these sources |

The prototype's W/ScFi calorimetry went on to EIC R&D; the HCal's WLS-plate side readout and SiPM readout survived into the built FCS [note].

## Open points ([open-questions](open-questions.md) #15)
1. ECal tower length 33 cm (talk) vs 37.73 cm (email stack arithmetic: 66 × 4.24 + 65 × 1.50 mm); depth 0.85 vs 0.93 λ (≈ 0.90 recomputed). PHENIX PbSc documentation should settle it.
2. Which end the SiPMs read: "front face" (Wang 2024) vs fibres read "at the back" (email).
3. No HCal or combined resolution measured in STAR in any of these sources.

## Related
[star-eemc](star-eemc.md) · [pi-mu-separation-calorimetry](pi-mu-separation-calorimetry.md) · [rhic-detector-status](rhic-detector-status.md) · [open-questions](open-questions.md)
