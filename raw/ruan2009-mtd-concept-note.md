---
title: "Ruan 2009 — Perspectives of a mid-rapidity dimuon program at the RHIC: a novel and compact muon telescope detector (curated notes)"
type: raw-note
source_type: paper
companion: ruan2009-mtd-concept.md
authors: "L. Ruan et al., 22 authors"
journal: "J. Phys. G: Nucl. Part. Phys. 36 (2009) 095001"
doi: 10.1088/0954-3899/36/9/095001
arxiv: "0904.3774"
notes_updated: 2026-11-11
ingested_version: "Publisher version, J. Phys. G 36 (2009) 095001: text first taken from the arXiv v4 HTML (Route 2, captured 2026-11-05), then aligned to and checked against the publisher PDF (2026-11-11), which is authoritative; Fig. 1 is a 300-dpi cut from the publisher PDF, Figs 2–11 are arXiv HTML images whose content matches the publisher pages"
earlier_version: []
later_version: []
published_version: "J. Phys. G 36 (2009) 095001 — the Layer-3 text follows the publisher PDF (IOPscience serves only the abstract, reference list and PDF for this article; no HTML full text)"
version_facts: "Received 30 April 2009, published 17 July 2009 (journal). arXiv HTML built from v4; arXiv title 'Perspectives of a Midrapidity Dimuon Program at RHIC: A Novel and Compact Muon Telescope Detector'. Journal and arXiv PDF numbers agree; differences are wording/typos only; PACS codes appear only in the arXiv version. Route re-check 2026-11-11: IOPscience still has no HTML full text."
versions_checked: 2026-11-11
---

# Ruan 2009 — MTD concept — curated notes

> **Full source:** [ruan2009-mtd-concept](ruan2009-mtd-concept.md) · Companion notes to [ruan2009-mtd-concept](ruan2009-mtd-concept.md) (full source; a full-content paraphrase).

Links: DOI <https://doi.org/10.1088/0954-3899/36/9/095001> · arXiv <https://arxiv.org/abs/0904.3774>

## Bibliographic

- **Title:** Perspectives of a mid-rapidity dimuon program at the RHIC: a novel and compact muon telescope detector
- **Authors:** L. Ruan, G. Lin, Z. Xu, … Y. Wang — 22 authors (BNL, Yale, USTC, UC Berkeley, Rice, Tsinghua). Contact: L. Ruan.
- **Journal:** J. Phys. G: Nucl. Part. Phys. 36 (2009) 095001 (15 pp); doi:10.1088/0954-3899/36/9/095001
- **arXiv:** 0904.3774 (v4 HTML used for the first capture). The arXiv version lists PACS 25.75.Cj, 29.40.Cs; the journal version prints none.

## What kind of paper

Concept/proposal paper for the STAR mid-rapidity Muon Telescope Detector (MTD): long-MRPC R&D results, 2007–2008 prototype-tray data in STAR, muon-ID/hadron-rejection studies, trigger-rate estimates and full-coverage physics simulations. Pre-construction; the full-MTD numbers are a design, not as-built.

## Abstract (paraphrased)

Proposes a large-area, low-cost MTD at mid-rapidity for STAR (and future EIC detectors), built from long-strip MRPCs read at both ends. Cosmic/beam tests give 60–70 ps intrinsic timing and ∼1 cm position resolution. The STAR prototype shows muons of a few GeV/c can be identified by combining MTD track matching, TPC dE/dx and time of flight, with a primary-to-secondary muon ratio better than 1/3. Simulations cover muon efficiency, J/ψ S/B, Υ(1S) vs 2S+3S separation, and charm e–μ correlations.

## Key numbers

**STAR context used (Sec. 2)**
- TPC: inner/outer field cage 50/200 cm, 4 m long, |η|<1.8. TOF: −1<η<1, r ∼220 cm (fully installed 2009). BEMC: −1<η<1.
- Magnet: 30 flux-return bars + four end rings + two pole tips; each bar 6.85 m long, trapezoidal, 60 cm thick, 363 cm outer radius, 57 cm wide at outer radius. Field 1.2 tesla in the bar vs 0.5 tesla in the TPC.
- Bars "amount to five interaction lengths" each (Sec. 4).

**Long-MRPC module (Sec. 3)**
- Two stacks, ten gas gaps of 250 μm; six copper pickup strips, 870 × 25 mm² each (strip width 25 mm; the inter-strip gap is not given, so the six strips span ≥ 150 mm [note]); double-ended readout.
- 12.6 kV, 95% C₂H₂F₄ + 5% iso-butane, 1 atm. Plateau 12.5 < HV < 13.0 kV: efficiency >95%, timing 60–70 ps; position along strip 0.6–1 cm.

**Simulation (full HIJING central Au+Au, full STAR geometry)**
- MTD on full return bars within |η|<0.8 = 56% of 2π.
- Match cuts: hit–projection distance within 4 cm, Δt < 400 ps (simple helix extrapolation).
- Muon (pT>2 GeV/c, from TPC center) efficiency incl. acceptance 40–50% (Fig. 3: about 45%); pion 0.5–1%; all hadrons <1% (yield-weighted). Rejection factor 50–100 at >80% trigger efficiency for prompt muons. [note] A factor 50–100 means 1–2% hadron acceptance, looser than the "<1%" statement (kaons reach ≈1.85% in Fig. 3).

**Prototype in STAR (Sec. 4)**
- 2007 (200 GeV Au+Au): π/60 in azimuth, −0.25<η<0.25, r ∼400 cm; two long-MRPC modules. 2008 (d+Au, p+p): −0.5<η<0, same radius. 2009: tray with STAR TOF electronics (25 ps time bin).
- Readout: trigger digitizer boards, 8-bit ADC, 30 mV discriminator thresholds, TAC; L0 decision <1.5 μs; trigger = ≥1 strip with valid hit.
- Table 1: Au+Au 20 k Hz interaction, 270 μb⁻¹, 0.31 M events, 7k matched hits; d+Au 100 k, 29 nb⁻¹, 1.6 M, 78 k; p+p 300 k, 404 nb⁻¹, 0.56 M, 8k; trigger rate 0.5–2 Hz in all.
- Δz match (d+Au, pT>2 GeV/c): narrow Gaussian σ ≈ 10 cm (GEANT muon at pT∼2.5 GeV/c: σ = 9 cm); window |Δz|<20 cm; narrow/broad ∼2.
- Au+Au timing: ∼300 ps total; minus start (two VPDs at 5.4 m, ∼160 ps) and material (∼100 ps at pT=2.5 GeV/c) → MTD 200–300 ps (trigger electronics not designed for timing).

**Muon ID / hadron rejection (Sec. 5)**
- μ dE/dx ∼3–4% above π for pT>2 GeV/c; TPC dE/dx resolution ∼8% → μ–π ≈ half a sigma, μ–K ≈ two sigma.
- Muon energy loss "in the return bar" ∼1.2 GeV for 2 < pT < 10 GeV/c (see caveats).
- Muon purity >80% within |Δz|<20 cm (matching + dE/dx + velocity).
- K⁰_S method: secondary muons from pion decay = 30–40% of muon candidates.
- Requiring a TOF hit in the same TPC sector (2008 p+p): inclusive muon yield down by factor 2.
- Table 2 (EMC > 0.75 GeV above pedestal), non-MTD (A) vs MTD (B): 1.5–2 GeV/c (2.21 ± 0.03)% vs (0.18 ± 0.02)%; 2–3: (3.67 ± 0.07)% vs (0.30 ± 0.04)%; 3–4: (5.89 ± 0.22)% vs (0.34 ± 0.10)%; 4–6: (7.92 ± 0.50)% vs (0.65 ± 0.24)%. MTD requirement cuts BEMC hadronic showers by ⩾10; hadron share ≃100% → ⩽10%.
- Primary muons = 6–10% of inclusive muons with MTD association only; raw-yield fit systematic about 20%.
- Table 3 (200 GeV d+Au): no cut 100% eff., S/B 1/15–1/9; nσ_π>0 61%, 1/10–1/6; nσ_π>1 26%, 1/6–1/3 (S/B ×3).

**Full detector and trigger (Sec. 6)**
- 56% of TPC acceptance at |η|<0.8; 540 long-MRPC modules, 2160 strips, 4320 channels (factor 5–6 fewer than TOF).
- Single-hit L0 reduction 0.19 (min-bias Au+Au) → dimuon enhancement 28; 1 billion min-bias = 36 million dimuon triggers → 5600 J/ψ, 85 Υ.
- Table 4 L0: min-bias Au+Au 0.2; 0–5% Au+Au 0.5 (0.2), L2 with TOF ∼0.3, RHIC II 100 k Hz, dimuon L2 ∼500 (100) Hz; 60–80% Au+Au 0.03; d+Au 0.02; p+p 0.01, L2 0.003, 2 M Hz, ⩽10 Hz.
- MTD–TOF matching (2008 p+p): trigger rate ÷3; z_expected − z_TOFhits σ ∼ 6 cm (fit 5.882 ± 0.179 cm).

**Physics projections (Sec. 7)**
- J/ψ→μμ S/B = 7:1 (d+Au); Υ 1S separable from 2S+3S; charm e–μ S/B = 2:1 for m_eμ>3 GeV/c² (2 billion min-bias d+Au); background ÷4 with photonic-electron and TOF rejection.
- RHIC II (26 nb⁻¹ Au+Au, 300 pb⁻¹ p+p): p+p 169 k J/ψ, 2500 Υ; Au+Au 630 k J/ψ, 9300 Υ.

## Methods / setup

GEANT simulation of single muons/hadrons from the TPC centre and HIJING central Au+Au in full STAR geometry; prototype tray (two long-MRPCs) behind one backleg at r ∼400 cm in Runs 7–8 read by STAR trigger digitizers; offline matching of TPC tracks to MTD hits in Δz (two-end time difference); muon enrichment by velocity and dE/dx; pion-decay fraction from K⁰_S daughters; hadron-shower check with BEMC; prompt fraction via non-photonic-electron yields; MTD–TOF z correlation using the east–west VPD time difference.

## What the paper does not give

- Strips per module in the full design (2160/540 = 4, which does not match the six strips per prototype module of Sec. 3).
- The inter-strip gap of the prototype module (only the 25 mm strip width).
- Signal propagation speed along the strips.
- Explanation of 56% azimuthal coverage vs the bar-face geometry.
- Formula behind Table 4 dimuon L2 rates; definition of the ">80% trigger efficiency".
- What material makes up "five interaction lengths".

## Source issues and caveats

- Fig. 1 image: the arXiv-HTML PNG was truncated and an earlier publisher-PDF extraction had inverted colours; since 2026-11-11 the kept `fig1.png` is a 300-dpi cut from the publisher PDF page (the inverted image is quarantined in `_to_delete/ruan2009-old/`).
- [source issue] Published Fig. 3 caption prints "(56)" without the % sign (arXiv: "(56%)").
- [source issue] Fig. 4 caption says 2006–2008; the text covers only the 2007 and 2008 runs.
- [source issue] The ∼1.2 GeV muon loss is attributed to "multiple scattering in the return bar"; it is ionization loss, and 60 cm Fe alone gives about 0.7–0.8 GeV (dE/dx ≈ 11.8–12.6 MeV/cm [note]), so ∼1.2 GeV fits all material/oblique paths better.
- [note] Strips per module: 2160 strips / 540 modules = 4, which does not match the six strips per prototype module of Sec. 3; the paper does not state strips per module for the full design, which may differ.
- Other: "25 ps" called a time-bin width (Sec. 4) and a timing resolution (Sec. 5) — bin width is the correct reading; reference typos (Ref. [3] "Saltz H" for Satz; Ref. [22] article number 062301).
- [note] (from the companion) 30 bars × 57 cm cover ≈75% of the azimuth at r = 363 cm vs the paper's 56%; "five interaction lengths" exceeds 60 cm Fe (≈3.6 λ_I).
- [note] Figure-reading caveats: Fig. 3 plateau reads 0.40–0.44 (vs "about 45%"); Fig. 7 pion contribution factor ≈0.22–0.51 point by point (vs 30–40%); Fig. 9 shows the MTD ε advantage only over PHENIX (STAR TOF+EMC ≈0.4 is higher); Fig. 10 separates 1S from 2S+3S but not 2S from 3S.
- Route: text first taken from the arXiv v4 HTML (Route 2, 2026-11-05) and aligned to the publisher J. Phys. G PDF on 2026-11-11, which is authoritative (abstract, body, captions, tables and references follow the journal version). The arXiv HTML dropped leading numbers of several ranges (e.g. −1<η<1, 12.5<HV<13.0 kV); pdftotext of the publisher PDF drops ≳, ⩾, ⩽, ≃, Δ. All values in the companion follow the rendered publisher PDF. The arXiv PDF used for comparison was not kept.

## Relevance

Founding design document for the STAR MTD: backleg absorber geometry, long-MRPC parameters, prototype performance and the muon-ID strategy (matching + dE/dx + TOF) that later papers build on.

## Related

- Synthesis: [star-mtd](../wiki/synthesis/star-mtd.md) · [mrpc-technology](../wiki/synthesis/mrpc-technology.md) · [star-magnet-absorber](../wiki/synthesis/star-magnet-absorber.md) · [pi-mu-separation-calorimetry](../wiki/synthesis/pi-mu-separation-calorimetry.md) · [star-daq-trigger](../wiki/synthesis/star-daq-trigger.md) · [star-barrel-tof](../wiki/synthesis/star-barrel-tof.md) · [star-bemc](../wiki/synthesis/star-bemc.md) · [open-questions](../wiki/synthesis/open-questions.md)
- Follow-ups: [yang2014-mtd-cosmic-calibration-note](yang2014-mtd-cosmic-calibration-note.md) (cosmic-ray calibration of the built MTD) · [huang2016-mtd-muon-id-note](huang2016-mtd-muon-id-note.md) (muon ID in 2013 p+p)
- TOF/MRPC lineage: [shao2002-mrpc-beam-test-note](shao2002-mrpc-beam-test-note.md) · [wu2007-star-barrel-tof-note](wu2007-star-barrel-tof-note.md) · [llope2012-star-mrpc-systems-note](llope2012-star-mrpc-systems-note.md)
- Absorber/calorimeter context: [beddo2003-bemc-note](beddo2003-bemc-note.md)
