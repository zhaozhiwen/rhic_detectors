---
title: "STAR 2018 — The STAR Forward Calorimeter System and Forward Tracking System (proposal, Nov 2018 review version; curated notes)"
type: raw-note
source_type: proposal
companion: star2018-forward-upgrade-proposal.md
authors: "The STAR Collaboration (no individual authors printed)"
journal: "STAR Collaboration proposal, November 2018 (version prepared for the November 2018 review), 84 pp.; not peer-reviewed"
doi: none
url: "https://drupal.star.bnl.gov/STAR/files/Proposal.ForwardUpgrade.Nov_.2018.Review.pdf"
arxiv: none
notes_updated: 2026-11-16
ingested_version: "local PDF copy supplied by the repo author (84 pages, 25 715 555 bytes; Word-made, clean text layer), same file name as the public STAR drupal copy; read 2026-11-16 via Route 3 (PDF only). User-approved scope: Ch. 1, 3, 4, 5 and the bibliography in full; Ch. 2 (physics case) summarised, with Tables 2-1 and 2-2 in full and its figures by caption only"
earlier_version:
  - "tsai2015-fcs-prototype (the 2014 FCS design and FNAL prototype that this proposal revises; a separate paper, not an earlier text of this document) -- ingested"
later_version:
  - "STAR Note SN0648, 'The STAR Forward Calorimeter System and Forward Tracking System beyond BES-II', https://drupal.star.bnl.gov/STAR/starnotes/public/sn0648 (relation to this text unverified) -- not ingested"
  - "ForwardUpgrade.v20.pdf, https://drupal.star.bnl.gov/STAR/files/ForwardUpgrade.v20.pdf (version relation unverified) -- not ingested"
published_version: "none -- STAR Collaboration proposal, not peer-reviewed; a public copy with the same file name is posted on the STAR drupal site"
version_facts: "Cover dated November 2018; file name marks it as the version for the November 2018 review. The locally ingested PDF has the same file name as the public drupal copy (byte identity with the drupal file not checked). Later STAR documents on the same upgrade exist (SN0648 and ForwardUpgrade.v20.pdf, above); whether either is a revision of this text was not checked. The as-built detector is described by the ingested gagliardi2022-star-forward-upgrade-talk (2022) and wang2024-star-forward-upgrade (2024); those are separate documents, not versions of this one."
versions_checked: 2026-11-16
---

# STAR 2018 Forward Upgrade proposal — Curated Notes

> **Full source:** [star2018-forward-upgrade-proposal](star2018-forward-upgrade-proposal.md) · Companion notes to [star2018-forward-upgrade-proposal](star2018-forward-upgrade-proposal.md) (full source).
> **Links:** no DOI · public copy: https://drupal.star.bnl.gov/STAR/files/Proposal.ForwardUpgrade.Nov_.2018.Review.pdf · **PDF:** `assets/star2018-forward-upgrade-proposal/source.pdf` (printed page = PDF page)

## Bibliographic / source

- **Title:** The STAR Forward Calorimeter System and Forward Tracking System
- **Authors:** The STAR Collaboration (the name appears only as faint text under the cover banner; no author list).
- **Type / date:** proposal, November 2018, review version; 84 pages; 6 chapters (executive summary, physics case, overview and simulation, FCS, FTS, bibliography of 141 entries).

## What kind of source

Collaboration design proposal, **not peer-reviewed**, written two to three years before installation. It is the design-stage description of both forward subsystems: the Forward Calorimeter System (FCS: re-used PHENIX ECal + new Fe/scintillator HCal, SiPM readout, DEP digitizers and trigger) and the Forward Tracking System (FTS: 3 silicon mini-strip disks + 4 sTGC wheels). Numbers are design values, simulations, R&D results and the 2014 FNAL prototype test; nothing is as-built. Tables: 2-1, 2-2 (physics requirements), 3-1 (performance requirements), 5-1 (silicon radiation dose); Fig. 4-19 is a table stored as an image. 96 figures (57 in Ch. 3–5 with vision descriptions in the Layer-3 file).

## Abstract (paraphrased)

STAR proposes, for running after 2020, a forward upgrade covering roughly 2.5 < η < 4 on the west side: an electromagnetic and a hadronic calorimeter plus charged-particle tracking. The cold-QCD programme (polarized p+p and p+A: transverse-spin asymmetries, transversity and Collins/IFF, Δg at small x with di-jets, nuclear PDFs with direct photons and Drell–Yan, gluon saturation) and an A+A programme (longitudinal decorrelation, η/s(T), ridge, global Λ polarization) drive the requirements. For cost reasons the calorimeter design was changed from the originally proposed W/ScFi SPACal + Pb/scintillator HCal to re-used PHENIX ECal towers plus an iron/scintillator HCal, both read out with SiPMs through common front-end electronics and the new STAR DEP digitizer/trigger platform. The tracker combines three silicon mini-strip disks (re-using the IST readout chip, DAQ and cooling) with four ATLAS-style small-strip thin gap chamber wheels (read out with the STAR TPC electronics freed by the iTPC upgrade). Simulations of jets, Drell–Yan e/h separation and tracking, the 2014 FNAL prototype test and a multi-year SiPM radiation study support the design.

## Key numbers

All values are design or simulation values from the 2018 text unless marked; page numbers are printed pages.

### Programme, coverage, requirements

| Item | Value | Where |
|---|---|---|
| PAC 2018 wording | forward upgrade to rapidities up to 4.2 for an additional $5.3 M | p. 4 |
| Forward coverage | 2.5 < η < 4 (most places); "2.5-4.5" (Ch. 1 upgrade description); –4.2 < η < –2.5 (A+A, Table 2-2) | pp. 4–5, 36 |
| Assumed running | 2023/2025: 20 and 24 weeks Au+Au 200 GeV; 2024: 24 weeks polarized pp and pA 200 GeV; proposed extra 20-week polarized pp at 500 GeV (end of FY2021 into Q1 FY22) | p. 6 |
| Table 3-1 ECal | ~10%/√E (pp, pA); ~20%/√E (AA) | p. 38 |
| Table 3-1 HCal | ~50%/√E+10% (pp, pA); — (AA) | p. 38 |
| Table 3-1 tracking | charge separation, photon suppression (pp, pA); 0.2 < p_T < 2 GeV/c with 20-30% 1/p_T (AA) | p. 38 |
| Text resolutions | EM "~8%" (Ch. 1 and §4.1) vs ~10%/√E (§4.2, Table 3-1); hadronic ~50%/√E + 10% | pp. 5, 53 |

**Table 2-1 (pp and pA, abbreviated):** 2024 p↑p @ 200: 300 pb⁻¹, 8 weeks (A_N for charged hadrons and flavour-enhanced jets; ECal+HCal+Tracking); 2024 p↑Au @ 200: 1.8 pb⁻¹, 8 weeks (R_pAu direct photons and DY; dihadrons, γ-jet, h-jet, diffraction; ECal+HCal+Tracking); p↑Al @ 200: 12.6 pb⁻¹, 8 weeks (A-dependence; ECal+HCal+Tracking); 2021/22 p↑p @ 510: 1.1 fb⁻¹, 10 weeks (Collins A_UT; ECal+HCal+Tracking); 2021/22 longitudinal pp @ 510: 1.1 fb⁻¹, 10 weeks (A_LL jets, di-jets, h/γ-jets; ECal+HCal).
**Table 2-2 (A+A):** FCS (–2.5 > η > –4.2, E_T of photons and hadrons) and FTS (charged particles) — one of the two needed for decorrelation, mixed harmonics and event-shape/jet studies; FTS "Important" for η/s(T) and the ridge; FCS "Good to have" for the ridge.

### FCS — calorimeters (Ch. 3.1, 4.1–4.3, 4.7–4.8)

| Item | ECal | HCal |
|---|---|---|
| Technology | refurbished PHENIX sampling ECal (shashlik); 1496 of the 15552 existing PHENIX towers | Fe/scintillator plate sandwich, LEGO-like assembly modelled on the ZEUS Pb/Sc prototype |
| Towers | 1496 | 520 |
| Total area | ≈ 2.6 m × 2 m (whole FCS) | |
| Layers | not given (refers to the PHENIX calorimeter paper, ref. [129]) | 38 Fe/Sc layers, ≈ 4.5 interaction lengths; Fe plates 20 mm; gap 3.1 mm; scintillator 3 mm |
| Light collection | readout mounted on the **front face** of the refurbished ECal so that no significant dead space opens between ECal and HCal (§3.1); FEE bolted to the module front, SiPM carrier board glued to a light-guide block at the end of each tower's fibre bundle (§4.4) | 3 mm WLS plate (EJ-280) in the gap between neighbouring towers, read at the downstream end; BC-620 reflector at the far end, aluminised mylar; printed filter gives uniformity within 10% |
| Simulation sampling fraction | 0.20 | 0.0145 |
| Mechanics | ≈ 10 tons; on the existing FMS rails and rollers (shortened plate), West Platform | ≈ 40 tons; over the west-wall cavity on a new rail-and-roller system with vertical support beams; 5 mm dowel pins, master plate over 1.5 rows of towers |
| Other | Preshower: existing Forward Preshower Detector (2.5 < η < 4), in STAR since 2015, on the FMS preshower structure | tiles cut from Eljen sheets by Ohio University, ACU, Rutgers; IHEP injection moulding dropped |

- Original design (§3.1): SPACal (W powder + scintillating fibres) in front of a Pb/scintillator HCal with 10×10×81 cm³ towers, 4 interaction lengths, fully compensated. Dropped for cost when the PHENIX ECal became free (2016).
- Fig. 4-10 drawing dimensions (read from the drawing): HCal 78.740 × 35.433, ECal 28.035 wide × 79.305 tall — **[note]** presumably inches: 2.000 m × 0.900 m (HCal), ≈ 0.71 m × 2.01 m (ECal).
- **[note]** 2.6 m × 2 m matches the as-built HCal face (2 × 13 × 9.99 cm = 2.60 m by 20 × 9.99 cm = 2.00 m, tower pitch from [ruan2026-fcs-specs-email-note](ruan2026-fcs-specs-email-note.md)).
- **[note]** Proposal HCal pitch 20 + 3.1 = 23.1 mm × 38 layers ≈ 0.88 m; as built 36 layers at 23.4 mm + 10 mm back plate (email).

### FCS — photosensors, FEE, SiPM R&D (§4.4, §4.9)

| Item | Value |
|---|---|
| 2014 FNAL photosensor | Hamamatsu MPPC S10931-025p |
| PHENIX Shashlyk at FNAL 2016 | ≈ 1000 p.e./GeV with PMT readout |
| ECal FEE | 4 towers per board; pogo pins, 4 pins per tower incl. NTC thermistor; 16 Ω load, passive shaper, CMOS-switched attenuator, 50 Ω amplifier/shaper/cable driver |
| HCal FEE | 2 towers per board, ~3 cm cables to the SiPM carriers, slightly different gain |
| Gain | normal full scale 180 GeV; ≈ 5x higher gain setting for vertical cosmics; relative gain < 1% after calibration |
| Bias | per-channel regulator, 14-bit DAC, 0–70 V; current limit ≈ 800 µA; output impedance < 150 Ω; noise < 1 mV; from +80 V unregulated |
| Temperature compensation | per channel from the SiPM-board thermistor; common slope 12-bit DAC, 0 to +66 mV/°C |
| Current monitor | 16-bit ADC, 0–410 µA (HCal 0–614 µA); 1–2% absolute uncalibrated |
| Control | I²C, up to 16 FEE per bus, master on the DEP (opto-isolated); cables ≥ 25 m to the digitizers |
| Run 17 exposure (510 GeV) | response loss up to 10% per run, sensor-dependent, from a breakdown-voltage shift |
| Mechanism | S12572-025P: ≈ 100 µA max per sensor after one 500 GeV run ⇒ ≈ 0.6 °C junction heating ⇒ ≈ 10% response loss |
| New HPK sensor S14160-015P | irradiated to ≈ 7×10¹⁰ n/cm²; temperature dependence ≈ 40 mV/C (was ≈ 60 mV/C); degradation ≈ 1% per run; ≈ 300 µA at ≈ 4.25 V over breakdown, ≈ 100 µA at ≈ 2.75 V; $8.9 per SiPM for 10k units |
| Noise impact | HAD resolution at 100 GeV ≈ 8 GeV vs radiation-noise equivalent ≈ 0.4 GeV (4 × 4 HAD cluster) |

Responsibilities: FEE design and production Indiana University; production testing University of Kentucky; final assembly at BNL with the STAR technical support group.

### FCS — 2014 FNAL prototype test (§4.5; the Tsai 2015 prototype)

- 3–32 GeV hadrons, electrons, muons; hodoscope 4.9 mm rods; ≈ 4 cm upstream scintillator; HCal at 2.5°, ECal at 4° to the beam.
- LED/pedestal at ≈ 1 Hz: gains stable to better than 1% per twelve-hour shift; laser matching of MPPCs within 1%.
- HCal MIP corrections ≈ 20%, ≈ 10% from WLS/MPPC alignment (3 mm active area, ≈ 250 µm placement tolerance).
- ECal weighting factor ≈ 2 at 3 GeV, 1.2 at 20 GeV and above; e/h close to 0.95 above 10 GeV.
- Electrons: stochastic ≈ 10%, constant 1.7% (no beam spread) or 11% and ≈ 0 (2012 spread 2.7% below / 2.3% above 4 GeV). Fig. 4-9 legends (read from the figure): hadrons (0.58±0.04)/√E + 0.015±0.015, electrons (0.11±0.007)/√E + 0.007±0.002.
- Hadron resolution ≈ 15% worse than MC at 10 GeV; LHEP physics list. Light yields ≈ 400 pixels/GeV (ECal), ≈ 130 pixels/GeV (HCal).

### FCS — DEP digitizers and trigger (§4.10–4.11)

| Item | Value |
|---|---|
| DEP/ADC board | 32 × 12-bit ADCs at 8× the RHIC clock (13.3 ns ticks); FPGA: pedestal subtraction, zero suppression, charge integration, < 1 ns timing, highest tower, tower sums; optical link to a DAQ PC; STAR TCD interface |
| Crate | up to 5 boards (160 channels) per chassis |
| DEP/IO | variant with serial differential links instead of ADCs; up to 34 links, > 2000 bits; final stage interfaces to the STAR Trigger DSMs |
| Link | 64 bits per bunch crossing (107 ns) per DEP/ADC |
| Board count | 74 DEP/ADC + 3 DEP/IO + spares |
| Layer 1 | per board: 32 contiguous towers → eight non-overlapping 2×2 sums; preshower hit maps |
| Layer 2 | 2 DEP/IO (north, south), each fed by 20 ECal + 8 HCal + 4 Pre-shower DEP/ADC; overlapping 4×4 trigger patches; e/h trigger needs > ½ MIP in two of three preshower layers; photon = no preshower; jet patches ≈ ¼ of the detector |
| Layer 3 | 1 DEP/IO; e⁺e⁻ (Drell–Yan, J/ψ) and di-jet coincidences; result within 1.35 µs |
| Cuts | HCal < ¼ ECal (EM) / HCal > ¼ ECal (hadronic); tighter 1/8 and ½ at low energy |
| Simulated efficiency | photons 99% at low energy → 96% at 80 GeV (threshold 80% of E); π⁻ 74% at 10 GeV (threshold 60%); Fig. 4-19 boxed values 0.83, 0.90, 0.91 at 20, 40, 80 GeV |
| Run 17 prototype | 16-channel DEP + 2 FEE prototypes (4 channels each), 8 SiPMs; shaper pulse 50 ns; timing width 3 ns |
| Old FMS chain (replaced) | QT boards + three-layer DSM tree (128 input bits, 32-bit output), mid-1990s FPGAs |

- **[note]** 2 × (20 + 8 + 4) = 64 trigger-feeding boards of the 74. With the as-built counts of [ruan2026-fcs-specs-email-note](ruan2026-fcs-specs-email-note.md) (24 ECal + 9 HCal DEP per half), 2 × (24 + 9 + 4) = 74 — the proposal total equals as-built calorimeter boards + 8 preshower boards. 748 ECal towers per half / 32 = 23.4 and 260 HCal / 32 = 8.1 boards per half.

### FTS — overview and simulation (Ch. 1, §3.3)

| Item | Value |
|---|---|
| Layout | 3 Si mini-strip disks at z = 139.9, 163.2, 186.5 cm ("140-187 cm"); 4 sTGC wheels at z = 273, 303, 333, 363 cm (30 cm apart) |
| Field | STAR 0.5 T |
| Simulated Si segmentation | 12 sectors × 128 (φ) × 8 (r) per disk |
| Simulated sTGC | four 60 cm square quadrants per station, two faces at 90°, four columns of 15 cm strips per face |
| Tracker | Stv (Kalman filter, follow-your-nose seeds); ≥ 4 hits |
| Efficiency (text) | > 80% to 100 tracks/event, > 50% at 300 tracks/event (vision pass: the figure supports "> 50%" only marginally and only for global tracks) |
| Pions (PYTHIA6, figure annotations) | charge mis-ID 0.86%; relative 1/p_T resolution ≈ 10–14% (read from Fig. 3-24) |
| Density | PHOBOS: most central 600 → 250 tracks over 2.5 < η < 4; 15-25% central 300 (η = 2.5) → 150 (η = 4.0) |

### FTS — silicon (FST) (§5.2)

| Item | Value |
|---|---|
| Sensor | single-sided double-metal silicon mini-strips (Hamamatsu), fine in φ, coarse in r; readout at the outer radius; prototypes due June 2019 / "summer 2019" |
| Model | STAR IST: S/N 25:1, ≈ 99% hit efficiency, 4% dead time at 1 kHz |
| Material | ≤ 1% X₀ per layer |
| Occupancy | 3.2% (η = 4) and 10% (η = 2.5) for 0-3% central Au+Au at 200 GeV |
| Chip | APV25-S1: 128 channels, 4 μs pipeline, 40 MHz sampling; 288 chips for 3 disks (in hand) |
| Wedge | 3 sensors + 8 chips on a flex hybrid; PPS + 10% carbon fibre support; O-shaped cooling pipe; inner and outer sensors on opposite faces |
| DAQ | IST DAQ (built for 864 APV) re-used: 6 readout modules per controller, ≤ 24 APV per module, cables up to 24 m (Fig. 5-6 label "120 feet"), 12-bit at 37.532 MHz, ALICE DDL 2.125 Gbps to a Linux PC → event builders |
| Cooling | ≈ 0.3 W per APV; IST system with 3M NOVEC re-used |
| Radiation | APV IBM 0.25 μm, 20+ Mrad; IST Run 14 bias-current rise 1-2 μA per 0.03×4×7.7 cm³ sensor ⇒ NIEL < 5×10¹⁰ cm⁻²; FST lifetime 1–7×10¹² cm⁻² (≈ 1.2×10¹² outer, 2×10¹² inner sensors) |
| Survey | sensor internal geometry known to better than 10 µm |
| Install | wedges assembled at UIC; 3 disks inside the IDS cone on a rail extension of the West Support Cone (FGT-style); mechanics by Aerospace Industrial Development Corporation |

**Table 5-1** (dose, krad, 12 weeks, RHIC II luminosity): r = 2.5 cm: 5.3-28 (200 GeV Au+Au), 29-133 (500 GeV p+p); r = 14 cm: 0.2-1, 1-4; r = 22 cm: 0.1-0.4, 0.4-2.
- **[note]** 288 / (3 disks × 8 chips) = 12 wedges per disk (our arithmetic; the text does not state the wedge count).

### FTS — sTGC (§5.3)

| Item | Value |
|---|---|
| Wires | 50 μm gold-plated tungsten, 1.8 mm pitch, 1.4 mm from each cathode, 2900 V |
| Cathode | graphite-epoxy, 100 kΩ ("kΩ" as printed), on 100 μm G-10 |
| Strips / pads | strip pitch 3.2 mm (design resolution < 100 µm; prototypes < 50 µm); pads on 1.5 mm PCB, probably unused at STAR |
| Gas | 55% CO₂ + 45% n-pentane |
| Plane | four 60cm x 60cm double-sided sTGCs; two layers with perpendicular strips per disk (x-y) |
| Readout | existing STAR TPC electronics (ALTRO), freed after 2019 by the iTPC project: FEE, RDO, power, fibres, PCs, DAQ software |
| Tests | Shandong: ATLAS module read with TPC electronics, HV 2900 → 2600 V; 30cm×30cm prototype to be installed for Run 2019 |
| Construction | Shandong University (building 40 ATLAS small-wheel modules); 4 disks × 2 layers × 4 modules; ≈ $200K, funded by the STAR Chinese groups |
| Channels | 24000 (3.2 mm pitch, strips cut in 4 × 15 cm, 4 two-layer disks) |
| Mass | ≈ 800 pounds (4 planes × ≈ 200 pounds); mounted on EPD brackets and pole-tip/EEMC threaded holes |

### Simulated physics performance (§3.2)

- Single 30 GeV photons and π⁻ at η = 3: ECal–HCal response linear but non-compensating (fit slopes −1.242 photons, −1.179 pions, read from Fig. 3-3).
- Jets: fast simulation 0.58/√E (hadrons), 0.11/√E (EM); anti-k_T R = 0.7; x₁ up to ≈ 0.6, x₂ down to 7×10⁻³; full simulation anti-k_t R = 0.6, E_T > 50 MeV, jet p_T > 3 GeV; detector p_T ≈ 5% below particle level.
- Collins: ≈ 2% asymmetries for 2.8 < η < 3.7, jet p_T > 3 GeV/c, 1 fb⁻¹, 60% polarization; toy model: FCS geometry strongly dilutes the Collins asymmetry for vertical polarization, radial polarization helps.
- Drell–Yan: hadron rejection 200–2000 for 15–50 GeV at 80% electron efficiency (BDT, 1000 trees, depth 4; Eratio, Swidth, NTratio, E/p); 4 billion PYTHIA events, 2.5 pb⁻¹ p+Au ≡ 500 pb⁻¹ p+p ≡ 240.5 billion events; conversion background not modelled.

## Methods

GEANT-based STAR simulation with a detailed FCS model (single particles 3–100 GeV, PYTHIA jets); fast simulation for jet kinematics, Collins/IFF and Drell–Yan; Stv Kalman tracking for the FTS with single-particle guns and PYTHIA6; 2014 FNAL beam test (prototype of a different, earlier design); SiPM irradiation in RHIC Runs 13, 17, 18 and bench heating/cooling measurements; DEP/FEE prototypes in Run 17 at the STAR IP.

## What it does not give

- No ECal tower length, depth in X₀ or λ, Molière radius or layer stack — the ECal is described only as re-used PHENIX towers (ref. [129], Aphecetche et al., NIM A499 (2003) 521).
- No FCS z position or η of tower edges; no HCal tower length in cm (only 38 layers and the Fig. 4-10 drawing).
- No total project cost or schedule beyond the PAC's $5.3 M, the sTGC ≈ $200K and the SiPM unit price; no cost table.
- No measured performance of the proposed (PHENIX + Fe) FCS; test-beam numbers are for the 2014 prototype.
- FTS material per sTGC layer, wedge count per disk and the final sensor geometry are not stated.

## Source issues and caveats

- **[source issue]** EM resolution printed "~8%√ (E)" in Ch. 1 (division sign missing); §4.1 gives ~8%/√E, while §4.2 and Table 3-1 give ~10%/√E.
- **[source issue]** Broken cross-references "Section 0", "section 0" (Ch. 1, §2.4, §3.2.3).
- **[source issue]** §3.2.1 points to Fig. 3-6 for the x₁–x₂ coverage; Fig. 3-4 is meant. §4.5 figure references run one number low (text Figs. 4-5…4-8 = Figs. 4-6…4-9).
- **[source issue]** "FSC" for FCS (§4.1); "FANL" for FNAL (§4.4); "Newton's low", "funder" (§4.9); "ALTAS" (§5.3.2); "hin" for "thin" (§5.2.3).
- **[source issue]** 500 GeV run luminosities inconsistent between §2.3 (8 weeks, 1.1 fb⁻¹; transverse 1 fb⁻¹) and Table 2-1 (1.1 fb⁻¹, 10 weeks).
- **[source issue]** Fig. 3-22 caption calls the red histogram "fake global tracks" though it is the correctly peaked distribution; Fig. 3-21 plot says ntracks = 310 vs 300 in the text.
- **[source issue]** FST DAQ cable "up to 24 m" in the text vs "120 feet" in Fig. 5-6. Fig. 5-8 caption 1.1 fb⁻¹ at 500 GeV vs panel label 1 fb⁻¹ at 510 GeV; panel Z = 140.0 vs 139.9 cm in the text.
- **[source issue]** "FTS"/"FST" used interchangeably for the silicon disks; "Microstrip" vs "Ministrip" (§5.2.8).
- **[source issue]** Installation weight "between 15 kg" — second bound missing (§5.4).
- **[source issue]** Swidth defined with the symbol R_p; refs. [137]/[138] duplicate [4]/[5] and [139]/[140]; several other duplicate bibliography entries.
- Internal coverage values differ: 2.5 < η < 4 (most places), 2.5-4.5 (Ch. 1, Fig. 3-20 cuts), up to 4.2 (PAC text, A+A tables).
- Fast-simulation resolutions (0.58/√E, 0.11/√E) are the 2014-prototype values, not the Table 3-1 targets.
- Tracking efficiency claim "> 50% at 300 tracks/event" is only marginally supported by Fig. 3-23 (global tracks ≈ 0.5, primary ≈ 0.2–0.3; from the vision pass).
- Ch. 2 is summarised in the Layer-3 file (user-approved scope); its figures were not vision-checked.

## Comparison with the as-built detector (from the other notes) [note]

| Item | 2018 proposal | As built / later | Source of the later value |
|---|---|---|---|
| ECal / HCal towers | 1496 / 520 | 1496 / 520 | [wang2024-star-forward-upgrade-note](wang2024-star-forward-upgrade-note.md), [ruan2026-fcs-specs-email-note](ruan2026-fcs-specs-email-note.md) |
| Sampling fractions | 0.20 / 0.0145 (simulation) | 0.20 / 0.0145 | [ruan2026-fcs-specs-email-note](ruan2026-fcs-specs-email-note.md) |
| HCal layers | 38 Fe/Sc, 20 mm + 3.1 mm gap, ≈ 4.5 λ | 36 × (20 mm + 3 mm), pitch 23.4 mm, + 10 mm back plate, 4.45 λ | [ruan2026-fcs-specs-email-note](ruan2026-fcs-specs-email-note.md) |
| ECal readout end | front face (so that no dead space opens between ECal and HCal) | "on the front face" (Wang 2024); fibres read "at the back" (email) | [wang2024-star-forward-upgrade-note](wang2024-star-forward-upgrade-note.md), [ruan2026-fcs-specs-email-note](ruan2026-fcs-specs-email-note.md) |
| ECal tower length / λ | not given | 33 cm, 0.85 λ_I (talk) vs 37.73 cm, 0.93 λ (email) | [gagliardi2022-star-forward-upgrade-talk-note](gagliardi2022-star-forward-upgrade-talk-note.md) |
| DEP boards | 74 DEP/ADC + 3 DEP/IO | 24 ECal + 9 HCal per half | [ruan2026-fcs-specs-email-note](ruan2026-fcs-specs-email-note.md) |
| FST disks | z = 139.9 / 163.2 / 186.5 cm; ≤ 1% X₀ per layer | z = 152 cm to 179 cm; 12 modules per disk, 3 sensors each; ~1.5% X₀ per disk | [wang2024-star-forward-upgrade-note](wang2024-star-forward-upgrade-note.md), [gagliardi2022-star-forward-upgrade-talk-note](gagliardi2022-star-forward-upgrade-talk-note.md) |
| sTGC | 4 wheels at z = 273–363 cm; four square 60 × 60 cm modules per plane; x-y strips; STAR TPC (ALTRO) readout | 4 planes × 4 pentagonal modules at z = 300 cm to 360 cm; X, Y and diagonal layers; VMM readout | same |
| sTGC gas / HV | 55% CO₂ + 45% n-pentane; 2900 V | same gas; 2900 V | [wang2024-star-forward-upgrade-note](wang2024-star-forward-upgrade-note.md) |

## Relevance

Design-stage reference for the STAR forward upgrade: the only ingested source with the FCS front-end, bias and DEP/trigger architecture in detail ([star-fcs](../wiki/synthesis/star-fcs.md), [star-daq-trigger](../wiki/synthesis/star-daq-trigger.md)), the SiPM radiation study, and the FTS silicon and sTGC design numbers ([star-forward-tracking](../wiki/synthesis/star-forward-tracking.md)). It states the design intent that the ECal readout sits on the front face, but gives no ECal tower length or depth ([open-questions](../wiki/synthesis/open-questions.md) #15). Several design choices changed before construction (sTGC module shape and readout electronics, FST z positions, HCal layer count).

## Related

- Synthesis: [star-fcs](../wiki/synthesis/star-fcs.md) · [star-forward-tracking](../wiki/synthesis/star-forward-tracking.md) · [star-daq-trigger](../wiki/synthesis/star-daq-trigger.md) · [open-questions](../wiki/synthesis/open-questions.md) · [rhic-detector-status](../wiki/synthesis/rhic-detector-status.md)
- Notes: [tsai2015-fcs-prototype-note](tsai2015-fcs-prototype-note.md) (2014 prototype, earlier design) · [gagliardi2022-star-forward-upgrade-talk-note](gagliardi2022-star-forward-upgrade-talk-note.md) (as built, Run 22) · [wang2024-star-forward-upgrade-note](wang2024-star-forward-upgrade-note.md) (as built, QM2023) · [ruan2026-fcs-specs-email-note](ruan2026-fcs-specs-email-note.md) (construction specs) · [star2026-detector-status-note](star2026-detector-status-note.md) (October 2026 status)
