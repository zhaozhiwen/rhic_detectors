---
title: STAR DAQ and trigger paths (BTOF, MTD, forward upgrade)
tags: [technology, detector]
sources: [llope2012-star-mrpc-systems.md, llope2012-star-mrpc-systems-note.md, ruan2009-mtd-concept.md, ruan2009-mtd-concept-note.md, yang2014-mtd-cosmic-calibration.md, yang2014-mtd-cosmic-calibration-note.md, huang2016-mtd-muon-id.md, huang2016-mtd-muon-id-note.md, gagliardi2022-star-forward-upgrade-talk.md, gagliardi2022-star-forward-upgrade-talk-note.md, schambach2006-star-tof-electronics.md, schambach2006-star-tof-electronics-note.md, kajimoto2009-star-tof-thesis.md, kajimoto2009-star-tof-thesis-note.md, star2018-forward-upgrade-proposal.md, star2018-forward-upgrade-proposal-note.md]
updated: 2026-11-16
---

# STAR DAQ and trigger paths (BTOF, MTD, forward upgrade)

**Same TOF readout chain for both. The papers spell it out for the BTOF; for the MTD they say only "STAR TOF electronics" and do not describe its path into STAR DAQ** ([open-questions](open-questions.md) #14). Detector pages: [star-barrel-tof](star-barrel-tof.md), [star-mtd](star-mtd.md); front-end comparison: [mrpc-technology](mrpc-technology.md). The forward-upgrade electronics (FCS DEP digitizers and trigger, FST readout via the IST DAQ, sTGC readout) are in the section [Forward upgrade](#forward-upgrade-fcs-and-fts-2018-design) below.

## BTOF chain [llope2012-star-mrpc-systems-note](../../raw/llope2012-star-mrpc-systems-note.md) · [schambach2006-star-tof-electronics-note](../../raw/schambach2006-star-tof-electronics-note.md) · [kajimoto2009-star-tof-thesis-note](../../raw/kajimoto2009-star-tof-thesis-note.md)

Llope 2012 describes the as-built chain; the 2006 electronics design paper [schambach2006-star-tof-electronics-note](../../raw/schambach2006-star-tof-electronics-note.md) gives the board internals, HPTDC arithmetic, cabling and the DAQ link. Values below are Llope 2012 unless marked (2006).

| Stage | Location | Role |
|---|---|---|
| TINO | on the tray; 8 per tray, also the gas-box lid and signal feed-through | 3 NINO amplifier-discriminators per 4 MRPCs (24 channels, 8 inputs per NINO); also gives "any channel over threshold" levels. NINO (2006): differential inputs, < 1 ns rise time, adjustable threshold, fixed offset on the output-pulse length so ToT needs no separate trailing-edge TDC |
| TDIG | on the tray, mounted on its TINO; water channel between them; 8 per tray | 3 HPTDCs (24 channels), 40 MHz clock, ~24.4 ps LSB, leading and trailing edges in the same channel (→ ToT); INL of all 23 040 channels measured on the bench. 2006: CANbus for HPTDC configuration, thresholds and temperature |
| TCPU | one per tray, at the high-z end | gathers, formats and buffers the 8 TDIGs; sends tray multiplicity 0–24 to the earliest STAR trigger level. 2006: distributes the 40 MHz clock from THUB; 12 HPTDCs of 4 TDIGs share one 80 Mbit/s serial port by hardware handshake → 2 data cables per tray (96 pads each); programmable logic + embedded CPU + SERDES to THUB |
| THUB | 4 in total, in chassis on the magnet steel | each collects 30 trays (240 TDIGs) and sends data over SIU/RORC links (ALICE DDL) to a receiver in STAR DAQ; one THUB generates the master clock for the others and the trays. 2006: 30 or 31 TCPUs each (two THUBs also take a start-side TCPU); SERDES over twisted pairs in CAT-6 cables, 4 SERDES channels → FPGA → fast memory; low-jitter 40 MHz clock; clock and commands from TCD, Busy back (Fig. 1); ALICE SIU daughter card, dual-fibre half-duplex link |
| DAQ receiver (2006) | DAQ room | Linux PC with a PCI RORC card and a Myrinet link to the rest of STAR DAQ; Fig. 1 also draws SIU fibres to L2 and DAQ |
| TPMD (2006) | start side (VPD) | replaces TINO: level adapters + discriminators for the PMT signals, then TDIG → TCPU as on the stop side; can split the PMT signals to separate fast z-vertex trigger electronics (not part of the TOF electronics) |

Per tray: 8 TINO, 8 TDIG, 1 TCPU, 192 channels, ~100 W, water-cooled.

### As built, with board history (2009) [kajimoto2009-star-tof-thesis-note](../../raw/kajimoto2009-star-tof-thesis-note.md)

The 2009 UT Austin thesis describes the chain as built and how the boards evolved. Renamings during R&D: **TFEE → TAMP → TINO** (MRPC front end), **TFEEb → TPMT → TPMD** (start side), **TMIT → THUB**.

| Board | Thesis details |
|---|---|
| TFEE (first) | MAXIM 3760 preamp + AD96685 comparator; designed for 24 channels, built as a 6-channel board for the prototype tray TOFr, with analog and NIM outputs (CAMAC ADC/TDC readout in the first cosmic stand) |
| TFEEb | TFEE variant for PMT input (start side) |
| TAMP | amplifier-only redesign, one card per 4 MRPCs, 960 cards; Maxim 3664 preamp, comparator (Maxim 9601) moved to the TDIG |
| TINO (final) | NINO ASIC (CERN, ALICE TOF), chosen February 2006 after UT cosmic tests; delays the trailing edge so both edges share one TDIG channel; 3 × 8-channel NINO per board |
| TDIG | 24 channels, 8 per tray; inputs discriminator hits, clock, multiplicity gate, L0 readout commands; outputs edge times and 5-bit partial multiplicity sums. Early: 3 HPTDC "very hi res" (25 ps bins) for leading edges + 1 HPTDC "hi res" (100 ps bins) for trailing edges; production: 3 HPTDCs "very hi res" for both. Hardware handshake lets 16 HPTDCs share one 80 Mbit/sec port ⇒ 2 data cables per tray; low-speed serial for configuration, thresholds, temperatures. Production board TDIG-F (2007), Altera Cyclone II |
| TPMT / TPMD | start side: PMT → fixed-threshold discriminator (half a MAX9601 per channel, 24 inputs on the TPMT) → TDIG; a branch to fast z-vertex electronics (Fig. 3.7) |
| TCPU | 120 on trays + 2 start side (East, West); two TDIG bus cables (up to 4 TDIGs each); CAN gateway; multiplicity sum to L0; readout of the tray's HPTDCs and SerDes link to THUB; configuration via CAN (to running settings or TDIG EEPROMs); trigger commands (Abort, L2 Accept) |
| THUB | 4, named NW, NE, SW, SE by position on the magnet ends; up to 16 SERDES daughter cards × 2 ports = 32 links; CAT-6 to each TCPU carries trigger, 40 MHz clock and serialized data; ALICE DDL SIU daughter card (thesis: "SUI") for the fibre to DAQ; Fig. 3.18 draws 31 TCPU interfaces |
| TOF DAQ receiver | Linux PC with 1 Myrinet interface, 4 fibre-optic interfaces and RORC cards (ALICE, built on the DDL DIU); needs PCI-X |
| TOF controller | Linux PC with 6 CAN-bus interfaces (PCAN-USB); root of slow control (GUIs Anaconda for tray tests, Anaconda II for the full system, from October 2008) |

Discrepancies: "16 HPTDCs per port" and "32 HPTDCs per tray" imply 4 HPTDCs per TDIG (the early layout), while the production text, Fig. 3.12 and the TDIG-F photo show 3; [schambach2006-star-tof-electronics-note](../../raw/schambach2006-star-tof-electronics-note.md) has 12 HPTDCs of 4 TDIGs per port, i.e. 3 per board — so 3 per TDIG is the production value [note]. The TCPU–THUB cable is CAT-6 in the data and SERDES descriptions but shielded CAT-5 in the clock description.

### Networks (thesis §3.3.11, Fig. 3.22) [kajimoto2009-star-tof-thesis-note](../../raw/kajimoto2009-star-tof-thesis-note.md)

| Network | Path |
|---|---|
| Data | MRPC → TINO twisted pairs (34-pin pigtail) → TDIG → 50-pin ribbon → TCPU → CAT-6 → THUB → DDL fibre → TOF DAQ receiver |
| CAN-bus | 6 networks from the TOF controller: 2 for the start-side TCPUs (East, West), the rest THUB ↔ tray TCPUs; in each tray two daisy-chains on the 50-pin ribbons |
| Trigger | Level-2 ↔ every THUB over DDL links of four dual optic fibres; TCD sends clock and commands, THUB returns Busy |
| Clock | single-rooted 40 MHz tree: master THUB (THUB-NW in Run 9) → slave THUBs (RG-58 coax) → TCPUs (shielded CAT-5) → TDIGs (50-pin ribbon) |
| Multiplicity | NINO → TDIG → TCPU, then a copper ribbon cable straight to the DSM of Level-0 |

Fig. 3.22: 30 trays per THUB; the pVPD West TCPU hangs on THUB-NW and pVPD East on THUB-NE.

### Run-9 operations [kajimoto2009-star-tof-thesis-note](../../raw/kajimoto2009-star-tof-thesis-note.md)
- HPTDC trigger matching window 25 µs (1001 coarse counts of 25 ns) and trigger offset 25225 ns at the start of Run 9; from March 17, 2009 (Day 76) 5000 ns (200 counts) with a 5200 ns (208 counts) offset. Tray tests used a 25 µs window, physics 5 µs (§5.3.1.2).
- New TCPU firmware (April 6–8, 2009) fixed an HPTDC fault when a trigger command arrives too close to a clock edge; a THUB-SW firmware fault (March 10–12) removed trays 1–20 and 51–60 from four runs.
- Day-50 threshold-scan runs show DAQ dead time rising from ≈ 1 % at 2500 mV to 40–50 % at 500 mV (Table 6.7 notes).

**HPTDC timing** [schambach2006-star-tof-electronics-note](../../raw/schambach2006-star-tof-electronics-note.md): 40 MHz input clock × PLL → 320 MHz (3.125 ns); 32-tap DLL → 97.66 ps per LSB; four samples offset by a 4-tap RC network → **24.41 ps** bin (Llope 2012's "~24.4 ps"). A clock-synchronous counter extends the range. Buffering: per-channel FIFO → 256-deep latency buffers → trigger matching (programmable window on trigger time tags) → 256-deep readout FIFO, read over a parallel (8 or 32 bit) or serial bus; untriggered mode sends every hit to the readout FIFO.

**Timing budget (2006 design)** [schambach2006-star-tof-electronics-note](../../raw/schambach2006-star-tof-electronics-note.md): total ≤ 100 ps after corrections, with 50 ps from the VPD start and 30 ps from corrections ⇒ stop < 80 ps; TOF = t_stop − t_start, start and stops digitized by the same electronics.

**Still open for the BTOF chain:** no source gives data, trigger or latency rates behind the buffering. The DDL is named by Llope 2012 and the thesis; the 2009 DAQ receiver (Myrinet, 4 fibre interfaces, RORC on PCI-X) is in [kajimoto2009-star-tof-thesis-note](../../raw/kajimoto2009-star-tof-thesis-note.md); changes after 2009 are not described in any ingested source.

## STAR trigger (thesis §2.2.10) [kajimoto2009-star-tof-thesis-note](../../raw/kajimoto2009-star-tof-thesis-note.md)

Levels 0 to 2 running on VME and NIM modules and Linux CPUs decide for every RHIC bunch crossing whether to read out the event. The fast trigger detectors (ZDC, BBC, pVPD, CTB, EEMC, BEMC, FPD) send digital data to the Data Storage and Manipulation boards (DSM). The CTB (240 scintillators in 120 trays) supplied the barrel charged multiplicity; its positions are now TOF trays, whose TCPU multiplicity goes to the Level-0 DSM over copper ribbon cable ([star-barrel-tof](star-barrel-tof.md)). Level-2 receives the TOF data over the THUB DDL fibres. Further reading: Bieser 2003 (below; thesis ref. [29]).

## MTD
- **2007–08 prototype (MTD7)**: simple front end, long cables to STAR trigger digitizer boards: 8-bit ADC, 30 mV discriminator, TAC gated by the RHIC clock. ADC and TAC values went into the Level-0 trigger, decided in < 1.5 µs; a hit on ≥ 1 strip triggered DAQ [ruan2009-mtd-concept-note](../../raw/ruan2009-mtd-concept-note.md). Timing in STAR ≈ 300 ps [llope2012-star-mrpc-systems-note](../../raw/llope2012-star-mrpc-systems-note.md).
- **From 2009 (MTD9) and the final system**: "STAR TOF electronics" (Llope 2012), "very similar to the STAR TOF system": HPTDC, 40 MHz, 24.4 ps LSB [yang2014-mtd-cosmic-calibration-note](../../raw/yang2014-mtd-cosmic-calibration-note.md).
- **Trigger**: each module end sends an analog multiplicity (OR of all strips) to Level-0, used to select events with MTD hits and to trigger on prompt hits only [yang2014-mtd-cosmic-calibration-note](../../raw/yang2014-mtd-cosmic-calibration-note.md). Single-muon and dimuon triggers count hits inside an online timing window; the 2013 dimuon trigger required ≥ 2 MTD hits in coincidence with the bunch crossing [huang2016-mtd-muon-id-note](../../raw/huang2016-mtd-muon-id-note.md). A Run-22 trigger table lists a dimuon trigger at 236 Hz [gagliardi2022-star-forward-upgrade-talk-note](../../raw/gagliardi2022-star-forward-upgrade-talk-note.md).
- **Not stated in any paper**: the MTD's path into STAR DAQ (own THUB/DDL or shared) and the trigger boards that receive its signals.

[note: from memory, unverified] The MTD shares the TOF's THUB and DDL path into DAQ, and its trigger signals go through STAR's QT trigger boards. Check against a dedicated MTD system paper or the STAR trigger/DAQ papers below before quoting.

## Forward upgrade: FCS and FTS (2018 design) [star2018-forward-upgrade-proposal-note](../../raw/star2018-forward-upgrade-proposal-note.md)

Design values from the November 2018 STAR proposal (not peer-reviewed); detector pages [star-fcs](star-fcs.md), [star-forward-tracking](star-forward-tracking.md).

**FCS front end → DEP.** SiPM → FEE (ECal: 4 towers per board; HCal: 2) → high-density differential-pair cables (≥ 25 m, as on the FMS postshower and EPD) → DEP/ADC. FEE slow control over I²C, up to 16 FEE per bus, bus master on the DEP (opto-isolated); bias, temperature-compensation and current monitors on the FEE.

| Board | Function |
|---|---|
| DEP/ADC ("Detector Electronics Platform", STAR BNL Electronics Group) | 32 × 12-bit ADCs at 8× the RHIC clock (13.3 ns ticks); FPGA does pedestal subtraction, zero suppression, charge integration, < 1 ns timing, highest tower and tower sums; up to 5 boards (160 channels) per chassis; fast optical link to a DAQ PC (bandwidth for full streaming at typical occupancy); STAR TCD interface for RHIC clock and trigger commands |
| DEP/IO | same platform with serial differential links instead of ADCs: up to 34 links, > 2000 bits per crossing; the last stage has a "STAR-standard" interface to the Trigger DSMs |
| Counts | 74 DEP/ADC (all ECal, HCal and preshower digitization) + 3 DEP/IO + spares. [note] As built: 24 ECal + 9 HCal DEP per half ([ruan2026-fcs-specs-email-note](../../raw/ruan2026-fcs-specs-email-note.md)); 2 × (24 + 9 + 4 preshower) = 74 |

**FCS trigger tree** (replaces the FMS scheme of QT boards + a three-layer DSM tree, whose 128-bit-in / 32-bit-out mid-1990s boards are too few, too slow and no longer buildable):
1. Layer 1 — DEP/ADC: pedestal and gain correction; each trigger board sends eight non-overlapping 2×2 tower sums of its 32 towers (64 bits per 107 ns crossing); preshower boards send hit maps.
2. Layer 2 — 2 DEP/IO (north, south), each fed by 20 ECal + 8 HCal + 4 preshower DEP/ADC: overlapping 4×4 trigger patches in ECal and HCal, ECal–HCal patch matching (Fig. 4-17 rule); EM if HCal < ¼ ECal, hadronic if HCal > ¼ ECal; electron/hadron need > ½ MIP in two of three preshower layers, photon none; jet sums over ≈ ¼ of the detector.
3. Layer 3 — 1 DEP/IO: single e/γ/jet/hadron thresholds; two separated electrons (Drell–Yan, J/ψ) and di-jets; decision to STAR trigger within 1.35 µs for every crossing.
- Simulated: photons 99% efficient at low energy → 96% at 80 GeV (threshold 80% of E); π⁻ 74% at 10 GeV (threshold 60%). Online gains set for hadrons; the ≈ 10% EM sampling difference corrected offline only.
- Run 17 test: 16-channel DEP prototype + 2 four-channel FEE prototypes on 8 SiPMs, under STAR Run Control and the trigger/clock network; 50 ns shaped pulses; 3 ns timing width.
- As built, Run 22 used FCS Drell–Yan (fcsDY ≈ 446 Hz, ≈ 20% of DAQ), J/ψ, jet-patch, di-jet, EM, hadron and high-tower triggers ([gagliardi2022-star-forward-upgrade-talk-note](../../raw/gagliardi2022-star-forward-upgrade-talk-note.md)) — the triggers the 2018 layer-3 design foresaw [note].

**FST (silicon) readout — IST DAQ re-used.** APV25-S1 (128 channels, 4 μs analog pipeline, 40 MHz) on the wedges inside the TPC inner field cage → unbuffered analog over cables up to 24 m (Fig. 5-6: "120 feet") → readout modules (≤ 24 APV each, isolated supplies, 12-bit at 37.532 MHz, buffering) → 6 modules per readout controller on a passive compact-PCI backplane → ALICE DDL (2.125 Gbps) → Linux PC → STAR event builders. 288 APV for the FST vs 864 for the IST. Slow control: Ethernet → DDL → RDO → I²C to the APVs. As built: IST electronics, DAQ and cooling re-used ([gagliardi2022-star-forward-upgrade-talk-note](../../raw/gagliardi2022-star-forward-upgrade-talk-note.md), [wang2024-star-forward-upgrade-note](../../raw/wang2024-star-forward-upgrade-note.md)).

**sTGC readout.** 2018 plan: the ALTRO-based STAR TPC chain freed by the iTPC upgrade (FEE, RDO, fibres, readout PCs, DAQ software), 24000 channels. **As built: VMM readout following the ATLAS design** ([wang2024-star-forward-upgrade-note](../../raw/wang2024-star-forward-upgrade-note.md)) — the plan was changed.

## Further reading (not ingested)
- J.M. Landgraf et al., "An overview of the STAR DAQ system", Nucl. Instrum. Meth. A 499 (2003) 762 — baseline (2001-era) DAQ architecture. Free PDF: https://www.star.bnl.gov/public/tpc/NimPapers/daq/daq_nim.pdf
- F.S. Bieser et al., "The STAR trigger", Nucl. Instrum. Meth. A 499 (2003) 766 — Level-0 trigger, where the MTD trigger signals go.
- J. Landgraf, "The Design and Implementation of the STAR DAQ system", talk at *Triggering Discoveries in High Energy Physics*, 9–14 September 2013: https://indico.cern.ch/event/246374/contributions/542866/ — how the DAQ evolved over 13 years as detectors such as the TOF and MTD were added. No slides attached on the indico page.
- Both NIM papers are in the NIM A 499 (2003) RHIC special issue, as are the BEMC and EEMC papers ([star-bemc](star-bemc.md), [star-eemc](star-eemc.md)) and the STAR magnet paper ([star-magnet-absorber](star-magnet-absorber.md)); the issue is linked from the SoLID wiki *RHIC detectors* page: https://solid.jlab.org/wiki/index.php?title=RHIC_detectors

## Related
[star-barrel-tof](star-barrel-tof.md) · [star-mtd](star-mtd.md) · [star-fcs](star-fcs.md) · [star-forward-tracking](star-forward-tracking.md) · [mrpc-technology](mrpc-technology.md) · [open-questions](open-questions.md)
