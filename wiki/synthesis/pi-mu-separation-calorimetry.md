---
title: Pion/muon separation with a hadron calorimeter
tags: [technology, overview]
sources: [ruan2009-mtd-concept.md, ruan2009-mtd-concept-note.md, huang2016-mtd-muon-id.md, huang2016-mtd-muon-id-note.md, yang2014-mtd-cosmic-calibration.md, yang2014-mtd-cosmic-calibration-note.md, beddo2003-bemc.md, beddo2003-bemc-note.md]
updated: 2026-11-09
---

# Pion/muon separation with a hadron calorimeter

Compiled 2026-11-05 as a general question (EIC/JLab-style J/ψ → μμ). §§1–5 draw on the external references at the end, not on raw/ sources; §4.5 is the cross-check against the STAR MTD sources in this wiki. External content is paraphrased.

## 1. Conclusion
An HCAL can separate π from μ; performance depends on momentum range, depth (λ_I) and segmentation.
- HCAL alone: π → μ misID typically ~10⁻² to 10⁻³.
- Below ~1–2 GeV/c separation degrades badly.
- Beyond ~10⁻³ needs extra absorber + muon chambers, and pion decay in flight then sets a floor.
- Per-track rejection is not the whole story: with a large π:μ flux ratio, the muon-tagged sample can still be pion-dominated.

## 2. Physics basis

| | Muon | Pion |
|---|---|---|
| Interaction | MIP, ionization only | strong interaction, hadronic shower within ~1 λ_I (~17 cm Fe or Pb) |
| Deposit | ≈ dE/dx × path, ~1.1–1.5 GeV/m steel | much larger, peaks partway in and dies off |
| Transverse profile | narrow, track-like | broad |
| Penetration | reaches all layers | usually contained |

Discriminants (roughly by power):
1. Penetration depth — does the track reach the last layers?
2. Energy deposit — consistent with MIP × path; equivalently small E/p vs pion-like E/p.
3. Transverse width — needs transverse segmentation.
4. Longitudinal profile — needs longitudinal segmentation.

An unsegmented single-readout HCAL gives only (2), which is much weaker.

## 3. Limitations
- **Pion punch-through**: non-interaction probability exp(−L/λ_I): ~0.7% at 5 λ_I, ~5 × 10⁻⁵ at 10 λ_I. Use the path length along the track angle. Shower leakage out the back adds to this, worse at high energy.
- **Pion decay in flight (π → μν)**: decay length ≈ 56 m × p[GeV/c]; at 2 GeV/c over a few metres, a few percent decay. These are real muons at the calorimeter, irreducible by any HCAL; usually the dominant background at low momentum. A tracker kink or tracker-vs-muon-system p mismatch helps somewhat.
- **Low momentum**: a 1 GeV/c muon stops in ~0.7 m iron; a sub-GeV pion deposit can look MIP-like and both may range out.
- **Very high-energy muons (≳ 100 GeV in iron)**: catastrophic losses can mimic a shower; mainly costs muon efficiency.

Practical impact: for J/ψ → μμ at EIC-like low/moderate momenta, HCAL muon ID is usable but decay-limited; background estimates must include in-flight decays, not just punch-through.

## 4. Experiments

### 4.1 NA62 (CERN, K⁺ → π⁺νν̄) — best quantified
Same discrimination in reverse (reject muons, keep pions).
- MUV1 Fe/scint 4.1 λ_I (new, fine transverse segmentation); MUV2 Fe/scint 3.7 λ_I (from NA48); 80 cm iron wall 4.8 λ_I; MUV3 fast scintillator-tile veto at L0.
- Calorimeters (LKr + MUV1/2) give μ misID ~10⁻⁵; RICH adds ~10⁻³. Design: μ misID < 10⁻⁷ at ~80% π acceptance.
- BDT: μ misID 1.2 × 10⁻⁵ at 75% π efficiency, 15–40 GeV/c. CNN: misID ×6 better at fixed 75% π efficiency, or π efficiency 72% → 91% at fixed 10⁻⁵.
- Lesson: fine segmentation + multivariate shower-shape analysis reaches 10⁻⁵; total energy alone would not.

### 4.2 ATLAS TileCal — HCAL as muon tagger
- The thick calorimeter is the hadron filter for muons above ~3 GeV; TileCal is mandatory for low-p_T muon ID at small rapidity (Physics TDR).
- TileMuId: tight selection = energy window in each of 3 Tile layers along a projective η path; loose = two layers in window, third above upper threshold (tolerates catastrophic loss). Efficient down to p_T ≈ 2 GeV/c; developed for Level-2.

### 4.3 ePIC (EIC) — closest to EIC/JLab conditions
- No dedicated muon detectors; muon ID (J/ψ, TCS, CLFV) relies on calorimeters.
- Backward HCAL: 10 layers of 4 cm steel + 4 mm scint (~2.4 λ), tail-catcher and muon ID for vector-meson decays. Barrel HCAL: refurbished sPHENIX outer HCal.
- Muon task force: per-calorimeter likelihood (E/p, number of hits, cluster radius).
- Muons below ~0.9 GeV/c curl up in the barrel ECal at η = 0 (1.7 T) and never reach the HCAL.
- Barrel ECal alone: preliminary > 90% π suppression at 95% μ efficiency.

### 4.4 Second EIC detector study (arXiv:2602.04636) — cautionary
- Single-muon ID from calorimeter information alone remains challenging; the dimuon invariant mass (J/ψ → μμ) suppresses background better.
- Preliminary (J. Kim, η = 1.74, PYTHIA): π:μ flux at 1 GeV/c ≈ 368k : 736 ≈ 500:1; per-pion misID of a few × 10⁻³ still leaves a mostly-pion muon-tagged sample after cross-section weighting. MIP selection used HCAL hit count (14–21 hits at 5 GeV) and localized hit positions.

### 4.5 STAR MTD — absorber + timing detector, no HCAL [note]
Cross-check against the STAR sources in this wiki; agrees with §§1–3. Details on [star-mtd](star-mtd.md) and [star-magnet-absorber](star-magnet-absorber.md).
- **Setup**: ≈ 61 cm of backleg steel (≈ 3.6 λ_I alone) + BEMC (≈ 0.7 λ_I, [beddo2003-bemc-note](../../raw/beddo2003-bemc-note.md)); the papers say "about 5" lengths. Then one MRPC layer at r ≈ 400 cm; no longitudinal segmentation. Muon ID uses track matching, TPC dE/dx and timing [ruan2009-mtd-concept-note](../../raw/ruan2009-mtd-concept-note.md), [huang2016-mtd-muon-id-note](../../raw/huang2016-mtd-muon-id-note.md).
- **Decay in flight dominates**, as §3 says: in 2008 d+Au prototype data prompt muons are only 6–10% of MTD muon candidates; pion decays 30–40%; the rest mostly kaon decays within the first ~2 m. A tight dE/dx cut raises prompt/secondary only to 1/6–1/3, at 26% efficiency [ruan2009-mtd-concept-note](../../raw/ruan2009-mtd-concept-note.md).
- **Per-track rejection**: simulation gives < 1% of hadrons accepted (rejection factor 50–100 with > 80% prompt-muon trigger efficiency); requiring an MTD muon candidate reduces BEMC hadronic showers by ≥ 10× [ruan2009-mtd-concept-note](../../raw/ruan2009-mtd-concept-note.md).
- **Multiple scattering** of 2 GeV/c muons in the steel: ≈ 10 cm, 100 ps [yang2014-mtd-cosmic-calibration-note](../../raw/yang2014-mtd-cosmic-calibration-note.md).
- **Result**: dimuon trigger + likelihood-ratio muon ID gives a clean J/ψ (ε ≈ 0.81 per muon; S/√B ×2 with both muons) [huang2016-mtd-muon-id-note](../../raw/huang2016-mtd-muon-id-note.md). As in §4.4, a dimuon invariant-mass constraint, not single-track ID, makes it work.

## 5. Takeaway
The per-track rejection numbers of §1 are achievable; whether they suffice depends on the π/μ flux ratio. In DIS-like environments with HCAL-only muon ID, expect to need (1) a dimuon invariant-mass constraint and/or (2) extra absorber + a tracking/veto plane behind it. NA62 reaches 10⁻⁵ only with ~8 λ, fine segmentation and ML shower-shape analysis.

## 6. References (external)
- NA62 beam and detector paper: https://arxiv.org/pdf/1703.08501
- NA62 status and perspectives: https://arxiv.org/pdf/1407.8213
- NA62 calorimetric PID with ML: https://eprints.gla.ac.uk/315533/1/315533.pdf
- NA62 ML PID talk (CAP 2021): https://indico.cern.ch/event/985448/contributions/4298279/attachments/2259660/3835071/ml_talk_cap2021.pdf
- ATLAS Physics TDR ch. 8 (muon ID): https://atlas.kek.jp/old/physics/TDR/Physics-TDR-8.pdf
- ATLAS TileMuId MC performance note: https://core.ac.uk/download/44195981.pdf
- ATLAS low-pT muon trigger with TileCal (Usai 2004): https://ebusca.uv.mx/Record/cern-818533
- Calorimetry for the ePIC Experiment: https://arxiv.org/html/2408.11075v2
- ePIC muon ID, Tracking Workfest 2026-09-16: https://indico.bnl.gov/event/31808/contributions/126717/attachments/71426/122411/MuonID_TrackingWorkfest_ePICMeeting_16-09-26.pdf
- ePIC HCal muon ID discussion: https://indico.bnl.gov/event/30574/
- ePIC barrel ECal review, performance: https://indico.bnl.gov/event/18517/contributions/73617/attachments/46469/78632/Performance.pdf
- Second EIC Detector physics case and conceptual design: https://arxiv.org/pdf/2602.04636
- J. Kim, 2nd EIC detector muon ID slides (2024-12-10): https://indico.bnl.gov/event/25846/contributions/100363/attachments/59053/101410/bnl-eic-2nd-det-JKIM-20241210.pdf

## Related
[star-mtd](star-mtd.md) · [star-magnet-absorber](star-magnet-absorber.md) · [star-fcs](star-fcs.md)
