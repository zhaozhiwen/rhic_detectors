---
title: "Wu 2007 — A barrel TOF for STAR at RHIC (curated notes)"
type: raw-note
source_type: paper
companion: wu2007-star-barrel-tof.md
authors: "J. Wu, M. Xu (USTC), for the STAR Collaboration"
journal: "J. Phys. G: Nucl. Part. Phys. 34 (2007) S729–S732 (Quark Matter 2006 proceedings)"
doi: "10.1088/0954-3899/34/8/S83"
arxiv: none
notes_updated: 2026-11-11
ingested_version: "Publisher version of record (IOP PDF, cover page + pp. S729–S732), read 2026-11-05 via Route 3 (PDF only; Chrome, JLab institutional access)"
earlier_version: []
later_version: []
published_version: "J. Phys. G 34 (2007) S729–S732 -- this is the ingested version"
version_facts: "Received 10 Jan 2007; published 12 Jul 2007 (J. Phys. G vol. 34 no. 8, QM2006 issue). No arXiv version listed by IOP or Crossref. IOP HTML abstract matches the PDF abstract word for word."
versions_checked: 2026-11-09
---

# Wu 2007 — Curated Notes

> **Full source:** [wu2007-star-barrel-tof](wu2007-star-barrel-tof.md) · Companion notes to [wu2007-star-barrel-tof](wu2007-star-barrel-tof.md) (full source; a full-content paraphrase).
> **DOI:** https://doi.org/10.1088/0954-3899/34/8/S83 · arXiv: none

## Bibliographic

- **Title:** A barrel TOF for STAR at RHIC
- **Authors:** J. Wu, M. Xu (both USTC, Hefei), for the STAR Collaboration.
- **Journal:** J. Phys. G: Nucl. Part. Phys. 34 (2007) S729–S732 (Quark Matter 2006 proceedings).

## What kind of paper

4-page conference proceeding, mostly physics motivation. Summarizes the TOFr prototype tray (Runs 3–5) and plans for the full MRPC barrel TOF. Almost no MRPC construction detail.

## Abstract (paraphrased)

After several years of successful MRPC TOF prototype running in STAR, a full barrel TOF is under construction, aimed at data taking from late 2008. Together with other STAR subsystems it extends PID, maximizing event-by-event soft-physics information and improving signal-to-noise for charm hadrons (D⁰, D⁺, D_s⁺, J/ψ), enabling charm thermalization and flow studies. Prototype physics results and expected full-TOF performance are shown.

## Key numbers

**Project**
- MRPC TOF R&D in STAR since 2000; ten US + six Chinese institutions; construction/commissioning by fall 2008.
- Full barrel: printed "η < 1" (means |η| < 1), 2π in φ. MRPC: sub-100 ps, ~95% MIP efficiency.
- Staging: four-tray system soon, then 48 more trays next year; full-TOF data hoped for 2008–2009 Au–Au full-energy runs.

**Beam test of final MRPC design (CERN PS T10, ref. [2] = Shao 2002)**
- Gas 90% C₂H₂F₄ + 5% iso-butane + 5% SF₆.
- Intrinsic time resolution 50–60 ps (after slewing and start corrections, several chambers); efficiency > 95% over a wide HV range.
- Rate capability and ageing studied in [3–5] (USTC theses, 2006) — no numbers given.

**TOFr prototype tray in STAR**

| Item | Value |
|---|---|
| Pre-installation test | BNL AGS radiation area |
| Installed | fall 2002; data since RHIC Run III |
| Coverage | π/30 in φ; −1 < η < 0 |
| Radius | 210 cm |
| MRPCs | 28 per tray (partly instrumented in 2003, 2004, 2005 runs) |
| HV / gas | 14 kV; 95% C₂H₂F₄ + 5% iso-butane (no SF₆), 1 atm |
| Start | two pVPDs, each 5.4 m from TPC centre |
| Start resolution (200 GeV) | ~140 ps (p+p), 85 ps (d+Au), 25 ps (Au+Au) |
| Stop resolution | ~85 ps after calibration with pure pion sample |

**PID performance**
- d+Au 200 GeV: π/K separation to p_T ~1.6 GeV/c; proton/meson to ~3.0 GeV/c. m² = p²(1/β² − 1).
- Electron ID: TOFr cut |1/β − 1| < 0.03 plus TPC dE/dx; hadron rejection ~10⁵ at p_T < 1 GeV/c (ref. [8]).
- φ background: TOF + TPC kaon ID suppresses φ background ~four times better than TPC alone (Fig. 2, Au+Au 200 GeV Run IV, 1.0 < p_T < 4.0 GeV/c; S/(S+B) peak ≈0.056 vs ≈0.014 read off plot).

**[note] L3-derived:** π/30 = 6°, arc ≈22.0 cm at R = 210 cm; −1 < η < 0 at 210 cm spans |z| ≤ 246.8 cm; 2π/(π/30) = 60 trays per η half → 120 trays for |η| < 1 (paper never states total). Cut |1/β − 1| < 0.03 passes π above ≈0.566 GeV/c, K above 2.00, p above 3.80 GeV/c.

## Methods / setup

- TOF = MRPC stop (TOFr tray at R = 210 cm) minus pVPD start; calibration with pure pion sample (ref. [7], Wu 2005).
- PID from 1/β vs p (Fig. 1 left), m² inset for 1.2 < p_T < 1.4 GeV/c; electron selection by combining TOF β with TPC dE/dx (Fig. 1 right).
- Physics achieved with single tray: identified spectra and Cronin effect (d+Au, Run III); first STAR non-photonic electron spectrum and total charm cross section (d+Au); spectra and v₂ (Runs IV–V); charm cross section in Au+Au.
- Table 1: ten-item physics programme for the full barrel TOF (multi-strange v₂, fluctuations, resonances, π–Ξ correlations, charm flow, D/B at high p_T, di-leptons, UPC e⁺e⁻, Λ⁰ polarization correlations).

## What the paper does not give

- No MRPC construction: gap count/size, glass type/thickness/resistivity, pad size, electronics, tray mechanics, channel count, total tray count, production-system radius.
- No in-STAR efficiency; no rate/ageing numbers; no signal propagation speed or readout geometry.

## Source issues and caveats

- **[source issue]** Coverage printed "η < 1"; should be |η| < 1.
- **[source issue]** "sub-one 100 ps time resolution" garbled; means sub-100 ps.
- **[source issue]** Even-page running head "J Wu an M Xu" (typo for "and").
- **[note]** Unclear whether the ~85 ps "stop time resolution" is stop-only or total; literally stop-only. If independent, d+Au total would be ≈120 ps (L3 arithmetic).
- Gas differs: beam test 90/5/5 with SF₆; TOFr in STAR 95/5 without SF₆.
- Fig. 1(b) black curve unexplained; y-axis "Energy loss" without unit.
- Route caveat: Route 3 (PDF only); pdftotext dropped Ξ, Λ⁰, Ω glyphs — rendered pages used. Fig. 2 values read off the plot.

## Relevance

Bridge between the 2002 USTC prototypes and the as-built STAR barrel TOF: gives TOFr prototype geometry (R = 210 cm, π/30, 28 MRPCs), in-STAR start/stop resolutions and the PID/electron-ID reach that motivated the full system.

## Related

- Synthesis: [star-barrel-tof](../wiki/synthesis/star-barrel-tof.md) · [mrpc-technology](../wiki/synthesis/mrpc-technology.md) · [open-questions](../wiki/synthesis/open-questions.md)
- Notes: [shao2002-mrpc-beam-test-note](shao2002-mrpc-beam-test-note.md) (ref. [2], prototype beam test) · [llope2012-star-mrpc-systems-note](llope2012-star-mrpc-systems-note.md) (final system, Table 1 includes these TOFr runs)
- [schambach2006-star-tof-electronics-note](schambach2006-star-tof-electronics-note.md) — contemporary (2006) electronics design paper: readout chain, MRPC and tray construction, timing budget, cosmic stand; supplies the construction details this paper lacks (gaps excepted).
