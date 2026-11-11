---
title: "Schambach 2006 — STAR TOF readout electronics, DAQ, and cosmic-ray test stand (curated notes)"
type: raw-note
source_type: paper
companion: schambach2006-star-tof-electronics.md
authors: "J. Schambach, L. Bridges, G. Eppley, J. Hoffmann, K. Kajimoto, J. Liu, W. J. Llope, C. Mesa, T. Nussbaum (UT Austin, Blue Sky Electronics, Rice, M6 Research)"
journal: "2006 IEEE Nuclear Science Symposium Conference Record, vol. 1, pp. 485–488 (paper N14-161; San Diego)"
doi: "10.1109/NSSMIC.2006.356203"
url: "https://ieeexplore.ieee.org/document/4179042"
arxiv: none
notes_updated: 2026-11-10
ingested_version: "Publisher version of record, read 2026-11-10 via Route 1 (IEEE Xplore full-text HTML in Chrome, institutional access), every number and the formula checked against the publisher PDF (4 pages)"
earlier_version: []
later_version: []
published_version: "2006 IEEE NSS Conference Record, vol. 1, pp. 485–488 -- this is the ingested version"
version_facts: "IEEE Xplore document 4179042; ISBN 1-4244-0560-2 (print). HTML and PDF texts agree. No arXiv version recorded. Written during the barrel-TOF design phase (2006), before the final trays were installed; the as-built system is described in llope2012-star-mrpc-systems (ingested)."
versions_checked: 2026-11-10
---

# Schambach 2006 — Curated Notes

> **Full source:** [schambach2006-star-tof-electronics](schambach2006-star-tof-electronics.md) · Companion notes to [schambach2006-star-tof-electronics](schambach2006-star-tof-electronics.md) (full source; a full-content paraphrase).
> **DOI:** https://doi.org/10.1109/NSSMIC.2006.356203 · IEEE Xplore: https://ieeexplore.ieee.org/document/4179042 · arXiv: none

## Bibliographic

- **Title:** STAR Time of Flight Readout Electronics, DAQ, and Cosmic Ray Test Stand
- **Authors:** J. Schambach, L. Bridges, G. Eppley, J. Hoffmann, K. Kajimoto, J. Liu, W. J. Llope, C. Mesa, T. Nussbaum (UT Austin; Blue Sky Electronics, Houston; Rice University; M6 Research, Austin). Not alphabetical → slug uses the first author.
- **Venue:** 2006 IEEE Nuclear Science Symposium Conference Record, vol. 1, pp. 485–488, paper N14-161 (San Diego).

## What kind of paper

4-page IEEE NSS conference record from the electronics group, written while the barrel TOF was still being designed. Its substance is the readout chain TINO → TDIG → TCPU → THUB → DAQ (with the TPMD start side), the HPTDC timing arithmetic, a short description of the MRPC module and tray, the system timing budget, and a cosmic-ray test stand result. No beam-test or in-STAR performance.

## Abstract (paraphrased)

The planned STAR TOF has 3840 six-pad MRPCs on 120 trays, 23040 channels. Each tray carries 192 channels and three card types — an analog front end built on the CERN NINO chip (TINO), a digitizer built on the CERN HPTDC (TDIG), and a buffer/formatter (TCPU). Every 30 trays feed one THUB, which interfaces to the STAR trigger and ships the data over optical fibre to a DAQ receiver. A cosmic-ray stand (three scintillators, four MRPC modules, prototype electronics) was built to see what timing the full system should reach; it gives 80–110 ps overall for cosmic rays.

## Key numbers

**System counts (abstract, Sections II–III)**

| Item | Value |
|---|---|
| MRPCs | 3840, 6 pads each |
| Trays | 120, as two adjoining cylindrical shells of 60; each shell spans ≈ 1 unit of η |
| Channels | 23040 total; 192 per tray |
| MRPC modules per tray | 32, 6 channels each |
| Pad size | **3.3 cm × 6.1 cm** (see caveats: 3.5 × 6.1 cm² in Llope 2012) |
| Acceptance (Sec. I) | TOF barrel \|η\| ≤ ~1; fraction of identified kaons and protons doubles to > 95% inside it |

**MRPC construction (Section II)**

| Item | Value |
|---|---|
| HV | 14 kV across the outer electrodes; internal plates floating |
| Glass | outer plates 0.7 mm, inner plates 0.55 mm |
| Spacers | 0.22 mm diameter nylon fishing line (sets the gap) |
| Electrodes | resistive graphite tape, 10⁵ Ω (per square implied) |
| Pad insulation | 0.35 mm Mylar between pickup pads and outer electrodes |
| Gas | 95% Freon R134a + 5% isobutane, atmospheric pressure |
| Number of gaps | not stated |

**Tray (Section II)**
- Aluminium box, 50 mil (0.13 cm) walls, welded corners; forms all walls of the gas volume but one.
- Lid = the TINO board, custom 1/8" thick: gas-box top, signal feed-through, front-end board and mount for the TDIGs above it.
- TCPU at the high-z end of the tray. Water channel between TINO and TDIG cools both.

**Electronics chain (Section III)**

| Board | Per tray / system | Content |
|---|---|---|
| TINO | 8 per tray, 24 channels each | 3 NINO per board, 8 inputs per NINO; serves 4 six-channel MRPC modules; differential inputs, < 1 ns rise time, adjustable threshold; fixed offset added to the output-pulse length to cover TDC dead time (ToT without a separate trailing-edge TDC) |
| TDIG | 8 per tray, 24 channels each | 3 HPTDC per card; leading edge (time) and trailing edge (ToT) per channel; CANbus for configuration, thresholds, temperature |
| TCPU | 1 per tray | concentrates 8 TDIGs; distributes the 40 MHz clock; tray multiplicity to L0; 12 HPTDCs of 4 TDIGs share one 80 Mbit/s serial port → 2 data cables per tray (4 TDIG, 96 pads each); programmable logic + embedded CPU + SERDES |
| THUB | 4 in total, on the magnet steel | 30 or 31 TCPUs each (two THUBs also take the start-detector TCPU); SERDES over twisted pairs in CAT-6 cables, 4 SERDES channels → FPGA → fast memory; one master THUB makes the low-jitter 40 MHz clock for all; ALICE SIU daughter card, dual-fibre half-duplex link |
| DAQ receiver | — | Linux PC with a PCI RORC card and a Myrinet link to the rest of STAR DAQ |
| TPMD (start side) | replaces TINO | level adapters + discriminators for the VPD PMT signals; can split them for separate vertex-trigger electronics (not part of the TOF electronics) |

**HPTDC arithmetic (Section III)**

| Step | Value |
|---|---|
| Input clock | 40 MHz |
| PLL multiplication | 320 MHz → 3.125 ns period |
| DLL | 32 taps → 97.66 ps per LSB |
| RC interpolation | 4 taps → 24.41 ps bin width |
| Buffers | per-channel FIFO; 256-deep latency buffers; 256-deep common readout FIFO; parallel (8 or 32 bit) or serial readout |
| Modes | triggered (programmable matching window on trigger time tags) or untriggered (every hit to the readout FIFO) |

**[note]** 3.125 ns / 32 = 97.66 ps; 97.66 / 4 = 24.41 ps (L3 arithmetic, as printed).

**Timing budget (Section III)**

| Term | Value |
|---|---|
| Total after all corrections | ≤ 100 ps |
| VPD start | 50 ps |
| Timing corrections | 30 ps |
| Required pure stop | < 80 ps |
| MRPC pure stop with near-final prototype electronics | 50–70 ps |

**[note]** In quadrature √(100² − 50² − 30²) ≈ 81 ps, consistent with "< 80 ps" (L3).

**Cosmic-ray test stand (Section IV)**
- Three plastic scintillators (two above, one below) around a Freon gas box holding up to 4 MRPC modules; PMT signals → TPMD → TDIG; MRPCs → TINO → TDIG; both TDIGs → one TCPU read out over CANbus to a PC; no THUB.
- Analysis: one module = stop, the others = start; hits in a single pad column only; HPTDC non-linearity corrected, then slewing vs ToT.
- Result: overall timing resolution 80–110 ps, module to module. Fig. 3 example: σ = 85.39 ± 1.96 ps (1790 entries; mean −309.8 ± 2.2 ps; RMS 99.5; χ²/ndf 109.7/86).
- **[note]** (L3) The quoted width is of a difference (one module minus the mean of the others); for N = 4 equal modules, 85 ps would be ≈ 74 ps per module. Not unfolded in the paper.

## Methods / setup

- Design description of the on-detector electronics (tray-level buffering, fibre links to DAQ), with one block diagram (Fig. 1) of tray side, start side and THUB.
- TOF = t_stop − t_start; start from the VPD (scintillator + PMT near the beam pipe), digitized like the stops; pulse widths (ToT) sent along for the slewing correction.
- Cosmic stand (Fig. 2) exercises every board except THUB; Fig. 3 is one corrected time-difference histogram. Collecting enough data takes a few days.

## What the paper does not give

- Number of gas gaps, glass type and bulk resistivity, MRPC outer size, inter-pad gap, pad orientation (z vs φ), MRPC tilt angles.
- Tray dimensions (only wall thickness), barrel radius.
- Number of modules in the stand for Fig. 3; per-module (unfolded) resolution; efficiency.
- Data rates, trigger rates or latency numbers behind the buffering requirement; HPTDC INL values.
- Anything about the MTD.

## Source issues and caveats

- **[source issue]** "more that 95%" printed; "more than" meant (Sec. I).
- **Pad size contradiction:** 3.3 cm × 6.1 cm here vs 3.5 × 6.1 cm² in [llope2012-star-mrpc-systems-note](llope2012-star-mrpc-systems-note.md) (also co-authored by W. J. Llope). **[note]** Six 3.3 cm pads = 19.8 cm, six 3.5 cm pads = 21 cm; either fits across the tray only with the short side along φ, so the pad-orientation inference on [star-barrel-tof](../wiki/synthesis/star-barrel-tof.md) stands. Unresolved; see [open-questions](../wiki/synthesis/open-questions.md).
- **Glass contradiction:** outer 0.7 mm / inner 0.55 mm here vs outer 1.1 mm / inner 0.54 mm in [llope2012-star-mrpc-systems-note](llope2012-star-mrpc-systems-note.md). This paper is a 2006 design; Llope 2012 describes the as-built system, but neither says the glass changed. Unresolved.
- **η per shell:** "about 1 unit" here vs ≈ 0.9 per tray in Llope 2012 and \|η\| < 0.9 as built in [yang2014-mtd-cosmic-calibration-note](yang2014-mtd-cosmic-calibration-note.md); consistent with "about".
- Fig. 1 draws half a tray (4 MRPC → 4 TINO → 4 TDIG, "96 CHAN"), matching the two data cables of 96 pads each; the text gives 8 TINO + 8 TDIG per tray. The TCPU–THUB label lists "DATA" twice (as printed).
- Fig. 3 peak at −309.8 ps (constant offset, not discussed); RMS 99.5 > σ shows non-Gaussian tails.
- Design-era paper: counts and construction numbers are plans as of 2006; Llope 2012 supersedes them where it gives a value, except where the two simply disagree (pad, glass) without explanation.
- Route caveat: Route 1 HTML checked against the PDF text layer; figures cropped from 300-dpi PDF renders (HTML GIFs too small).

## Relevance

The only ingested source that describes the BTOF readout boards in detail: NINO features, HPTDC PLL/DLL/RC interpolation down to 24.41 ps, buffering, TCPU cabling, THUB clock distribution, SIU/RORC/Myrinet path into STAR DAQ, and the start-side TPMD. Also the design timing budget (≤ 100 ps = 50 ps start + 30 ps corrections + < 80 ps stop) and a set of MRPC construction numbers that partly disagree with Llope 2012.

## Related

- Synthesis: [star-barrel-tof](../wiki/synthesis/star-barrel-tof.md) · [star-daq-trigger](../wiki/synthesis/star-daq-trigger.md) · [mrpc-technology](../wiki/synthesis/mrpc-technology.md) · [rhic-detector-status](../wiki/synthesis/rhic-detector-status.md) · [open-questions](../wiki/synthesis/open-questions.md)
- Notes: [llope2012-star-mrpc-systems-note](llope2012-star-mrpc-systems-note.md) (as-built system; pad 3.5 vs 3.3 cm, glass 1.1/0.54 vs 0.7/0.55 mm) · [wu2007-star-barrel-tof-note](wu2007-star-barrel-tof-note.md) (contemporary QM2006 overview, no construction details) · [shao2002-mrpc-beam-test-note](shao2002-mrpc-beam-test-note.md) (USTC prototype; same 0.22 mm fibre spacers) · [yang2014-mtd-cosmic-calibration-note](yang2014-mtd-cosmic-calibration-note.md) (MTD read out with "STAR TOF" electronics)
