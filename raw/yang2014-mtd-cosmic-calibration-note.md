---
title: "Yang 2014 — Calibration and performance of the STAR Muon Telescope Detector using cosmic rays (curated notes)"
type: raw-note
source_type: paper
companion: yang2014-mtd-cosmic-calibration.md
authors: "C. Yang et al., 38 authors"
journal: "Nucl. Instrum. Meth. A 762 (2014) 1–6"
doi: 10.1016/j.nima.2014.05.075
arxiv: "1402.1078"
notes_updated: 2026-11-11
ingested_version: "Published journal version via publisher HTML (ScienceDirect, Route 1), checked against the publisher PDF; critical items also checked in the arXiv v1 text (captured 2026-11-05)"
earlier_version: []
later_version: []
published_version: "Nucl. Instrum. Meth. A 762 (2014) 1–6 — this is the ingested version"
version_facts: "arXiv:1402.1078 v1, 5 Feb 2014. Journal: received 20 Feb 2014, revised 5 May 2014, accepted 6 May 2014, online 27 May 2014. No substantive HTML/PDF/arXiv differences; arXiv v1 differs only in minor wording."
versions_checked: 2026-11-09
---

# Yang 2014 — MTD cosmic-ray calibration — curated notes

> **Full source:** [yang2014-mtd-cosmic-calibration](yang2014-mtd-cosmic-calibration.md) · Companion notes to [yang2014-mtd-cosmic-calibration](yang2014-mtd-cosmic-calibration.md) (full source; a full-content paraphrase).

Links: DOI <https://doi.org/10.1016/j.nima.2014.05.075> · arXiv <https://arxiv.org/abs/1402.1078>

## Bibliographic

- **Title:** Calibration and performance of the STAR Muon Telescope Detector using cosmic rays
- **Authors:** C. Yang, X.J. Huang (corresponding), C.M. Du, B.C. Huang, et al. — 38 authors (BNL, USTC, Tsinghua, IMP Lanzhou, Rice, UC Davis, UT Austin, Variable Energy Cyclotron Centre, West Bengal, Texas A&M)
- **Journal:** Nucl. Instrum. Meth. A 762 (2014) 1–6; doi:10.1016/j.nima.2014.05.075
- **arXiv:** 1402.1078 [physics.ins-det] (v1)
- **Keywords:** Muon telescope detector; Cosmic ray; Timing resolution; Spatial resolution

## What kind of paper

Short detector-performance paper: timing and spatial resolution of MTD MRPCs (prototypes 2007–2011, 10% of the full MTD in Run 12) measured with cosmic muons triggered in STAR, read out with STAR TOF (HPTDC) electronics. Contains the slewing/offset calibration procedure and the final-design (type B) module parameters.

## Abstract (paraphrased)

Reports the MTD timing and spatial resolution in STAR using cosmic-ray muons (average pT 6 GeV/c, small multiple scattering). Results: ~100 ps timing and ~1–2 cm position resolution, consistent with earlier bench and beam tests.

## Key numbers

**Detector and placement**
- MTD behind the magnet return bars; 45% of full azimuth within |η|<0.5; mounted on BEMC PMT boxes at ~400 cm. Construction from 2011, completion planned 2014.
- Backlegs: 30 flux-return bars, 6.85 m long, trapezoidal, "57 cm thick at a radius of 363 cm"; backlegs + BEMC = hadron absorber.
- STAR context: TPC 4 m, |η|<1, 24 super-sectors, 45 pad rows, 0.5 T; TOF |η|<0.9, ~220 cm (fully installed before 2010 run).

**MRPC module types (Sec. 2)**

| Type | Stack | Gas gaps | Strips | Module size | Strip width / gap |
|---|---|---|---|---|---|
| A | double | 10 | 6 | 87 × 17 cm² | 2.5 cm / 0.4 cm |
| B (final design) | single | 5 × 250 μm | 12 | 87 × 52 cm² | 3.8 cm / 0.6 cm |
| C | single | 6 × 250 μm | 12 | 87 × 52 cm² | 3.8 cm / 0.6 cm |

- Fig. 1 (type B) also shows glass 1.1 mm (outer) and 0.7 mm (inner), Mylar 0.15 mm, PC board 1.5 mm, honeycomb 10 mm; 580 mm PC-board width.
- Gas 95% Freon R-134a + 5% isobutane. Electronics: STAR TOF type, 40 MHz clock, 24.4 ps LSB; analog multiplicity per module end to STAR Level-0.
- Run 12: 12 type-B modules in 12 trays (10% of the full MTD).

**Cosmic trigger and selection**
- Trigger (2010 run): one MTD hit + two TOF hits. Cosmic tracks pT > 2 GeV/c; ≥ 25 TPC hits (of 45) per track; mean pT ≈ 6 GeV/c; Δp/p σ = 0.1005 (text "≈10%"); cut |Δp/p| < 27%.
- Collision muons reaching the MTD: mean pT ~2 GeV/c; for 2 GeV/c, backleg multiple scattering gives 10 cm and 100 ps.

**Spatial resolution**
- Field map: 0.5 T inside, −1.26 T in backleg steel, zero at the MTD.
- Raw residual σ: ΔZ 2.6 cm (fit 2.551 cm), Δφ 0.006 rad (fit 0.006111 rad).
- Fit y = √(p0/x² + p1); intrinsic √p1: 0.8 cm (Z) and 2.2×10⁻³ rad (φ) = 0.9 cm at 400 cm.

**Timing**
- Matching cuts: ΔZ < 6 cm, Δφ < 0.2 rad.
- σ(ΔT₀) = 90 ps → single TOF hit 64 ps.
- Total ΔT σ = 104 ps; minus start 45 ps and multiple scattering 25 ps (6 GeV/c) → MTD 90 ps.
- Slewing: ⟨ToT⟩ = √(ToT_L·ToT_R), fifth-order polynomial; raw strip-to-strip offsets up to ≈1.7 ns (Fig. 8 reading).

**Table 2 — resolution by run**

| Conditions | Type | Resolution |
|---|---|---|
| Cosmic & test-beams | A | 60 ps, 0.6 cm |
| Run 7–8 | A | 200–300 ps |
| Run 9–10 | A | 90 ps, 0.8 cm (z), 0.9 cm (ϕ) |
| Run 11 | A | 89 ps, 1.1 cm (z), 1.1 cm (ϕ) |
| Run 11 | B | 101 ps, 1.4 cm (z), 1.6 cm (ϕ) |
| Run 11 | C | 127 ps, 2.4 cm (z), 1.8 cm (ϕ) |
| Run 12 | B | 108 ps, 2.6 cm (z), 1.9 cm (ϕ) |

## Methods / setup

Cosmic muon crosses MTD, backleg, BEMC, TOF, TPC and is reconstructed as two TPC tracks. Start time from the two TOF hits corrected by the TPC-expected flight time; ΔT = (t_TOF2 − t_TPC + t_TOF1)/2 − t_MTD − t_Steel per strip. Three-pass calibration: per-strip offsets, ToT slewing curve, re-equalised offsets (worked example: 2010 data, three type-A modules, 18 strips). Position: φ from strip centre, Z from leading-edge time difference of the two strip ends; resolution vs momentum fit to separate multiple scattering.

## What the paper does not give

- Signal propagation speed along the strips (no cm/ns value; a 15–18 cm/ns sentence once in the Layer-3 file was not from the paper and was removed on 2026-11-11 — the from-memory value lives in [open-questions](../wiki/synthesis/open-questions.md) #9).
- Which data set Fig. 5 shows; whether Run 12 values are multiple-scattering-corrected.
- Module design parameters in Table 1 (despite its caption; they are in the text only).
- Reconciliation of the 580 mm PC-board width with the 52 cm module size.

## Source issues and caveats

- [source issue] Fig. 9 caption: "as a function of ." — variable missing in HTML, publisher PDF and arXiv v1; axis label shows it is ⟨ToT⟩.
- [source issue] (minor) t_Steel said to use "the 0.5 T magnetic field", while Sec. 4.2 uses −1.26 T in the steel; [note] effect on timing ≪ 1 ps.
- [note] Δφ < 0.2 rad cut is printed identically in all versions; ≈ one backleg width (2π/30 = 0.209 rad) and very loose vs the 0.006 rad σ — a typo for 0.02 rad is possible but not shown.
- [note] Run 12 type-B z = 2.6 cm equals the raw Fig. 5 ΔZ σ; possibly not multiple-scattering-corrected (unresolvable).
- [note] "≈10%" momentum resolution is the width of the two-track Δp/p difference; per-track ≈7% if independent.
- [note] 64 ps TOF single-hit value includes the t_TPC uncertainty (upper bound). Δφ residual peak offset −0.0074 rad not discussed.
- [note] Strip-pitch/√12 check: type A 0.84 cm vs 0.9 cm measured; type B 1.27 cm vs 1.6–1.9 cm.
- Route caveat: publisher pdftotext loses "~", minus and "×"; values taken from HTML and confirmed in arXiv text. The arXiv v1 PDF was not kept.

## Relevance

Primary measured MTD resolution numbers (≈90–108 ps, 1–2.6 cm) and the final module design (type B, 12 strips 3.8 cm, 87 × 52 cm²) for the STAR detector study.

## Related

- Synthesis: [star-mtd](../wiki/synthesis/star-mtd.md) · [mrpc-technology](../wiki/synthesis/mrpc-technology.md) · [star-magnet-absorber](../wiki/synthesis/star-magnet-absorber.md) · [star-barrel-tof](../wiki/synthesis/star-barrel-tof.md) · [star-daq-trigger](../wiki/synthesis/star-daq-trigger.md) · [open-questions](../wiki/synthesis/open-questions.md)
- Other notes: [ruan2009-mtd-concept-note](ruan2009-mtd-concept-note.md) (design and 2007–08 prototype) · [huang2016-mtd-muon-id-note](huang2016-mtd-muon-id-note.md) (cites this paper for ~100 ps, 1–2 cm) · [llope2012-star-mrpc-systems-note](llope2012-star-mrpc-systems-note.md) (TOF/MTD electronics) · [wu2007-star-barrel-tof-note](wu2007-star-barrel-tof-note.md)
