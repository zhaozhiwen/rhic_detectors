---
title: "Wang 2024 — STAR forward detector upgrade status and performance (full-content paraphrase)"
type: raw-source
source_type: paper
authors: "Zhen Wang (Shandong University) for the STAR Collaboration"
journal: "EPJ Web of Conferences 296, 16003 (2024) — Quark Matter 2023 proceedings"
doi: 10.1051/epjconf/202429616003
arxiv: none
captured_via: "Route 3 — publisher PDF (no full-text HTML, no arXiv version); text from pdftotext -layout, figures extracted with pdfimages"
captured_date: 2026-11-06
captured_as: full-content paraphrase
figures: "3 (vision descriptions added 2026-11-06)"
vision_model: "general-purpose subagent (session model, not recorded), 2026-11-06"
---

# STAR forward detector upgrade status and performance (Wang, QM2023 proceedings, 2024)

- **Citation:** Zhen Wang (Shandong University) for the STAR Collaboration, "STAR forward detector upgrade status and performance", Quark Matter 2023 (30th Int. Conf. on Ultra-Relativistic Nucleus-Nucleus Collisions), section Spin/EIC Physics. 4 pages, published online 26 June 2024.
- **Journal ref + DOI:** EPJ Web of Conferences **296**, 16003 (2024); doi:[10.1051/epjconf/202429616003](https://doi.org/10.1051/epjconf/202429616003). Open access, CC BY 4.0. Title, author, affiliation and DOI confirmed on the publisher abstract page and in the PDF metadata. The author is **Zhen** Wang (wang.zhen@sdu.edu.cn).
- **arXiv:** none found. arXiv title searches ("STAR forward detector upgrade status and performance", "forward detector upgrade STAR") return nothing. An all-fields search for "STAR forward upgrade Wang" finds only the related, separate paper on the STAR FST, arXiv:2407.09952 (Brandenburg et al.).
- **Route used:** route 3 (PDF). The epj-conferences.org article page offers only Abstract / PDF / References; this proceedings has no full-text HTML version (route 1 not available), and with no arXiv version route 2 was not available either. The text below is from the publisher PDF (`pdftotext -layout`), with the rendered pages checked by eye.
- **PDF backup:** `assets/wang2024-star-forward-upgrade/source.pdf` (791,458 bytes, 4 pages; publisher PDF, downloaded 2026-11-06).
- **Figures:** the 3 figures are raster images embedded in the PDF (1536 px wide, 300 ppi). They were extracted with `pdfimages`, with their alpha masks flattened onto white, and saved as `assets/wang2024-star-forward-upgrade/fig1.png` to `fig3.png`. Each was checked by eye against the page.
- **Verification:** every number in this note was checked against `pdftotext -layout` of the publisher PDF. The paper has **no equations and no tables**. The only text-layer quirk: the title is stored twice in the text layer (lower case and Title Case, overlapping); the rendered page shows the lower-case title, as on the publisher page.
- **Related material (not the paper):** the QM2023 talk slides (23 slides; supplied by the repo author, not ingested in this repo). Numbers from them are used only in **[note]** items and are labelled "from the talk slides". [[ruan2026-fcs-specs-email-note]] (FCS construction specs from Lijuan Ruan) is used for comparison only.
- Figure descriptions were added by a separate figure pass that looked at the images.

---

## Full content

### Abstract

STAR finished a forward-rapidity upgrade before RHIC Run 2022. It has two parts:
- the **Forward Tracking System (FTS)**: a Silicon Tracker plus a small-strip Thin Gap Chamber (sTGC) Tracker;
- the **Forward Calorimeter System (FCS)**: an Electromagnetic Calorimeter (ECal) plus a Hadronic Calorimeter (HCal).

Together they cover **2.5 < η < 4** and detect neutral pions, photons, electrons, jets and charged hadrons. Physics aims:
- cold QCD at very high and very low Bjorken x;
- the longitudinal structure of the initial state in heavy-ion collisions, studied through decorrelations at large η.

The proceedings describes the upgrade, its status and its performance in STAR Run22.

### 1 Introduction

The main goal of the forward upgrade is cold-QCD physics at very high and very low Bjorken x: it extends STAR's reach to **x < 2×10⁻³** and **x > 0.3**. The upgrade also serves hot-QCD topics: the longitudinal structure of the initial state, and the temperature dependence of the transport properties of the matter made in heavy-ion collisions [1].

The two subsystems are the FTS (Silicon Tracker + sTGC Tracker) and the FCS (ECal + HCal). Both sit on the side of STAR that **faces the blue beam** and both cover **2.5 < η < 4**. Installation was **completed in 2021**, and the upgrade has been part of the trigger and data-taking system **since 2022**. Fig. 1 shows a sketch of STAR with the forward upgrade.

### 2 Forward Tracking System

The FTS has two subsystems: the **Forward Silicon Tracker (FST)** and the **Forward sTGC Tracker (FTT)**. Together they give **7 points** for reconstructing a forward track over η = 2.5–4.

![Fig. 1](assets/wang2024-star-forward-upgrade/fig1.png)

**Fig. 1.** Sketch of STAR with the forward upgrade, drawn in Blender from the real STAR detector geometry. The labelled components, left to right, are FST, FTT, ECal and HCal.

*Figure description (from the image):* Single 3D cut-away rendering; no axes and no numbers. Printed labels: "FST", "FTT", "ECal", "HCal", and "FCS" above the two calorimeters. The beam pipe runs from the lower left (inside the cut-open STAR, drawn as unlabelled red and purple structures) out to the right. FST: 3 disks with blue/green modules on a grey conical support around the beam pipe. FTT: 4 blue polygonal planes just outside the opening of the red structure. FCS: ECal in front, HCal behind it; each is drawn as two separate blocks (halves), one on each side of the beam pipe, on a grey support stand. An unlabelled cluster of yellow cylinders sits on the beam pipe in front of the ECal. Main feature: the order along the beam, FST, FTT, ECal, HCal, matching the caption.

**FST.**
- 3 identical disks inside the STAR TPC [2], at **z = 152 cm to 179 cm** from the interaction point.
- 12 identical modules per disk, each fine-grained in φ and coarse-grained in R.
- To save cost, the FST reuses the electronics, DAQ and cooling of the earlier STAR Intermediate Silicon Tracker (IST) [3].
- Readout chips: "AVP25-S1" (see the [source issue] below).
- Bias voltage during data taking: **140 V** for the inner sensors and **160 V** for the outer sensors.

**FTT (forward small-strip Thin Gap Chamber tracker).**
- 4 identical planes, each made of 4 pentagon-shaped gaseous detector modules [4].
- Planes at **z = 300 cm to 360 cm** from the interaction point, inside the opening of the magnet pole tip.
- Each module has two sTGCs, with one X, one Y and two diagonal readout layers, used to reconstruct the hit position.
- Gas: **45% n-pentane + 55% CO₂**.
- Readout: VMM electronics following the ATLAS design [5, 6].
- High voltage during data taking: **2900 V**.

**Track reconstruction.** A first software framework for forward tracking is in place and is being optimised and tested on real and simulated data.
- The FST gives up to 3 points and the FTT up to 4 points.
- A Cellular Automaton (CA) algorithm finds tracks within each detector: points on the FTT (or on the FST) are first fitted together to form candidate track segments.
- These segments are the seeds for the full fit, which adds points from the other detector to find the final track.
- The collision vertex from the TPC constrains the tracks. If there is no TPC vertex, or the vertex fit fails for the forward track, the beamline can be used as the constraint instead.

**Track–calorimeter matching.** Matching forward tracks to calorimeter hits tests the tracking performance. Fig. 2 shows ΔX and ΔY between forward-track projections and HCal hits, for all (random) track–hit combinations.
- Both distributions show a clear peak near zero, which means tracking and calorimeter match well.
- The ΔX distribution has two extra peaks at **±60 cm**. The paper attributes them to the HCal being made of two independent modules in X.

![Fig. 2](assets/wang2024-star-forward-upgrade/fig2.png)

**Fig. 2.** ΔX (left) and ΔY (right) between forward-track projections and HCal hits, for random track–hit combinations, in Run22 p+p data (the panel titles say p+p 510 GeV).

*Figure description (from the image):* Two side-by-side filled (teal) 1D histograms, each titled "Run 22 p+p 510 GeV Data". A legend above them shows a black square = "FCS hit" and a red dot = "Track projection"; each panel has an inset sketch of two blue rectangles (the two HCal halves) with a red dot and a black square, plus an arrow labelled "X" (left) or "Y" (right). Left: x = "ΔX (trk − HCal) (cm)", −200 to 200 (labels every 50); y = "Counts", labels 0 to 1400 every 200. A narrow peak at ΔX ≈ 0 reaches ≈1460 counts; two broad side bumps of ≈480–490 counts sit near ΔX ≈ −60 and ≈ +60 cm, on a wide base that falls to ≈20 counts at ±200 cm. Right: x = "ΔY (trk − HCal) (cm)", −200 to 200; y = "Counts", labels 0 to 1400. A single narrow peak just above ΔY = 0 (≈ +3 cm) reaches ≈1520 counts, on a broad, roughly symmetric base (shoulders of ≈550 counts near −20 and +35 cm); there are no side peaks. Only the axis labels are printed; values marked ≈ are read off the plots.

**[note]** The image agrees with the text: clear peaks at ΔX ≈ 0 and ΔY ≈ 0, and side bumps in ΔX only, at about ±60 cm.

### 3 Forward Calorimeter System

The FCS has an ECal and an HCal and sits about **7 m** from the interaction point.
- **ECal:** refurbished PHENIX lead–scintillator calorimeter [7], **1496 channels**.
- **HCal:** iron–scintillator sandwich sampling calorimeter, **520 channels**.
- **Readout:** SiPM-based readout electronics on the front face, developed together with the EIC R&D group.

**Radiation monitoring.** An LED system built into the FCS monitors radiation damage to the SiPMs: the leakage current measured in LED runs is used to assess and qualify the damage. For most SiPMs the damage stayed within expectations. The attenuator and SiPM bias voltage on the front-end boards were adjusted regularly to make up for the gain lost to radiation damage.

**ECal calibration.**
- The ECal is calibrated from the reconstructed π⁰ invariant mass. A gain correction factor for each channel comes from iterating the mass reconstruction.
- Fig. 3 (right) shows the mass distribution after calibration. After **two iterations**, every ECal channel reconstructs π⁰ well.
- Fig. 3 (left and middle) shows, channel by channel, how far the reconstructed π⁰ mass is from the PDG value. The z (colour) axis gives each channel's fit status; red means a deviation **below 10%**.

**HCal calibration.** The HCal will be calibrated with MIPs; this work is in progress.

![Fig. 3](assets/wang2024-star-forward-upgrade/fig3.png)

**Fig. 3.** Left and middle: ECal channel status before and after the iteration. Red means the reconstructed mass peak is close to the π⁰ mass; other colours mean the peak is away from it or the fit failed. Right: reconstructed invariant-mass distribution for one ECal channel.

*Figure description (from the image):* Three panels. Left and middle: 2D channel maps under one shared heading, "Channel status"; x = "Column" (labels 2–22; 22 columns), y = "Row" (labels 0 to −30; 34 rows, down to about −33). The colour scale runs from red (top) through orange, yellow, green and cyan to blue/purple (bottom). Only the middle panel's colour bar is labelled: "10%" near the top, "40%" at the green, "fit failed" at the purple bottom. The two maps carry no "before"/"after" labels. Left map: mostly red, with many yellow cells (about a quarter of the 748 cells by pixel sampling), clustered in the bottom rows and in scattered patches, plus a few green and blue/purple cells, mostly in the bottom row and the rightmost column. Middle map: almost all red; about 20 non-red cells, nearly all in the rightmost column (yellow, green, blue/purple), plus the corners and one yellow cell in the top row near column 8. Text under the maps: "Red: Mass peak very close to π0 mass" and "Other Color: Mass peak away from π0 mass". Right: unfilled 1D histogram titled "Invariant mass plot for FCS ECal"; x = "Invariant mass [GeV/c²]", 0 to 0.4 (labels every 0.05); y = "counts", labels 0, 10000, …, 60000, and a top label whose first digit is hidden behind the axis title (70000 from the even spacing). The peak is at ≈0.135 GeV/c² and reaches ≈69 000 counts; a red vertical line labelled "M_π0^PDG" sits at the peak. The histogram rises from ≈0 near 0.01 GeV/c², and a long high-mass tail falls from ≈26 000 at 0.2 to ≈17 000 at 0.4 GeV/c². Values marked ≈ are read off the plot.

**[source issue]** The caption says the right panel is "one ECal channel", but its title is "Invariant mass plot for FCS ECal" and no channel number is shown. This confirms the issue raised in the Remarks. One correction to that remark: the peak holds about 7×10⁴ counts, not about 2×10⁴. The "20000" label sits far below the peak, and the top label (70000) is partly hidden. About 7×10⁴ counts in the peak makes a sum over channels even more likely. The image alone cannot prove it.

**[note]** The caption's "before and after the iteration" is not printed on the maps; reading left = before and middle = after is the paper's ordering. The middle map is not all red: about 20 cells, nearly all in the rightmost column, are yellow, green or blue/purple (fit failed). So "every ECal channel reconstructs π⁰ well" (§3) is stronger than the image shows; the Checks section's "a few edge channels still off or failing the fit" matches it.

### 4 Summary

- All STAR forward-upgrade detectors are fully installed, commissioned and part of data taking.
- The upgrade performed as expected, and data taking ran smoothly in **Run22 and Run23**.
- The forward-tracking algorithm is in place; the software group is testing and optimising it on Run22 p+p data.
- ECal calibration is finished; HCal calibration is ongoing.

### Acknowledgements

Supported by NSFC (Grants 12075139 and 12075140), MOST China (Grant 2020YFE0202001) and the Shandong Provincial Natural Science Foundation (Grant ZR2022JQ03).

---

## Remarks, cross-checks and source issues

- **[source issue]** In §2 the FST readout chip is printed "AVP25-S1". This is almost certainly the **APV25-S1** chip used by the STAR IST, whose electronics the FST reuses. The talk slides also write "APV25".
- **[source issue]** The Fig. 3 caption says the right panel is the mass distribution of *one ECal channel*. The panel title reads "Invariant mass plot for FCS ECal", and the peak bin holds about 7×10⁴ counts (corrected by the figure pass; first read as about 2×10⁴), which looks more like a sum over many channels. It cannot be settled from the paper.
- **[note]** Abstract and §1 differ slightly on timing: the abstract says the upgrade was completed "before RHIC Run 2022"; §1 says installation finished in 2021, with data taking from 2022. These agree. The talk slides add that FCS construction was completed in early 2021.
- **[note]** Point count ✓: 3 FST disks + 4 FTT planes = 7 points, matching "7 points". FTT module count: 4 planes × 4 modules = 16 modules, with 2 chambers each.
- **[note]** Plane positions from the talk slides:
  - FST disks at **152, 165 and 179 cm**, consistent with the paper's 152–179 cm ✓.
  - FTT disks at **307, 325, 343 and 361 cm**. The paper's "300 cm to 360 cm" is a rounded range; the last disk (361 cm) is just past 360 cm.
- **[note]** FST acceptance recomputed with the module radii from the talk slides (inner region 5 < R < 16.5 cm, outer region 16.5 < R < 28 cm):
  - R = 28 cm gives η = 2.39 at z = 152 cm and η = 2.55 at z = 179 cm;
  - R = 5 cm gives η = 4.11 at z = 152 cm and η = 4.27 at z = 179 cm.

  So the FST spans roughly 2.4–4.3, consistent with the quoted 2.5 < η < 4 ✓.
- **[note]** Channel counts ✓:
  - ECal: 1496 = 2 halves × 22 columns × 34 rows (748 per half). Fig. 3 (left and middle) shows a 22-column × 34-row map, so one ECal half.
  - HCal: 520 = 2 × 13 × 20 (260 per half), using the geometry in [[ruan2026-fcs-specs-email-note]].
- **[note]** The ±60 cm side peaks in ΔX (Fig. 2) are about half the width of one HCal half: 13 × 9.99 cm = 129.9 cm, from [[ruan2026-fcs-specs-email-note]]. The paper gives only a qualitative reason (the two independent HCal modules in X).
- **[note]** Readout location: the paper puts the SiPM readout electronics "on the front face". [[ruan2026-fcs-specs-email-note]] says, for the ECal, that the WLS fibres are "read out at the back". These sources cannot resolve which end the SiPM boards sit on. Check against an FCS NIM or design document.

### Comparison with [[ruan2026-fcs-specs-email-note]] (and the talk slides)

| Quantity | This paper | Talk slides (QM2023) | ruan2026-fcs-specs-email | Agreement |
|---|---|---|---|---|
| Location | "about 7 m" from IP | 7 m from IP, on the "FMS platform" | ECal front z = 710.16 cm; HCal front z = 782.63 cm | ✓ |
| η coverage | 2.5 < η < 4 | 2.5 < η < 4 | "roughly 2.2 < eta < 4.3" | consistent (email's range is the outer geometric edge; see below) |
| ECal technology | refurbished PHENIX Pb–scintillator | PHENIX Pb–Sc; 66 cells of 1.5 mm Pb / 4 mm Sc; 36 WLS fibres per cell | Pb/scint shashlik, 65 × 1.5 mm Pb, 66 × 4.0 mm scint, WLS fibre | ✓ |
| ECal channels | 1496 | 1496 | 1496 (2 × 22 × 34) | ✓ |
| ECal tower size | — | 5.52 × 5.52 × 33 cm³ | 5.542 × 5.542 cm face, 37.73 cm deep | face ≈ (5.52 vs 5.542 cm); **depth differs (33 vs 37.73 cm)** |
| ECal depth | — | 18 X₀; 0.85 λ_I | 18.1 X₀; 0.93 λ | X₀ ✓; **λ differs (0.85 vs 0.93)** |
| HCal technology | Fe–scintillator sandwich | Fe/Sc (20 mm / 3 mm) | 36 × (20 mm steel + 3 mm scint), WLS plate | ✓ |
| HCal channels | 520 | 520 | 520 (2 × 13 × 20) | ✓ |
| HCal tower size | — | 10 × 10 × 84 cm³ | 9.99 × 9.99 cm face, 84.24 cm deep (+10 mm back plate) | ✓ |
| Readout | SiPM, front face, with EIC R&D | SiPMs, used in trigger; same SiPM readout for ECal and HCal | SiPM | ✓ (location: see [note] above) |
| Halves | HCal: "two independent modules in X" | "2 movable halves inside and outside of ring" | North and South halves | ✓ |

- **[note]** ECal depth: the talk's 33 cm is shorter than the 37.73 cm stack depth computed in [[ruan2026-fcs-specs-email-note]] (66 × 4.24 mm + 65 × 1.50 mm). The 33 cm may be a rounded or differently defined length; neither source explains it.
- **[note]** ECal λ_I recomputed from the email's layer stack, using PDG λ_I of 17.59 cm for Pb and 77.07 cm for polystyrene: 9.75/17.59 + 26.4/77.07 = 0.55 + 0.34 = **0.90 λ_I**. This sits between the talk's 0.85 and the email's 0.93. The same stack gives 9.75/0.561 + 26.4/41.31 = **18.0 X₀** ✓ (slides 18; email 18.1).
- **[note]** Geometric acceptance from the email's numbers, ignoring the unknown gap at the beam pipe: one ECal half is 22 × 5.542 = 121.9 cm wide and 34 × 5.542 = 188.4 cm tall.
  - At z = 710.16 cm the outer edge (x = 121.9 cm) is at η = 2.46, and the outer corner at η = 2.23.
  - The HCal outer corner (129.9 cm × 99.9 cm at z = 782.63 cm) is at η = 2.27.

  So the email's "2.2" is the outer geometric corner, while the 2.5 lower edge in the paper and slides is roughly the full-azimuth edge ✓.

---

## Checks

**(a) Components and coverage.** Everything is on the STAR west side, facing the RHIC blue beam, over 2.5 < η < 4:
- **FST:** 3 silicon disks inside the TPC at z = 152–179 cm (slides: 152, 165, 179 cm), 12 modules per disk, fine φ and coarse R granularity.
- **FTT (sTGC):** 4 planes of 4 pentagon modules at z = 300–360 cm (slides: 307, 325, 343, 361 cm), inside the magnet pole-tip opening.
- **FCS:** about 7 m from the IP. ECal front at z = 710.16 cm and HCal front at z = 782.63 cm, per [[ruan2026-fcs-specs-email-note]].
- The FTS gives up to 7 points per track (3 FST + 4 FTT).

**(b) FCS design.**
- **ECal:** refurbished PHENIX Pb–scintillator calorimeter, 1496 channels. From the talk slides: 5.52 × 5.52 × 33 cm³ towers; 66 cells of 1.5 mm Pb / 4 mm scintillator; 36 WLS fibres per cell; 18 X₀ and 0.85 λ_I; PMTs replaced by SiPMs.
- **HCal:** Fe–scintillator sandwich, 520 channels. From the talk slides: 20 mm Fe / 3 mm scintillator; 10 × 10 × 84 cm³ towers.
- **Readout:** SiPM-based front-end electronics "on the front face", developed with the EIC R&D group, with attenuator and bias adjustable on the front-end board. The paper itself gives no tower dimensions or depths.
- **Match with [[ruan2026-fcs-specs-email-note]]:** channel counts (1496 = 2 × 22 × 34; 520 = 2 × 13 × 20), layer structure, HCal tower size and depth, and 18 X₀ all agree. Differences: ECal tower depth (slides 33 cm vs email 37.73 cm), ECal λ (0.85 vs 0.93; my recomputation gives 0.90), and readout end ("front face" in the paper vs WLS fibres "read out at the back" in the email). See the comparison table.

**(c) Performance.**
- **Energy resolution:** no number is given, for either calorimeter.
- **ECal calibration:** π⁰ invariant-mass reconstruction, iterated for per-channel gain factors. After 2 iterations all channels reconstruct the π⁰ mass to within 10% (red in Fig. 3); Fig. 3 (left/middle) shows a few edge channels still off or failing the fit.
- **HCal calibration:** with MIPs, still ongoing at the time of writing.
- **Tracking:** CA-based segment finding in FST and FTT, combined fit, and a TPC-vertex or beamline constraint. Forward-track to HCal matching shows a clear peak at ΔX, ΔY ≈ 0 in Run22 p+p 510 GeV data (Fig. 2). The talk slides quote δp_T/p_T ~ 20–30% for 0.2 < p_T < 2 GeV/c as the design goal; the paper gives no momentum-resolution result.
- **Jets, electrons, photons:** listed only as capabilities, with no reconstruction results.
- **Trigger:** the paper says only that the upgrade has been part of the trigger and data-taking system since 2022; the talk slides add that the FCS SiPM readout is used in the trigger and that the trigger system was commissioned. No trigger rates or thresholds are given.

**(d) Status and run history.**
- Installation was completed in 2021 (FCS construction finished in early 2021, per the talk slides).
- Data taking began in Run22: p+p at √s = 510 GeV (the Fig. 2 data).
- Data taking ran smoothly in Run22 and Run23; the talk slides list Run23 as Au+Au 200 GeV.
- From the talk slides, planned runs: p+p and p+Au at 200 GeV in 2024, and Au+Au 200 GeV in 2025.

**(e) Rates, radiation damage and SiPM issues.**
- **Rates:** no numbers.
- **SiPM radiation damage:** tracked with the LED system through the leakage current measured in LED runs. For most SiPMs the damage was within expectations. Gain loss was offset by regularly adjusting the front-end attenuator and the SiPM bias voltage.
- **From the talk slides:** leakage current rose sharply towards the end of Run22, and towers closer to the beam pipe had more radiation damage.
- **Tracker running conditions:** FST bias 140 V (inner) / 160 V (outer). The talk slides say some APV chips were missing and a few sensors ran at lower bias. FTT at 2900 V (1500 V standby, per the talk slides).

---

## References (hardware-relevant)

- [1] STAR Note SN0648, "The STAR Forward Calorimeter System and Forward Tracking System beyond BES-II" (2016), https://drupal.star.bnl.gov/STAR/starnotes/public/sn0648 (forward-upgrade proposal).
- [2] M. Anderson et al., Nucl. Instrum. Meth. A 499, 659 (2003), nucl-ex/0301015 (STAR TPC).
- [3] B. Buck et al., arXiv:1404.0993 (2014) (STAR Intermediate Silicon Tracker; source of the FST electronics, DAQ and cooling).
- [4] Y. Shi, C. Yang, Q. Yang (STAR), JINST 15, C09021 (2020) (STAR forward sTGC).
- [5] X. Wang, L. Guan, S. Sun, B. Zhou, J. Zhu, G. Jin, Nucl. Instrum. Meth. A 1028, 166326 (2022) (VMM-based sTGC readout).
- [6] G. Sekhniaidze, JINST 12, C03020 (2017) (VMM / ATLAS NSW electronics).
- [7] L. Aphecetche et al. (PHENIX), Nucl. Instrum. Meth. A 499, 521 (2003) (PHENIX EMCal; origin of the FCS ECal modules).
- Related, not cited in the paper: J. D. Brandenburg et al., "The STAR Forward Silicon Tracker", arXiv:2407.09952.
