---
title: "Kajimoto 2009 — A Large Area Time of Flight Detector for the STAR Experiment at RHIC (PhD thesis, curated notes)"
type: raw-note
source_type: thesis
companion: kajimoto2009-star-tof-thesis.md
authors: "Kohei Kajimoto (The University of Texas at Austin); supervisor Gerald Hoffmann"
journal: "PhD dissertation, The University of Texas at Austin, December 2009, 184 + xvi pp."
doi: none
url: "https://repositories.lib.utexas.edu/bitstreams/c344eec2-720a-4e8a-9a0b-06bfe42b7a74/download"
arxiv: none
notes_updated: 2026-11-16
ingested_version: "Texas ScholarWorks open-access PDF (197 pages), read 2026-11-16 via Route 3 (PDF only; no HTML or arXiv version); user-approved reduced scope: Ch. 3–7 in full, Ch. 1–2 summarised except §2.2.4 (CTB), §2.2.7 (pVPD) and §2.2.10 (Trigger), appendices by caption, acronyms and bibliography in full"
earlier_version: []
later_version: []
published_version: "PhD dissertation, The University of Texas at Austin, December 2009 -- this is the ingested version"
version_facts: "Single version: the dissertation PDF deposited in Texas ScholarWorks (UT Austin repository). No journal or arXiv version. Status statements are as of August 2009 (after RHIC Run 9, before Run 10). Figs. 3.3–3.5 (mass resolution, MRPC cross-section, pad board) are reproduced from the 2004 STAR TOF proposal (Fachini et al., thesis ref. [8]), which is not in this wiki. The author is a co-author of schambach2006-star-tof-electronics (ingested)."
versions_checked: 2026-11-16
---

# Kajimoto 2009 — Curated Notes

> **Full source:** [kajimoto2009-star-tof-thesis](kajimoto2009-star-tof-thesis.md) · Companion notes to [kajimoto2009-star-tof-thesis](kajimoto2009-star-tof-thesis.md) (full source; a full-content paraphrase).
> **URL (open access PDF, Texas ScholarWorks):** https://repositories.lib.utexas.edu/bitstreams/c344eec2-720a-4e8a-9a0b-06bfe42b7a74/download · DOI: none · arXiv: none

## Bibliographic

- **Title:** A Large Area Time of Flight Detector for the STAR Experiment at RHIC
- **Author:** Kohei Kajimoto (B.S., M.S.), The University of Texas at Austin. Supervisor: Gerald Hoffmann. Committee: G. Hoffmann, E. Komatsu, C. Markert, R. Ray, P. Riley.
- **Type:** PhD dissertation, The University of Texas at Austin, December 2009; 197 PDF pages (printed page = PDF page − 13).
- **Slug:** thesis rule `<author><year>-<topic>-thesis`.

## What kind of source

A hardware thesis from the UT Austin group that assembled and tested every production tray of the STAR barrel TOF. Chapters 1–2 are physics motivation and a STAR overview (summarised in Layer 3); the substance is Ch. 3 (TOF design and the full electronics chain with its board history), Ch. 4 (MRPC module QA and three generations of cosmic-ray test stands, with the analysis methods), Ch. 5 (tray assembly and tray-level QA statistics for all 126 trays), Ch. 6 (shipments, installation and Run 8 / Run 9 status, day-by-day Run-9 log, dead channels, threshold scan) and Ch. 7 (summary). No calibrated in-STAR timing resolution: Run-9 calibration was still in progress.

## Abstract (paraphrased)

The thesis presents the time-of-flight system built for STAR at RHIC from multi-gap resistive plate chambers. The new detector sits where the Central Trigger Barrel used to be and consists of 120 trays; each tray carries 32 MRPC modules with 6 readout pads apiece. Adding it roughly doubles the transverse-momentum range over which STAR can identify particles, which opens up a wider physics programme.

## Key numbers

All values from the Layer 3 full source; section, table or figure in brackets. **[note]** = our derivation.

**System and tray (§3, §3.1)**

| Item | Value |
|---|---|
| Coverage | full 2π in φ, \|η\| ≤ 1.0 (Ch. 3); each tray 6° in φ and one unit of η (−1 < η < 0 or 0 < η < 1) |
| Trays | 120, a cylindrical shell around the TPC; shape almost identical to a CTB tray |
| Tray box | **95" (241.3 cm) long × 8.5" (21.6 cm) wide × 3.5" (8.9 cm) high**; gas-tight, flowing R134a (freon) |
| Per tray | 32 MRPCs inside, 17 electronics boards outside, 192 channels; **[note]** 17 = 8 TINO + 8 TDIG + 1 TCPU |
| System | 23,040 channels |
| Construction | started November 2006, finished May 2009; prototype trays tested at the AGS and at RHIC from 2001 |
| Start side | two pVPD assemblies, 19 PMTs each coupled to scintillator, z ~ ±5 m (§3.1); §2.2.7: on the beam-pipe I-beam 5.6 m from the IP, 10 PMTs inner ring + 9 outer; this "upVPD" since before Run-6; Runs 2–5 had 3 PMTs per side in one ring |
| PID design (Fig. 3.3, from [8]) | inputs δp/p = 1.3%, δs/s = 0.2%, δt = 100 ps; path lengths ≈ 220 cm (η ≈ 0) and ≈ 320 cm (η ≈ 1); read off the figure: π/K to ≈ 1.7–2.0 GeV/c, K/p to ≈ 3.1–3.2 GeV/c |

**MRPC module (§3.2, Fig. 3.4 reproduced from the 2004 proposal [8], §4.1–4.2)**

| Item | Value |
|---|---|
| Stack | 2 honeycomb boards, 2 graphite electrodes, 2 outer glass plates, **5 inner glass plates** (spaced by fishing line), 2 PCBs with 6 copper pads each; avalanche mode. **[note]** 7 glass plates ⇒ **6 gas gaps**; Fig. 3.4 draws 6 |
| Gas gap | 220 µm |
| Glass | **outer 1.1 mm, inner 0.54 mm** |
| Pads | 6 per board, **pad width 3.15 cm, pad interval 0.3 cm**. **[note]** pitch 3.45 cm; 6 × 3.15 + 5 × 0.3 = 20.4 cm. Eq. (4.2) uses a pad area 6.1 × 3.1 (printed in mm, see caveats) |
| Long-edge lengths | honeycomb 20.8 cm, electrode 20.2 cm, inner glass 20.0 cm, outer glass 20.6 cm, PC board 21.0 cm |
| Thicknesses | honeycomb 4 mm, Mylar 0.35 mm (not drawn), PC board 1.5 mm |
| Short-edge layout (Fig. 3.4 axis, cm) | PC board 0–9.4; honeycomb 0.5–8.9; outer glass 0.8–8.6; electrode 1.0–8.4; pad 1.1–7.4; inner glass 1.3–7.4. **[note]** pad extent 6.3 cm and inner-glass width 6.1 cm across the module (figure-read) |
| Pad orientation (§5.3.2) | the 6 pads of each module are aligned **perpendicular to the tray's long side**, i.e. the pad row runs across the tray. **[note]** so the 3.15 cm pad width lies along φ and the ≈ 6.1 cm side along z |
| Module spec (Table 4.1) | length 212.0 (211.5–212.5) mm, width 94.0 (93.5–94.5) mm, thickness 17.9 (16.9–18.9) mm |
| Measured (Table 4.2; TM001-090, UM001-040, summer 2006) | length 211.94 mm (σ 0.101), width 94.04 mm (σ 0.062), thickness 18.21 mm (σ 0.141); later batches checked with sizing jigs |
| Signal cabling (§4.2) | each pad pair wired redundantly to two twisted-pair cables; 12 twisted pairs end in a 34-pin connector (10 pins unused) |
| Producers (Ch. 4, §5.1) | Tsinghua University (TM serials) and USTC (UM serials) |

**Module QA (§4.2–4.3)**

| Test | Numbers |
|---|---|
| Cable connection tester | PIC16F913 microcontroller + four MAX306 16-channel multiplexers; green/red LED; built December 2006 – January 2007 |
| HV test | aluminium box for 6 MRPCs, pumped then filled with R134a, ~5 min to HV ramp; **682 modules** tested July 16 – October 11, 2007; **3 failed** to hold HV (TM0101, TM0107, TM0151); dropped once the "submarine" stand ran |

**Electronics boards and their history (§3.3)**

Renamings: TFEE → TAMP → TINO (MRPC front end); TFEEb → TPMT → TPMD (start side); TMIT → THUB.

| Board | Content |
|---|---|
| TFEE | original MRPC amplifier + discriminator: MAXIM 3760 preamp, AD96685 comparator; designed for 24 channels (4 MRPCs), built as a 6-channel board for the prototype tray TOFr, with analog and NIM outputs; used in the first cosmic stand |
| TFEEb | TFEE variant taking PMT input, for the start side |
| TAMP | TFEE redesign, amplifier only; one card per four 6-channel MRPCs; 960 cards; Maxim 3664 preamp; the Maxim 9601 comparator moved to the TDIG |
| TINO | final front end, custom NINO ASIC (CERN, built for ALICE TOF); chosen February 2006 after UT cosmic tests; delays the trailing-edge signal so the TDIG takes both edges on one channel; 3 × 8-channel NINO per board (Fig. 3.10) |
| TDIG | 24 channels (4 MRPCs); 8 TDIG/TINO pairs per tray; inputs: discriminator signals, clock, multiplicity gate, L0 readout commands; outputs: edge times and 5-bit partial multiplicity sums; 3–4 HPTDCs. Early: LE by 3 HPTDCs in 8-channel "very hi res mode" (25 ps bins), TE by 1 HPTDC in 32-channel "hi res mode" (100 ps bins); production: both edges of all 24 channels by 3 HPTDCs in "very hi res mode". 16 HPTDCs share one 80 Mbit/sec serial port ⇒ 2 data cables per tray (4 TDIG, 96 pads each). Production board "TDIG-F", 2007, Altera Cyclone II (Fig. 3.13) |
| TPMT / TPMD | start side: PMT signal → fixed-threshold discriminator → TDIG; TPMT diagram: 24 PMT inputs, half a MAX9601 per channel, threshold from the TDIG (Fig. 3.14) |
| TCPU | 120 on the trays + 2 start side (East, West); two bus cables, each daisy-chaining up to 4 TDIGs; CAN-bus node and gateway to the TDIGs; functions: multiplicity sum to L0, readout of the tray's 32 HPTDCs and SerDes link to THUB, configuration over CAN (mode, thresholds, HPTDC settings; can be stored in TDIG EEPROMs), trigger commands (e.g. Abort, L2 Accept) |
| THUB | 4, named by position on the magnet ends: NW, NE, SW, SE; up to 16 SERDES daughter cards × 2 ports = 32 links; CAT-6 link to each TCPU carries trigger, 40 MHz clock and serialized data; ALICE DDL SIU daughter card (spelled "SUI" in the thesis) for the fibre to STAR DAQ; Fig. 3.18 draws 31 TCPU interfaces |
| TOF DAQ receiver | Linux PC with one Myrinet interface, 4 fibre-optic interfaces and RORC cards (built on the DDL DIU); needs a PCI-X bus |
| TOF controller | Linux PC with 6 CAN-bus interfaces (PCAN-USB, PEAK-System); root of slow control |

**Networks (§3.3.11, Fig. 3.22)**

| Network | Path |
|---|---|
| Data | MRPC → TINO over twisted pairs (34-pin pigtail); TDIG ↔ TCPU 50-pin ribbon; TCPU → THUB CAT-6; THUB → STAR DAQ by DDL fibre |
| CAN-bus | 6 networks from the TOF controller: 2 for the start-side TCPUs, the others THUB ↔ tray TCPUs (Fig. 3.22 draws 4 THUB lines); inside a tray two daisy-chains on the 50-pin ribbons |
| Trigger | STAR Level-2 ↔ every THUB over DDL links of four dual optic fibres; TCD clock and commands in, Busy out (Figs. 3.7, 3.18) |
| Clock | single-rooted tree, 40 MHz: master THUB (THUB-NW in Run 9) → slave THUBs over RG-58 coax → TCPUs over shielded CAT-5 → TDIGs over 50-pin ribbon |
| Multiplicity | NINO → (data path) → TCPU → copper ribbon cable → DSM of STAR Level-0 |

**Cosmic-ray test stands and results (§4.4)**

| Stand | Set-up | Results |
|---|---|---|
| "Small" box (built summer 2003, used through 2004) | 3 MRPCs ~1" apart in a gas box; stand 39"h × 48"w × 24"d; scintillators S1, S3 3″ × 3″ × 6″, S2 6″ × 6″ × 1/4″, EMI9813B PMTs; S1–S3 23.2″ apart, Ω = 3.3 × 10⁻² sr; LeCroy 623 discriminators, 821 coincidence, 2248A ADC, 2228A TDC, KS 2915 controller; R134a at 20 sccm; only pads 2 and 4 read (6-channel TFEE) | Sept 4–11, 2003: 578,116 s, 23,324 events, 4.034 × 10⁻² event/s; middle-pad efficiency 86.9% (pad 4, 2316/2665) and 90.6% (pad 2, 1939/2140); after slewing correction pad 4: 2.1 bins (105 ps) for the three-pad combination, 1.7 bins (86 ps) per pad; pad 2: 2.2 bins (110 ps), 1.8 bins (90 ps) per pad; "90 ps or better" with prototype electronics |
| "Big" box (from spring 2004; first data late July 2004) | larger gas box and scintillators; April 2005: TAMP, TDIG, TCPU replace TFEE + CAMAC; then a 9-channel TINO prototype (3 × 3 pads); CAN-bus readout to a Linux PC via the `pcanloop` daemon (J. Schambach); results in a MySQL database | about 197 modules, more than 6000 hours, until the final stand was finished in October 2007 |
| "Submarine" | pumpable Al box with 32 MRPCs in 8 Lexan stacks of 4; trigger = coincidence of two CTB trays above and below (Table 4.4); TINO/TDIG/TCPU from the top of a production tray; 34-pin vacuum feedthroughs; trigger delayed 5 µs; 24-bit packets over CAN | Run 10000352 (Aug 9–14, 2007): 406431 s, 250506 events, 0.616 event/s, 3443 tracks; module TM0320 per-pad resolution 83.9 / 65.1 / 70.9 / 75.5 / 66.3 / 94.2 ps, all pads 74.4 ps (Table 4.7); outer pads see fewer tracks |

- Expected cosmic rate per pad (Eqs. 4.1–4.2): I ≈ 70 m⁻² s⁻¹ sr⁻¹ for E_μ > 1 GeV/c; f ≈ 8.31 × 10⁻³ Hz per pad (about one hit every two minutes) as printed; see caveats.
- **[note]** The Table 4.7 widths are dt against the mean of the other pads in the stack (Eq. 4.6), not unfolded; Layer 3 notes that 70.9 ps for 4 equal pads would be ≈ 61 ps per pad.

**MRPC noise tests (§4.4.5)**

| Item | Value |
|---|---|
| Method | internal HPTDC trigger, HPTDC read-in window 50 µs; r = c/(50 µs · c_trig) = 2 · 10⁴ (c/c_trig) Hz (Eq. 4.4) |
| Typical | 1000 s per measurement, about 10 Hz; at UT typically 20–30 min per test |
| Conditioning | ~100 Hz right after HV ramp-up (purging, dust), relaxing to ~10 Hz after 24 h with HV on and freon at ~50 sccm |
| Statistics | t_wall ≫ 1/(r · 50 · 10⁻⁶ r_trig) = 20 s for r_trig = 100 Hz, r = 10 Hz (Eq. 4.5; Table 4.5) |

**Tray assembly and tray QA (§5)**

| Item | Value |
|---|---|
| Suppliers | MRPCs: Tsinghua, USTC; Al tray box sets (bottom, top, cover, feet): Oaks Precision Fabricating, Houston (126 sets, Fig. 5.1); TINO: designed at Rice, tested at Rice; TCPU, TDIG: Blue Sky Electronics, Houston, TDIG INL tables made at Rice (tied to each HPTDC); cooling loops, Lexan holders, shims, strain reliefs: UT shop |
| Assembly | 10 steps with a sign-off checklist and a UT tray database; DC430 sealant cured ~1 week; cooling loop clamped between TINO and TDIG at 4.5 inch-pounds |
| Cooling-loop leak test | 1/4" × 3/8" copper loop, brass barbed fittings at the high-η end; N₂ at 200 psi under water, no bubbles for 2 hours |
| Gas leak test | pressure (Magnehelic) stable for at least one day after barometric correction; freon sniffer at maximum sensitivity must not alarm |
| RF test | air-core transformer on the HV bus (TOFr and first production batch); abandoned |
| Manual noise test | first 6 trays (A–C, 1–3) with NIM scalers via a TINO read-out adapter; Tray A, December 1, 2006: 13–65 (figure, units not printed); missing TDIG-F extender ⇒ 8 dead channels in a row |
| Computerized noise test | via THUB and fibre, or via TDIG debug over CAN (trigger ≤ 180 Hz); r_noise = n_count/(n_event · Δt) (Eq. 5.1); Δt = 25 µs for tray tests, 5 µs for physics |
| Noise summary | 126 trays = 24192 channels; threshold 2500 mV; spec 50 Hz; Fig. 5.13 stat box: 24186 entries, mean 7.37 Hz, RMS 6.684; **101 channels > 50 Hz = 0.417 %** in 10 trays (SN 1, 3, 4, 7, 10, 26, 61, 94, 112, 114; Table 5.1); peripheral pads noisier; module 13 of tray SN 3 noisy (UT-Run 10000376) |
| Assembly errors found | Tray 8: module 1 HV reversed, two signal-cable pairs swapped on module 3; Tray 22: module 28 HV reversed |
| Tray cosmic test | 2 stands; first: 3 TOF trays + 3 CTB scintillator trays, 3-fold coincidence; 120 of 126 trays measured (A and 1–5 untested); 250–350 ps per channel without slewing correction (text; Fig. 5.17 shows ≈ 170–310); Fig. 5.18: 23034 entries, mean 238.6 ps; first 12 trays unreliable (short runs); runs of 1–2 weeks better |
| Final test at WAH (BNL) | noise rates and HV currents on a stand holding 30 trays |
| Threshold scan, Tray 114 (UT, Jan 21–22, 2009) | 2500 mV down in 100 mV steps, 26 one-hour runs; exponential rise down to roughly 300 mV (figure: ≈ 12 Hz at 2300 mV to ≈ 67 Hz at 400 mV, ≈ 1000 Hz at 300 mV) |

**Production, shipments and installation (Ch. 6)**

| Item | Value |
|---|---|
| Production (August 7, 2009) | 126 trays assembled (120 + 6 spares, §7.1); 122 with production electronics; A–C and 121–123 on a prototype aluminium body |
| Shipments (Table 6.1) | 125 trays to BNL in 5 shipments, Oct 5, 2007 – Jul 9, 2009 (6, 30, 32, 27, 31 trays); Tray 6 returned and re-sent in shipment 3 |
| Run 8 | 5 trays (4.2 %) at CTB/TOF positions 76–80; 960 channels, 2 dead (Table 6.2: position 77, SN 2, channel 130 = module 22 pad 4; position 79, SN 4, channel 168 = module 28 pad 6) |
| Between runs | all trays removed after Run 8; new TDIGs on trays 1 and 2; TDIG 4 of tray 49 SN328 → SN254 |
| Run 9 | 94 trays (78 %) at positions 1–12, 15–41, 44–72, 75–78, 97–101, 104–120; 86 active (71.7 %); empty positions 13, 14, 42, 43, 73, 74, 102, 103 blocked by TPC support structures (fixture in development); p+p at 250 GeV and 100 GeV, January 16 – July 4, 2009 |
| Run-9 problem trays (§6.2, Tables 6.4–6.5) | positions 38, 39 no LV connection; 52 HV cables not mated; 75 bad TCPU; 47, 68, 112, 118 low rates (112 and 118 missing the positive HV connection); 46 high rates; HV distribution box 5 (positions 49–60) |
| Dead channels, run 10087063 (Table 6.6) | position 4 (SN 6): 6 channels, 43 (8, 1), 71 (12, 5), 72 (12, 6), 80 (14, 2), 106 (18, 4), 108 (18, 6); position 10 (SN 60): 49 (9, 1); position 60 (SN 55): 124 (21, 4); position 76 (SN 4): 168 (28, 6). Total printed "9 out of 16152", "0.55%"; §7.1 says 10 of 16,512 |
| Live channels | requirement > 175 per tray, met by every installed tray; averages printed 195.60 (Run 8) and 195.88 (Run 9), see caveats |
| Day-50 threshold scan in STAR (Feb 19, 2009; Table 6.7) | 500–2500 mV, 14 runs of 1M events; most trays well behaved (Tray 1 ≈ 5.6 Hz at 2500 mV to ≈ 22 Hz at 500 mV, figure); some diverge at 500–600 mV (Tray 78 ≈ 2470 Hz at 500 mV); values above 100 Hz signal a too-low threshold; group decided to test 1200 mV in beam |
| Run-9 operations | trigger match window 25 µs at start; from Day 76 (March 17, 2009) 5000 ns (200 coarse counts) with 5200 ns (208) trigger offset; new TCPU firmware Days 96–98 against an HPTDC fault when a trigger arrives near a clock edge; THUB SW firmware fault Days 69–71 |
| After Run 9 | trays 77, 117, 120 back to UT for repair; 4, 58, 64 re-fitted with new boards; 75 awaits a new TCPU; all 120 trays scheduled for Run 10 |

**Replaced and neighbouring systems (§2.2.4, §2.2.7, §2.2.10)**

- **CTB:** −1 ≤ η ≤ 1, 2π; 240 plastic scintillators with PMTs in 120 trays (one unit of η × 6° each), charged-multiplicity measurement; production CTB trays aluminium, no cooling loop (prototype drawing Fig. 2.12 shows 2 slabs + 2 PMTs per tray). The TOF trays take the CTB positions.
- **pVPD:** see the system table above.
- **Trigger:** levels L0–L2 on VME, NIM and Linux CPUs, a decision for every bunch crossing; inputs from ZDC, BBC, pVPD, CTB, EEMC, BEMC and FPD as digital signals to the DSM boards.

## Methods

- Thesis-length description of design, construction and QA; numbers come from the UT test database and STAR run logs ([NH-…] references in the Run-9 log).
- Module timing analysis (§4.4.6): CTB-triggered cosmic events; vertical pad coincidence (2–4 pads); **MaxTOT** (keep only the largest-ToT pad per module, require vertical alignment) and a cap N_hit^max on fired pads; ToT = trailing − leading edge.
- **Slewing correction** (Eqs. 4.6–4.10): dt_ij = t_ij minus the mean of the other pads in the vertical stack; correct one pad at a time against its own ToT with a polynomial or a0 + a1 exp(−a2 x) fit, iterating down the stack; one round only (further rounds did not help); fit window 1.5σ inside a 2σ ToT cut (Fig. 4.18). Later STAR productions used splines (TSplineFit).
- **Correlation method** (Eq. 4.11): Pearson correlation of binary pad-fired variables, used to map cross-talk (Fig. 4.19: ridges along vertically aligned pads; more neighbour cross-talk in one module).
- Tray tests: noise (manual scaler, then HPTDC packet counting), cosmic stands with CTB triggers, final noise/HV check at BNL; dead channels found from per-tray hit patterns in beam runs (Figs. 6.2–6.4).
- Software (App. 2): Anaconda (CAN-bus tray-test GUI used at WAH, built on `pcanloop`) and Anaconda II (C++/Qt GUI for the full TOF electronics, SQLite configuration), started October 2008.

## What the thesis does not give

- MRPC operating HV, gas mixture beyond "R134a (freon)", glass and electrode resistivities, avalanche charge.
- MRPC tilt angles in the tray, the barrel radius, pad length printed as a number in cm (only the mm-labelled Eq. 4.2 and the Fig. 3.4 axis).
- Calibrated timing resolution of the installed system or start-time resolution (Run-9 calibration in progress); efficiency in beam.
- Anything about the MTD; the pVPD electronics beyond the TPMT/TPMD boards.

## Source issues and caveats

- **Eq. (3.3)** puts γ² on the momentum term; differentiating Eq. (3.2) puts it on the timing and path-length terms, as the formula inside Fig. 3.3 does. Fig. 3.3 caption says the two lines are the "two edges of TOF tray"; the legend shows two path lengths.
- **Pad area in Eq. (4.2)** printed as 6.1 mm × 3.1 mm = 1.89 · 10⁻⁵ m²; centimetres are meant, so the rate would be ≈ 100 × larger (Layer 3 [note] ≈ 0.83 Hz); the 2π × vertical-intensity estimate also ignores the cos²θ fall-off.
- **Gas-gap count:** the stack (5 inner + 2 outer plates) and Fig. 3.4 give 6 gaps; [llope2012-star-mrpc-systems-note](llope2012-star-mrpc-systems-note.md) prints "five gaps of 220 μm". Not resolved by either source ([open-questions](../wiki/synthesis/open-questions.md)).
- **HPTDCs per TDIG:** production design and the TDIG-F photo show 3; "16 HPTDCs per serial port" and "32 HPTDCs in the tray" imply 4 (the early 3 + 1 layout). [schambach2006-star-tof-electronics-note](schambach2006-star-tof-electronics-note.md) has 12 HPTDCs of 4 TDIGs per port (3 per board).
- **TCPU–THUB cable:** CAT-6 (data network, §3.3.8.1) vs shielded CAT-5 (clock network).
- **TFEE vs TAMP preamp:** MAXIM 3760 (TFEE) vs Maxim 3664 "still" on the TAMP.
- "SUI" printed for the ALICE DDL SIU; "HPDTC" in Fig. 3.10; "Auxilliarary" in Fig. 3.12.
- **pVPD distance:** ~5 m (§3.1) vs 5.6 m (§2.2.7); [ruan2009-mtd-concept-note](ruan2009-mtd-concept-note.md) says 5.4 m.
- Text cross-references swapped (Figs. 4.3/4.4) or broken ("Figure 4.4.2.1", "Table 4.4.5"); Table 4.5 cell 50 Hz × 50 Hz printed 20 sec, Eq. (4.5) gives 8 s.
- Sept 2003 run: 578,116 s printed as "∼188 hours" (160.6 h).
- PIC16F913 called "16 bit" (an 8-bit device).
- Run numbers with wrong digit counts: UT-Run "100000376" (Fig. 5.11 caption; 10000376 in the text), "1001303" (Fig. 5.17 caption; 10001303 in the text), "100001382"; STAR runs "1008033", "100036044", 1005058–1005071 (Table 6.7).
- Day-76 match window printed "250025 ns" for 1001 coarse counts; 25025 ns is meant. Day 60 gives 4 dead channels on position 4, all other entries 6. Day 195: tray-68/69 cable swap direction ambiguous.
- **Table 6.1** shipment 4 lists only 22 serial numbers for "27"; SN 73–77 appear in no shipment ([note]: adding them gives 27). Driver "G. Epply" vs "G. Eppley".
- **Dead-channel totals:** "9 out of 16152" (86 × 192 = 16512) and "0.55%" (9/16512 ≈ 0.055 %); §7.1 says 10 of 16,512. Live-channel averages "195.60" and "195.88" exceed 192 per tray; (960 − 2)/5 = 191.60 and (16512 − 10)/86 ≈ 191.88 are presumably meant (Layer 3 [note]).
- Tray cosmic text quotes 250–350 ps; Fig. 5.17 shows ≈ 170–310 ps.
- Figure-read values (Fig. 3.3 crossings, Fig. 5.21 and Figs. 6.5–6.6 readings, Fig. 3.4 short-edge pad extent) are approximate.
- Ch. 2 is summarised in Layer 3 (except §2.2.4, §2.2.7, §2.2.10); Ch. 2 figure-label issues (Figs. 2.2/2.3 swapped; "CBT/TOF"; FMS cell counts 14400 vs 1440 and 37² − 20² ≠ 756) are recorded there.

## Relevance

The most detailed ingested description of the STAR barrel TOF as built: tray box dimensions, MRPC module outer size and QA tolerances, the pad layout (3.15 cm pads at 0.3 cm spacing, row across the tray), glass thicknesses, the full board history and network topology, and production statistics for all 126 trays (noise mean ≈ 7 Hz per channel at 2500 mV, 0.417 % above 50 Hz, ≈ 239 ps tray-cosmic width without slewing correction). It fixes the pad orientation that the wiki had only inferred and settles the glass thicknesses in favour of Llope 2012. Its Run-8/Run-9 records (positions, dead channels, failure modes such as unmated HV and missing LV) document the hardware history of the trays that remain in STAR.

## Related

- Synthesis: [star-barrel-tof](../wiki/synthesis/star-barrel-tof.md) · [star-daq-trigger](../wiki/synthesis/star-daq-trigger.md) · [mrpc-technology](../wiki/synthesis/mrpc-technology.md) · [rhic-detector-status](../wiki/synthesis/rhic-detector-status.md) · [open-questions](../wiki/synthesis/open-questions.md)
- Notes: [schambach2006-star-tof-electronics-note](schambach2006-star-tof-electronics-note.md) (2006 electronics design paper, author is a co-author; pad 3.3 cm and glass 0.7/0.55 mm there) · [llope2012-star-mrpc-systems-note](llope2012-star-mrpc-systems-note.md) (as-built overview; glass 1.1/0.54 mm agrees, five gaps vs six here) · [wu2007-star-barrel-tof-note](wu2007-star-barrel-tof-note.md) (TOFr prototype tray, QM2006) · [shao2002-mrpc-beam-test-note](shao2002-mrpc-beam-test-note.md) (USTC prototype MRPCs) · [ruan2009-mtd-concept-note](ruan2009-mtd-concept-note.md) (VPD position 5.4 m) · [beddo2003-bemc-note](beddo2003-bemc-note.md) (BEMC outside the CTB/TOF)
