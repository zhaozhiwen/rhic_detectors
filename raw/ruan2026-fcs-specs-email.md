---
title: "Ruan 2026 — STAR Forward Calorimeter System (FCS): ECal and HCal (conversion of the email; text verbatim except one corrected unit typo)"
type: raw-source
source_type: email
authors: "Lijuan Ruan (BNL)"
venue: "email, 2026-10-29"
doi: none
arxiv: none
captured_via: "docx converted to Markdown, 2026-11-05"
captured_date: 2026-11-05
captured_as: verbatim conversion
figures: 0
---

# STAR Forward Calorimeter System (FCS): ECal and HCal

- **Source:** email from Lijuan Ruan, 2026-10-29; original file `assets/ruan2026-fcs-specs-email/source.docx`
- **Converted:** 2026-11-05, from the .docx text (a single paragraph with tab stops and line breaks). The tab-aligned block became a Markdown table. Everything else is kept verbatim, except one corrected unit typo (see the last section). My additions are only in the last section, tagged **[note]** and **[source issue]**.

## 1. Overview

A lead/scintillator shashlik electromagnetic calorimeter of 18 radiation lengths in 5.5 cm towers, backed by a steel/scintillator hadron calorimeter of 4.5 interaction lengths in 10 cm towers, both SiPM read out, covering roughly 2.2 < eta < 4.3 at 7-8 m from the interaction point, with the electromagnetic section built from re-used PHENIX PbSc modules.

| | ECal | HCal |
|---|---|---|
| technology | Pb / scintillator, sampling, WLS fibre | Fe / scintillator, sampling, WLS plate |
| absorber | 1.5 mm lead x 65 | 20 mm steel x 36 |
| active | 4.0 mm scint x 66 | 3.0 mm scint x 36 |
| layer pitch | 5.74 mm | 23.4 mm |
| tower face | 5.542 x 5.542 cm | 9.99 x 9.99 cm |
| tower depth | 37.73 cm | 84.24 cm (+10 mm back plate) |
| towers per half | 22 col x 34 row = 748 | 13 col x 20 row = 260 |
| total towers | 1496 (two halves) | 520 (two halves) |
| front face z | 710.16 cm | 782.63 cm |
| depth | 18.1 X0 / 0.93 lambda | 41 X0 / 4.45 lambda |
| effective X0 | 2.06 cm | -- |
| effective lambda | -- | 18.9 cm |
| Moliere radius | 5.6 cm | -- |
| sampling fraction | 0.20 | 0.0145 |
| readout | SiPM | SiPM |
| DEP boards per half | 24 | 9 |

The two "halves" are North and South of the beam line

## 2. ECal: lead / scintillator sampling

**Construction**

- 66 scintillator layers, each 4.00 mm thick, each wrapped in 2 x 0.12 mm paper
- 65 lead layers, each 1.50 mm -- no lead after the last scintillator (:276)
- 0.5 cm back plastic plate
- layer pitch 1.5 + 4.0 + 0.24 = 5.74 mm
- stack depth 66 x 4.24 + 65 x 1.50 = 377.3 mm → 37.73 cm

This is the classic lead-scintillator shashlik construction with wavelength-shifting fibres running through the stack, read out at the back. The cell size, layer count and layer thicknesses are those of the PHENIX PbSc electromagnetic calorimeter, which these modules come from.

## 3. HCal: steel / scintillator sampling

**Construction**

- 36 layers, pitch 23.4 mm, each layer
  - 20.0 mm steel absorber
  - 3.0 mm scintillator
  - remainder air gap, (23.4 - 20.0 - 3.0)/2 either side
- 10 mm steel back plate
- 3 mm wavelength-shifting plate down one side of each tower , which is how the light is collected -- a WLS plate, not fibres through the stack
- stack depth 36 x 2.34 = 84.24 cm, 85.24 cm including the back plate

4.45 lambda contains roughly 95% of a pion shower's energy at these momenta but not the tail; combined with the ECal in front the total is about 5.4 lambda.

## Conversion notes and checks

All arithmetic was recomputed. Material constants used: Pb X0 = 0.56 cm and λ_I = 17.6 cm; Fe X0 = 1.76 cm and λ_I = 16.8 cm (PDG values).

- **[source issue] (corrected here)** In the ECal stack depth, the email has 66 × 4.24 + 65 × 1.50 = "37.73 mm". The sum is 377.3 mm, and this file now reads 377.3 mm. The final 37.73 cm was already correct.
- **[source issue]** "(:276)" after the lead-layer line looks like a leftover line reference, probably to a geometry or source file. Its meaning isn't given.
- **[note]** The ECal effective X0 from the table (37.73 cm / 18.1 X0) is 2.08 cm, against the 2.06 cm quoted. The small difference probably comes from rounding or from counting the paper wrap.
- **[note]** These items are consistent:
  - layer pitches: 1.5 + 4.0 + 0.24 = 5.74 mm and 20 + 3 + 2 × 0.2 = 23.4 mm (0.2 mm air gap each side)
  - tower counts: 748, 1496, 260 and 520
  - HCal depth: 84.24 / 85.24 cm
  - HCal effective λ: 84.24 / 4.45 = 18.9 cm
  - HCal 41 X0: 73 cm of steel / 1.76 cm ≈ 41.5
  - HCal 4.45 λ: about 4.35 λ from 73 cm of steel, plus about 0.1 λ from scintillator
  - ECal + HCal total: 0.93 + 4.45 = 5.38 ≈ 5.4 λ
- **[note]** Estimated from the lead alone, the ECal depth is 9.75 cm / 0.56 cm ≈ 17.4 X0; the scintillator adds about 0.6 X0, giving about 18.0 X0. This agrees with the 18.1 X0 quoted.
- **[note]** Face size of one half, computed from columns and rows × tower face:
  - ECal: about 1.22 m × 1.88 m
  - HCal: about 1.30 m × 2.00 m
  - The email doesn't say whether columns run horizontally.
- **[note]** The email has no "1." section number; the Overview heading was added here.
