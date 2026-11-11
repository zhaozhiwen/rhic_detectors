---
title: "Allgower 2003 — The STAR endcap electromagnetic calorimeter (full-content paraphrase)"
type: raw-source
source_type: paper
authors: "STAR EEMC group: C.E. Allgower et al., 46 authors (alphabetical)"
journal: "Nucl. Instrum. Meth. A 499 (2003) 740–750"
doi: 10.1016/S0168-9002(02)01971-X
arxiv: none
captured_via: "Route 1 — publisher HTML (ScienceDirect full text in the user's Chrome); Table 1 rebuilt from the publisher PDF"
captured_date: 2026-11-09
captured_as: full-content paraphrase
figures: "5 (vision descriptions added 2026-11-09)"
vision_model: "general-purpose subagent (session model, not recorded), 2026-11-09"
---

# The STAR endcap electromagnetic calorimeter (Allgower et al., NIM A 499 (2003) 740) — reading note

- **Citation:** C.E. Allgower, B.D. Anderson, A.R. Baldwin, J. Balewski, M. Belt-Tonjes, L.C. Bland, R.L. Brown, R.V. Cadman, W. Christie, I. Cyliax, V. Dunin, L. Efimov, G. Eppley, C.A. Gagliardi, N. Gagunashvili, T. Hallman, W. Hunt, W.W. Jacobs, A. Klyachko, K. Krueger, A. Kulikov, A. Ogawa, Y. Panebratsev, M. Planinic, J. Puskar-Pasewicz, G. Rakness, S. Razin, O. Rogachevski, S. Shimansky, K.A. Solberg, J. Sowinski, H. Spinka, E.J. Stephenson, V. Tikhomirov, M. Tokarev, R.E. Tribble, D. Underwood, A.M. Vander Molen, S.E. Vigdor (corresponding author), J.W. Watson, G. Westfall, S.W. Wissink, A. Yokosawa, V. Yurevich, W.-M. Zhang, A. Zubarev, "The STAR endcap electromagnetic calorimeter". **46 authors**, taken from page 1 of the PDF. The ScienceDirect HTML page shows only a truncated list ending "K. Krueger … A. Zubarev". The INSPIRE record (608097) also gives author_count = 46.
- **Affiliations:** (a) Indiana University Cyclotron Facility, Bloomington; (b) Kent State University; (c) Michigan State University; (d) BNL Physics Division; (e) Argonne HEP Division; (f) JINR Dubna, Laboratory of High Energy Physics; (g) Rice University; (h) Cyclotron Institute, Texas A&M; (i) Penn State. Corresponding author: S.E. Vigdor (IUCF).
- **Journal ref:** Nucl. Instrum. Meth. A **499** (2003) 740–750. This is the RHIC special issue "The Relativistic Heavy Ion Collider Project: RHIC and its Detectors", edited by M. Harrison, T. Ludlam and S. Ozaki, dated 1 March 2003 (© 2002 Elsevier). PII S016890020201971X. **DOI:** [10.1016/S0168-9002(02)01971-X](https://doi.org/10.1016/S0168-9002(02)01971-X). PACS 29.40.Vj; 29.40.Mc; 07.85.+n.
- **arXiv:** none. The INSPIRE record for this DOI has no arXiv e-print. A direct arXiv API query could not be made because the network refused it.
- **Route used:** Route 1, the ScienceDirect HTML full text read in the user's Chrome. The HTML body loaded with all 7 sections, Table 1, 5 figures and 11 references. **The article contains no equations**: the HTML has no MathML and the PDF has no numbered or display equations. The only formula is the resolution requirement inside Table 1, written out below.
  - The HTML version of Table 1 lost its cell structure. The table below was therefore rebuilt from `pdftotext -layout` of the PDF.
- **PDF backup:** `assets/star2003-eemc/source.pdf` (publisher PDF, 489 030 bytes, 11 pages = journal pages 740–750).
- **Figures:** `assets/star2003-eemc/fig1.png`, `fig3.png`, `fig4.png` and `fig5.png` are crops from 200-dpi `pdftoppm` renders of the PDF. These are vector drawings, and the crops have higher resolution than the small HTML GIFs (≈ 230–340 px wide). `fig2.jpg` is the embedded photograph extracted with `pdfimages` (567 × 458 px, larger than the 320 × 258 px HTML JPEG). Every crop was checked by eye.
- **Verification:** every number, unit, caption and table entry below was checked against `pdftotext -layout` of the PDF. Where the PDF text layer is ambiguous (its symbol font maps μ→m and ±→7), the rendered page was checked by eye. Results:
  - "300 μCi" is confirmed as μCi on the rendered page. pdftotext prints "300 mCi", which is a font-mapping artefact.
  - "50 mA" is confirmed as mA.
  - HTML and PDF otherwise agree. The HTML writes the η meson as "η0" where the PDF has "η⁰"/"η".
  - Derived numbers that I recomputed are marked ✓ (or ✗ / ≈) in **[note]**s.
- Figure descriptions were added by a separate figure pass that looked at the images.

---

## Abstract (paraphrase)

The STAR endcap EMC (EEMC) is to give full-azimuth coverage over **1.086 ≤ η ≤ 2.00** for high-$p_T$ photons, electrons and electromagnetically decaying mesons. It has three special detectors:

- a **scintillating-strip shower-maximum detector (SMD)** for π⁰/γ discrimination;
- **preshower** layers and
- a **postshower** layer, both to help separate electrons from charged hadrons.

Its triggering ability and coverage are essential to much of the spin programme with polarized p+p collisions.

Keywords: detectors; electromagnetic calorimeter; π⁰/γ discrimination; electron/hadron discrimination.

---

## Full content

### 1. Motivation and requirements

**Scope.** One EEMC was being built for installation in **2002–2003 on the west poletip** of STAR. It covers **1 < η ≤ 2** over the full azimuth and complements the barrel EMC (BEMC) described in the preceding article of the same issue. **[note]** That article is Beddo et al., NIM A 499 (2003) 725; this is from my own knowledge and is not cited by number in this paper.

**What the EEMC adds within its acceptance:**

- detection of photons and electromagnetically decaying mesons (π⁰, η);
- e± identification;
- triggering on high-energy particles of these kinds.

**Detector components:**

- The SMD is optimised to separate photons from π⁰/η over **10–40 GeV**.
- The preshower and postshower layers are for e/h discrimination.
- The EEMC also greatly improves STAR's jet acceptance and jet triggering.

**Physics drivers** (polarized p+p at RHIC [1–3]):

- **Gluon polarization ΔG(x_g).** The main goal is to measure ΔG(x_g) as a function of the gluon momentum fraction x_g, and to tightly constrain its integral, which is the gluon contribution to the proton spin. The probe is quark–gluon Compton scattering. One measures longitudinal double-spin asymmetries in **direct-photon production at $p_T \gtrsim 10$ GeV/c**, i.e. the difference over the sum of the cross sections for equal and opposite beam helicities.
- **Why the endcap matters for ΔG.** The endcap covers *asymmetric* partonic collisions, in which the photon and the away-side jet from the final-state quark are both boosted forward. A highly polarized quark at **x_q ≳ 0.2** in one proton then probes the gluon in the other proton at **x_g < 0.1**, where most gluons are [2,3]. In such events both the photon and many jet fragments typically land in the endcap.
- **W± production [3,4].** The EEMC raises STAR's sensitivity to the flavour dependence of sea-antiquark polarization through W± production. When the high-$p_T$ decay e± is detected in the EEMC, the production and decay kinematics give the cleanest extraction of both x values and of the separate quark and antiquark polarizations. The q and q̄ polarizations follow from the independent parity-violating sensitivities of the W± yield to a helicity flip of one beam or of the other.

**Requirements.** These physics goals set the requirements summarised in Table 1. The main ones are:

- a very wide dynamic range, nearly **1000:1 in energy**;
- strong π⁰/γ and hadron/electron suppression;
- an accurate absolute energy scale.

**Design trade-off.** Because the programme is p+p rather than A+A, tower segmentation can be somewhat coarser than in the BEMC. The design therefore uses fewer tower readout channels but spends more on a **scintillator SMD**. For the higher-energy showers typical of the relevant $p_T$ range at endcap η, a scintillator SMD is expected to do much better than the gaseous BEMC SMD, both in delineating the transverse shower profile and in energy-deposition resolution.

**Table 1.** Some requirements on EEMC coverage and performance (rebuilt from the PDF; wording kept close because these are specifications)

| Feature | Requirement | Driving physics goals |
|---|---|---|
| Geom. acceptance | 1 ≲ η ≤ 2; full φ | γ+jet sensitivity to 0.01 ≲ x_g ≲ 0.3 |
| E_min in one tower | ≈ 0.2 GeV | MIPs for calibration; γ's from asymmetric π⁰ decay; ≈2% shower leakage from p_T = 10 GeV/c γ's |
| E_max in one tower | 150 GeV | e± from W± decay at η = 2 |
| Linearity | < 10% integral non-linearity, ∼1–150 GeV | Correct to give W± daughter p_T to ±1 GeV/c from lower-E calibrations |
| Depth | ≥ 20 X₀, ≤ 1 hadron interaction length | < 10% shower leakage for 150 GeV e±; minimize hadron sensitivity to fit within existing space |
| Energy resolution | $(\sigma_E/E) \le (16\%/\sqrt{E}) + (2\%)$ | x_q̄ uncertainty ≲ ±0.01 for W± reconstruction at p_T,e ≤ 30 GeV/c |
| γ/π⁰ discrimination | π⁰/γ suppress factor > 3 for p_T ≈ 10–20 GeV/c ⇒ SMD | Keep background subtraction from enlarging ΔG(x) errors by more than a factor of 2 |
| e±/h± discrimination | Suppress h±/e± by > 10 for p_T ≳ 5 GeV/c ⇒ pre/post-shower | Reach > 3:1 W signal/hadronic bkgrd. ratio for p_T > 20 GeV/c; enhance Drell–Yan signal/bkgrd. |
| Jet reconstruction | σ ≈ 0.1 for η_jet, φ_jet | Reconstruct x_1,2 values for colliding partons in γ+jet coinc. to ≈ ±0.01 |
| Segmentation / rate capability | Tower occupancy < 10% @ L_pp = 2 × 10³² ; tower size ≳ 2 × shower diam. | Trigger on isolated γ or e± vs. jet; minimize tower hadron occupancy; obey WLS fiber min. bend radius |
| Tower calibration | Absolute E calibration to ±2% (±10% online) | Minimize: systematic errors in x_g, ∫ΔG(x)dx (p_T, hence x, threshold at acceptable trigger rates) |
| Coverage gaps | < 2% systematic shower E loss in cracks | Minimize systematic errors in extracted x_g, ∫ΔG(x)dx |
| SMD calibration | Relative gains of adjacent strips known to ≲ ±10% | Maintain sufficient γ vs. π⁰ shower shape discrimination |
| Timing response | < 1 RHIC beam period (110 ns) | Aid TPC pileup reject; no occupancy from neighboring beam crossings |

The energy-resolution requirement, written as a display formula (unnumbered in the paper; E in GeV):

$$\frac{\sigma_E}{E} \;\le\; \frac{16\%}{\sqrt{E}} + 2\%$$

**[note]** The terms are written as a linear sum ("+") in both the HTML and the PDF, not in quadrature.

**[note]** The table gives L_pp without units. The text of §5 uses ∼10³² cm⁻² s⁻¹, so the table value is presumably 2 × 10³² cm⁻² s⁻¹.

**[note]** "110 ns" is the RHIC bunch spacing as quoted. RHIC's nominal 120-bucket spacing is ≈ 107 ns, so the table value is rounded. This is from my own knowledge.

### 2. Tower structure and optical chain

**Choice of technology.** The EEMC is a conventional **Pb/plastic-scintillator sampling calorimeter**, chosen for cost and simplicity and because it shares technology with the BEMC.

**Coverage.** The actual coverage is **1.086 ≤ η ≤ 2.00**. The small gap between endcap and barrel is needed for services to leave the solenoid. **[note]** η = 1.086 corresponds to θ = 37.3° and η = 2.00 to θ = 15.4° ✓.

**Overall layout.**

- The full annulus is built as **two halves**; one half is shown in Fig. 1. The lower part of the figure shows the alternating Pb-radiator and scintillator layers.
- A high-resolution scintillator-strip **SMD sits after the fifth radiator plate**.
- Light from the towers and the SMD travels on optical fibres to outside the STAR magnet, to PMTs on the **rear of the poletip**.
- The calorimeter hangs from a strong **stainless-steel back plate** bolted to the poletip, and from a **terraced conical stainless-steel hub** at the inner radius, to which the radiator sheets are attached.

![Fig. 1](assets/star2003-eemc/fig1.png)

**Fig. 1.** Schematic EEMC tower structure.
- **Left view:** the tower layout of one half of the EEMC, which has **720 towers in total**. Towers are projective, with edges pointing to the centre of the interaction region. The interaction point is **2.7 m along z from the EEMC front face**.
- **Tower size:** each tower spans **Δφ = 0.1** and **Δη = 0.057 to 0.099**, depending on η.
- **Mounting:** in STAR the two halves are mounted with their dividing line **15° from horizontal**.
- **Right view** (different scale): a constant-φ cross-section showing the depth (z) profile and the structural tie-rods, which sit every **30° in φ**.
- **Stack:** each tower has **23 Pb/stainless-steel absorber layers interleaved with 24 plastic-scintillator layers**.
- **Also marked:** the preshower, postshower and SMD layers, and the stainless-steel mounting ring that fits into a poletip recess and partly carries the lower half.

*Figure description (from the image):* Line drawing, two views side by side. **Left:** a half-annulus (opening to the right, z axis marked ⊗ at the centre) divided into a projective tower grid; I count 30 radial sectors over the 180° (spokes every 6°) and 13 arcs, i.e. 12 η rings per sector. Printed labels: "1.086" at the outer edge (top and bottom ends), "2.00" at the inner edge (both ends), "η" with arrows pointing from 1.086 toward 2.00, "φ" with a curved arrow around the inner edge, "z", and "Δφ = 6°" with arrows across one sector at lower left. Two thin lines run from the 1.086 ends of the left view to the top and bottom of the right view. **Right:** cross-section in depth ("depth →" at top), with many thin vertical absorber/scintillator layers that step outward (projective staircase) at the bottom. Printed labels: "SS hub" (hatched, along the slanted top edge), "Al front plate", "mounting-ring" (hatched tab sticking out of the back), "tie-rods" (two arrows to two horizontal rods crossing the stack), "pre-shower" (two arrows to the first two layers), "SMD", "Pb/SS", "plastic scint.", "post-shower" (last layer) and "SS back plate" (hatched, rear). No dimensions, layer thicknesses or radii are printed in either view.

**[note]** Confirmed: the drawing prints "Δφ = 6°" while the caption says Δφ = 0.1; 6° = 0.105 rad, so the caption value is rounded. The grid in the drawing (30 sectors per half, 12 η rings) agrees with 720 towers in total. The caption's 2.7 m, the 15° tilt of the dividing line and the 30° tie-rod spacing are not printed (the half is drawn with a vertical dividing line).

**[note]** The right view prints no layer thicknesses, and the individual layers cannot be counted reliably at this resolution, so neither the 23 + 24 layer count nor the 21.4 X₀ depth question can be checked from this drawing.

**[note]** Checks on the Fig. 1 geometry:
- **Tower count:** 720 towers = 60 φ-sectors × 12 η-bins ✓. 360°/6° = 60, and the 12 η-bins match the 12 tiles of a 6° megatile.
- **Δφ:** the drawing labels Δφ = 6°, which is 0.105 rad. The caption's "Δφ = 0.1" is a rounded value: 60 × 0.1 rad would not close 2π.
- **Δη:** the mean η-bin width is (2.00 − 1.086)/12 = 0.076, which lies inside the quoted 0.057–0.099 range ✓.
- **Radii at the front face** (z = 270 cm from the IP): r = z / sinh η gives **74.4 cm at η = 2.00** and **205.7 cm at η = 1.086**.
  - The SMD radii in Fig. 3 (77.7 cm and 217 cm) imply z ≈ 281.8 cm at η = 2.00 and ≈ 284.8 cm at η = 1.086. That is ≈ 12–15 cm behind the front face, consistent with the SMD sitting after the 5th radiator ✓ (approximately).

**Standard layer.**

- **Absorber:** a Pb/stainless-steel laminate. Each radiator sheet is **4.57 mm calcium-loaded Pb laminated with 0.5 mm stainless steel on each face**, about **0.85 radiation lengths** in total.
- **Active layer:** a **4 mm Kuraray SCSN-81** plastic scintillator.
- The four specially configured layers (preshower, postshower, SMD) are described in later sections.

**Mass and structure.**

- Radiator sheets plus active elements weigh **≈ 25,000 kg** for both halves together.
- Following D0 [7] and CDF [8] endcap designs, the large loads are carried by stainless steel, ultimately by the back plate and the hub. The Pb only fills the laminated radiator plates.
- **Tie-rods** bolt the aluminium front plate to the back plate at two radii, along radial lines every 30° in azimuth (Figs. 1 and 3). They pass through stainless-steel inserts in every radiator sheet, so the detector divides naturally into **30° modules**.

**Depth and sampling.**

- The whole assembly is **21.4 radiation lengths at normal incidence**.
- It gives a **shower-energy sampling fraction of 5.0%**. Ref. [3] shows this gives enough resolution and depth for the physics programme.
- On average, **∼1 X₀ of STAR material** lies in front of the EEMC along particle trajectories.
- The whole assembly is **slightly less than one hadronic interaction length**.

**[note] Depth check** (PDG X₀: Pb 0.56 cm, stainless steel ≈ Fe 1.757 cm, scintillator 41 cm):

| Item | Recomputed |
|---|---|
| One radiator sheet: Pb part, 0.457 cm / 0.56 cm | 0.816 X₀ |
| One radiator sheet: steel part, 0.10 cm / 1.757 cm | 0.057 X₀ |
| One radiator sheet, total | **0.873 X₀** (paper "≈ 0.85" ✓ within rounding; Ca-loaded Pb is slightly less dense than pure Pb) |
| 23 radiators | 20.1 X₀ (19.6 X₀ with 0.85 each) |
| 24 scintillators (21 × 4 mm + 3 × 5 mm pre/post, §4) | 0.24 X₀ |
| SMD (36 mm of polystyrene-like material) | ≈ 0.09 X₀ |
| **Sum** | **≈ 20.4 X₀** (≈ 19.9 X₀ with 0.85 per sheet) |

The paper quotes **21.4 r.l.**, ≈ 1 X₀ more than this sum. The difference is plausibly the Al front plate, the fibre-routing layers and the back plate or other structure, none of whose thicknesses are given. The figure is therefore **≈ ✓ but not fully reconcilable** from the information in the paper. The ≥ 20 X₀ requirement of Table 1 is met either way.

**[note] Sampling-fraction check.**

- A MIP-based estimate uses dE/dx of polystyrene 2.0 MeV/cm, Pb 12.74 MeV/cm and Fe ≈ 11.4 MeV/cm. It gives 0.80 / (0.80 + 5.82 + 1.14) ≈ **10.3%**.
- The quoted EM sampling fraction of **5.0%** is about half of this. That is plausible: e/mip ≈ 0.5–0.6 is typical of Pb/scintillator samplers, where soft shower electrons are absorbed in the high-Z layers. The 5.0% is presumably from GEANT.
- A rough stochastic-term estimate, 2.7% × √(d_scint[mm] / f_mip), gives 2.7% × √(4/0.103) ≈ **17%/√E**. This is comparable to the 16%/√E requirement. It is a rule-of-thumb only, not from the paper.

**Megatiles.**

- Tower segmentation uses **megatile** construction, developed for CDF [5] and adopted for the BEMC [6].
- EEMC megatiles span **6° or 12° in φ**. Machined isolation grooves divide them into **12 or 24 trapezoidal tiles** respectively.
- One 30° sector of a layer = **two 12° megatiles**, each flush against the tie-rods on its side, plus **one 6° "keystone" megatile**.

**Limiting dead regions.**

- The megatiles are **slightly staggered in azimuth** from layer to layer, which reduces shower-energy loss in the cracks between megatiles and near the tie-rods. The stagger comes from small tailored notches in the 12° megatile edges that engage the tie-rods (like the SMD tie-rod notches of Fig. 3, but smaller).
- The **15° tilt** of the dividing line between the halves lines the tie-rods up with the thick spokes that define the 30° sector structure in the endcap of the STAR TPC.

**WLS fibres in the tiles.**

- **Kuraray Y11 (200 ppm), 0.83 mm diameter** WLS fibres sit in **σ-shaped grooves** machined in each tile face.
- They run through channels in a white plastic **fibre-routing layer (FRL)** to the η ≈ 1 (outer) edge of each megatile; Fig. 2 shows a megatile and its FRL.
- **Wiggles** machined into the FRL channels take up slack. This allows **equal-length WLS fibres for every layer of a given tower** despite the projective geometry, which meets the tile-to-tile light-uniformity requirement within a tower and makes fibre bundles easier to prepare.

![Fig. 2](assets/star2003-eemc/fig2.jpg)

**Fig. 2.** Close-up photographs near the η = 1 edge of an assembled 6° megatile.
- **Upper photo:** the machined isolation grooves and σ-grooves in the scintillator. Running near the upper edge is the "leaky" UV-transparent fibre that illuminates each tile with diagnostic laser pulses.
- **Lower photo:** the other side of the fibre-routing layer, with WLS fibres in undulating channels from which they enter the σ-grooves of each tile.

*Figure description (from the image):* Two black-and-white photographs stacked vertically; no printed labels or scale in either. **Upper:** a white scintillator megatile seen at an angle, showing three full tiles and part of a fourth, separated by straight isolation grooves; each tile has a bright rounded-rectangle loop (the σ-groove with fibre) near its border, and a thin bright fibre runs along the upper edge across the tiles into a fixture at the right end. **Lower:** the other side, a flat white plastic layer with a broad bright undulating (sinusoidal) band of fibres running from the right edge leftward, plus thin curved arcs where individual fibres branch off; at the right edge are connectors/brackets with screws and a stuck-on label whose text is unreadable.

**[note]** The image matches the caption (σ-grooves and isolation grooves in the upper photo; undulating fibre channels in the lower). That the fibre along the upper edge is the leaky laser fibre is the caption's statement; the photo itself does not label it.

**Light path to the tower PMTs.**

1. At each megatile edge, optical connectors couple the WLS fibres of the 12 tiles in a given 6° sector to **0.9 mm clear fibres**. These run to the rear of the poletip.
2. There, the clear-fibre bundles from all **24 scintillator layers** of a 6° sector go into one steel box. The box houses the **12 PMTs (Electron Tubes Ltd 9107B)** for that sector's towers.
3. Inside each box, a **fibre harness** of 1 mm clear fibres, **20–45 cm** long, regroups the light from megatile groupings into tower groupings.
4. An **optical mixer** combines the light of the 24 layers of a tower onto **one PMT**. The PMT signal is proportional to the total energy deposited in the tower.

**PMTs and photoelectron yield.**

- **Bases:** Cockcroft–Walton bases (spelled "Cockroft–Walton" in the paper), fed with **160 V DC**, generate a specially tapered dynode high-voltage distribution.
- **Linearity:** at a gain of **2 × 10⁵** the PMTs are linear to **±2%** for peak pulse currents from 0 up to at least **50 mA**, which corresponds to shower energies **∼100 GeV**.
- **Photoelectron yield:** with the full installed optical chain and PMTs, a cosmic muon crossing one 4 mm tile at normal incidence gives on average **2.3–3.2 photoelectrons**, depending on WLS fibre length. This is sufficient for the tower resolution requirement.

**[note] Photostatistics check.**

- A MIP deposits ≈ 0.8 MeV in 4 mm of scintillator, so the yield is ≈ 2.9–4.0 p.e. per MeV of visible energy.
- With a 5.0% sampling fraction, 1 GeV of shower energy gives ≈ 50 MeV visible, i.e. **≈ 145–200 p.e./GeV**. The photostatistics term is then ≈ **7–8%/√E**. That is subdominant but not negligible beside the 16%/√E requirement when added in quadrature to the sampling term.

**[note] PMT linearity check.** 100 GeV × ≈ 170 p.e./GeV × 2 × 10⁵ × e ≈ 0.54 nC. Over a ≈ 10–20 ns pulse this is ≈ 27–54 mA, consistent with the quoted "50 mA ↔ ∼100 GeV" ✓.

### 3. Shower-maximum detector design and performance

**Depth and purpose.**

- The SMD sits about **5 X₀ deep**. It provides the fine granularity needed to tell the transverse profile of a single photon from that of the close photon pair from π⁰ or η⁰ decay.
- The depth is a compromise: the statistical definition of the profile improves somewhat deeper, while the overlap of the two daughter showers gets worse with depth.
- The SMD also helps e/h discrimination and the matching of e± hits to TPC tracks.

**Strips and planes.**

- The SMD is made of **extruded polystyrene-based scintillator strips with triangular cross-section**. They form orthogonal **u and v planes** (Fig. 3).
- The triangular shape shares the energy deposit between neighbouring strips. This improves position resolution and the stability of the measured profile shape. D0 developed a similar design for its tracking preshower [9].

**Modules and overlap.**

- The SMD is built in (nominally) **30° modules**. Each module has notches cut on one radial edge, so most strips can extend a few cm past the tie-rods.
- Adjacent u- or v-sectors are offset longitudinally so that their azimuthal coverage overlaps. This gives an essentially gapless detector (except very near the tie-rods) from **three layers of 36 mm total depth**.
- Each **90° segment** of each of the three layers holds **one active u-plane module, one active v-plane module, and one plastic spacer module** spanning slightly less than 30°.

![Fig. 3](assets/star2003-eemc/fig3.png)

**Fig. 3.** Layout of one 30° SMD sector. Each of the two orthogonal planes is built from triangular scintillating strips extruded with an axial hole for the WLS fibre. Labels in the drawing:
- 30° opening angle;
- **217 cm** outer radius and **77.7 cm** inner radius;
- "3 cm" offset at the tie-rod edge;
- u-plane and v-plane SMD, and the tie-rod notches;
- in the inset: strip height **7 mm** and base **10 mm**, with the WLS fibre on the axis of each extruded strip.

*Figure description (from the image):* Line drawing of two hatched 30° wedge-shaped modules, the u-plane module upper right and the v-plane module drawn displaced to the lower left, plus a circular magnified inset at lower right. Printed labels: "30°" (opening angle between two radial lines), "217 cm radius" (outer arc), "77.7 cm radius" (inner arc, arrows to both modules), "3 cm" (dimension between the radial sector boundary line and the module edge at upper left), "u-plane SMD", "v-plane SMD", "tie-rod notches" (two arrows to notches cut in the left radial edge; the v-plane module also has notches on its right edge). A row of short dark bars runs along the outer arc of each module (unlabelled). The inset (linked to a circle on the u-module's right edge by a double arrow) shows a row of alternating apex-up and apex-down triangular strips between two horizontal lines, each with a small circular hole; labels "wavelength-shifting fiber" (arrow to a hole), "plastic scint. (extruded strips)", "7 mm" (height of the strip layer) and "10 mm" (dimension lines between two adjacent bottom vertices, i.e. the base of one triangle).

**[note]** The inset agrees with the note's reading: the 10 mm is the base of one triangle and neighbouring strips alternate orientation, so the strip pitch is ≈ 5 mm (half the base); the pitch itself is not printed. 7 mm and 10 mm are the only thicknesses in the drawing; the 36 mm total SMD depth and the radiator thicknesses are not shown, so the figure gives no check of the 21.4 X₀ depth.

**[note] Strip counts and pitch.**

- In the Fig. 3 inset the strips alternate apex-up and apex-down with a 10 mm base, so the strip-to-strip pitch is ≈ 5 mm. This pitch is my reading of the drawing; the paper does not state it.
- 286 strips × 5 mm ≈ 143 cm, comparable to the radial extent 217 − 77.7 = 139.3 cm of a sector ✓ (approximately).
- Total strips: 12 sectors × 572 = **6864** (3432 per plane orientation). This is derived; the paper gives only the per-sector numbers.

**SMD optical readout.**

- **WLS fibres** run the length of each strip in **1.0 mm axial holes** formed during extrusion.
- They leave the module by one of two paths:
  - directly at the outer circumference of the SMD, where they are grouped in **8-fibre optical connectors**; or
  - along the radial sector edge opposite the tie-rod notches. These fibres bend round to the outer circumference through a grooved FRL mounted on the strip plane, and are coupled there to clear fibres via **12-fibre connectors**.
- Clear fibres carry the light to **16-anode PMTs (Hamamatsu R5900-M16)** in steel boxes on the rear of the poletip.
- **Three boxes, each with 12 MAPMTs** plus their Cockcroft–Walton bases and front-end electronics, serve the **572 strips (286 per plane) of each 30° sector**. **[note]** 3 × 12 × 16 = 576 anodes ≥ 572 strips ✓.
- The fibre-to-pixel mapping is chosen so that the small inter-pixel **crosstalk (∼1% in amplitude)** is unlikely to distort the apparent transverse profile in a physically significant way.

**Light yield.** Cosmic-ray tests of prototype planes gave **0.6 photoelectrons per mm of strip thickness** traversed by a MIP, at the MAPMT photocathode. **[note]** For a 7 mm strip at its full height this is ≈ 4 p.e. per MIP. A track through the triangular strip sees on average half of that path length per strip, shared between two strips.

**Simulated π⁰/γ separation [3].** With this light output, the discrimination algorithm of Fig. 4 rejects **80% of π⁰'s at 10–40 GeV while keeping 80% of photons** of similar energy.

- Combined with isolation cuts that remove π⁰'s embedded in jets, this is enough background suppression for the direct-photon ΔG measurement.
- Photon retention could improve further with an invariant-mass cut on apparent two-photon events, using the energies and positions of the two SMD clusters.

![Fig. 4](assets/star2003-eemc/fig4.png)

**Fig. 4.** Two-dimensional SMD response distributions used to separate γ from π⁰(η⁰) events in the EEMC.
- **Simulation:** PYTHIA [10] events for the two reactions shown, at $\sqrt{s_{pp}}$ = 200 GeV and equal integrated luminosity. Kinematic and isolation cuts favour γ–jet coincidences in STAR.
- **Fit:** GEANT shower profiles are fitted with a lineshape matching the average simulated SMD response to single photons.
- **y-axis:** the fitted peak integral, summed over the u and v planes.
- **x-axis:** the summed "sided" fit residual, $R_{0,u} + R_{0,v}$. In each plane the residual is taken on the side of the peak where the fit deviates most from the data, as a second peak would cause.
- **Result:** about **80% (20%) of photon (meson) events lie above the curve** drawn in both panels.
- Panel labels: left "π⁰(η⁰) Events From p p → π⁰(η⁰) + jet + X"; right "γ Events From p p → γ + jet + X". Both axes run 0–250 (y) and 0–200 (x), with a log colour scale 1 to >10².

*Figure description (from the image):* Two side-by-side 2D histograms in grey scale, each with its own colour bar. y axis "Fitted Peak Integral", 0–250 (labels 0, 50, 100, 150, 200, 250); shared x axis "Fit Residual Sum (R_{0,u} + R_{0,v})", 0–200 (labels 0, 50, 100, 150, 200); no units printed. Dashed grid lines every 25 in y and every 50 in x. Colour bars are logarithmic with labels "1", "10" and "10²" and one black band above 10². **Left** (legend "π⁰(η⁰) Events From p p → π⁰(η⁰) + jet + X"): a broad distribution densest near the origin (black bins up to x ≈ 30, y ≈ 80) that spreads across the full x range to 200 and up to y ≈ 240. **Right** (legend "γ Events From p p → γ + jet + X"): a narrow band hugging the y axis, x ≲ 75, y up to ≈ 245. The same solid curve is drawn in both panels, rising from y ≈ 17 at x = 0 to y ≈ 225 at x = 50 and leaving the top at x ≈ 53; most photon entries lie on its upper-left side, most meson entries on its lower-right side (positions read off the plot).

**[note]** The image matches the caption and the note's axis description (0–250 in y, 0–200 in x, log scale 1 to above 10²). The 80%/20% fractions are not printed on the figure.

**SLAC test beams.**

- GEANT shower development for this geometry was compared with **two test-beam exposures of a 12-tower EEMC prototype**. The prototype included an SMD layer with **x and y strips read by MAPMTs**.
- **Beam:** Final Focus Test Beam at **SLAC**, **5, 10 and 20 GeV electrons**, typically **1–2 electrons per pulse**.
- The prototype was scanned horizontally and vertically across the beam to map the position dependence of its response.

**First run (October 1999).** The prototype SMD used triangular strips only **5 mm apex-to-base**, obtained from D0. Fig. 5 shows the response of every strip averaged over many **5 GeV** single-electron events, at three detector positions.

- The **downstream y-plane** profile is **quantitatively reproduced** by the simulation. The simulation uses GEANT showers and includes photostatistics, intrinsic MAPMT resolution and crosstalk.
- The **upstream x-plane** profiles are **slightly broader** than simulated.

**Second run (January 2001).** Strips of the final geometry gave consistent results. The cause of the difference between the two planes was still under investigation.

**Next step.** The SMD response to π⁰'s was to be measured in the **2001 RHIC run**, with the prototype EEMC installed at a far-forward location in STAR.

![Fig. 5](assets/star2003-eemc/fig5.png)

**Fig. 5.** Average EM shower profile measured by the x-plane (left) and y-plane (right) of the prototype SMD at SLAC.
- **Points:** measured average pulse heights for **5 GeV** single electrons.
- **Solid histograms:** simulation.
- **Rows:** three horizontal detector positions ("Detector Location 1, 2, 3"). The x-plane axis covers strips 0–60 and the y-plane axis strips 0–100; average pulse height runs 0 to ≈ 500.

*Figure description (from the image):* Six panels in three rows × two columns. Shared y label "Average Pulse Height" (tick labels 0, 200, 400; the frame extends to ≈ 570). Left column x axis "SMD x strip #", 0–60 (labels 0, 20, 40, 60); right column "SMD y strip #", 0–100 (labels 0, 20, …, 100). Each panel has open circles (data) and a grey stepped histogram (simulation), and a label "Detector Location 1", "2" or "3" by row. x-plane peak at about strip 55 (location 1), 31 (location 2) and 5–6 (location 3); y-plane peak at about strip 40 in all three rows. Baselines ≈ 20–60 away from the peak. The simulated histogram peak reaches or runs past the top of the frame in every panel; data maxima are ≈ 450–550 (read off the plot). In the x-plane panels the data points sit visibly above the histogram on the flanks of the peak; in the y-plane panels data and histogram coincide closely. The location-3 y-plane histogram has an extra bump near strips 1–3 (≈ 120).

**[note]** Consistent with the caption (horizontal scan: the x-plane peak moves while the y-plane peak stays near strip 40) and with the text (x-plane slightly broader than simulated). The note's "average pulse height runs 0 to ≈ 500" understates the frame, which extends to ≈ 570; only 0, 200 and 400 are labelled.

### 4. Preshower/postshower layers

**Dual-fibre readout.**

- The **first two scintillator layers** behind the front plate and the **last layer** each have **two independent WLS fibres** in deeper-than-normal σ-grooves.
- One fibre per tile adds its light to the other layers at the tower PMT.
- The second fibre is read out separately, **one Hamamatsu R5900-M16 MAPMT channel per tile**, forming the preshower or postshower detector.

**Physics use.**

- Comparing a tile's light with the whole tower helps separate electrons from hadrons, through their very different shower probabilities and longitudinal development.
- The preshower also helps π⁰/γ separation for the highest-energy photons, because a γ is **roughly twice as likely** as a π⁰ of similar energy to deposit no energy in these layers.

**Scintillator.**

- For adequate photostatistics, the pre/postshower tiles use **thicker (5 mm), brighter (Bicron BC400)** scintillator than normal megatiles.
- The dopant concentration of the WLS fibres that feed the tower sum is adjusted so that, for a given energy deposit, these tiles give the same light as normal layers.

**[note]** The paper gives no pre/postshower channel count. Derived: 3 layers × 720 tiles = **2160 MAPMT channels**.

**Simulated e/h performance.**

| Cut | Hadron/electron suppression |
|---|---|
| Preshower energy loss (5–30 GeV/c) | factor **≈ 4.5** |
| Postshower energy | additional factor **2** |
| SMD-to-tower energy ratio (independent alternative) | factor 2 |

- **Why it matters.** EEMC-only discrimination is important in the endcap. There, worse TPC tracking resolution weakens the otherwise powerful comparison of TPC $p_T$ with calorimeter $E_T$.
- **W± and Drell–Yan:** an isolation cut around the electron candidate suppresses the hadronic background to W± by **another order of magnitude** [3]. So does an independent cut that rejects (dijet) events with sizable energy opposite in azimuth to the electron.
- **π⁰/γ:** the preshower gives an extra π⁰/γ suppression of **≈ 2**, but at the cost of substantially fewer surviving photons.

### 5. Front-end electronics and triggering

**Tower readout.**

- The BEMC tower readout and trigger electronics are used for the EEMC towers essentially unchanged, and already include the triggers needed for spin physics.
- Tower pulse heights are digitised by **12-bit flash ADCs every RHIC crossing** and stored in digital pipelines.

**Level 0 and triggers.**

- The STAR **level-0 trigger** can compare single-tower ADCs and **multi-tower sums** with thresholds, and look for simple correlations with other subsystems.
- **Primary trigger** for high-$p_T$ direct photons and W±: a **very high $E_T$ in a single tower**, i.e. a high-tower trigger.
- **Jets** are flagged by large $E_T$ plus large charged multiplicity, measured in the Central Trigger Barrel and the Multi-Wire Chamber at the TPC end, in extended correlated regions.
- For triggered events, the full tower ADC information covers single MIPs (e.g. non-showering charged hadrons) up to **150 GeV** electrons.

**[note]** The phrase "jet patch" does not appear in the paper. The jet trigger is described only as large $E_T$ in extended regions plus multi-tower sums at L0.

**MAPMT front end (SMD, preshower, postshower).**

- This electronics was still under development.
- Each MAPMT anode feeds its own **preamplifier, gated integrator and 12-bit ADC** with remotely adjustable conversion gain, digitising every crossing.
- **192 channels** of this electronics, plus a **multiplexer board** for buffering and simple data manipulation, sit in the same steel box as the **12 MAPMTs** they serve. **[note]** 12 × 16 = 192 ✓.
- MAPMT data are not planned for level 0 but are available at **level 2**. For example, they could suppress hadrons to keep trigger rates manageable for J/ψ or low-mass dilepton studies in p+p.

**TPC pile-up.**

- The slow TPC drift is a particular problem for p+p at the expected **∼10³² cm⁻² s⁻¹**. Each triggered event comes with **up to a few thousand pile-up track segments** from several hundred crossings before and after.
- **Level-3 processors** [11] will prune pile-up tracks and reduce data volume.
- Matching TPC tracks to prompt EMC hits allows a quick vertex estimate. This is a key part of the algorithm that removes TPC clusters on tracks matching neither fired EMC towers nor the event vertex.

### 6. Calibration systems

**Requirements.**

| Quantity | Requirement |
|---|---|
| Absolute tower energy scale | eventually **±2%** |
| Tower gain matching before first beam | **±10%** |
| Relative gains of SMD strips and pre/postshower tiles | eventually **±10%** |
| Hardware gain compensation for MAPMT channels | **±20%**, via ADC conversion-gain adjustment |

- **Absolute scale.** The final ±2% calibration will be done **in situ**, e.g. from the π⁰ and Z⁰ invariant-mass peaks, cross-checked with broader resonances such as ρ±.
- **Tower gain matching to ±10% before first beam** is needed so that the desired spectral landmarks fit within each channel's tight dynamic range, and so that high-gain channels do not dominate the trigger rate.
- **MAPMT channels.** The ±10% relative gains are needed for the γ/π⁰ and e/h performance. Because these channels are not in the L0 trigger, their hardware matching only has to fit the interesting dynamic range into **12 bits**. MAPMT gain spread and the wide range of WLS fibre lengths cause large channel-to-channel variations, which the ADC conversion gain must compensate at the **±20%** level.
- **Monitoring.** Gain stability of every tower, SMD, preshower and postshower channel must be monitored over the calorimeter's lifetime, to catch sudden failures promptly and to track slow deterioration.

**Three complementary injection systems** are planned:

- **Pulsed UV laser (355 nm)**, externally triggerable.
  - It injects light directly into every scintillator tile of all towers, through "leaky" (abraded) UV-transparent fibres running radially inward in each megatile's FRL.
  - It monitors almost the whole optical chain of the towers and the pre/postshower layers.
  - An adjustable attenuator at the laser output allows **linearity checks over the full dynamic range**.
  - Laser intensity is monitored by PMTs that also view **α-sources** embedded in scintillator.
  - Variable beamsplitters can inject pulses into chosen tower layers, for diagnostics or to vary the longitudinal profile of the injected energy.
- **Pulsed LEDs.**
  - They flash directly into each tower PMT and into **one pixel of each pre/postshower MAPMT**, to monitor stability.
  - For the SMD, LEDs replace the laser: they inject pulses into the WLS readout fibres and monitor most of each channel's optical chain.
- **⁶⁰Co source, 300 μCi**, on the end of a long thin rod.
  - It is inserted by hand through the light-tight skin and irradiates all SMD strips and the tower layers near the SMD in depth.
  - It can be routed through **radial holes in the plastic spacer layers** of the SMD when the poletip is separated from the rest of STAR.
  - The peak currents measured during source scans allow an absolute calibration made at one location to be transferred to another.

**Overall calibration scheme.**

- The absolute EEMC scale is set with **cosmic rays, detector horizontal**.
- It is extended over the full dynamic range with the **laser**.
- It is transferred between locations with the **⁶⁰Co source** (primary method) and **cosmic rays with the detector vertical** (secondary method).
- The scheme is checked with **test beams on a small prototype**, not on a full half.

### 7. Summary

- **Installation plan:** the lower half of the EEMC in the **summer-2002 RHIC shutdown**, and the upper half a year later.
- Together with the BEMC, this gives STAR extensive EM calorimetry to complement TPC tracking.
- The new subsystems will greatly improve STAR's measurement and triggering for high-$p_T$ particle spectra in A+A, p+A and polarized p+p collisions.

### Acknowledgements (summary)

The authors thank:

- earlier EEMC designers (T. Fornek, E. Bielick, S. Heppelmann);
- several advisers from Fermilab, BNL, D0/CDF, JLab and elsewhere;
- the STAR BEMC group;
- SLAC staff (T. Fieguth, R. Iverson) for the beam tests;
- the Fermilab extrusion group (A. Pla, K. Mellott) for SMD scintillator preparation;
- technical staff who contributed to the design and construction.

Support: US NSF (PHY-9602872, PHY-9977216, PHY-9971947 and others) and US DOE (W-31-109-ENG-38, DE-FG03-93ER40765 and others).

---

## Checks

**(a) EEMC geometry**

- **η coverage:** 1.086 ≤ η ≤ 2.00 (design requirement 1 ≲ η ≤ 2).
- **φ coverage:** full 2π, built as two halves. The dividing line is 15° from horizontal, so the tie-rods line up with the TPC endcap spokes.
- **z position:** the front face is **2.7 m from the interaction point** along z, on the west poletip.
  - **[note]** Front-face radii: 74.4 cm at η = 2 and 205.7 cm at η = 1.086.
  - The SMD spans radii 77.7–217 cm, ≈ 12–15 cm deeper.
- **Towers:** **720** projective towers = 60 in φ × 12 in η. Each spans Δφ = 6° (≈ 0.1 rad) and Δη = 0.057–0.099.
- **Megatiles:** 6° (12 tiles) or 12° (24 tiles). Each 30° sector = 2 × 12° + one 6° keystone.
- **Depth:** **21.4 X₀** at normal incidence, plus ≈ 1 X₀ of upstream STAR material; slightly less than 1 λ_I.
  - **[note]** Recomputed from the layers: ≈ 20.4 X₀ (≈ 19.9 X₀ with the paper's 0.85 X₀ per sheet). The missing ≈ 1 X₀ is presumably front plate and structure, which the paper does not itemise.
- **Layers:** 23 absorbers + 24 scintillator layers.
  - **Absorber:** 4.57 mm Ca-loaded Pb + 2 × 0.5 mm stainless steel, ≈ 0.85 X₀ (recomputed 0.873 ✓).
  - **Scintillator:** 4 mm Kuraray SCSN-81. The preshower 1, preshower 2 and postshower tiles are 5 mm Bicron BC400.
  - **SMD:** after the 5th radiator, at ≈ 5 X₀.
- **Sampling fraction:** **5.0%** (EM). **[note]** The MIP-based estimate is 10.3%.
- **Mass:** ≈ 25,000 kg for both halves (radiators plus active elements).

**(b) Preshower, postshower and SMD**

- **Preshower/postshower:**
  - Tiles of scintillator layers 1 and 2 (preshower) and of the last layer (postshower), i.e. the same 720-tower tile pattern.
  - Each tile has two WLS fibres: one goes to the tower PMT sum; the other to one Hamamatsu R5900-M16 MAPMT pixel per tile.
  - 5 mm BC400; WLS dopant adjusted so the summed light matches normal layers.
- **SMD:**
  - Extruded polystyrene-based scintillator strips of **triangular cross-section**: **7 mm high, 10 mm base** (Fig. 3), with a 1.0 mm axial hole for a WLS fibre.
  - The 1999 prototype used 5 mm-high D0 strips.
  - Two orthogonal planes, **u and v**, with **286 strips per plane per 30° sector** (572 per sector; 6864 in total, derived).
  - Three physical layers, 36 mm total depth. Each 90° contains one u module, one v module and one spacer module per layer; modules are offset longitudinally for overlap.
  - Radii 77.7–217 cm.
  - **Readout:** WLS fibre → 8- or 12-fibre connectors at the outer circumference → clear fibre → **Hamamatsu R5900-M16 16-anode MAPMTs**. 3 boxes × 12 MAPMTs per 30° sector. Inter-pixel crosstalk ∼1%.
  - **Light yield:** 0.6 p.e. per mm of strip for a MIP.

**(c) Readout chain**

- **Towers:**
  - Kuraray Y11 (200 ppm) WLS fibres, 0.83 mm, in σ-grooves, routed through the FRL; equal lengths within a tower.
  - Optical connector at the megatile edge → 0.9 mm clear fibre to the back of the poletip.
  - Fibre harness (1 mm clear, 20–45 cm) and optical mixer → **one Electron Tubes 9107B PMT per tower**, 12 PMTs per 6° box.
  - Cockcroft–Walton bases (160 V DC in), gain 2 × 10⁵, ±2% linear to ≥ 50 mA (∼100 GeV).
  - 2.3–3.2 p.e. per MIP per tile.
- **Tower electronics:**
  - BEMC electronics reused: 12-bit flash ADC every crossing, digital pipelines.
  - **L0 trigger** on single-tower ADC thresholds (**high-tower trigger** for direct γ and W) and on multi-tower sums.
  - Jets: large $E_T$ plus CTB/MWC multiplicity in extended regions. The term "jet patch" is not used in the paper.
- **MAPMT electronics** (SMD, preshower, postshower):
  - Per anode: preamp + gated integrator + 12-bit ADC with remotely adjustable gain, digitised every crossing.
  - 192 channels plus a multiplexer board per box of 12 MAPMTs.
  - Not used in L0; available at L2.
  - Level 3 handles TPC pile-up pruning using EMC hit matching.

**(d) Calibration and performance**

- **Energy resolution:** requirement only, **σ_E/E ≤ 16%/√E + 2%** (linear sum as written). **No measured stochastic or constant term** is given in this paper.
- **Linearity:**
  - Requirement < 10% integral non-linearity over ∼1–150 GeV.
  - PMT linearity ±2% up to ≥ 50 mA (∼100 GeV).
  - The laser attenuator is for linearity checks over the full range.
- **Dynamic range:** E_min ≈ 0.2 GeV (MIP) to E_max = 150 GeV per tower.
- **π⁰/γ (simulation):**
  - 80% π⁰ rejection at 80% γ efficiency, 10–40 GeV, from SMD profile fits.
  - The preshower gives an extra factor ≈ 2 at a cost in statistics.
  - Requirement: suppression > 3 for $p_T$ ≈ 10–20 GeV/c.
- **e/h (simulation):** preshower ≈ 4.5 (5–30 GeV/c); postshower × 2 (or the SMD/tower ratio × 2); isolation and away-side cuts × 10 each for W.
- **Test beam:**
  - SLAC FFTB, Oct 1999 and Jan 2001, 12-tower prototype, 5/10/20 GeV e⁻.
  - SMD y-plane profile matches GEANT; x-plane slightly broader than simulated (unexplained at the time of writing).
  - No resolution numbers are quoted.
- **Cosmics:**
  - 2.3–3.2 p.e. per tile (tower chain) and 0.6 p.e./mm (SMD).
  - Cosmics (detector horizontal) set the absolute scale; cosmics (detector vertical) are the secondary transfer method.
- **Calibration hardware:** 355 nm UV laser via leaky fibres (monitored with α-source PMTs); LEDs into PMTs, one pre/post MAPMT pixel each, and the SMD WLS fibres; 300 μCi ⁶⁰Co rod source through the SMD spacer layers.
- **Targets:** tower absolute ±2% (±10% online/pre-beam); SMD and pre/post relative ±10%; hardware ±20% via ADC gain.
- **In situ:** π⁰ and Z⁰ masses, with ρ± as a cross-check.

**(e) Rates, radiation, ageing**

- **Rates:**
  - Tower occupancy < 10% at L_pp = 2 × 10³² (Table 1).
  - Tower size ≳ 2 shower diameters.
  - Timing response < 1 beam period (110 ns).
  - TPC pile-up at ∼10³² cm⁻² s⁻¹: up to a few thousand pile-up segments per trigger, handled by Level 3 using EMC–track matching.
  - MAPMT information at L2 to control J/ψ and dilepton trigger rates.
- **Radiation and ageing:** **nothing quantitative.** The only related statement is that gain stability of every channel must be monitored over the detector's lifetime, to catch sudden failures and slow deterioration, using the laser, LED and ⁶⁰Co systems.
- **[note]** This is a pre-installation design paper (written 2001–2002). Its "2001 RHIC run" prototype and installation dates are plans. For context, the STAR detector status table (October 2026; see [[rhic-detector-status]]) lists the Endcap EMCal as "All", "In situ; no readout".

---

## References (hardware-relevant subset; full list has 11 entries)

- [3] L.C. Bland et al., STAR Note 401 (1999). EEMC conceptual design and simulations: resolution, π⁰/γ, e/h, W isolation.
- [5] S. Kim, Nucl. Instr. and Meth. A 360 (1995) 206. CDF megatile construction.
- [6] Technical Design Report for the Barrel EMC in STAR (1998).
- [7] W. Edwards, private communication. D0 endcap structural design.
- [8] G. Apollinari, P. de Barbaro, M. Mishina, Proc. 4th Int. Conf. on Calorimetry in HEP, Elba (1993); CDF II TDR, FNAL Pub-96/390-E (plug calorimeter).
- [9] M. Adams et al., Nucl. Instr. and Meth. A 378 (1996) 131. D0 triangular-strip scintillator preshower.
- [10] T. Sjöstrand, Comput. Phys. Commun. 82 (1994) 74. PYTHIA.
- [11] J.S. Lange et al., Nucl. Instr. and Meth. A 453 (2000) 397. STAR Level-3 trigger.
- Physics: [1] G. Bunce, N. Saito, J. Soffer, W. Vogelsang, Annu. Rev. Nucl. Part. Sci. 50 (2002) 525 (sic; the volume year is 2000 in the standard citation, **[source issue]** possible). [2] L.C. Bland, hep-ex/0002061. [4] S.E. Vigdor, Proc. SPIN2000, Osaka (2000).
