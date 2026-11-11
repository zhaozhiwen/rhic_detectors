---
title: "Shao 2002 — Beam test results of two kinds of multi-gap resistive plate chambers (curated notes)"
type: raw-note
source_type: paper
companion: shao2002-mrpc-beam-test.md
authors: "M. Shao et al. (10 authors; USTC Hefei; corresponding author J. Wu)"
journal: "Nucl. Instrum. Meth. A 492 (2002) 344–350"
doi: "10.1016/S0168-9002(02)01355-4"
arxiv: none
notes_updated: 2026-11-09
ingested_version: "Publisher version of record (ScienceDirect PDF, 7 pages), read 2026-11-06 via Route 3 (PDF only; pdftotext + page renders read by eye)"
earlier_version: []
later_version: []
published_version: "Nucl. Instrum. Meth. A 492 (2002) 344–350 -- this is the ingested version"
version_facts: "Received 21 March 2002; revised 27 June 2002; accepted 9 July 2002. No arXiv version (arXiv API search returned only the 2008 long-strip MRPC paper 0805.2459). Title, authors, volume, pages confirmed via Crossref and PDF page 1."
versions_checked: 2026-11-09
---

# Shao 2002 — Curated Notes

> **Full source:** [[shao2002-mrpc-beam-test]] · Companion notes to [[shao2002-mrpc-beam-test]] (full source; a full-content paraphrase).
> **DOI:** https://doi.org/10.1016/S0168-9002(02)01355-4 · arXiv: none

## Bibliographic

- **Title:** Beam test results of two kinds of multi-gap resistive plate chambers
- **Authors:** M. Shao, L.J. Ruan, H.F. Chen, J. Wu (corresponding), C. Li, Z.Z. Xu, X.L. Wang, S.L. Huang, Z.M. Wang, Z.P. Zhang — 10 authors, all USTC (Hefei).
- **Journal:** Nucl. Instrum. Meth. A 492 (2002) 344–350. PACS 12.38Qk; 29.40Gx; 29.40Cs.
- **Cited as:** ref. [2] ("final MRPC design", CERN PS T10 test) in [[wu2007-star-barrel-tof-note]].

## What kind of paper

Short NIM detector paper: construction details and CERN PS-T10 beam-test results for two USTC multi-cell MRPC prototypes (6-gap and 10-gap) built for the STAR TOF. No numbered equations, no tables.

## Abstract (paraphrased)

USTC built and beam-tested a 6-gap and a 10-gap multi-gap RPC at the CERN PS-T10 area. The 6-gap chamber reaches about 65 ps time resolution, enough for the STAR TOF; the 10-gap chamber reaches below 55 ps. The paper describes the chambers and the test setup.

## Key numbers

**STAR motivation (Introduction / Conclusions)**
- PMT-based TOF for STAR: ~25,000 fast PMTs for 64 m², each unit 6.3 × 3.1 cm² (granularity), field-insensitive PMTs needed; cost too high. **[note]** L3 check: 25,000 × 6.3 × 3.1 cm² = 48.8 m², not 64 m².
- MRPC TOF with < 100 ps would extend STAR 3σ π/K and K/p separation from 0.65 and 1.3 GeV/c to 1.6 and 2.6 GeV/c.
- Generic MRPC: glass bulk resistivity ~10¹²–10¹³ Ω cm, gaps 0.2–0.3 mm, avalanche mode with freon-containing gas.

**6-gap MRPC (Fig. 1)**

| Item | Value |
|---|---|
| Readout | 12 pads, 2 × 6 array; pad 3.1 × 3.0 cm² (31 mm across, 30 mm along); 3 mm inter-pad gap |
| Sensitive area | 20 × 6.3 cm² (pad region 195 × 65 mm from figure, [note]) |
| Glass stack | 5 inner × 0.70 mm + 2 outer × 1.2 mm (7 plates, 6 gaps) |
| Glass size | outer 21.6 × 8.9 cm², inner 19.8 × 6.8 cm² (text swaps the labels; figure is right) |
| Glass resistivity | 2.57 × 10¹³ Ω cm (0.7 mm), 1.8 × 10¹³ Ω cm (1.2 mm), at 16 °C ("Shanghai glass") |
| Gas gap | 250 μm, nylon fiber spacers |
| Electrodes | carbon film, 8 × 10⁵ Ω/□, on outer faces of 1.2 mm glass; mylar insulation; pads on PCBs (1.5 mm) |
| Mechanics | 6 mm honeycomb plates outside PCBs (not drawn in figures) |
| Fig. 1 dims | electrode 208 × 80 mm; upper PCB 102 mm, bottom PCB 126 mm wide; PCB/mylar/outer glass length 216 mm; mylar tape 93 mm |

**10-gap MRPC (Fig. 2)**
- Two 5-gap stacks; negative HV on two outer electrodes, positive HV on shared middle electrode; pads on both faces of middle PCB.
- Gas gap 0.22 mm (Ø 0.22 mm nylon fiber); fibers ~33 mm apart, gap variation < 20 μm; fiber over pad gap.
- From figure labels only: outer glass 1.1 mm, inner glass 0.6 mm (each stack 2 + 4 plates); outer glass 208 × 85 mm, inner 198 × 68 mm, electrode 204 × 80 mm; PCB & mylar length 214 mm; outer PCBs 102 mm, middle PCB 126 mm wide. Glass resistivity not given.
- Dark current < 5 nA per electrode at 15 kV (chamber not specified).

**Common**
- Gas: 90% C₂H₂F₄, 5% SF₆, 5% iso-C₄H₁₀, 1 atm, sealed box.

**Beam test (CERN PS-T10)**
- 7 GeV/c π beam (some scattered protons); beam half-width 1.0 cm; spill 250 ms; rate < 100 Hz/cm².
- Trigger: single-readout MRPC; start: mean of 4 PMTs on two crossed scintillator pairs, 30 ps.
- Tracking: 3 pairs of MWPCs, 4 mm wire spacing, 0.3 mm position resolution.
- TDC binning 50 ps/channel (from Fig. 5/10 axis).

**Results — 6-gap**
- HV scan: nine settings, 14–17 kV. Efficiency (non-zero TDC / tracked events) > 97% plateau 15.5–17.0 kV.
- Time walk vs HV slope −30.36 ± 1.18 ps/kV (Fig. 4).
- Slewing: sixth-order polynomial (small amplitude) + linear (large amplitude).
- Time resolution ~65 ps after start-jitter subtraction (Fig. 5: σ = 1.324 ch = 66.2 ps; 1227 entries; χ²/ndf 26.93/11). Fig. 4 plateau reads ≈57–60 ps.
- X scan at ±7.875 kV (= 15.75 kV): in pad gap efficiency ~80%, timing ~100 ps (figure: Pad 2 points to ≈124–145 ps).
- Z scan at ±8.25 kV: similar.

**Results — 10-gap**
- HV 22.5–25 kV: efficiency 98% at 22.5 kV (plot ≈98.9%); 54 ps at 23.5 kV; streamers appear at 25.0 kV; working point 23.5 kV (±5.875 kV per stack ×2).
- X scan at 23.5 kV: within 10 mm of centre ~50 ps and > 99%; best 40 ps at centre (error bar ≈23–61 ps); worse at strip edge from charge sharing / cross-talk.
- Overall ~55 ps incl. electronic jitter (Fig. 10: σ = 1.153 ch = 57.7 ps; 1944 entries; χ²/ndf 20.88/10).
- **[note]** L3-derived gas field: ≈105 kV/cm (6-gap) and ≈106.8 kV/cm (10-gap), i.e. same working field.

## Methods / setup

- Chamber in sealed gas box on 3D-movable platform; beam along Y, scans in X and Z; hit position from external MWPC telescope (MRPC gives pad only).
- Time from rising edge, offline slewing correction vs amplitude; start-time jitter subtracted (exact treatment ambiguous, see caveats).
- Two test types: centre HV scans and position scans across pads.

## What the paper does not give

- Front-end electronics: no preamp/discriminator, TDC model or board named; ADC not named (amplitude implied by slewing correction).
- Signal propagation speed; sub-pad position resolution; readout single- vs double-ended or differential scheme; orientation of pads in STAR (z vs φ).
- Rate dependence (only < 100 Hz/cm² beam), ageing, cross-talk fraction, 10-gap glass resistivity.

## Source issues and caveats

- **[source issue]** Abstract writes "MPRCs" once; attaches "around 65 ps" to both time resolution and efficiency.
- **[source issue]** Text swaps inner/outer glass areas (figure: inner 19.8 × 6.8, outer 21.6 × 8.9 cm²).
- **[source issue]** Fig. 1(a) / 2(a) labels "pad width = 3mm", "pad gap/internal = 0.3mm" — must be cm.
- **[source issue]** Fig. 3 label "Scintilators"; caption "PS-10" for PS-T10.
- **[source issue]** "sixth-oder" typo.
- **[source issue]** Fig. 5 x-axis tick left of 0 printed "10" instead of "−10".
- Ambiguity: Fig. 5 σ alone is 66.2 ps (59.0 ps if 30 ps start removed in quadrature); Fig. 10 σ 57.7 ps (49.2 ps start-removed). Whether the quoted 65 ps / 55 ps are start-subtracted is unresolved.
- Ambiguity: which chamber the 15 kV / < 5 nA dark current refers to; whether the fiber-placement rules apply to both chambers; how 10-gap pad signals are combined.
- 10-gap text says 98% at 22.5 kV; plot reads ≈98.9%. Fig. 7 Z scan at a different HV (±8.25 kV) than X scan, unmentioned.
- Route caveat: Route 3 (PDF only); text layer garbles Ω, ×, ±, μ, ° — rendered pages used; values read from figures are approximate.

## Relevance

Earliest USTC multi-cell MRPC prototype for the STAR barrel TOF; sets the glass/gap/gas lineage and the < 100 ps STAR PID motivation. **[note]** The production STAR TOF MRPC differs (5 gaps, different glass and pad layout; see [[llope2012-star-mrpc-systems-note]]), so use this paper for prototype performance, not as-built geometry.

## Related

- Synthesis: [[mrpc-technology]] · [[star-barrel-tof]] · [[open-questions]]
- Notes: [[wu2007-star-barrel-tof-note]] (cites this as ref. [2]) · [[llope2012-star-mrpc-systems-note]] (final TOF and MTD MRPCs)
