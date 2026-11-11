---
title: "Huang 2016 — Muon identification with Muon Telescope Detector at the STAR experiment (full-content paraphrase)"
type: raw-source
source_type: paper
authors: "T.C. Huang et al., 12 authors"
journal: "Nucl. Instrum. Meth. A 833 (2016) 88–93"
doi: 10.1016/j.nima.2016.07.024
arxiv: "1601.02910"
captured_via: "Route 2 — arXiv HTML (v3) for text, Eq. (1) and Table 1, cross-checked against the arXiv v3 PDF and rechecked against the publisher PDF (ScienceDirect served no HTML body)"
captured_date: 2026-11-05
captured_as: full-content paraphrase
figures: "7 (vision descriptions added 2026-11-05)"
vision_model: "general-purpose subagent (session model, not recorded), 2026-11-05"
---

# Muon identification with the Muon Telescope Detector at STAR (Huang et al., NIM A 2016) — reading note

- **Citation:** T.C. Huang, R. Ma, B. Huang, X. Huang, L. Ruan, T. Todoroki, Z. Xu, C. Yang, S. Yang, Q. Yang, Y. Yang (corresponding, yiyang@ncku.edu.tw), W. Zha, "Muon identification with Muon Telescope Detector at the STAR experiment".
- **Journal ref:** Nucl. Instrum. Meth. A 833 (2016) 88–93 (volume and pages confirmed on page 1 of the publisher PDF). **DOI:** [10.1016/j.nima.2016.07.024](https://doi.org/10.1016/j.nima.2016.07.024) (from the arXiv abstract page "Related DOI"; resolves to ScienceDirect PII S0168900216307392).
- **arXiv:** [1601.02910](https://arxiv.org/abs/1601.02910) [physics.ins-det], v3 dated 15 Jul 2016 ("Preprint submitted to NIMA July 18, 2016").
- **Affiliations:** National Cheng Kung University (Tainan); Brookhaven National Laboratory; Tsinghua University; University of Illinois at Chicago; University of Science and Technology of China.
- **Route used:** Route 2 — arXiv HTML (https://arxiv.org/html/1601.02910) for text, Eq. (1) LaTeX (LaTeXML `alttext`) and Table 1, cross-checked line by line against `pdftotext -layout` of the arXiv v3 PDF. **Why Route 1 failed:** the ScienceDirect article page (JLab access, "Full text access") serves only the abstract, keywords and a "View PDF" link — no HTML body, no `<figure>` elements, no MathML for the article text (page text ≈1.8 kB). The publisher PDF could be opened in Chrome (pdf.sciencedirectassets.com/…/main.pdf, HTTP 200, ≈1.03 MB, starts with `%PDF-`), but the scripted save failed (three attempts; most likely Chrome's automatic-multiple-downloads block for that host, which I did not try to bypass). Reading the PDF text in-browser via an external pdf.js import was refused by the permission system.
- **PDF backup:** `assets/huang2016-mtd-muon-id/source.pdf` (publisher NIM A version, 1 031 955 bytes; saved manually from Chrome on 2026-11-05 after the scripted download was blocked). The arXiv v3 PDF (239 743 bytes) used for the line-by-line check was not kept (publisher version kept).
- **Figures:** `assets/huang2016-mtd-muon-id/fig1.jpg` … `fig7.jpg`, full-resolution publisher images (ars.els-cdn.com `1-s2.0-S0168900216307392-grN_lrg.jpg`, gr1–gr7; gr8+ return 404). gr N = Fig. N (one-to-one; Fig. 4(a)/(b) are one image).
- **Verification:** every equation, number, cut value and table entry below was first checked against `pdftotext -layout` of the arXiv v3 PDF. The publisher HTML abstract is identical to the arXiv abstract. arXiv HTML vs arXiv PDF: no content discrepancies found (Eq. (1), Table 1, cut values, captions agree). Figure descriptions were added by a separate figure pass that looked at the images. **Publisher-PDF recheck (main agent, 2026-11-05):** every number in the note body was searched in `pdftotext` of the publisher PDF. Table 1 (all rows incl. MC), all cut values, 28.3 pb⁻¹, the 1.004/0.022 smearing, the [2.92, 3.25] window, R > −0.2, 403 cm, "about 5 absorption lengths", the factor 1.38, S/√B = 31.89, the "about 60%" conclusion and the Fig. 3 caption listing ΔToF all match. In the publisher text layer "±" is rendered as "7" (e.g. "1656 7 143 7 114"), a font artifact only. Numbers printed inside figures (e.g. the Fig. 1 inset) are images in the publisher PDF and were checked in the arXiv vector figures. The only text difference found: the arXiv duplicated word "particles particles" is corrected in the journal.

---

## Abstract (paraphrase)

The MTD is a newly installed STAR subsystem that opens up heavy-quarkonium studies in the dimuon channel in heavy-ion collisions. Using $p+p$ collisions at $\sqrt{s}=500$ GeV, the authors evaluate the MTD muon identification with several methods. With the Likelihood Ratio method the muon identification efficiency reaches $\sim$90% for muons with $p_T > 3$ GeV/$c$, and the $J/\psi$ signal significance is improved by a factor of 2 relative to the basic selection.

**Keywords:** STAR, MTD, muon identification, muon, dimuon, quarkonium.

---

## Full content

### 1. Introduction

STAR [1] is one of the two large experiments at RHIC (BNL). After 15 years of running it has produced many results on QCD; in particular, evidence for the Quark Gluon Plasma (QGP) [2]. Heavy quarkonia are ideal probes of QCD matter: suppression by colour screening of surrounding partons is sensitive to the partonic nature and temperature of the QGP [3, 4]. Quarkonia are reconstructed from the invariant mass ($M_{inv.}$) of their dilepton decays; muons can be reconstructed more precisely than electrons because they suffer much less bremsstrahlung in material. The MTD, a new STAR subdetector dedicated to muons, was proposed in 2009 and installed between 2012 and 2014 [5, 6]. This paper presents its muon identification performance; muon ID studies at other experiments are in Refs. [7, 8, 9].

Layout: Sec. 2 STAR detector; Sec. 3 data sets and event selection; Sec. 4 three muon-ID methods; Sec. 5 efficiency and resulting $J/\psi$ significance; Sec. 6 summary.

### 2. The STAR detector

STAR is a general-purpose detector for high-energy nuclear physics. The subsystems relevant here are the Time Projection Chamber (TPC), the Magnet System and the MTD.

- **TPC** [10]: main tracking detector for charged particles; particle identification via energy loss (dE/dx). Full azimuth ($0<\phi<2\pi$), $|\eta|<1$. $p_T$ and charge $q$ from track curvature in the **0.5 T** solenoidal field of the Magnet System.
- **Magnet backlegs** [11]: **30 bars** ("backlegs") outside the coil provide the magnetic flux return. They are **61 cm thick at a radius of 363 cm**, "corresponding to about 5 absorption lengths" (PDF wording). They absorb hadrons from the collision and so are essential for muon purity.
- **MTD**: a fast detector based on Multi-gap Resistive Plate Chamber (MRPC) technology that records signals ("hits") from charged particles traversing it. It provides single-muon and dimuon triggers based on the number of hits within a predefined online timing window. Modules sit at a **radius of about 403 cm** and cover **about 45% in azimuth within $|\eta|<0.5$** [5]. Installation was **10%, 63% and 100%** complete for the **2012, 2013 and 2014** runs. From cosmic-ray data [12], the MTD **timing resolution is ~100 ps** and the **spatial resolutions are ~1–2 cm in both $r\phi$ and $z$**.

**[note]** 61 cm of iron is ≈3.6 nuclear interaction lengths ($\lambda_I(\mathrm{Fe}) = 16.8$ cm) or ≈5.9 nuclear collision lengths (10.4 cm); "about 5 absorption lengths" matches neither exactly for the backleg iron alone and presumably counts the full material in front of the MTD (or a loose definition). Treat the "5" as approximate.

**[source issue]** (minor wording) "to record signals, also referred to as signals ('hits')" is garbled in the PDF; the intended meaning is that the recorded signals are called hits.

### 3. Dataset and event selection

#### 3.1. Data and Monte Carlo

- Data: STAR **$p+p$ run at $\sqrt{s}=500$ GeV in 2013**, recorded with the **MTD dimuon trigger** (≥2 MTD hits in coincidence with the bunch crossing). Integrated luminosity **28.3 pb$^{-1}$**.
- MC: $J/\psi\to\mu^+\mu^-$ from a single-particle generator, flat in $p_T$, $\phi$, $\eta$; passed through full **GEANT3** [13] STAR simulation, **embedded** into real events and reconstructed with the standard chain. Kinematics of embedded $J/\psi$ and $\mu^\pm$ weighted by the $J/\psi$ $p_T$ spectrum in 500 GeV $pp$ obtained by interpolation through a global fit of world differential $J/\psi$ cross sections [14].
- MC muon $p_T$ additionally smeared with a Gaussian of **mean $= 1.004\times p_T$** and **width $= 0.022\times p_T$** to reproduce the reconstructed $J/\psi$ mass distribution in data.

#### 3.2. Track selection ("basic selection")

| Requirement | Value | Purpose |
|---|---|---|
| $p_T$ | > 1 GeV/$c$ | — |
| DCA to collision vertex | < 3 cm | suppress secondary decays |
| TPC clusters used in fit | > 15 (max. possible 45) | momentum resolution |
| TPC clusters for dE/dx | > 10 | dE/dx resolution |
| used / possible clusters | ≥ 0.52 ("not less than") | reject split tracks |
| MTD | track projects to MTD hits that fired the trigger | — |

[note] Table compiled from the text; the paper gives these in prose.

With these criteria on both daughters, the opposite-sign dimuon mass spectrum (Fig. 1) shows a clear $J/\psi$ peak near 3.1 GeV/$c^2$, with **more than 1500 $J/\psi$ candidates**. Lighter mesons (ω, φ, η) are hidden by large background at low $M_{inv.}$.

![Fig. 1](assets/huang2016-mtd-muon-id/fig1.jpg)

**Fig. 1.** Dimuon invariant-mass spectrum with the basic selection (Sec. 3.2) on both muons; black solid circles = opposite-sign pairs, red open circles = same-sign pairs. Inset: fit of the $J/\psi$ peak with a single Gaussian plus a fourth-order polynomial (solid red line); the two vertical black dashed lines mark the **mass window [2.92 – 3.25] GeV/$c^2$** used to select $J/\psi$ candidates. Inset fit values (read from the figure text in the PDF): $\chi^2/\mathrm{ndf} = 53.0/37.0$, $N_{J/\psi} = 1584\pm116$, $M = 3.086\pm0.004$ GeV/$c^2$, $\sigma = 0.056\pm0.005$ GeV/$c^2$, $S/\sqrt{B} = 15.36\pm1.14$; bins of 0.04 GeV/$c^2$.

*Figure description (from the image):* Single panel with an inset. Main: x = $M_{\mu\mu}$ [GeV/$c^2$], 0–6.5 (labels 0–6); y = Counts/Bin, ×10$^6$, 0 to ≈0.34 (labels 0, 0.1, 0.2, 0.3). Black solid circles "Opposite-sign", red open circles "Same-sign"; variable bin widths (fine bins at ≈0.6–0.8, ≈1.0 and ≈3.0–3.2 GeV/$c^2$, ≈0.2-GeV/$c^2$ bins over 1.4–3.0, wide bins above 3.4). OS maximum ≈0.25×10$^6$ at ≈0.45–0.65 GeV/$c^2$, steep fall over 0.7–0.85, a step near 1.0 GeV/$c^2$, smooth continuum with a small peak at ≈3.1 GeV/$c^2$ (OS ≈0.047×10$^6$ vs SS ≈0.025×10$^6$), both ≈0 above 5 GeV/$c^2$. SS lies below OS everywhere except the first bin (≈0.25 GeV/$c^2$: SS ≈0.13, OS ≈0.11 ×10$^6$). Inset: x = $M_{\mu\mu}$ [GeV/$c^2$], ≈2.3–3.9 (labels 2.4–3.8); y = Events/0.04 [GeV/$c^2$], ×10$^3$, 0 to ≈3.5 (labels 0–3). Black points, red solid "fit", red dashed "background", blue hatched Gaussian "signal" (peak ≈0.45×10$^3$ at ≈3.09); two vertical black dashed lines at the window edges (≈2.92 and ≈3.25 GeV/$c^2$). Data fall from ≈2.0×10$^3$ at 2.3 to ≈0.55×10$^3$ at 3.9, with the J/ψ peak ≈1.7×10$^3$ at ≈3.1. Printed text: χ²/ndf = 53.0/37.0; N$^{J/\psi}$ = 1584±116; M = 3.086±0.004 GeV/c²; σ = 0.056±0.005 GeV/c²; S/√B = 15.36±1.14 (same as the caption text above).

**[note]** (figure pass) The main-panel y values agree with the inset only if "Counts/Bin" is read as counts per GeV/$c^2$ (bin-width normalised): near 2.3 GeV/$c^2$ the main panel shows ≈0.049×10$^6$ in a ≈0.2-GeV/$c^2$-wide bin, while the inset shows ≈1.9×10$^3$ per 0.04 GeV/$c^2$, i.e. ≈4.8×10$^4$ per GeV/$c^2$ but only ≈1×10$^4$ per 0.2-GeV/$c^2$ bin. The axis label is therefore probably misleading; this is my inference from reading the axes, not stated in the paper.

**[note]** The Fig. 1 inset yield (1584 ± 116, $S/\sqrt B$ = 15.36) is a single fit; Table 1's basic-selection numbers (1656, 15.89) are averages over all signal×background fit-model combinations (Sec. 4.1), which explains the difference.

**[source issue]** (typo, arXiv v3 only) "ω, φ and η particles particles" — duplicated word; corrected in the journal version.

### 4. Muon identification

#### 4.1. Methods

Four discriminating variables are used:

- **ΔToF**: calculated time of flight from track extrapolation under the muon hypothesis minus the MTD-measured time.
- **Δz**, **Δy**: residuals between MTD hit position and the extrapolated track position on the MTD; $z$ is along the beam pipe, $y$ is perpendicular to $z$ in the plane of each MTD module (≈ $r\phi$). Δy is multiplied by the charge (**Δy × q**) to remove charge dependence.
- **$n\sigma_\pi$**: measured dE/dx minus the expected value for a pion (pion hypothesis chosen for compatibility with existing code), normalised to the TPC dE/dx resolution:

$$
n\sigma_{\pi}=\frac{(\log\frac{dE}{dx})_{{\rm measured}}-(\log\frac{dE}{dx})_{\pi,{\rm theory}}}{\sigma(\log\frac{dE}{dx})_{{\rm measured}}}. \tag{1}
$$

**PDFs.** Background probability distribution functions (PDFs) of each variable are taken from **same-sign (SS)** pairs inside $M_{inv.}\in[2.92, 3.25]$ GeV/$c^2$; pure-muon PDFs are obtained by subtracting these from the **opposite-sign (OS)** PDFs in the same window. Equivalent distributions are built from MC, **except ΔToF**, because the MTD timing signal is not modelled in the simulation. Fig. 2 compares signal (data and MC) and background PDFs; data and MC signal agree reasonably.

![Fig. 2](assets/huang2016-mtd-muon-id/fig2.jpg)

**Fig. 2.** Probability density functions of Δz, Δy × q, ΔToF and $n\sigma_\pi$. Black points: data signal (OS − SS); solid histograms: MC signal (embedded); dashed histograms: data background (SS). (Panel axes in the PDF: Δz in cm over ±80, Δy×q in cm over ±50, $n\sigma_\pi$ over ±5, ΔToF in ns over ±5.)

*Figure description (from the image):* 2×2 panels, y = Probability Density in each, black horizontal line at 0. Top-left: Δz [cm], −80 to 80; y labels 0, 0.2, 0.4. Top-right: Δy×q [cm], −50 to 50; y labels 0, 0.1, 0.2, 0.3. Bottom-left: nσ$_\pi$, −5 to 5; y labels 0, 0.1, 0.2, 0.3. Bottom-right: ΔToF [ns], −5 to 5; y labels 0, 0.2, 0.4, 0.6. Legend: blue solid histogram "MC Signal (embed.)" (absent in the ΔToF panel), black points "Data Signal (OS-SS)", black dashed histogram "Background (SS)". Δz: signal sharply peaked at 0 (data ≈0.30, MC ≈0.30), mostly within ≈±10 cm; background broad (peak ≈0.10) over ≈±60 cm; data-signal points dip slightly below 0 (to ≈−0.03) in the tails. Δy×q: signal peak ≈0.17–0.18 at 0, mostly within ≈±10 cm; background peak ≈0.07 just below 0 with a longer tail toward negative values. nσ$_\pi$: signal broad over ≈−2 to 3 (MC peak ≈0.17 at ≈0.5, data maximum ≈0.18 at ≈0.8); background peak ≈0.14 at ≈−0.2, shifted to lower nσ$_\pi$ than the signal. ΔToF (data only): signal very narrow at 0 (two points ≈0.43 and ≈0.35 at ≈−0.1 and ≈+0.1 ns); background peak ≈0.17 at ≈+0.2 ns with a tail to the right out to ≈+3 ns; the data signal goes negative (≈−0.06) near +1.5 ns. Data and MC signal shapes agree within the error bars; panel content matches the caption.

**Performance metric (tag-and-probe).** Three methods are compared — straight cuts, N−1 iteration, Likelihood Ratio — using tag and probe:
- low muon $p_T$ (**$p_T < 3.5$ GeV/$c$**): tag = higher-$p_T$ muon, probe = lower-$p_T$ muon;
- high muon $p_T$ (**$p_T > 3.5$ GeV/$c$**): tag (probe) = lower (higher) $p_T$ muon, to gain statistics.

Muon-ID cuts are applied to the probed muon; efficiency and background rejection come from the $J/\psi$ yield and significance before/after the cut. The mass spectra are fitted with several signal models (single Gaussian or Crystal-Ball) and background models (third- or fourth-order polynomial). The efficiency uses the **average** fitted $J/\psi$ yield over all signal×background combinations; the fit-model uncertainty is the **maximum deviation** of any combination from the average.

**• Straight cut method.** Direct cuts on the four variables: a window of about ±2.5σ on Δz and Δy × q, and an asymmetric window from −1.5σ to +2.5σ on $n\sigma_\pi$ (σ = width of the signal distributions in Fig. 2), to keep high efficiency while rejecting background. An empirical asymmetric cut is used on ΔToF because the hadron background has a long tail to the right. Cuts:

$$-5 < \Delta\mathrm{ToF} < 0.2\ \mathrm{ns},\quad |\Delta z| < 20\ \mathrm{cm},\quad |\Delta y\times q| < 20\ \mathrm{cm},\quad -1 < n\sigma_\pi < 3.$$

Footnote 1: the mean $n\sigma_\pi$ of muons is shifted to the right by ≈0.5σ relative to pions, so a tighter cut on the low side of $n\sigma_\pi$ reduces pion contamination.

**• N−1 iteration method.** One variable at a time is varied to optimise the $J/\psi$ significance $S/\sqrt{B}$ while the other N−1 variables are held fixed, iterating. Resulting cuts:

$$-4.8 < \Delta\mathrm{ToF} < 0.7\ \mathrm{ns},\quad -15 < \Delta z < 19\ \mathrm{cm},\quad -9 < \Delta y\times q < 14\ \mathrm{cm},\quad -0.5 < n\sigma_\pi < 3.6.$$

**• Likelihood Ratio method.** A multivariate discriminant built as a likelihood ratio (inline in the paper, unnumbered):

$$R = \frac{1-Y}{1+Y},\qquad Y=\prod_i y_i,\qquad y_i = PDF^{\rm bkg}_{i}/PDF^{\rm sig}_{i}.$$

Because the data signal PDFs fluctuate strongly with limited statistics, the **embedded MC** is used for the signal PDFs. **Only three variables — Δy × q, Δz and $n\sigma_\pi$ — enter R** for the probed muon; the **ΔToF cut is fixed to the N−1 iteration value** ($-4.8<\Delta$ToF$<0.7$ ns). Fig. 3 shows the ratios $PDF^{bkgd}/PDF^{sig}$ for Δy×q, Δz and $n\sigma_\pi$: bin-to-bin interpolation (solid red) in the central region, linear fit (dashed red) in the low-statistics side regions. Fig. 4(a) shows the discriminating power of R; the cut **$R > -0.2$** maximises the $J/\psi$ significance (Fig. 4(b)).

**[note]** $R\in(-1,1]$ for $Y\ge 0$: $R\to 1$ when background/signal ratios are small (muon-like), $R\to -1$ when they are large.

![Fig. 3](assets/huang2016-mtd-muon-id/fig3.jpg)

**Fig. 3.** PDF ratios of "Δz, Δy × q, ΔToF, and $n\sigma_\pi$" (caption wording). Solid red line = bin-to-bin interpolation; dashed red line = linear fit used to parameterise the ratio. (Legend in the $n\sigma_\pi$ panel of the PDF: "linear extrapolation", "linear fit", "linear fit (±1σ)"; the ±1σ variations are the blue dot-dashed lines referred to in Sec. 4.2.)

*Figure description (from the image):* Three PDF-ratio panels plus a legend in the lower-right quadrant; y = PDF ratio in each. Top-left: Δz [cm], −80 to 80, y −10 to 50. Top-right: Δy×q [cm], −50 to 50, y ≈−5 to 15 (labels −4 to 14). Bottom-left: nσ$_\pi$, −5 to 5, y −10 to 50. Legend: black points with error bars "PDF ratio", red solid "linear extrapolation", red dashed "linear fit", blue dot-dot-dashed "linear fit (±1σ)"; a thin black dashed horizontal line at ratio = 1. All three ratios are below 1 in the central region (minimum ≈0.4–0.5) and rise steeply outside it. The red solid line joins the central points (Δz ≈−28 to +28 cm, Δy×q ≈−18 to +24 cm, nσ$_\pi$ ≈−1.6 to +3.3); outside, wide bins with large errors are described by the red dashed fits and blue ±1σ lines. Largest points: Δz ≈34 at −75 cm and ≈27 at +68 cm; Δy×q ≈12.7 at −46 cm and ≈7 at +40 cm; nσ$_\pi$ ≈15 at −2.5 (the low-side fit lines reach ≈23–46 at −5), while the high side of nσ$_\pi$ stays ≈1–2 up to 5.

**[note]** (figure pass) The image has exactly three PDF-ratio panels (Δz, Δy×q, nσ$_\pi$) and no ΔToF panel; the fourth quadrant holds only the legend. This confirms the [source issue] below: "ΔToF" in the caption is a leftover.

**[source issue]** (figure pass) The legend calls the solid red line "linear extrapolation", while the caption and Sec. 4.1 call it bin-to-bin interpolation.

**[source issue]** The Fig. 3 caption lists ΔToF among the PDF ratios, but the text says R uses only three variables (Δy×q, Δz, $n\sigma_\pi$), the in-text description of Fig. 3 names only those three, and the figure (per the PDF text layer) has three panels (Δz, Δy×q, $n\sigma_\pi$). "ΔToF" in the caption appears to be a leftover. Also a stray comma in "for, Δy×q, Δz, and $n\sigma_\pi$".

![Fig. 4](assets/huang2016-mtd-muon-id/fig4.jpg)

**Fig. 4.** (a) Likelihood Ratio R distributions for signal (blue; OS−SS) and background (red; SS), per 0.10 in R. (b) Optimisation of the R cut value using the signal significance $S/\sqrt{B}$.

*Figure description (from the image):* Two panels, (a) left and (b) right. (a): x = Likelihood Ratio (R), ≈−1.1 to 1.1 (labels −1, −0.5, 0, 0.5, 1); y = "Probabilty(R)/0.10" (sic), 0 to ≈0.26 (labels 0–0.25); hatched histograms, blue "Signal (OS-SS)" and red "Background (SS)", 0.1-wide bins. Background peaks in the lowest bin (≈0.20 at R ∈ [−1, −0.9]), then ≈0.09 and ≈0.06, a flat ≈0.04–0.05 plateau up to R ≈ 0.7, and ≈0.015 in [0.7, 0.8]. Signal is zero below R = −0.8, low (≈0.01–0.06) up to R ≈ −0.1, then rises to its maximum ≈0.145 at R ∈ [0.5, 0.6] (≈0.10 at [0.3, 0.4]); ≈0 above 0.8. (b): x = Likelihood Ratio cut, −1 to 1; y = S/√B, 0 to 1.4; blue points joined by a black line in steps of 0.1. Value 1.0 at cut −1, a broad plateau ≈1.17–1.25, maximum ≈1.28 at cut −0.2 (marked by a red vertical and a red horizontal line), then falling: ≈1.08 at 0.4–0.5, ≈0.82 at 0.6, ≈0.65 at 0.7, ≈0.08 at 0.8, 0 at 0.9 and 1.0.

**[note]** (figure pass) The y axis of (b) is labelled S/√B but is clearly normalised (1.0 at the loosest cut, whereas the absolute values in Table 1 are 15.89–22.01); the caption does not state the normalisation. The maximum ≈1.28 is relative to the loosest-cut point (which presumably already includes the fixed ΔToF cut), so it need not equal the 22.01/15.89 = 1.385 gain over the basic selection.

**[source issue]** (figure pass, minor) The y-axis label of (a) is misspelled "Probabilty(R)/0.10".

#### 4.2. Systematic uncertainties

Sources on the muon-ID efficiency, for all three methods: (i) signal and background fit models in data; (ii) the muon $p_T$ smearing in MC. For the Likelihood Ratio method also (iii) how the PDF ratios are built and (iv) how they are extracted.

- Fit-model variations (Sec. 4.1): **about 5–7%** in data.
- MC $p_T$ smearing: mean and width of the smearing function varied so that the reconstructed $J/\psi$ mass mean and width move within ±1σ.
- Likelihood Ratio only: background PDFs from **sideband vs. same-sign** data; central-region ratios from **bin-to-bin interpolation vs. a third-order polynomial fit**; side-region fit varied by **±1σ** (blue dot-dashed lines in Fig. 3). The maximum deviation from the average of these variants is the PDF-ratio uncertainty.

Total systematic uncertainty across $p_T$ bins, data (MC):

| Method | Data | MC |
|---|---|---|
| Straight cuts | 0.9 – 8.7% | 0.6 – 2.6% |
| N−1 iteration | 0.9 – 10.5% | 0.2 – 2.1% |
| Likelihood Ratio | 0.6 – 15.4% | 0.5 – 3.8% |

[note] Table compiled from the prose.

### 5. Results

Performance is evaluated on $J/\psi\to\mu^+\mu^-$ with the selection applied to the **probed (subleading)** muon (Fig. 5). All three methods cut the **background by more than 65%** while keeping a relatively high $J/\psi$ efficiency. Efficiencies relative to the basic selection (Sec. 3.2) vs. $p_T$ are in Fig. 6. **Plateau efficiency ($p_T > 3$ GeV): about 90% for the Likelihood Ratio method, about 80% for the others.** For the $J/\psi$ signal the Likelihood Ratio method gives an overall efficiency of **about 80%** and improves the significance by a **factor of 1.38**. Full comparison in Table 1.

**[source issue]** (unit) "pT > 3 GeV" in Sec. 5 should be GeV/$c$ (the abstract has GeV/$c$).

![Fig. 5](assets/huang2016-mtd-muon-id/fig5.jpg)

**Fig. 5.** Dimuon mass spectra for the various muon-ID methods. Solid curves: Gaussian + fourth-order-polynomial fits; dashed lines: fitted background. Solid circles: basic selection on both muons ("μ_tagged & μ_probed matched to MTD"); open boxes / open circles / solid triangles: subleading muon selected with straight cuts / N−1 iteration / Likelihood Ratio. (0.04 GeV/$c^2$ bins, 2.4–3.8 GeV/$c^2$.)

*Figure description (from the image):* Single panel. x = $M_{\mu\mu}$ [GeV/$c^2$], ≈2.3–3.9 (labels 2.4–3.8); y = Events/0.04 [GeV/$c^2$], ×10$^3$, 0 to 3 (labels 0, 1, 2, 3). Four data sets, all black filled markers: circles "μ$^{tagged}$ & μ$^{probed}$ matched to MTD", squares "μ$^{probed}$ with Straight Cuts", stars "μ$^{probed}$ with N-1 Iteration", triangles "μ$^{probed}$ with Likelihood Ratio"; each with a red solid fit curve and a red dashed background curve. Basic selection: continuum ≈2.0×10$^3$ at 2.3 falling to ≈0.55×10$^3$ at 3.9, J/ψ peak ≈1.7×10$^3$ at ≈3.1. After the probe-muon cuts the continuum drops to about a third or less: Likelihood Ratio ≈0.63→0.2 ×10$^3$ with peak ≈0.77×10$^3$; Straight Cuts ≈0.5→0.15 ×10$^3$, peak ≈0.6×10$^3$; N-1 Iteration ≈0.35→0.12 ×10$^3$, peak ≈0.5×10$^3$; all peaks at ≈3.08–3.10 GeV/$c^2$. No fit numbers are printed on the plot.

**[source issue]** (figure pass) The caption gives open boxes / open circles / solid triangles for straight cuts / N−1 iteration / Likelihood Ratio, but the publisher image uses filled squares / filled stars / filled triangles (legend and points). **[note]** The axis spans ≈2.3–3.9 GeV/$c^2$, slightly wider than the "2.4–3.8" in the caption paraphrase above (those are the tick labels).

**Table 1.** Performance of the three muon identification methods. $\varepsilon_{signal}$ and $1-\varepsilon_{bkgd.}$ are the muon-ID efficiency and background rejection relative to the basic selection; first error statistical, second systematic.

| | Basic selection | Straight cut | N-1 iteration | Likelihood Ratio |
|---|---|---|---|---|
| Signal | 1656 ± 143 ± 114 | 1006 ± 67 ± 20 | 891 ± 58 ± 12 | 1346 ± 74 ± 22 |
| Background | 10861 ± 104 ± 317 | 2682 ± 52 ± 80 | 1962 ± 44 ± 58 | 3743 ± 61 ± 79 |
| $S/B$ | 0.15 ± 0.01 ± 0.01 | 0.38 ± 0.03 ± 0.01 | 0.45 ± 0.03 ± 0.01 | 0.36 ± 0.02 ± 0.01 |
| $S/\sqrt{B}$ | 15.89 ± 1.37 ± 1.12 | 19.44 ± 1.31 ± 0.49 | 20.11 ± 1.33 ± 0.39 | 22.01 ± 1.23 ± 0.43 |
| $\varepsilon_{signal}$ | — | 0.61 ± 0.01 ± 0.05 | 0.54 ± 0.01 ± 0.05 | 0.81 ± 0.01 ± 0.07 |
| $1-\varepsilon_{bkgd.}$ | — | 0.75 ± 0.01 ± 0.02 | 0.82 ± 0.01 ± 0.01 | 0.66 ± 0.01 ± 0.01 |
| $\varepsilon_{signal}^{MC}$ | — | 0.62 ± 0.01 ± 0.03 | 0.51 ± 0.01 ± 0.03 | 0.80 ± 0.01 ± 0.04 |

**Recomputation of derived quantities from the yields** (my arithmetic; ✓ = agrees with the table at the quoted precision):

| | Basic | Straight cut | N−1 iteration | Likelihood Ratio |
|---|---|---|---|---|
| $S/B$ | 1656/10861 = 0.1525 → 0.15 ✓ | 1006/2682 = 0.3751 → 0.38 ✓ | 891/1962 = 0.4541 → 0.45 ✓ | 1346/3743 = 0.3596 → 0.36 ✓ |
| $S/\sqrt{B}$ | 1656/104.22 = 15.89 ✓ | 1006/51.79 = 19.43 (table 19.44; rounding of yields) ✓ | 891/44.29 = 20.12 (table 20.11; rounding) ✓ | 1346/61.18 = 22.00 (table 22.01; rounding) ✓ |
| $\varepsilon_{signal}$ = S/1656 | — | 0.6075 → 0.61 ✓ | 0.5380 → 0.54 ✓ | 0.8128 → 0.81 ✓ |
| $1-\varepsilon_{bkgd.}$ = 1 − B/10861 | — | 1 − 0.2469 = 0.7531 → 0.75 ✓ | 1 − 0.1806 = 0.8194 → 0.82 ✓ | 1 − 0.3446 = 0.6554 → 0.66 ✓ |
| significance gain vs basic | — | 19.44/15.89 = 1.22 | 20.11/15.89 = 1.27 | 22.01/15.89 = 1.385 (text: "1.38") ✓ |
| stat. error on B vs $\sqrt{B}$ | 104.2 → 104 ✓ | 51.8 → 52 ✓ | 44.3 → 44 ✓ | 61.2 → 61 ✓ |

**[note]** The "by more than 65%" background reduction holds for all three methods (75%, 82%, 65.5%), but the Likelihood Ratio value is only marginally above 65%. N−1 iteration gives the best $S/B$ (0.45) and the lowest signal efficiency (0.54); the Likelihood Ratio gives the best $S/\sqrt{B}$ (22.01) with the highest efficiency (0.81). Data and MC signal efficiencies agree within uncertainties for all three methods.

![Fig. 6](assets/huang2016-mtd-muon-id/fig6.jpg)

**Fig. 6.** Muon identification efficiency vs. muon $p_T$ ($p_T^\mu$, 0–10 GeV/$c$) for straight cuts, N−1 iteration and Likelihood Ratio. Blue solid points: MC; red open circles: data. Error bars: total (stat. + syst.) uncertainty; shaded boxes: systematic uncertainty.

*Figure description (from the image):* Three panels (Straight Cuts top-left, N-1 Iteration top-right, Likelihood Ratio bottom-left) and a legend (bottom-right). x = $p_T^\mu$ [GeV/$c$], 0–10; y = Muon ID efficiency, 0–1.2. Blue filled circles "MC" with blue hatched boxes, red filled circles "Data" with red hatched boxes; legend also shows "Total errors" (vertical bars) and "Systematic errors" (hatching). MC bins: 0.5 GeV/$c$ wide from 1 to 5, then 5–10; data bins: 1–1.5, 1.5–2, 2–3.5, 3.5–10. Readings (≈, from the axes): Straight Cuts — MC 0.50, 0.64, 0.75, 0.79, 0.81, 0.84, 0.79, 0.82, 0.81; data 0.43, 0.65, 0.75, 0.67. N-1 Iteration — MC 0.39, 0.53, 0.69, 0.79, 0.83, 0.84, 0.83, 0.86, 0.83; data 0.43, 0.52, 0.72, 0.72. Likelihood Ratio — MC 0.70, 0.83, 0.93, 0.95, 0.97, 0.97, 0.97, 0.97, 0.97; data 0.66, 0.77, 0.90, 0.92 (3.5–10 bin error ≈±0.08). All curves rise steeply below ≈2.5 GeV/$c$ and are flat above ≈3 GeV/$c$.

**[source issue]** (figure pass) Data are drawn as red filled circles (legend and points), not "red open circles" as in the caption; the systematic uncertainties are hatched bands rather than shaded boxes.

**[note]** (figure pass) The "about 80%" plateau quoted in Sec. 5 for straight cuts and N−1 iteration matches the MC; the data plateaus are lower (≈0.67 and ≈0.72 for $p_T$ = 3.5–10 GeV/$c$). For the Likelihood Ratio the data plateau is ≈0.90–0.92 and the MC ≈0.97.

When the Likelihood Ratio selection is applied to **both** muons, the $J/\psi$ significance increases **by a factor of 2 ($S/\sqrt{B} = 31.89$)**, and light-meson peaks (ρ, ω, φ) become clearer (Fig. 7), enabling studies of light mesons, heavy quarkonium and the dimuon continuum at STAR.

Check: 31.89/15.89 = 2.007 ✓ ("factor of 2").

![Fig. 7](assets/huang2016-mtd-muon-id/fig7.jpg)

**Fig. 7.** Dimuon mass spectrum (0–6 GeV/$c^2$) with both muons selected by the Likelihood Ratio method, compared with the basic selection scaled by 0.1. The $J/\psi$ significance is strongly enhanced and the light mesons (ρ/ω, φ labelled) are clearly visible.

*Figure description (from the image):* Single panel. x = $M_{\mu\mu}$ [GeV/$c^2$], 0–6.5 (labels 0–6); y = Counts/Bin, ×10$^3$, 0 to ≈32 (labels 0, 10, 20, 30). Red open circles "Basic selection (×0.1)", black filled circles "Likelihood Ratio"; same variable binning as Fig. 1 (the red points equal Fig. 1's opposite-sign points ×0.1, e.g. first bin ≈11.2×10$^3$ vs ≈0.112×10$^6$). Peaks labelled "ρ,ω" (black up to ≈27×10$^3$ near 0.75–0.78 GeV/$c^2$), "φ" (black spike ≈20.6×10$^3$ at ≈1.02) and "J/ψ" (black ≈14.7×10$^3$ at ≈3.1 vs ≈4.7×10$^3$ for basic ×0.1). Below ≈0.5 GeV/$c^2$ the Likelihood Ratio spectrum lies under the scaled basic one (first bin ≈7.8 vs ≈11.2 ×10$^3$); above ≈1.1 GeV/$c^2$ its continuum lies slightly above it (e.g. ≈10.8 vs ≈9.4 ×10$^3$ at ≈1.3). Both fall to ≈0 above 5 GeV/$c^2$. The J/ψ peak stands out far more clearly over the continuum after the Likelihood Ratio selection.

### 6. Conclusion

The MTD is a newly installed STAR detector dedicated to triggering on and identifying muons with a low kinematic threshold. Three muon-ID methods were evaluated — straight cut, N−1 iteration and Likelihood Ratio. The paper states that each "can reduce the background level by more than 65% and keep the $J/\psi$ signals with about 60% of efficiency". With this capability the MTD opens heavy-ion physics with muons, especially quarkonia, at STAR.

**[source issue]** The conclusion's "about 60%" for each method is inconsistent with Table 1 and Sec. 5: $\varepsilon_{signal}$ = 0.61 (straight), 0.54 (N−1), **0.81** (Likelihood Ratio; Sec. 5 says "about 80%"). Only the two cut-based methods are near 60%.

### 7. Acknowledgments

Thanks to the STAR Collaboration, the RACF at BNL and National Cheng Kung University; support from the U.S. DOE Office of Science (contract No. de-sc0012704) and the Goldhaber Fellowship at BNL; L. Ruan acknowledges a DOE Office of Science Early Career Award; Gene Van Buren (BNL) thanked for proofreading.

---

## Checks (answered from the arXiv v3 PDF; rechecked against the publisher PDF)

**(a) Backleg thickness, radius, wording.** "They are 61 cm thick at a radius of 363 cm corresponding to about 5 absorption lengths." 30 backleg bars, flux return outside the coil, Ref. [11]. The word used is **"absorption lengths"** (not "interaction lengths"). [note] 61 cm Fe ≈ 3.6 $\lambda_I$.

**(b) MTD radius and coverage.** "installed at a radius of about 403 cm, and cover about 45% in azimuth within |η| < 0.5 [5]". Installation 10% / 63% / 100% in the 2012 / 2013 / 2014 runs.

**(c) "About 60%" in the conclusion.** Yes — the conclusion says each method keeps the $J/\psi$ signal "with about 60% of efficiency". Table 1: 0.61 ± 0.01 ± 0.05 (straight), 0.54 ± 0.01 ± 0.05 (N−1), 0.81 ± 0.01 ± 0.07 (Likelihood Ratio). True for straight cuts, roughly for N−1, **false for the Likelihood Ratio** (≈81%, and Sec. 5 itself says ~80%). [source issue]

**(d) Abstract "factor of 2".** It is the **both-muon** result: Sec. 5 says that applying the Likelihood Ratio selection "on both muons" enhances the significance by a factor of 2 ($S/\sqrt{B} = 31.89$ vs 15.89 → 2.007). The single-muon (probe only) Likelihood Ratio gain is 1.38 (22.01/15.89). The abstract does not specify both-muon.

**(e) Fig. 3 caption vs text.** Yes: the caption reads "The PDF ratios of Δz, Δy × q, ΔToF, and nσπ variables", while the text says "only three variables, Δy × q, Δz and nσπ, are used to calculate the R value" with ΔToF cut fixed from N−1, and describes Fig. 3 as showing ratios for those three only. The figure has three panels. [source issue]

**(f) MTD timing/position resolution.** Sec. 2: "As shown in cosmic ray data, the timing resolution of the MTD is ∼100 ps and the spatial resolutions are ∼1-2 cm in both rφ and z directions [12]" — Ref. [12] = C. Yang et al., NIM A 762 (2014) 1–6 (the MTD cosmic-ray calibration paper, see [yang2014-mtd-cosmic-calibration-note](yang2014-mtd-cosmic-calibration-note.md)). [note] The MTD timing is not simulated in MC (Sec. 4.1), so ΔToF is data-driven only.

---

## References (detector-relevant, as printed in the paper)

- [1] K.H. Ackermann et al. (STAR), Nucl. Instr. and Meth. A 499 (2003) 624 — STAR detector overview.
- [5] L. Ruan et al., J. Phys. G 36 (2009) 095001 — MTD proposal/design (see [ruan2009-mtd-concept-note](ruan2009-mtd-concept-note.md)).
- [6] Z. Xu, BNL LDRD project 07-007; Beam Test Experiment (T963) at Fermilab — MTD R&D.
- [7] ATLAS Collaboration, Eur. Phys. J. C 74 (2014) 3130 — muon reconstruction/ID performance.
- [8] CMS Collaboration, J. of Instr. 7 (2012), 10 — printed this way; [note] presumably JINST 7 (2012) P10002 (CMS muon reconstruction performance).
- [9] LHCb Collaboration, J. of Instr. 10 (2013), 10 — **[source issue]** volume 10 of JINST is 2015, not 2013; presumably JINST 8 (2013) P10020 (LHCb muon identification performance).
- [10] M. Anderson et al. (STAR), Nucl. Instr. and Meth. A 499 (2003) 659 — STAR TPC.
- [11] F. Bergsma et al. (STAR), Nucl. Instr. and Meth. A 499 (2003) 633 — STAR magnet.
- [12] C. Yang et al., Nucl. Instr. and Meth. A 762 (2014) 1–6 — MTD cosmic-ray calibration and performance.
- [13] CERN Program Library Long Writeup W5013 — GEANT3.
- [14] W. Zha et al., arXiv:1506.08985 (2015) — global fit of $J/\psi$ cross sections used for MC weighting.

(Physics references not listed: [2] Gyulassy nucl-th/0403032; [3] Matsui & Satz PLB 178 (1986) 416; [4] Mocsy EPJC 61 (2009) 705.)
