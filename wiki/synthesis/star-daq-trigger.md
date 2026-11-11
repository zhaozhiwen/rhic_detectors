---
title: STAR DAQ and trigger path for the BTOF and MTD
tags: [technology, detector]
sources: [llope2012-star-mrpc-systems.md, llope2012-star-mrpc-systems-note.md, ruan2009-mtd-concept.md, ruan2009-mtd-concept-note.md, yang2014-mtd-cosmic-calibration.md, yang2014-mtd-cosmic-calibration-note.md, huang2016-mtd-muon-id.md, huang2016-mtd-muon-id-note.md, gagliardi2022-star-forward-upgrade-talk.md, gagliardi2022-star-forward-upgrade-talk-note.md, schambach2006-star-tof-electronics.md, schambach2006-star-tof-electronics-note.md]
updated: 2026-11-10
---

# STAR DAQ and trigger path for the BTOF and MTD

**Same TOF readout chain for both. The papers spell it out for the BTOF; for the MTD they say only "STAR TOF electronics" and do not describe its path into STAR DAQ** ([[open-questions]] #14). Detector pages: [[star-barrel-tof]], [[star-mtd]]; front-end comparison: [[mrpc-technology]].

## BTOF chain [[llope2012-star-mrpc-systems-note]] · [[schambach2006-star-tof-electronics-note]]

Llope 2012 describes the as-built chain; the 2006 electronics design paper [[schambach2006-star-tof-electronics-note]] gives the board internals, HPTDC arithmetic, cabling and the DAQ link. Values below are Llope 2012 unless marked (2006).

| Stage | Location | Role |
|---|---|---|
| TINO | on the tray; 8 per tray, also the gas-box lid and signal feed-through | 3 NINO amplifier-discriminators per 4 MRPCs (24 channels, 8 inputs per NINO); also gives "any channel over threshold" levels. NINO (2006): differential inputs, < 1 ns rise time, adjustable threshold, fixed offset on the output-pulse length so ToT needs no separate trailing-edge TDC |
| TDIG | on the tray, mounted on its TINO; water channel between them; 8 per tray | 3 HPTDCs (24 channels), 40 MHz clock, ~24.4 ps LSB, leading and trailing edges in the same channel (→ ToT); INL of all 23 040 channels measured on the bench. 2006: CANbus for HPTDC configuration, thresholds and temperature |
| TCPU | one per tray, at the high-z end | gathers, formats and buffers the 8 TDIGs; sends tray multiplicity 0–24 to the earliest STAR trigger level. 2006: distributes the 40 MHz clock from THUB; 12 HPTDCs of 4 TDIGs share one 80 Mbit/s serial port by hardware handshake → 2 data cables per tray (96 pads each); programmable logic + embedded CPU + SERDES to THUB |
| THUB | 4 in total, in chassis on the magnet steel | each collects 30 trays (240 TDIGs) and sends data over SIU/RORC links (ALICE DDL) to a receiver in STAR DAQ; one THUB generates the master clock for the others and the trays. 2006: 30 or 31 TCPUs each (two THUBs also take a start-side TCPU); SERDES over twisted pairs in CAT-6 cables, 4 SERDES channels → FPGA → fast memory; low-jitter 40 MHz clock; clock and commands from TCD, Busy back (Fig. 1); ALICE SIU daughter card, dual-fibre half-duplex link |
| DAQ receiver (2006) | DAQ room | Linux PC with a PCI RORC card and a Myrinet link to the rest of STAR DAQ; Fig. 1 also draws SIU fibres to L2 and DAQ |
| TPMD (2006) | start side (VPD) | replaces TINO: level adapters + discriminators for the PMT signals, then TDIG → TCPU as on the stop side; can split the PMT signals to separate fast z-vertex trigger electronics (not part of the TOF electronics) |

Per tray: 8 TINO, 8 TDIG, 1 TCPU, 192 channels, ~100 W, water-cooled.

**HPTDC timing** [[schambach2006-star-tof-electronics-note]]: 40 MHz input clock × PLL → 320 MHz (3.125 ns); 32-tap DLL → 97.66 ps per LSB; four samples offset by a 4-tap RC network → **24.41 ps** bin (Llope 2012's "~24.4 ps"). A clock-synchronous counter extends the range. Buffering: per-channel FIFO → 256-deep latency buffers → trigger matching (programmable window on trigger time tags) → 256-deep readout FIFO, read over a parallel (8 or 32 bit) or serial bus; untriggered mode sends every hit to the readout FIFO.

**Timing budget (2006 design)** [[schambach2006-star-tof-electronics-note]]: total ≤ 100 ps after corrections, with 50 ps from the VPD start and 30 ps from corrections ⇒ stop < 80 ps; TOF = t_stop − t_start, start and stops digitized by the same electronics.

**Still open for the BTOF chain:** the paper gives no data, trigger or latency rates behind the buffering, and does not name the DDL (Llope 2012 does); later changes to the DAQ receiver (after 2006) are not described in any ingested source.

## MTD
- **2007–08 prototype (MTD7)**: simple front end, long cables to STAR trigger digitizer boards: 8-bit ADC, 30 mV discriminator, TAC gated by the RHIC clock. ADC and TAC values went into the Level-0 trigger, decided in < 1.5 µs; a hit on ≥ 1 strip triggered DAQ [[ruan2009-mtd-concept-note]]. Timing in STAR ≈ 300 ps [[llope2012-star-mrpc-systems-note]].
- **From 2009 (MTD9) and the final system**: "STAR TOF electronics" (Llope 2012), "very similar to the STAR TOF system": HPTDC, 40 MHz, 24.4 ps LSB [[yang2014-mtd-cosmic-calibration-note]].
- **Trigger**: each module end sends an analog multiplicity (OR of all strips) to Level-0, used to select events with MTD hits and to trigger on prompt hits only [[yang2014-mtd-cosmic-calibration-note]]. Single-muon and dimuon triggers count hits inside an online timing window; the 2013 dimuon trigger required ≥ 2 MTD hits in coincidence with the bunch crossing [[huang2016-mtd-muon-id-note]]. A Run-22 trigger table lists a dimuon trigger at 236 Hz [[gagliardi2022-star-forward-upgrade-talk-note]].
- **Not stated in any paper**: the MTD's path into STAR DAQ (own THUB/DDL or shared) and the trigger boards that receive its signals.

[note: from memory, unverified] The MTD shares the TOF's THUB and DDL path into DAQ, and its trigger signals go through STAR's QT trigger boards. Check against a dedicated MTD system paper or the STAR trigger/DAQ papers below before quoting.

## Further reading (not ingested)
- J.M. Landgraf et al., "An overview of the STAR DAQ system", Nucl. Instrum. Meth. A 499 (2003) 762 — baseline (2001-era) DAQ architecture. Free PDF: https://www.star.bnl.gov/public/tpc/NimPapers/daq/daq_nim.pdf
- F.S. Bieser et al., "The STAR trigger", Nucl. Instrum. Meth. A 499 (2003) 766 — Level-0 trigger, where the MTD trigger signals go.
- J. Landgraf, "The Design and Implementation of the STAR DAQ system", talk at *Triggering Discoveries in High Energy Physics*, 9–14 September 2013: https://indico.cern.ch/event/246374/contributions/542866/ — how the DAQ evolved over 13 years as detectors such as the TOF and MTD were added. No slides attached on the indico page.
- Both NIM papers are in the NIM A 499 (2003) RHIC special issue, as are the BEMC and EEMC papers ([[star-bemc]], [[star-eemc]]) and the STAR magnet paper ([[star-magnet-absorber]]); the issue is linked from the SoLID wiki *RHIC detectors* page: https://solid.jlab.org/wiki/index.php?title=RHIC_detectors

## Related
[[star-barrel-tof]] · [[star-mtd]] · [[mrpc-technology]] · [[open-questions]]
