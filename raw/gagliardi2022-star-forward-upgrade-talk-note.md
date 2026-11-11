---
title: "Gagliardi 2022 — The STAR Forward Upgrade (curated notes)"
type: raw-note
source_type: talk-slides
companion: gagliardi2022-star-forward-upgrade-talk.md
authors: "Carl Gagliardi (Texas A&M University)"
venue: "STAR Juniors meeting, February 2022 (slides finalized 2022-02-12); not peer-reviewed"
doi: none
arxiv: none
notes_updated: 2026-11-09
ingested_version: "talk-slide PDF, 52 slides (PDF created 2022-02-12 23:36 UTC), supplied by the repo author; captured 2026-11-06 via Route 3"
earlier_version: []
later_version: []
published_version: "none -- internal collaboration talk slides, not peer-reviewed; published in this repo with Zhiwen's agreement"
version_facts: "Slide footers: 'STAR Forward Upgrade - 2-22 Juniors - Carl Gagliardi'. Exact talk date and venue not printed. PDF title metadata 'Thinking About Run 22 Triggering' is a leftover from another file."
versions_checked: 2026-11-09
---

# Gagliardi 2022 — Curated Notes

> **Full source:** [[gagliardi2022-star-forward-upgrade-talk]] · Companion notes to [[gagliardi2022-star-forward-upgrade-talk]] (full source).
> **Links:** no DOI (talk slides) · **PDF:** `assets/gagliardi2022-star-forward-upgrade-talk/source.pdf`

## Bibliographic / source

- **Title:** The STAR Forward Upgrade
- **Speaker:** Carl Gagliardi (Texas A&M University).
- **Venue / date:** STAR Juniors meeting, February 2022; slides finalized Saturday 12 Feb 2022 (screenshots and luminosity plots stamped that day). 52 slides.

## What kind of source

Internal collaboration talk slides, **not peer-reviewed**; collaboration material published in this repo with Zhiwen's agreement. Three parts: what the forward upgrade is (s2–s15), the physics it enables (s16–s35), and how Run 22 is going (s36–s51). Projections and preliminary plots as presented; many values read off plots (≈ in the Layer-3 file).

## Summary (paraphrased)

The forward upgrade adds tracking (Si FST + sTGC) and calorimetry (ECal + HCal with SiPM readout, new ADC and trigger electronics) at 2.5 < η < 4, where STAR previously had only Pb-glass EM calorimetry; same coverage as the EIC hadron arm. Physics: Sivers and Collins asymmetries with jets and hadrons in jets, transversity at high x, GPD E_g via ultra-peripheral J/ψ, nuclear PDFs via direct photons and Drell–Yan, saturation via forward correlations, and A+A flow, decorrelation and Λ polarization. As of 12 Feb 2022 the FCS and trackers were running and taking good data; luminosity and polarization were behind goals.

## Key numbers

**Requirements [s4]:** ECal ~10%/√E (pp, pA), ~20%/√E (AA); HCal ~50%/√E + 10%; tracking: charge separation and photon suppression (pp, pA), 0.2 < p_T < 2 GeV/c with 20–30% 1/p_T (AA).

**FST [s5]:** 3 disks × 12 modules; 3 single-sided double-metal mini-strip Hamamatsu sensors per module; ~1.5% X₀ per disk; APV25-S1; IST DAQ and cooling reused.

**sTGC [s7–s10]:** 4 planes × 4 pentagonal modules; x, y, u strips; < 200 μm resolution; ~0.5% X₀ per layer; VMM readout; CO₂ + n-pentane (flash point −49 °C, explosive limits 1.5–7.8%, boiling point 36.1 °C). Test-stand efficiency 98.7% (X, 777/787) and 98.2% (Y, 323/329); headline "Efficiency > 97%".

**Simulated tracking [s11]:** charge mis-ID < 6% (8%) and p_T resolution < 35% for p_T < 5 GeV/c at √s = 500 (200) GeV. FTT + FST fits at 500 GeV: mis-ID 0.1% + 1.1% × p_T; resolution 14.9% + 4.0% × p_T.

**FCS [s12–s13]:**
- 7 m from the centre of STAR; 2 movable halves; slightly projective.
- ECal: re-used PHENIX Pb/Sc; 1496 channels of 5.52 × 5.52 × 33 cm³; 66 cells of 1.5 mm Pb / 4 mm Sc; 36 WLS fibres per cell; 18 X₀; 0.85 λ_I; PMTs replaced by SiPMs.
- HCal: Fe/Sc 20 mm / 3 mm; 520 channels of 10 × 10 × 84 cm³; ≈ 4.5 λ_I; same SiPM readout as ECal; developed with EIC R&D.
- Preshower: signals split off from the EPD for triggering.
- Installed during 2020; commissioned in Run 21 (Au+Au √s_NN = 7.7 GeV, brief O+O and d+Au at 200 GeV); ready on Run 22 day 1 except gain tweaks.

**Run 22 (pp 510 GeV) status, 12 Feb 2022 [s42–s51]:**
- Run 23043055, production_pp500_2022: total ≈ 2238 Hz to DAQ. FCS triggers include fcsDY (446 Hz recorded, ≈ unprescaled, ≈ 20% of DAQ), fcsJPsi (109 Hz DAQ), fcsJP2 (159 Hz DAQ), di-jet, EM, hadron and high-tower triggers. Thresholds not given.
- Offline: ECal di-photon π⁰ peak at ≈ 0.135 GeV (647091 entries); ECal–HCal MIP matching Y(ECal) − Y(HCal) peaked at 0 (RMS 15.48); HCal MIP peak fitted at 1.574 ± 0.006 vs expected ≈ 1.5 (units not given).
- Luminosity behind goals: ≈ 3 weeks lost (cryogenics cool-down delay, Blue snake coils, AGS MG); polarization in the upper 40s % vs planned 55%; 4-week extension requested, projecting to 90% of the FoM goal.

**Physics reach (selected):** quarks up to x ~ 0.5, gluons down to x ~ 0.005; transversity at 0.3 < x < 0.5; direct photons 0.0025 ≲ x ≲ 0.025 (nuclear gluons); Drell–Yan 0.001 ≲ x ≲ 0.01 (nuclear sea); charge-tagged jet A_N projection at 510 GeV, P = 60%, 350 pb⁻¹ with up to 10σ separation.

## What it does not give

- No calibrated ECal/HCal energy resolution — only the design requirements.
- No SiPM type, bias, DEP boards, radiation damage, dark current, annealing or temperature control.
- No trigger thresholds; no exact talk date or venue.

## Source issues and caveats

- **[source issue]** ECal "33 cm" tower length inconsistent with "66 sampling cells with 1.5 mm Pb / 4 mm Sc" (66 × 5.5 mm = 36.3 cm without wrap; 37.73 cm with wrap per the email).
- **[source issue]** [s11] charge mis-ID panel legends read "σ_pT = …", copied from the resolution panels.
- **[source issue]** [s31] projection panels say 2.5 < η < 4.5, while the upgrade covers 2.5 < η < 4 elsewhere (and [s30] labels direct photons 2.8 < η < 3.8) — probably older plots.
- [s11] 200 GeV fits at p_T = 5 GeV/c give 8.3% mis-ID and 35.6% resolution, marginally above the stated 8% / 35%; the last histogram bins sit above the fits.
- [s8] "Totle" for "Total"; cut formula printed without absolute value and copied into the Y panel.
- [s25] projection assumes P = 60%; Run 22 achieved upper 40s %.
- Not peer-reviewed; internal/collaboration material published with Zhiwen's agreement. Many plot values eyeballed.

## FCS cross-checks (vs [[ruan2026-fcs-specs-email-note]])

- Agree: 7 m vs ECal front z = 710.16 cm / HCal front z = 782.63 cm; 1496 and 520 channels; 66-cell 1.5 mm Pb / 4 mm Sc ECal; HCal 20 mm / 3 mm, 10 × 10 × 84 cm³ vs 9.99 × 9.99 cm, 84.24 cm; HCal ≈ 4.5 λ_I vs 4.45 λ; 18 X₀ vs 18.1 X₀; two halves.
- ECal face 5.52 cm vs 5.542 cm (rounding).
- **ECal tower length 33 cm vs 37.73 cm** — unexplained.
- **ECal depth 0.85 λ_I vs 0.93 λ** (recomputed from layers ≈ 0.90 λ_I).
- DEP boards (24 per half ECal, 9 per half HCal) appear only in the email.
- Readout end not addressed in the talk; Wang 2024 says SiPM electronics "on the front face", the email says ECal fibres "read out at the back". See [[open-questions]].

## Relevance

Fullest single description of the as-built [[star-fcs]] and its role in the forward physics programme, plus a snapshot of Run 22 operations: FCS trigger menu and rates ([[star-daq-trigger]]), first offline π⁰ and MIP signals, and run-plan context (Run 22 pp 500 GeV, 2023/2025 Au+Au 200 GeV, 2024 pp and p+Au 200 GeV). Mid-rapidity triggers in the same DAQ table (BHT3, JP2, EHT1, dimuon) and TOF/BTOW/ETOW rates connect to [[star-bemc]], [[star-eemc]], [[star-barrel-tof]] and [[star-mtd]].

## Related

- Synthesis: [[star-fcs]] · [[star-daq-trigger]] · [[star-bemc]] · [[star-eemc]] · [[star-barrel-tof]] · [[star-mtd]] · [[rhic-detector-status]] · [[open-questions]]
- Notes: [[tsai2015-fcs-prototype-note]] (2014 prototype) · [[wang2024-star-forward-upgrade-note]] (QM2023 proceedings) · [[ruan2026-fcs-specs-email-note]] (construction specs) · [[star2026-detector-status-note]]
