---
title: "Shao 2002 — Beam test results of two kinds of multi-gap resistive plate chambers (full-content paraphrase)"
type: raw-source
source_type: paper
authors: "M. Shao et al. (10 authors; USTC Hefei; corresponding author J. Wu)"
journal: "Nucl. Instrum. Meth. A 492 (2002) 344–350"
doi: "10.1016/S0168-9002(02)01355-4"
arxiv: none
captured_via: "Route 3 — publisher PDF only (ScienceDirect served no HTML body; no arXiv version); text from pdftotext -layout, every page also rendered at 130 and 300 dpi and read by eye; figures cropped from 200 dpi renders"
captured_date: 2026-11-06
captured_as: full-content paraphrase
figures: "10 (vision descriptions added 2026-11-06)"
vision_model: "general-purpose subagent (session model, not recorded), 2026-11-06"
---

# Beam test results of two kinds of multi-gap resistive plate chambers (Shao et al., NIM A 2002) — reading note

- **Citation:** M. Shao, L.J. Ruan, H.F. Chen, J. Wu (corresponding, wujian@ustc.edu.cn), C. Li, Z.Z. Xu, X.L. Wang, S.L. Huang, Z.M. Wang, Z.P. Zhang, "Beam test results of two kinds of multi-gap resistive plate chambers". Department of Modern Physics, University of Science and Technology of China (USTC), Hefei, 230027 Anhui, China.
- **Journal ref:** Nucl. Instrum. Meth. A 492 (2002) 344–350. Received 21 March 2002; revised 27 June 2002; accepted 9 July 2002. **DOI:** [10.1016/S0168-9002(02)01355-4](https://doi.org/10.1016/S0168-9002(02)01355-4) (ScienceDirect PII S0168900202013554). Title, author list, volume and pages confirmed with the Crossref API and on page 1 of the publisher PDF.
- **arXiv:** none. An arXiv API search (title "resistive plate chambers" AND author Shao) returns only the 2008 long-strip MRPC paper (0805.2459), not this one.
- **Route used:** Route 3, PDF only. Text from `pdftotext -layout` of the publisher PDF; every page was also rendered (130 and 300 dpi) and read by eye, because the PDF text layer garbles symbols (Ω shows as "O", × is dropped, ± shows as "7", μ shows as "m", ° shows as "1"). **Why Route 1 failed:** the ScienceDirect article page (JLab access, "Full text access") serves only the abstract, PACS codes, keywords and "View PDF". There is no HTML body, no MathML and no `<figure>` elements. **Why Route 2 failed:** no arXiv version exists.
- **PDF backup:** `assets/shao2002-mrpc-beam-test/source.pdf` (publisher PDF, 7 pages, 419 006 bytes; downloaded from pdf.sciencedirectassets.com on 2026-11-06 by script).
- **Figures:** `assets/shao2002-mrpc-beam-test/fig1.png` … `fig10.png`, cropped from the publisher PDF rendered at 200 dpi (no HTML figures exist). Each crop includes its caption and was checked by eye.
- **Verification:** every number below was checked against `pdftotext -layout` of the publisher PDF and against the rendered pages (the rendered page wins where the text layer garbles a symbol). Numbers printed inside the figures (dimension labels in Figs. 1–2, fit boxes in Figs. 5 and 10, HV labels in Figs. 6, 7, 9, the time-walk slope in Fig. 4) were read from the 300 dpi renders. The paper has **no numbered equations and no tables**. The few formulas below are my own derived checks, tagged **[note]**.
- Figure descriptions were added by a separate figure pass that looked at the images.

---

## Abstract

The paper reports beam tests of a 6-gap and a 10-gap Multi-gap Resistive Plate Chamber (MRPC) and describes the setup in the CERN PS-T10 area. The 6-gap MRPC has a time resolution of about **65 ps** (the abstract says "time resolution and detection efficiency … is around 65 ps"), good enough for the STAR TOF detector. The 10-gap MRPC has a time resolution **below 55 ps**.

- PACS: 12.38Qk; 29.40Gx; 29.40Cs. Keywords: MRPC; Time resolution; TOF.
- **[source issue]** The abstract spells the acronym "MPRCs" once (should be MRPCs). It also attaches "around 65 ps" to both "time resolution and detection efficiency", which only makes sense for the time resolution.

## 1. Introduction

- TOF detectors need high time resolution, high efficiency and low cost; MRPCs are a good candidate. The traditional TOF is shaped scintillators read by fast PMTs.
- For RHIC-STAR, a PMT TOF would need about **25,000 fast PMTs** to cover **64 m²**. Each PMT unit would cover **6.3 × 3.1 cm²** to give the needed granularity, which matters in STAR because heavy-ion collisions produce many final-state particles. The PMTs would also have to be insensitive to magnetic fields. The cost of a PMT solution is too high.
  - **[note]** 25,000 × 6.3 × 3.1 cm² = 48.8 m², not 64 m². Equivalently 64 m²/25,000 = 25.6 cm² per PMT. The difference is presumably dead area or overlaps; the paper does not explain it.
- MRPC technology [1,2] uses only cheap materials and makes an affordable TOF with good timing possible.
- An MRPC is a stack of parallel glass plates with bulk resistivity of about **10¹²–10¹³ Ω cm** between two electrode plates. The gap between glass plates is **0.2–0.3 mm**. The outermost glass plates are connected to HV through resistive electrodes. With a gas mixture containing some freon the chamber runs in **avalanche mode**.
- A charged particle ionizes the gas in the gaps. The avalanches in the high field induce signals on the electrodes. The resistive plates are electrically floating, so they have no internal field and are transparent to the induced signals. The signal on the electrodes is the **analogue sum** of the signals induced by every gap. Small gaps keep the fluctuation of avalanche development time small, which improves time resolution.
- ALICE (LHC) and STAR (RHIC) both chose MRPCs for their new TOF systems. The USTC HEP group recently joined STAR and is designing and testing MRPC units for the STAR TOF. Preliminary results and the structure of a single-cell MRPC were reported earlier [3]. This paper gives the detailed structure of two multi-cell MRPCs and their beam-test results at the CERN PS-T10 facility.

## 2. Chamber structure and experimental setup

### 6-gap MRPC

- **12 readout units in a 2 × 6 array.** Cross-section in Fig. 1.
- Each electrode pad on the printed circuit board (PCB) covers **3.1 × 3.0 cm²**. There is a **3 mm** gap between pads. The total sensitive area is **20 × 6.3 cm²**.
- Glass stack: **five layers of 0.70 mm glass between two layers of 1.2 mm glass** (7 plates, 6 gas gaps).
- The text says "inner and outer glass plates cover an area of **21.6 × 8.9** and **19.8 × 6.8 cm²**, respectively".
  - **[source issue]** The text swaps inner and outer. Fig. 1 labels the **inner** glass as 198 mm long × 68 mm wide (= 19.8 × 6.8 cm²) and the **outer** glass as 216 mm long ("PC board, mylar and outer glass width = 216 mm") × 89 mm wide (= 21.6 × 8.9 cm²). The figure is self-consistent (outer plates are larger and carry the electrodes), so the figure is right.
- Glass: "Shanghai glass". Bulk resistivity **2.57 × 10¹³ Ω cm** for the 0.7 mm glass and **1.8 × 10¹³ Ω cm** for the 1.2 mm glass, measured at **16 °C**.
- Gas gap: **250 μm**, set by nylon fiber of that diameter.
- Electrodes: the outer surfaces of the thick (outer) glass are coated with a carbon film of surface resistivity **8 × 10⁵ Ω/□**. These are the electrodes for positive and negative HV. A mylar film separates the carbon film from the readout pads.
- Mechanics: **6 mm honeycomb plates** outside the PCBs keep the structure rigid and the glass flat.
- The MRPC sits in a sealed box flushed with **90% C₂H₂F₄, 5% SF₆, 5% iso-C₄H₁₀** at **1 atm**. SF₆ quenches streamers to keep avalanche mode.

![Fig. 1](assets/shao2002-mrpc-beam-test/fig1.png)

**Fig. 1.** Structure of the 6-gap MRPC: (a) longitudinal view, (b) transverse view.

*Figure description (from the image):* Two-panel cross-section line drawing with legend: PC board (hatched), pad (dark grey), electrode (graphite) (black), mylar (white), glass (light grey); no scale bar. (a) Longitudinal view, top to bottom: hatched PC board; mylar layer carrying a row of 6 dark-grey pads separated by 5 small white gaps; black graphite electrode; outer glass; 5 thinner, shorter inner glass plates; outer glass; electrode; mylar with 6 pads; PC board. Printed dimensions: "electrode length = 208 mm" (end-to-end span of the electrode); "pad width = 3mm" (arrow spans one pad); "pad gap = 0.3mm" (gap between two pads); "PC Board thickness = 1.5 mm" (top board); "outer glass thickness = 1.2mm"; "gas gap = 250 micron" (arrow into the inner-plate stack); "inner glass thickness = 0.7mm"; "inner glass length = 198 mm"; "PC board, mylar and outer glass width = 216 mm" (full length of board, mylar and outer glass). (b) Transverse view: same layer order with 2 pads per PC board (one central gap) and 5 inner plates between 2 outer plates; the upper PC board is narrower than the bottom PC board; unlabelled dark-grey blocks stand at both sides of the stack (same fill as the legend's "pad") and thin vertical rods pass through both boards at each end; a dashed region labelled "signal trace area" lies on the bottom board to the right of the stack. Printed dimensions: "upper PC board width = 102mm"; "mylar tape width = 93 mm"; "pad width = 31*2+3 = 65 mm" (two pads plus gap); "inner glass width = 68 mm"; "electrode width = 80 mm"; "outer glass width = 89 mm"; "bottom PC board width = 126 mm". No honeycomb plate is drawn. Main feature: a 7-plate, 6-gap glass stack with graphite electrodes on the outer glass and pads on the inner faces of the two PC boards.

- **[note]** The 6 mm honeycomb plates described in the text are not drawn in Fig. 1 (nor in Fig. 2). The dark-grey side blocks in (b) are not labelled; their fill matches the legend's "pad", so their identity cannot be read from the figure.
- **[note]** The (a) labels "pad width = 3mm" and "pad gap = 0.3mm" are the unit issue flagged in the [source issue] below the dimension table.

**[note] Dimension labels read from Fig. 1** (300 dpi render):

| Item (Fig. 1) | Value |
|---|---|
| electrode length (a) | 208 mm |
| "pad width" (a) | printed "3mm" — see [source issue] below |
| "pad gap" (a) | printed "0.3mm" — see [source issue] below |
| PC board thickness (a) | 1.5 mm |
| outer glass thickness (a) | 1.2 mm |
| gas gap (a) | 250 micron |
| inner glass thickness (a) | 0.7 mm |
| inner glass length (a) | 198 mm |
| PC board, mylar and outer glass width [i.e. length] (a) | 216 mm |
| upper PC board width (b) | 102 mm |
| mylar tape width (b) | 93 mm |
| pad width (b) | 31*2+3 = 65 mm |
| inner glass width (b) | 68 mm |
| electrode width (b) | 80 mm |
| outer glass width (b) | 89 mm |
| bottom PC board width (b) | 126 mm |

- **[source issue]** Fig. 1(a) labels "pad width = 3mm" and "pad gap = 0.3mm". The text says pads are 3.0–3.1 cm with a 3 mm gap, and Fig. 1(b) gives 31 mm pads with a 3 mm gap. The (a) labels must be in cm (3 cm and 0.3 cm). Same in Fig. 2(a) ("pad width = 3mm", "pad internal = 0.3mm").
- **[note]** Longitudinal pad row: 6 × 30 mm + 5 × 3 mm = 195 mm ✓ fits inside the 198 mm inner glass and the 208 mm electrode; ≈ "20 cm" sensitive length ✓. Transverse: 2 × 31 mm + 3 mm = 65 mm ✓ (as printed in Fig. 1b). The text's "6.3 cm" sensitive width is close to but not equal to 65 mm (2 × 3.1 cm = 6.2 cm without the gap). So the pad is **31 mm** in the transverse direction (2 pads across) and **30 mm** in the longitudinal direction (6 pads along).
- **[note]** The "signal trace area" in Fig. 1(b) is at one side, outside the glass stack, where the pad signal traces leave the chamber.

### 10-gap MRPC

- Similar structure and running conditions to the 6-gap chamber (Fig. 2). Glass thicknesses and gap differ.
- It is effectively **two 5-gap MRPCs stacked**, with an extra electrode between them supplying **positive HV**. The **negative HV** goes to the two outer electrodes. The text says "this electrode is used to collect induced signals as well".
  - **[note]** "This electrode" is ambiguous; Fig. 2 shows pads on both outer PCBs and on both faces of the middle PCB. The paper does not say how the stacks' signals are combined (e.g. differential or summed).
- The double stack increases the signal amplitude and improves efficiency and time resolution, at the cost of more space.
- Gas gap **0.22 mm**, set by nylon fiber (Ø 0.22 mm). Fibers in the same gap are about **33 mm** apart to keep the gap variation below **20 μm**. Each fiber is placed over the gap between electrode pads.
  - **[note]** 33 mm = 30 mm pad + 3 mm gap = the longitudinal pad pitch ✓, consistent with "fiber over the pad gap".
  - **[note]** The fiber-placement sentences come right after the 10-gap description, but they likely apply to both chambers.
- At **15 kV** the dark current of each electrode is **below 5 nA**. (Which chamber is not specified; it follows the 10-gap text, but 15 kV is a 6-gap operating voltage.)

![Fig. 2](assets/shao2002-mrpc-beam-test/fig2.png)

**Fig. 2.** Structure of the 10-gap MRPC: (a) longitudinal view, (b) transverse view.

*Figure description (from the image):* Two-panel cross-section line drawing, same legend as Fig. 1 (PC board hatched, pad dark grey, mylar white, electrode (graphite) black, glass light grey). (a) Longitudinal view: two 5-gap stacks, each = outer glass + 4 inner glass plates + outer glass (6 plates), with a graphite electrode on the outside of each outer glass; three PC boards (top, middle, bottom); rows of 6 dark-grey pads with 5 gaps on the inner face of the top and bottom boards and on both faces of the middle board. Printed dimensions: "electrode length = 204 mm"; "pad width = 3mm" (one pad); "pad internal = 0.3mm" (gap between pads); "outer glass thickness = 1.1mm"; "inner glass thickness = 0.6mm"; "gas gap = 220 micron"; "inner glass length = 198 mm"; "outer glass length = 208 mm"; "PC board & mylar length = 214 mm". (b) Transverse view: same two stacks with 2 pads per board face; the middle PC board is the widest and extends on both sides; dashed "signal trace area" region on the middle board to the right of the stacks; unlabelled dark-grey side blocks next to each stack and thin vertical rods through the boards at both ends. Printed dimensions: "mylar tape width = 90 mm"; "electrode width = 80 mm"; "pad width = 31*2+3 = 65 mm"; "inner glass width = 68 mm"; "outer glass width = 85 mm"; "outer PC board width = 102 mm"; "middle PC board width = 126 mm". No honeycomb is drawn. Main feature: double 5-gap stack sharing a central PC board with pads on both faces.

- **[note]** Pads drawn on both faces of the middle PC board and on the inner faces of both outer boards (consistent with the [note] above that "this electrode" is ambiguous). The figure does not show how the pad signals are combined.

**[note] Dimension labels read from Fig. 2:**

| Item (Fig. 2) | Value |
|---|---|
| electrode length (a) | 204 mm |
| "pad width" (a) | printed "3mm" (means 3 cm) |
| "pad internal" (a) | printed "0.3mm" (means 0.3 cm) |
| outer glass thickness (a) | 1.1 mm |
| inner glass thickness (a) | 0.6 mm |
| gas gap (a) | 220 micron |
| inner glass length (a) | 198 mm |
| outer glass length (a) | 208 mm |
| PC board & mylar length (a) | 214 mm |
| mylar tape width (b) | 90 mm |
| electrode width (b) | 80 mm |
| pad width (b) | 31*2+3 = 65 mm |
| inner glass width (b) | 68 mm |
| outer glass width (b) | 85 mm |
| outer PC board width (b) | 102 mm |
| middle PC board width (b) | 126 mm |

- **[note]** Each 5-gap stack in Fig. 2(a) = 2 outer (1.1 mm) + 4 inner (0.6 mm) plates = 6 plates, 5 gaps ✓; two stacks = 10 gaps ✓. The text does not give the 10-gap glass thicknesses or resistivity; they are only in the figure labels.

### Beam-test setup (CERN PS-T10)

- **7 GeV/c pion beam** from the PS: the primary proton beam hits a target, beam optics select 7 GeV/c pions. Some scattered protons remain.
- Beam half-width at the chamber **1.0 cm**. Beam pulse (spill) length **250 ms**. Beam rate **below 100 Hz/cm²**.
- Test system = trigger system + tracking telescope + chamber under test (Fig. 3).
  - **Trigger:** a single-readout MRPC plus two pairs of scintillator counters. The single-readout MRPC is the trigger. The scintillators give the reference start time. Each pair is a scintillation crystal with 2 PMTs; the two pairs are perpendicular to each other. The **average time of the 4 PMTs** is the start time, with a resolution of **30 ps**.
  - **Tracking telescope:** three pairs of multi-wire proportional chambers with **4 mm** wire spacing; position resolution **0.3 mm**.
- The MRPC under test is in its sealed box on a platform movable in three dimensions; gas is fed in and out through plastic pipes. The beam direction is the **Y-axis**; the MRPC faces the beam and can be scanned in **X and Z**.

![Fig. 3](assets/shao2002-mrpc-beam-test/fig3.png)

**Fig. 3.** The MRPC test system at the PS-T10 test-beam facility (caption says "PS-10").

*Figure description (from the image):* Schematic beam-line sketch, not to scale, no dimensions. A horizontal beam line with an arrow at the right labelled "PS π beams" (beam enters from the right). Elements from right (upstream) to left: a box labelled "Trigger MRPC"; a wire-chamber box; "Scintilators" drawn as a small rectangle plus a circle on the beam line; a second wire-chamber box; the box labelled "MRPC" (chamber under test); a third wire-chamber box. The label "Wire Chambers" points with three lines to the three wire-chamber boxes. Main feature: the MRPC under test sits between tracking chambers, downstream of the trigger MRPC and the start scintillators.

- **[note]** The text describes three *pairs* of MWPCs and two *pairs* of perpendicular scintillator counters; the sketch shows three single wire-chamber boxes and one rectangle plus one circle (consistent with two crossed counters). Whether each box is a pair is not shown.
- **[source issue]** The figure label is spelled "Scintilators".

## 3. Results and analysis

### 3.1. The 6-gap MRPC

- Two kinds of test: beam through the chamber centre, and X/Z position scans.
- Centre test at **nine HV settings between 14 and 17 kV** (Fig. 4).
- **Efficiency definition:** events with a non-zero TDC count divided by events recorded by the tracking telescope.
- With efficiency above **97%**, the chamber has an **HV plateau from 15.5 to 17.0 kV**.
- Fig. 4 also shows the time walk vs HV with a fitted slope of **−30.36 ± 1.18 ps/kV** (printed in the panel).
- **Slewing correction:** the time is taken from the rising edge, so signals of different amplitude need correction offline. A **sixth-order polynomial** fits the time–amplitude distribution at small amplitude, and a **linear function** fits the large-amplitude region, giving the correction coefficients. After subtracting the start-time jitter the time resolution is **about 65 ps** (Fig. 5).
  - **[source issue]** "sixth-oder" typo in the source.

![Fig. 4](assets/shao2002-mrpc-beam-test/fig4.png)

**Fig. 4.** Detection efficiency and time resolution of the 6-gap MRPC versus HV (panel title "6×2 cell MRPC"; third panel: time walk vs HV).

*Figure description (from the image):* Three stacked panels sharing the x-axis "High Voltage (kV)", 13.5–17.5 (labels every 0.5); panel title "6×2 cell MRPC". Top: "Efficiency (%)", 75–100 (labels every 5); filled circles at nine HV values (14, 14.5, 15, 15.5, 15.75, 16, 16.25, 16.5, 17 kV) reading ≈85, ≈92, ≈96, ≈98, ≈98, ≈99, ≈99, ≈99, ≈99.5%, with a smooth rising curve that flattens near 99%. Middle: "Time Resolution (ps)", 40–120 (labels every 20); filled squares at the same HVs reading ≈103, ≈101, ≈76, ≈70, ≈64, ≈57, ≈60, ≈60, ≈59 ps, with a smooth falling curve that flattens at ≈58 ps above ≈16.5 kV. Bottom: "Time Walk (ps)", labels −40 to 40 in steps of 20 (axis extends to ≈−50, unlabelled); stars with small error bars at the same HVs reading ≈35, ≈37, ≈20, ≈0, ≈−2, ≈−12, ≈−25, ≈−32, ≈−44 ps, and a straight-line fit; printed "Time walk : -30.36 ± 1.18 ps/kV". Main feature: efficiency plateau ≥98% from 15.5 kV, time resolution saturating near 60 ps, time walk falling linearly with HV.

- **[note]** On the plateau (16–17 kV) Fig. 4 reads ≈57–60 ps, below the "about 65 ps" the text quotes from Fig. 5. The paper does not say whether the Fig. 4 values have the 30 ps start subtracted.
- **[note]** The printed caption ("The detection efficiency and time resolution of the 6-gap MRPC.") does not mention the third (time-walk) panel.

![Fig. 5](assets/shao2002-mrpc-beam-test/fig5.png)

**Fig. 5.** Time distribution of the 6-gap MRPC after correction (x-axis "Time (50ps/chn)").

*Figure description (from the image):* Single histogram with Gaussian fit. x-axis "Time (50ps/chn)", ≈−20 to ≈36 channels, labels "-20", "10" (sic, at −10), "0", "10", "20", "30". y-axis "Counts", logarithmic, labels 1, 10, 10² (axis runs from below 1 to ≈700). Step histogram with a smooth Gaussian curve over the core. Stat box: ID 192; Entries 1227; χ²/ndf 26.93 / 11; Constant 361.6; Mean -0.1650; Sigma 1.324. Peak ≈370 counts at 0; Gaussian core over about ±5 channels; tail bins of a few counts at ≈+3 to +5 channels lie above the fit; isolated 1-count bins at ≈−8, ≈−5.5 and ≈+10 channels. Main feature: σ = 1.324 channels (66.2 ps at 50 ps/channel).

- **[note] Fig. 5 fit box:** ID 192, Entries 1227, χ²/ndf = 26.93/11, Constant 361.6, Mean −0.1650, Sigma 1.324 (channels). With 50 ps/channel:

$$\sigma_{\rm fit} = 1.324 \times 50~{\rm ps} = 66.2~{\rm ps}, \qquad \sqrt{66.2^2 - 30^2}~{\rm ps} = 59.0~{\rm ps}$$

  The text says "after subtracting the start time jitter … around 65 ps as shown in Fig. 5". The fitted width alone is already 66.2 ps; if the 30 ps start were subtracted from that in quadrature one would get 59 ps. So either the histogram is already start-subtracted, or "65 ps" is the raw width including the start. The paper does not resolve this. ✓ arithmetic.
- **[source issue]** In Fig. 5 the x-axis tick left of 0 is printed "10" instead of "−10".

- **X scan** at **±7.875 kV** (Fig. 6) across pads 3 and 2. It shows the edge effect at the gap between pads: efficiency drops to about **80%** and time resolution degrades to about **100 ps** there. The dotted straight line marks each pad's boundary (in the printed figure the pads are shown as grey bands).
  - **[note]** ±7.875 kV = 15.75 kV across the stack, on the Fig. 4 plateau ✓.
- **Z scan** (Fig. 7): results similar to the X scan.

![Fig. 6](assets/shao2002-mrpc-beam-test/fig6.png)

**Fig. 6.** Scan results of the 6-gap MRPC along the X-axis (Pad 2 & Pad 3, X scan; HV ±7.875 kV; time resolution and efficiency vs position).

*Figure description (from the image):* Single panel with two y-axes. x-axis "Pad 2 & Pad 3, X scan (mm)", ≈−50 to 50, labels −40, −20, 0, 20, 40. Left y "Time Resolution (ps)", 0–200 (labels every 20); right y "Efficiency (%)", 0–100 (labels every 20). Two light-grey bands labelled "Pad 3" (≈−31.7 to ≈−1.5 mm) and "Pad 2" (≈+1.5 to ≈+31.7 mm), i.e. ≈30 mm wide with a ≈3 mm white gap centred at 0. Legend: "●-■ Time resolution", "○-□ Efficiency"; squares = Pad 3, circles = Pad 2. Box: "High Voltage: ±7.875kV". Efficiency (open markers, smooth curves): ≈97–99% inside each pad; Pad 3 falls to ≈88% at ≈−1 mm and ≈81% at ≈+1 mm; Pad 2 is ≈89% at ≈−1.7 mm and ≈93% at ≈0 to +2 mm. The two curves cross at ≈89% near −1 mm. Time resolution (filled markers): Pad 3 ≈58–68 ps from ≈−21 to ≈−7 mm, rising to ≈73, ≈83, ≈84.5 and ≈91 ps approaching the gap (last at ≈+1 mm); Pad 2 ≈145 ps at ≈−1.7 mm and ≈124 ps at ≈+0.3 mm (both with large error bars), ≈102 ps at ≈+2 mm, ≈81–88 ps at ≈4–8 mm, ≈62–68 ps from ≈10 to ≈22 mm, then rising to ≈75, ≈83, ≈91 and ≈110 ps at ≈24–30 mm. Main feature: efficiency loss and timing degradation in the inter-pad gap and at the outer pad edge.

- **[note]** No dotted boundary lines are visible; the pads are shown as grey bands (as the note above says). The band widths (≈30 mm, ≈3 mm gap) match the 30 mm pad dimension and 3 mm gap in the text.
- **[note]** In the gap the Pad 2 time-resolution points reach ≈124–145 ps (large error bars), above the "about 100 ps" in the text; the ≈81% Pad 3 efficiency at ≈+1 mm matches "about 80%".

![Fig. 7](assets/shao2002-mrpc-beam-test/fig7.png)

**Fig. 7.** Scan results of the 6-gap MRPC along the Z-axis (Pad 1, Z scan; HV ±8.25 kV).

*Figure description (from the image):* Single panel with two y-axes. x-axis "Pad 1, Z scan (mm)", −30 to 30 (labels every 10). Left y "Time Resolution (ps)", 0–200 (labels every 20); right y "Efficiency (%)", 0–100 (labels every 10). Legend: filled markers with solid curve = "Time resolution"; open squares with dotted curve = "Efficiency". Box: "High Voltage: ±8.25kV". Time resolution (21 points, ≈2 mm steps from ≈−19 to ≈+21 mm): ≈56 ps at ≈−19 mm, ≈61–72 ps from ≈−17 to ≈+9 mm, then ≈72 (≈11 mm), ≈75 (≈13), ≈81 (≈15), ≈86 (≈17), ≈104 ps at ≈19 and ≈21 mm (the last with error bar ≈87–120 ps). Efficiency: ≈92.5% at ≈−19 mm, ≈97% at ≈−17 mm, ≈99% from ≈−15 to ≈+9 mm, then ≈97% (≈11 mm), ≈95% (≈13), ≈88% (≈15), ≈79% (≈17); no efficiency markers between ≈−7 and ≈−1 mm or beyond ≈+17 mm; the dotted curve continues down to ≈48% at ≈+20 mm. Main feature: flat ≈65 ps timing and ≈99% efficiency over the pad, with a sharp edge on the +Z side.

- **[note]** Fig. 7's HV label is ±8.25 kV (16.5 kV total), different from the ±7.875 kV of the X scan; the text does not mention this.

### 3.2. The 10-gap MRPC

- Fig. 8: efficiency and time resolution vs HV (22.5–25 kV). Efficiency reaches **98%** at **22.5 kV**; time resolution is **54 ps** at **23.5 kV**. At **25.0 kV** a few large-amplitude streamer signals appear. Working HV set to **23.5 kV**.
- X scan at 23.5 kV (Fig. 9). Within **10 mm** of the chamber centre the time resolution is mostly about **50 ps** and the efficiency is above **99%**. At the centre the time resolution is as good as **40 ps**. Near the edge of the readout strip results are worse: a particle hitting the edge induces signal on **two neighbouring strips**, so there is **cross-talk** between the two sides, which worsens the time resolution.
- The position in the figure is reconstructed from the **tracking system**, and the quoted time resolution **includes electronic jitter**. Overall time resolution about **55 ps** (Fig. 10).

![Fig. 8](assets/shao2002-mrpc-beam-test/fig8.png)

**Fig. 8.** Efficiency and time resolution of the 10-gap MRPC versus HV.

*Figure description (from the image):* Single panel with two y-axes. x-axis "High Voltage (kV)", 22–26 (labels every 0.5). Left y "Efficiency (%)", 94–100 (labels every 1); right y "Time resolution (ps)", 50–75 (labels every 2.5). Legend: filled circles = "Efficiency", filled squares = "Time resolution"; points at 22.5, 23, 23.5, 24 and 25 kV (none at 24.5 kV), no error bars. Efficiency ≈98.9, ≈99.4, ≈99.3, ≈99.2, ≈99.6% with a slowly rising fitted curve; time resolution ≈56.6, ≈55.4, ≈53.4, ≈56.6, ≈56.0 ps with a shallow U-shaped curve (minimum ≈55 ps near 23.7 kV). Main feature: efficiency ≥98.9% and timing ≈53–57 ps over the whole 22.5–25 kV range.

- **[note]** The plot reads ≈98.9% at 22.5 kV, higher than the "98% at 22.5 kV" in the text. The 23.5 kV time resolution reads ≈53.4 ps, consistent with the quoted 54 ps.

![Fig. 9](assets/shao2002-mrpc-beam-test/fig9.png)

**Fig. 9.** Scan results for (a) pad 4 (HV 23.5 kV) and (b) pads 3 and 4 (HV ±5.875*2 kV) of the 10-gap MRPC.

*Figure description (from the image):* Two stacked panels, each with two y-axes and x-axis −30 to 30 mm (labels every 10). (a) x "Pad 4, X scan (mm)"; left "Time Resolution (ps)" 0–140 (labels every 20); right "Efficiency (%)" 90–100 (labels every 1). Legend: filled points + curve = "Time resolution", open squares + curve = "Efficiency". Box: "High Voltage: 23.5kV". Efficiency ≈99–99.8% from ≈−12 to ≈+16 mm, except ≈98.7% at ≈−2 mm and ≈97.3% at ≈+13.7 mm; fitted curve peaks ≈99.6% near −4 mm. Time resolution (≈2 mm steps from ≈−16 to ≈+16 mm): ≈60 (large error bar ≈42–78), ≈65, ≈47, ≈50, ≈52.5, ≈49.5, ≈55, ≈53.5, ≈41.5 ps at ≈0 mm (error bar ≈23–61 ps), ≈52, ≈52.5, ≈47.5, ≈64, ≈73.5, ≈71.5, ≈89 (≈+13.7 mm), ≈65 ps (≈+15.7 mm); parabola-like fit with minimum ≈49 ps near −4 mm, rising to ≈80 ps at +15 mm. (b) x "Pad 3-4, X scan (mm)"; left "Time Resolution (ps)" 0–150 (labels every 20 up to 140); right "Efficiency (%)" 85–100 (labels 86–100 every 2). Labels "Pad 4" (left) and "Pad 3" (right); an unlabelled hatched band from ≈−3.5 to ≈+3.4 mm extends from 50 ps to the top. Legend: "●-○ Time resolution", "□-■ Efficiency" (filled time points and open efficiency squares = Pad 4; open time points and filled efficiency squares = Pad 3). Box: "High Voltage: ±5.875*2 kV". Efficiency ≈99.2–99.8% away from the band; Pad 4 dips to ≈97.3% at ≈0 mm; Pad 3 ≈99.0% at ≈+2 mm. Time resolution: Pad 4 ≈41.5 ps at ≈−13.5 mm (error bar ≈23–60), ≈52, ≈52.5, ≈47.5, ≈64, ≈74, ≈72, ≈89 ps at ≈0 mm; Pad 3 ≈65 ps at ≈+2 mm, then ≈59, ≈53.5, ≈50, ≈49.5, ≈42, ≈47, ≈49 ps out to ≈+17.5 mm; curves peak at the band. Main feature: ≈50 ps timing and >99% efficiency inside the pads, worse timing (to ≈89 ps) at the pad boundary.

- **[note]** The x origin differs between panels: in (a) the scan spans one pad (≈−16 to +16 mm); in (b) 0 is at the inter-pad boundary (hatched band).
- **[note]** In (a), within ±10 mm one efficiency point (≈−2 mm) reads ≈98.7%, slightly below the text's "above 99%"; the "as good as 40 ps" at the centre is the ≈41.5 ps point at ≈0 mm, whose error bar spans ≈23–61 ps.
- **[note]** The hatched band in (b) is ≈7 mm wide, wider than the 3 mm pad gap; neither the caption nor the text explains it.

![Fig. 10](assets/shao2002-mrpc-beam-test/fig10.png)

**Fig. 10.** Time distribution of the 10-gap MRPC after correction.

*Figure description (from the image):* Single histogram with Gaussian fit. x-axis "Time (50ps/chn)", −20 to ≈31 channels, labels −20, −10, 0, 10, 20, 30. y-axis "Counts", logarithmic, labels 1, 10, 10², 10³. Step histogram with a smooth Gaussian curve. Stat box: ID 192; Entries 1944; Mean -0.3117E-01; RMS 1.223; UDFLW 0.000; OVFLW 3.000; χ²/ndf 20.88 / 10; Constant 664.5; Mean -0.4752E-01; Sigma 1.153. Peak ≈650 counts near 0; Gaussian core over about ±4 channels; tail bins of a few counts at ≈+4 to +5 channels lie above the fit; isolated 1-count bins at ≈−9, ≈−7 to −5 and ≈+6.5 channels. Main feature: σ = 1.153 channels (57.7 ps at 50 ps/channel), narrower than Fig. 5.

- **[note] Fig. 10 fit box:** ID 192, Entries 1944, Mean −0.3117E−01, RMS 1.223, UDFLW 0.000, OVFLW 3.000, χ²/ndf = 20.88/10, Constant 664.5, Mean −0.4752E−01, Sigma 1.153 (channels).

$$\sigma_{\rm fit} = 1.153 \times 50~{\rm ps} = 57.7~{\rm ps}, \quad {\rm RMS} = 1.223\times 50~{\rm ps} = 61.2~{\rm ps}, \quad \sqrt{57.65^2-30^2}~{\rm ps} = 49.2~{\rm ps}$$

  The text quotes "about 55 ps" for Fig. 10, which is closer to neither 57.7 ps (raw) nor 49.2 ps (start subtracted); same ambiguity as Fig. 5. ✓ arithmetic.
- **[note] HV per gap.** Fig. 9(b) gives ±5.875 kV "×2", i.e. 11.75 kV across each 5-gap stack, 23.5 kV summed. Field in the gas (floating glass carries no field in steady state):

$$E_{6\text{-gap}} = \frac{15.75~{\rm kV}}{6 \times 0.025~{\rm cm}} = 105~{\rm kV/cm}, \qquad E_{10\text{-gap}} = \frac{11.75~{\rm kV}}{5 \times 0.022~{\rm cm}} = 106.8~{\rm kV/cm}$$

  So the 10-gap "23.5 kV" is the sum over the two stacks, and both chambers run at about the same gas field ✓.

## 4. Conclusions

- MRPCs are stable, reliable and cheap; their timing is much better than single-gap RPCs [4]. Units can be made as small as needed and large arrays mass-produced, which is why MRPC is the first choice for many next-generation TOF systems.
- An MRPC TOF with time resolution below **100 ps** would extend STAR's [5] 3σ separation power for **π/K** and **K/p** from the present **0.65** and **1.3 GeV/c** to **1.6** and **2.6 GeV/c**, respectively, useful for the quark–gluon plasma search.
- The 6-gap MRPC has **~65 ps** and fits STAR's physics needs and space constraints. The 10-gap chamber reaches **55 ps**.

## Acknowledgements (summary)

Supported by the National Science Foundation of China (grants 10045004, 10075045, 10155002). Thanks to the CERN ALICE-TOF group and Rice University (especially Dr. Crispin Williams), which made the short beam-time tests possible, and to Prof. H. Huang (UCLA).

---

## Checks

**(a) MRPC module geometry.**
- 6-gap: 7 glass plates = 2 outer × **1.2 mm** + 5 inner × **0.70 mm**, **6 gaps × 250 μm** (nylon fiber). Glass: Shanghai glass, bulk resistivity **2.57 × 10¹³ Ω cm** (0.7 mm) and **1.8 × 10¹³ Ω cm** (1.2 mm) at 16 °C. Electrodes: carbon film **8 × 10⁵ Ω/□** on the outer glass, mylar insulation, readout pads on PCBs (1.5 mm), 6 mm honeycomb outside. Outer glass 21.6 × 8.9 cm², inner glass 19.8 × 6.8 cm² (text swaps these; figure is right). Electrode 208 × 80 mm. PCBs: upper 102 mm wide, bottom 126 mm wide, 216 mm long. Active area **20 × 6.3 cm²** (pad region 195 × 65 mm from the figure).
- 10-gap: two 5-gap stacks, each 2 × **1.1 mm** outer + 4 × **0.6 mm** inner glass, **0.22 mm** gaps; HV − on the two outer electrodes, + on the shared middle electrode. Outer glass 208 × 85 mm, inner glass 198 × 68 mm, electrode 204 × 80 mm, PCB & mylar length 214 mm, outer PCBs 102 mm and middle PCB 126 mm wide. Glass resistivity for 10-gap not given.
- Gas: 90% C₂H₂F₄ / 5% SF₆ / 5% iso-C₄H₁₀ at 1 atm.

**(b) Readout pads.** **12 pads in a 2 × 6 array** per chamber; pad **3.1 × 3.0 cm²** (31 mm across the module width, 2 pads; 30 mm along the module length, 6 pads); **3 mm** gap between pads. Same pad layout in the 10-gap chamber (Fig. 2). **Orientation in STAR is not stated** (the paper only uses test-beam X/Z axes and does not say which maps to STAR z or φ). **Single- vs double-ended: not stated**; each pad is one "output unit" with signal traces leaving at one side of the module ("signal trace area" in Figs. 1b/2b). The paper does not say whether signals are read differentially between anode and cathode pads.
- **[note]** Pad size/√12: 31 mm/√12 = **8.95 mm**; 30 mm/√12 = **8.66 mm** (pitch 33 mm/√12 = 9.53 mm; 34 mm pitch across the width/√12 = 9.81 mm).

**(c) Hit position.** The MRPC gives only the pad (cell) hit. All positions in the scans come from the **external MWPC telescope** (3 pairs, 4 mm wire spacing, **0.3 mm** resolution). No MRPC position resolution, no sub-pad interpolation, **no signal propagation speed**. Pad-size discussion is limited to the inter-pad edge effects (6-gap: ~80% efficiency, ~100 ps in the gap; 10-gap: worse timing near strip edges from charge sharing). The intro's 6.3 × 3.1 cm² PMT-unit size sets the STAR granularity requirement.

**(d) Performance.**
- 6-gap: efficiency > 97% plateau **15.5–17.0 kV**; time resolution **~65 ps** (Fig. 5 σ = 66.2 ps raw); time walk slope −30.36 ± 1.18 ps/kV; dark current < 5 nA per electrode at 15 kV; scans at ±7.875 kV (X) and ±8.25 kV (Z).
- 10-gap: efficiency **98%** at 22.5 kV, > 99% within ±10 mm of centre; time resolution **54 ps** at 23.5 kV (working point), ~50 ps near centre, best 40 ps, ~55 ps overall incl. electronics jitter (Fig. 10 σ = 57.7 ps raw); streamers begin at 25.0 kV.
- Rate: beam **< 100 Hz/cm²**; no rate-dependence or occupancy study.
- Cross-talk: only qualitative (charge sharing between neighbouring strips at the edge worsens timing); no cross-talk fraction quoted.
- Field ≈ 105–107 kV/cm in both chambers ([note]).

**(e) Electronics.** Essentially not described. Known from the paper: a TDC with **50 ps/channel** binning (from the Fig. 5/10 axis), an amplitude measurement (implied by the slewing correction; ADC not named), start from 4 PMTs on two crossed scintillators (**30 ps**), a single-readout MRPC as trigger, and MWPC tracking. No preamplifier/discriminator, TDC model or front-end board is named. **[note]** The thanks to the CERN ALICE-TOF group and Rice suggests the test used their beam-test infrastructure, but the paper does not say so.

## References (hardware-relevant)

- [1] M.C.S. Williams, E. Cerron, et al., Nucl. Instr. and Meth. A 434 (1999) 362. (MRPC technique)
- [2] M. Spegel, Nucl. Instr. and Meth. A 453 (2000) 308. (MRPC technique)
- [3] Li Cheng, Wu Jian, et al., HEP & NP 25 (2001) 933 (in Chinese). (USTC single-cell MRPC, preliminary results)
- [4] E. Gorini, et al., Nucl. Instr. and Meth. A 396 (1997) 93. (RPC timing comparison)
- [5] Letter of Intent, RICE-TOF Group, Proposal for a single tray of MRPC-TOF for STAR, 2001-6.
