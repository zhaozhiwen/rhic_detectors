---
title: "Wang 2024 — STAR forward detector upgrade status and performance (curated notes)"
type: raw-note
source_type: paper
companion: wang2024-star-forward-upgrade.md
authors: "Zhen Wang (Shandong University) for the STAR Collaboration"
journal: "EPJ Web of Conferences 296, 16003 (2024) — Quark Matter 2023 proceedings (Spin/EIC Physics section)"
doi: 10.1051/epjconf/202429616003
arxiv: none
notes_updated: 2026-11-11
ingested_version: "publisher PDF (open access, CC BY 4.0; 4 pages; published online 2024-06-26), captured 2026-11-06 via Route 3"
earlier_version: []
later_version: []
published_version: "EPJ Web of Conferences 296, 16003 (2024) -- this is the ingested version"
version_facts: "No arXiv version found (title searches, 2026-11-06). The matching QM2023 talk slides (23 slides) exist and were consulted by the Layer-3 capture only for [note] items labelled 'from the talk slides'; they were not ingested in this repo. Route re-check 2026-11-11: EPJ Web of Conferences still serves PDF only (no HTML full text)."
versions_checked: 2026-11-11
---

# Wang 2024 — Curated Notes

> **Full source:** [wang2024-star-forward-upgrade](wang2024-star-forward-upgrade.md) · Companion notes to [wang2024-star-forward-upgrade](wang2024-star-forward-upgrade.md) (full source).
> **DOI:** [10.1051/epjconf/202429616003](https://doi.org/10.1051/epjconf/202429616003) · **PDF:** `assets/wang2024-star-forward-upgrade/source.pdf`

## Bibliographic / source

- **Title:** STAR forward detector upgrade status and performance
- **Author:** Zhen Wang (Shandong University), for the STAR Collaboration.
- **Published:** EPJ Web Conf. 296, 16003 (2024); Quark Matter 2023 (30th Int. Conf. on Ultra-Relativistic Nucleus-Nucleus Collisions). No arXiv version.

## What kind of source

Short (4-page) peer-reviewed conference proceedings; 3 figures, no tables, no equations. Status report on the as-built forward upgrade after Run22/Run23. Qualitative on performance: no energy or momentum resolution numbers.

## Summary (paraphrased)

STAR completed a forward upgrade before RHIC Run 2022: the Forward Tracking System (Silicon tracker FST + small-strip TGC tracker FTT) and the Forward Calorimeter System (ECal + HCal), covering 2.5 < η < 4 on the side facing the blue beam. Physics aims: cold QCD at very high and very low Bjorken x, and longitudinal structure of the heavy-ion initial state. The proceedings describes the subsystems, forward-tracking software, track–HCal matching, ECal π⁰ calibration and SiPM radiation monitoring.

## Key numbers

- Coverage 2.5 < η < 4; extends x reach to x < 2×10⁻³ and x > 0.3. Installation completed 2021; in trigger and data taking since 2022; ran in Run22 and Run23.
- **FST:** 3 disks at z = 152 cm to 179 cm, 12 modules per disk (fine φ, coarse R); reuses IST electronics, DAQ, cooling; bias 140 V (inner) / 160 V (outer) sensors.
- **FTT (sTGC):** 4 planes × 4 pentagon modules at z = 300 cm to 360 cm, inside the magnet pole-tip opening; two sTGCs per module with X, Y and two diagonal layers; gas 45% n-pentane + 55% CO₂; VMM readout (ATLAS design); HV 2900 V.
- **Tracking:** up to 3 FST + 4 FTT = 7 points; Cellular Automaton seeding, combined fit, TPC vertex or beamline constraint.
- **Track–HCal matching (Run22 p+p 510 GeV):** ΔX and ΔY peak near zero; ΔX side peaks at ±60 cm attributed to the two independent HCal modules in X.
- **FCS:** ~7 m from IP. ECal = refurbished PHENIX Pb–scintillator, 1496 channels. HCal = Fe–scintillator sandwich, 520 channels. SiPM readout electronics "on the front face", developed with EIC R&D.
- **SiPM radiation:** LED system; leakage current in LED runs tracks damage; within expectations for most SiPMs; attenuator and bias adjusted regularly to recover gain.
- **ECal calibration:** π⁰ invariant mass, per-channel gain factors; after two iterations deviation from PDG mass below 10% (red in Fig. 3) — "every channel" per text; Fig. 3 still shows about 20 non-red cells, mostly in the rightmost column.
- **HCal calibration:** MIP-based, in progress at writing.
- ECal map in Fig. 3 = one half, 22 columns × 34 rows.

## Methods / setup

Status report; methods described only qualitatively (CA tracking, π⁰ iterative gain calibration, MIP calibration plan, LED leakage-current monitoring).

## What it does not give

- No energy resolution (ECal or HCal), no momentum resolution, no tower dimensions or depths, no trigger rates or thresholds, no SiPM type or radiation-dose numbers, no jet/electron/photon reconstruction results.

## Source issues and caveats

- **[source issue]** FST readout chip printed "AVP25-S1"; almost certainly APV25-S1 (STAR IST chip; the talk slides write "APV25").
- **[source issue]** Fig. 3 caption says the right panel is "one ECal channel", but its title is "Invariant mass plot for FCS ECal" and the peak holds about 7×10⁴ counts — more likely a sum over channels; not settled from the paper.
- Fig. 3 maps carry no "before"/"after" labels; ordering inferred from the caption.
- FTT range "300 cm to 360 cm" is rounded (talk slides: last disk at 361 cm).

## FCS cross-checks (vs [ruan2026-fcs-specs-email-note](ruan2026-fcs-specs-email-note.md) and the unpublished QM2023 slides, from the Layer-3 file)

- Channel counts agree: ECal 1496 = 2 × 22 × 34; HCal 520 = 2 × 13 × 20.
- Location agrees: "about 7 m" vs ECal front z = 710.16 cm, HCal front z = 782.63 cm.
- ΔX ±60 cm side peaks are only approximately half the width of one HCal half (13 × 9.99 cm = 129.9 cm; half ≈ 65 cm).
- η: paper 2.5 < η < 4 vs email "roughly 2.2 < eta < 4.3" — the 2.2 is the outer geometric corner (ECal corner η = 2.23, outer edge 2.46; HCal corner 2.27).
- **ECal tower length:** QM2023 slides 33 cm vs email 37.73 cm stack depth — unexplained.
- **ECal depth in λ:** slides 0.85 λ_I vs email 0.93 λ (recomputed from the layer stack: 0.90 λ_I); X₀ agrees (18 vs 18.1; recomputed 18.0).
- **Readout end:** paper "SiPM readout electronics on the front face" vs email ECal WLS fibres "read out at the back" — cannot be resolved from these sources. See [open-questions](../wiki/synthesis/open-questions.md).

## Relevance

Most recent peer-reviewed description of the as-built STAR forward upgrade ([star-fcs](../wiki/synthesis/star-fcs.md)) and its first performance in Run22: confirms channel counts, PHENIX-module ECal, Fe/scint HCal, SiPM radiation monitoring and π⁰ calibration. The tracking (FST, FTT) is context for track–calorimeter matching. For the October 2026 hardware status see [star2026-detector-status-note](star2026-detector-status-note.md) and [rhic-detector-status](../wiki/synthesis/rhic-detector-status.md).

## Related

- Synthesis: [star-fcs](../wiki/synthesis/star-fcs.md) · [rhic-detector-status](../wiki/synthesis/rhic-detector-status.md) · [star-daq-trigger](../wiki/synthesis/star-daq-trigger.md) · [open-questions](../wiki/synthesis/open-questions.md)
- Notes: [tsai2015-fcs-prototype-note](tsai2015-fcs-prototype-note.md) (2014 prototype) · [gagliardi2022-star-forward-upgrade-talk-note](gagliardi2022-star-forward-upgrade-talk-note.md) (2022 talk: specs, triggers, Run 22) · [ruan2026-fcs-specs-email-note](ruan2026-fcs-specs-email-note.md) (construction specs) · [star2026-detector-status-note](star2026-detector-status-note.md)
