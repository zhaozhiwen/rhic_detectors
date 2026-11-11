---
title: "Llope 2012 — Multigap RPCs in the STAR experiment at RHIC (curated notes)"
type: raw-note
source_type: paper
companion: llope2012-star-mrpc-systems.md
authors: "W.J. Llope (Rice University), for the STAR Collaboration"
journal: "Nucl. Instrum. Meth. A 661 (2012) S110–S113 (RPC 2010 workshop proceedings)"
doi: "10.1016/j.nima.2010.07.086"
arxiv: none
notes_updated: 2026-11-11
ingested_version: "Publisher version of record, read 2026-11-06 via Route 1 (ScienceDirect HTML in Chrome, JLab access), verified against the publisher PDF (4 pages)"
earlier_version: []
later_version: []
published_version: "Nucl. Instrum. Meth. A 661 (2012) S110–S113 -- this is the ingested version"
version_facts: "Available online 5 August 2010; issue date 1 January 2012 (X Workshop on RPCs and Related Detectors, RPC 2010; eds. N. Herrmann, S.P. Ratti, R. Santonico). No arXiv version found (arXiv title search: 0 results). Status statements are as of mid-2010 (Run 10 ongoing)."
versions_checked: 2026-11-09
---

# Llope 2012 — Curated Notes

> **Full source:** [llope2012-star-mrpc-systems](llope2012-star-mrpc-systems.md) · Companion notes to [llope2012-star-mrpc-systems](llope2012-star-mrpc-systems.md) (full source; a full-content paraphrase).
> **DOI:** https://doi.org/10.1016/j.nima.2010.07.086 · arXiv: none

## Bibliographic

- **Title:** Multigap RPCs in the STAR experiment at RHIC
- **Author:** W.J. Llope (Rice University), for the STAR Collaboration (single named author).
- **Journal:** Nucl. Instrum. Meth. A 661 (2012) S110–S113; online 5 Aug 2010 (RPC 2010 proceedings).

## What kind of paper

4-page workshop overview of both STAR MRPC systems: the as-built barrel TOF (MRPC stack, tray/system counts, TINO/TDIG/TCPU/THUB electronics, timing by run) and the planned MTD (LMRPC prototypes, final WMRPC design). Written during Run 10.

## Abstract (paraphrased)

STAR has installed a 50 m² MRPC time-of-flight system read out with custom electronics built on CERN NINO and HPTDC chips, after prototypes ran in STAR 2002–2006; ~70% was installed for Run 9. A future Muon Telescope Detector would use very large double-ended MRPCs behind the magnet back-legs to identify muons by timing. Design and performance of the TOF prototypes, final TOF and MTD prototypes are presented.

## Key numbers

**TOF MRPC (Section 2)**

| Item | Value |
|---|---|
| Stack | single stack, five 220 μm gaps |
| Glass | inner 0.54 mm float glass; outer 1.1 mm with graphite electrodes; ~10¹³ Ω cm |
| Electrode | graphite, 10⁵ Ω/□ |
| HV | ~14 kV across electrodes |
| Gas | 95% R-134a + 5% isobutane |
| Pads | one row of six, 3.5 × 6.1 cm², read from one edge via two twisted-pair cables |
| Signal | ~25 fC/hit |
| Dark rate | ~1 Hz/cm² (~20 Hz/pad) |
| CERN test beam | 200 Hz/cm² (RHIC-II max); > 95% efficiency plateau; pure-stop σ < 75 ps |

**TOF prototypes and system (Section 3)**
- Prototypes: TOFr (Run 3), TOFr′ (Run 4) via CAMAC/TOFp with long cables; TOFr5 (Runs 5–6) on-board HPTDC. MRPC design final 2001. No ageing seen in MRPCs used in all three prototypes.
- Final trays first in Run 8 (5 trays); MAXIM 3760 amplifier replaced by NINO. 94 trays before Run 9; all 120 before Run 10.
- Layout: 120 trays = two rings × 60 just outside TPC; each tray ~0.9 in η, 1/60 of φ; 32 MRPCs/tray, nearly projective → 3840 MRPCs, 23 040 channels. Occupancy ~12% (central full-energy Au+Au).
- MRPCs made in China; trays built/tested in Texas, retested at BNL.
- Electronics: TINO = 4 MRPCs (24 ch) → 3 NINO, plus multiplicity level; TDIG = 3 HPTDC, 40 MHz clock, very-high-resolution mode ~24.4 ps LSB, leading+trailing edge on same channel → ToT; INL of all 23 040 channels measured on bench; TCPU = 8 TDIG per tray, tray multiplicity 0–24 to earliest trigger level; THUB = 4 boards × 30 trays (240 TDIG), SIU/RORC to DAQ, one THUB is master clock.
- Power/cooling: ~100 W per tray (8 TINO + 8 TDIG + 1 TCPU); ~90% removed by 1/4 in. × 3/8 in. copper water loop; Al cover = mechanical + RF shield.
- Calibration (stop side): HPTDC INL → per-channel offsets vs start → ToT slewing. Run 9 p+p calibrated per 24 channels (one TDIG).
- Fig. 3 (Run 9): constant fit p0 = 0.1119 ± 0.0001 ns, χ²/ndf 2059/687.
- Reliability: 8 of 94 Run 9 trays had problems (2 LV sense wires, 5 HV cables, 1 TCPU), all repaired; Run 10: 1 tray off (HV cable), 3 dead channels.

**Table 1 — timing by run (ps)**

| Run | Beams, √s_NN (GeV) | Start | Total | Stop |
|---|---|---|---|---|
| 3 | d+Au 200 | 85 | 120 | 85 |
| 3 | p+p 200 | 140 | 160 | 80 |
| 4 | Au+Au 62 | 55 | 105 | 89 |
| 4 | Au+Au 200 | 27 | 86 | 82 |
| 5 | Cu+Cu 200 | 50 | 92 | 75 |
| 5 | Cu+Cu 62 | 82 | 125 | 94 |
| 8 | p+p 200 | 83 | 112 | 75 |
| 9 prelim. | p+p 500 | 85 | 115 | 78 |
| 9 prelim. | p+p 200 | 81 | 111 | 74 |
| 10 prelim. | Au+Au 200 | 30 | 87 | 82 |

- Final-tray pure stop 74–82 ps; Run 9/10 preliminary, ~10 ps improvement possible; start detector changed before Run 8 (not named).

**PID reach (Introduction)**
- Before TOF: π/K (p) PID only up to ~0.7 (1.0) GeV/c.
- 100 ps total: π:K:p to ~1.7–1.9 GeV/c; (π+K):p to ~2.9–3.1 GeV/c; TOF + dE/dx covers ~98% of hadron spectra.
- Beam-energy scan 5 < √s_NN < 39 GeV starting Run 10.

**MTD (Section 4)**
- Concept: BEMC + magnet back-legs ≈ 6 interaction lengths between TPC and MTD; muons = TPC tracks with matching MTD time and position. Prototypes since Run 7.
- LMRPC: double stack, ten 250 μm gaps (5 per stack), 12.6 kV per stack, 95% C₂H₂F₄ + 5% isobutane, six 87 × 2.5 cm² strips, double-ended; > 95% efficiency for 12.5 < HV < 13.0 kV; ~70 ps; < 1 cm along strip.
- MTD7 (two LMRPCs end to end; simple FEE, long cables, trigger-system digitization): ~300 ps in STAR (long cables, electronics). MTD9: three LMRPCs side by side, TOF electronics.
- Final WMRPC: 117 detectors; single stack, five gaps; 91.5 × 58.0 × 3 cm³; twelve 87 × 3.8 cm² strips, 0.6 cm gaps; read at both ends with TOF electronics; five trays per back-leg; three before Run 11; full MTD hoped before Run 13.
- **[note]** L3-derived: 117 × 12 = 1404 strips → 2808 TDC channels (not stated); 23 040 × 21.35 cm² = 49.2 m² TOF pad area.

## Methods / setup

- Overview of test-beam (CERN, Fig. 1 HV scan 14.75–16.0 kV) and in-STAR running; resolutions from TOF − start with stop-side calibrations listed above; Table 1 compiles start/total/stop per run.

## What the paper does not give

- Barrel TOF radius, total η range, MRPC outer dimensions, inter-pad gap, which pad dimension is along z vs φ, MRPC tilt angles, start-detector name, local-z/hit-position correction, in-situ efficiency.
- MTD signal propagation speed; MTD DAQ path; WMRPC strip orientation relative to beam (Fig. 4 has no axes).

## Source issues and caveats

- **[source issue]** Abstract "~70%" installed for Run 9 vs Section 3 "three-quarters" (94/120 = 78.3%).
- **[source issue]** "100 GeV/c/nucleon" acceptable; BES range "5 < √s_NN < 39 GeV/nucleon" has redundant "/nucleon".
- **[source issue]** Text says Fig. 3 is vs "board number"; plot x-axis is "Channel ID" (0–~23 000).
- **[source issue]** "WMPRCs" typo for WMRPCs.
- Run 9/10 Table 1 values preliminary (fast-offline, partly uncalibrated TPC). Two Table 1 rows (Cu+Cu 200; Run 9 p+p 200) differ from quadrature by 1–2 ps (L3 check).
- HV in STAR operation not stated (only "~14 kV" and test-beam scan).
- Fig. 3 ndf = 687 → 688 points < 752 TDIGs installed; possibly 86 trays (L3 inference, not stated).
- Route caveat: Route 1 HTML verified against PDF; pdftotext glyph artefacts only ("TOFru", "34", "o"). Figure readings approximate.

## Relevance

Primary single source for the as-built STAR barrel TOF counts (120 trays, 3840 MRPCs, 23 040 channels), its MRPC stack and electronics chain, and the in-STAR timing table; also the first compact description of the MTD LMRPC/WMRPC design and its ~6 λ absorber concept.

## Related

- Synthesis: [star-barrel-tof](../wiki/synthesis/star-barrel-tof.md) · [star-mtd](../wiki/synthesis/star-mtd.md) · [mrpc-technology](../wiki/synthesis/mrpc-technology.md) · [star-daq-trigger](../wiki/synthesis/star-daq-trigger.md) · [star-magnet-absorber](../wiki/synthesis/star-magnet-absorber.md) · [open-questions](../wiki/synthesis/open-questions.md)
- Notes: [shao2002-mrpc-beam-test-note](shao2002-mrpc-beam-test-note.md) · [wu2007-star-barrel-tof-note](wu2007-star-barrel-tof-note.md) · [ruan2009-mtd-concept-note](ruan2009-mtd-concept-note.md) (ref. [14], MTD concept and MTD7) · [yang2014-mtd-cosmic-calibration-note](yang2014-mtd-cosmic-calibration-note.md) · [huang2016-mtd-muon-id-note](huang2016-mtd-muon-id-note.md) · [beddo2003-bemc-note](beddo2003-bemc-note.md) (BEMC part of the MTD absorber)
- [schambach2006-star-tof-electronics-note](schambach2006-star-tof-electronics-note.md) — 2006 design paper on the same TINO/TDIG/TCPU/THUB electronics (board internals, HPTDC arithmetic, DAQ link); prints the pad as 3.3 cm × 6.1 cm vs 3.5 × 6.1 cm² here, and glass 0.7/0.55 mm vs 1.1/0.54 mm (unresolved, [open-questions](../wiki/synthesis/open-questions.md) #16)
