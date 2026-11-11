---
title: "Ruan 2026 — STAR Forward Calorimeter System (FCS): ECal and HCal construction specs (curated notes)"
type: raw-note
source_type: email
companion: ruan2026-fcs-specs-email.md
authors: "Lijuan Ruan (BNL)"
venue: "email, 2026-10-29"
doi: none
arxiv: none
notes_updated: 2026-11-09
ingested_version: "email as .docx (assets/ruan2026-fcs-specs-email/source.docx), converted to Markdown 2026-11-05; text verbatim except one corrected unit typo"
earlier_version: []
later_version: []
published_version: "none -- private email, not peer-reviewed; published in this repo with Zhiwen's agreement"
version_facts: "Email dated 2026-10-29. No section number '1.' in the original; the Overview heading was added in the conversion."
versions_checked: 2026-11-09
---

# Ruan 2026 — Curated Notes

> **Full source:** [ruan2026-fcs-specs-email](ruan2026-fcs-specs-email.md) · Companion notes to [ruan2026-fcs-specs-email](ruan2026-fcs-specs-email.md) (full source).
> **Links:** no DOI (email) · **Original:** `assets/ruan2026-fcs-specs-email/source.docx`

## Bibliographic / source

- **Title (as converted):** STAR Forward Calorimeter System (FCS): ECal and HCal
- **From:** Lijuan Ruan (BNL), email of 2026-10-29.
- **Form:** one .docx paragraph with tab stops and line breaks; the tab-aligned block was turned into a Markdown table.

## What kind of source

Private email with construction specifications of the as-built FCS — **not peer-reviewed**; internal/collaboration material published with Zhiwen's agreement. No figures, no references, no performance numbers. The only source in this repo with full layer-by-layer stack dimensions, z positions and DEP board counts.

## Summary (paraphrased)

The FCS is a Pb/scintillator shashlik ECal (18 X0, 5.5 cm towers, re-used PHENIX PbSc modules) in front of a steel/scintillator HCal (4.5 λ, 10 cm towers), both with SiPM readout, at 7–8 m from the interaction point and covering roughly 2.2 < η < 4.3, in North and South halves.

## Key numbers

| | ECal | HCal |
|---|---|---|
| technology | Pb / scintillator, sampling, WLS fibre | Fe / scintillator, sampling, WLS plate |
| absorber | 1.5 mm lead × 65 | 20 mm steel × 36 |
| active | 4.0 mm scint × 66 | 3.0 mm scint × 36 |
| layer pitch | 5.74 mm | 23.4 mm |
| tower face | 5.542 × 5.542 cm | 9.99 × 9.99 cm |
| tower depth | 37.73 cm | 84.24 cm (+10 mm back plate) |
| towers per half | 22 col × 34 row = 748 | 13 col × 20 row = 260 |
| total towers | 1496 | 520 |
| front face z | 710.16 cm | 782.63 cm |
| depth | 18.1 X0 / 0.93 λ | 41 X0 / 4.45 λ |
| effective X0 / λ | X0 2.06 cm | λ 18.9 cm |
| Molière radius | 5.6 cm | — |
| sampling fraction | 0.20 | 0.0145 |
| readout | SiPM | SiPM |
| DEP boards per half | 24 | 9 |

- ECal layers: scintillator 4.00 mm wrapped in 2 × 0.12 mm paper; no lead after the last scintillator; 0.5 cm back plastic plate; stack 66 × 4.24 + 65 × 1.50 = 377.3 mm. WLS fibres through the stack, "read out at the back". Cell size, layer count and thicknesses are those of the PHENIX PbSc EMCal.
- HCal layers: 20.0 mm steel + 3.0 mm scintillator + air gap (0.2 mm each side); 10 mm steel back plate; 3 mm WLS plate down one side of each tower (plate, not fibres); 85.24 cm including back plate.
- Email claims 4.45 λ contains roughly 95% of a pion shower's energy at these momenta (not the tail); ECal + HCal ≈ 5.4 λ.
- Halves are North and South of the beam line.

## What it does not give

- No energy resolution, e/h, calibration, SiPM type/count per tower, bias, radiation damage, or electronics details beyond DEP board counts.
- No gap size at the beam pipe; no statement of whether columns run horizontally; no source for the "95%" containment figure.

## Source issues and caveats

- **[source issue] (corrected)** ECal stack depth written "37.73 mm" for 66 × 4.24 + 65 × 1.50; the sum is 377.3 mm (final 37.73 cm already correct). The Layer-3 file carries the corrected value.
- **[source issue]** "(:276)" after the lead-layer line — apparently a leftover line reference; meaning not given.
- ECal effective X0 recomputed as 37.73 cm / 18.1 = 2.08 cm vs 2.06 cm quoted (rounding or paper wrap).
- All other arithmetic consistent (pitches, tower counts, HCal depths, 18.9 cm effective λ, ≈ 41.5 X0 from 73 cm steel, 0.93 + 4.45 = 5.38 ≈ 5.4 λ). ECal X0 from layers ≈ 18.0.
- Not peer-reviewed; internal/collaboration material published with Zhiwen's agreement.

## FCS cross-checks with the other FCS sources

- **ECal tower length:** 37.73 cm here vs 33 cm in [gagliardi2022-star-forward-upgrade-talk-note](gagliardi2022-star-forward-upgrade-talk-note.md) (and the QM2023 slides quoted in [wang2024-star-forward-upgrade-note](wang2024-star-forward-upgrade-note.md)) — unexplained.
- **ECal depth:** 0.93 λ here vs 0.85 λ_I in the talk; recomputed from the layer stack ≈ 0.90 λ_I. X0 agrees (18.1 vs 18).
- **Readout end:** ECal WLS fibres "read out at the back" here vs Wang 2024 "SiPM-based readout electronics on the front face"; **[note]** the Tsai 2015 prototype was read out upstream of the beam (front). Unresolved — see [open-questions](../wiki/synthesis/open-questions.md).
- **η coverage:** "roughly 2.2 < eta < 4.3" here vs 2.5 < η < 4 in the paper and talk; the 2.2 is the outer geometric corner (ECal corner η = 2.23 at z = 710.16 cm, computed in the Wang 2024 and Gagliardi 2022 Layer-3 files), 2.5 roughly the full-azimuth edge.
- Agree: channel counts 1496 / 520; ≈ 7 m location; PHENIX-module ECal; HCal 20 mm Fe / 3 mm Sc, 84 cm, ≈ 4.5 λ; two halves.
- Versus the 2014 prototype ([tsai2015-fcs-prototype-note](tsai2015-fcs-prototype-note.md)): ECal technology, HCal absorber (Pb(Sb) 10 mm → steel 20 mm) and tower counts all changed; the WLS-plate HCal light collection and SiPM readout survived.

## Relevance

Reference for the as-built [star-fcs](../wiki/synthesis/star-fcs.md) geometry: layer stacks, tower counts, z positions, depths in X0 and λ, sampling fractions and DEP board counts. Depth figures (HCal 4.45 λ; total ≈ 5.4 λ) are inputs for hadron-shower containment and [pi-mu-separation-calorimetry](../wiki/synthesis/pi-mu-separation-calorimetry.md) arguments. October 2026 status of the FCS: [star2026-detector-status-note](star2026-detector-status-note.md).

## Related

- Synthesis: [star-fcs](../wiki/synthesis/star-fcs.md) · [pi-mu-separation-calorimetry](../wiki/synthesis/pi-mu-separation-calorimetry.md) · [rhic-detector-status](../wiki/synthesis/rhic-detector-status.md) · [open-questions](../wiki/synthesis/open-questions.md)
- Notes: [tsai2015-fcs-prototype-note](tsai2015-fcs-prototype-note.md) · [wang2024-star-forward-upgrade-note](wang2024-star-forward-upgrade-note.md) · [gagliardi2022-star-forward-upgrade-talk-note](gagliardi2022-star-forward-upgrade-talk-note.md) · [star2026-detector-status-note](star2026-detector-status-note.md)
