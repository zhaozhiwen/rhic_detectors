---
title: "Wu 2007 — A barrel TOF for STAR at RHIC (full-content paraphrase)"
type: raw-source
source_type: paper
authors: "J. Wu, M. Xu (USTC), for the STAR Collaboration"
journal: "J. Phys. G: Nucl. Part. Phys. 34 (2007) S729–S732 (Quark Matter 2006 proceedings)"
doi: "10.1088/0954-3899/34/8/S83"
arxiv: none
captured_via: "Route 3 — publisher PDF only (IOPscience page has abstract only; no arXiv version), fetched in Chrome via JLab institutional access; text from pdftotext -layout, symbols/table/figures checked on 200 dpi renders; figures cropped from 200 dpi renders"
captured_date: 2026-11-05
captured_as: full-content paraphrase
figures: "2 (vision descriptions added 2026-11-05)"
vision_model: "general-purpose subagent (session model, not recorded), 2026-11-05"
---

# A barrel TOF for STAR at RHIC — reading note

- **Citation:** J. Wu and M. Xu (for the STAR Collaboration), "A barrel TOF for STAR at RHIC". Both authors: Department of Modern Physics, University of Science and Technology of China (USTC), Hefei 230026, China. Contact: wujian@ustc.edu.cn. (The author list is only these two names plus the STAR Collaboration. The member list is "at the end of this issue".)
- **Journal ref:** J. Phys. G: Nucl. Part. Phys. **34** (2007) S729–S732 (J. Phys. G vol. 34, no. 8, the Quark Matter 2006 proceedings issue). Received 10 Jan 2007, published 12 Jul 2007.
- **DOI:** [10.1088/0954-3899/34/8/S83](https://doi.org/10.1088/0954-3899/34/8/S83). Found with a Crossref title search and confirmed on the IOPscience article page.
- **arXiv ID:** none known (the IOP page and Crossref list none).
- **Route used:** Route 3 (PDF only). Route 1 failed because the IOPscience page for this 2007 article has only the abstract, author and affiliation block, dates and a "PDF" link. It has no HTML full text, figures or references (the article-body container holds about 1 kB of abstract text). Route 2 did not apply because there is no arXiv version. The publisher PDF (5 pages: an IOP cover page plus pp. S729–S732) was fetched in Chrome through the JLab institutional access. Text came from `pdftotext -layout`. I checked equations, symbols, the table and the figures on 200-dpi renders of the pages.
- **PDF backup:** `assets/wu2007-star-barrel-tof/source.pdf` (316 923 bytes).
- **Figures:** cropped from 200-dpi page renders (`pdftoppm -r 200`) into `assets/wu2007-star-barrel-tof/fig1.png` (from p. S730) and `fig2.png` (from p. S731). I looked at each crop to confirm it holds the right figure.
- **Verification:** I checked every number, unit, symbol, the caption equation, Table 1 and the reference list against `pdftotext -layout` of the PDF. Where pdftotext dropped symbol-font glyphs, I used the rendered pages. The glyphs it dropped: "π − Ξ" printed as "π −", "Λ⁰" printed as "0", and "di-Ω" printed as "di-". The rendered page decides these. HTML vs PDF: the HTML has only the abstract, which matches the PDF abstract word for word. The only difference is formatting ("(forSTAR Collaboration)" spacing, and $D_s^+$ written as "D+s").
- **Figure descriptions:** Figure descriptions were added by a separate figure pass that looked at the images.

> **[note] Scope warning.** This is a 4-page conference proceeding, mostly about physics. It gives **no** MRPC construction details: no gap count or gap size, no glass type, thickness or resistivity, no pad size, no electronics, no tray or module mechanics, no channel count and no total tray count. The only hardware facts are gas mixtures, HV, timing and efficiency numbers, and the TOFr tray's coverage and radius. They are all reproduced below. For construction details see refs [1] (STAR TOF proposal), [2] (Shao 2002, NIM A 492 344) and [7] (Wu 2005, NIM A 538 243).

---

## Abstract (paraphrase)

MRPC-based time-of-flight prototypes have run successfully in STAR for several years, so a full barrel TOF is being built and is meant to start taking data in late 2008. Combined with the other STAR subsystems, it will widen particle identification (PID). That will let STAR pull the most information out of soft-physics observables event by event. It will also improve signal-to-noise in charm-hadron reconstruction ($D^0$, $D^+$, $D_s^+$, $J/\psi$), which makes systematic studies of charm thermalization and charm-meson flow possible. The paper shows the physics results from the prototypes and what the full TOF is expected to achieve.

---

## Full content

### 1. Introduction

- STAR TOF R&D using the **multi-gap resistive plate chamber (MRPC)** began in **2000**.
- The proposed full barrel TOF covers **$\eta < 1$** (as printed) and **$2\pi$ in azimuth**. It is meant to extend STAR's PID, which until then came from the TPC (dE/dx) and was limited to low momentum.
  - **[source issue]** The coverage is printed as "$\eta < 1$". It should be $|\eta| < 1$, since the barrel is symmetric about $\eta = 0$ and the prototype tray covers $-1<\eta<0$.
- The MRPC can reach a time resolution below 100 ps and a high detection efficiency (**95%**) for minimum-ionizing particles.
  - **[source issue]** The text reads "sub-one 100 ps time resolution", which is garbled. The meaning is "sub-100 ps".
- The full barrel TOF is said to be essential for several key measurements that could not be done without it.
- The STAR TOF project is a joint programme of **ten US and six Chinese institutions**. Construction and commissioning were scheduled to finish by **fall 2008** [1].

### 2. The prototype TOF – TOFr

**Beam test of the final MRPC design (CERN PS T10) [2]:**

| Item | Value (as stated) |
|---|---|
| Test beam | CERN PS, T10 beam line |
| Gas mixture | 90% C$_2$H$_2$F$_4$ + 5% iso-butane + 5% SF$_6$ |
| Intrinsic time resolution (after slewing and start corrections, several chambers) | **50–60 ps** |
| Detection efficiency | **> 95%** over a wide high-voltage range |

- These figures meet the STAR physics requirements.
- More recent tests covered control of MRPC operating conditions, **rate capability** and **ageing** [3–5] (two USTC PhD theses and one master's thesis, all 2006). The paper gives **no numbers** from them. They are cited as assurance for mass production and for running in the STAR environment.

**TOFr prototype tray in STAR:**

| Item | Value (as stated) |
|---|---|
| Name | TOFr tray (STAR TOF prototype based on the USTC-designed MRPCs) |
| Pre-installation test | BNL AGS radiation area |
| Installed | fall 2002; taking data since RHIC Run III |
| Azimuthal coverage | $\pi/30$ |
| Pseudorapidity coverage | $-1 < \eta < 0$ |
| Radius | 210 cm |
| MRPCs per tray | 28 (partly instrumented in the 2003, 2004 and 2005 runs) |
| Operating HV | 14 kV |
| Gas | 95% C$_2$H$_2$F$_4$ + 5% iso-butane (no SF$_6$), at 1 atm |
| Start detector | two identical pseudo-vertex position detectors (pVPD), each 5.4 m from the TPC centre along the beam line [6] |
| Start-time resolution at $\sqrt{s_{NN}} = 200$ GeV (set by forward multiplicity) | about 140 ps (p+p), 85 ps (d+Au), 25 ps (Au+Au) |
| Stop-time resolution (after detailed calibration with a pure pion sample [7]) | about 85 ps |

- **[note]** Derived geometry (my calculation, not in the paper): $\pi/30$ rad $= 6^\circ$, an arc of $210\,\text{cm}\times\pi/30 \approx 22.0$ cm at $R = 210$ cm ✓. The range $-1<\eta<0$ at $R = 210$ cm spans $|z| \le R\sinh 1 = 210\times1.1752 \approx 246.8$ cm ✓. A full $2\pi$ ring of such trays needs $2\pi/(\pi/30) = 60$ trays per $\eta$ half, so 120 trays for $|\eta|<1$ ✓. **The paper itself never gives the total tray count.**
- **[note]** The paper does not say whether the 85 ps "stop" resolution includes the start term. If the 85 ps start (d+Au) and 85 ps stop resolutions are independent, the total in d+Au would be $\sqrt{85^2+85^2}\approx 120$ ps ✓ (arithmetic only; the paper does not quote a total).
- **[note]** Note the gas difference: the beam-test gas had 5% SF$_6$, while the TOFr in STAR ran without SF$_6$ (95/5).

**PID performance (Fig. 1).** With this timing, TOFr extends PID a long way. In 200 GeV d+Au, $\pi$/K separation reaches $p_T \sim 1.6$ GeV/$c$ and proton/meson separation reaches $\sim 3.0$ GeV/$c$ (left panel of Fig. 1). Hadron PID in Au+Au with TOFr was reported in [8].

The inset of Fig. 1 plots the mass squared computed from momentum and velocity (equation as given in the Fig. 1 caption; the paper does not number it):

$$
m^2 = p^2\left(\frac{1}{\beta^2} - 1\right)
$$

![Fig. 1](assets/wu2007-star-barrel-tof/fig1.png)

**Fig. 1.** Left: inverse velocity $1/\beta$ vs momentum $p$ from 200 GeV d+Au collisions (MRPC-TOFr). The inset shows $m^2 = p^2(1/\beta^2-1)$ for $1.2 < p_T < 1.4$ GeV/$c$, with $\pi$, K and p peaks. Right: electron identification using $\beta$ from TOFr together with dE/dx from the TPC. Panel (a) is dE/dx vs $p$ from the TPC alone. Panel (b) adds the cut $|1/\beta - 1| < 0.03$, after which the electron band stands clearly apart from the hadrons.

*Figure description (from the image):* Two parts side by side. **Left:** colour-scale 2D histogram (z-scale not shown) of y = "Inversed velocity 1/β" (as printed) vs x = "Particle momentum p (GeV/c)"; x ticks 0–3.5 in steps of 0.5, axis to about 3.7; y ticks labelled 1, 1.5, 2 (top edge at 2; lower edge unlabelled, about 0.6 by tick spacing). Label in the panel: "MRPC-TOFr d+Au @ 200 GeV". Bands labelled *e* (flat at 1/β = 1), π (red core, rising to about 1.3 at the lowest p), *K* and *p*; data start at p ≈ 0.15–0.2 GeV/c. Thin overlaid lines follow the K band (green) and the p band (dark blue); the K and p bands leave the top (1/β = 2) at p ≈ 0.28 and ≈ 0.54 GeV/c; all bands merge toward 1/β = 1 at high p. **Inset:** "Counts" (ticks 0, 500, 1000) vs "Mass² (GeV/c²)" (ticks 0, 0.5, 1; axis about −0.5 to 1.5), black line histogram, label "1.2<p_T/(GeV/c)<1.4". Peaks: π at about 0.02 (height about 1300), K at about 0.25 (height about 250, with a low-side shoulder), p at about 0.87 (height about 180); the three peaks are clearly separated. **Right:** two stacked panels sharing x = "Particle momentum p (GeV/c)", ticks 0–3 in steps of 0.5. (a) y = "dE/dx (keV/cm)", ticks 2–6: a dense red/yellow band at about 2.5 keV/cm for p ≈ 0.2–1 GeV/c flattening to about 2.7 at higher p, two steep unlabelled bands rising past 6 keV/cm at p below about 0.3 and 0.55 GeV/c, and a weaker band around 3–4 keV/cm at low p that runs into the main band. (b) y = "Energy loss" (no unit printed), ticks 2–6; labels "TOFr d+Au @ 200 GeV" and "|1/β−1|<0.03". The steep bands are gone; an upper band at about 3–4 at low p (orange spot near p ≈ 0.2) is separated from a lower band at about 2.5 (red core at p ≈ 0.5–0.9 GeV/c) by a solid black curve running from about 2.3 at p ≈ 0.15 to about 3.35 at p = 3 GeV/c. The two bands are clearly apart below about 1.5 GeV/c and come together above that.

- **[note]** The black curve in (b) is not explained in the caption or text (presumably the electron selection line). Panel (b)'s y-axis reads "Energy loss" with no unit, while (a) reads "dE/dx (keV/cm)" on the same scale. Neither right-hand panel is labelled "TPC"; the caption gives that.
- **[note]** In (b) the lower band still has entries down to p ≈ 0.2 GeV/c, below the ≈ 0.57 GeV/c pion threshold computed in the note above. The image does not show why; finite 1/β resolution would let some slower pions pass the cut.

**Electron identification.** Besides separating hadrons, TOFr identifies electrons when its velocity $\beta$ is combined with TPC dE/dx. With the TPC alone (Fig. 1 right, upper panel), the electron band crosses the hadron bands, so electrons are hard to pick out. A TOFr velocity cut

$$
\left|\frac{1}{\beta} - 1\right| < 0.03
$$

removes slow hadrons strongly, and the electron band then sits clearly apart (lower panel). The hadron rejection power is about **$10^5$ at $p_T < 1$ GeV/$c$** [8].

- **[note]** Check (my calculation): a hadron of mass $m$ passes the cut once $p > m/\sqrt{1.03^2-1} = m/0.2468$. That gives $p > 0.566$ GeV/$c$ for $\pi$, $p > 2.00$ GeV/$c$ for K and $p > 3.80$ GeV/$c$ for p ✓. So the cut removes kaons and protons in the plotted range but lets pions through above about 0.57 GeV/$c$. Above that point the electron/pion separation in panel (b) comes from the TPC dE/dx band gap.
- **[note]** Check (my calculation): at $p = 1.6$ GeV/$c$, $\Delta(1/\beta)_{K-\pi} = \sqrt{1+(0.4937/1.6)^2} - \sqrt{1+(0.1396/1.6)^2} = 1.0465 - 1.0038 = 0.0427$. With a flight path of about 2.1 m ($\approx 7.0$ ns for $\beta=1$), that is a time difference of about 300 ps, roughly $2.5\sigma$ for a total resolution of about 120 ps ✓. This fits the quoted $\pi$/K limit of about 1.6 GeV/$c$ (I used the radius as the flight path; the real path is longer at $\eta \ne 0$).

### 3. Physics results achieved and expected

**Achieved with the single TOFr tray:**
- Run III d+Au: identified-particle spectra up to intermediate $p_T$, and the first observation of the identified-particle "Cronin effect" with TOFr [9].
- TOFr + TPC: the first STAR measurement of the non-photonic electron spectrum in d+Au and an extracted total charm cross section at RHIC [10].
- Runs IV and V: identified-particle spectra and elliptic flow in heavy-ion collisions [11–13].
- Charm cross section in Au+Au from a similar non-photonic-electron analysis [14].
- These results were published and presented at major conferences.

**Expected with the full barrel TOF:**
- Much lower integrated luminosity needed for multi-strange hadrons, open charm and other resonances.
- Large- and small-scale correlations and fluctuations.
- Electron ID for electromagnetic probes: inclusive leptons and di-lepton pairs.
- A search for exotic states such as the di-$\Omega$ (pdftotext drops the $\Omega$; it is clear on the rendered page).
- **Fig. 2:** using TOF together with TPC suppresses $\phi$ background about **four times** better than the TPC alone.
  - **[note]** Check against the figure: the peak $S/(S+B)$ is about 0.056 for $K_{TOF}+K_{TPC}$ and about 0.014 for $K_{TPC}+K_{TPC}$, a ratio of about 4.0 ✓ (values read off the plot).

![Fig. 2](assets/wu2007-star-barrel-tof/fig2.png)

**Fig. 2.** $\phi$ background suppression with the TOF: $S/(S+B)$ vs $K^+K^-$ invariant mass $M_{inv}$ (1.00–1.04 GeV/$c^2$), Au+Au 200 GeV Run IV, $1.0<p_T<4.0$ GeV/$c$, STAR Preliminary. $K_{TOF}+K_{TPC}$ means one $\phi$-daughter kaon is identified by the TPC and the other by the TOF. $K_{TPC}+K_{TPC}$ means both are identified by the TPC.

*Figure description (from the image):* Single panel. y = "Ratio S/(S+B)", ticks 0–0.08 in steps of 0.01; x = "M_inv (GeV/c²)", ticks 1–1.04 in steps of 0.005. Labels: "STAR PRELIMINARY" (blue), "AuAu 200GeV RunIV", "1.0<p_T<4.0GeV/c". Legend: open blue squares = "K_TOF+K_TPC", filled red squares = "K_TPC+K_TPC". Blue points are every 0.002 GeV/c² with horizontal bars (no vertical error bars visible) and a smooth blue fitted peak curve; red points are every 0.001 GeV/c², with no curve and no visible error bars. Both show a φ peak at M_inv ≈ 1.019–1.020 GeV/c². The blue peak point is at about 0.056 (curve maximum about 0.057); the red peak is about 0.014 (values read off the plot, not printed). The FWHM of the blue curve is about 0.007 GeV/c² (about 1.016 to 1.023). In the tails, blue goes from about 0.0035 at 1.002 to about 0.0015 at 1.04, and red stays at about 0.001 or below.

**Table 1.** Physics program at STAR with a full barrel TOF. (Symbols checked on the rendered page; pdftotext dropped Ξ and Λ.)

| Measurement | Physics goal |
|---|---|
| All particle (especially multi-strange particle $v_2$) | Fix the partonic collectivity parameters |
| Fluctuation/correlation studies with PID | Understand the nature of possible phase transition |
| Away-side jet fragmentation yields, spectra | Search for chiral and $U_A(1)$ symmetry restoration |
| Yields, spectra of high-mass resonances | Map out resonance production from RHIC |
| Unlike-particle (e.g. $\pi - \Xi$) correlations | Spatial & temporal distributions of hadrons |
| Charmed hadron flow & yield ratios | Charm collectivity & thermalization of light quarks |
| D,B-meson spectra at high $p_T$ | Probe partonic medium, nature of parton interactions |
| Lepton & di-lepton invariant mass spectra | Study possible in-medium modification of hadrons |
| $e^+e^-$ pair production in UPC | Strong field QED effects |
| $\Lambda^0$ longitudinal polarization correlations | CP violation search |

**Schedule / system layout (all the paper gives):**
- A **four-tray** system was to be installed in STAR soon, and **48 more trays** the following year.
- Full construction and commissioning by **fall 2008**, with data taking with the full barrel TOF hoped for in the **2008–2009 Au–Au full-energy runs**.
- **[note]** 4 + 48 = 52 trays is an intermediate stage, not the full barrel (which takes 120 trays at $\pi/30$ each, as derived above). The paper gives no channel count, modules per production tray, readout electronics, pad geometry or radius for the production system. The only radius given is TOFr's 210 cm.

### Acknowledgments (paraphrase)
The authors thank the STAR TOF group. Funding: NSFC grants 10275060, 10475071 and 10610286, and the CAS Knowledge Innovation Project grant KJCX2-YW-A14.

---

## Source issues collected
- **[source issue]** Coverage printed as "$\eta < 1$". It should be $|\eta| < 1$.
- **[source issue]** "sub-one 100 ps time resolution" is garbled. It means sub-100 ps.
- **[source issue]** The running head on even pages reads "J Wu an M Xu" (a typo for "and").
- **[source issue]** It is unclear whether the 85 ps "stop time resolution" is the TOFr-only term or the total. Taken literally, it is the stop side only.

---

## Checks

**(a) Signal propagation speed along readout strips/pads.** **Not stated.** The paper gives no readout geometry (pads or strips) and no propagation velocity.

**(b) Glass type, thickness, resistivity and rate capability.** **Not stated.** No glass type, thickness, resistivity, gap number or gap width is given. Rate capability and ageing are only mentioned as studied in [3–5] (USTC theses, 2006), with **no numbers**. The operating conditions that are given: beam-test gas 90% C$_2$H$_2$F$_4$ / 5% iso-butane / 5% SF$_6$; TOFr in STAR at 14 kV with 95% C$_2$H$_2$F$_4$ / 5% iso-butane at 1 atm.

**(c) Intrinsic timing and efficiency.**
- Beam test (CERN PS T10, final MRPC design, 90/5/5 gas): intrinsic time resolution **50–60 ps** after slewing and start corrections, for several chambers. Efficiency **> 95%** over a wide HV range.
- Introduction: the MRPC gives sub-100 ps resolution and about **95%** efficiency for MIPs.
- In STAR (TOFr, 14 kV, 95/5 gas): stop-time resolution **about 85 ps** after calibration with pure pions. The pVPD start resolution is about **140 ps (p+p), 85 ps (d+Au), 25 ps (Au+Au)** at 200 GeV. No in-STAR efficiency number is given.

**(d) System channel count and coverage.**
- Channel count: **not stated**.
- Full barrel: **$|\eta| < 1$** (printed as "$\eta<1$") and **$2\pi$** in $\phi$. Radius for the full system not stated.
- TOFr prototype: $\pi/30$ in $\phi$, $-1<\eta<0$, **R = 210 cm**, **28 MRPCs**.
- Staging: 4 trays, then 48 more. The total tray count is not stated (120 by my calculation from the $\pi/30$ tray width).

---

## References (hardware-relevant subset)
- [1] STAR TOF Collaboration 2004, *STAR TOF Proposal*.
- [2] M. Shao et al. 2002, Nucl. Instrum. Methods A **492** 344. (MRPC final design; CERN PS T10 beam test.)
- [3] Y. J. Sun 2006, PhD thesis, USTC. (MRPC operating conditions, rate and ageing tests; [3–5] together.)
- [4] Y. E. Zhao 2006, PhD thesis, USTC.
- [5] Y. L. Wu 2006, master's thesis, USTC.
- [6] W. J. Llope et al. 2004, Nucl. Instrum. Methods A **522** 252. (pVPD start detector.)
- [7] J. Wu et al. 2005, Nucl. Instrum. Methods A **538** 243. (TOFr timing calibration with a pure pion sample.)
- [8] M. Shao et al. 2006, Nucl. Instrum. Methods A **558** 419. (TOFr PID in Au+Au; electron ID and $10^5$ hadron rejection.)

Physics references (not hardware): [9] Adams et al. 2005 PLB 616 8; [10] Adams et al. 2005 PRL 94 062301; [11] Shao et al. 2005 J. Phys. G 31 S85; [12] Barannikova et al. 2005, QM2005 proceedings; [13] Adams et al. 2006 PRL 97 152301; [14] Zhang et al. 2005, QM2005 proceedings.
