---
title: "Tsai 2015 — Development of a forward calorimeter system for the STAR experiment (full-content paraphrase)"
type: raw-source
source_type: paper
authors: "O.D. Tsai, E. Aschenauer, W. Christie, L.E. Dunkelberger, S. Fazio, C.A. Gagliardi, S. Heppelmann, H.Z. Huang, W.W. Jacobs, G. Igo, A. Kisilev, K. Landry, X. Liu, M.M. Mondal, Y.X. Pan, M. Sergeeva, N. Shah, E. Sichtermann, S. Trentalange, G. Visser, S. Wissink (21 authors)"
journal: "J. Phys.: Conf. Ser. 587 (2015) 012053 — Proceedings of CALOR 2014, Giessen, 6–11 April 2014"
doi: 10.1088/1742-6596/587/1/012053
arxiv: none
captured_via: "Route 3 — IOP publisher PDF (no HTML full text, no arXiv version); text from pdftotext -layout, in-figure numbers from 400-dpi renders, figures cropped from 200-dpi renders"
captured_date: 2026-11-06
captured_as: full-content paraphrase
figures: "12 (vision descriptions added 2026-11-06)"
vision_model: "general-purpose subagent (session model, not recorded), 2026-11-06"
---

# Development of a forward calorimeter system for the STAR experiment (Tsai et al., CALOR 2014) — reading note

- **Citation:** O.D. Tsai, E. Aschenauer, W. Christie, L.E. Dunkelberger, S. Fazio, C.A. Gagliardi, S. Heppelmann, H.Z. Huang, W.W. Jacobs, G. Igo, A. Kisilev, K. Landry, X. Liu, M.M. Mondal, Y.X. Pan, M. Sergeeva, N. Shah, E. Sichtermann, S. Trentalange, G. Visser and S. Wissink, "Development of a forward calorimeter system for the STAR experiment". The 21st author is **S. Wissink** (Indiana University, CEEM). This list was confirmed from page 1 of the PDF and from the IOP `citation_author` metadata (21 names, same order). Corresponding e-mail: tsai@physics.ucla.edu.
- **Affiliations:** (1) UCLA: Tsai, Dunkelberger, Huang, Igo, Landry, Liu, Pan, Sergeeva, Shah, Trentalange. (2) BNL: Aschenauer, Christie, Fazio, Kisilev. (3) Texas A&M: Gagliardi, Mondal. (4) Penn State: Heppelmann. (5) Indiana University, CEEM: Jacobs, Visser, Wissink. (6) LBNL: Sichtermann.
- **Journal ref:** J. Phys.: Conf. Ser. **587** (2015) 012053. Proceedings of the 16th International Conference on Calorimetry in High Energy Physics (CALOR 2014), Giessen, Germany, 6–11 April 2014. Open access (CC-BY 3.0). **DOI:** [10.1088/1742-6596/587/1/012053](https://doi.org/10.1088/1742-6596/587/1/012053)
- **arXiv:** none found. I searched arXiv by title words ("forward calorimeter" STAR, all fields and title field), which gave no results. An author search for "Tsai, O D" gave 194 hits, all STAR Collaboration physics papers and none of them this proceeding.
- **Route used:** Route 3 (PDF only).
  - Route 1 failed. The IOPscience article page has no HTML full text for this 2015 JPCS article: the page carries only the abstract, metadata and a PDF link, about 3.6 k characters of page text.
  - Route 2 failed because there is no arXiv version.
  - Text was taken from `pdftotext -layout`. Figure-internal numbers (fit legends, statistics boxes) were read from 400-dpi renders of the PDF pages.
- **PDF backup:** `assets/tsai2015-fcs-prototype/source.pdf` (IOP publisher PDF, 7 254 938 bytes, 11 pages). PDF page 1 is an IOP cover page that IOP added, so paper pages 1–10 are PDF pages 2–11.
- **Figures:** `assets/tsai2015-fcs-prototype/fig1.png` … `fig12.png`. They were cropped from 200-dpi `pdftoppm` renders of the PDF, because there are no HTML figures. Every crop was checked by eye and contains the figure without its caption.
- **Verification:** every number, unit and caption below was checked against `pdftotext -layout` of the PDF. Fit results printed inside Figs. 8, 9, 10 and 12 are not in the text layer; they were read from 400-dpi renders and are marked "(read from figure)". The paper has **no numbered equations and no tables**. The only formulas are the fit functions printed in the Fig. 10 legend and the Fig. 12 caption, reproduced below as unnumbered display equations. Discrepancies are tagged **[source issue]**.
- Figure descriptions were added by a separate figure pass that looked at the images.

---

## Abstract (paraphrase)

The paper reports an R&D programme for a Forward Calorimeter System (FCS) for STAR at RHIC. The FCS is meant to be a very compact, compensated, finely segmented, high-resolution calorimeter system for the p+p and p+A programme.

- **Prototype:** it has an electromagnetic (EM) and a hadronic part.
- **EM section:** tungsten powder with scintillating fibres.
- **Hadronic calorimeter (HCal):** a conventional Pb/scintillator-plate sandwich.
- **Readout:** Hamamatsu MPPCs for both sections.
- **Test:** a full-scale prototype was tested with beam at FNAL in March 2014. The paper gives the design, the construction technique and the test-beam performance.

---

## Full content

### 1. Introduction

STAR is a large-acceptance RHIC detector. Over the coming years it will keep evolving through upgrades towards better detection capability and broader kinematic coverage, for p+p, p+A and A+A running and for the initial phase of an Electron-Ion Collider (EIC) [1]. The forward upgrade is driven mainly by QCD physics at very high or very low Bjorken $x$. Its core is the Forward Calorimeter System (Fig. 1), which is to detect neutral pions, photons, electrons, jets and leading hadrons over **pseudorapidity 2.5–4.5**. The design is driven by detector performance, integration into STAR and cost.

**FCS concept as proposed in 2014**

- **Layout:** a Spaghetti EM calorimeter (**SPACal**) followed by a **lead/scintillator-plate sampling HCal**.
- **Compensation:** both the EM and the HCal sections are said to be **compensated** calorimeters. Compensation, which requires a small sampling fraction, gives the best possible energy measurement for single hadrons while keeping the system compact.
- **EM sampling:** to get good EM resolution, the sampling frequency in the EM section is kept high by using scintillating-fibre (ScFi) technology.
- **SPACal construction:** tungsten powder and scintillating fibres in spaghetti geometry. The authors developed a new construction technique for this under an EIC generic detector R&D project [2]. A prototype module was tested at FNAL in early 2012 with satisfactory performance [2]. Development continued for two more years under STAR forward-upgrade R&D, and the technique is now judged mature enough to mass-produce W/ScFi modules.
- **SPACal size:** **120 × 80 towers**. The active volume of one tower is about **2.5 cm × 2.5 cm × 17 cm**, corresponding to **23 X0**.
- **HCal size:** lead and scintillating tiles; each tower is **10 cm × 10 cm × 81 cm**, corresponding to **4 interaction lengths**. There are **30 × 20 HCal towers**, covering the same area as the SPACal.
- **HCal sampling:** the sampling fraction and frequency were **copied from the ZEUS Pb/Sc prototype [3]**.
- **HCal construction:** a new technique lets the HCal be built by stacking tiles in situ, which eases integration into STAR. Mechanical parts, and the construction and operating resources needed from the collaboration, are kept to a minimum to fit the expected budget and resource limits.

![Fig. 1](assets/tsai2015-fcs-prototype/fig1.png)

**Fig. 1.** The planned STAR upgrade with a Forward Calorimeter System; only the West side of STAR is drawn.

*Figure description (from the image):* Engineering line drawing, side elevation of the West half of STAR with the beam axis horizontal at mid-height. Scale bar at top left labelled METERS, 0–5 in 1 m steps (alternating 0.5 m black/white segments). Printed labels: MTD (top and bottom), EMC ELECTRONICS, MAGNET, COIL (twice), EMC, EMC END CAP, TPC, WTOF, WEST BBC, WEST START DETECTOR, ROMAN POT, EMCAL, HCAL, EM and HAD (on the calorimeter block), POLETIP CARRIAGE, and the truncated labels "…WARD …CKING DISKS" (left edge) and "WEST WAL…" (right edge). Dashed lines from the interaction point carry tiny labels that read ETA=1.000 and ETA=2.000 (at the limit of resolution). A bold "FCS" annotation with an arrow points to the calorimeter block beyond the West Start Detector, just in front of the West Wall: a hatched EMCAL layer (labelled EM) in front of a solid grey HCAL block (labelled HAD), on a support stand. Scaled from the bar (my measurement; the η lines converge at the bar's 0): EMCAL front face ≈7.1 m from the IP, HCal block ≈7.4–8.2 m, so the drawn HCal depth is ≈0.8 m, consistent with the 81 cm towers. No 2.5–4.5 pseudorapidity lines are drawn.

**[note]** The left edge of the image cuts the "0" of the scale bar and the forward-tracking-disk label, and the right edge cuts "WEST WALL". The truncation is either in the crop or in the original figure; nothing physics-relevant is lost.

**[note] Geometry checks (ticked)**

- SPACal transverse size: 120 × 2.5 cm = 3.0 m by 80 × 2.5 cm = 2.0 m. HCal: 30 × 10 cm = 3.0 m by 20 × 10 cm = 2.0 m. The two match, consistent with "the same area". ✓
- Tower counts: 9600 SPACal and 600 HCal.
- SPACal effective radiation length: 17 cm / 23 X0 = **0.74 cm per X0**. Pure W has X0 = 0.35 cm. The W-powder/epoxy/fibre mixture is therefore about half as dense in X0 terms as solid W. The paper gives no W-powder or epoxy density and no fibre fraction; see ref. [2].

### 2. Description of FCS prototypes

#### EM section construction

The EM construction technique is described in detail in [2]. In brief:

1. A matrix of scintillating fibres is formed.
2. Absorber powder is poured into the matrix.
3. The residual air in the powder is replaced by epoxy, which makes the assembly rigid.

Different fibre arrangements and very fine sampling structures are easy to make. The resulting W/ScFi composite has mechanical properties close to structural steel, so hermetic, self-supporting structures can be built from it. For the FCS EM section the group developed a way to build **superblocks of four towers at once**. The technique is considered ready for industrialisation.

#### HCal mechanics

The HCal section is a stack of absorber and scintillator plates. The assembly is likened to building the whole HCal block layer by layer from LEGO-like parts. Figure 2 shows the mechanical structure of the HCal mechanical prototype.

![Fig. 2](assets/tsai2015-fcs-prototype/fig2.png)

**Fig. 2.** HCal mechanical structure.

*Figure description (from the image):* Black-and-white photograph of the HCal mechanical prototype on a table, seen from the front and slightly above. The near face is two equal square steel front plates separated by a narrow vertical gap that holds a thin light-coloured plate seen edge-on (consistent with the WLS plate that the text places between adjacent towers). On top, a flat steel master plate with rows of protruding steel dowel pins and open holes covers most of the stack. At the right rear, where the master plate is absent, the edges of the individual stacked plates and their dowel pins show as a comb of alternating light and dark layers. No labels, scale or dimensions are printed.

- **Plate positioning:** holes in the bottom base plate locate the absorber plates. Each absorber plate has four dowel-pin holes, two at the bottom and two at the top. **Steel dowel pins of 5 mm diameter** position the absorber plates relative to the bottom base plate and the top steel master plates.
- **Master plates:** one master plate covers **one and a half rows** of HAD towers. It interlinks all absorber plates within a tower, the front and back steel plates of the HAD section, and adjacent rows of HAD towers.
- **Absorber:** plates **10 mm** thick, of **lead–antimony alloy (4% Sb)**, painted with white diffuse reflective paint (Sherwin Williams F63WC134).
- **Scintillator:** the gap between adjacent absorber plates is **3.1 mm**. Scintillator plates **2.5 mm** thick (**EJ-212**) sit in these gaps.
- **Layer count:** one HCal tower has **63 absorber plates and 64 scintillator plates**.
- **Light collection:** the scintillation light of one tower is collected by a **3 mm thick wavelength-shifting (WLS) plate (EJ-280)** placed in the gap between two adjacent HCal towers (Fig. 2).
- **No load on optics:** all scintillator and WLS plates "float" within their layer and carry no mechanical load.
- **Assembly at the beam line:** Fig. 3 shows the assembled HCal prototype. It was assembled in place at the FNAL test beam to validate the technique. Four people took about **eight hours** to build the **sixteen-channel** prototype from parts on site.

![Fig. 3](assets/tsai2015-fcs-prototype/fig3.png)

**Fig. 3.** A sixteen-channel HCal prototype.

*Figure description (from the image):* Black-and-white photograph of the assembled HCal prototype on a table, viewed obliquely from one side. The long side shows a dense stack of thin vertical white-painted plates held by horizontal tie rods running the length of the module, and the top is covered with protruding dowel pins. The near end face (right) is a steel plate divided into vertical columns that carry small fittings. A box labelled "LIFT-A-LOFT" is in the background. No scale, labels or dimensions are printed.

#### HCal light collection

The HCal light collection was optimised for uniform and efficient collection from every tile along the tower depth.

- **Air-gap coupling:** all optical connections in the HCal are through a thin air gap, except the coupling of the SiPMs to the WLS plate.
- **Reflectors:** the best reflector combination for the WLS plate was white diffuse reflector (**Bicron BC-620**) at the far end (away from the photodetector) and **aluminised mylar** on the back side (opposite the tile edges). The mylar also optically isolates HCal towers within a layer.
- **Uniformity filter:** to make the light collection uniform **within 10%** along the tower depth, a **variable-density filter printed on clear mylar** is placed between the tiles and the WLS plate. MC shows that without it the HCal energy resolution degrades by **about a factor of two above 20 GeV** compared with an ideal detector.
- **Tolerances:** a tile-to-tile light variation within 10% has negligible effect on the resolution. Bench tests show that variations of the thin tile–WLS air gap, which come from the mechanical tolerances needed for assembly, also have a negligible effect.
- **No wrapping:** unwrapped tiles between painted absorber plates collected light as efficiently as tiles wrapped in Tyvek.

#### Readout (both sections)

A new compact readout was developed for the FCS. Both sections use silicon photomultipliers: Hamamatsu Multi-Pixel Photon Counters (MPPC) **S10931-025P**. These are very compact, fast, insensitive to magnetic field and sufficiently radiation-hard for FCS readout in STAR [4].

- **Light yield:** the EM prototype gave **2000 p.e./GeV** in the 2012 test run, measured with a very efficient light collection scheme and PMTs.
- **MPPC count:** the authors estimated that **4 MPPCs per EM tower** and **8 MPPCs per HCal tower** collect enough light to make photostatistics a negligible contribution to the resolution.
- **Geometric efficiency:** the ratio of the active area of the MPPCs to the output area of the light-collecting element is **8.2% for the HCal** (eight MPPCs on the WLS plate) and **~21% for the EMcal towers**.

**[note] Geometric-efficiency check**

- EM: 4 × (3 × 3 mm²) = 36 mm² against the 13 × 13 mm² = 169 mm² output face of the light guide (given later in this section) gives **21.3%** ✓.
- HCal: 8 × 9 mm² = 72 mm². An 8.2% efficiency implies an output area of about 880 mm². A 3 mm thick WLS plate read out along a 10 cm tower edge has an output face of only 300 mm², which would give 24%. **The 8.2% cannot be reproduced** from the dimensions given. It might include the pixel fill factor or a different output geometry; the paper does not say.

#### EM light collection

A WLS-plate scheme gives perfect light mixing in the HCal towers. The EM section is different: the MPPCs collect the fibre light through a short (**25 mm long**) light guide/mixer. A bench test before the run showed that the non-uniformity of this scheme could reach **20%**, between the hottest spots directly under the MPPCs and the tower corners. The group nevertheless kept this scheme, to measure the absolute MPPC-based light yield, and planned to redesign the EM light collection after the run. The optical, mechanical and electrical integration of the two readouts is described next.

![Fig. 4](assets/tsai2015-fcs-prototype/fig4.png)

**Fig. 4.** Compact HCal readout. Left: the HCal FEE board coupled to a WLS plate with Dow Corning 3145 RTV. Right: eight MPPCs mounted on the HCal FEE board.

*Figure description (from the image):* Two black-and-white photographs side by side. Left: a dark HCal FEE board mounted vertically against a steel plate at the end of the HCal stack; the white-painted plates recede behind it, and a thin white plate (the WLS plate) protrudes edge-on above the board's centre. The board's silkscreen is unreadable. Right: close-up of the FEE board face with eight square SiPM packages in one vertical column, numbered 0–7 in two groups of four (0–3 upper, 4–7 lower). Each package is flanked by two large plated holes and labelled D3–D6 / D7–D10, R49–R52 / R100–R103 and C28–C31 / C52–C55. Each group of four has two multi-pin ICs with resistor arrays to its right; the IC labels are unreadable. There are four corner mounting holes, and the board marking reads "101483 / 35-13 / 002-005 / MADE IN USA". No scale. Matches the caption (eight MPPCs on the HCal FEE board).

#### Front-end electronics

Two different front-end electronics (FEE) sets read the MPPCs during the test run.

**HCal FEE (Fig. 4)**

- **Design goal:** low power, reliable, and low-cost integration into a large system.
- **Bias:** an unregulated **90 VDC** input is regulated to the required SiPM bias, set by **two DAC channels**, one of which includes a **thermistor**. Both the voltage and the **temperature-compensation slope** that keeps the SiPM gain constant are therefore programmable.
- **Preamplifier:** signals from **four SiPMs are summed directly** at the input of one preamplifier, a regulated common-base stage with **BFR92A** transistors.
- **Input impedance:** very low, a few Ω. The high capacitance of the four SiPMs in parallel (**1.3 nF**) therefore does not limit the charge collection time, as it would with a 50 Ω input.
- **Output:** a differential driver gives a **4 V peak-to-peak** signal over low-cost, low-mass twisted-pair cable to an external ADC system. The large swing and differential interface keep the high dynamic range robust against external EMI or ground noise.

**EM FEE (Fig. 5)**

- **Gain matching:** the four MPPCs of each EM tower were grouped to have the same gain at the same bias.
- **Bias:** **a single bias voltage served all sixteen channels**, with a simple resistive divider setting the bias of each tower. **There was no temperature compensation of the bias for the EM prototype.**
- **Summing:** the analogue signals of the four MPPCs were summed with an **OPA691** op-amp.
- **Mounting:** the MPPCs were mounted on the FEE board, calibrated, then potted in **Dow Corning Sylgard 184** silicone. The silicone layer (**~2 mm**) acts as an optical cookie and as a spring that holds the board against the light guide with one plastic screw, visible at the centre of the light guide in Fig. 5.
- **Light guide:** not fully optimised before the run. It is an **acrylic truncated pyramid**, **25 mm** high, with a **25 mm × 25 mm** base and a **13 mm × 13 mm** top. The MPPC centres are **7 mm** apart. Geometric efficiency is about **21%**.

![Fig. 5](assets/tsai2015-fcs-prototype/fig5.png)

**Fig. 5.** Compact EM readout: an EM FEE board with four MPPCs attached to a light guide.

*Figure description (from the image):* Black-and-white close-up photograph looking through the clear acrylic truncated-pyramid light guide onto the EM FEE board. The view shows an apparent 4 × 4 array of square MPPC packages with small SMD parts. Only the central 2 × 2 are seen directly through the top face; the outer ring is formed by reflections in the four inclined faces. The silkscreen labels "D1" and "D2" read normally above the central pair and mirror-reversed at the left and right edges; the lower labels are partly hidden and unreadable. A round clear plastic object sits at the centre between the four sensors, consistent with the plastic screw mentioned in the text, and its reflections appear at the sides. No scale.

**[note]** The apparent sixteen sensors in Fig. 5 are reflections. The board carries four MPPCs, as the caption says.

**[note]** Four S10931-025P devices at 1.3 nF give about 325 pF each, consistent with the ~320 pF terminal capacitance of a 3 × 3 mm², 25 µm-pixel MPPC (datasheet value, not from this paper). Each device has 3 mm / 25 µm = 120 → 120² = **14 400 pixels**.

### 3. Preliminary results of the test run.

#### Setup

The FCS and an EM prototype of a central-barrel calorimeter for a dedicated EIC detector were tested at the FNAL test beam facility in **March 2014** as **experiment T1018**. Data analysis and MC comparison were still in progress.

- **EIC barrel prototype:** built with the same technique as the FCS EM prototype, but with **wedge-shaped towers** as needed for a cylindrical barrel.
- **Readout position:** upstream of the incoming beam for the FCS prototype; downstream for the EIC EM prototype.
- **Shared FEE:** the same MPPC FEE assemblies read out both EM prototypes.

![Fig. 6](assets/tsai2015-fcs-prototype/fig6.png)

**Fig. 6.** Left: an eighteen-channel, **18 X0** deep EM prototype of the central-barrel calorimeter for a dedicated EIC detector. Right: a sixteen-channel, **23 X0** deep prototype of the forward EM calorimeter for the FCS. Both use similar light collection and front-end electronics.

*Figure description (from the image):* Black-and-white photograph of two EM prototype modules on a granite table (plate "STANDRIDGE GRANITE CORP."). A wooden ruler in front is marked in cm from 0 to beyond 27 and printed "Made in U.S.A." and "falcon auburn, maine 04210". Left module, labelled "EIC BEMC": an aluminium box whose open face shows 3 rows × 6 columns = 18 acrylic truncated-pyramid light guides, with the fibre-end dot pattern visible through each. Right module, labelled "STAR Forward Upgrade": 4 × 4 = 16 light guides. Matches the caption (left: 18-channel EIC barrel prototype; right: 16-channel FCS EM prototype).

- **Beam:** the FCS response to hadrons, electrons and muons was measured at **3–32 GeV**.
- **Electron ID:** a differential Cherenkov counter (standard equipment at the MTBF).
- **Impact position:** a scintillator XY hodoscope of **4.9 mm wide square scintillator rods** read by **SensL SiPMs**.
- **Upstream material:** minimised to about **4 cm of scintillation counters**. FTBF staff also installed **He-filled beam pipes** between the apparatus and the upstream Cherenkov.
- **Monitoring:** the initial setup is shown in Fig. 7. Two MTBF **MWPCs** (one is visible in Fig. 7) monitored the reproducibility of the beam settings during energy scans.
- **Geometry:** the HCal was set at a fixed **2.5°** angle between the beam and the tower axis. The EM prototype was attached to the HCal front steel plate with its tower axis at **4°** to the beam.
- **LED monitoring:** every FCS channel had an LED monitor. LED and pedestal events were recorded continuously at about **1 Hz** for most of the run. Preliminary analysis shows the HCal and EMcal FEE gains were stable to **better than 1%** over a typical **twelve-hour** shift.

![Fig. 7](assets/tsai2015-fcs-prototype/fig7.png)

**Fig. 7.** The FCS HCal prototype on the beam line. The Pb-glass calorimeter in front of the HCal was used for initial beam studies.

*Figure description (from the image):* Black-and-white panoramic photograph of the FNAL test-beam line. Overlaid white labels, left to right: "He Pipe" (striped beam pipe on stands), "MWPC" (chamber on a frame), "Sc Hodoscope" (small detector on a post), "Pb Glass" (black box with a cylindrical phototube housing; its small label plate is unreadable) and "FCS HCal" (large dark-framed box with many cables, on a scissor-lift table). An EXIT sign is visible. The order of the labelled items implies the beam arrives from the left. No EM prototype is visible in front of the HCal in this initial setup, consistent with the caption.

#### Calibration

All MPPCs were tested with a laser system before the run. The gains of the MPPC assemblies for both the HCal and EM prototypes were set equal **within 1%**.

**EM prototype:** no extra tower-by-tower beam calibration was needed. This was expected after the 2012 test, which showed excellent internal homogeneity of EM modules built with this technique.

**HCal:** extra tower-by-tower calibration with MIPs was required.

- **Method:** an absorber was inserted in the beam (the **8 GeV muon mode of the MT6 line**). A MIP peak was selected in each tower with an isolation requirement: one muon hit in a tower and no other energy anywhere in the HCal. The EM prototype was removed from the beam for this.
- **Size of corrections:** large, about **20%** on top of the pre-run calibration.
- **Alignment:** about **10%** of the shift is attributed to WLS-plate–MPPC alignment. Both have a **3 mm** active dimension, and a misalignment of about **250 µm** is possible from placing the MPPCs on the FEE board.
- **Optical components:** the rest is attributed to the quality of the optical components. One possible cause is a tower-to-tower difference in WLS response: dopant concentration and attenuation length were not measured for every WLS plate and were assumed identical.

#### Hadron response

The FCS hadron response is shown in Fig. 8. In an ideal, fully compensated system the reconstructed hadron energy is simply the sum of the EM and HCal depositions, assuming the response in both sections is the same and energy-independent.

- **EM weighting:** for the best hadron resolution, the EM weighting factor had to be **energy-dependent**. It goes from **about 2 to 1.2** between **3 and 20 GeV** and is flat above that.
- **e/h:** with this weighting, the measured FCS **e/h ratio is close to 0.95** and almost constant **above 10 GeV** (Fig. 8, right).

![Fig. 8](assets/tsai2015-fcs-prototype/fig8.png)

**Fig. 8.** FCS prototype response to hadrons. Left: HCal energy deposition (y) vs EMcal energy deposition (x) for 12 GeV hadrons. Centre: weighted EM + HCal energy sum for 12 GeV hadrons. Right: ratio of the FCS response to electrons and to hadrons (e/h) vs beam energy.

*Figure description (from the image):* Three ROOT panels. Left: 2D histogram with y "HCalSum" 0–4000 and x "ECalSum" 0–4000 (no units); the grey-scale z axis runs 0 to ≈42 (ticks 0–40 in steps of 5). It shows two populations. One is a dense vertical band at ECalSum ≈ 0–100 spanning HCalSum ≈ 100–3000, densest at ≈1300–2600, with a compact spot at HCalSum ≈ 200–300. The other is a diffuse anti-correlated band running from (ECalSum ≈ 100, HCalSum ≈ 2000) to (≈3500, ≈0). Centre: 1D histogram with no axis titles, x 0–6000 and y 0–60. Stat box "CalSumAllCuts": Entries 12403, Mean 1767, RMS 633.3, χ²/ndf 393.9 / 423, Constant 45 ± 0.6, Mean 1912 ± 3.9, Sigma 367 ± 3.4. It has a narrow peak near x ≈ 300 (height ≈35–45) and a broad main peak at ≈1900, fitted with a Gaussian (solid curve over ≈1100–2800). Right: y "Ratio of response e/h" 0–1.2, x "Beam Energy (GeV)" 0–35. Ten filled circles with no visible error bars at 3, 4, 6, 8, 10, 12, 16, 20, 25 and 32 GeV; my readings are ≈0.98, 0.90, 0.87, 0.91, 0.90, 0.935, 0.915, 0.92, 0.945 and 0.94.

**[note]** The Fig. 8 stat-box values agree exactly with the note's "Values read from Fig. 8". The beam energy (12 GeV) is not printed on the left or centre panel; it comes from the caption. Above 10 GeV the plotted e/h points are ≈0.90–0.945, slightly below the text's "close to 0.95".

**[note] Values read from Fig. 8**

- **Centre panel ("CalSumAllCuts"):** Entries 12403; Mean 1767; RMS 633.3; χ²/ndf 393.9/423. Gaussian fit: Constant 45 ± 0.6, Mean 1912 ± 3.9, Sigma 367 ± 3.4. This gives σ/E = 367/1912 = **19.2% at 12 GeV** ✓, consistent with the Fig. 10 hadron fit (0.58/√12 + 0.015 = 18.2%).
- **Right panel:** the e/h points lie between about 0.87 and 0.98: ≈0.98 at 3 GeV, ≈0.87–0.91 at 4–10 GeV, and ≈0.92–0.94 at 12–32 GeV (approximate readings).
- **What this ratio is:** a ratio of *weighted, reconstructed* responses (effectively e/π after an energy-dependent EM weight). It is not the intrinsic e/h of either section.

#### Leakage and MC comparison

No corrections were applied for transverse or longitudinal leakage. Qualitatively the result is close to MC, but the MC model left out some structural elements between the EM and HCal sections and the limited size of the prototype. Optimal weighting and e/h still have to be settled with an MC of the exact test-beam geometry.

#### Electron response

The FCS electron response is shown in Fig. 9. Because the MPPC light collection is non-uniform, the EM response depends on impact position. For these preliminary results the EM energy was corrected for impact position, and the impact area was limited to a **circle of 1.4 cm diameter** at the centre of the EM tower.

![Fig. 9](assets/tsai2015-fcs-prototype/fig9.png)

**Fig. 9.** FCS EM prototype response to electrons. Left: EM energy for **4 GeV** electrons, with the impact point restricted by the scintillator hodoscope to **5 mm × 5 mm**. Centre and right: EM energy vs impact position in local X and local Y.

*Figure description (from the image):* Three ROOT panels. Left: title "ECal Electron Sum", y "#Events" 0 to ≈65, x "Energy (ADC Ch)" 0–1400. Single peak at ≈630 (≈520–750) with a Gaussian fit, plus a few counts scattered over 0–500. Stat box "ECalSumElectron": Entries 2956, Mean 609.8, RMS 126.2, χ²/ndf 309.9 / 258, Constant 50.87 ± 1.29, Mean 631.6 ± 0.8, Sigma 40.75 ± 0.66. Centre: "LocX_Sum_Profile" with no axis titles, x −15 to 15, y 420–590. The stat box is in small print at the limit of resolution: Entries 215839, Mean −0.6942, Mean y 532.5, RMS 7.361, RMS y 93.16, χ²/ndf 2114 / 63, p0 565.5 ± 0.3, p1 −0.000119 ± 0.000060, p2 0.00116 ± 0.00001. The points rise from ≈495 at x ≈ −12 to ≈570 at x ≈ −2, fall to ≈500 at x ≈ +12, then rise again at the edges (≈520–540 at |x| ≈ 14–15). A solid parabola-like fit over −10 to +10 peaks at ≈565 and ends at ≈500. One isolated point sits at x ≈ 0, y ≈ 430. Right: "LocY_Sum_Profile", x −15 to 15, y 460–585. Stat box: Entries 215919, Mean −0.7492, Mean y 532.1, RMS 6.71, RMS y 92.4, χ²/ndf 2321 / 63, p0 572.6 ± 0.2, p1 −0.0006125 ± 0.0000578, p2 0.001704 ± 0.000010. This profile is narrower and deeper: ≈575 at x ≈ 0 and ≈470–475 at |x| ≈ 12, rising again at the edges. The fit over −10 to +10 falls from ≈572 to ≈475–480, and one isolated point sits at x ≈ 0, y ≈ 470.

**[note]** The Fig. 9 fit values agree with the note's "Values read from Fig. 9". The fit curves end at x = ±10 at ≈500 (X) and ≈475 (Y). That matches p0(1 − p2·x²): 565.5 × 0.884 = 500 and 572.6 × 0.830 = 475, which supports the note's inferred fit form. The 4 GeV energy and the 5 mm × 5 mm hodoscope cut are not printed on the figure; they come from the caption.

The local impact coordinates were found from calorimeter information alone, using **logarithmic weighting with cut-off parameter 3.8**. The X and Y response shapes differ because the EM prototype was tilted by **4° about the Y axis**.

**[note] Values read from Fig. 9**

- **Left panel ("ECalSumElectron"):** Entries 2956; Mean 609.8; RMS 126.2; χ²/ndf 309.9/258. Gaussian fit: Constant 50.87 ± 1.29, Mean 631.6 ± 0.8, Sigma 40.75 ± 0.66 (ADC channels). This gives σ/E = **6.45% at 4 GeV** ✓, consistent with the Fig. 10 electron fits (6.2% and 6.9% at 4 GeV).
- **Centre panel (LocX profile, x axis −15 to 15, presumably mm):** p0 = 565.5 ± 0.3, p1 = −0.000119 ± 0.000060, p2 = 0.00116 ± 0.00001, χ²/ndf = 2114/63.
- **Right panel (LocY profile):** p0 = 572.6 ± 0.2, p1 = −0.0006125 ± 0.0000578, p2 = 0.001704 ± 0.000010, χ²/ndf = 2321/63.
- **Size of the non-uniformity:** the curves match p0(1 − p2·x²) at x = ±10. That gives a response drop of about **12% (X) and 17% (Y) at 10 mm** from the tower centre, and about 6% / 8% at the 7 mm radius of the analysis cut. This is my inference; the fit function is not given.

#### Linearity and resolution

Summary plots are in Fig. 10.

- **Linearity:** the electron response is almost linear. The hadron response clearly departs from linearity **above 15 GeV**. The most likely causes are the weighting of the EM fraction and leakage from the FCS. The HCal alone (EM section removed) showed no such deviation in this energy range.
- **Hadron resolution:** about **15% worse than MC at 10 GeV**. One reason is transverse leakage from the prototype, which was not corrected. The MC resolution also depends on the GEANT4 physics list. They used **LHEP**, which they consider the most accurate for the FCS.
- **Electron resolution:** close to MC. Two fits are shown:
  - assuming zero beam momentum spread, the stochastic term is close to **10%** and the constant term **1.7%**;
  - using the 2012 estimates of beam momentum spread (**2.7% below 4 GeV, 2.3% above**), the stochastic term is **11%** and the constant term close to zero.

![Fig. 10](assets/tsai2015-fcs-prototype/fig10.png)

**Fig. 10.** Left: FCS prototype response to electrons and hadrons vs energy. Right: FCS energy resolution for hadrons and electrons vs energy.

*Figure description (from the image):* Two panels. Left: legend title "Linearity of ECAL + HCAL", y "Detector Response" ≈100–5200 (no units), x "Beam Energy (GeV)" 0 to ≈35. Filled diamonds (hadron) and filled stars (electron) at 3, 4, 6, 8, 10, 12, 16, 20, 25 and 32 GeV, each with a dotted straight-line fit. Legend: "hadron, (157.1 ± 2.4)·E + 54.3 ± 22.4"; "electron, (144.5 ± 1.2)·E + 40.9 ± 10.9". The hadron points lie on their line up to 16 GeV and below it at 20, 25 and 32 GeV (my readings ≈3100, ≈3770 and ≈4800, against line values ≈3200, ≈3980 and ≈5080). Right: legend title "Resolution of ECAL + HCAL", y "Resolution ΔE/E" 0–0.5, x "Beam Energy (GeV)" 0 to ≈35. Filled diamonds (hadron), filled stars (electron) and open stars (elec. no beam spread) at the same energies, with dotted fit curves. Legend: "hadron, ΔE/E = (0.58 ± 0.04)/√E + 0.015 ± 0.015"; "electron, ΔE/E = (0.11 ± 0.007)/√E + 0.007 ± 0.002"; "elec. no beam spread, ΔE/E = (0.103 ± 0.005)/√E + 0.017 ± 0.002". The hadron points fall from ≈0.34 at 3–4 GeV to ≈0.13 at 32 GeV; the 4 GeV point is above the curve and the 8 GeV point (≈0.20) below it. The electron points fall from ≈0.075–0.08 at 3 GeV to ≈0.02–0.035 at 32 GeV, with the open stars slightly above the filled ones.

**[note]** The Fig. 10 legend values agree exactly with the note's transcription. In the linearity panel the 32 GeV electron point (≈4540) also sits below its line (≈4665), about 3% low by my reading. Hadrons are therefore not the only species that falls below its line at the top energy, though the text only calls the electron response "almost linear".

**Fit results printed in Fig. 10 (read from figure; not in the text layer)**

Linearity of ECAL + HCAL, detector response vs beam energy $E$ (GeV):

$$ \text{hadron:}\quad R = (157.1\pm2.4)\,E + 54.3\pm22.4 $$

$$ \text{electron:}\quad R = (144.5\pm1.2)\,E + 40.9\pm10.9 $$

Resolution of ECAL + HCAL. Note that the fit is a **linear** sum of stochastic and constant terms, not a quadrature sum:

$$ \text{hadron:}\quad \frac{\Delta E}{E} = \frac{0.58\pm0.04}{\sqrt{E}} + 0.015\pm0.015 $$

$$ \text{electron:}\quad \frac{\Delta E}{E} = \frac{0.11\pm0.007}{\sqrt{E}} + 0.007\pm0.002 $$

$$ \text{electron, no beam spread:}\quad \frac{\Delta E}{E} = \frac{0.103\pm0.005}{\sqrt{E}} + 0.017\pm0.002 $$

**[note] Checks on the Fig. 10 fits**

- The text's "close to 10% / 1.7%" matches 0.103/0.017 ✓. "11% / close to zero" corresponds to 0.11/0.007 ✓; "close to zero" means 0.7 ± 0.2%.
- **e/π from the slopes:** 144.5/157.1 = 0.92, and 0.915 at 12 GeV including offsets. This is consistent with the Fig. 8 right panel ✓.
- **Linearity fit and hadron data:** the hadron points at 25 and 32 GeV fall below the line (e.g. ≈4800 vs 5081 from the fit at 32 GeV), as the text says.
- **Equivalent quadrature form:** a linear-sum fit is not directly comparable with the usual quadrature form $a/\sqrt{E}\oplus b$. For hadrons, 58%/√E (+1.5%) linear corresponds roughly to 60%/√E ⊕ a few % in quadrature over 3–32 GeV. This is my estimate.

#### Light yield

- **EM section:** about **400 pixels/GeV**, with the EM front face painted with white diffuse paint BC-620.
- **HCal section:** about **130 pixels/GeV**.
- **Linearity:** with these yields the MPPCs of both sections should be almost linear over the test-run energies.
- **Masks:** the EM yield is high enough to add a mask between fibres and light guide to make the light collection more uniform.
- **Fibre-end reflector:** newer MPPCs already have much better PDE than those used here, and SiPMs are expected to improve further. The authors therefore see no need for any reflector at the fibre ends, which simplifies EM construction considerably. The 2012 measurements with EM prototypes carrying either a good mirror or black tape at the fibre ends showed that the whole difference in resolution is explained by photostatistics. Degradation of fibre attenuation length is therefore not critical in this case.

![Fig. 11](assets/tsai2015-fcs-prototype/fig11.png)

**Fig. 11.** The eighteen-channel EIC EM prototype on the beam line at FNAL. The in-figure label reads "Sintillator Hodoscope" (sic).

*Figure description (from the image):* Black-and-white photograph at the beam line. Right: a rectangular aluminium box labelled "EIC EM prototype", with a bundle of cables leaving its top, mounted on a cylindrical rotation stage. The stage's dark collar carries tick marks with hand-written degree values whose digits are unreadable. Left: a black box with a "FRAGILE" sticker and cables, labelled "Sintillator Hodoscope" (the in-figure spelling, confirming the caption's sic). No scale.

**[note] Photostatistics and saturation estimates (mine, not in the paper)**

- **EM photostatistics:** 400 pixels/GeV implies a Poisson term of $1/\sqrt{400\,E} = 5\%/\sqrt{E}$, before the excess-noise factor. In quadrature with ~10%/√E this is not negligible: it is about a quarter of the variance. This is consistent with the authors wanting better PDE rather than less light.
- **HCal photostatistics:** 130 pixels/GeV gives 8.8%/√E, negligible against 58%/√E.
- **EM saturation:** one EM tower has 4 × 14 400 = 57 600 pixels. At 32 GeV and 400 pixels/GeV, a fully contained shower would fire about 12 800 pixels (22% occupancy). The simple saturation formula $N_{fired}=N_{pix}(1-e^{-N_{pe}/N_{pix}})$ then implies an ≈10% deficit. "Almost linear" may therefore be optimistic at the top of the range, particularly with hot spots under the MPPCs.
- **HCal saturation:** 8 × 14 400 pixels at 130 pixels/GeV is far from saturation.

#### EIC central-barrel EM prototype

Alongside the FCS, a prototype of the central-barrel EM calorimeter for the EIC was tested (Fig. 11). The goal was its response at different impact angles.

- **Design:** same technology as the FCS EM prototype except for the tower geometry. Wedge geometries have always been hard for ScFi calorimeters. Here the wedge is made by **progressively inclining the meshes** that form the fibre matrix along the tower depth, which is as simple as building straight FCS towers.
- **Sampling:** the sampling fraction and frequency rise slightly towards the tower front face. MC shows this has only a minor effect on resolution.
- **Programme:** response, energy resolution and absolute light yield were measured vs impact angle. Energy scans were done at **three angles**, and **three light collection schemes** were tested.
- **Uniformity:** the light collection is similar to the FCS EM detector and showed similar uniformity problems. At shallow impact angles (detector rotated about the vertical Y axis), the response non-uniformity along X almost disappears.
- **Analysis cut:** for the preliminary results the impact area in Y was limited to **5 mm**, to reduce non-uniformity and leakage from the small prototype.

![Fig. 12](assets/tsai2015-fcs-prototype/fig12.png)

**Fig. 12.** EIC EM prototype. Left: response to electrons vs energy for different impact angles. Right: energy resolution $(p0/\sqrt{E} + p1)$ for electrons vs energy for different impact angles.

*Figure description (from the image):* Two ROOT panels. Left: title "EIC BEMC Linearity. 0 < eta < 0.9", y untitled 0–2200, x "Beam Energy (GeV)" 0 to ≈13. Markers: cross (eta = 0.9), small diamond (eta = 0.3) and grey circle (eta = 0), at ≈1, 2, 3.1, 4.1, 6, 8, 10 and 11.8 GeV, with dashed straight-line fits. The markers overlap below 8 GeV; at 11.8 GeV they separate to ≈2020 (0.9), ≈1940 (0.3) and ≈1880 (0). Stat boxes: eta = 0.9: χ²/ndf 2.93 / 6, p0 −1.177 ± 5.653, p1 169.2 ± 2.202. eta = 0.3: χ²/ndf 4.175 / 6, p0 0.4278 ± 5.581, p1 166.9 ± 2.174. eta = 0: χ²/ndf 4.284 / 6, p0 23.83 ± 5.452, p1 160.8 ± 2.101. Right: title "EIC BEMC at eta=0.9, 0.3, 0, Energy Resolution", y "Resolution ΔE/E" ≈0.03–0.155, x "Beam Energy (GeV)" 0 to ≈13. Same markers and energies, with three fit curves drawn solid from ≈2 GeV and dashed below. Stat boxes: eta = 0.9: χ²/ndf 11.53 / 5, p0 0.01315 ± 0.002239, p1 0.09586 ± 0.005512. eta = 0.3: χ²/ndf 10.46 / 5, p0 0.003409 ± 0.002268, p1 0.1213 ± 0.005746. eta = 0: χ²/ndf 12.78 / 5, p0 0.01133 ± 0.002383, p1 0.1083 ± 0.005906. The points fall from ≈0.143–0.150 at 1 GeV (well above the curves, which reach ≈0.105–0.122 there) and ≈0.085–0.090 at 2 GeV to ≈0.036–0.046 at 11.8 GeV.

**[source issue]** Confirmed from the image: the Fig. 12 resolution parameters are swapped relative to the caption's p0/√E + p1. At η = 0 the plotted curve and point are at ≈0.088 at 2 GeV and ≈0.042 at 11.8 GeV. The form p1/√E + p0 reproduces both (0.1083/1.414 + 0.0113 = 0.088; 0.1083/3.435 + 0.0113 = 0.043), whereas the caption form gives 0.116 and 0.112. p1 is therefore the stochastic term and p0 the constant term. All six stat-box rows in the note's table agree with the image.

**[note]** The resolution fits have ndf = 5 with eight energies plotted, so seven points were fitted. The 1 GeV points lie far above the curves, which are dashed there, so they appear to be excluded from the fit (my inference). The linearity fits (ndf = 6) use all eight points.

Fit form as stated in the Fig. 12 caption:

$$ \frac{\Delta E}{E} = \frac{p0}{\sqrt{E}} + p1 $$

**Fit results printed in Fig. 12 (read from figure)**

| Panel | η | χ²/ndf | p0 | p1 |
|---|---|---|---|---|
| Linearity (0 < η < 0.9) | 0.9 | 2.93/6 | −1.177 ± 5.653 | 169.2 ± 2.202 |
| Linearity | 0.3 | 4.175/6 | 0.4278 ± 5.581 | 166.9 ± 2.174 |
| Linearity | 0 | 4.284/6 | 23.83 ± 5.452 | 160.8 ± 2.101 |
| Resolution | 0.9 | 11.53/5 | 0.01315 ± 0.002239 | 0.09586 ± 0.005512 |
| Resolution | 0.3 | 10.46/5 | 0.003409 ± 0.002268 | 0.1213 ± 0.005746 |
| Resolution | 0 | 12.78/5 | 0.01133 ± 0.002383 | 0.1083 ± 0.005906 |

(This table is my transcription of the in-figure statistics boxes; the paper itself has no tables.)

**[source issue] Fig. 12 fit parameters are swapped relative to the caption.** The caption gives the fit as $p0/\sqrt{E}+p1$, but the printed values only describe the data if p1 is the stochastic term and p0 the constant term.

- At η = 0, E = 2 GeV, the data are ≈0.09. With p1/√E + p0: 0.1083/1.414 + 0.0113 = 0.088 ✓. With the caption form p0/√E + p1: 0.116 ✗.
- So the EIC barrel prototype has a stochastic term of **≈9.6–12.1%/√E** and a constant term of **≈0.3–1.3%**, read with that swap.
- The linearity panel has the usual p0 = offset, p1 = slope.

#### Interpretation of Fig. 12

As MC predicted, the response depends only slightly on impact angle. The change of slope in the left panel is explained by the slightly higher sampling fraction at shallower impact angles; the slope rises from 160.8 at η = 0 to 169.2 at η = 0.9. The resolution will be practically the same over the whole pseudorapidity range of an EIC central barrel (right panel), again in reasonable agreement with MC.

- **Light yield:** **430, 530 and 600 pixels/GeV**, depending on the front-face reflector and the materials around the light guides. The highest yield came from white diffuse paint (BC-620) on the front face plus diffuse reflectors around the light guides.
- **Fibres:** multi-clad fibres (**Kuraray SCSF 78M**, used in the EIC prototype) give only slightly more light than single-clad fibres (**Kuraray SCSF 78**, used in the FCS EM prototype).
- **Readout side:** EM prototype performance did not differ between upstream readout (FCS) and downstream readout (EIC).

### 4. Summary

- **2012:** a proof of principle of a new, simple and cost-effective way to build compact tungsten-powder scintillating-fibre calorimeters.
- **2014 EM prototypes:** two new EM prototypes, one for the STAR forward upgrade and one for a future EIC central-barrel EM calorimeter, were tested successfully at FNAL in March 2014.
- **HCal technique:** a new construction technique was developed for a high-resolution lead/scintillating-tile hadronic calorimeter.
- **EIC use:** the FCS, designed for the STAR forward upgrade, is called an ideal candidate for the forward (outgoing-hadron) calorimeter of a dedicated EIC detector.
- **Performance:** met expectations. The compact SiPM readout works well for the HCal prototype.
- **EM uniformity:** must be improved soon. With the measured light yield, properly designed masks between fibres and light guides should cure the non-uniformity.
- **Ongoing work:** bench tests with the existing prototypes, final data analysis and an MC of the exact test-beam configuration were in progress.

### Acknowledgments (paraphrase)

The authors thank the STAR technical support group at BNL for help preparing the front-end electronics, and FNAL and the FTBF group for beam time and help with setup and running. The work was supported by the US Department of Energy.

---

## Derived quantities and recomputations

PDG constants used: Pb X0 = 0.56 cm and λ_I = 17.6 cm; W X0 = 0.35 cm and λ_I = 9.9 cm; Fe X0 = 1.76 cm and λ_I = 16.8 cm. For the polystyrene/PVT scintillator I used X0 ≈ 41–42 cm and λ_I ≈ 77 cm. The effect of the 4% Sb in the absorber was ignored except where stated.

**HCal tower (63 × 10 mm Pb(Sb) + 64 × 2.5 mm EJ-212 in 3.1 mm gaps)**

- **Length:** 63 × 10 + 64 × 3.1 = **828.4 mm**, or 63 × 13.1 = 825.3 mm. The paper quotes **81 cm**. **[source issue]** (minor) The stack described is ≈82.5–82.8 cm, about 2% longer than quoted. The quoted figure may exclude an end gap, or be rounded.
- **λ_I:** 63.0 cm Pb / 17.6 = 3.58 λ_I, plus 16.0 cm scintillator / 77 ≈ 0.21 λ_I, giving **≈3.8 λ_I**. The paper says **4 λ_I**, approximately ✓. With the lower density of a 4% Sb alloy (≈10.9 vs 11.35 g/cm³, my estimate) it is ≈3.7 λ_I.
- **X0:** 63.0 / 0.56 = 112.5 X0, plus 16.0 / 41.3 ≈ 0.4 X0, giving **≈113 X0**.
- **Effective lengths:** λ_I,eff ≈ 82.8 / 3.8 ≈ 22 cm; X0,eff ≈ 0.73 cm.
- **Sampling:** the Pb:scintillator thickness ratio is 10:2.5 = **4:1**, the classic compensating ratio for Pb/plastic, as in the ZEUS Pb/Sc prototype [3]. The paper says it copied ZEUS but does not give e/h for the HCal alone. The MIP sampling fraction I estimate is 0.25 × 2.0 MeV/cm ÷ (0.25 × 2.0 + 1.0 × 12.7 MeV/cm) ≈ **3.8%**; the paper does not give it.

**SPACal / EM tower (W powder + epoxy + ScFi)**

- **Effective X0:** 17 cm / 23 X0 = **0.74 cm**.
- **λ_I:** not given. Pure W has λ_I/X0 = 28.4, and adding low-Z material lowers this ratio. For a plausible mix (≈50% W, 35% epoxy, 15% fibre by volume; ρ ≈ 10.2 g/cm³) I get λ_I/X0 ≈ 25. That puts the 17 cm section at **≈0.9 λ_I**, with the composition assumed. A 0.9 λ_I EM section is consistent with the large EM weight needed for hadrons (Fig. 8 / Sec. 3).
- **Total:** EM + HCal ≈ 0.9 + 3.8 ≈ **4.7 λ_I**.

**Prototype sizes**

- **HCal:** 16 channels = 4 × 4 towers of 10 cm = **40 cm × 40 cm** transverse. This is small for hadron-shower containment, consistent with the transverse leakage the authors invoke.
- **EM:** 16 channels = 4 × 4 towers of 2.5 cm = **10 cm × 10 cm**. In Fig. 6 the FCS EM prototype shows 4 × 4 light guides.

---

## Checks

### (a) HCal design (2014 prototype)

- **Absorber:** lead–antimony alloy (**4% Sb**), plates **10 mm** thick, painted with white diffuse reflective paint (Sherwin Williams F63WC134). Positioned by 5 mm steel dowel pins and steel master plates; built "LEGO-style" in situ.
- **Scintillator:** **EJ-212**, **2.5 mm** thick, floating in **3.1 mm** gaps. Unwrapped tiles were as good as Tyvek-wrapped ones.
- **Layers:** **63 absorber + 64 scintillator** plates per tower.
- **Tower size:** **10 cm × 10 cm × 81 cm** (the stack arithmetic gives ≈82.8 cm). The proposed full detector has **30 × 20 towers**; the prototype has 16 towers.
- **Depth:** quoted as **4 λ_I**. I recompute ≈3.8 λ_I and ≈113 X0, ✓ within rounding.
- **Sampling fraction:** not quoted. It is the **ZEUS Pb/Sc 10 mm / 2.5 mm (4:1)** structure [3]; I estimate the MIP sampling fraction at ≈3.8%.
- **Compensation:** the HCal and the whole FCS are called "compensated". The only measurement given is the combined FCS e/h ("e/h" of the weighted sum) **≈0.95, constant above 10 GeV**. This needed an energy-dependent EM weight of **2 → 1.2** from **3 → 20 GeV**. No HCal-alone e/h is quoted.
- **Light collection:** one **3 mm EJ-280 WLS plate** per tower, in the gap between adjacent towers, read out at the end. The WLS plate has a BC-620 reflector at the far end and aluminised mylar on the back, which also isolates towers optically. A **printed variable-density mylar filter** between tiles and WLS plate makes the light collection uniform within 10% along the depth; without it the resolution above 20 GeV is ~2× worse (MC). All optical joints are air gaps except SiPM–WLS, which is RTV (Dow Corning 3145).
- **Photosensor:** **8 × Hamamatsu MPPC S10931-025P per tower** (3 × 3 mm², 25 µm pixels), geometric efficiency quoted as 8.2% (not reproducible from the given dimensions; see the note in Sec. 2).
- **Readout:** FEE with bias regulated from 90 VDC by two DACs (one with a thermistor), giving programmable voltage and temperature-compensation slope. Four SiPMs are summed into one BFR92A common-base preamp of a few Ω input impedance (1.3 nF of SiPM capacitance), followed by a differential **4 Vpp** driver over twisted pair to an external ADC.
- **Light yield:** **≈130 pixels/GeV**.

### (b) EMCal design (2014 prototype)

- **Absorber:** **tungsten powder**, poured into a fibre matrix and then epoxy-impregnated ("spaghetti" SPACal). Built as 4-tower superblocks; the composite has steel-like mechanical strength. The powder/epoxy density and fibre pitch and diameter are not given here; see [2].
- **Active medium:** scintillating fibres, **Kuraray SCSF 78 (single-clad)** for the FCS prototype. The EIC prototype used SCSF 78M (multi-clad), which gave only a slightly higher light yield.
- **Tower size:** **≈2.5 × 2.5 × 17 cm³** active. The proposed full detector has **120 × 80 towers**; the prototype has 16 channels (4 × 4).
- **Depth:** **23 X0** (X0,eff = 0.74 cm ✓). λ_I is not given; I estimate ≈0.9 λ_I.
- **Sampling fraction:** not given; the sampling frequency is described only as "high".
- **Compensation:** claimed for the EM section too, but no number is given. The energy-dependent weight of 2 → 1.2 for hadronic energy deposited in the EM section shows that this section is far from e/h = 1 for low-energy hadrons.
- **Light collection:** fibres → **25 mm acrylic truncated-pyramid light guide** (25 × 25 mm² base → 13 × 13 mm² top) → MPPCs, with a ~2 mm Sylgard 184 cookie. Non-uniformity is up to **20%** (hottest spots under the MPPCs vs the tower corners). The front face is painted BC-620, and no reflector is planned at the fibre ends.
- **Photosensor:** **4 × MPPC S10931-025P per tower** at 7 mm centre spacing; geometric efficiency **≈21%** ✓.
- **Readout:** summed with an OPA691. One common bias for all 16 channels, with a resistive divider per tower, and **no temperature compensation**.
- **Light yield:** **≈400 pixels/GeV**, compared with **2000 p.e./GeV** in 2012 with PMTs. The EIC prototype gave 430/530/600 pixels/GeV.

### (c) Test-beam setup and results

**Setup**

- **Where and when:** FNAL MTest / FTBF, line **MT6**, experiment **T1018**, March 2014.
- **Particles:** hadrons, electrons and muons at **3–32 GeV**.
- **Beam instrumentation:** differential Cherenkov for electron ID; XY hodoscope of 4.9 mm scintillator rods with SensL SiPMs; two MWPCs; He-filled beam pipes. Upstream material ≈4 cm of scintillator.
- **Angles:** HCal tilted **2.5°** to the beam, EM tilted **4°**. The EM prototype was mounted on the HCal front plate.
- **Calibration:** LED and pedestal monitoring at ~1 Hz showed gain stability **< 1%** per 12 h shift. Laser gain-matching was within 1%. The HCal needed a further ~**20%** tower-by-tower MIP correction, using 8 GeV muons with the EM section removed. The EM section needed no beam calibration.

**Results**

| Quantity | Electrons (EM+HCal) | Hadrons (EM+HCal, weighted) |
|---|---|---|
| Resolution fit (linear sum, read from Fig. 10) | $(11\pm0.7)\%/\sqrt{E} + (0.7\pm0.2)\%$ with beam spread unfolded; $(10.3\pm0.5)\%/\sqrt{E} + (1.7\pm0.2)\%$ with no beam-spread correction | $(58\pm4)\%/\sqrt{E} + (1.5\pm1.5)\%$ |
| Point checks | 6.45% at 4 GeV (Fig. 9, EM only, 1.4 cm central circle, position-corrected) | 19.2% at 12 GeV (Fig. 8) |
| vs MC | close to MC | ≈15% worse than MC at 10 GeV (transverse leakage not corrected; LHEP physics list) |
| Linearity fit (ADC vs GeV) | $(144.5\pm1.2)E + 40.9\pm10.9$, almost linear | $(157.1\pm2.4)E + 54.3\pm22.4$, deviates above 15 GeV (EM weighting and leakage); HCal alone stays linear |
| e/π (called e/h) | — | ≈0.95, flat above 10 GeV (points 0.87–0.98); slopes give 0.92 |

- **HCal-alone resolution:** **not reported** in this paper. Only the "HCal alone shows no non-linearity" statement is given.
- **EM-alone resolution:** effectively the electron curve, since the HCal sees little of an electron shower, but it is not given separately.
- **EM uniformity:** the position dependence of the EM response is large. The fitted profiles fall by ≈12% (X) and 17% (Y) at 10 mm from the tower centre (my inference from the fit parameters). A 1.4 cm central circle was therefore used.
- **EIC barrel prototype (Fig. 12):** stochastic term ≈9.6–12.1%/√E and constant term ≈0.3–1.3% at η = 0–0.9, reading the fit parameters with the swap noted above.

### (d) 2014 prototype vs as-built FCS (from [ruan2026-fcs-specs-email-note](ruan2026-fcs-specs-email-note.md))

| Item | 2014 prototype / proposal (this paper) | As-built STAR FCS (ruan2026-fcs-specs-email) |
|---|---|---|
| η coverage | 2.5–4.5 | ≈2.2–4.3 |
| EMCal technology | W powder + epoxy + ScFi spaghetti (SPACal), new construction | Pb/scintillator shashlik with WLS fibres, **re-used PHENIX PbSc** modules |
| EMCal tower | 2.5 × 2.5 cm², 17 cm, **23 X0** (X0,eff 0.74 cm), ≈0.9 λ_I (my estimate) | 5.542 × 5.542 cm², 37.73 cm, **18.1 X0** (X0,eff 2.06 cm), 0.93 λ_I, Molière radius 5.6 cm |
| EMCal sampling | W powder / fibres (fraction not given) | 65 × 1.5 mm Pb + 66 × 4.0 mm scint; sampling fraction 0.20 |
| EMCal towers | 120 × 80 = 9600 proposed | 1496 (2 × 748) |
| EMCal light path | acrylic pyramid light guide → 4 MPPCs per tower | WLS fibres → SiPM |
| HCal absorber | **Pb (4% Sb), 10 mm**, 63 plates | **Fe (steel), 20 mm**, 36 plates (+10 mm back plate) |
| HCal scintillator | 2.5 mm EJ-212, 64 tiles, 3.1 mm gap | 3.0 mm, 36 tiles, 23.4 mm pitch |
| HCal tower | 10 × 10 cm², 81 cm, 4 λ_I quoted (≈3.8 recomputed), ≈113 X0 | 9.99 × 9.99 cm², 84.24 cm, 4.45 λ_I, 41 X0 |
| HCal sampling | ZEUS-like 4:1 Pb:scint, intended to be compensating (e/π ≈0.95 after EM weighting) | Fe/scint, sampling fraction 0.0145; not a compensating ratio for iron |
| HCal towers | 30 × 20 = 600 proposed | 520 (2 × 260) |
| HCal light collection | 3 mm EJ-280 WLS plate between towers, printed uniformity filter | 3 mm WLS plate down one side of each tower — **same concept** |
| Photosensors | Hamamatsu MPPC S10931-025P: 8 per HCal tower, 4 per EM tower | SiPM (type and count not given in the email) |
| Total depth | ≈0.9 + 3.8 ≈ 4.7 λ_I | 0.93 + 4.45 ≈ 5.4 λ_I |

**[note] What changed and what survived**

- The 2014 FCS concept was a dense, fine-grained, compensating system: a W/ScFi SPACal plus a Pb/scintillator ZEUS-type HCal. The as-built FCS dropped the W/ScFi SPACal in favour of re-used PHENIX Pb/Sc shashlik modules. These are coarser (5.5 cm vs 2.5 cm), longer (37.7 cm vs 17 cm) and shallower in X0 (18 vs 23).
- The HCal absorber changed from Pb(Sb) to steel, with thicker plates (20 vs 10 mm) and fewer layers (36 vs 63). This gives up the compensating Pb:scint ratio, though the as-built HCal is deeper in λ_I (4.45 vs ≈3.8–4).
- Three elements survive: the **WLS-plate side readout of the HCal tower**, **SiPM readout throughout**, and ~10 cm HCal towers.
- The W/ScFi technology itself went on to EIC R&D (see the EIC barrel prototype in this paper).
- The email does not give e/h or resolution for the as-built system, so performance cannot be compared from these two sources.

### (e) Rates, radiation, SiPM gain/temperature

- **Radiation:** the only statement is that the MPPCs are "sufficiently radiation hard for FCS readout in STAR", citing [4] (Fisyak et al. 2014, NIM A 756, 68). No fluence or dose numbers are given.
- **Rates:** nothing on rates, occupancy or pile-up.
- **SiPM gain and temperature:**
  - HCal FEE: programmable bias voltage and **programmable temperature-compensation slope** via a DAC channel with a thermistor, to hold the SiPM gain constant.
  - EM FEE: **no temperature compensation**, and one bias for all 16 channels with resistive dividers, since the MPPCs were pre-sorted into equal-gain groups of four.
  - Laser test before the run: assembly gains matched within **1%**. LED monitoring at ~1 Hz showed gain stability **better than 1% over 12 h** for both FEEs.
  - HCal MIP recalibration needed ≈20% corrections, ≈10% of which came from WLS–MPPC misalignment (~250 µm on 3 mm).
- **Dynamic range and linearity:** 400 pixels/GeV (EM) and 130 pixels/GeV (HCal), which the authors say keeps the MPPCs "almost linear" up to 32 GeV. My estimate gives ≈10% pixel-saturation effects at 32 GeV in one EM tower (57 600 pixels; see the note in Sec. 3). The HCal FEE output is 4 Vpp differential, designed for high dynamic range.

---

## References (hardware-relevant)

- [1] D. Boer et al., "Gluons and the quark sea at high energies: distributions, polarization, tomography", arXiv:1108.1713v2 (2011). This is the EIC physics case; it is not a hardware reference.
- [2] O. Tsai et al., J. Phys.: Conf. Ser. **404** (2012) 012023. The W-powder/ScFi construction technique and the 2012 FNAL test. **Key source** for the W/ScFi composition, sampling fraction and 2012 resolution/light-yield results that this paper does not repeat.
- [3] E. Bernardi et al., Nucl. Instr. Meth. **A262** (1987) 229. The ZEUS Pb/scintillator compensating prototype whose sampling fraction and frequency the FCS HCal copied.
- [4] Y. Fisyak et al., Nucl. Instr. Meth. **A756** (2014) 68. Cited for MPPC radiation hardness in STAR.
