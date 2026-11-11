---
title: "Yang 2014 — Calibration and performance of the STAR Muon Telescope Detector using cosmic rays (full-content paraphrase)"
type: raw-source
source_type: paper
authors: "C. Yang et al., 38 authors"
journal: "Nucl. Instrum. Meth. A 762 (2014) 1–6"
doi: 10.1016/j.nima.2014.05.075
arxiv: "1402.1078"
captured_via: "Route 1 — publisher HTML (ScienceDirect, institutional full-text access in the user's Chrome); MathML transcribed to LaTeX; checked against the publisher PDF"
captured_date: 2026-11-05
captured_as: full-content paraphrase
figures: "10 (vision descriptions added 2026-11-05)"
vision_model: "general-purpose subagent (session model, not recorded), 2026-11-05"
---

# Calibration and performance of the STAR Muon Telescope Detector using cosmic rays

- **Citation:** C. Yang, X.J. Huang (corresponding author), C.M. Du, B.C. Huang, et al. (38 authors in total; BNL, USTC, Tsinghua, IMP Lanzhou, Rice, UC Davis, UT Austin, VECC Kolkata, Texas A&M), "Calibration and performance of the STAR Muon Telescope Detector using cosmic rays"
- **Journal:** Nucl. Instrum. Meth. A 762 (2014) 1–6, doi:[10.1016/j.nima.2014.05.075](https://doi.org/10.1016/j.nima.2014.05.075). Received 20 Feb 2014, revised 5 May 2014, accepted 6 May 2014, online 27 May 2014.
- **arXiv:** 1402.1078 [physics.ins-det] (v1, 5 Feb 2014)
- **Keywords (paper):** Muon telescope detector; Cosmic ray; Timing resolution; Spatial resolution
- **Route used:** route 1 — publisher HTML (ScienceDirect) via the user's Chrome (JLab full-text access). MathJax v4 source MathML was read from the page and transcribed to LaTeX.
- **PDF backup:** `assets/yang2014-mtd-cosmic-calibration/source.pdf` (publisher). The arXiv v1 PDF used for the cross-checks was not kept (publisher version kept).
- **Verification:** every number, unit, cut, equation and both tables were checked against `pdftotext -layout` of the publisher PDF; the critical items (Δφ cut, −1.26 T, t_Steel field, Fig. 9 caption) were also checked in the arXiv PDF text. No substantive HTML-vs-PDF disagreement was found (see Checks). Fit-box values quoted for Figs. 7, 8, 10 are read from the PDF text layer of the figures. Figure descriptions were added by a separate figure pass that looked at the images (`assets/yang2014-mtd-cosmic-calibration/fig1–10.jpg`; fit-box numbers re-read from the images).
- **Figures:** `assets/yang2014-mtd-cosmic-calibration/fig1.jpg … fig10.jpg` (publisher full resolution). Order checked against the HTML: gr1 = Fig. 1 … gr10 = Fig. 10; the image shapes match the panel layouts of the captions.

The paper has no numbered equations; the relations written inline in the text are set below as display equations, labelled by section, not by a paper number.

---

## Abstract

The paper gives the timing and spatial resolution of the Muon Telescope Detector (MTD) installed in STAR at RHIC. Cosmic-ray muons crossing STAR have an average transverse momentum of 6 GeV/c; their multiple scattering is small, which makes them a good tool for calibration and resolution measurements. The results are ~100 ps (timing) and ~1–2 cm (spatial), in line with earlier cosmic-ray bench tests and test beams.

---

## 1. Introduction

- **Physics motivation.** RHIC data over the previous decade show a hot, dense medium with partonic degrees of freedom (QGP). A goal for the next decade is to measure its temperature, density profile and colour-screening length with electromagnetic probes such as di-leptons [1–9]. Muons suffer less bremsstrahlung in detector material than electrons, so they can be measured more precisely; this is needed to separate the ϒ(1S) from the excited states (2S+3S), which are predicted to melt at very different temperatures.
- The STAR MTD is to measure ϒ and J/ψ through di-muon decays over a broad p_T range (colour-screening studies), and μ–e correlations to separate heavy-flavour correlations from initial lepton-pair production [10]; i.e. direct information on the temperature and colour screening in the QGP.
- **Technology.** Multi-gap Resistive Plate Chambers (MRPC), as in the STAR TOF system [11,12]. Unlike the TOF MRPCs [13], the MTD MRPCs are much larger and have **long, double-ended read-out strips**.
- **Placement and acceptance.** Behind the iron return bars of the STAR magnet; **45% of the full azimuth** within **$|\eta|<0.5$**. Construction/installation began in 2011, to be completed in 2014.
- **Prototype history.**
  - Prototypes built and studied 2007–2011: laboratory cosmic rays, test beams, and in STAR during RHIC runs. Cosmic and beam tests gave timing **$\le 100\,\mathrm{ps}$** and spatial resolution **~1 cm**, sufficient for the physics goals [14].
  - STAR operation 2007–2008 showed that clean muon identification is possible for muon p_T above a few GeV/c; bench, test-beam and simulation results indicated the MTD would deliver quarkonium and primordial di-lepton physics [15].
  - But in STAR in 2007–2008 the timing resolution was only **200–300 ps**, much worse than in the bench/beam tests, because of the digitization electronics then used [16] and the long cables between detectors and digitizers.
  - **2009:** new prototypes installed; the simple on-board front-end electronics previously used [17] to drive long cables were replaced by the STAR TOF electronics [12,18], based on the CERN **HPTDC** chip [19].
  - **2010:** a cosmic-ray trigger based on the MTD prototypes was implemented in the STAR trigger. High-energy (~6 GeV) cosmic rays suit resolution studies because multiple-scattering smearing is relatively small.
- **Scope of the paper.** Timing and spatial resolution of MTD MRPCs read out with STAR TOF electronics, for cosmic muons reconstructed in STAR in 2010–2011, plus the performance of **10% of the full MTD** operated during the 2012 RHIC run. Layout: Sec. 2 MRPCs; Sec. 3 experimental aspects; Sec. 4 analysis and performance; Sec. 5 summary.

---

## 2. MTD MRPC modules

- Several MRPC designs were studied: single- and double-stack, with five or six gas gaps, and several read-out pad geometries. During the 2007–2011 runs some prototypes were installed in STAR near mid-rapidity at a radius of **~400 cm**, integrated into STAR DAQ and trigger, and took data for full runs. Performance events were recorded with a trigger requiring a hit in at least one read-out strip.
- Modules are housed in gas-tight aluminium boxes called **"trays"**.
- **Type A:** double-stack, **10 gas gaps**, **6 read-out strips**, outer dimensions **87 × 17 cm²**; double-ended read-out pads **2.5 cm wide** with **0.4 cm gaps** between pads.
- **Type B (C):** single-stack, **5 (6) gas gaps of 250 μm**, **12 read-out strips**, read out at both ends; module size **87 × 52 cm²**; pads **3.8 cm wide** with **0.6 cm gaps**.
- Run 11 (2011): one type B and two type C MRPCs installed. **Type B** (Fig. 1) was chosen as the **final design** for the full MTD; **12** final-design modules were installed and operated in **Run 12**.

**Table 1.** The design parameters for the MTD MRPCs operated in STAR during the 2007–2012 RHIC runs.

| Conditions | Type | Trays |
|---|---|---|
| Cosmic and test-beam | Type A | – |
| Run 7: Au+Au | Type A | 2 modules in 1 tray |
| Run 8: d+Au, p+p | | |
| Run 9: p+p | Type A | 3 modules in 1 tray |
| Run 10: Au+Au, cosmic trigger | | |
| Run 11: Au+Au, cosmic trigger | Type A | 3 A modules in 1 tray |
| | Type B | 1 B module in 1 tray |
| | Type C | 2 C modules in 2 trays |
| Run 12: p+p, cosmic trigger | Type B | 12 modules in 12 trays |

**[note]** Blank cells are as printed (HTML and PDF agree): Run 8 shares the Type A / 2-modules entry of Run 7, and Run 10 shares the Type A / 3-modules entry of Run 9. Despite its caption, the table lists only module type and tray count; the actual design parameters (gaps, strips, sizes, pad widths) are given only in the text above.

![Fig. 1](assets/yang2014-mtd-cosmic-calibration/fig1.jpg)

**Fig. 1.** Side view of a type B MRPC module: honeycomb in yellow, strips red, PC boards green, Mylar light yellow, glass sheets sky blue; vertical scale expanded for clarity.

*Figure description (from the image):* Single schematic cross-section (no axes), mirror-symmetric top/bottom. From the outside in on each side: honeycomb panel (yellow, hexagon pattern), a row of 12 red read-out strips, green PC board, thin light-yellow Mylar layer; in the centre 6 sky-blue glass sheets (2 longer outer sheets, 4 shorter inner sheets) separated by 5 white gas gaps. Dimension labels and what their arrows bracket: 580 mm = full width of the PC board (widest element of the drawing); 38 mm = one strip; 6 mm = gap between strips; 1.5 mm = PC-board thickness; 1.1 mm = outer glass sheet; 0.7 mm = inner glass sheet; 0.25 mm = gas gap; 0.15 mm = Mylar; 10 mm = honeycomb panel. Vertical scale not proportional (as the caption says).

**[note]** The drawing confirms the type-B text: 12 strips of 38 mm with 6 mm gaps and 5 gas gaps of 0.25 mm (6 glass sheets); it adds the glass thicknesses (1.1 mm outer, 0.7 mm inner), which the text does not give. The 580 mm overall width is the PC board and is larger than the 52 cm module size quoted in the text; the strip pattern alone (12 × 38 + 11 × 6 = 522 mm) matches 52 cm. The paper does not reconcile 580 mm with 52 cm.

**[note]** Dimension labels in the PDF figure's text layer: 580 mm, 38 mm, 6 mm, 1.5 mm, 1.1 mm, 0.7 mm, 0.25 mm, 0.15 mm, 10 mm. 38 mm / 6 mm match the 3.8 cm strip / 0.6 cm gap and 0.25 mm the gas gap; the others are assigned in the figure description above. Check: 12 × 3.8 cm + 11 × 0.6 cm = 52.2 cm ≈ the 52 cm module width ✓.

- **Gas:** **95% Freon R-134a + 5% isobutane**.
- **Electronics:** very similar to the STAR TOF system. They record absolute hit times relative to a **40 MHz** master clock with a least-significant-bit time of **24.4 ps**. **[note]** 25 ns / 2¹⁰ = 24.41 ps ✓.
- They also deliver analog multiplicity from each end of each MRPC module (an OR of all strips in the module) to the STAR **Level-0 trigger**, used to select events with MTD hits and to allow triggers on prompt hits only, which suppresses MTD backgrounds from hadronic showers in the magnet backlegs. Details in [12,18].

---

## 3. Experimental setup

### 3.1. The STAR detector

- **TPC** [20,21]: main tracker; **4 m long**, full azimuth, **$|\eta|<1$**. Ionization electrons drift to the nearest end. **24 super-sectors** (12 per end), each with **45 pad rows** along the radius, each divided into inner and outer sectors. Tracks curve in the **0.5 T** STAR field according to p_T; dE/dx from cluster charge gives PID [22–24].
- **TOF** [12]: fully installed before the 2010 run; full azimuth, **$|\eta|<0.9$**, radius **~220 cm**; extends PID to ~3 GeV/c for p and $\bar{p}$ [25].
- **BEMC** [26]: outside the TOF. TPC, TOF and BEMC sit inside the solenoid.
- **Magnet** [27]: cylindrical; **30 flux-return bars**, four end rings, two pole tips; return flux through the outer steel. The flux-return bars ("**backlegs**") are **6.85 m long**, **trapezoidal** in cross-section, and **57 cm thick at a radius of 363 cm**. Backlegs plus BEMC act as the hadron absorber, so mostly muons reach the MTD in both elementary and heavy-ion collisions.
- Outside the backlegs are the BEMC PMT/electronics boxes; the **MTD is mounted on the BEMC PMT boxes at ~400 cm**.

### 3.2. STAR cosmic ray trigger

- A central Au+Au simulation with realistic STAR geometry showed that most charged hadrons stop in the BEMC and backlegs; the few escaping particles (primary or secondary) mostly go through the gaps between backlegs [15].
- In collision data the mean p_T of muons reaching the MTD is **~2 GeV/c**. For 2 GeV/c muons, multiple scattering in the backlegs gives an MTD **spatial resolution of 10 cm** and a **timing resolution of 100 ps**. This makes the intrinsic MRPC resolution hard to measure with collision muons, and the large smearing causes random TPC–MTD matches, i.e. background for muon ID.
- **Cosmic trigger (2010 run):** wanted cosmic muons cross MTD, backlegs, BEMC, TOF and TPC, leaving long TPC tracks and two hits each in the MTD and TOF barrels. Since only a small MTD patch existed and the TOF was complete, the trigger was a coincidence of **one MTD hit and two TOF hits**.
- TPC hits of a muon are reconstructed into tracks with trajectory, momentum p and dE/dx. STAR reconstruction assumes particles come from the centre, so one cosmic muon crossing all of STAR becomes **two TPC tracks**.
- **Time definitions (Fig. 2):** $t_{\mathrm{TOF1}}$, $t_{\mathrm{TOF2}}$, $t_{\mathrm{MTD}}$ are the measured times at the two TOF hits and the MTD hit. $t_{\mathrm{TPC}}$ is the time of flight between the two TOF hits computed from the TPC path length and p. $t_{\mathrm{Steel}}$ is the time of flight from the MTD to the first TOF hit, derived from the track helix parameters, p, and **the 0.5 T magnetic field** (see Check b).

![Fig. 2](assets/yang2014-mtd-cosmic-calibration/fig2.jpg)

**Fig. 2.** Schematic of a cosmic-ray event in STAR.

*Figure description (from the image):* Single schematic, no axes (transverse view). Three concentric circles, not labelled with detector names. A curved track labelled "Cosmic Ray" (top right) crosses the outer circle at a star labelled tMTD, the middle circle at tTOF1, runs through the centre (segment labels "1" above and "2" below the inner circle, i.e. the two TPC tracks), crosses the middle circle again at tTOF2 and the outer circle at a fifth star at lower left that has no label. Thin leader lines join "tSteel" to the tMTD and tTOF1 points and "tTPC" to the tTOF1 and tTOF2 points, marking the path segments for the two expected flight times. Text in the figure: Cosmic Ray, tSteel, tMTD, tTOF1, tTOF2, tTPC, 1, 2.

**[note]** The figure matches the time definitions in the text. The second crossing of the outer circle (lower left) carries no time label, consistent with only one MTD hit being used; the figure does not say whether an MTD module sits there.

---

## 4. Performance of the MTD

### 4.1. Muon identification

- Selection: cosmic tracks with **$p_T > 2\,\mathrm{GeV}/c$** matched to TOF and MTD hits; each of the two tracks from one muon must have **≥ 25 TPC hits (of 45 possible)**.
- Fig. 3 left: p_T distribution for $p_T>2$ GeV/c; **mean p_T ≈ 6 GeV/c**. Fig. 3 right: relative momentum difference $\Delta p/p$ of the two TPC tracks of one muon; **average momentum resolution ≈ 10%**.
- Cut: $|\Delta p/p| < 27\%$.

![Fig. 3](assets/yang2014-mtd-cosmic-calibration/fig3.jpg)

**Fig. 3.** Left: p_T distribution of cosmic muons with $p_T > 2\,\mathrm{GeV}/c$. Right: relative momentum difference of the two tracks of one cosmic muon, with a Gaussian fit.

*Figure description (from the image):* Two panels side by side. Left: histogram of p_T (GeV/c), x 0–15, y "Counts" 0–~1100, 1 GeV/c bins starting at 2 GeV/c; highest bin 2–3 GeV/c (≈1040), then falling monotonically to ≈125 in the 14–15 GeV/c bin; still non-zero at the right edge, so the tail above 15 GeV/c is not shown. No fit and no mean printed. Right: histogram of Δp/p, x −1 to 1, y "Counts" 0–~280, fine bins; entries only between ≈ −0.25 and ≈ +0.31 (sharp edges on both sides), peak ≈270 at 0; Gaussian (thick black curve) fitted over about −0.15 to +0.15. Fit box: χ²/ndf = 50.18/27, Constant = 242.7 ± 4.8, Mean = −0.0002657 ± 0.0018702, Sigma = 0.1005 ± 0.0026. Tails above the Gaussian beyond about ±0.1, with a shoulder near +0.25.

**[note]** The "≈10%" of the text is the fitted σ of the two-track Δp/p distribution (0.1005), which settles the question in the next note: it is the width of the difference, so the per-track value would be ≈ 0.10/√2 ≈ 7% if the two errors are independent.

**[note]** The sharp edges at ≈ −0.25 and ≈ +0.31 (read off the axis) probably reflect the |Δp/p| < 27% cut but are not symmetric about zero; the paper does not define which momentum is in the denominator, so this cannot be checked further.

**[note]** The paper does not say whether "≈10%" is the width of the Δp/p distribution or a per-track value. If the two tracks have independent errors, the per-track resolution is the width / √2.

- Fig. 4: TPC dE/dx versus p. The expected muon dE/dx from the Bichsel function [23] (line) describes the data well, showing a clean cosmic-muon sample.

![Fig. 4](assets/yang2014-mtd-cosmic-calibration/fig4.jpg)

**Fig. 4.** TPC dE/dx versus momentum p; the solid curve is the expected muon dE/dx.

*Figure description (from the image):* Single 2D colour histogram. x: p (GeV/c), log scale, ≈2 to 100 (only 10 and 10² labelled; the lower edge ≈2 GeV/c is inferred from the tick spacing); y: dE/dx, labelled "KeV/cm", 0–10; colour scale 0 to ~230 counts (violet → red). The data form one narrow band: ≈2.4–3.7 keV/cm at p = 2–3 GeV/c, densest (yellow–red) near 2.8–3.0 keV/cm at the lowest p, rising slowly and thinning with p; above ~20 GeV/c only sparse entries around 3.3–4.0 keV/cm. The magenta curve (legend "expected μ dE/dx", legend marker a tiny dot) runs from ≈2.85 keV/cm at 2 GeV/c to ≈3.7 keV/cm at 100 GeV/c (relativistic rise) and follows the band centre. A few isolated entries at ≈5.6–5.9 keV/cm near p ≈ 2.3 and ≈ 5 GeV/c; no second band.

### 4.2. Spatial resolution

- TPC tracks are extrapolated to the MTD radius to measure the resolution in **Z (along the strips)** and **φ (perpendicular to the strips)**.
- Field map used in the extrapolation: **0.5 T** in one direction at the radii of TPC, TOF and BEMC; **opposite direction, −1.26 T, inside the backleg steel**; the BEMC PMT boxes and MTD are field-free.
- Hit position: φ = centre of the strip with the largest signal; Z from the **leading-edge time difference between the two ends of the strip**. (No signal propagation speed is given; see Check c.)
- Fig. 5: ΔZ (left) and Δφ (right) between extrapolated track and MTD hit. Standard deviations: **2.6 cm** and **0.006 rad**.

![Fig. 5](assets/yang2014-mtd-cosmic-calibration/fig5.jpg)

**Fig. 5.** ΔZ and Δφ between TPC tracks extrapolated to the MTD and the MTD hits, with Gaussian fits.

*Figure description (from the image):* Two panels side by side, histograms with Gaussian fits (thick black curves). Left: Δz (cm), x −30 to 30, y "Counts" 0–~380; peak ≈375 at 0; fit over about −6 to +6 cm. Fit box: χ²/ndf = 131.5/39, Constant = 330.9 ± 5.4, Mean = 0.02751 ± 0.03215, Sigma = 2.551 ± 0.032. Peak bins above the fit and non-Gaussian tails beyond ≈ ±5 cm. Right: Δφ (rad), x −0.1 to 0.1, y "Counts" 0–~620; peak ≈595 just below 0; fit over about −0.023 to +0.008 rad. Fit box: χ²/ndf = 173.3/26, Constant = 513.4 ± 8.5, Mean = −0.007424 ± 0.000076, Sigma = 0.006111 ± 0.000075. Tails mostly on the negative side.

**[note]** The text's 2.6 cm and 0.006 rad are the rounded fit σ values (2.551 cm, 0.006111 rad) ✓. The Δφ peak is offset from zero by −0.0074 rad (≈ −3 cm at 400 cm, ≈1.2σ), which the paper does not mention. The plot does not state the data set (year, module type).

**[note]** 0.006 rad × 400 cm = 2.4 cm ✓ (arithmetic), so before the multiple-scattering unfolding both directions are ~2.5 cm. The Fig. 5 axes in the PDF span ΔZ ±30 cm and Δφ ±0.1 rad.

- Fig. 6: resolution versus muon momentum, fitted with a form motivated by multiple scattering:

$$
y=\sqrt{\left(p_0/x^{2}\right)+p_1}
\qquad\text{(Sec. 4.2, inline in the paper)}
$$

  with $p_0$, $p_1$ fit parameters and $x$ the momentum. The intrinsic MTD resolution (no multiple scattering) is $\sqrt{p_1}$.
- Results: **0.8 cm (Z)** and **$2.2\times10^{-3}$ rad (φ)**; the φ value equals **0.9 cm** at the 400 cm MTD radius.

**[note]** $2.2\times10^{-3}\times400$ cm = 0.88 cm ✓. The $1/x^2$ term in $y^2$ is the expected $\sigma_{\rm MS}\propto1/p$ ✓.

**[note]** Strip-pitch check (an item in [[open-questions]]): a digital "centre of the strip" position gives σ ≈ pitch/√12: type A (2.5 + 0.4 = 2.9 cm) → 0.84 cm, close to the measured 0.9 cm ✓; type B (3.8 + 0.6 = 4.4 cm) → 1.27 cm, against 1.6–1.9 cm measured for type B in Table 2. Worked out in [[mrpc-technology]].

![Fig. 6](assets/yang2014-mtd-cosmic-calibration/fig6.jpg)

**Fig. 6.** Spatial resolution in Z (left) and φ (right) versus muon momentum; the curves are fits with the function above.

*Figure description (from the image):* Two panels side by side. Left: "z Resolution (cm)", 0–10, vs p (GeV/c), 0–20; black squares with blue error bars (horizontal bars = 1 GeV/c bins); 17 visible points at p = 2.5…18.5 GeV/c, falling from ≈4.6 cm at 2.5 GeV/c to ≈1.2–1.4 cm above 12 GeV/c (two low points ≈0.8 cm at 16.5 and 17.5 GeV/c, one high ≈1.7 cm with a large error at 18.5 GeV/c). Black curve = fit y = √(p0/x² + p1), drawn from ≈1 to 20 GeV/c, ≈1.05 cm at 20 GeV/c. Box: Entries = 19, Mean = 11.5 ± 2.242, RMS = 6.555 ± 1.585, χ²/ndf = 26.32/16, p0 = 149.6 ± 6.7, p1 = 0.6873 ± 0.1287. Right: "φ Resolution (rad)", 0–0.03, vs p (GeV/c), 0–20; same style; 18 visible points at 2.5…19.5 GeV/c, from ≈0.0117 rad at 2.5 GeV/c to ≈0.002–0.005 rad above 9 GeV/c. Box: Entries = 19, Mean = 9.009 ± 1.403, RMS = 5.344 ± 0.9923, χ²/ndf = 27.45/16, p0 = 0.0008779 ± 0.0000495, p1 = 4.981e-06 ± 9.260e-07.

**[note]** √p1 = √0.6873 = 0.83 ± 0.08 cm and √(4.981×10⁻⁶) = (2.23 ± 0.21)×10⁻³ rad, matching the text's 0.8 cm and 2.2×10⁻³ rad ✓. Entries/Mean/RMS are ROOT statistics of the plotted histogram, not physics results. ndf = 16 implies 18 fitted points, while the z panel shows only 17 points in range.

### 4.3. Time resolution

- **Matching cuts for "well-matched" tracks:** $\Delta Z < 6\,\mathrm{cm}$ and $\Delta\phi < 0.2\,\mathrm{rad}$ (see Check a).
- **Start time from TOF.** The two TOF times give the event start time. Its resolution comes from

$$
\Delta T_0=\left(t_{\mathrm{TOF2}}-t_{\mathrm{TOF1}}\right)-t_{\mathrm{TPC}}
\qquad\text{(Sec. 4.3, inline)}
$$

  where $(t_{\rm TOF2}-t_{\rm TOF1})$ is the measured time of flight and $t_{\rm TPC}$ the time of flight expected for a muon with the TPC trajectory and momentum. Fig. 7: **σ(ΔT₀) = 90 ps**, so the single TOF time resolution is $90\,\mathrm{ps}/\sqrt{2}=$ **64 ps**.

**[note]** 90/√2 = 63.6 ps ✓. Fit box of Fig. 7 (PDF text layer): χ²/ndf = 61.53/35, Mean = −0.003857 ± 0.001566 ns, Sigma = 0.08952 ± 0.00128 ns ✓ (90 ps). The 64 ps also absorbs the $t_{\rm TPC}$ uncertainty, so it is an upper bound on the pure TOF single-hit resolution.

![Fig. 7](assets/yang2014-mtd-cosmic-calibration/fig7.jpg)

**Fig. 7.** ΔT₀ from the two TOF hits and the TPC-expected time of flight, with a Gaussian fit.

*Figure description (from the image):* Single panel. Histogram of ΔT0 (ns), x −2 to 2, y "Counts" 0–~380, with Gaussian fit (black curve over about −0.4 to +0.4 ns). Narrow peak ≈375 at 0; small tails out to about ±0.5 ns, otherwise empty. Fit box: χ²/ndf = 61.53/35, Constant = 364 ± 8.2, Mean = −0.003857 ± 0.001566, Sigma = 0.08952 ± 0.00128. Box values agree with the note above (σ = 90 ps) ✓.

- **Quantity used for slewing calibration and resolution:** MTD time minus the TOF start time and minus the expected TOF→MTD flight time:

$$
\Delta T=\left(t_{\mathrm{TOF2}}-t_{\mathrm{TPC}}+t_{\mathrm{TOF1}}\right)/2-t_{\mathrm{MTD}}-t_{\mathrm{Steel}}
\qquad\text{(Sec. 4.3, inline)}
$$

  ΔT distributions are built per MTD read-out strip.

**[note]** $(t_{\rm TOF2}-t_{\rm TPC})$ and $t_{\rm TOF1}$ are two estimates of the time at the first TOF hit, so the first term is their average.

- **Slewing calibration, three passes**, illustrated with the **2010 data with three type A modules**. Pulse-size variable (TOF and MTD): pulse width at the leading-edge threshold, **Time over Threshold (ToT)**.
  1. **Relative offsets:** fit each strip's ΔT with a Gaussian and record the means. Fig. 8: ΔT versus strip (left), ΔT of one strip with Gaussian fit (right).
  2. **Slewing curve:** combine all channels using the offsets and plot ΔT versus ⟨ToT⟩, the geometric mean of the ToT at the two ends of the hit strip,
$$
\langle \mathrm{ToT}\rangle=\sqrt{\mathrm{ToT}_{L}\ast\mathrm{ToT}_{R}}
\qquad\text{(Sec. 4.3, inline; "∗" = multiplication)}
$$
     fitted with a **fifth-order polynomial** (Fig. 9).
  3. **Re-equalize** the channel time offsets after applying the step-1 offsets and subtracting the polynomial slewing.

![Fig. 8](assets/yang2014-mtd-cosmic-calibration/fig8.jpg)

**Fig. 8.** ΔT versus read-out strip (left), and ΔT for the first read-out strip with a Gaussian fit (right).

*Figure description (from the image):* Two panels side by side. Left: scatter (black dots) of ΔT (ns), 232–236, vs "Strip Number", 0–18; 18 vertical columns at strips 0–17 (strip 0 drawn on the left axis), each ≈1–1.5 ns tall; column centres range from ≈233.2 ns (strip 0) to ≈234.9 ns (strips 3 and 6), i.e. strip-to-strip offsets up to ≈1.7 ns before calibration. Right: histogram of ΔT (ns), 232–236, y "Counts" 0–~28, with Gaussian fit; peak ≈28 near 233.2 ns; entries from ≈232.5 to ≈233.8 ns plus one isolated count at ≈235.3 ns. Fit box: χ²/ndf = 28.89/25, Constant = 26.79 ± 2.15, Mean = 233.2 ± 0.0, Sigma = 0.1825 ± 0.0107 ("± 0.0" as printed).

**[note]** Box values agree with the note below ✓, and the right-panel mean (233.2 ns) matches the strip-0 column of the left panel. The absolute ΔT ≈ 233–235 ns is an uncalibrated offset; after the offset step ΔT is centred near 0 (Figs. 9, 10).

**[note]** PDF text layer: strip axis 0–18 (3 type-A modules × 6 strips = 18 ✓); right-panel fit χ²/ndf = 28.89/25, Constant = 26.79 ± 2.15, Mean = 233.2 ± 0.0 ns, Sigma = 0.1825 ± 0.0107 ns (one strip, before slewing correction).

![Fig. 9](assets/yang2014-mtd-cosmic-calibration/fig9.jpg)

**Fig. 9.** Gaussian mean ΔT as a function of [variable missing in the caption; the x axis is labelled "TOT (ns)", i.e. ⟨ToT⟩], with a fifth-order polynomial fit.

*Figure description (from the image):* Single panel. x "TOT (ns)", 11–21; y "ΔT (ns)", −0.8 to 0.8. Black squares with blue vertical error bars at ToT steps of ≈0.2 ns from ≈11.9 to ≈20.3 ns; no points between ≈17.5 and ≈19.1 ns. Black curve (fifth-order polynomial, drawn ≈11.55–20.45 ns): minimum ≈ −0.38 ns near 12.6 ns, rising almost linearly to ≈ +0.2 ns at ≈17.3 ns, flat at ≈0.21 ns up to ≈19 ns, then rising to ≈ +0.39 ns at the right end; total swing ≈0.6–0.7 ns. The points at ≈11.9, 12.5, 13.1 and 19.1 ns have error bars spanning most or all of the y range (low statistics); the points at ≈11.9 ns (+0.14) and ≈12.1 ns (−0.47) lie well off the curve. No fit parameters printed.

**[note]** The x-axis label "TOT (ns)" supports the source-issue fix below (the missing caption variable is ⟨ToT⟩). The y values are centred near 0, i.e. after the step-1 offsets, unlike the raw ≈233 ns of Fig. 8.

**[source issue]** The Fig. 9 caption reads "as a function of ." with the variable missing, identically in the HTML, the publisher PDF and arXiv v1. From the text and the axis label it should be ⟨ToT⟩.

- **Result.** Time resolution = σ of a Gaussian fit to the corrected ΔT, per strip in Fig. 10 (top). All strips combined (Fig. 10, bottom): **total 104 ps**. This includes the start-time resolution **90 ps/2 = 45 ps** and the multiple-scattering contribution for 6 GeV/c muons, **25 ps**. Subtracting both in quadrature gives an **MTD time resolution of 90 ps**, close to early test-beam and cosmic bench values.

$$
\sigma_{\rm MTD}=\sqrt{104^{2}-45^{2}-25^{2}}\ \mathrm{ps}=90.4\ \mathrm{ps}\quad\checkmark
$$

**[note]** Start-time resolution: σ of $(t_{\rm TOF2}-t_{\rm TPC}+t_{\rm TOF1})/2$ is ½ × the quadrature sum of the same three terms that make up σ(ΔT₀), i.e. exactly 90/2 = 45 ps ✓ (the $t_{\rm TPC}$ error is included). Fig. 10 fit box (PDF text layer): χ²/ndf = 18.17/9, Constant = 612.7 ± 14.1, Mean = −0.0003339 ± 0.0018802 ns, Sigma = 0.1043 ± 0.0016 ns ✓ (104 ps). The top panel's axis spans 0.07–0.14 ns.

**[note]** The 2 GeV/c multiple-scattering timing figure of 100 ps (Sec. 3.2) scaled as 1/p would give ~33 ps at 6 GeV/c, against the quoted 25 ps; the two numbers refer to different geometries (collision muons through the backleg vs. cosmic tracks), so this is only an order-of-magnitude consistency.

![Fig. 10](assets/yang2014-mtd-cosmic-calibration/fig10.jpg)

**Fig. 10.** Time resolution versus read-out channel (top), and ΔT from all strips after slewing and offset corrections (bottom), with the Gaussian fit giving the total MTD+TOF timing resolution.

*Figure description (from the image):* Two panels stacked. Top: "Timing Resolution (ns)" vs "Strip Number" 0–18; 18 black squares (strips 0–17) with vertical error bars ≈ ±0.005–0.009 ns; y axis labelled 0.07–0.14 (lower edge ≈0.065). Values from ≈0.077 ns (strip 3) to ≈0.126 ns (strip 17), most between ≈0.084 and ≈0.115 ns; no trend with strip number. Bottom: histogram of ΔT (ns), x −2 to 2, y "Counts" 0–~650, bins ≈0.05 ns; peak bin ≈640 at 0; Gaussian fit over about −0.28 to +0.30 ns; small tails to about −0.7 and +0.6 ns. Fit box: χ²/ndf = 18.17/9, Constant = 612.7 ± 14.1, Mean = −0.0003339 ± 0.0018802, Sigma = 0.1043 ± 0.0016.

**[note]** Box values agree with the note above (104 ps) ✓. The per-strip values in the top panel scatter around ≈0.10 ns, consistent with the combined 104 ps.

- The other data sets of Table 1 were calibrated the same way; results are in Table 2. The same MRPC type gives consistent performance across years.

**Table 2.** The time and/or spatial resolution of the MTD MRPCs operated in STAR during the 2007–2012 RHIC runs.

| Conditions | Type | Resolution |
|---|---|---|
| Cosmic & test-beams [14] | Type A | 60 ps, 0.6 cm |
| Run 7: Au+Au [15] | Type A | 200–300 ps |
| Run 8: d+Au, p+p | | |
| Run 9: p+p | Type A | 90 ps, 0.8 cm (z), 0.9 cm (ϕ) |
| Run 10: Au+Au, cosmic trigger | | |
| Run 11: Au+Au, cosmic trigger | Type A | 89 ps, 1.1 cm (z), 1.1 cm (ϕ) |
| | Type B | 101 ps, 1.4 cm (z), 1.6 cm (ϕ) |
| | Type C | 127 ps, 2.4 cm (z), 1.8 cm (ϕ) |
| Run 12: p+p, cosmic trigger | Type B | 108 ps, 2.6 cm (z), 1.9 cm (ϕ) |

**[note]** Blank cells as printed: Run 8 shares the Run 7 entry, Run 10 the Run 9 entry. The Run 9/10 row equals the worked 2010 type-A example in the text (90 ps, 0.8 cm, 0.9 cm) ✓. Final-design type B: 101 ps (Run 11) and 108 ps (Run 12), z 1.4–2.6 cm, φ 1.6–1.9 cm.

**[note]** The Run 12 type-B z value (2.6 cm) equals the raw ΔZ σ quoted for Fig. 5 (2.6 cm). The paper does not say which data set Fig. 5 shows or whether the Run 12 values are √p₁ values. If Fig. 5 is Run 12 data, the Run 12 entry may be the raw width rather than the multiple-scattering-corrected value. Not resolvable from the paper.

---

## 5. Conclusions

Cosmic-ray muons crossing STAR were used to measure the MTD time and spatial resolution. The relatively high-momentum muons can be triggered and selected cleanly, and their multiple-scattering contribution is small. Over several years of data, the MTD gives **~100 ps** timing and **1–2 cm** spatial resolution.

## Acknowledgments

The authors thank the STAR Collaboration and the RACF at BNL.

---

## Checks

**(a) Δφ matching cut.** Publisher PDF: "Δϕ < 0.2 rad" (pdftotext: "Δϕ o0:2 rad"); HTML MathML: `Δϕ < 0.2 rad`; arXiv v1: "∆φ<0.2 rad". All three say **0.2 rad**. Context:
- 2π/30 = 0.2094 rad is the azimuthal width of one backleg (30 backlegs, Sec. 3.1; that the full MTD has its trays arranged per backleg is outside knowledge, not stated here). A 0.2 rad window therefore means roughly "same backleg sector" as the extrapolated track.
- Against the measured widths it is very loose: 0.2 rad ≈ 33 × the raw 0.006 rad σ and ≈ 80 cm at 400 cm, while the companion cut ΔZ < 6 cm is ≈ 2.3 × the raw 2.6 cm σ. The Fig. 5 Δφ axis only spans ±0.1 rad, so the cut lies outside the plotted range.
- 0.02 rad (≈ 3.3σ, ≈ 8 cm at 400 cm) would match the tightness of the ΔZ cut and the phrase "well-matched".
- **Verdict:** the printed value is 0.2 rad in every version; read as a sector-level match it is self-consistent. A typo for 0.02 rad stays possible but cannot be shown from the paper. Flag softened to a **[note]**, not a [source issue].

**(b) Field used for t_Steel.** Sec. 3.2 (PDF and arXiv): t_Steel "can be derived from the track's helix parameters, momentum p, and the 0.5 T magnetic field". Sec. 4.2 uses 0.5 T inside, **−1.26 T** in the backleg steel (arXiv prints "-1.26 T"; in the publisher PDF the minus is a font glyph that pdftotext turns into a control character; the HTML has −1.26 T) and zero field at the MTD for the position extrapolation. **[source issue]** (minor): the stated 0.5 T for t_Steel does not match the Sec. 4.2 field map. **[note]** For timing this hardly matters: for a 6 GeV/c track over ~1.8 m (220 → 400 cm), the path-length excess over a chord is L³/(24R²) ≈ 0.15 mm (R = 40 m at 0.5 T) → 0.5 ps, and through 57 cm of steel at 1.26 T (R = 15.9 m) ≈ 0.03 mm → 0.1 ps. The difference between field models is therefore ≪ 1 ps, far below the 25 ps multiple-scattering term. The field model matters for the ΔZ/Δφ position matching, not for t_Steel. (Rough estimate: a radial straight path is assumed; cosmic tracks are not radial.)

**(c) Signal propagation speed along the strips.** **Not stated.** The paper only says that Z is derived from the leading-edge time difference between the two strip ends (Sec. 4.2). No cm/ns value, effective speed, or strip length conversion appears in the HTML, the publisher PDF or the arXiv text (searched for speed/velocity/propagat/cm/ns). The 15–18 cm/ns value listed in [[open-questions]] cannot be confirmed from this paper.

**(d) Backleg thickness.** "57 cm thick at a radius of 363 cm", trapezoidal cross-section, 6.85 m long, 30 flux-return bars (Sec. 3.1; HTML = PDF = arXiv). **[note]** 57 cm Fe ≈ 3.4 λ_I (λ_I = 16.8 cm); the BEMC adds to the absorber, as the paper says ("return bars and the BEMC serve as a hadron absorber").

**HTML vs PDF differences.** None of substance. All values, cuts, equations and both tables agree. Text-extraction artefacts only: in pdftotext the publisher PDF loses "~" (e.g. "at a radius of 400 cm" in Sec. 2), minus signs and "×" (rendered as control characters or spaces), and "<"/">" come out as "o"/"4". The HTML is the clean reading for these, and the arXiv text confirms "∼400 cm", "−1.26 T" and "2.2×10⁻³". The Fig. 9 caption gap is in all versions (source issue above). arXiv v1 differs in wording only in minor places (e.g. "and are 2.6 cm and 0.006 radians, respectively").

**Recomputed numbers.** √(104² − 45² − 25²) = 90.4 ps ✓ (90 ps); 90/√2 = 63.6 ps ✓ (64 ps); 90/2 = 45 ps ✓; 2.2×10⁻³ rad × 400 cm = 0.88 cm ✓ (0.9 cm); 0.006 rad × 400 cm = 2.4 cm; 25 ns/1024 = 24.41 ps ✓ (24.4 ps LSB); 12 × 3.8 + 11 × 0.6 = 52.2 cm ✓ (52 cm module); 2π/30 = 0.209 rad.

---

## References (hardware-relevant subset)

Numbering as in the paper. The topic in parentheses is a **[note]** annotation, not part of the citation.

- [10] STAR Muon Telescope Detector Proposal (L. Ruan et al.), STAR web, MTD_proposal_v14 (2010).
- [11] STAR Time-of-Flight Proposal (2004), STAR web.
- [12] W.J. Llope, et al., Nucl. Instrum. Meth. A 661 (2012) S110 (STAR TOF system/electronics).
- [13] B. Bonner, et al., NIM A 508 (2003) 181; M. Shao, et al., NIM A 492 (2002) 344; J. Wu, et al., NIM A 538 (2005) 243 (TOF MRPCs).
- [14] Y. Sun, et al., NIM A 593 (2008) 307; Y. Wang, et al., NIM A 640 (2011) 85 (MTD prototype cosmic / beam tests).
- [15] L. Ruan, et al., J. Phys. G 36 (2009) 095001 (MTD design); Z. Xu, BNL LDRD project 07-007; Beam Test Experiment (T963) at FermiLab.
- [16] F.S. Bieser, et al., NIM A 499 (2003) 766 (STAR trigger / earlier digitization).
- [17] W.J. Llope, et al., NIM A 596 (2008) 430 (earlier front-end electronics).
- [18] J.J. Schambach, et al., Int. J. Mod. Phys. E 16 (2007) 2496 (TOF electronics).
- [19] High Performance Time to Digital Converter (HPTDC) Manual, v2.2, CERN.
- [20] K.H. Ackermann, et al., NIM A 499 (2003) 624 (STAR detector overview).
- [21] M. Anderson, et al., NIM A 499 (2003) 659 (STAR TPC).
- [22] M. Shao, et al., NIM A 558 (2006) 419 (TPC PID).
- [23] H. Bichsel, NIM A 562 (2006) 154 (dE/dx / Bichsel function).
- [24] Y. Xu, et al., NIM A 614 (2010) 28 (PID with TPC dE/dx).
- [25] J. Adams, et al., Phys. Lett. B 616 (2005) 8 (TOF PID).
- [26] M. Beddo, et al., NIM A 499 (2003) 725 (STAR BEMC).
- [27] F. Bergsma, et al., NIM A 499 (2003) 633 (STAR magnet).

Physics references [1]–[9] (QGP white papers, di-lepton and quarkonium theory) are omitted here as not hardware-relevant.
