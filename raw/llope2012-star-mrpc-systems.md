---
title: "Llope 2012 — Multigap RPCs in the STAR experiment at RHIC (full-content paraphrase)"
type: raw-source
source_type: paper
authors: "W.J. Llope (Rice University), for the STAR Collaboration"
journal: "Nucl. Instrum. Meth. A 661 (2012) S110–S113 (RPC 2010 workshop proceedings)"
doi: "10.1016/j.nima.2010.07.086"
arxiv: none
captured_via: "Route 1 — ScienceDirect publisher HTML (full body, 4 figures, Table 1) in Chrome via JLab institutional access; every number checked against pdftotext -layout of the publisher PDF; the 4 publisher high-resolution figure images saved"
captured_date: 2026-11-06
captured_as: full-content paraphrase
figures: "4 (vision descriptions added 2026-11-06)"
vision_model: "general-purpose subagent (session model, not recorded), 2026-11-06"
---

# Multigap RPCs in the STAR experiment at RHIC — reading note

- **Citation:** W.J. Llope (Rice University, Houston, TX 77005, USA), for the STAR Collaboration, "Multigap RPCs in the STAR experiment at RHIC". Single named author. Contact: llope@rice.edu.
- **Journal ref:** Nucl. Instrum. Meth. A **661** (2012) S110–S113. This is the proceedings issue of the X Workshop on Resistive Plate Chambers and Related Detectors (RPC 2010), edited by N. Herrmann, S.P. Ratti and R. Santonico. Available online 5 August 2010; the issue date is 1 January 2012.
- **DOI:** [10.1016/j.nima.2010.07.086](https://doi.org/10.1016/j.nima.2010.07.086) (ScienceDirect PII S0168900210017006). Confirmed with a Crossref query (title, author, volume 661, pages S110–S113) and on the ScienceDirect article page.
- **arXiv:** none found. An arXiv API title search for "Multigap RPCs in the STAR" returned 0 results, and the paper is not among the arXiv entries for author Llope that I checked.
- **Route used:** Route 1 (publisher HTML on ScienceDirect, opened in the user's Chrome with JLab institutional access). The HTML has the full body: 5 sections, 4 figures, Table 1 and the references. The paper has no displayed equations. The few inline math expressions are simple, and I read them from the rendered text, so no MathML transcription was needed. Routes 2 and 3 were not needed for the text. The PDF was still downloaded and used for verification.
- **PDF backup:** `assets/llope2012-star-mrpc-systems/source.pdf` (595 331 bytes, 4 pages, S110–S113).
- **Figures:** the 4 high-resolution figure images from the publisher (`…-grN_lrg.jpg`) are saved as `assets/llope2012-star-mrpc-systems/fig1.jpg` … `fig4.jpg`. I opened Fig. 1 and Fig. 3 to confirm they match their captions.
- **Verification:** I checked every number, unit and table entry, and the reference list, against `pdftotext -layout` of the PDF. The HTML and the PDF agree on every number and on all of Table 1. The only differences are glyph artefacts in pdftotext, where the PDF and HTML themselves agree: "TOFr′" comes out as "TOFru", the "3/4" in the Fig. 3 caption as "34", and "<" as "o".
- Figure descriptions were added by a separate figure pass that looked at the images.

> **[note] Scope.** This is a 4-page workshop proceeding and an overview. It gives the TOF MRPC stack (gaps, glass, resistivities, HV, gas, pad size), the tray and system counts, the electronics chain (TINO/TDIG/TCPU/THUB) and a table of timing resolutions by run. It does **not** give the barrel radius, the outer MRPC dimensions, the inter-pad gap, which pad dimension lies along $z$ or along $\phi$, the tilt angles, the start-detector name, or any hit-position (local-$z$) correction. Those gaps are flagged in the Checks section.

---

## Abstract (paraphrase)

STAR has recently installed a large-area Time-of-Flight system of about **50 m²**. Its detectors are Multigap Resistive Plate Chambers (MRPCs), read out by custom electronics built around the CERN **NINO** and **HPTDC** chips. Several prototype systems were built and run in STAR from 2002 to 2006. The paper presents the design and performance of these prototypes and of the final system, which was about **70 %** installed during the 2009 RHIC run. A possible future STAR upgrade, the Muon Telescope Detector (MTD), would use very large MRPCs with double-ended readout to identify, by time of flight, muons that pass through the steel back-legs of the STAR magnet. The paper also presents the MTD design and the performance of MTD prototypes.

**Keywords:** Time of flight; Multigap resistive plate chamber; STAR experiment; RHIC.

- **[source issue]** The abstract says "∼70 %" of the final system was installed for Run 9. Section 3 says 94 trays were installed before Run 9 and calls this "three-quarters" (also in the Fig. 3 caption). 94/120 = 78.3 %, which is closer to 3/4 than to 70 %. A small inconsistency in the source.

---

## 1. Introduction

RHIC at Brookhaven collides two ¹⁹⁷Au nuclei at up to **100 GeV/c per nucleon** (as printed). The matter produced is dense enough to quench jets, yet flows like a nearly perfect fluid [1]. Of the two RHIC experiments studying this matter, STAR is the one with wide, azimuthally complete acceptance, set by its Time Projection Chamber (TPC). STAR had important "blind spots", though. It could not efficiently identify charged $\pi$ and K (p) above about **0.7 (1.0) GeV/c**, so roughly half of the charged hadrons in an event could not be identified directly. Its ability to identify muons directly was also very limited. To close these gaps, STAR built and installed a large-area TOF system for charged-hadron identification and is developing a second large-area system for muon identification. Both are based on MRPCs [2].

A TOF system [3] with **100 ps total timing resolution**, in the STAR geometry and with the STAR TPC tracking resolution, gives direct $\pi$:K:p identification up to about **1.7–1.9 GeV/c** and $(\pi+\mathrm{K})$:p identification up to about **2.9–3.1 GeV/c**. Combining TOF with TPC dE/dx gives high-efficiency PID over about **98 %** of the hadron spectra. Using TOF to reject "slow" tracks also lets electrons be separated cleanly from pions using the track dE/dx.

This wider PID improves signal-to-background for $\rho$, K*(892), $f_0$, $\phi(1020)$, $\Delta$, $\Sigma(1385)$, $\Lambda(1520)$, $D^0$, $D^+$ and $D_s^+$ by significant factors. In some cases it allows complete spectra of these particles to be measured in a single RHIC run for the first time. TOF is also seen as especially important [4] for the RHIC beam-energy scan ($5<\sqrt{s_{NN}}<39$ GeV, printed as "GeV/nucleon"), which searches for the QCD critical point and starts in Run 10. Every observable of interest improves with TOF. For example, the K⁺/π⁺ ratio and its event-by-event fluctuations improve for two reasons: π and K misidentification is suppressed, and the large dynamical-fluctuation contribution from finite counting statistics is reduced (that contribution comes from the low efficiency of TPC dE/dx PID).

Better direct muon identification would give large samples of identified $J/\psi$ and $\Upsilon$ and a unique measurement of $\mu$–e correlations from heavy-flavour decays. A large-area muon system would therefore give access to colour degrees of freedom and the equation of state. For example, colour screening makes quarkonium states with different binding energies dissociate at different temperatures. So precise transverse-momentum spectra of quarkonia across centralities and beam entrance channels act as a direct thermometer of the hottest stage of the collision. The MRPCs planned for the STAR MTD are much larger than the TOF MRPCs and read long strips at both ends. The MTD concept also differs from conventional muon systems, which use several layers of absorber and tracking. In STAR, the electromagnetic calorimeter plus the steel magnet back-legs form an absorber of about **6 interaction lengths** between the TPC and the MTD. TPC tracks that produce MTD hits at the right times and positions are identified as muons. Prototype MRPCs and MTD detectors have been studied in test beams and in STAR since **RHIC Run 7**.

Section 2 covers the TOF MRPCs, Section 3 the full-size prototypes and the final system, Section 4 the MTD MRPCs and the status of a large-area MTD, and Section 5 the conclusions.

- **[source issue]** Units as printed: "100 GeV/c/nucleon" is a momentum per nucleon, which is fine for the beam. The beam-energy-scan range "$5<\sqrt{s_{NN}}<39$ GeV/nucleon" has a redundant "/nucleon", because $\sqrt{s_{NN}}$ is already per nucleon pair and is quoted in GeV.
- **[note]** A rough PID-reach check (my calculation, not in the paper; the radius is not given here, so I assume a flight path of $L\approx 2.2$ m). For $p = 1.7$ GeV/c, $\Delta t_{K\pi} = \frac{L}{c}\left[\sqrt{1+m_K^2/p^2}-\sqrt{1+m_\pi^2/p^2}\right] \approx 7.34\ \text{ns}\times(1.0413-1.0034)\approx 278$ ps. That is about $2.8\sigma$ at 100 ps, consistent with the quoted π/K limit of about 1.7–1.9 GeV/c ✓.

---

## 2. The multi-gap resistive plate chambers for STAR TOF

The CERN ALICE group first developed the MRPC [2]. Working closely with them, the STAR group built a STAR variant and tested it in a CERN test beam [5].

**MRPC construction (as given):**

| Item | Value |
|---|---|
| Inner resistive plates | 0.54 mm-thick float glass |
| Gas gaps | five gaps of 220 μm |
| Outer glass plates | 1.1 mm thick, graphite electrodes on the outer surface |
| HV | ∼14 kV voltage difference across the electrodes |
| Glass resistivity | ∼10¹³ Ω cm |
| Electrode (graphite) surface resistivity | 10⁵ Ω/□ |
| Readout cells | one row of **six pads, 3.5 × 6.1 cm²**, read out from one edge by traces that go to two twisted-pair signal cables |
| Gas | 95 % R-134a + 5 % isobutane |
| Signal charge | ∼25 fC per hit ("extremely small") |
| Dark rate | ∼1 Hz/cm² (i.e. ∼20 Hz per pad) |

Because the signals are so small, careful preamplification in the front end and careful shielding of the mechanics against outside radio-frequency interference are essential.

Fig. 1 shows the CERN test-beam results versus voltage: detection efficiency (open circles), time resolution (solid circles) and average signal area (triangles). The flux was **200 Hz/cm²**, the highest rate expected for STAR TOF in the RHIC-II era. There is a wide voltage plateau with **>95 % efficiency** and a pure-stop timing resolution **below 75 ps**, so these MRPCs are suitable for STAR TOF.

![Fig. 1](assets/llope2012-star-mrpc-systems/fig1.jpg)

**Fig. 1.** Performance of the STAR MRPCs measured in a CERN test beam.

*Figure description (from the image):* Single panel, CERN test-beam HV scan. x-axis "Voltage (kV)", 13 to 17 kV (labels every 0.5 kV, top and bottom). Left y-axis "Efficiency (%)", 0 to 100. Right y-axis is one shared scale, 20 to 120, labelled both "ADC (bins)" (upper) and "Time resolution (ps)" (lower). Printed legend: "200 Hz/cm²"; open circles "Efficiency"; solid triangles "Mean ADC"; solid circles "Time resolution, sigma". Each set has six points at 14.75, 15.0, 15.25, 15.5, 15.75 and 16.0 kV with a smooth curve through them. No point values are printed; my approximate readings from pixel positions: efficiency ≈95 % at 14.75 kV and ≈97.5–98.5 % from 15.0 to 16.0 kV; mean ADC rises from ≈76 to ≈114 bins; time resolution ≈62–64 ps from 14.75 to 15.5 kV, then ≈68 and ≈72 ps at 15.75 and 16.0 kV. Main feature: an efficiency plateau near 98 % above 15 kV while σ_t stays below about 72 ps (minimum ≈62 ps around 15.0–15.5 kV) and the mean signal size climbs steeply. Matches the caption.

- **[note]** The text's "average signal area (triangles)" is the plot's "Mean ADC" in "ADC (bins)", so text and figure agree. The plot labels the resolution only as "sigma"; it does not itself say pure-stop. The lowest-voltage efficiency point (14.75 kV) sits at about 95 %, so ">95 %" holds clearly from 15.0 kV upward. All resolution points are below 75 ps ✓.

- **[note]** Derived pad numbers (my calculation): pad area $3.5\times6.1 = 21.35$ cm². At 1 Hz/cm² that gives a dark rate of about 21 Hz/pad, consistent with the quoted ∼20 Hz/pad ✓. Pad size divided by √12: $3.5/\sqrt{12} = 1.01$ cm and $6.1/\sqrt{12} = 1.76$ cm. This is the position resolution you get by assigning a hit to the pad centre, since each pad is read at one edge and gives no position within the pad. **The paper does not say which pad dimension is along the beam ($z$) and which along $\phi$**, and it does not give the inter-pad gap.
- **[note]** Total pad area: $23\,040\times21.35$ cm² = 49.2 m², consistent with the "50 m²" in the abstract ✓.
- **[note]** HV: the text gives "∼14 kV" as the applied voltage difference. The voltage axis of the test-beam scan in Fig. 1 runs from 13 to 17 kV, with data points from about 14.75 to 16 kV. The text does not say what HV was used in STAR operation. This is not necessarily an inconsistency, but the in-STAR operating point is not stated here.
- **[note]** "R-134a" (Section 2) and "C₂H₂F₄" (Section 4) are the same gas (tetrafluoroethane), so the TOF and MTD gas descriptions are consistent ✓.

---

## 3. The STAR TOF prototypes and the full system

The TOF MRPC design was finalized in 2001. The technology was then tested in STAR in full-size prototype "trays":

| Prototype | RHIC run(s) | Digitization |
|---|---|---|
| TOFr | Run 3 | CAMAC, via the existing STAR TOFp subsystem [6], long signal cables |
| TOFr′ | Run 4 | CAMAC, via TOFp [6], long cables |
| TOFr5 | Runs 5 and 6 | on-board, CERN HPTDC [9] |

(Table assembled from the text.) Each prototype was built from scratch, with step-by-step improvements to the mechanics and electronics to make construction simpler, tighten mechanical tolerances and improve performance. A few MRPCs were used in all three prototypes to look for ageing; **none was seen**. TOFr was also tested extensively in an AGS radiation area [7].

The TOF electronics were optimized over several years. Final MRPCs, final tray mechanics and final electronics were first used in **Run 8 (5 trays)**. In the final electronics the **MAXIM 3760** amplifier was replaced by the CERN **NINO** amplifier/discriminator [8]. **94 trays** were installed before Run 9, and **all 120 trays** before Run 10 (ongoing at the time of writing). The MRPCs were made in China. The trays were built, assembled and tested as complete units in Texas, then fully retested on arrival at Brookhaven.

**Layout.** The 120 trays form **two adjacent rings of 60 trays each**, just outside the STAR TPC. Each tray covers about **0.9 units of pseudorapidity** and **1/60 of the azimuth**. Each tray holds **32 MRPCs**, arranged **nearly projectively** for collisions at the centre of STAR. That gives **3840 MRPCs** and **23 040 readout channels** in total. Occupancy in central full-energy Au+Au collisions is about **12 %**.

- **[note]** Counts check (my calculation): $120\times32 = 3840$ MRPCs ✓; $3840\times6 = 23\,040$ channels ✓; $32\times6 = 192$ channels per tray. Azimuth per tray: $360^\circ/60 = 6^\circ$. Two rings of about 0.9 in $\eta$ each, meeting at $\eta=0$, imply roughly $|\eta|\lesssim0.9$ (the paper gives no total $\eta$ range).
- **[note]** "Nearly projectively for collisions at the centre of STAR" means the MRPCs are tilted to point roughly at $z=0$. The tilt angles are not given.

**Circuit boards [10]:**

- **TINO** closes the gas box and feeds through the differential signals of **four MRPCs (24 channels)** into **three NINO chips**. The NINOs amplify and discriminate the signals. Each also outputs a level when any of its eight channels is over threshold.
- **TDIG** time-digitizes the TINO signals against a **40 MHz clock** using **three HPTDC chips**. The leading and trailing edges of each signal go to the **same HPTDC channel** in "very high resolution" mode (**∼24.4 ps LSB**). The resulting **time-over-threshold (ToT)** is the pulse-size measure used for offline **slewing corrections** of the leading-edge times. The **integral non-linearity (INL)** of all 23 040 HPTDC channels was measured on the bench and stored in the STAR database for offline use.
- **TCPU** gathers, formats and buffers the data from the **eight TDIG boards** of a tray. It also collects the TINO multiplicity levels and outputs a digital tray multiplicity (0–24) to the **earliest level of the STAR trigger**.
- **THUB**: **four THUB boards**, each collecting data from **30 trays (240 TDIG boards)**, send the data to a receiver in STAR DAQ over **SIU/RORC** links [11]. One THUB generates the master clock, which it distributes to the other three THUBs and to the trays.

- **[note]** Electronics counts check (my calculation): 8 TINO × 4 MRPCs = 32 MRPCs per tray ✓. 3 NINO × 8 channels = 24 channels per TINO ✓. 8 TDIG × 24 = 192 channels per tray ✓ (this implies 8 channels per HPTDC in very-high-resolution mode; the per-chip channel count is not stated in the paper). 4 THUB × 30 trays = 120 trays ✓; 30 × 8 = 240 TDIG ✓. LSB: 25 ns (40 MHz) / 1024 = 24.41 ps ✓, consistent with the quoted ∼24.4 ps. The TCPU multiplicity range 0–24 equals the 24 NINO "any-channel" levels per tray (8 TINO × 3 NINO) ✓.

**Power and cooling.** The eight TINO, eight TDIG and one TCPU board on each tray together draw about **100 W**. About **90 %** of the heat is removed by a rectangular **1/4 in. × 3/8 in.** copper cooling-water loop that touches the TINO layer below and the TDIG layer above. An aluminium cover over the electronics on top of each tray protects them mechanically and shields them from radio-frequency noise.

**Performance.** The first five final trays ran stably through Run 8. Fig. 2 shows their PID performance in the p+p part of that run. The stop-side calibrations needed for this performance were:

1. the HPTDC INL correction,
2. channel-by-channel timing offsets relative to the start time,
3. a standard leading-edge slewing correction using the ToT.

Three-quarters of the full system was installed for Run 9, which was also p+p. Because multiplicities are low in p+p, the calibration was done in groups of **24 channels (one TDIG board)**. Fig. 3 shows the total time resolution versus board number. The system performed quite uniformly.

![Fig. 2](assets/llope2012-star-mrpc-systems/fig2.jpg)

**Fig. 2.** PID performance of the first five final TOF trays, installed for RHIC Run 8.

*Figure description (from the image):* Single 2D density plot with a colour scale (blue/violet = few entries, red = most; no colour bar or z-scale printed). x-axis "Momentum p (GeV/c)", 0 to 3.5 (labels every 0.5). y-axis "1/β", 0.6 to 2 (labels every 0.2). Three black expected-1/β curves, labelled "π", "K" and "p"; the π curve starts at about p ≈ 0.17 GeV/c, 1/β ≈ 1.3, and the K and p curves leave the top of the plot (1/β = 2) at about 0.27 and 0.52 GeV/c, which fits the K and p masses (my check). An "e" label sits at 1/β ≈ 1.05 at the low-p start of the band near 1/β = 1; I see no separate electron curve. The π band is the most populated (red/yellow) and approaches 1/β = 1; the K and p bands are clearly separated from it at low p and merge toward 1 at high p (by eye the K band is distinct up to roughly 1.5–2 GeV/c and the p band to roughly 3 GeV/c). Sparse background fills the plane, including 1/β < 1 down to 0.6 at low p. No run, beam species or energy is printed on the plot; those come only from the caption and text (Run 8, p+p, first five trays). Matches the caption.

![Fig. 3](assets/llope2012-star-mrpc-systems/fig3.jpg)

**Fig. 3.** Total time resolution of the ¾-installed STAR TOF system in RHIC Run 9.

*Figure description (from the image):* Single panel. x-axis "Channel ID", 0 to about 23 000 (labels every 2000 up to 22000). y-axis "Time resolution (ns)", 0.0 to 0.2 (labels 0.0, 0.1, 0.2), dotted grid. Black points with small error bars and a red horizontal line (constant fit). ROOT fit box: "χ² / ndf 2059 / 687", "p0 0.1119 ± 0.0001". Points lie mostly within ≈0.105–0.125 ns; the highest outlier is ≈0.14 ns near channel ≈21 100, with a local rise to ≈0.13 ns near ≈13 600. Ranges with no points (approximate, from pixel positions): ≈2300–2600, ≈7100–7400, ≈8000–8200, ≈14 000–14 300, ≈15 000–18 350 (largest), ≈19 350–19 700. Main feature: a uniform total resolution of about 112 ps across the installed part of the system. Matches the caption.

- **[source issue]** Confirmed: the text says Fig. 3 shows the total time resolution "versus the board number", but the plotted x-axis is "Channel ID" (0 to about 23 000), not a board index. The text's statement that calibration was done per 24-channel TDIG board suggests each point is one board placed at its channel position, but the plot does not say so.
- **[note]** If p0 is the only fit parameter, ndf = 687 means 688 points were fitted. That is fewer than the 94 × 8 = 752 TDIG boards installed for Run 9; 86 trays × 8 = 688 would match if the eight trays that developed problems were left out (my inference, not stated in the paper). p0 = 111.9 ps agrees with the Run 9 p+p 200 GeV total of 111 ps in Table 1 ✓.

Table 1 summarizes the total, pure-start and pure-stop timing resolutions of the prototypes and the final trays. On-board TDIG digitization was used from Run 5, and from then on the slewing correction used ToT. Before that, the slewing correction used the signal area from CAMAC ADCs. The **start detector was also changed before Run 8** (the paper does not name it). The Run 9 and Run 10 values are **preliminary**. They come from the first "fast-offline" production, so they are based on small subsets of the data and/or a TPC that was not fully calibrated, and improvements of about **10 ps** are possible. Even so, the pure-stop resolution of the final trays (Run 8 onward) is **74–82 ps**, and the total resolution in full-energy Au+Au in Run 10 meets the **sub-100 ps** requirement for the physics goals.

**Table 1.** Time resolutions of the TOF prototype and final trays during operation in STAR, by RHIC run.

| RHIC run (year) | Beams and $\sqrt{s_{NN}}$ (GeV) | Start (ps) | Total (ps) | Stop (ps) |
|---|---|---|---|---|
| 3 (2003) | d+Au, 200 | 85 | 120 | 85 |
|  | p+p, 200 | 140 | 160 | 80 |
| 4 (2004) | Au+Au, 62 | 55 | 105 | 89 |
|  | Au+Au, 200 | 27 | 86 | 82 |
| 5 (2005) | Cu+Cu, 200 | 50 | 92 | 75 |
|  | Cu+Cu, 62 | 82 | 125 | 94 |
| 8 (2008) | p+p, 200 | 83 | 112 | 75 |
| 9 prelim. (2009) | p+p, 500 | 85 | 115 | 78 |
|  | p+p, 200 | 81 | 111 | 74 |
| 10 prelim. (2010) | Au+Au, 200 | 30 | 87 | 82 |

- **[note]** Quadrature check (my calculation). If start and stop are independent, the three columns should satisfy
$$
\sigma_\text{total}^2 = \sigma_\text{start}^2 + \sigma_\text{stop}^2
$$
(not an equation in the paper). Results, as $\sqrt{\text{start}^2+\text{stop}^2}$ vs printed total: 120.2/120 ✓, 161.2/160 ✓, 104.6/105 ✓, 86.3/86 ✓, **90.1/92** (Cu+Cu 200; the stop implied by the printed total would be 77.2 ps rather than 75), 124.7/125 ✓, 111.9/112 ✓, 115.4/115 ✓, 109.7/111 (implied stop 75.9 rather than 74), 87.3/87 ✓. All rows agree within about 2 ps. The two rows that differ by 1–2 ps are probably rounding or separate fits, not errors.
- **[note]** The start resolution follows multiplicity, as expected: 27–30 ps in Au+Au 200 GeV, about 50–55 ps in Cu+Cu 200 / Au+Au 62, and 81–140 ps in p+p and d+Au.

**Reliability.** Of the 94 trays installed before Run 9, **eight** developed problems: on two trays the LV-cable sense wires came disconnected, five HV cables were installed wrongly or damaged by the STAR magnet pole-tips, and one tray had a bad TCPU card. All were repaired after Run 9. In Run 10 only **one tray** is not working, because of a single intermittently bad HV cable in a hard-to-reach place, to be fixed in the coming shutdown. Only **three readout channels** in the whole system are dead.

---

## 4. The multi-gap resistive plate chambers for STAR MTD

The MTD MRPCs are much larger than the TOF MRPCs, and their readout is double-ended. Prototype systems built from "Long MRPCs" (LMRPCs) [12] ran in STAR in **Runs 7–10**:

- **MTD7:** two LMRPCs end to end. Simple FEE [13] and long cables, digitized on the platform by STAR trigger-system electronics.
- **MTD9:** three LMRPCs side by side, two of them taken from MTD7. Same on-board electronics as STAR TOF.

**LMRPC module:**

| Item | Value |
|---|---|
| Stack | double stack of resistive glass plates |
| Gas gaps | ten gas gaps, each 250 μm wide (5 per stack) |
| HV | 12.6 kV per 5-gap stack |
| Gas | 95 % C₂H₂F₄ + 5 % isobutane (same as STAR TOF) |
| Readout | six copper pads (strips), 87 × 2.5 cm² each |
| Efficiency | >95 % for 12.5 < HV < 13.0 kV |
| Timing resolution | ∼70 ps (cosmic-ray and beam tests [12]) |
| Spatial resolution along the strip (from timing) | <1 cm |

The MTD7 prototype reached only about **300 ps** in STAR, because of its long cables and the particular electronics used [14]. Analysis of the Run 9 and Run 10 data is in progress.

**Final MTD design.** The final system will use much wider MRPCs, called "WMRPCs" (printed once as "WMPRCs"):

| Item | Value |
|---|---|
| Number in full system | 117 |
| Stack | single stack, five gaps |
| Outer dimensions | 91.5 × 58.0 × 3 cm³ |
| Readout | twelve 87 × 3.8 cm² strips, 0.6 cm gaps between strips, read out at both ends with STAR TOF electronics |
| Before Run 11 | three such detectors to be installed |

Fig. 4 is a schematic of five MTD trays per magnet back-leg mounted on the outside of STAR.

![Fig. 4](assets/llope2012-star-mrpc-systems/fig4.jpg)

**Fig. 4.** Planned arrangement of the MTD trays on the outside of STAR.

*Figure description (from the image):* Single 3D engineering rendering (no axes, scale or dimensions). It shows four parallel magnet back-legs (blue, labelled "Magnet Backleg"), each topped by a long tan box (labelled "Calorimeter Electronics Box"), with five rectangular MTD trays (one labelled "MTD tray") laid along the top of each box. Along each back-leg the trays alternate between two heights, so neighbouring trays appear staggered/overlapping at their edges. Each tray carries one small box near its centre (two side by side on the end tray of the two nearest back-legs) and two short dashed lines whose meaning is not labelled. Printed text is only the three labels "MTD tray", "Calorimeter Electronics Box" and "Magnet Backleg". Matches the caption and the text's "five MTD trays per magnet back-leg".

- **[note]** The figure prints no dimensions, no strip count and no beam (z) direction, so it does not show which WMRPC dimension or strip direction lies along the beam. The long axis of the back-legs is not labelled either.

- **[source issue]** "WMPRCs" in the text is a typo for "WMRPCs" (the next sentence uses "WMRPC"). Same in HTML and PDF.
- **[note]** WMRPC geometry check (my calculation): $12\times3.8 + 11\times0.6 = 45.6 + 6.6 = 52.2$ cm of strips plus gaps, which fits inside the 58.0 cm outer width ✓. The strip pitch is 4.4 cm, and 87 cm strips fit inside the 91.5 cm length ✓. Channels: $117\times12 = 1404$ strips, so $2808$ TDC channels with two ends each (not stated in the paper). Strip width / √12: $3.8/\sqrt{12} = 1.10$ cm (WMRPC); $2.5/\sqrt{12} = 0.72$ cm (LMRPC). Along the strip, the position comes from the time difference between the two ends (<1 cm for LMRPC). **The signal propagation speed is not given.**
- **[note]** The LMRPC "6 pads of 87 × 2.5 cm²" are long strips. Ref. [12] (Sun et al. 2008) gives an active area of 87 × 17 cm² and strips 2.5 cm wide and 90 cm long. Those details come from that paper's arXiv abstract (0805.2459), not from this one.

---

## 5. Conclusions

STAR has adopted MRPC technology twice over: for charged-hadron identification by time of flight inside the magnet (STAR TOF), and for muon identification outside it (STAR MTD). Many prototypes of both kinds ran in test beams and in STAR and work well. The TOFr prototypes were the first use of MRPCs in a collider experiment, proved the technology, and gave the first physics results from an MRPC-based TOF system [15]. The large-area TOF was finished in late 2009 and is running successfully in RHIC Run 10. Next-generation MTD prototypes will be installed for Run 11, and the large-area MTD is hoped to be complete before **RHIC Run 13**.

**Acknowledgments (paraphrase).** The author thanks the organizers and the STAR Collaboration, credits CERN's pioneering work on the MRPC, the NINO and HPTDC chips and the SIU/RORC links, and acknowledges US DOE grant DE-FG02-10ER41666.

---

## Checks

**(a) System layout**

- **Trays:** 120, in two adjoining rings of 60 just outside the TPC (Section 3).
- **MRPCs per tray:** 32. **Pads per MRPC:** 6 (one row). **Totals:** 3840 MRPCs and 23 040 channels ✓ (recomputed: 120 × 32 = 3840; × 6 = 23 040). The active area is about 50 m² (49.2 m² recomputed from pad area ✓).
- **Radius:** **not given** in this paper (only "immediately outside of the STAR TPC"). The companion note [wu2007-star-barrel-tof-note](wu2007-star-barrel-tof-note.md) records R = 210 cm for the TOFr prototype tray, but that is from a different paper.
- **η coverage:** about 0.9 units per tray, two rings, so roughly $|\eta|\lesssim0.9$ (my inference; no total range is printed).
- **φ coverage:** 1/60 of $2\pi$ per tray = 6°, full $2\pi$ for each ring.
- **Orientation:** the 32 MRPCs per tray are arranged "**nearly projectively** for collisions occurring at the center of STAR", i.e. tilted toward the nominal vertex at $z = 0$. Tilt angles are not given.

**(b) MRPC geometry**

- **Outer MRPC size:** **not given.**
- **Pads:** 3.5 × 6.1 cm², six in a single row, read out from one edge. **Inter-pad gap: not given.** **Which dimension is along $z$ and which along $\phi$: not stated.**
- **Gaps:** five 220 μm gas gaps, single stack.
- **Glass:** inner plates 0.54 mm float glass; outer plates 1.1 mm with graphite electrodes; glass resistivity ∼10¹³ Ω cm; electrode resistivity 10⁵ Ω/□.
- **HV:** ∼14 kV difference across the electrodes. The CERN test-beam scan in Fig. 1 covers about 14.75–16 kV.
- **Gas:** 95 % R-134a + 5 % isobutane.
- **Signal and noise:** about 25 fC/hit; dark rate about 1 Hz/cm² (about 20 Hz/pad).
- **[note] Pad size/√12:** 3.5/√12 = 1.01 cm and 6.1/√12 = 1.76 cm.

**(c) Hit position within a pad**

- **TOF: not discussed.** Pads are read out single-ended from one edge, and the paper lists no local-$z$ or hit-position-dependent time correction. The stop-side calibrations it lists are INL, per-channel offsets relative to the start time, and ToT-based slewing.
- **Position resolution and propagation speed:** not given for TOF.
- **MTD:** LMRPCs are read at both ends. Spatial resolution along the strip from timing is <1 cm. The propagation speed is not given.

**(d) Electronics, start detector and calibration**

- **Prototype electronics:**
  - TOFr and TOFr′: MAXIM 3760 amplifier, read out through the CAMAC TOFp system over long cables, with slewing based on ADC signal area.
  - TOFr5 onward: on-board HPTDC with slewing based on ToT.
- **Final electronics chain:**
  - **TINO:** 3 NINO amplifier/discriminators per 4 MRPCs (24 channels); also provides multiplicity levels.
  - **TDIG:** 3 HPTDCs, 40 MHz clock, "very high resolution" mode with about 24.4 ps LSB (= 25 ns/1024 ✓). Leading and trailing edges go to the same channel and give ToT.
  - **TCPU:** one per tray, 8 TDIGs; sends a 0–24 tray multiplicity to the earliest trigger level.
  - **THUB:** 4 boards, 30 trays each, SIU/RORC links to DAQ; one THUB is the master clock.
- **Power and cooling:** about 100 W per tray, with about 90 % removed by a 1/4 × 3/8 in. copper water loop.
- **Start detector:** **not named.** The paper says only that it "was changed before Run 8" and gives the start resolutions in Table 1.
  - **[note]** From outside this paper: the TOFp/pVPD system is ref. [6], and the upgraded VPD is W.J. Llope et al., NIM A 759 (2014) 23 (arXiv:1403.6855).
- **Calibration steps:**
  1. HPTDC INL correction, from bench measurements of all 23 040 channels stored in the database.
  2. Channel-by-channel offsets relative to the start time.
  3. Leading-edge slewing correction versus ToT.

  In the low-multiplicity Run 9 p+p data, calibration was done in groups of 24 channels (one TDIG board).

**(e) Achieved performance**

- **CERN test beam at 200 Hz/cm²:** >95 % efficiency plateau and pure-stop resolution below 75 ps.
- **In STAR (Table 1):**
  - Run 10 Au+Au 200 GeV (prelim.): start 30, total 87, stop 82 ps.
  - Run 9 p+p 200 GeV (prelim.): start 81, total 111, stop 74 ps.
  - Run 9 p+p 500 GeV: start 85, total 115, stop 78 ps.
  - Run 8 p+p 200 GeV: start 83, total 112, stop 75 ps.
  - Final trays (Run 8 onward): stop 74–82 ps.
  - Quadrature consistency was checked above ✓.
- **In-situ efficiency:** **not quoted** in this paper.
- **Rates and occupancy:**
  - Occupancy about 12 % in central full-energy Au+Au.
  - Design maximum rate 200 Hz/cm² (RHIC-II).
  - Dark rate about 1 Hz/cm².
  - Three dead channels, and one tray off in Run 10.
- **MTD:**
  - Concept: muons that pass about 6 interaction lengths (BEMC + magnet back-legs) and are matched in time and position to TPC tracks.
  - LMRPC (10 × 250 μm gaps, 12.6 kV per stack, 87 × 2.5 cm² strips): >95 % efficiency, about 70 ps, and <1 cm along the strip.
  - MTD7 in STAR: about 300 ps, limited by cables and electronics.
  - Final WMRPC: 117 detectors, 5 gaps, 91.5 × 58.0 × 3 cm³, twelve 87 × 3.8 cm² strips with 0.6 cm gaps, double-ended TOF electronics, five trays per back-leg.
  - Schedule: three WMRPCs before Run 11, full system hoped for before Run 13.

---

## References (hardware-relevant, as printed)

- [2] E. Cerron Zeballos et al., Nucl. Instr. and Meth. A 374 (1996) 132; M.C.S. Williams, Nucl. Phys. A 698 (2002) 464 — the MRPC concept.
- [3] Proposal for a Large-Area Time-Of-Flight System for STAR, http://wjllope.rice.edu/~TOF/TOF/Documents/TOF_20040524.pdf.
- [4] STAR Note SN0493, http://drupal.star.bnl.gov/STAR/starnotes/public/sn0493.
- [5] B. Bonner et al., Nucl. Instr. and Meth. A 478 (2002) 176 — STAR MRPC prototype at the CERN test beam.
- [6] W.J. Llope et al., Nucl. Instr. and Meth. A 522 (2004) 252 — the TOFp/pVPD system.
- [7] F. Geurts et al., Nucl. Instr. and Meth. A 533 (2004) 60 — TOFr in the AGS radiation area.
- [8] F. Anghinolfi et al., Nucl. Instr. and Meth. A 533 (2004) 183 — NINO.
- [9] M. Mota et al., IEEE J. Solid-State Circuits 34 (1999) 1360 — HPTDC.
- [10] J. Schambach et al., IEEE NSS Conference Record, vol. 1, 2006, p. 485 — TOF electronics boards.
- [11] ALICE DDL (SIU/RORC), http://alice-proj-ddl.web.cern.ch/alice-proj-ddl/ddl_intro.html.
- [12] Y. Sun et al., Nucl. Instr. and Meth. A 593 (2008) 307 — LMRPC.
- [13] W.J. Llope et al., Nucl. Instr. and Meth. A 596 (2008) 430 — simple MRPC FEE.
- [14] L. Ruan et al., J. Phys. G 36 (2009) 095001 — MTD concept and MTD7 performance.
- [15] J. Adams et al. (STAR), Phys. Lett. B 616 (2005) 8; Phys. Rev. Lett. 94 (2005) 062301 — first physics with MRPC TOF.
- (Physics only: [1] E. Shuryak, Prog. Part. Nucl. Phys. 53 (2004) 273.)
