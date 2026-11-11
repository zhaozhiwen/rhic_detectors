---
title: "Gagliardi 2022 — The STAR Forward Upgrade (full-content paraphrase)"
type: raw-source
source_type: talk-slides
authors: "Carl Gagliardi (Texas A&M University)"
venue: "STAR Juniors meeting, February 2022 (slides finalized 2022-02-12); not peer-reviewed"
doi: none
arxiv: none
captured_via: "Route 3 — talk-slide PDF supplied by the repo author; text from pdftotext -layout, image-only content read from rendered slides (80 dpi, 220-dpi crops)"
captured_date: 2026-11-06
captured_as: full-content paraphrase
figures: "13 (vision descriptions added 2026-11-06)"
vision_model: "general-purpose subagent (session model, not recorded), 2026-11-06"
---

# The STAR Forward Upgrade (Gagliardi, STAR Juniors talk, Feb 2022) — reading note

- **Source:** Carl Gagliardi (Texas A&M University), "The *STAR* Forward Upgrade", talk slides, 52 slides. Title slide: "With thanks for LOTS of work by LOTS of STAR Collaborators!"; supported in part by DOE Office of Science and NSF.
- **Date / venue:** every slide footer reads "STAR Forward Upgrade - 2-22 Juniors - Carl Gagliardi", i.e. a STAR Juniors (junior-researcher) meeting in February 2022. The slides were finalized on Saturday 12 Feb 2022: all run-status screenshots are from "mid-afternoon on Saturday" [s40], the luminosity plots are stamped "As of Saturday, Feb 12, 2022 15:10" [s51], and the PDF creation time is 2022-02-12 23:36 UTC. The exact talk date and venue (presumably online or at BNL) are not printed on the slides; it was most likely given within a few days after 12 Feb 2022.
- **Type:** talk slides, **not peer-reviewed**. Projections and preliminary results are shown as presented.
- **PDF metadata:** the PDF title field is "Thinking About Run 22 Triggering" (author "cg", Microsoft PowerPoint 2016). This is a leftover from an earlier PowerPoint file and is not the talk title.
- **Route used:** route 3 (PDF only; slides supplied by the repo author).
- **PDF backup:** `assets/gagliardi2022-star-forward-upgrade-talk/source.pdf` (8 187 849 bytes, 52 pages, 960 × 540 pt).
- **Verification:** slide text was checked against `pdftotext -layout`. Content that exists only in images (plot labels, fit boxes, statistics boxes, trigger-rate tables, screenshots) was read from rendered slides (80 dpi for all slides, 220 dpi crops for slides 8, 11, 15, 28, 42, 49 and 51). Values I read off plot axes are marked ≈. Numbers printed in plots are transcribed exactly.
- **Comparison file:** [ruan2026-fcs-specs-email-note](ruan2026-fcs-specs-email-note.md) (FCS ECal/HCal construction specs from Lijuan Ruan), used only for the [note] comparison table under slides 12–13.
- Figure descriptions were added by a separate figure pass that looked at the images.

---

## Full content

### Title and outline [s1]

Outline: (1) What is the Forward Upgrade? (2) What science will it do? (3) How are we doing in Run 22?

### Part 1 — What is the STAR Forward Upgrade? [s2–s15]

**The STAR detector [s3].** A 3D drawing of STAR. The TPC tracks for |η| < 1.5. PID uses dE/dx together with Time-of-Flight. Electromagnetic calorimetry surrounds the detector and covers −1 < η < 4. Many ancillary subsystems complement this.

**The STAR Forward Upgrade [s4].**
- Covers 2.5 < η < 4, where STAR formerly had only Pb-glass electromagnetic calorimetry. This is the same rapidity coverage as the EIC hadron arm.
- Adds four new subsystems:
  - charged-particle tracking with Si detectors and small-strip Thin Gap Chambers (sTGC);
  - electromagnetic and hadronic calorimetry with SiPM readout and new ADC + trigger electronics.
- Built to measure h^±, e^± (with good e/h discrimination), photons, π⁰ and jets.
- Performance-requirement table:

| Detector | pp and pA | AA |
|---|---|---|
| ECal | ~10%/√E | ~20%/√E |
| HCal | ~50%/√E + 10% | --- |
| Tracking | charge separation; photon suppression | 0.2 < p_T < 2 GeV/c with 20–30% 1/p_T |

- **[note]** The table does not say whether the HCal constant term adds linearly or in quadrature; it is written "+10%". The AA tracking entry presumably means 20–30% resolution in 1/p_T.

![Slide 04](assets/gagliardi2022-star-forward-upgrade-talk/slide04.png)

**Slide 04.** Cut-away of STAR showing the forward tracker (inside the pole tip) and the two FCS calorimeter halves downstream, with the coverage, subsystem list and resolution-requirement table.

*Figure description (from the image):* Left two-thirds: an unlabelled 3D cut-away rendering of STAR (grey magnet/return-iron, red support structure and endcap wheel, purple and yellow calorimeter layers, grey beam pipe along the axis). Inside the pole-tip cone near the beam pipe sit a small multicoloured disk set and a stack of four light-blue disk-shaped elements; downstream on a grey support platform around the beam pipe stand two box-shaped calorimeter blocks (purple fronts with blue-violet rear sections), one each side of the beam pipe. Right: bullet text and the orange-headed requirement table already transcribed above. No labels, dimensions or numbers inside the drawing.

**Silicon detector — Forward Silicon Tracker, FST [s5–s6].**
- Three disks, each with 12 modules.
- Each module has 3 single-sided, double-metal mini-strip sensors (Hamamatsu Si), with fine granularity in φ and coarse granularity in R.
- Material budget ~1.5% X₀ per disk.
- Technology is similar to the STAR Intermediate Silicon Tracker (IST): same APV25-S1 front-end chip, and the IST DAQ and cooling systems are reused.
- [s6] repeats the text with three installation photos of the wedge-shaped disks around the beam pipe.
- **[note]** Derived counts: 3 × 12 = 36 modules and 36 × 3 = 108 sensors ✓ (not stated on the slide).

![Slide 05](assets/gagliardi2022-star-forward-upgrade-talk/slide05.png)

**Slide 05.** The FST (red circle) at the upstream end of the forward tracker inside the STAR pole tip, with its specifications.

*Figure description (from the image):* Upper left: a crop of the same 3D rendering as slide 4, zoomed on the pole-tip region; a red circle encloses the small multicoloured (yellow/green/blue) disk structure around the beam pipe just upstream of the four light-blue disks, with the two purple/blue calorimeter blocks visible downstream at upper right. Bullet text below; right half of the slide is empty. No labels or numbers in the drawing.

**Small-strip Thin Gap Chambers, sTGC [s7–s9].**
- Four planes, each of four pentagonal modules. Double-sided sTGCs with diagonal strips give x, y and u in each layer. Position resolution < 200 μm.
- Material budget ~0.5% X₀ per layer.
- Readout based on VMM chips; similar to the ATLAS sTGC system.
- [s8] adds construction photos (a pentagonal chamber), a photo captioned "Electronics under test", and two test-stand efficiency histograms:
  - **Efficiency in X:** "Totle [sic] Event" = 787 (events with hits in both layers 1 and 2) and "Signal Event" = 777 (all three layers have hits, with cut |X_mid − (X_up + X_down)/2| < 10 mm). Efficiency = 98.7%. Recomputed: 777/787 = 98.73% ✓.
  - **Efficiency in Y:** 329 total, 323 signal, efficiency 98.2%. Recomputed: 323/329 = 98.18% ✓.
  - Headline on the slide: "Efficiency > 97%".
- [s9] shows installation photos of the four sTGC planes on the beam pipe, downstream of the FST.
- **[note]** Derived count: 4 × 4 = 16 pentagonal modules ✓. "Totle" is a typo for "Total" in the test-stand plots.

![Slide 08](assets/gagliardi2022-star-forward-upgrade-talk/slide08.png)

**Slide 08.** sTGC chamber construction, a finished pentagonal chamber, test-stand efficiency histograms for X and Y strips, and the readout electronics on a bench.

*Figure description (from the image):* Layout: two construction photos top left/centre, two ROOT histograms top right, bullet text bottom left, electronics photo bottom right. Photo 1: a worker in cleanroom garb (hairnet, mask) guiding a large flat panel lifted by an overhead hoist, with a pentagonal frame and a set of cylindrical metal weights on the table below. Photo 2: a large copper-clad pentagonal chamber panel on a dark table, with yellow edge connector strips along the angled edge and a gas tube. Histograms "Efficiency in X" and "Efficiency in Y": two-bin plots, y axis "Event" (0–800+ for X, 0–350 for Y), bins labelled "Totle Event" and "Signal Event"; bin contents printed as 787/777 (X) and 329/323 (Y); embedded text gives the definitions and efficiencies 98.7 % and 98.2 % (as in the note). Electronics photo: three circuit boards on a bench connected by ribbon and grey cables — a small blue board, a larger blue board with a row of network-style connectors and fibre/SFP-type ports, and a large green board; the green board carries a Brookhaven-logo silkscreen with partly legible text "… 8 Channel LV …" and "… LV Power System" (rest unreadable).

**[note]** As printed, the cut condition reads "X_mid − (X_up+X_down)/2 < 10 mm" with no absolute-value bars, and the Y-panel uses the same X-labelled formula (X_mid, X_up, X_down), apparently copied from the X panel; the note's |…| is an interpretation.

**sTGC gas system [s10].** Photos of the gas cabinet, the front of the controls cabinet ("sTGC gas interlock system") and the gas distribution panel.
- The sTGCs use a mixture of CO₂ and n-pentane.
- n-pentane is highly flammable and needs extreme care: flash point −49 °C; explosive limits 1.5–7.8%. Its boiling point of 36.1 °C complicates things further.
- The system "has operated extremely well through major power failures and big storms".
- **[note]** The mixing fraction of CO₂ and n-pentane is not given.

**Simulated performance of the Forward Tracker [s11].** Four simulation panels, for √s = 500 GeV (left) and 200 GeV (right), all at 2.5 < η < 4.0. Red = sTGCs only (labelled FTT); blue = sTGCs + Si disks (FTT + FST). The primary-vertex constraint is PV(σ_xy = 200 μm) at 500 GeV and PV(σ_xy = 500 μm) at 200 GeV. Linear fits f(x) = [0] + [1]·p_T are printed in each panel:

| Panel | FTT (sTGC only) | FTT + FST |
|---|---|---|
| Charge mis-ID rate, 500 GeV | −0.3% + 3.4% × p_T | 0.1% + 1.1% × p_T |
| Charge mis-ID rate, 200 GeV | −0.2% + 3.4% × p_T | −0.2% + 1.7% × p_T |
| p_T resolution (p_T^GEN − p_T^RECO)/p_T^GEN, 500 GeV | 18.0% + 5.7% × p_T | 14.9% + 4.0% × p_T |
| p_T resolution, 200 GeV | 18.1% + 5.5% × p_T | 15.1% + 4.1% × p_T |

- Slide conclusions: charge mis-ID rate is below 6% (8%) for p_T < 5 GeV/c at √s = 500 GeV (200 GeV); p_T resolution is better than 35% for p_T < 5 GeV/c at both energies.
- **[note]** Fits evaluated at p_T = 5 GeV/c:
  - FTT + FST mis-ID: 5.6% at 500 GeV ✓ (< 6%); 8.3% at 200 GeV (slightly above the "8%" claim).
  - FTT + FST resolution: 34.9% at 500 GeV ✓; 35.6% at 200 GeV (marginally above 35%).
  - sTGC-only at 5 GeV/c: mis-ID 16.7% / 16.8%; resolution 46.5% / 45.6%.
  - The histograms themselves sit above the fit line in the last bins (blue mis-ID ≈ 6.8% at 500 GeV and ≈ 9.3% at 200 GeV; blue resolution ≈ 0.35–0.37). So the claims hold for the fits rather than bin by bin.
- **[source issue]** In the charge mis-ID panels the fit legends still read "σ_pT = …", copied from the resolution panels. The quantity fitted is the mis-ID rate.

![Slide 11](assets/gagliardi2022-star-forward-upgrade-talk/slide11.png)

**Slide 11.** Simulated charge mis-identification rate and relative p_T resolution versus p_T for sTGC-only and sTGC + Si tracking, at 500 and 200 GeV.

*Figure description (from the image):* 2 × 2 grid of ROOT plots: columns √s = 500 GeV (left) and 200 GeV (right); rows charge mis-ID (top) and p_T resolution (bottom); row labels at left and the red/blue colour key at right. Top panels: y axis "Charge Mis-Id Rate" 0–0.18 (500 GeV) and 0–≈0.17 (200 GeV), x axis p_T 0–5 with no axis title printed. Bottom panels: y axis (p_T^GEN − p_T^RECO)/p_T^GEN 0–0.5+, x axis "p_T^GEN (GeV/c)" 0–5. Each panel has red (PV + FTT) and blue (PV + FTT + FST) step histograms with error bars in ≈0.25 GeV/c bins and black dashed linear fits; fit boxes label the two lines "FTT:" and "FST:" (the FST line corresponds to FTT + FST). Red mis-ID rises roughly linearly to ≈0.17 at p_T = 5 GeV/c at both energies; blue reaches ≈0.07 (500) and ≈0.09 (200). Resolution histograms begin at p_T ≈ 0.2 GeV/c near ≈0.17–0.19 and rise to ≈0.47 (red) and ≈0.35–0.37 (blue) at 5 GeV/c.

**Forward Calorimeter System, FCS [s12–s13].** (NSF logo on the slide.)
- Located 7 m from the center of STAR; split into 2 movable halves; slightly projective.
- **ECal:** reuses the PHENIX Pb-scintillator calorimeter.
  - 1496 channels of 5.52 × 5.52 × 33 cm³.
  - 66 sampling cells of 1.5 mm Pb / 4 mm Sc.
  - 36 wavelength-shifting fibers per cell [s12] (reworded to "per channel" on [s13]).
  - 18 X₀; 0.85 nuclear interaction lengths.
  - PMTs replaced with SiPM readout.
- **HCal:** Fe/Sc (20 mm / 3 mm) sandwich.
  - 520 channels of 10 × 10 × 84 cm³; approximately 4.5 nuclear interaction lengths.
  - Uses the same SiPM readout as the ECal.
  - Developed in collaboration with EIC R&D.
- **Preshower** (not shown in the drawing): signals split off from the STAR Event Plane Detector (EPD) for triggering.
- [s13] adds: the entire FCS (ECal + HCal + electronics) was installed during 2020 and commissioned during Run 21, with extensive running with Au+Au at √s_NN = 7.7 GeV and brief runs with O+O and d+Au at √s_NN = 200 GeV.

![Slide 13](assets/gagliardi2022-star-forward-upgrade-talk/slide13.png)

**Slide 13.** The two FCS halves (red ellipse) downstream of the forward tracker, with the ECal/HCal/preshower specifications and the 2020 installation and Run-21 commissioning history.

*Figure description (from the image):* Left: crop of the same 3D rendering as slides 4–5, with a large red ellipse around the two box-shaped calorimeter halves downstream of the light-blue tracker disks (each half drawn as a purple front block with a blue-violet rear block; the drawing does not label which is ECal or HCal). NSF logo top right. Red and black text bottom left and green/blue specification bullets on the right as transcribed. No numbers or labels inside the drawing.

**[note] FCS numbers: this talk vs [ruan2026-fcs-specs-email-note](ruan2026-fcs-specs-email-note.md).**

| Quantity | Gagliardi talk [s12–s13] | ruan2026-fcs-specs-email | Comment |
|---|---|---|---|
| Distance from IP | "7 m from the center of STAR" | ECal front face z = 710.16 cm; HCal front face z = 782.63 cm | consistent ✓ (talk rounds) |
| η coverage | 2.5 < η < 4 [s4] | ≈ 2.2 < η < 4.3 | the email gives the geometric reach, the talk the design physics range |
| ECal technology | PHENIX Pb/Sc, WLS fibers, SiPM | Pb/Sc shashlik, WLS fibre, SiPM, re-used PHENIX PbSc | consistent ✓ |
| ECal channels | 1496 | 1496 = 2 × 748 (22 col × 34 row per half) | ✓ |
| ECal tower face | 5.52 × 5.52 cm | 5.542 × 5.542 cm | talk rounds down; difference 0.02 cm |
| ECal tower length | 33 cm | 37.73 cm stack (66 × 4.24 mm + 65 × 1.5 mm) | **differs** — see below |
| ECal sampling | 66 cells, 1.5 mm Pb / 4 mm Sc | 66 Sc × 4.0 mm (+ 2 × 0.12 mm paper), 65 Pb × 1.5 mm | consistent; the email specifies 65 Pb layers |
| WLS fibers | 36 per cell/channel | not given | — |
| ECal depth | 18 X₀; 0.85 λ_I | 18.1 X₀; 0.93 λ | X₀ ✓; λ differs (0.85 vs 0.93) |
| HCal technology | Fe/Sc 20 mm / 3 mm sandwich | 20 mm steel × 36, 3 mm Sc × 36, 3 mm WLS plate per tower | consistent ✓ |
| HCal channels | 520 | 520 = 2 × 260 (13 col × 20 row per half) | ✓ |
| HCal tower size | 10 × 10 × 84 cm³ | 9.99 × 9.99 cm; 84.24 cm (+10 mm back plate) | consistent ✓ |
| HCal depth | ≈ 4.5 λ_I | 4.45 λ; 41 X₀ | consistent ✓ |
| Readout | SiPM (same for ECal and HCal); new ADC + trigger electronics | SiPM; DEP boards: 24 per half (ECal), 9 per half (HCal) | DEP board counts only in the email |
| Halves | 2 movable halves | North and South halves | ✓ |

- **[note]** Checks on the talk's numbers:
  - ECal stack: 66 × (1.5 + 4.0) mm = 36.3 cm without wrapping, or 37.73 cm with the paper wrap (email). Neither matches the 33 cm on the slide. **[source issue]** The "33 cm" tower length is inconsistent with "66 sampling cells with 1.5 mm Pb / 4 mm Sc". It may refer to some other length (for example the active length excluding end pieces), but the slide does not say.
  - ECal X₀: 65 × 1.5 mm Pb = 9.75 cm / 0.561 cm ≈ 17.4 X₀, plus 26.4 cm scintillator / ≈41.3 cm ≈ 0.64 X₀, giving ≈ 18.0 X₀ ✓ (18 X₀ on the slide).
  - ECal λ_I: 9.75/17.59 + 26.4/77.1 ≈ 0.55 + 0.34 ≈ 0.90 λ_I. This lies between the talk's 0.85 and the email's 0.93; the difference is within the rounding of the inputs.
  - HCal λ_I: 36 × 2.0 cm Fe = 72 cm / 16.77 cm ≈ 4.29 λ_I, plus ≈ 0.14 from 10.8 cm scintillator and ≈ 0.06 from the back plate, giving ≈ 4.5 ✓.
  - HCal length: 36 × 2.3 cm = 82.8 cm without air gaps; 84.24 cm with the 0.4 mm gaps (email). The talk's "84 cm" ✓.
  - Face of one half: ECal 22 × 5.52 = 121.4 cm by 34 × 5.52 = 187.7 cm; HCal 13 × 10 = 130 cm by 20 × 10 = 200 cm. The online maps on [s15] and [s44] confirm this layout: ECal columns −22…+22 with rows 0…34 (or −1…−34); HCal columns −13…+13 with rows −1…−20.

**FCS photos [s14].** Construction and installation photos: HCal absorber/scintillator assembly on a bench, a crew with HCal modules, the SiPM/readout side of the calorimeter with cabling, and a view through the magnet bore toward the forward region. No numbers.

![Slide 14](assets/gagliardi2022-star-forward-upgrade-talk/slide14.png)

**Slide 14.** Photos of FCS construction and installation (HCal module assembly, back-side readout cabling, forward view through the STAR bore).

*Figure description (from the image):* Photo collage, five photos plus NSF logo, no captions or numbers. (1) Top left: a masked worker leaning over a long steel absorber assembly with many regularly spaced slots, another person behind holding a long thin strip (plausibly a scintillator plate), laptop on a side table. (2) Bottom left: five masked people in blue lab coats posing around a stacked block of slotted absorber plates. (3) Top centre: a person crouched in front of a tall wall of green circuit boards mounted in a grid on the calorimeter back face. (4) Bottom centre: close-up of the back face with dense multicoloured (orange, blue, purple, yellow) cabling running into black cable ports. (5) Right: wide-angle view through a large circular steel bore along the beam pipe (with bellows and support brackets), looking toward walls of green readout boards, with thick black flexible hoses in the foreground.

**FCS readout and commissioning [s15].**
- Photo of an electronics rack with dense cabling.
- **"LED mapping check":** ECal and HCal hit maps "View from Back", in columns (North ↔ South) by rows. ECal axes run ≈ −22…+22 columns and −1…−34 rows; HCal axes run ≈ −13…+13 columns and −1…−20 rows. The LED-pulsed channels form deliberate character-like patterns in each half; any mis-cabled channel would break the pattern.
- **"Online monitoring plots during 7.7 GeV Au+Au"** (stamped Sun Mar 7 16:49:59 2021):
  - ECal occupancy map ("35-Row" vs "+-Col North <-> South"), highest near the beam gap at column 0;
  - ECal ADC (0–500) vs time bin (0–100), with the signal band at time bin ≈ 50.
- During Run 21 the team exercised the online machinery, monitoring systems and slow controls; offline and Monte Carlo machinery were also in place; the trigger system was commissioned.
- The FCS was ready to go on Run 22 day 1, except for some gain tweaks.

![Slide 15](assets/gagliardi2022-star-forward-upgrade-talk/slide15.png)

**Slide 15.** FCS readout rack, LED channel-mapping patterns in the ECal and HCal, and Run-21 online monitoring (ECal occupancy and ADC vs time bin) from 7.7 GeV Au+Au.

*Figure description (from the image):* Layout: tall photo of a rack (left), two LED-mapping hit maps (centre column), two online monitoring plots (right), NSF logo top right, bullets below. Rack photo: densely cabled rack with yellow-faced modules and bundles of white and teal cables. "Ecal View from Back": x "+-Col (North <-> South)" −20…20, y "-Row (Bottom <-> Top)" −5…−30 ticks, z colour scale 1–10^6; red/orange cells (high counts) form letter-like line patterns in each half against a blue background, but I cannot read them as definite characters. "Hcal View from Back": x −10…10, y −2…−20, colour 1–10^6; each half shows a symmetric loop shape in rows ≈−2…−10 and a crossed shape in rows ≈−12…−20 (unreadable as characters). "Ecal" occupancy: x "+-Col North <-> South" −20…20, y "35-Row" 0…≈34, colour 1–10^6, a "fcs_Ecal" tooltip overlay; mostly yellow-orange with red maximum around the central gap, a few white (empty) cells scattered. "Ecal" ADC vs "Timebin": x 0–100, y "ADC" 0–500, colour 1–10^6; a narrow vertical high-count band at time bin ≈48–52 spanning all ADC values, flared at low ADC, with sparse blue points elsewhere. Both monitoring plots stamped "Sun Mar 7 16:49:59 2021".

### Part 2 — What science will the STAR Forward Upgrade enable? [s16–s35]

**Physics program [s17]** (forward rapidity, 2.5 < η < 4).
- **A+A** (beam: full-energy Au+Au) topics:
  - temperature dependence of the viscosity through flow harmonics up to η ~ 4;
  - longitudinal decorrelation up to η ~ 4;
  - global Λ polarization and its strong rapidity dependence.
- **p+p and p+A** (beam: 500 GeV p+p; 200 GeV p+p and p+A) topics:
  - Sivers asymmetries for hadrons, (tagged) jets and di-jets;
  - TMD measurements at high x: transversity → tensor charge;
  - GPD E_g: gluon spin-orbit correlations;
  - gluon PDFs for nuclei: R_pA for direct photons and Drell–Yan;
  - tests of saturation predictions through di-hadrons and γ-jets.
- Observables:
  - charged and neutral hadrons;
  - inclusive jets and di-jets;
  - hadrons in jets;
  - photons;
  - Drell–Yan and J/ψ di-electrons;
  - Λs;
  - mid-forward and forward-forward rapidity correlations.
- Running periods:
  - STAR alone: 2021–22, 500 GeV polarized pp, a 20-week "Run 22".
  - STAR in parallel with sPHENIX: 2023 and 2025, 200 GeV Au+Au; 2024, 200 GeV polarized pp and p+Au.

**Why TMD phenomena? [s18].** Plot: x f₁(x, k_T, S_T) density in the (k_x, k_y) plane (−0.5 to 0.5 GeV) for u and d quarks in a transversely polarized proton. The u-quark density is shifted toward +k_x and the d-quark density toward −k_x (Sivers shift). Motivation:
- image the transverse and longitudinal (2+1D) structure of the nucleon and of nuclei ("Tomography of the nucleon!");
- access transverse momenta at non-perturbative scales, probing at the confinement scale;
- TMDs exhibit correlations that arise from spin-orbit effects.

**Separating initial- and final-state effects [s19].**
- *Sivers or twist-3 mechanisms* are sensitive to correlations between proton spin and parton transverse motion. Signatures: A_N for jets or direct photons; A_N for W^±, Z⁰ and Drell–Yan; A_N for heavy flavor (gluon). The Sivers function is not universal: its sign changes from SIDIS to W, Z and Drell–Yan.
- *Collins or novel fragmentation-function (FF) mechanisms* are sensitive to transversity. Signatures: the Collins effect; interference fragmentation functions (IFF); A_N for pions (→ novel FF). The Collins function is predicted to be universal.

**Color interactions in QCD [s20].** Controlled non-universality of the Sivers function:
- DIS has a final-state interaction (opposite colors attract); Drell–Yan, W or Z have an initial-state interaction (like colors repel).
- Hence Sivers_DIS = −Sivers_Drell-Yan (or −Sivers_W, −Sivers_Z). This is a critical test of factorization and an opportunity to visualize the repulsive interaction between like color charges.
- Direct photons are sensitive to similar physics, but not via TMDs.
- All of these observables can be explored in 510 GeV pp collisions at RHIC.
- **[note]** "510 GeV" here vs "500 GeV" elsewhere: 510 GeV is the actual pp energy and 500 GeV the nominal label.

**Transversity and the Collins FF [s21].**
- Transversity δq(x) = Δ_T q(x) is the quark polarization along the spin of a transversely polarized proton. It is the third collinear leading-twist distribution.
- Its integral gives the tensor charge, a critical input for low-energy beyond-the-Standard-Model calculations. The difference between helicity and transversity is directly related to parton orbital angular momentum.
- Transversity is chiral-odd, so there is much less data than for helicity.
- The Collins FF is an azimuthal modulation of hadron fragments and an excellent testing ground for TMD factorization, universality and evolution.
- Before STAR, transversity had been observed only in SIDIS + e⁺e⁻.
- Several recent global analyses, all with large uncertainties:
  - Collins-effect SIDIS input: PRD 93, 014009 (2016); PRD 92, 114023 (2015); PRD 102, 054002 (2020);
  - IFF SIDIS + STAR pp input: PRL 120, 192001 (2018).
- Plot: x h₁(x, Q²) for u (peak ≈ 0.2–0.25 at x ≈ 0.2–0.35) and d (minimum ≈ −0.13 at x ≈ 0.15–0.2), showing "Kang et al (2015)" (red) and "Anselmino et al (2013)" (blue dotted) with uncertainty bands.

**TMD PDFs and FFs [s22].**
- Plot: Q² (1–10⁴ GeV²) vs x (10⁻⁴–1), "current data for Collins and Sivers asymmetry":
  - COMPASS h^± (P_hT < 1.6 GeV), HERMES π^{0,±}, K^± (P_hT < 1 GeV), JLab Hall-A π^± (P_hT < 0.45 GeV), JLab 12;
  - STAR 500 GeV and 200 GeV, −1 < η < 1 Collins; STAR 500 GeV and 200 GeV, 1 < η < 4 Collins; STAR W bosons;
  - EIC lines for √s = 140 GeV and 45 GeV (0.01 ≤ y ≤ 0.95).
- Sivers effect: unpolarized partons with a spin-dependent intrinsic k_T. Collins effect: correlation between the polarization of a scattered quark and the momentum of a hadron fragment transverse to the quark momentum.
- Before STAR, TMDs came only from fixed-target ep data (high x, low Q²); measurements at high Q² and over a broad x range are needed.
- STAR mid- plus forward rapidity gives excellent kinematic overlap with future EIC measurements. The Forward Upgrade gives access to quarks up to x ~ 0.5 and gluons down to x ~ 0.005.
- High-precision data in pp and DIS@EIC are needed to establish TMD universality.

**Inclusive transverse spin asymmetries at forward rapidities [s23].**
- Left, STAR PRD 103, 092009: π⁰ A_N vs x_F (0–0.7) with ⟨p_T⟩ vs x_F, comparing:
  - STAR 500 GeV and 200 GeV, 2.7 < η < 4.0 ("This Paper");
  - STAR 200 GeV, ⟨η⟩ = 3.7 and 3.3;
  - RHICf 510 GeV, η > 6;
  - PHENIX 62.4 GeV, 3.1 < η < 3.8;
  - E704 19.4 GeV.
  - A_N rises to ≈ 0.1–0.15 at high x_F.
- Right: predicted asymmetries for π^± from Kanazawa et al., PRD 89, 111501, for 3 < η < 4. π⁺ reaches A_N ≈ +0.12 and π⁻ ≈ −0.10, for 200 GeV (solid) and 500 GeV (dashed), over x_F ≈ 0.2–0.7.
- These asymmetries come from an interplay of the initial-state Sivers distribution (or its twist-3 analog, the Efremov–Teryaev–Qiu–Sterman, ETQS, function) and the final-state Collins effect (or the related twist-3 function H_FU).
- A_N for h^±, direct photons and π⁰ can constrain the evolution and flavor dependence of the ETQS distribution and determine the role of H_FU.

**TMDs at forward rapidity [s24].**
- STAR PRD 103, 092009, π⁰ A_N (p↑+p → π⁰+X, p_T > 2 GeV/c, 2.7 < η < 4.0): isolated vs non-isolated π⁰ at 200 and 500 GeV, with theory bands. The 3.0/3.4% beam-polarization scale uncertainty is not shown.
- STAR PRD 103, 092009, EM-jet A_N (anti-k_T R = 0.7, p_T^jet > 2 GeV/c, 2.9 < η^jet < 3.8): 200 and 500 GeV, photon multiplicity > 2, and A_N^DY 500 GeV.
- Boglione et al., PLB 815, 136135: Sivers first moments (SIDIS vs SIDIS + jet, GPM and CGI-GPM).
- STAR finds A_N lower for non-isolated π⁰ and for higher-multiplicity EM-jets. This gives substantial constraints on the Sivers effect at high x and raises the question of an additional mechanism producing large A_N for isolated π⁰.
- STAR has also measured a small Collins asymmetry for π⁰ in EM-jets (not shown).
- The Forward Upgrade will enable forward-rapidity asymmetry measurements of charge-tagged jets and di-jets, the hadron-in-jet Collins asymmetry, and diffractive processes with rapidity gaps.

**How well can the Forward Upgrade do? [s25].**
- STAR projection: PYTHIA anti-k_T R = 0.6, √s = 510 GeV, jet p_T > 4 GeV/c, η = 2.5–4, P = 60%, L = 350 pb⁻¹. Shows A_N, A_N^{h+} and A_N^{h−} vs x_F = p_z/p_beam (0.15–0.65).
- The projections are drawn on twist-3 predictions from Gamberg, Kang, Prokudin at η = 2.5: A_N^down ≈ +0.004 and A_N^up ≈ −0.004 to −0.005 at x_F ≈ 0.45–0.6.
- The measurement is A_N for full jet reconstruction combined with charge-sign tagging of a hadron fragment with z > 0.5. It gives up to 10σ separation between plus-tagged and minus-tagged jet A_N.
- **[note]** This projection assumes P = 60% and 350 pb⁻¹. Slide 51 reports a planned 55% and an achieved polarization in the upper 40s.

![Slide 25](assets/gagliardi2022-star-forward-upgrade-talk/slide25.png)

**Slide 25.** Projected statistical precision for charge-tagged forward-jet A_N vs x_F in 510 GeV pp, overlaid on twist-3 predictions.

*Figure description (from the image):* Single ROOT plot: y axis A_N, −0.01 to 0.01; x axis "x_F = p_z/p_beam", ticks 0.2–0.6 (frame ≈0.13–0.68); dashed zero line. Points (statistical error bars only) at x_F = 0.15, 0.25, 0.35, 0.45, 0.55, 0.65 for A_N (black), A_N^{h+} (red) and A_N^{h−} (blue); legend for curves "Gamberg, Kang, Prokudin: η = 2.5": A_N (black), A_N^up (red), A_N^down (blue), drawn only for x_F 0.2–0.6. Read-off (≈): blue points 0.0024, 0.0040, 0.0043, 0.0037 at x_F 0.25–0.55 and 0.0025 ± ≈0.005 at 0.65; red −0.0010, −0.0025, −0.0037, −0.0047 and −0.0056 ± ≈0.0025 at 0.65; black ≈0.0014, 0.0014, 0.0005, −0.0011 and −0.0033 at 0.65, the black curve crossing zero at x_F ≈ 0.48. Error bars are ≈±0.0002 at x_F = 0.25, growing to ≈±0.0007 at 0.55. At x_F = 0.15 the points lie off the curves (red ≈ +0.0010, blue ≈ −0.0008, black ≈ +0.0002).

**Di-jet Sivers effect [s26].**
- Plot (STAR Preliminary, 2012+2015, +z/−z combined, statistical uncertainties only, di-jet p_T > 6 GeV/c and 4 GeV/c): ⟨k_T⟩ [MeV/c] vs η^total (−4 to 6) for u quark, d quark and gluon+sea. The averages are u ≈ +30, d ≈ −65 and gluon+sea ≈ +5 MeV/c (≈).
- STAR made the first-ever observation of the Sivers effect in di-jet production. Mid-rapidity results at √s = 200 GeV show that up and down quarks have opposite-sign spin-dependent ⟨k_T⟩: ⟨k_T⟩_d ~ −2⟨k_T⟩_u, and gluon + sea quarks have ⟨k_T⟩ ~ 0.
- η^total = η₁ + η₂ ~ ln(x₁/x₂). Mid-rapidity STAR covers only |η₁ + η₂| < 3; the Forward Upgrade gives access to |η₁ + η₂| ~ 6 and so samples much higher (and lower) x.
- **[note]** −2 × (+30) = −60, consistent with the ≈ −65 average ✓ (eyeballed).

**Collins effect at high x [s27–s28].**
- [s27] Predicted Collins asymmetries vs z for 3.0 < η_jet < 4.0 in three bins: 4.0 < P_T,jet < 5.0, 5.0 < P_T,jet < 7.0 and 7.0 < P_T,jet < 9.0 GeV/c. Red curves are positive and blue negative; the asymmetries reach ≈ ±0.05 at high p_T (dashed blue down to ≈ −0.12 in the highest bin). Black triangles show the z binning.
- [s28] adds the projected statistical uncertainties for A_N of h⁺ and h⁻ in jets vs hadron z (0.1–0.9), for 2.5 < η_jet < 4.0. These are ≈ ±0.0002 at low z, growing to ≈ ±0.001–0.0015 at z ≈ 0.85. Per p_T bin:
  - 4.0 < p_T,jet < 5.0: ⟨x₁⟩ = 0.294, ⟨x₂⟩ = 0.034;
  - 5.0 < p_T,jet < 7.0: ⟨x₁⟩ = 0.354, ⟨x₂⟩ = 0.034;
  - 7.0 < p_T,jet < 9.0: ⟨x₁⟩ = 0.395, ⟨x₂⟩ = 0.036.
- Extending Collins measurements to forward rapidity gives direct access to transversity in 0.3 < x < 0.5. This region has never been explored in SIDIS and is essential to constrain experimental measurements of the nucleon tensor charge.
- The same data give "Collins-like" asymmetries, with similar uncertainties, that access linearly polarized gluons in transversely polarized protons down to x ~ 0.005.

**GPD E_g [s29].**
- Left (STAR preliminary): A_N^γ vs W_γp (5–40 GeV) for p↑Au → e⁺e⁻pAu at √s_pN = 200 GeV, |y| < 1. It shows γp → J/ψ p data at ⟨p_T^J/ψ⟩ = 0.48 GeV/c (A_N ≈ 0.05 ± ≈ 0.2 at W ≈ 24 GeV, statistical uncertainty only), the Lansberg et al. curve (peak ≈ 0.38 at W ≈ 8 GeV) and a Run-24 projection point at W ≈ 14 GeV.
- Right: STARlight p↑Au, γp↑ cross-section (arb. units) vs W_γp for −1 < η < 1, −1 < η < 2.2, and −1 < η < 2.2 plus 2.5 < η < 4. Adding forward coverage extends the acceptance down to W ≈ 8 GeV, where the cross section is largest.
- Exclusive J/ψ A_N in 200 GeV ultra-peripheral p+Au collisions is sensitive to the GPD E_g, at Q² ~ 10 GeV² and 10⁻⁴ < x < 10⁻¹. E_g determines gluon spin-orbit correlations in the proton.
- STAR made a proof-of-principle measurement with the TPC in 2015. The Forward Upgrade will enable the measurement at smaller W_γp, where both the cross section and the signal are expected to be much larger.

**Nuclear PDFs [s30–s31].**
- [s30] Q² vs x map of existing nuclear data (A ≥ 56): W/Z pPb at 5 TeV (LHCb, CMS/ATLAS, ALICE), νA DIS, DY (E772, E866, E906), eA DIS, JLab-12. It also shows the STAR-pA DY region at √s = 200 GeV, STAR direct photons at 2.8 < η < 3.8, a "RHIC pA y≤4" boundary, EIC lines at √s = 90 and 45 GeV, and a saturation line.
- The Forward Upgrade enables R_pAu measurements for direct photons and Drell–Yan at √s_NN = 200 GeV:
  - direct photons constrain the nuclear gluon distribution over 0.0025 ≲ x ≲ 0.025;
  - Drell–Yan di-electrons constrain the nuclear sea-quark distribution over 0.001 ≲ x ≲ 0.01.
- [s31] Projections:
  - Direct photons in pA at 2.5 < η < 4.5: R^γ_p+Au statistical uncertainties at √s_NN = 200 GeV vs p_T = 2–8 GeV/c. Inset scale ±0.02 at low p_T; the uncertainties grow to ≈ ±0.1–0.15 at p_T ≈ 7–8 GeV/c. Luminosity scenarios: recorded 2015 L_pp = 100 pb⁻¹ and L_pAu = 0.45 pb⁻¹; delivered L_pp = 293 pb⁻¹ and L_pAu = 1.76 pb⁻¹; and combined.
  - Drell–Yan in pA at 2.5 < η < 4.5: nuclear modification factor R^DY_pA (DY signal) vs M_pair = 4–10 GeV with ≈ 1 central values. Uncertainties are small at low mass and ≈ ±0.6 at M ≈ 9 GeV.
  - Impact on EPPS16 at Q² = 10 GeV²: R_g^Au and R_sea^Au vs x (10⁻⁵–1), EPPS16 vs EPPS16 including STAR pseudo-data. The bands shrink noticeably for x ≈ 10⁻³–10⁻¹.
  - Precision measurements of the nuclear gluon and sea-quark distributions are essential for a stringent test of nPDF universality at the EIC.
- **[source issue]** The panel headings on [s31] say 2.5 < η < 4.5, while the Forward Upgrade coverage is 2.5 < η < 4 elsewhere in the talk, and [s30] labels direct photons 2.8 < η < 3.8. These are probably older projection plots made for a different acceptance assumption.

![Slide 31](assets/gagliardi2022-star-forward-upgrade-talk/slide31.png)

**Slide 31.** Projected R_pAu precision for forward direct photons and Drell–Yan di-electrons, and their impact on the EPPS16 nuclear gluon and sea-quark ratios.

*Figure description (from the image):* Four plots: top left direct-photon R_p+Au projection, top right Drell–Yan R_pA projection, each with a blue arrow to an EPPS16 impact plot below ("to constrain gluons", "to constrain sea quarks"), separated by a vertical blue line. Direct photons: y axis 0.8–1.15, x "p_T (GeV/c)" 2–8+, header "R_p+Au: statistical uncertainties, √s_NN = 200 GeV"; vertical bars centred at 1 for cyan (recorded 2015), teal (delivered) and blue (combined), at p_T ≈ 2.6–8.4 GeV/c; inset (0.98–1.02 scale) magnifies the first five bins; bars grow with p_T, and the last bar at p_T ≈ 8.4 GeV/c spans the full frame (beyond ±0.15). Drell–Yan: y "Nuclear Modification Factor (R^DY_pA)" 0–2, x "M_pair / GeV" 4–10, legend "DY signal"; 11 points at 1 from M ≈ 4.2 to 9.3 GeV with error bars growing from ≈±0.01 to ≈±0.6. Lower plots: "R_g^Au(x,Q²=10 GeV²)" and "R_sea^Au(x,Q²=10 GeV²)", y 0–1.5, x 10^-5–1 (log), cyan band EPPS16, blue band "EPPS16 including STAR pseudo-data", red central curve; the sea panel has a dotted line at 1. Gluon central curve ≈0.75 at low x, peak ≈1.15 at x ≈ 0.1, dip ≈0.8 near x ≈ 0.6; cyan band ≈0.5–1.05 at low x vs blue ≈0.65–0.85. Sea central curve ≈0.7 at low x, peak ≈1.03 near x ≈ 0.1, dip ≈0.6 near x ≈ 0.6; blue band only modestly narrower than cyan.

**[note]** In the image the gluon band narrows over the whole low-x range shown (10^-5 to ≈3×10^-2), not only for x ≈ 10^-3–10^-1, while the sea-quark band narrows only modestly; and the last direct-photon bar (p_T ≈ 8.4 GeV/c) extends beyond the plotted ±0.15 rather than ≈±0.1–0.15 (all eyeballed).

**Probing non-linear effects in QCD [s32]** (STAR, arXiv:2111.10396).
- Cartoons of p+p vs p+A di-jet topologies.
- C(Δφ) for forward π⁰π⁰ at √s_NN = 200 GeV, 2.6 < η < 4, comparing pp, pAl and pAu:
  - low p_T: p_T^trig = 2–2.5 GeV/c, p_T^asso = 1–1.5 GeV/c;
  - high p_T: p_T^trig = 2.5–3 GeV/c, p_T^asso = 2–2.5 GeV/c.
- Relative area vs E.A. (ΣE_BBC) for pAu/pp and pAl/pp, and relative area vs A^{1/3} for p, Al and Au, with p_T^trig = 1.5–2 GeV/c, p_T^asso = 1–1.5 GeV/c, Δφ ∈ [π/2, 3π/2]. The fitted slope is P = −0.09 ± 0.01, falling from 1 (p) to ≈ 0.57 (Au).
- Forward rapidities at STAR are a unique opportunity to study very high gluon densities with an unambiguous probe: the disappearance of the backward jet in p+A.
- STAR π⁰–π⁰ correlations show strong suppression at low p_T in p+A, where gluon saturation is expected, and no suppression at high p_T (larger x), outside the non-linear domain.
- Such hadro-production measurements are essential to explore the universality of non-linear effects at the EIC. The Forward Upgrade will enable similar studies with h^±–h^±, di-jets and γ-jet.

**Flow in Au+Au to constrain η/s [s33].**
- Left: ηT/(ε+P) vs T for four parametrizations:
  - (ηT/(ε+P))_min = 0.04, a = 0, b = 10;
  - 0.12, a = 0, b = 0;
  - 0.04, a = 10, b = 0;
  - 0.04, a = 10, b = 2.
  - The RHIC regime is near T ≈ 0.15–0.2 GeV and LHC at higher T.
- Right: v₂(η) for 0–6. PHOBOS Au+Au 200 GeV (0–40%) data, 3D hydro η/s(T) param-1…4, and a "Run 2023 STAR Projection 10 B" (10 billion events) at η ≈ 2.7–3.9 in the FTS region. The FTS band spans η ≈ 2.5–4 and the EPD band ≈ 2.1–5.1.
- η/s is expected to be smallest in the RHIC energy regime. Forward flow is sensitive to the temperature dependence of η/s. STAR measurements will be far more precise than the earlier PHOBOS ones.

**Longitudinal structure of the initial state [s34].**
- r_n(η_a, η_b) = V_nΔ(−η_a, η_b)/V_nΔ(η_a, η_b), where V_nΔ is the Fourier coefficient from pairs of particles in different rapidity ranges.
- Plot vs η_a/Y_beam (0–1):
  - 0–5% CMS Pb+Pb 2.76 TeV for n = 2 and 3;
  - 3D-Glasma and Torque (WNM) model curves;
  - 0–5% STAR run-23 Au+Au 200 GeV projection, 10 B events (n = 2 at r ≈ 0.92 and n = 3 at r ≈ 0.84 markers in the iTPC range);
  - iTPC, FTS and EPD ranges marked.
- r_n is sensitive to the initial-state input. The 3D glasma model gives weaker decorrelation and describes CMS r₂ but not r₃; the wounded-nucleon model gives stronger decorrelation than the data.
- A precise measurement over a wide rapidity window will provide a stringent constraint.

**Global vorticity transfer [s35].**
- P_H [%] vs η for STAR Au+Au √s_NN = 200 GeV, 20–60% centrality (40–80% for 2.5 < η < 4).
- Models: Λ geometric model (rising toward forward η), Λ PICR hydro, Ξ⁰ AMPT, Ω⁻ AMPT.
- Data: Λ and Λ̄ (≈ 0.2–0.35%). Run-2023 projections for Λ+Λ̄, Ξ⁻+Ξ̄⁺ and Ω⁻+Ω̄⁺ at mid-rapidity (iTPC) and at η ≈ 2.8, 3.3 and 3.8 (FTS).
- Questions: how is the global vorticity transferred to the fluid, and how does the fluid's local thermal vorticity become spin angular momentum? The rapidity dependence of Λ global polarization probes this. Initial geometry and local thermal vorticity + hydro predict opposite trends.

### Part 3 — How well are we doing during Run 22? [s36–s51]

**STAR online pages [s37–s43].** Screenshots of the STAR Online Web Server (online.star.bnl.gov; page last modified 01/06/2022 12:02:54) used to show juniors where to look:
- the URL [s37];
- RunLog Browser and Electronic ShiftLog [s38];
- RHIC Performance Plots [s39–s40]: Accelerator Performance Plots of RHIC beam, luminosity and main dipoles over the last 4, 24 and 168 hours. "This and all following sample screen shots are from mid-afternoon on Saturday."
- DAQ monitoring [s41–s42];
- Online QA histograms [s43].

**What is STAR doing "right now"? [s42].** DAQ status page for run **23043055**, production_pp500_2022 [PHYSICS], started Sat Feb 12 14:11:43 2022, running ≈ 22 min at the screenshot. Warning on the slide: the page often lags on first opening; hit "Auto Update Now" a few times until the message times at the bottom are current. Trigger table excerpt (DAQ Hz = recorded rate; L0 Hz; Sca Hz = raw scaler rate; Sca Dead = scaler deadtime):

| Trigger | DAQ evts | DAQ Hz | L0 Hz | Sca Hz | Sca dead |
|---|---|---|---|---|---|
| fcsJP2 | 180460 | 159 | 148 | 1711 | 14% |
| fcsJPA1 / fcsJPA0 | 35572 / 35266 | 33 / 27 | 29 / 29 | 5653 / 57680.2 | 15% / 14% |
| fcsJPBC1 / fcsJPBC0 | 70965 / 70169 | 58 / 66 | 59 / 58 | 7037 / 63081.2 | 15% / 14% |
| fcsJPDE1 / fcsJPDE0 | 69743 / 69368 | 56 / 55 | 59 / 57 | 3092 / 26201.1 | 14% / 14% |
| fcsDiJP | 126737 | 80 | 86 | 524 | 7% |
| fcsDiJPAsy | 130525 | 107 | 106 | 1601 | 6% |
| fcsDY | 578553 | 446 | 433 | 435 | 7% |
| fcsDYNoEpd | 78065 | 57 | 61 | 785 | 7% |
| fcsJPsi | 154405 | 109 | 117 | 1703 | 8% |
| fcsHad2 / Had1 / Had0 | 80126 / 80979 / 80572 | 56 / 66 / 61 | 56 / 61 / 61 | 579 / 6375 / 171773.6 | 7–8% |
| fcsEM2 / EM1 / EM0 | 142010 / 157892 / 159934 | 103 / 113 / 116 | 106 / 117 / 121 | 120 / 427 / 5516 | 4–7% |
| fcsEM2_tpc / EM1_tpc / EM0_tpc | 13830 / 13182 / 13380 | 10 / 8 / 12 | 11 / 10 / 11 | 120 / 427 / 5516 | 10–14% |
| fcsELE2 / fcsEM3 | 1203 / 1204 | 1 / 1 | 1 / 1 | 54744.2 / 76450.3 | 7% |
| fcsEHT-N / -S, fcsHHT-N / -S | 1–3 each | 0 | 0 | 19058.1 / 19573.1 / 159430.6 / 179962.6 | 7% |
| upcJpsiNS / upcJpsiSN | 2833 / 2517 | 3 / 0 | 6 / 0 | 4 / 3 | 0% / 67% |
| **ALL** | 2856702 | **2238** | 2222 | 9383505.7 | 0% |

- Mid-rapidity triggers seen in the same table include BHT3 (64 Hz DAQ, 57 Hz scaler), BHT1*VPDTAC30 (91 Hz), JP2 (85 Hz), EHT1 (18 Hz), dimuon (236 Hz), zerobias, VPD, BBC, ZDC and EPD.
- Detector table: TOF 1785 Hz, BTOW 2227 Hz, Trigger 2222 Hz, ETOW 2243 Hz. Event builders evb01–04 at 139–181 Hz each.
- The message log shows iTPC RDO auto-recoveries, "TOF: recovery: also setting FCS BUSY!", and "FOB 2 (R#14:F#81) NOT found -- power-cycle ROB #14 …".
- **[note]** Checks:
  - The run number decodes as STAR convention 23 = Run 22 and day 043 = 12 Feb 2022 ✓.
  - fcsDY alone is 446/2238 ≈ 20% of the recorded rate. Its scaler rate (435 Hz) ≈ its L0 rate (433 Hz), so it is effectively unprescaled. fcsJPsi (1703 → 117 Hz), fcsJP2 (1711 → 148 Hz) and fcsHad2 (579 → 56 Hz) are prescaled.
  - The trigger names are the slides' only information on the FCS trigger menu: jet patches (JP), di-jet, Drell–Yan (with and without the EPD preshower), J/ψ, EM and hadron thresholds, and ECal/HCal high towers. The talk does not define the thresholds.
  - The phone status bar reads 1:33 PM, while the log times are ≈14:31. This is consistent with the speaker reading the page from US Central time (my inference).

![Slide 42](assets/gagliardi2022-star-forward-upgrade-talk/slide42.png)

**Slide 42.** Live STAR DAQ page for Run-22 pp500 run 23043055, showing per-trigger rates, including the FCS triggers (fcsDY, fcsJPsi, jet patches, EM/hadron triggers).

*Figure description (from the image):* Two overlapping iPad Safari screenshots of online.star.bnl.gov placed side by side (status bar "1:33 PM Sat Feb 12", 69% battery); the right screenshot is scrolled right to show the second half of the trigger table and the message column. Blue header bar: "RUNNING [to RCF]", 23043055, production_pp500_2022 [PHYSICS], Run started Sat Feb 12 14:11:43 2022, Duration 0 days, 0 hr, 22. Left sidebar: STAR DAQ logo, menu (Monitoring, Rate Charts, Current Rates, LED Status, Slow Controls, Current RunLog, Today's ShiftLog, Critical Support, TPC Gating Grid, DAQ Plots, Jeff's Plots, STP Monitor, DET Status, ETOF), green "RUNNING 23043055" status, Auto Update and Run Playback controls, credit "Tonko Ljubicic/BNL". Main trigger table columns: Trigger, DAQ Evts, DAQ Hz, L0 Evts, L0 Hz, Sca Hz, Sca Dead, Built, Xpress, Abt, Err; ALL row highlighted in blue. Below: detector table (Det, State, Dead, CPU, Evts, Evts In, Hz, MB/s EVB, Err, MB/s RDO) and event-builder table (Evb, State, Built, EvtsIn, Err, Hz, MB/s, Written, Free GB, RCF W+S; e.g. Free GB 20062 [93%], 10770 [85%], 8976 [82%]); message log (Time, #, Node, Severity, Task, Source#line, Message) with OPERATOR-level iTPC, TOF and FOB messages from 14:11:52 to 14:31:47. Blue warning text at right as transcribed. Numbers I checked against the note's table match.

**What do the FCS data look like online? [s44].** Online QA (run 23043055, running for 34.1 minutes):
- HCal occupancy map, columns ≈ −13…+13, rows −1…−20;
- ECal occupancy map, columns ≈ −22…+22, rows ≈ −1…−34;
- preshower ("Pres", Phi-Row vs column, ≈ 16 columns × 12 rows per side) occupancy map.
- All three are nearly uniformly populated. One HCal tower is low (≈ column 10, row −4), and a few preshower channels are empty or low near the central gap (≈ column −1 to −2, rows −3 to −5). These are eyeballed.

![Slide 44](assets/gagliardi2022-star-forward-upgrade-talk/slide44.png)

**Slide 44.** Online FCS occupancy maps (HCal, ECal, preshower) from Run-22 pp500 running.

*Figure description (from the image):* Screenshot of the STAR online QA (Jevp) browser: header "Live…", "(23043055:production_pp500_2022:running for 34.1 minutes)", progress bar, buttons Run Log…, Calendar…, << >> Live; tab rows "l4 / shift", then Summary, CriticalShiftPlots (selected), DAQ, Trigger, Centrality, Bunch_Crossings, TPC, BEMC, epd, EEMC, ESMD, TOF, MTD, BBC, GMT, FCS, sTGC, FST, and sub-tabs MTD, BTOW, ETOW, ESMD, VPD, TOF, FCS (selected), FST, STGC. Three 2D maps with log colour scales: "Hcal" (x "+-Col North <-> South" −13…13, y "-Row" −1…−20, colour 1–10^6), "Ecal" (x −22…22, y "-Row" −1…−34, colour 1–≈3×10^5), both stamped "Sat Feb 12 14:45:36 2022", and "Pres" (x −16…16, y "Phi/-Row", colour 1–10^6). HCal and ECal are yellow-orange with highest (red) occupancy next to the central beam gap; one HCal cell at ≈ column 10, row −4 is cyan (≈10^2–10^3). Preshower is uniformly red-orange over rows −2…−11, with an empty cell at ≈ column −3, row −3, cyan (low) cells at ≈ column −3, row −4 and column −1, row −3, and the innermost column on each side of the gap filled only in alternate rows.

**[note]** The preshower map shows populated rows −2…−11 (10 rows) over columns ≈ ±16, not 12 rows; the alternating filled/empty pattern in the innermost columns looks systematic (geometry or mapping) rather than random dead channels, but the slide does not explain it.

**FST online [s45].**
- Max ADC time bin (mostly bins 1–2 of 0–3);
- max ADC distribution (peak ≈ 500 ADC, tail to 4000);
- number of time bins (≈ 3);
- hit maps for disks 1–3 (disk 3 shows a missing wedge-shaped region, ≈);
- signal vs channel for disks 1–3;
- random RMS vs channel for disks 1–3 (≈ 20–30 ADC).

**sTGC online [s46–s48].** Hits per plane (4 planes, flat), per quadrant, per FOB (front-end board, ≈ 1–96), per VMM ("VMM index (96 VMM / Plane)", ≈ 0–380), and per time bin (two timing windows: −400…400 and −100…40).
- [s47]: the dips in the hits-per-FOB (≈ FOB 29) and hits-per-VMM (≈ VMM 100–110) plots are real. The horizontal chamber for one quadrant of plane 2 stopped holding voltage "this past week" and will need to be repaired, or replaced with a spare, before Run 23.
- [s48]: much more real-time information is available for these and all other subsystems (FCS, sTGC and FST tabs).

**Offline data at present [s49].**
- **Di-photon invariant mass** for FCS ECal clusters (vertex z = 0; plot date Feb 9, 2022), "shows a clear π⁰ peak". Histogram h1_inv_mass_cluster: Entries 647091, Mean 0.1781, RMS 0.0939. Peak at ≈ 0.135 GeV, height ≈ 8700 counts/bin, on a broad background extending to 0.4 GeV.
- **Correlation between MIPs in the ECal and HCal:** distribution of Y(ECal) − Y(HCal) (histogram "DYX_py": Entries 1.212861e+07, Mean 0.3358, RMS 15.48; range −30 to 30, units not given). It peaks at 0 (≈ 105 × 10³) above a flat ≈ 30 × 10³ background.
- **HCal spectrum in coincidence with an ECal MIP** ("EngEcalCoin_HcalN", box label "+1.08V"; log scale, x from 0 to 3, units not given). Fit = falling background + Gaussian-like peak:
  - Entries 835498, Mean 0.5739, RMS 0.5472, χ²/ndf = 581.3/191;
  - A = 3010 ± 7.5, x0 = 0.8251 ± 0.0010, p = −2.243 ± 0.009;
  - peak = 485.4 ± 6.9, mean = 1.574 ± 0.006.
  - An arrow at x ≈ 1.5 is labelled "Expected HCal MIP location".
- The speaker hopes to see analogous offline FST and sTGC results soon.
- **[note]**
  - The fitted MIP mean (1.574) lies close to the expected position (arrow ≈ 1.5), but no energy unit or calibration constant is given. "+1.08V" plausibly labels a SiPM bias setting; this is my interpretation, as the slide does not explain it.
  - The π⁰ peak position ≈ 0.135 GeV is eyeballed. No fitted mass or width is given; the Mean/RMS in the stat box are for the whole histogram including background.
  - χ²/ndf = 581.3/191 ≈ 3.0.

![Slide 49](assets/gagliardi2022-star-forward-upgrade-talk/slide49.png)

**Slide 49.** First offline FCS results from Run 22: the ECal di-photon π⁰ peak, ECal–HCal MIP position matching, and the HCal MIP peak in ECal-MIP-coincident events.

*Figure description (from the image):* Three ROOT plots. Left: "invariant mass plot for FCS ECal cluster (vertex z 0)", x "invariant mass [GeV]" 0–0.4, y counts 0–9000, stamp "…d Feb 9 11:54:07 2022" (first characters cut off); histogram rises from ≈0.01 GeV, shows a shoulder ≈4500–5000 at ≈0.07–0.1 GeV, a sharp peak of ≈8750 at ≈0.13–0.14 GeV, then a falling tail to ≈1550 at 0.4 GeV. Top right: panel "DY", x Y(ECal) − Y(HCal) −30…30 (units not printed), y ×10^3 with suppressed zero (axis starts ≈13×10^3, ticks 20–100); very spiky histogram with strong bin-to-bin alternation, baseline ≈20–50×10^3, broad enhancement over ≈ −8…+8 with the maximum bin ≈107×10^3 at 0. Bottom right: "EngEcalCoin_HcalN", x 0–3 (units not printed), log y ≈70–4000; data off-scale above the frame for x < ≈0.7 (sharp rise near x ≈ 0–0.1 at left), then falling; fit drawn from x ≈ 0.72 to 3: blue falling background, magenta bell-shaped peak (max ≈485 at x ≈ 1.57, spanning ≈0.77–2.38), red total following the data. Blue arrow under x = 1.5 labelled "Expected HCal MIP location". Stat/fit-box numbers as transcribed in the note.

**How are we doing relative to our goals? [s50–s51].**
- [s50] points to the Luminosity Tracker link.
- [s51] shows four integrated-luminosity plots (15 Dec 2021 to 06 Apr 2022, as of Saturday Feb 12, 2022, 15:10). The red line is the goal, the black curve the delivered/sampled value and the green dotted line the projection. Values are eyeballed:

| Trigger / quantity | Goal at 06 Apr | Status on 12 Feb | Projection at 06 Apr |
|---|---|---|---|
| BHT3, L [pb⁻¹] | ≈ 400 | ≈ 150 | ≈ 350 |
| BHT3, P²L [pb⁻¹] | ≈ 120 | ≈ 36 | ≈ 83 |
| EHT1, P²_blue L [pb⁻¹] | ≈ 120 | ≈ 35 | ≈ 85 |
| fcsDY, P²_blue L [pb⁻¹] | ≈ 120 | ≈ 39 | ≈ 95 |

- About 3 weeks were lost to accelerator issues: the cryogenics upgrade delayed cool-down by two weeks, and there were failures of 2 of 4 coils in the Blue 9 o'clock snake and of the AGS Siemens MG. As a result, integrated luminosity is behind goals.
- Polarization has been lower than anticipated (upper 40s % vs a planned 55%). Since it enters squared in the polarized figure of merit (FoM), the integrated FoM is further behind goals.
- Commissioning has gone very well, and STAR is running smoothly.
- STAR has requested a 4-week extension, which projects to 90% of the FoM goal.
- **[note]** Checks:
  - (0.45–0.49 / 0.55)² = 0.67–0.79, so the lower polarization alone costs ≈ 20–33% of the FoM.
  - 15 Dec → 06 Apr is 112 days (16 weeks), while [s17] quotes a 20-week Run 22. The difference is presumably cool-down/set-up time outside the physics-goal window; the slides don't say.
  - Rough check of the extension: the BHT3 P²L projection rises ≈ 83 pb⁻¹ over ≈ 95 days (≈ 0.87 pb⁻¹/day). Four more weeks add ≈ 24, giving ≈ 107/120 ≈ 89% of the goal ✓ (≈ 90%).

![Slide 51](assets/gagliardi2022-star-forward-upgrade-talk/slide51.png)

**Slide 51.** Run-22 integrated luminosity and polarization-weighted luminosity (BHT3, EHT1, fcsDY) vs goals, as of 12 Feb 2022, with the list of accelerator problems and the request for a 4-week extension.

*Figure description (from the image):* Left 2 × 2 grid of ROOT plots of integrated luminosity vs "day" (x ticks 15/Dec, 12/Jan, 09/Feb, 09/Mar, 06/Apr), each with a thin red straight goal line from 0 at 15 Dec, a black measured curve up to ≈12 Feb, and a green dotted linear projection to 06 Apr that starts from zero in early January. Panels: "BHT3" y "L [pb⁻¹]" 0–600; "BHT3" y "P² L [pb⁻¹]" 0–180; "EHT1" y "P²_blue L [pb⁻¹]" 0–180; "fcsDY" y "P²_blue L [pb⁻¹]" 0–180. Timestamps "Sat Feb 12 15:10:31 2022", "15:10:32", "15:10:32", "15:10:33"; the fcsDY stamp is boxed with an arrow to "As of Saturday, Feb 12, 2022 15:10". The fcsDY black curve stays at zero until ≈ late December, later than the others. Read-off values as in the note's table (consistent with the image). Right: bullet text as transcribed.

### Conclusion [s52]

The physics-program graphic from [s17] is repeated. Conclusions:
- The STAR Forward Upgrade enables a wide range of high-impact measurements in polarized pp, polarized and unpolarized p+Au, and Au+Au collisions.
- The Forward Upgrade is running well and taking good data.
- "Stay tuned to see what we learn!"

---

## Checks

**(a) Forward upgrade components and coverage.**
- Coverage 2.5 < η < 4 (same as the EIC hadron arm), where STAR previously had only Pb-glass EM calorimetry [s4].
- Four new subsystems [s4]:
  - FST: 3 Si disks × 12 modules, 3 Hamamatsu mini-strip sensors per module, ~1.5% X₀ per disk, APV25-S1 readout, IST DAQ and cooling reused [s5];
  - sTGC: 4 planes × 4 pentagonal double-sided modules, x/y/u strips, < 200 μm resolution, ~0.5% X₀ per layer, VMM readout, ATLAS-like, CO₂ + n-pentane gas [s7, s10];
  - FCS ECal: 1496 PHENIX PbSc towers with SiPMs [s12];
  - FCS HCal: 520 Fe/Sc towers with SiPMs [s12].
- Preshower signals are split from the EPD for triggering [s12].
- The FCS sits ≈ 7 m from the IP in two movable halves [s12].
- Simulated tracking: charge mis-ID < 6% (8%) and p_T resolution < 35% for p_T < 5 GeV/c at 500 (200) GeV [s11]; see the [note] there on the 200 GeV values.

**(b) FCS HCal and ECal design.**
- ECal: Pb/Sc sampling with 66 cells of 1.5 mm Pb / 4 mm Sc, 36 WLS fibers per tower, 5.52 × 5.52 cm towers (33 cm length on the slide — see [source issue]), 18 X₀, 0.85 λ_I, PMTs replaced by SiPMs.
- HCal: Fe/Sc 20 mm / 3 mm, 10 × 10 × 84 cm towers, ≈ 4.5 λ_I, same SiPM readout as the ECal, developed with EIC R&D [s12].
- Electronics: "new ADC + trigger electronics" [s4]. The talk does **not** mention DEP boards, SiPM type or bias. The DEP counts (24 per half for the ECal, 9 per half for the HCal) come only from [ruan2026-fcs-specs-email-note](ruan2026-fcs-specs-email-note.md).
- Trigger: FCS triggers exist for jet patches, di-jets, DY, J/ψ, EM, hadron and high-tower thresholds, with rates on [s42]; the preshower comes from the EPD. Thresholds are not given.
- Comparison with the email (table under s12–s13): all counts, the HCal geometry and the ECal sampling structure agree. The ECal tower face is 5.52 cm vs 5.542 cm (rounding). The talk's ECal length (33 cm) and λ (0.85) differ from the email (37.73 cm, 0.93 λ); my estimate from the layers is ≈ 0.90 λ.
- Resolution requirements [s4]: ECal ~10%/√E (pp, pA) and ~20%/√E (AA); HCal ~50%/√E + 10%.

**(c) Physics goals and what the HCal enables.**
- Jets need the HCal. Specifically:
  - full forward jet reconstruction with charge-tagged hadrons (z > 0.5) for Sivers A_N, with projected up-to-10σ separation of plus- and minus-tagged jet A_N at 510 GeV, P = 60%, 350 pb⁻¹ [s25];
  - di-jet Sivers at |η₁ + η₂| ~ 6 [s26];
  - hadron-in-jet Collins asymmetries probing transversity at 0.3 < x < 0.5 and linearly polarized gluons down to x ~ 0.005 [s27–s28];
  - di-jets and γ-jet for saturation [s32].
- e/h discrimination (ECal + HCal + tracking) enables Drell–Yan di-electrons:
  - R_pAu constraining nuclear sea quarks over 0.001 ≲ x ≲ 0.01 [s30–s31];
  - Sivers sign change via DY [s19–s20];
  - J/ψ for GPD E_g in ultra-peripheral p↑Au [s29].
- Direct photons give R_pAu for nuclear gluons over 0.0025 ≲ x ≲ 0.025 [s30].
- A+A: forward flow for η/s(T) [s33], decorrelation r_n [s34], and Λ global polarization [s35].
- The Run-22 FCS triggers include fcsDY (≈ 446 Hz recorded, ≈ 20% of the DAQ bandwidth) and fcsJPsi, plus several jet-patch and di-jet triggers [s42].

**(d) Run 22 status and performance numbers** (as of 12 Feb 2022).
- The FCS was installed in 2020 and commissioned in Run 21 (7.7 GeV Au+Au; brief O+O and d+Au at 200 GeV). It was ready on Run 22 day 1 except for gain tweaks [s13, s15].
- Online maps for the FCS, FST and sTGC are healthy apart from the issues listed in (e) [s44–s48].
- Offline:
  - ECal di-photon π⁰ peak at ≈ 0.135 GeV (647091 entries) [s49];
  - ECal–HCal MIP matching, Y(ECal) − Y(HCal) peaked at 0 (RMS 15.48 over ±30) [s49];
  - HCal MIP peak fitted at 1.574 ± 0.006 against an expected ≈ 1.5 (units not given) [s49].
- sTGC test-stand efficiency: 98.7% (X) and 98.2% (Y), claimed > 97% [s8].
- Trigger rates: total ≈ 2238 Hz to DAQ; FCS trigger rates as in the [s42] table.
- Luminosity: integrated lumi and FoM behind goal. Polarization in the upper 40s vs 55% planned; ≈ 3 weeks lost; a 4-week extension requested, projecting to 90% of the FoM goal [s51].
- No calibrated energy resolution or calibration constants are shown for the ECal or HCal. The only resolution figures are the design requirements on [s4].

**(e) Issues.**
- One sTGC quadrant chamber (horizontal chamber, plane 2) stopped holding HV in the week before 12 Feb 2022; it needs repair or replacement before Run 23 [s47].
- The sTGC gas uses flammable n-pentane (flash point −49 °C, explosive limits 1.5–7.8%, boiling point 36.1 °C), which requires extreme care; the gas system nonetheless survived power failures and storms [s10].
- On the online maps: one low HCal tower and a few dead/low preshower channels [s44], and a missing wedge region in the FST disk-3 hit map [s45] (all eyeballed, not discussed by the speaker).
- The DAQ log shows TOF recovery setting FCS BUSY and an sTGC/FOB "NOT found" message [s42].
- The talk says **nothing** about SiPM radiation damage, SiPM noise/dark-current growth, annealing or temperature control. Questions on SiPM radiation tolerance must be answered from other sources.
- Accelerator issues (cryogenics, Blue snake coils, AGS MG) and low polarization are the main Run-22 concerns [s51].

---

## References

Cited on the slides (journal references as printed; author names only where the slide gives them):

- STAR Collaboration, Phys. Rev. D 103, 092009 (2021) — forward π⁰ and EM-jet A_N [s23, s24].
- Kanazawa et al., Phys. Rev. D 89, 111501 — predicted π^± A_N [s23].
- Boglione et al., Phys. Lett. B 815, 136135 — Sivers function from SIDIS + jets [s24].
- Phys. Rev. D 93, 014009 (2016); Phys. Rev. D 92, 114023 (2015); Phys. Rev. D 102, 054002 (2020) — Collins-effect SIDIS global analyses [s21].
- Phys. Rev. Lett. 120, 192001 (2018) — IFF SIDIS + STAR pp transversity analysis [s21].
- STAR Collaboration, arXiv:2111.10396 — forward π⁰–π⁰ correlations in p+p, p+Al, p+Au [s32].
- Named in plot legends without a full citation: Kang et al. (2015) and Anselmino et al. (2013) transversity fits [s21]; Gamberg, Kang, Prokudin twist-3 predictions [s25]; Lansberg et al. [s29]; STARlight [s29]; EPPS16 [s31]; PHOBOS Au+Au 200 GeV v₂(η) [s33]; CMS Pb+Pb 2.76 TeV r_n, 3D-Glasma and Torque (WNM) models [s34]; PICR hydro and AMPT [s35]; STAR Preliminary di-jet Sivers 2012+2015 [s26].
