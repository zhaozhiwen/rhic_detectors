---
title: "Huang 2016 — Muon identification with Muon Telescope Detector at the STAR experiment (curated notes)"
type: raw-note
source_type: paper
companion: huang2016-mtd-muon-id.md
authors: "T.C. Huang et al., 12 authors"
journal: "Nucl. Instrum. Meth. A 833 (2016) 88–93"
doi: 10.1016/j.nima.2016.07.024
arxiv: "1601.02910"
notes_updated: 2026-11-09
ingested_version: "arXiv:1601.02910 v3 (arXiv HTML, Route 2), cross-checked against the arXiv v3 PDF and rechecked number by number against the publisher PDF (captured 2026-11-05)"
earlier_version: []
later_version: []
published_version: "Nucl. Instrum. Meth. A 833 (2016) 88–93 — publisher PDF recheck: all numbers match; only text difference is the arXiv duplicated word 'particles particles', corrected in the journal"
version_facts: "arXiv v3 dated 15 Jul 2016 ('Preprint submitted to NIMA July 18, 2016'). Publisher HTML abstract identical to arXiv abstract. ScienceDirect served no HTML body."
versions_checked: 2026-11-09
---

# Huang 2016 — MTD muon identification — curated notes

> **Full source:** [[huang2016-mtd-muon-id]] · Companion notes to [[huang2016-mtd-muon-id]] (full source; a full-content paraphrase).

Links: DOI <https://doi.org/10.1016/j.nima.2016.07.024> · arXiv <https://arxiv.org/abs/1601.02910>

## Bibliographic

- **Title:** Muon identification with Muon Telescope Detector at the STAR experiment
- **Authors:** T.C. Huang, R. Ma, B. Huang, X. Huang, L. Ruan, T. Todoroki, Z. Xu, C. Yang, S. Yang, Q. Yang, Y. Yang (corresponding), W. Zha — 12 authors (NCKU Tainan, BNL, Tsinghua, UIC, USTC)
- **Journal:** Nucl. Instrum. Meth. A 833 (2016) 88–93; doi:10.1016/j.nima.2016.07.024
- **arXiv:** 1601.02910 [physics.ins-det], v3
- **Keywords:** STAR, MTD, muon identification, muon, dimuon, quarkonium

## What kind of paper

Performance/analysis-method paper: muon identification with the installed MTD in 2013 p+p data at √s = 500 GeV, comparing straight cuts, N−1 iteration and a Likelihood Ratio, evaluated by tag-and-probe on J/ψ→μ⁺μ⁻.

## Abstract (paraphrased)

The newly installed STAR MTD enables quarkonium measurements in the dimuon channel. Several muon-ID methods are evaluated on 500 GeV p+p data. The Likelihood Ratio method reaches ~90% muon-ID efficiency for pT > 3 GeV/c and doubles the J/ψ significance relative to the basic selection.

## Key numbers

**Detector (Sec. 2)**
- TPC |η|<1, 0.5 T. Backlegs: 30 bars, 61 cm thick at radius 363 cm, "about 5 absorption lengths".
- MTD: radius about 403 cm, about 45% in azimuth within |η|<0.5; installed 10%, 63%, 100% for 2012, 2013, 2014 runs. Timing ~100 ps, spatial ~1–2 cm in rφ and z (from [[yang2014-mtd-cosmic-calibration-note]]).
- Triggers: single-muon and dimuon from hit counts in an online timing window; dimuon trigger = ≥2 MTD hits in coincidence with the bunch crossing.

**Data / MC**
- 2013 p+p, √s = 500 GeV, MTD dimuon trigger, 28.3 pb⁻¹.
- MC: J/ψ→μ⁺μ⁻ flat single-particle, GEANT3, embedded; pT smearing mean 1.004 × pT, width 0.022 × pT.
- Basic selection: pT > 1 GeV/c; DCA < 3 cm; > 15 fit clusters (of 45); > 10 dE/dx clusters; used/possible ≥ 0.52; track projects to triggering MTD hits. >1500 J/ψ candidates.
- Fig. 1 fit: N = 1584 ± 116, M = 3.086 ± 0.004 GeV/c², σ = 0.056 ± 0.005 GeV/c², S/√B = 15.36 ± 1.14; window [2.92, 3.25] GeV/c².

**Variables and cuts**
- ΔToF, Δz, Δy × q, nσ_π (Eq. 1, log dE/dx relative to pion). Muon mean nσ_π shifted ≈0.5σ above pions.
- Straight cuts: −5 < ΔToF < 0.2 ns, |Δz| < 20 cm, |Δy×q| < 20 cm, −1 < nσ_π < 3.
- N−1 iteration: −4.8 < ΔToF < 0.7 ns, −15 < Δz < 19 cm, −9 < Δy×q < 14 cm, −0.5 < nσ_π < 3.6.
- Likelihood Ratio R = (1−Y)/(1+Y), Y = Π PDF_bkg/PDF_sig over Δy×q, Δz, nσ_π (MC signal PDFs, SS background PDFs); ΔToF fixed to the N−1 window; cut R > −0.2.
- Tag-and-probe split at muon pT 3.5 GeV/c.

**Table 1 (relative to basic selection; stat ± syst)**

| | Basic | Straight cut | N−1 iteration | Likelihood Ratio |
|---|---|---|---|---|
| Signal | 1656 ± 143 ± 114 | 1006 ± 67 ± 20 | 891 ± 58 ± 12 | 1346 ± 74 ± 22 |
| Background | 10861 ± 104 ± 317 | 2682 ± 52 ± 80 | 1962 ± 44 ± 58 | 3743 ± 61 ± 79 |
| S/B | 0.15 | 0.38 | 0.45 | 0.36 |
| S/√B | 15.89 | 19.44 | 20.11 | 22.01 |
| ε_signal | — | 0.61 ± 0.01 ± 0.05 | 0.54 ± 0.01 ± 0.05 | 0.81 ± 0.01 ± 0.07 |
| 1 − ε_bkgd | — | 0.75 | 0.82 | 0.66 |
| ε_signal (MC) | — | 0.62 | 0.51 | 0.80 |

- Plateau (pT > 3 GeV/c): about 90% (Likelihood Ratio), about 80% (others). Background reduced by more than 65% for all methods. Probe-only LR significance gain factor 1.38.
- LR on both muons: S/√B = 31.89 (factor 2); ρ/ω and φ peaks become visible.
- Systematics (data / MC): straight 0.9–8.7% / 0.6–2.6%; N−1 0.9–10.5% / 0.2–2.1%; LR 0.6–15.4% / 0.5–3.8%; fit-model part about 5–7%.

## Methods / setup

Signal PDFs = opposite-sign minus same-sign pairs in the J/ψ window (data) or embedded MC; background PDFs = same-sign pairs (sideband variant for systematics). ΔToF not simulated in MC, so data-driven only. Yields from Gaussian/Crystal-Ball + 3rd/4th-order polynomial fits, averaged over model combinations; systematic = maximum deviation.

## What the paper does not give

- MTD hardware details beyond radius/coverage/resolution (no module design, electronics, or trigger-window value).
- Normalisation of the Fig. 4(b) S/√B axis.
- Heavy-ion (Au+Au) performance; only p+p.

## Source issues and caveats

- [source issue] Conclusion says each method keeps J/ψ "with about 60% of efficiency"; Table 1 has 0.81 for the Likelihood Ratio (Sec. 5: about 80%).
- [source issue] Fig. 3 caption lists ΔToF among PDF ratios; R uses three variables and the figure has three panels.
- [source issue] Fig. 3 legend calls the solid line "linear extrapolation"; caption/text say bin-to-bin interpolation. Stray comma in the caption text.
- [source issue] Fig. 4(a) y label misspelled "Probabilty(R)/0.10".
- [source issue] Fig. 5 caption marker styles (open boxes/open circles/solid triangles) differ from the image (filled squares/stars/triangles).
- [source issue] Fig. 6 caption says red open circles and shaded boxes; image has filled circles and hatched bands.
- [source issue] Sec. 5 unit "pT > 3 GeV" should be GeV/c.
- [source issue] Garbled sentence "to record signals, also referred to as signals ('hits')".
- [source issue] arXiv v3 duplicated word "particles particles" (fixed in the journal).
- [source issue] Ref. [9] (LHCb) "J. of Instr. 10 (2013)" — volume/year mismatch.
- [note] "about 5 absorption lengths" for 61 cm Fe (≈3.6 λ_I) is approximate. Compare 57 cm in [[yang2014-mtd-cosmic-calibration-note]] and 60 cm in [[ruan2009-mtd-concept-note]].
- [note] Abstract "factor of 2" is the both-muon result; probe-only gain is 1.38. Data efficiency plateaus for straight/N−1 (≈0.67, ≈0.72) are below the "about 80%" (which matches MC).
- [note] Fig. 1 inset (1584, 15.36) differs from Table 1 basic (1656, 15.89): single fit vs average over fit models.
- Route caveat: ScienceDirect served no HTML body; text from arXiv v3 HTML, rechecked against the publisher PDF ("±" rendered as "7" in its text layer). Publisher PDF saved by hand. The arXiv v3 PDF was not kept.

## Relevance

The working muon-ID recipe and its measured efficiency/rejection for the full MTD; quantifies how much hadron background survives the backleg absorber in p+p.

## Related

- Synthesis: [[star-mtd]] · [[pi-mu-separation-calorimetry]] · [[star-magnet-absorber]] · [[star-daq-trigger]] · [[open-questions]]
- Other notes: [[ruan2009-mtd-concept-note]] (MTD design, Ref. [5]) · [[yang2014-mtd-cosmic-calibration-note]] (resolution, Ref. [12])
