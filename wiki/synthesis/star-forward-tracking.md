---
title: STAR Forward Tracking System (FST silicon disks + sTGC tracker)
tags: [experiment, detector, status]
sources: [star2018-forward-upgrade-proposal.md, star2018-forward-upgrade-proposal-note.md, wang2024-star-forward-upgrade.md, wang2024-star-forward-upgrade-note.md, gagliardi2022-star-forward-upgrade-talk.md, gagliardi2022-star-forward-upgrade-talk-note.md, star2026-detector-status.md, star2026-detector-status-note.md]
updated: 2026-11-16
---

# STAR Forward Tracking System (FTS)

Charged-particle tracker of the STAR Forward Upgrade on the west side (the side facing the blue beam), 2.5 < η < 4, in the 0.5 T solenoid field, in front of the [star-fcs](star-fcs.md) calorimeters. Two parts: three silicon mini-strip disks (Forward Silicon Tracker, **FST**) inside the TPC inner field cage and four small-strip thin gap chamber planes (**sTGC**, called **FTT** in Wang 2024) in the pole-tip opening; up to 3 + 4 = 7 points per track. Sources: the November 2018 STAR design proposal (design values; not peer-reviewed) [star2018-forward-upgrade-proposal-note](../../raw/star2018-forward-upgrade-proposal-note.md), the February 2022 STAR Juniors talk (not peer-reviewed) [gagliardi2022-star-forward-upgrade-talk-note](../../raw/gagliardi2022-star-forward-upgrade-talk-note.md), the QM2023 proceedings [wang2024-star-forward-upgrade-note](../../raw/wang2024-star-forward-upgrade-note.md) and the October 2026 status sheet [star2026-detector-status-note](../../raw/star2026-detector-status-note.md).

## Role and requirements

- Charge sign of hadrons for transverse-spin asymmetries (π⁺/π⁻ separation up to 80 GeV/*c*) and of e⁺e⁻ pairs for Drell–Yan; vertex association and pointing to the calorimeters against pile-up; momentum and charged-track veto for electron/photon ID (hadron suppression by 3-4 orders of magnitude together with the FCS) [star2018-forward-upgrade-proposal-note](../../raw/star2018-forward-upgrade-proposal-note.md).
- A+A: p_T of charged particles over 0.2 < p_T < 2 GeV/c with 20-30% 1/p_T resolution (2018 Table 3-1; same in the 2022 talk).
- Low material, to limit multiple scattering and conversions; conversion background in the Drell–Yan study was not modelled in 2018 because the beam pipe and FTS supports were not yet designed.

## Design (2018 proposal) vs as built

| Item | 2018 design [star2018-forward-upgrade-proposal-note](../../raw/star2018-forward-upgrade-proposal-note.md) | As built (2022–2024) |
|---|---|---|
| Layout | 3 Si disks + 4 sTGC wheels | same: FST 3 disks + FTT 4 planes ([wang2024-star-forward-upgrade-note](../../raw/wang2024-star-forward-upgrade-note.md)) |
| FST z | 139.9, 163.2, 186.5 cm (lever arm set by η 2.5–4 and the beam-pipe / TPC inner-field-cage radii) | 152 cm to 179 cm (Wang 2024); 152, 165, 179 cm in the QM2023 slides quoted in the Wang 2024 Layer-3 file |
| FST sensors | single-sided double-metal Si mini-strips (Hamamatsu), fine φ, coarse r, readout at the outer radius | same type; 12 modules per disk, 3 Hamamatsu mini-strip sensors per module ([gagliardi2022-star-forward-upgrade-talk-note](../../raw/gagliardi2022-star-forward-upgrade-talk-note.md)) |
| FST wedge / module | 3 sensors + 8 APV chips on a flex hybrid; PPS + 10% carbon-fibre support; inner and outer sensors on opposite faces; [note] 288 APV / (3 × 8) = 12 wedges per disk | 12 modules per disk (talk, Wang 2024) |
| FST material | ≤ 1% X₀ per layer | ~1.5% X₀ per disk (talk) |
| FST readout | APV25-S1 (128 channels, 4 μs pipeline, 40 MHz); 288 chips (in hand); IST DAQ and 3M NOVEC cooling re-used ([star-daq-trigger](star-daq-trigger.md)) | APV25-S1, IST electronics, DAQ and cooling re-used (talk, Wang 2024; Wang prints "AVP25-S1"); bias 140 V inner / 160 V outer sensors (Wang 2024) |
| sTGC z | 273, 303, 333, 363 cm (30 cm spacing) | 300 cm to 360 cm (Wang 2024); 307, 325, 343, 361 cm (QM2023 slides, via the Wang 2024 Layer-3 file) |
| sTGC modules | four square 60 cm × 60 cm double-sided sTGCs per plane; two layers with perpendicular strips (x-y) | four **pentagonal** modules per plane, two sTGCs per module, X, Y and two diagonal layers (Wang 2024); x, y, u strips (talk) |
| sTGC chamber | 50 μm Au-plated W wires, 1.8 mm pitch, 1.4 mm to the cathodes, 2900 V; graphite cathode 100 kΩ on 100 μm G-10; strip pitch 3.2 mm (< 100 µm design, < 50 µm in ATLAS prototypes) | HV 2900 V (Wang 2024); resolution < 200 μm; ~0.5% X₀ per layer (talk) |
| sTGC gas | 55% CO₂ + 45% n-pentane | same (Wang 2024) |
| sTGC readout | re-used STAR TPC electronics (ALTRO), freed by the iTPC upgrade after 2019; 24000 channels (strips cut in 4 × 15 cm) | **VMM** electronics following the ATLAS design (Wang 2024, talk); online plots show 96 VMM per plane (talk s46, in the Gagliardi Layer-3 file) |
| sTGC construction | Shandong University, ≈ $200K (STAR Chinese groups) | built and tested; test-stand efficiency 98.7% (X), 98.2% (Y) (talk) |
| Mounting | Si disks inside the IDS cone, rail extension of the West Support Cone (FGT-style); sTGC ≈ 800 pounds (4 × ≈ 200) on EPD brackets and pole-tip/EEMC holes | sTGC planes on the beam pipe downstream of the FST (talk s9) |

**[note]** Two design changes stand out: the sTGC moved from square modules with TPC (ALTRO) readout to pentagonal ATLAS-style modules with VMM readout, and both detectors moved in z (FST outermost disk 186.5 → 179 cm; sTGC first plane 273 → ≈ 300 cm). No ingested source explains why ([open-questions](open-questions.md) #25).

## Silicon details (2018 design) [star2018-forward-upgrade-proposal-note](../../raw/star2018-forward-upgrade-proposal-note.md)

- Model: STAR IST — S/N 25:1, ≈ 99% hit efficiency, 4% dead time at 1 kHz.
- Occupancy (0-3% central Au+Au 200 GeV, from PHOBOS multiplicities): 3.2% at η = 4, 10% at η = 2.5.
- DAQ: IST system (built for 864 APV) — 6 readout modules per readout controller, ≤ 24 APV per module, front-end cables up to 24 m (Fig. 5-6 label "120 feet"), 12-bit digitization at 37.532 MHz, ALICE DDL at 2.125 Gbps to a Linux PC; slow control over Ethernet → DDL → RDO → I²C.
- Cooling: ≈ 0.3 W per APV, IST NOVEC system re-used.
- Radiation: APV in IBM 0.25 μm, 20+ Mrad; lifetime NIEL 1–7×10¹² cm⁻² (≈ 1.2×10¹² outer, 2×10¹² inner sensors), scaled from an IST Run-14 NIEL < 5×10¹⁰ cm⁻²; Table 5-1 dose at r = 2.5 cm 5.3-28 krad (200 GeV Au+Au) and 29-133 krad (500 GeV p+p) per 12 weeks. Power off during injection and machine studies.
- Alignment: sensor geometry known to better than 10 µm; planes then aligned with tracks.

## Simulated performance

| Study | Result | Source |
|---|---|---|
| 2018, single particles (3 Si + 4 sTGC, Stv Kalman, ≥ 4 hits) | efficiency > 80% up to 100 tracks/event, > 50% at 300 (the figure supports the 300-track claim only marginally, global tracks ≈ 0.5, primary ≈ 0.2–0.3) | [star2018-forward-upgrade-proposal-note](../../raw/star2018-forward-upgrade-proposal-note.md) |
| 2018, PYTHIA6 pions | charge mis-ID 0.86%; relative 1/p_T resolution ≈ 10–14% for p_T up to ≈ 2 GeV/c (read from figures) | same |
| 2018, track density | PHOBOS: 600 → 250 tracks (most central) and 300 → 150 (15-25% central) over 2.5 < η < 4 | same |
| 2022 talk (FTT + FST, p_T < 5 GeV/c) | charge mis-ID < 6% (8%), p_T resolution < 35% at √s = 500 (200) GeV; 500 GeV fits mis-ID 0.1% + 1.1% × p_T, resolution 14.9% + 4.0% × p_T | [gagliardi2022-star-forward-upgrade-talk-note](../../raw/gagliardi2022-star-forward-upgrade-talk-note.md) |

## Reconstruction and data (as built)

- Cellular Automaton seeding within each detector, combined fit with the other, constrained by the TPC vertex or the beamline [wang2024-star-forward-upgrade-note](../../raw/wang2024-star-forward-upgrade-note.md).
- Run 22 p+p 510 GeV: track–HCal matching peaks at ΔX, ΔY ≈ 0, with ΔX side peaks at ±60 cm from the two HCal halves (Wang 2024).
- Run 22 online (12 Feb 2022): one sTGC quadrant chamber (plane 2) stopped holding HV and needed repair before Run 23; a region missing in the FST disk-3 hit map (talk s45–s47, in the Gagliardi Layer-3 file) [gagliardi2022-star-forward-upgrade-talk-note](../../raw/gagliardi2022-star-forward-upgrade-talk-note.md).
- Installed for Run 22 (installation completed 2021, Wang 2024); used in Run 22 and Run 23.

## Status (October 2026) [star2026-detector-status-note](../../raw/star2026-detector-status-note.md)

- sTGC: availability "All", **dismounted**.
- FST: availability "One of two halves (3 layers)", **dismounted**. [note] Read with the 3-disk FST, presumably one half of each disk remains; the sheet does not say so ([rhic-detector-status](rhic-detector-status.md)).

## Open questions

- Exact as-built z positions and module geometry are given in the peer-reviewed source only as ranges (152–179 cm, 300–360 cm); why the sTGC changed shape and readout is not stated ([open-questions](open-questions.md) #25). Candidate sources: STAR Note SN0648 and the STAR ForwardUpgrade.v20 document (both on the STAR drupal site), and the separate FST paper arXiv:2407.09952 named in the Wang 2024 Layer-3 file.
- No measured momentum resolution or efficiency in data in any ingested source.

## Related
[star-fcs](star-fcs.md) · [star-daq-trigger](star-daq-trigger.md) · [rhic-detector-status](rhic-detector-status.md) · [open-questions](open-questions.md)
