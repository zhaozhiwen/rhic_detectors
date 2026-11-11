---
title: "Ruan 2009 — Perspectives of a mid-rapidity dimuon program at the RHIC: a novel and compact muon telescope detector (full-content paraphrase)"
type: raw-source
source_type: paper
authors: "L. Ruan et al., 22 authors"
journal: "J. Phys. G: Nucl. Part. Phys. 36 (2009) 095001"
doi: 10.1088/0954-3899/36/9/095001
arxiv: "0904.3774"
captured_via: "Route 2 — arXiv HTML (v4, LaTeXML) for text, structure and figures; text checked line by line against the publisher PDF (IOPscience has no HTML full text for this article)"
captured_date: 2026-11-05
captured_as: full-content paraphrase
figures: "11 (vision descriptions added 2026-11-05)"
vision_model: "general-purpose subagent (session model, not recorded), 2026-11-05"
---

# Ruan et al. 2009: the mid-rapidity MTD concept for STAR (J. Phys. G 36, 095001)

- **Citation:** L. Ruan, G. Lin, Z. Xu, K. Asselta, H. F. Chen, W. Christie, H. J. Crawford, J. Engelage, G. Eppley, T. J. Hallman, C. Li, J. Liu, W. J. Llope, R. Majka, T. Nussbaum, J. Scheblein, M. Shao, R. Soja, Y. Sun, Z. Tang, X. Wang and Y. Wang, "Perspectives of a mid-rapidity dimuon program at the RHIC: a novel and compact muon telescope detector". Affiliations: BNL, Yale, USTC, UC Berkeley, Rice, Tsinghua. Contact: ruan@bnl.gov.
- **Journal ref + DOI:** J. Phys. G: Nucl. Part. Phys. **36** (2009) 095001 (15 pp). Received 30 April 2009, published 17 July 2009. doi:10.1088/0954-3899/36/9/095001
- **arXiv:** 0904.3774. The arXiv HTML is built from v4. The arXiv title is "Perspectives of a Midrapidity Dimuon Program at RHIC: A Novel and Compact Muon Telescope Detector".
- **PACS:** 25.75.Cj, 29.40.Cs (listed on arXiv only).
- **Route used:** **Route 2 (arXiv HTML)** for structure, figure placement and figures. The text was checked line by line against the publisher PDF.
  - Route 1 failed: the IOPscience article page (https://iopscience.iop.org/article/10.1088/0954-3899/36/9/095001) has **no HTML full text** for this 2009 article. It shows only the abstract, the reference list and a PDF link. IOP did serve the PDF through institutional access.
  - Route 2 used https://arxiv.org/html/0904.3774 (v4, LaTeXML). The full page text and all 11 figure PNGs were extracted.
  - The publisher PDF is authoritative. Wherever the HTML and the PDF differ, this note follows the PDF (see "HTML vs PDF discrepancies").
- **PDF backup:**
  - `assets/ruan2009-mtd-concept/source.pdf`: publisher PDF, 16 pages (an IOP cover page plus journal pp. 1–15), 2 060 374 bytes.
  - The arXiv PDF (latest version, 19 pages) was used for the number-by-number comparison but was not kept; only the publisher version is kept.
  - Figures: `assets/ruan2009-mtd-concept/fig1.png` … `fig11.png`, from the arXiv HTML (the publisher has no HTML figures), except `fig1.png`, which is the publisher-PDF extraction (see the Fig. 1 source issue). Each is a single image; no figure is split across several files.
- **Verification:** every number, range, table and inline formula below was checked against `pdftotext -layout` of the publisher PDF. Where pdftotext loses glyphs, the rendered PDF pages were inspected visually (journal pp. 4, 5, 7, 8, 9, 10, 11, 12). pdftotext silently drops ≳, ⩾, ⩽, ≃ and Δ in this PDF. For example, "|Δz| < 20 cm" comes out as "|z| < 20 cm", and "⩽10 Hz" comes out as "10". The arXiv PDF text was also compared number by number with the publisher text, and no numerical differences were found (the arXiv copy was not kept).
- The paper contains **no numbered (display) equations**. Inline formulas are given in LaTeX below.
- Figure descriptions were added by a separate figure pass that looked at the images.

---

## Full content

### Abstract
- The authors propose a large-area, cost-effective muon telescope detector (MTD) at mid-rapidity. It is intended for STAR and for next-generation detectors at a possible electron–ion collider.
- The design is built on large multi-gap resistive plate chambers with long readout strips ("long-MRPC").
- In cosmic-ray and beam tests, a long-MRPC reaches an intrinsic timing resolution of **60–70 ps** and a spatial resolution of **∼1 cm**.
- The prototype MTD at STAR shows that muons at transverse momenta of a few GeV/$c$ can be identified by combining three pieces of information:
  - track matching to the MTD;
  - TPC ionization energy loss;
  - time of flight.
- A **primary-to-secondary muon ratio better than 1/3** is achievable.
- Simulations are presented for:
  - the muon efficiency;
  - the $J/\psi$ signal-to-background ratio;
  - separating $\Upsilon$(1S) from 2S+3S;
  - the $e$–$\mu$ correlation from charm pairs in the RHIC environment.

### 1. Introduction

**What RHIC has shown so far** [1]. RHIC data show dense, rapidly thermalizing matter with three features:
1. initial energy densities far above the lattice-QCD critical values for QGP formation;
2. opacity to jets;
3. nearly ideal fluid flow, implying very short mean free paths, most probably established before hadron formation.

**The next goal** is to characterize this partonic matter: its color degrees of freedom and its equation of state.
- Color screening dissociates the quarkonium states at different temperatures, because their binding energies differ.
- Precise quarkonium $p_T$ spectra versus centrality, collision system and energy would therefore act as a QGP thermometer.
- A large-area mid-rapidity MTD would address open questions from the RHIC white papers [1, 2].

**Why muons.** Muons do not interact strongly, so they are penetrating probes of the QGP. A large-area detector that identifies few-GeV/$c$ muons at mid-rapidity gives access to [3]:
- dimuons from QGP thermal radiation;
- quarkonia and light vector mesons;
- possible quark/gluon correlations appearing as resonances in the QGP;
- Drell–Yan production;
- heavy flavour, through semi-leptonic decays to single muons.

**Why not electrons or photons.** Electrons and photons can reach some of the same physics, but they carry large backgrounds:
- hadron decays;
- $\pi^0$ and $\eta$ Dalitz decays;
- photon conversions in the detector material.

These backgrounds prevent effective triggering in central A+A collisions at mid-rapidity in STAR.

**Other advantages of muons.**
- $e$–$\mu$ correlations separate lepton-pair production from heavy-quark decays: $c+\bar c \to e+\mu(e)$ and $B\to e(\mu)+c\to e+\mu(e)$.
- Muons lose much less energy to bremsstrahlung in the material than electrons do. This gives excellent mass resolution for vector mesons and quarkonia.
- That resolution is essential to separate $\Upsilon$(1S) from (2S+3S). These states are predicted to melt at very different temperatures.

**Detector approach.**
- Conventional muon systems rely on tracking stations. This detector instead uses **<100 ps** timing and **∼1 cm** spatial resolution to identify few-GeV/$c$ muons [4].
- The MTD prototypes use MRPC technology with large modules, long strips and double-ended readout (long-MRPC).
- The same technology with small pads is already built and installed in STAR as the TOF [5].
- The paper covers:
  - the conceptual design;
  - R&D results (intrinsic timing and spatial resolution of the long-MRPC);
  - prototype performance at STAR;
  - muon ID and hadron rejection;
  - physics perspectives.

### 2. Simulation

The studies use the STAR detector [6]. Figure 1 shows the layout.

**TPC [7]**
- Inner field cage at **50 cm** and outer field cage at **200 cm** from the beam axis.
- **4 m** long.
- Covers $|\eta|<1.8$ and $2\pi$ in azimuth.
- $dE/dx$ is used for particle identification [8–10].

**TOF**
- MRPC-based [11], fully installed in 2009.
- Covers $2\pi$ in azimuth and **$-1<\eta<1$** at a radius of **∼220 cm**.
- Extends PID to $p_T\sim3$ GeV/$c$ for $p$ and $\bar p$ [12].

**BEMC**
- Sits outside the TOF radius.
- Covers **$-1<\eta<1$** uniformly and $2\pi$ in azimuth [13].

**Magnet**
- The TPC sits in a solenoidal field from the surrounding coils.
- The flux return is the magnet steel [14]. It is roughly cylindrical and consists of **30 flux return bars, four end rings and two pole tips**.
- Each return bar is **6.85 m** long, trapezoidal in cross-section and **60 cm thick**, with a **363 cm outer radius**. Its **width at the outer radius is 57 cm**.

![Fig. 1](assets/ruan2009-mtd-concept/fig1.png)

**Fig. 1.** Cut-away perspective view of STAR showing the inner detectors. The trigger barrel drawn here is to be fully replaced by the TOF in 2009. The figure is taken from [6].

*Figure description (from the image; publisher PDF version):* Single colour cut-away drawing of STAR on a black background, no axes. The octagonal magnet (blue) with its return-bar segments surrounds the detector; one quadrant is cut away to show, from outside in, the labelled "Coils", "Magnet", "E-M Calorimeter" (pale band), "Trigger Barrel", "Time Projection Chamber" (pink) and "Silicon Vertex Tracker" near the beam pipe. The end of the magnet shows the pole-tip/end-ring structure (green segmented disk) with purple elements, and a green ring at the beam axis. "Forward Time Projection Chamber" is labelled at the bottom, "Electronics Platforms" (multi-level decks with yellow railings) at left; a person stands at lower right for scale. No TOF or MTD is drawn (the trigger barrel is shown, as the caption says).

**[source issue]** The arXiv-HTML PNG of Fig. 1 is truncated: only the bottom strip survives. The embedded image `assets/ruan2009-mtd-concept/fig1.png` was extracted from the publisher PDF (page with Figure 1) with pdfimages; the truncated arXiv PNG was discarded.

**Full-event simulation (Fig. 2)**
- A full HIJING central Au+Au event was simulated with the full STAR geometry and complete material budget.
- The simulated muon detector (blue) covers the full return bars (green) within **$|\eta|<0.8$**. The gaps between bars are left uncovered.
- This acceptance corresponds to **56% of $2\pi$** in azimuth.
- Most particles stop before the BEMC. The few that escape, primary or secondary, come mainly through the gaps between return bars.

**[note]** Recompute of the coverage: $30\times57\ \text{cm}/(2\pi\times363\ \text{cm}) = 1710/2281 = 0.75$. So the bars' outer faces cover about **75%** of the azimuth at $r=363$ cm. The paper's 56% must therefore refer to the instrumented (detector) width, not the bar width. The paper does not explain the difference. 56% of $2\pi$ at $r=400$ cm corresponds to about 47 cm of active width per bar.

**Muon and pion efficiency [15]**
- For a muon with $p_T>2$ GeV/$c$ generated at the TPC center, the MTD detection efficiency including acceptance is about **40–50%**. For a pion it is **0.5–1%**.
- Method: TPC tracks are extrapolated to the MTD and must match the hit in both position and time of flight.
  - The hit-to-projection distance must be **within 4 cm**.
  - The timing difference must be **less than 400 ps**.
- The extrapolation is a simple helix. In reality the return bar has a field of **1.2 tesla**, while the TPC has **0.5 tesla**.

**Sources of fake muons**
- $\pi$ and $K$ misidentification comes mainly from decays to muons before absorption in the return bar. These daughter muons then cross the bars.
- Protons are suppressed by a much larger factor than pions and kaons.

**Fig. 3 summary**
- The MTD detects muons with $p_T\gtrsim2$ GeV/$c$ at about **45%**.
- **Less than 1%** of all hadrons are accepted, after weighting by the relative $\pi$, $K$, $p$ yields.
- From these simulations, a **rejection factor of 50–100** is possible while keeping an **efficient trigger (>80%) for prompt muons**.
- Further rejection can come from TPC tracking, TPC $dE/dx$ and TOF hit matching. These were studied with a prototype tray (Sections 4–5).
- Combining this muon efficiency with measured $J/\psi$ $p_T$ spectra [16] gives the $J/\psi$ efficiency versus $p_T$ in Fig. 9.

![Fig. 2](assets/ruan2009-mtd-concept/fig2.png)

**Fig. 2.** A full HIJING central Au+Au event simulated in STAR. TPC tracks are projected onto the plane transverse to the beam.

*Figure description (from the image):* Single panel, transverse (r–φ) event display with no axes, numbers or labels. Red: a dense mass of TPC tracks filling the central disk, with many tracks and short stubs leaking outward. Green: some tracks inside the TPC, plus the outlines of the trapezoidal return bars in the outer ring. Dark-blue dots crowd a magenta ring at the TPC outer edge. Blue dashed arcs sit just outside the green bars (the simulated MTD), and black and red circles mark the outermost boundary. Visible feature: almost all tracks stop inside the inner ring. Only a few red tracks reach the bar region, mostly through the gaps between bars, as the text says.

**[note]** A pixel count of the blue MTD arcs finds about 29–30 segments covering about 72–75% of the azimuth (limited by the image resolution). This matches the ~75% bar-face coverage estimated earlier in this note, not the paper's 56%.

![Fig. 3](assets/ruan2009-mtd-concept/fig3.png)

**Fig. 3.** Top: muon efficiency. Bottom: misidentification probabilities for $\pi$, $K$ and $p$, versus $p_T$. The muon inefficiency comes mainly from the MTD acceptance, printed as "(56)" in the journal and "(56%)" on arXiv.

*Figure description (from the image):* Two stacked panels sharing the x axis $p_T$ (GeV/c), 0–15, in 1 GeV/c bins with horizontal bars giving the bin width. **Top:** y = "MTD detection efficiency", 0–0.6, for μ (filled black circles). The efficiency is 0 at 0.5, ≈0.20 at 1.5, ≈0.39 at 2.5 and ≈0.44 at 3.5 GeV/c. It then stays flat at ≈0.40–0.44 up to 14.5 GeV/c; the lowest plateau point is ≈0.40 at 10.5. **Bottom:** y axis 0–0.025 with no axis title. Legend: π (open black circles), K (open red crosses), p (open blue triangles). π values lie at ≈0.004–0.011, starting at 1.5 GeV/c. K values lie at ≈0.003–0.0185, starting at 2.5 GeV/c; the highest point is ≈0.0185 at 4.5. p values are ≈0.0003 at 5.5–6.5 GeV/c and ≈0.001–0.005 above 7 GeV/c, with nothing plotted below 5 GeV/c. All read by eye. Main feature: a muon plateau of ≈0.4–0.44 above 3 GeV/c, against hadron probabilities around 1% (K highest, p lowest).

**[note]** The bottom panel has no y-axis title in the image. The muon plateau reads 0.40–0.44, at or slightly below the text's "about 45%". The 2.5 GeV/c bin (≈0.39) is just under 40%.

**[source issue]** The published Fig. 3 caption reads "acceptance of the MTD (56)". The % sign is missing; arXiv has "(56%)". This was confirmed on the rendered PDF page.

### 3. The R&D results for the MTD

**Long-MRPC module design**
- Two stacks of resistive glass plates, giving **ten uniform gas gaps** in total.
- Each gap is **250 μm** wide.
- HV is applied to electrodes on the outer surfaces of the outer plates of each stack.
- Avalanches are read out by **six copper pickup strips**, each **870 × 25 mm²**.

**Operating point and performance** (cosmic-ray and beam tests)
- Operated at **12.6 kV** with **95% C₂H₂F₄ + 5% iso-butane** at **1 atm**.
- For **12.5 < HV < 13.0 kV**:
  - efficiency **>95%**;
  - timing resolution about **60–70 ps**.
- Spatial resolution along the long strip is about **0.6–1 cm** in the same tests.
- This meets the needs of a large-area muon detector. Construction details are in [17].

**[note]** The strip pitch is 25 mm, so six strips span 150 mm across the module.

### 4. Performances of a prototype MTD

**Prototype placement**
- **2007 run (200 GeV Au+Au):** covered **$\pi/60$** in azimuth and **$-0.25<\eta<0.25$**, at a radius of **∼400 cm**.
- **2008 run (200 GeV d+Au and p+p):** moved to **$-0.5<\eta<0$** at the same radius.
- It held **two long-MRPC modules**.
- It sat outside the return bars, which act as the hadron absorber. Each bar "amounts to five interaction lengths".
- Fig. 4 shows the location and geometry.

**Readout chain**
- Analog signals [18] went to STAR trigger digitizer boards [19] for amplitude and timing.
- Each board has an **8-bit ADC**.
- Discriminator outputs, with **30 mV** thresholds, fed a **time-to-analog converter (TAC)** gated by the RHIC clock. The TAC output went to another digitizer channel.
- ADC and TAC values went through the trigger distribution and processing system for the level-0 decision [19].
- The **L0** decision is made in **<1.5 μs** (printed "1.5 us") from all fast detector information. It starts digitization of slow detectors such as the TPC.

**Trigger condition**
- No time-difference or other matching was required in the trigger, unlike the simulation in Section 2.
- A valid hit needed non-zero, non-overflow ADC and TAC values within the 8-bit range.
- The prototype successfully triggered DAQ when **at least one strip** had a valid hit.
- Table 1 gives the trigger rates, luminosities and event counts.

**2009 tray**
- A further prototype tray was installed for the 2009 run, with the **same electronics as the STAR TOF** [5], to improve timing.
- The TOF electronics have a **25 ps time bin**, small compared with the detector resolution.
- On-board digitization removes the degradation from long cables.
- A significant offline timing improvement is expected.

**[note]** Recompute: $\pi/60$ rad at 400 cm is 20.9 cm of arc. In $z=r\sinh\eta$ at $r=400$ cm:
- $-0.25<\eta<0.25$ gives $|z|<101$ cm, a 2.0 m span. This is consistent with two modules with 87 cm strips laid along $z$.
- $-0.5<\eta<0$ gives $-208<z<0$ cm.

![Fig. 4](assets/ruan2009-mtd-concept/fig4.png)

**Fig. 4.** Position of the MTD prototype in STAR, installed **400 cm** radially from the interaction point during **2006–2008**.

*Figure description (from the image):* Single-panel black-line engineering drawing: an end view (r–φ) of one STAR sector, with no physics axes. From left to right it shows:
- the spoked TPC end wheel with a box labelled "SVT READOUT BOX";
- the arc of BEMC modules ("BEMC MODULE", dimension 12.135" [30.82cm]);
- the trapezoidal return bars ("BACKLEG");
- rectangular tray outlines on the outer faces of the backlegs, with a dark tray labelled "CTB";
- at lower right, a support structure with pipes whose small labels are unreadable.

Dimensions printed on the drawing:
- 24.000" [60.96cm] across the backleg (radial thickness);
- 22.500" [57.1?cm] (the last digit of the cm value is blurred) and 22.520" [57.20cm] at the outer face and tray;
- 17.4?5" [44.34cm] (blurred);
- 8.622" [21.90cm];
- "COIL I.D.= 208.582"–208.742"" and "COIL O.D.= 235.290"–235.818"";
- a long arc dimension "18.02…" (the rest is unreadable).

Title block: "MUON TELESCOPE DETECTOR", "FEB. 27, 2007", "MTD010.DWG", "REV. C", "JAS". Footer: "D:\Dwgs\MTD\MTD010C.dwg, 7/12/2007 2:46:56 PM". The small rotated text on the tray next to the CTB is unreadable.

**[note]** The 400 cm radius in the caption is not printed on the drawing. The backleg dimensions 60.96 cm thick and 57.1–57.2 cm wide match the text's 60 cm and 57 cm. The drawing is dated Feb. 27, 2007, consistent with the 2007 run.

**[source issue]** The Fig. 4 caption says 2006–2008, but the text describes only the 2007 and 2008 runs.

**Table 1.** Trigger rates, sampled luminosities, recorded events and matched hits with TPC tracks at $p_T>1.5$ GeV/$c$, for the prototype MTD in 2007 and 2008.

| Beam species | Interaction rate (Hz) | Trigger rate (Hz) | Sampled luminosity | Recorded events (M) | Matched hits |
|---|---|---|---|---|---|
| Au+Au | 20 k | 0.5–2 | 270 μb⁻¹ | 0.31 | 7k |
| d+Au | 100 k | 0.5–2 | 29 nb⁻¹ | 1.6 | 78 k |
| p+p | 300 k | 0.5–2 | 404 nb⁻¹ | 0.56 | 8k |

**Track matching (Fig. 5)**
- Fig. 5 shows the azimuthal distribution of TPC tracks extrapolated to 400 cm in triggered d+Au events, versus $p_T$.
- There is a clear yield enhancement at the MTD's azimuth, so offline TPC tracks do match long-MRPC hits.
- Track extrapolation gives one position. The time difference between the two strip ends gives a second position along the strip.
- The MTD sits behind the backleg steel, so multiple hits are not an issue.

**The $\Delta z$ distribution (Fig. 5 inset)**
- $\Delta z$ is the difference between the two positions along the beam direction $z$. It is fitted with a double Gaussian.
- For $p_T>2$ GeV/$c$ tracks, the narrow Gaussian has **σ ≈ 10 cm**; the other is much broader.
- Within the match window **$|\Delta z|<20$ cm**, the narrow-to-broad yield ratio is **∼2**. Table 1 gives the matched-hit totals in this window for $p_T>1.5$ GeV/$c$.
- In GEANT, muons of $p_T\sim2.5$ GeV/$c$ from the TPC center produce a Gaussian with **σ = 9 cm** in $z$ at the MTD after crossing all the material. Pions give a much broader distribution because of strong interactions.

![Fig. 5](assets/ruan2009-mtd-concept/fig5.png)

**Fig. 5.** Azimuthal distribution versus $p_T$ of d+Au tracks extrapolated from the TPC to $r=400$ cm.
- The arrow marks the prototype tray's azimuth.
- Inset: the $\Delta z$ distribution, where $\Delta z = z_{\rm trackhits}-z_{\rm rawhits}$.
  - $z_{\rm trackhits}$ is the extrapolated TPC track position.
  - $z_{\rm rawhits}$ is the position from the two-end time difference along the hit strip.
- Inset labels: "μ/h ≈ 2 at |Δz|<20", "$p_T$ > 2 GeV/c", "200 GeV d+Au".

*Figure description (from the image):* Main panel: a 2D colour map of φ (rad), −3 to 3, versus $p_T$ (GeV/c), 0–15. The colour scale bar on the right has no numbers. The track population starts sharply at $p_T$≈0.8–0.9 GeV/c and covers all φ, falling off by $p_T$≈3–5 GeV/c. A narrow red/yellow band at φ≈−2.6 rad, marked by a red arrow on the y axis, is the hottest region at $p_T$≈1–2 GeV/c and extends out to $p_T$≈8–10 GeV/c with sparse entries beyond. The straight cutoff at $p_T$≈4.8 GeV/c for φ ≳ −1.1 rad is where the inset's white pad covers the map; it is not a physics edge. **Inset:** y = "Counts", 0–2500 (ticks 0, 500, …, 2500); x = $z_{\rm trackhits}-z_{\rm rawhits}$ (cm), −80 to 80. It shows a black data histogram (peak ≈2800 at 0), a black total fit, a red "Muon" Gaussian (peak ≈2.1k at ≈0; a pixel estimate of FWHM ≈25 cm, i.e. σ≈10 cm) and a blue dashed "Hadron" broad Gaussian (max ≈600, centred near −5 to −15 cm). Inset labels: "μ/h ≈ 2 at |Δz|<20" (no unit printed), "$p_T$ > 2 GeV/c", "200 GeV d+Au".

**[note]** In the inset the broad hadron Gaussian is visibly centred at negative Δz (about −5 to −15 cm), while the muon Gaussian is centred near 0. The text does not mention this offset.

**[note]** σ(narrow) ≈ 10 cm in data versus 9 cm simulated for muons ✓ consistent. Almost all of this width is multiple scattering in the material. It is about 10× the intrinsic ∼1 cm strip resolution.

### 5. Muon identification capability and hadron rejection

**dE/dx separation**
- For $p_T>2$ GeV/$c$, a muon's $dE/dx$ is **∼3–4%** higher than a pion's [20].
- The TPC $dE/dx$ resolution is **∼8%** [7], so the μ–π separation is about **half a sigma**. The μ–K separation is about **two sigma**.
- **[note]** 3–4% / 8% = 0.38–0.5σ ✓.

**Energy loss in the return bar**
- The paper states: "The energy loss due to multiple scattering in the return bar will cause an energy loss of **∼1.2 GeV** for muons at **2 < $p_T$ < 10 GeV/$c$**", with negligible change in velocity.
- Hadrons instead start a hadronic shower. They lose a lot of energy, slow down, and reach the MTD later.

**[source issue]** Multiple scattering does not cause energy loss; a muon's energy loss in steel is ionization (collisional). A rough check gives
$$
\langle dE/dx\rangle_{\rm Fe}\approx 1.5\text{–}1.6\ \text{MeV cm}^2/\text{g} \times 7.87\ \text{g/cm}^3 \approx 12\text{–}13\ \text{MeV/cm}.
$$
Over 60 cm of iron at normal incidence this is about **0.7–0.8 GeV**. A ∼1.2 GeV figure is plausible for the full path: oblique tracks, plus the coil, BEMC and other material in front of the MTD. The sentence, however, attributes it to "the return bar" only.

**Muon-enriched selection**
- Selecting high-velocity, large-$dE/dx$ tracks markedly reduced the hadron background and raised the narrow-to-broad ratio.
- This is consistent with a muon-dominated narrow Gaussian and a hadron-dominated broad one.
- Within **$|\Delta z|<20$ cm**, combining track matching, $dE/dx$ and velocity gives a **muon purity >80%**.

**Timing in Au+Au**
- The average long-MRPC timing resolution for the two modules was **∼300 ps**.
- The start time came from two identical VPDs, each **5.4 m** from the nominal collision point along the beamline [21].
- After subtracting the start resolution (**∼160 ps**) and the material contribution (**∼100 ps at $p_T=2.5$ GeV/$c$**), the MTD resolution is **200–300 ps**. This is worse than in the cosmic and beam tests.
- The reason is that the trigger readout electronics were not designed for precise timing.
- The full detector will use **TOF electronics**, quoted as having "a timing resolution of **25 ps**". These are proven low-cost and reliable for recording timing and sending it to STAR DAQ. They can be used for the MTD without design changes.

**[note]** Recompute: $\sqrt{300^2-160^2-100^2}=\sqrt{54400}=233$ ps ✓ (within 200–300 ps).

**[note]** "25 ps" is called a *time bin width* in Section 4 and a *timing resolution* here. The bin width is the correct reading.

![Fig. 6](assets/ruan2009-mtd-concept/fig6.png)

**Fig. 6.** Reconstructed $K^0_S$ candidates in two samples:
- Top: candidates not associated with MTD-triggered particles. Legend: "Outside of the MTD", ($p_T^1$ or $p_T^2$) > 2 GeV/c.
- Bottom: candidates with at least one daughter pion associated with the MTD-triggered particle. The dot-dashed line is the $K^0_S$ yield projected under the assumption that all MTD-associated particles come from pion decays.

*Figure description (from the image):* Two stacked panels sharing the x axis "$K^0_S\to\pi^+\pi^-$ invariant mass (GeV/$c^2$)", 0.25–0.8; y = "Counts". Each shows data as black points with error bars, a black "total" fit, a red "$K^0_S$ signal" Gaussian and a blue dashed "background". **Top** ("Outside of the MTD", "($p_T^1$ or $p_T^2$) >2 GeV/c"; y 0–400): data peak ≈385 at ≈0.49; total fit ≈378; signal ≈302 at ≈0.50; background ≈78 near the peak. **Bottom** ("MTD matched tracks"; y 0–150): data ≈71 and ≈69 at ≈0.49–0.51; total fit ≈63; signal ≈55; background ≈8–9. A black dot-dashed "projection if all from π" peaks at ≈147. All peak values were read by eye. Main feature: a clear $K^0_S$ peak at ≈0.5 GeV/$c^2$ in both samples. In the MTD-matched sample the fitted signal is well below the all-from-π projection.

**[note]** The readings give signal/projection ≈55/147 ≈ 0.37. This is consistent with the text's 30–40% of muon candidates coming from pion decay.

**Pion contamination from $K^0_S$**
- Pions from $K^0_S\to\pi^+\pi^-$ are identified to measure the fraction of muon candidates from pion decay. The $K^0_S$ is reconstructed from the V0 decay topology.
- Fig. 6 compares:
  - top: raw $K^0_S$ from pairs at azimuths away from the MTD;
  - bottom: raw $K^0_S$ with at least one daughter matched to an MTD hit;
  - dot-dashed: the projection if every MTD-associated particle came from pion decay.
- Result: **secondary muons from pion decay make up 30–40% of all muon candidates.**

**Kaon contamination and TOF coincidence**
- The rest of the background to prompt muons is secondary muons from kaon decay. This can be attacked with the K–μ $dE/dx$ difference.
- A cut $n\sigma_\pi>0$ removes part of the kaon-decay products. Here $n\sigma_\pi$ is the measured $dE/dx$ normalized to the expected pion value [8].
- In 2008 p+p MTD-triggered data, requiring a valid TOF hit in the same TPC sector **reduced the inclusive muon yield by a factor of 2**.

**Table 2.** Fraction of TPC tracks matched to a non-zero EMC energy (> MIP):
- (A): from non-MTD sectors;
- (B): with non-zero EMC tower energy (> MIP) and an MTD hit.

"Non-zero EMC energy" means **> 0.75 GeV above pedestal**.

| $p_T$ (GeV/$c$) | EMC & non-MTD (A) | EMC & MTD (B) |
|---|---|---|
| 1.5–2 | (2.21 ± 0.03)% | (0.18 ± 0.02)% |
| 2–3 | (3.67 ± 0.07)% | (0.30 ± 0.04)% |
| 3–4 | (5.89 ± 0.22)% | (0.34 ± 0.10)% |
| 4–6 | (7.92 ± 0.50)% | (0.65 ± 0.24)% |

**Hadron-rejection check with the BEMC**
- STAR uses several detectors (TPC, TOF, MTD) to improve muon ID, and others to check the hadron rejection.
- One check uses BEMC hadronic showers. These measure the fraction of inclusive muon candidates that come from hadrons showering in the EMC and still penetrating the absorbers.
- Only a few percent of hadrons shower and deposit more than MIP energy in the BEMC.
- Table 2 gives the fraction above 0.75 GeV with and without an associated MTD hit.
- Requiring an MTD muon candidate reduces BEMC hadronic showers by a factor of **⩾10**.
- Electrons are only about **0.1%** of inclusive hadrons in 2008 200 GeV p+p at STAR [24]. So all BEMC showers with a TPC track and no MTD hit can be taken as hadrons.
- With the MTD requirement, the hadron share falls from **≃100% to ⩽10%**, and muons (prompt plus decay) rise to **⩾90%** of what remains.
- So particles reaching the BEMC in coincidence with a valid MTD hit are mostly muons. These muons, however, come mainly from π and K decays in the first **2 m** of STAR.

**[note]** Recompute A/B ratios: 2.21/0.18 = 12.3; 3.67/0.30 = 12.2; 5.89/0.34 = 17.3; 7.92/0.65 = 12.2. All are ✓ ⩾10.

**Prompt fraction from non-photonic electrons**
- Prompt muons come mainly from charm semi-leptonic decay. The muon yields are therefore compared with non-photonic electron yields in the same $p_T$ bin to estimate the π/K-decay contamination.
- Raw muon yields come from Gaussian fits to the $\Delta z$ distributions, with the narrow component taken as muons. The systematic uncertainty from fit range and parameter constraints is **about 20%**.
- Acceptance and efficiency come from simulation and are corrected for.
- Fig. 7 shows the ratio of raw yields $d^2N/(2\pi p_T\,dp_T\,dy)$ of inclusive muons, $(\mu^++\mu^-)/2$, to non-photonic electrons in 200 GeV d+Au at mid-rapidity, for several selections.
- Fig. 7 also shows the pion-decay contribution versus $p_T$ from the $K^0_S$ method. The non-photonic electron yields are from STAR [22].
- **With only the MTD-hit association, primary muons are 6–10% of inclusive muons.**
- Table 3 gives the primary-muon efficiency and S/B (primary versus π+K-decay secondary muons) for different $dE/dx$ cuts. With **$n\sigma_\pi>1$, S/B improves by a factor of 3**.

![Fig. 7](assets/ruan2009-mtd-concept/fig7.png)

**Fig. 7.**
- Top: fraction of detected muons that are prompt versus $p_T$, estimated from the ratio of non-photonic electrons to inclusive muons. Non-photonic electrons are those not from conversions, hadron decays or Dalitz decays.
  - Shown without a $dE/dx$ cut and with $n\sigma_\pi>0$ and $n\sigma_\pi>1$. The cuts are on TPC $dE/dx$ relative to the pion expectation, for the track projected to the MTD.
  - A muon's $dE/dx$ in this momentum range exceeds a pion's, so a tighter $n\sigma_\pi$ cut raises the prompt fraction.
- Bottom: the pion-decay contribution to the inclusive muon signal, from the MTD response to $K^0_S$ daughter pions. Y-axis labels: $e_{\rm nonphotonic}/\mu_{\rm inclusive}$ (top) and "pion contribution factor" (bottom).

*Figure description (from the image):* Two stacked panels sharing the x axis $p_T$ (GeV/c), about 1.5–7. **Top** ("200 GeV d+Au"): y = $e_{\rm nonphotonic}/\mu_{\rm inclusive}$, 0–0.5. Legend: "without dedx cut" (open black squares), "nσ_π>0" (filled magenta down-triangles), "nσ_π>1" (open red circles). Approximate values by eye:
- without cut: ≈0.08, 0.05, 0.07, 0.07, 0.08, 0.07, 0.06, 0.06 at $p_T$≈1.7, 1.9, 2.2, 2.7, 3.5, 4.5, 5.5, 6.5;
- nσ_π>0: ≈0.12, 0.09, 0.13, 0.15, 0.17, 0.19, 0.21 at $p_T$≈1.7–5.5;
- nσ_π>1: ≈0.18, 0.13, 0.23, 0.26, 0.33 at $p_T$≈1.7–3.5, with no points above 3.5.

**Bottom:** y = "pion contribution factor", 0–0.65, "without dedx cut" (open black squares). Values ≈0.22, 0.29, 0.51, 0.39, 0.43, 0.28 at $p_T$≈1.7, 1.9, 2.2, 2.7, 3.5, 4.5, with error bars of about ±0.06–0.14. Main feature: the ratio rises with a tighter nσ_π cut (roughly ×2–4 versus no cut), and the uncut ratio is flat at ≈0.05–0.08.

**[note]** The uncut points read ≈0.05–0.08, slightly lower than the text's "6–10%" primary fraction. The pion contribution factor spans ≈0.22–0.51 point by point, wider than the text's summary of 30–40%.

**Table 3.** Signal-to-background ratio and primary-muon selection efficiency for different conditions in 200 GeV d+Au. The S/B ratio depends on $p_T$.

| Selection criterion | Primary muon efficiency (%) | S/B ratio |
|---|---|---|
| Without cut | 100 | 1/15–1/9 |
| $n\sigma_\pi>0$ | 61 | 1/10–1/6 |
| $n\sigma_\pi>1$ | 26 | 1/6–1/3 |

**[note]** Recompute: (1/6–1/3)/(1/15–1/9) = 2.5–3 ✓ "factor of 3". The abstract's "primary/secondary better than 1/3" is the upper end of the $n\sigma_\pi>1$ row. It comes at only 26% primary-muon efficiency.

### 6. Trigger capability

**Full-detector size**
- The full MTD would cover **56%** of the TPC acceptance at **$|\eta|<0.8$**.
- With the prototype-tray design: **540 long-MRPC modules, 2160 read-out strips, 4320 read-out channels**. That is a factor of **5–6** fewer than the STAR TOF uses.
- With the same electronics, a full MTD would be very cost effective, comparable in scope to the smaller RHIC II upgrades.

**[note]** Derived counts:
- 4320 = 2 × 2160, i.e. double-ended readout ✓.
- 540/30 bars = 18 modules per bar.
- 2160/540 = **4 strips per module**. This is **inconsistent with the six strips per module** in Section 3 (see Checks (d)). The paper does not state strips per module for the full design.

**Table 4.** Trigger-rate reduction from requiring one or two MTD hits, for different 200 GeV systems with full MTD coverage. Column definitions:
- **L0:** single-hit L0 rate output from the MTD per collision event.
- **L2 with TOF:** single-hit rate reduction at L2 when a TOF hit is required near the muon-candidate path. Measured in p+p; only estimated for central Au+Au.
- **RHIC II Lumi:** RHIC II luminosity expressed as a collision rate.
- **Dimuon L2 rate:** dimuon trigger rate at L2, in Hz, at RHIC II.
- Values in parentheses come from simulations with a tighter timing cut, assuming the electronics give ∼100 ps resolution.

| Collision system | L0 | L2 with TOF | RHIC II Lumi (Hz) | Dimuon L2 rate (Hz) |
|---|---|---|---|---|
| Minbias Au+Au | 0.2 | – | | |
| 0–5% Au+Au | 0.5 (0.2) | ∼0.3 | 100 k | ∼500 (100) |
| 60–80% Au+Au | 0.03 | – | | |
| d+Au | 0.02 | – | | |
| p+p | 0.01 | 0.003 | 2 M | ⩽10 |

**Trigger-rate estimates**
- From the 2007 Au+Au prototype rate, the full-coverage single-hit L0 reduction would be **0.19** in minimum-bias Au+Au.
- The online enhancement for a dimuon trigger would therefore be **28**.
- **1 billion** minimum-bias Au+Au events correspond to **36 million** dimuon-triggered events. These would yield **5600 $J/\psi$** and **85 $\Upsilon$** in the dimuon channel.
- Table 4's L0 values were estimated from prototype trigger rates and enhancement factors: 2007 Au+Au, and 2008 d+Au and p+p. The table also shows the central-Au+Au dimuon capability.

**[note]** Recompute: $0.19^2=0.036$, and $1/0.036=27.7$ ✓ 28. $10^9/27.7=36$ M ✓. One plausible reading of the ∼500 Hz entry is 100 kHz × 5% (0–5% centrality) × (0.3)² = 450 Hz ≈ 500. Under the same simple product, the "(100)" and p+p "⩽10" (2 MHz × 0.003² = 18 Hz) are not reproduced exactly. The paper does not give the formula.

**MTD–TOF matching**
- In p+p, requiring a TOF hit in the same TPC sector cut the trigger rate by a **factor of 3**.
- The expected TOF hit position is obtained by extrapolating a valid MTD hit, using the east–west VPD time difference.
- TOF modules are arranged sequentially in $z$, so the ID of the TOF module with a hit gives an independent position.
- Fig. 8 (left) plots the extrapolated $z$ against the measured TOF module ID in 200 GeV p+p. The correlation is strong.
- Fig. 8 (right) shows the $z$ difference. A single Gaussian gives **σ ∼ 6 cm**.
- Combining MTD and TOF gives an **order of magnitude** of rejection. This greatly improves the dimuon-trigger efficiency in central 200 GeV Au+Au.

### 7. Physics perspectives with full coverage

This section explores the physics reach of a full-coverage mid-rapidity MTD in STAR. Two cases are highlighted:
- online triggering, used to measure $J/\psi$ elliptic flow and $R_{AA}$ at high $p_T$;
- improved momentum resolution, used to resolve $\Upsilon$(1S) from the excited states.

In addition, $e$–$\mu$ correlations separate lepton-pair production from heavy-quark decays: $c+\bar c\to e+\mu(e)$ and $B\to e(\mu)+c\to e+\mu(e)$.

![Fig. 8](assets/ruan2009-mtd-concept/fig8.png)

**Fig. 8.** 200 GeV p+p, 2008.
- Left: expected $z$ at the TOF versus the ID of the TOF module with a valid hit. Modules are sequential in $z$.
- Right: distribution of $z_{\rm expected}-z_{\rm TOFhits}$.
- $z_{\rm expected}$ comes from extrapolating a valid MTD hit using the east–west VPD time difference.
- Fit box: $\chi^2$/ndf = 9.584/8, Constant = 244.4 ± 8.0, Mean = −2.912 ± 0.168, Sigma = 5.882 ± 0.179 (cm).

*Figure description (from the image):* Two panels. **Left:** a 2D colour map of $z_{\rm expected}$ at TOF (cm), −160 to −20, versus "TOF Module Id", 0–32. The colour scale runs 0–18. It shows a tight, strong anticorrelation from module ≈4 (z≈−40 cm) to module ≈25 (z≈−155 cm). The hottest cells sit at modules ≈13–17, z≈−80 to −105 cm. **Right:** y = "Counts", 0–250; x = $z_{\rm expected}-z_{\rm TOFhits}$ (cm), −50 to 50. A black histogram peaks at ≈248 near −3 cm, with a Gaussian fit drawn over about −13 to +7 cm. Fit box: χ²/ndf 9.584 / 8; Constant 244.4 ± 8.0; Mean -2.912 ± 0.168; Sigma 5.882 ± 0.179. Small tails extend to about ±30 cm.

**[note]** All $z_{\rm expected}$ values are negative (−30 to −160 cm). This is consistent with the 2008 prototype position at −0.5<η<0. The fit box matches the caption values in this note.

![Fig. 9](assets/ruan2009-mtd-concept/fig9.png)

**Fig. 9.** $J/\psi$ efficiency, $\epsilon$ (acceptance × efficiency), versus $p_T$. Curves:
- "MTD |y|<0.5";
- "TOF+EMC |y|<0.5";
- "PHENIX EMC |y|<0.35 [PRC69]".

PHENIX [23] and STAR detect $J/\psi\to e^+e^-$ at mid-rapidity with several detectors combined with EM calorimeters.

*Figure description (from the image):* Single panel with a log y axis "ε (acceptance × efficiency)", 10⁻³ to 1, versus "J/ψ $p_T$ (GeV/c)", 0–10. - Solid black "MTD |y|<0.5" (label in red): ≈0.023 at $p_T$≈0.2, a minimum ≈0.014 at ≈1.1–1.3 GeV/c, then rising steadily to ≈0.14 at ≈9.8 GeV/c.
- Dotted horizontal "TOF+EMC |y|<0.5": flat at ≈0.4 across 0–10 GeV/c.
- Dot-dashed "PHENIX EMC |y|<0.35 [PRC69]": ≈0.004 at low $p_T$, a minimum ≈0.0017 at ≈3.3 GeV/c, ending at ≈0.0022 at ≈4.7 GeV/c.

Values were read with a pixel calibration of the log axis. Main feature: the MTD curve sits about 4–20× above PHENIX over 0–5 GeV/c and keeps rising with $p_T$.

**[note]** In the image the STAR TOF+EMC line (≈0.4) is above the MTD curve at all $p_T$. Fig. 9 alone therefore shows the MTD ε advantage only over PHENIX. The claimed advantage over STAR EMC+TOF is trigger rejection, which this plot does not show.

**Comparison with existing $J/\psi$ measurements (Fig. 9)**
- Both PHENIX and STAR measure mid-rapidity $J/\psi\to e^+e^-$, using EM calorimeters as trigger and electron identifier.
- Their limits differ:
  - STAR is limited by its ability to trigger on low-momentum electrons;
  - PHENIX by its lower efficiency × acceptance ($\epsilon$) [23].
- An MTD measuring $J/\psi\to\mu^+\mu^-$ would have much higher trigger rejection than STAR EMC+TOF, and larger acceptance than PHENIX. It would yield much larger $J/\psi$ samples than current RHIC setups.

![Fig. 10](assets/ruan2009-mtd-concept/fig10.png)

**Fig. 10.**
- Top: expected dimuon invariant mass from $J/\psi$ plus background in d+Au. Label "200 GeV d+Au J/ψ→μ⁺μ⁻", "S/B≈7".
- Bottom: dimuon mass from $\Upsilon$ decays at $0<p_T<5$ GeV/$c$, with curves for 1S+2S+3S, 1S, 2S and 3S. The states are separable.
- The background under the $\Upsilon$ is not simulated, because the small prototype did not reach high enough $p_T$.

*Figure description (from the image):* Two separate panels. **Top:** y = "Counts", 0–40; x = $\mu^+\mu^-$ invariant mass (GeV/$c^2$), 2.2–4. It shows a solid "J/ψ→μ⁺μ⁻" histogram and a dashed "background" histogram, with labels "200 GeV d+Au" and "S/B≈7". The J/ψ peak reaches ≈28.5 counts at ≈3.08–3.12 and spans ≈2.95–3.22 GeV/$c^2$. The background is flat at ≈1–4 counts per bin across the range. **Bottom:** y = "Counts", 0–160; x = $\mu^+\mu^-$ invariant mass (GeV/$c^2$), 8.5–11. Labels: "Υ→μ⁺μ⁻", "0<$p_T$<5 GeV/c". Legend: "1S+2S+3S" (black), "1S" (red dashed), "2S" (blue), "3S" (magenta). The 1S peaks at ≈162 counts at ≈9.4–9.45 GeV/$c^2$. The 2S peaks at ≈31 near 10.0 and the 3S at ≈17 near 10.3–10.35. The sum shows the 1S peak followed by a broad shoulder of ≈25–35 counts from ≈9.8 to ≈10.4 GeV/$c^2$. No background is drawn in the bottom panel.

**[note]** In the image the 1S is clearly separated from the excited states. The 2S and 3S, however, merge into one plateau in the 1S+2S+3S histogram and are not resolved from each other. "Separable" therefore applies to 1S versus 2S+3S.

![Fig. 11](assets/ruan2009-mtd-concept/fig11.png)

**Fig. 11.** Expected $e$–$\mu$ correlation from charm pairs and from random background in d+Au. The statistics correspond to **2 billion** minimum-bias d+Au collisions. Labels:
- "$c\bar c\to e\mu$";
- "background", "background II";
- "S/B≈2 ($m_{e\mu}>3$ GeV/$c^2$)";
- "$p_T(e\mu)<2$ GeV/c".

*Figure description (from the image):* Single panel with a log y axis "Counts", 10⁻² to ~5×10³, versus "eμ invariant mass (GeV/$c^2$)", 0–10. Legend: "$c\bar c\to e\mu$" (red crosses), "background" (solid black histogram), "background II" (dashed black histogram). Labels: "S/B≈2 ($m_{e\mu}$>3 GeV/$c^2$)", "200 GeV d+Au", "$p_T(e\mu)$<2 GeV/c". - The solid background peaks at ≈2.5×10³ near 1.4–1.6 GeV/$c^2$ and falls steeply. It drops to isolated bins of a few counts at 5–6 GeV/$c^2$, with nothing above ≈6.
- Background II has the same shape at about ¼ of the level (peak ≈6–7×10²).
- The red signal peaks at ≈2×10² around 2–2.5 GeV/$c^2$ and falls slowly. It crosses above the solid background at ≈3 GeV/$c^2$, sits at ≈10 for 5–6.5 GeV/$c^2$, and has points out to ≈9.7 GeV/$c^2$.

Main feature: the signal dominates the background above ≈3 GeV/$c^2$.

**[note]** In the image the dashed curve is labelled "background II". The ≈4× ratio between the solid and dashed curves matches the text's factor-4 background reduction.

**Dimuon and $e$–$\mu$ simulations**
- **$J/\psi$ (Fig. 10 top):** $J/\psi\to\mu^+\mu^-$ with **S/B = 7:1**. The background pairs are built from the measured inclusive muon yields of the previous sections.
- **$\Upsilon$ (Fig. 10 bottom):** the dimuon mass from $\Upsilon$ decays, simulated in STAR geometry. $\Upsilon$(1S), (2S) and (3S) are clearly separable in the dimuon channel. In the electron channel, bremsstrahlung in the material, including future inner-tracker upgrades, makes this hard.
- **$e$–$\mu$ (Fig. 11):**
  - Signal is shown as crosses. The background (solid line) is formed from random combinations of photonic electrons measured in d+Au [24] with the inclusive muons.
  - For charm pairs, **S/B = 2:1** when $m_{e\mu}>3$ GeV/$c^2$ and $p_T<2$ GeV/$c$.
  - Pairing photonic electrons with other TPC particles gives a **factor of 2** rejection. Associating inclusive muons with TOF hits gives **at least another factor of 2**.
  - Together these reduce the background by a **factor of 4** (dashed line), greatly improving the $e$–$\mu$ S/B.

**RHIC II projections** [25]
- Assumed delivered luminosity: **26 nb⁻¹** Au+Au and **300 pb⁻¹** p+p.
- Expected yields:
  - p+p: **169 k $J/\psi$** and **2500 $\Upsilon$**;
  - Au+Au: **630 k $J/\psi$** and **9300 $\Upsilon$**.
- These measurements are essential to understanding the QCD matter made at RHIC.

**[note]** Internal consistency of the Υ/J/ψ ratios:
- 85/5600 = 0.0152 (1 B min-bias);
- 2500/169k = 0.0148;
- 9300/630k = 0.0148.

All are ✓ consistent at about 1.5%.

### 8. Conclusions
- A large-area, cost-effective MTD is proposed for STAR and for future EIC-era detectors.
- Cosmic-ray and beam tests give a long-MRPC intrinsic timing resolution of **about 60–70 ps** and a spatial resolution **better than 1 cm**.
- The prototype tray successfully triggered STAR DAQ, and offline TPC tracks matched long-MRPC hits.
- A **muon purity >80%** is achievable.
- The primary-to-secondary muon ratio was studied and found to be of high quality for the RHIC quarkonium program.

### Acknowledgments
- Support came from the STAR Collaboration, the RCF at BNL and the BNL LDRD fund 07-007.
- Long-MRPC R&D at USTC was funded by NSFC (10775131).
- L. Ruan held the Goldhaber Distinguished Fellowship (Battelle Memorial Institute / Stony Brook).
- Z. Xu was supported in part by a PECASE Award.

---

## HTML vs PDF discrepancies (arXiv v4 HTML / arXiv PDF versus publisher PDF; the PDF wins)
1. **The LaTeXML HTML drops the leading number of several ranges.** All are correct in both PDFs:
   - TOF and BEMC: "−<η<1" instead of **−1<η<1**;
   - prototype 2007: "−<η<0.25" instead of **−0.25<η<0.25**;
   - prototype 2008: "−<η<0" instead of **−0.5<η<0**;
   - HV: "<HV<13.0 kV" instead of **12.5<HV<13.0 kV**;
   - muon energy loss: "<pT<10" instead of **2<pT<10**;
   - Fig. 10 caption: "<pT<5" instead of **0<pT<5**.
2. **The HTML author block is broken.** It shows only "Y. Wang, Tsinghua University" and a date of "August 24, 2026", which is a conversion artifact.
3. **Wording differences, arXiv versus journal.** None of these change any number.
   - "1.2 Telsa" (arXiv typo) versus "1.2 tesla".
   - "5 interaction lengths" versus "five interaction lengths".
   - "5.4 meter" versus "5.4 m".
   - Fig. 3 caption "(56%)" (arXiv) versus "(56)" (journal; % missing).
   - Fig. 11 caption "equavelant" (arXiv typo).
   - "In this report" versus "In this paper".
   - Table 3 header "primary muon efficiency" with % in the cells versus "(%)" in the header.
4. **pdftotext of the publisher PDF loses symbols.** It drops ≳, ⩾, ⩽, ≃ and Δ (e.g. "factor of 10", "100% to 10%", "|z|<20 cm", p+p dimuon "10"). The rendered pages show **⩾10**, **≃100% → ⩽10%**, **⩾90%**, **|Δz|<20 cm** and **⩽10 Hz**. The arXiv text agrees with the rendered PDF.
5. **Every number was cross-checked.** The publisher and arXiv-PDF number lists agree apart from page numbers, dates and reference ranges.

---

## Checks (answered from the publisher PDF)

**(a) TOF η coverage.**
- Written as **"−1 < η < 1"** (2π in azimuth, radius ∼220 cm). It is **not** |η|<0.9.
- The BEMC is also given as −1<η<1.
- The arXiv HTML shows "−<η<1" because of a rendering bug.

**(b) Energy lost by muons "in the return bar".**
- Exact wording: "The energy loss due to multiple scattering in the return bar will cause an energy loss of ∼1.2 GeV for muons at 2 < $p_T$ < 10 GeV/$c$ while the velocity change is negligible."
- Value: **∼1.2 GeV**. Momentum range: **2 < $p_T$ < 10 GeV/$c$**.
- The text refers to **the return bar only**, not all the material.
- It attributes the loss to **multiple scattering**, which is a **[source issue]**. Physically this is ionization loss; multiple scattering changes direction, not energy.
- 60 cm Fe at normal incidence gives about 0.7–0.8 GeV. ∼1.2 GeV fits better with all the material and oblique paths.

**(c) Hadron-rejection statements (Section 2, from the Fig. 3 simulation).** All three are simulation numbers, not measurements.
- **Simulation conditions:**
  - single tracks generated at the TPC center;
  - full STAR geometry;
  - simple helix extrapolation;
  - hit match within 4 cm and Δt < 400 ps;
  - MTD covering the full return bars within |η|<0.8 (56% of 2π).
- **"<1% hadrons":** "less than 1% of overall hadrons are accepted taking into account the relative yields of pions, kaons and protons". This is the combined acceptance × efficiency (Fig. 3 bottom), averaged over π, K and p with their relative yields. Per species, the π efficiency is 0.5–1% and protons are suppressed much more.
- **"Rejection factor 50–100":** "can be obtained based on the simulations shown in figure 3 while maintaining an efficient trigger (>80%) for prompt muons". This is the inverse of the hadron acceptance (1–2%).
- **">80% trigger efficiency":** not defined further. It cannot be the absolute muon efficiency, which is 45% including acceptance for $p_T\gtrsim2$ GeV/$c$. So it presumably means relative to the MTD-accepted prompt muons.
- **Do not confuse with "muon purity >80%".** That is a separate result in Section 5 and the Conclusions. It is measured in prototype data within |Δz|<20 cm, combining track matching, dE/dx and velocity.

**(d) Full-MTD counts.**
- The paper states "**540 long-MRPC modules, 2160 read-out strips and 4320 read-out channels**", a factor 5–6 fewer than the TOF, assuming "the similar design as for the prototype tray".
- **Strips per module are not stated.** 2160/540 = **4**, but Section 3 says each long-MRPC module is read out by **six** strips of 870 × 25 mm². This is an internal inconsistency.
- Channels = 2 × strips (double-ended readout).
- 540/30 = 18 modules per backleg (derived).

**(e) Backleg geometry and interaction lengths.**
- "The 6.85 m long flux return bars are trapezoidal in cross-section and **60 cm thick** with a **363 cm outer radius**. The **width at the outer radius** of the return bar is **57 cm**."
- 30 return bars in total.
- Section 4: the return bars "serve as a hadron absorber, **each of which amounts to five interaction lengths**" (arXiv: "5 interaction lengths").
- **[note]** 60 cm Fe / λ_I(Fe) = 16.8 cm gives about 3.6 λ_I. "Five interaction lengths" exceeds the steel alone and probably includes other material, which the paper does not say.

**(f) Field in the steel.**
- "the magnetic flux return bar has a magnetic field of **1.2 tesla** while the TPC has a **0.5 tesla** field".
- The simulation nevertheless used a simple helix extrapolation.

**(g) Signal propagation speed along the strips.**
- **None is stated.** The paper only says that the two-end time difference gives the position along the strip.
- It quotes a resolution of 0.6–1 cm in tests, ∼1 cm in the abstract, and "better than 1 cm" in the Conclusions.

**(h) MRPC plateau and prototype η ranges.**
- **Plateau:** "In the high-voltage range **12.5 < HV < 13.0 kV**, the efficiency is above **95%** and timing resolution is about **60–70 ps**". The operating point was 12.6 kV with 95% C₂H₂F₄ + 5% iso-butane at 1 atm.
- **2007 prototype (200 GeV Au+Au):** **−0.25 < η < 0.25**, π/60 in azimuth, r ∼ 400 cm.
- **2008 prototype (d+Au, p+p):** relocated to **−0.5 < η < 0** at the same radius.
- **Other prototype facts:** two long-MRPC modules; a further prototype tray with TOF electronics was installed for 2009.

---

## Other source issues spotted
- Fig. 3 caption reads "(56)" instead of "(56%)" (journal only).
- Fig. 4 caption says the prototype was installed "in 2006–2008", while the text discusses only the 2007 and 2008 runs.
- "25 ps" is called a time bin width (Section 4) and also a timing resolution (Section 5).
- Ref. [3] spells "Saltz H"; the author is H. Satz. Ref. [22] gives "Phys. Rev. Lett. 94 62301"; the article number is 062301.

---

## References (hardware-relevant subset, as printed)
- [5] STAR Time-of-Flight Proposal: http://www.star.bnl.gov/STAR/tof/publications/TOF_20040524.pdf
- [6] Ackermann K H et al 2003 Nucl. Instrum. Methods A 499 624 (STAR detector overview)
- [7] Anderson M et al 2003 Nucl. Instrum. Methods A 499 659 (STAR TPC)
- [8] Shao M et al 2006 Nucl. Instrum. Methods A 558 419 (TPC/TOF PID, $n\sigma$)
- [9] Bichsel H 2006 Nucl. Instrum. Methods A 562 154 (dE/dx)
- [10] Xu Y et al arXiv:0807.4303 (dE/dx PID)
- [11] Bonner B et al 2003 Nucl. Instrum. Methods A 508 181; Shao M et al 2002 Nucl. Instrum. Methods A 492 344; Wu J et al 2005 Nucl. Instrum. Methods A 538 243 (MRPC)
- [12] Adams J et al 2005 Phys. Lett. B 616 8 (TOF PID reach)
- [13] Beddo M et al 2003 Nucl. Instrum. Methods A 499 725 (BEMC)
- [14] Bergsma F et al 2003 Nucl. Instrum. Methods A 499 633 (STAR magnet)
- [15] Lin G (STAR) 2006, "A New Large-area Muon Telescope Detector at Mid-rapidity at RHIC", DNP 2006 talk, Nashville, 25–28 Oct.
- [17] Sun Y et al 2008 Nucl. Instrum. Methods A 593 307 (long-MRPC construction and tests)
- [18] Llope W J et al 2008 Nucl. Instrum. Methods A 596 430 (analog signals / front end)
- [19] Bieser F S et al 2003 Nucl. Instrum. Methods A 499 766 (STAR trigger)
- [21] Llope W J et al 2004 Nucl. Instrum. Methods A 522 252 (VPD / pVPD start detector)
- [4] Xu Z, BNL LDRD project 07-007; Beam Test Experiment (T963) at Fermilab
- Physics references used for comparisons: [16] Tang Z QM2008, J. Phys. G 35 104135 (arXiv:0804.4846) and Abelev B I et al arXiv:0904.0439; [20] Eidelman S et al 2004 PLB 592 1 (PDG); [22] Adams J et al 2005 PRL 94 062301, Abelev B I et al 2007 PRL 98 192301; [23] Adler S S et al 2004 PRC 69 014901; [24] Jin F SQM2008, arXiv:0901.0693; [25] Frawley A D, Ullrich T, Vogt R 2008 Phys. Rep. 462 125.
