---
title: "Schambach 2006 — STAR TOF readout electronics, DAQ, and cosmic-ray test stand (full-content paraphrase)"
type: raw-source
source_type: paper
authors: "J. Schambach, L. Bridges, G. Eppley, J. Hoffmann, K. Kajimoto, J. Liu, W. J. Llope, C. Mesa, T. Nussbaum (UT Austin, Blue Sky Electronics, Rice, M6 Research)"
journal: "2006 IEEE Nuclear Science Symposium Conference Record, vol. 1, pp. 485–488 (paper N14-161; San Diego, CA, Oct.–Nov. 2006)"
doi: "10.1109/NSSMIC.2006.356203"
arxiv: none
url: "https://ieeexplore.ieee.org/document/4179042"
captured_via: "Route 1 — IEEE Xplore full-text HTML (4 sections, 3 figures) in the user's Chrome via institutional access; text and MathJax TeX taken from the DOM, references from the Xplore reference list; every number and formula checked against pdftotext -layout of the publisher PDF (4 pp.), which matches the HTML; figures cropped from 300-dpi renders of the PDF (the HTML 'large' GIFs are only ~380 px wide)"
captured_date: 2026-11-10
captured_as: full-content paraphrase
figures: "3 (vision descriptions added 2026-11-10)"
vision_model: "claude-opus-5-5 (general-purpose subagent, model opus), 2026-11-10"
---

# STAR Time of Flight Readout Electronics, DAQ, and Cosmic Ray Test Stand — full-content paraphrase

- **Citation:** J. Schambach¹, L. Bridges², G. Eppley³, J. Hoffmann¹, K. Kajimoto¹, J. Liu³, W. J. Llope³, C. Mesa⁴, T. Nussbaum³, "STAR Time of Flight Readout Electronics, DAQ, and Cosmic Ray Test Stand". ¹University of Texas at Austin; ²Blue Sky Electronics, Houston; ³Rice University, Houston; ⁴M6 Research, Austin (all Texas, USA). The author list is not alphabetical, so the slug uses the first author.
- **Venue:** 2006 IEEE Nuclear Science Symposium Conference Record, vol. 1, pp. 485–488, paper N14-161 (San Diego). ISBN 1-4244-0560-2 (print).
- **DOI:** [10.1109/NSSMIC.2006.356203](https://doi.org/10.1109/NSSMIC.2006.356203) · IEEE Xplore document 4179042 · arXiv: none.
- **Route used:** Route 1 (publisher HTML). IEEE Xplore serves the full text as HTML (sections I–IV, 3 figures, 5 references). The only formula is set in MathJax; its TeX was read from the page. There is no acknowledgment section in either version.
- **PDF backup:** `assets/schambach2006-star-tof-electronics/source.pdf` (226 115 bytes, 4 pages, publisher version).
- **Verification:** every number, unit and the formula checked against `pdftotext -layout` of the PDF; the HTML and PDF texts agree. Figures were cropped from 300-dpi renders of PDF pages 2 and 4 (Fig. 1 and Figs. 2–3), checked for completeness and for no caption/text bleed.
- **Figure descriptions:** added by a separate vision subagent that read each crop.

> **[note] Scope.** A 4-page conference record written while the barrel TOF was still being designed (2006). Its value for this wiki is the **electronics chain** (TINO → TDIG → TCPU → THUB → DAQ), the **HPTDC timing arithmetic**, the **MRPC module and tray construction numbers**, the **timing budget**, and a cosmic-ray test stand result. It gives no beam or in-STAR performance.

---

## Abstract (paraphrase)

STAR is designing a new time-of-flight (TOF) system: 3840 multi-gap resistive plate chambers (MRPCs), each with 6 pads, spread over 120 trays, 23040 channels in all. Each tray carries 192 detector channels and three kinds of electronics cards, in data-flow order "TINO", "TDIG" and "TCPU". The data of every 30 trays go to one "THUB" card, which talks to the STAR trigger and sends the data over fiber to a receiver that is part of STAR DAQ. TINO holds the analog front end, built on the CERN/LAA NINO chip; TDIG digitizes with the CERN HPTDC ASIC; TCPU formats and buffers the digital data and passes them to THUB, which ships them over optical fiber to the DAQ room. A cosmic-ray test system (three plastic scintillators, 4 MRPC modules, prototype TOF electronics) was built to find the timing resolution the full system should reach; it gives an overall timing resolution of 80–110 ps for cosmic-ray events.

## I. The TOF proposal

RHIC's heavy-ion programme aims to make a new state of matter, the quark–gluon plasma (QGP), and to study QCD in matter at high temperature. Early measurements of particle multiplicities and transverse-momentum (energy) spectra show that RHIC nucleus–nucleus collisions reach energy densities never reached before. Recent RHIC results give a new view of the gluon-dominated initial stage, the partonic and hadronic evolution, and hadronic freeze-out.

STAR's particular strength is a large, uniform acceptance that measures and identifies a large share of the particles from heavy-ion collisions; this has already produced results such as the suppression of back-to-back jets in central Au+Au collisions. STAR's large-acceptance detectors are the Silicon Vertex Tracker (SVT), the Time-Projection Chamber (TPC) and the Barrel Electromagnetic Calorimeter (BEMC), each covering $2\pi$ in azimuth and $\vert\eta\vert \leq \sim 1.5$ in pseudorapidity. STAR proposes a barrel TOF detector based on MRPC technology that matches this acceptance [1]. It adds essential particle identification: the fraction of identified kaons and protons doubles to more than 95% of those produced inside the TOF barrel acceptance, $(\vert\eta\vert \leq \sim 1)$. High PID efficiency over a large solid angle matters most for multi-particle correlations, because their feasibility scales (on average) as the single-particle efficiency raised to the number of particles in the correlation. The wider momentum range for identified-particle spectra is needed to interpret the large-scale correlations and fluctuations seen in Au–Au collisions.

**[source issue]** "more that 95%" is printed; "more than" is meant.

## II. The detector

Large-acceptance TOF was part of the STAR design from the start, but the technology then proposed (mesh-dynode phototubes) was too expensive. Low-cost MRPCs developed for ALICE, together with new CERN electronics chips, now make it affordable. After extensive MRPC tests at CERN and BNL, and its use in the HARP experiment, the technology is mature; a full-scale prototype MRPC tray, with successive versions of prototype electronics, has been in STAR for in-situ tests since the 2003 RHIC run.

**MRPC construction.**
- An MRPC is a stack of resistive glass plates separated by uniform gas gaps. Electrodes sit on the outer surfaces of the outer plates; a 14 kV high voltage across them makes a strong field in every sub-gap. The internal plates are electrically floating.
- The gas is highly electronegative, mainly Freon R134a. A charged particle makes avalanches in the gaps; the signal induced on the pads is the sum of the avalanches in all gaps.
- The electrodes are resistive graphite tape, transparent to the induced charge, with a surface resistivity of $10^{5}\ \Omega$, covering the whole active area. Signals are picked up by copper pads.
- Glass: outer plates 0.7 mm, inner plates 0.55 mm thick. Spacers: 0.22 mm diameter nylon fishing line, which keeps the plates parallel. The pickup-pad layers are separated from the outer electrodes by 0.35 mm of Mylar.

**[note]** The fishing-line diameter sets the gap width, 0.22 mm (220 µm); the paper does not state the number of gaps. Surface resistivity is printed as "$10^5\ \Omega$" (per square implied).

**Trays.**
- The tray is the main mechanical structure: it holds the detectors at fixed positions and angles in three dimensions, supports the on-detector electronics, and forms all walls of the gas volume but one. It is an aluminium box with 50 mil (0.13 cm) walls and welded corners.
- 120 trays cover the outer cylindrical radius of the TPC, arranged as two adjoining cylindrical shells of 60 trays; each shell spans about 1 unit of pseudorapidity.
- Inside the gas volume are standard MRPC "modules" of 6 channels each, with channel (pad) dimensions $3.3\,\mathrm{cm} \times 6.1\,\mathrm{cm}$. 32 modules fill a tray.
- The tray "top" is a custom 1/8" thick board, the "TINO" board, which carries the front-end electronics. The TINO boards are at once the top of the gas box, the signal feed-through, the FEE boards and the mounting point for the TOF Digitization (TDIG) boards just above them. The electronics are therefore two layers: TINO (first electronics layer and tray lid) and TDIG (digitization) above it. One more board, "TCPU", at the high-$z$ end of the tray handles the digital data communication.
- The gas system supplies 95% Freon (R134a) + 5% isobutane at atmospheric pressure.

**[note] Pad size differs from Llope 2012.** This paper prints the pad as 3.3 cm × 6.1 cm; Llope 2012 (NIM A 661, S110; by a co-author of this paper) gives 3.5 × 6.1 cm². Six 3.3 cm pads span 19.8 cm, six 3.5 cm pads 21 cm. Which value is the as-built one is not settled by these two sources.

## III. Electronics design

A TOF system measures time intervals defined by one independently measured "start time" and some number of "stop times" per event. The proposed system digitizes the stop times on the detector for about 23000 channels, relative to a common clock. The start time (collision time) comes from the vertex position detector (VPD) — scintillator + PMT detectors close to the beam pipe — digitized the same way as the stops. These times, plus pulse-width data for the rise-time ("slewing") correction, are sent digitally to STAR DAQ, and the flight time is

$$\mathrm{TOF} = t_{\mathrm{stop}} - t_{\mathrm{start}}$$

(unnumbered in the source).

**Timing budget.** STAR's physics goals need a total resolution after all corrections of $\leq 100\,\mathrm{ps}$. With 50 ps from the VPD start and 30 ps from the timing corrections, the pure stop resolution must be below 80 ps. The MRPCs developed for the project have shown pure stop resolutions of 50–70 ps with prototype electronics very close to those described below.

**[note]** In quadrature, $\sqrt{100^2 - 50^2 - 30^2} \approx 81$ ps, consistent with the "less than 80 ps" requirement.

The other basic requirement on the electronics is enough buffering and transport capacity to deliver TOF data to STAR DAQ within the limits set by hit rates, trigger (event) rates and trigger latency.

![Fig. 1](assets/schambach2006-star-tof-electronics/fig1.png)

**Fig. 1.** Top-level diagram of the TOF electronics: the tray electronics (TINO, TDIG and TCPU boards), the start-detector electronics (TPMD, TDIG and TCPU boards), and the off-detector THUB board that connects to DAQ and trigger.

**Figure 1 — vision description.** Block diagram. Upper box "TOF Tray": inside a sub-box "TRAY CAN BUS" are four "TDIG" boxes linked to each other by double-headed arrows, four "TINO" boxes each feeding the TDIG above it, and four "MRPC" boxes (drawn as stacks, each marked "4") each feeding the TINO above it; the sub-box is labelled "96 CHAN". To its right is a tall box with vertical text "96 CHAN", then a tall "TCPU" box; an arrow "DATA, CLOCK & CANbus" runs between the TDIGs and TCPU. Outside the tray: TCPU → "MULTIPLICITY" → "L0 Trigger"; TCPU ↔ THUB labelled "COPPER: DATA, SAMPLE CLOCK, RESET TRIGGER STROBE & DATA"; "COPPER LINKS TO 29 TRAYS"; a "TOP LEVEL CAN BUS" line that branches to "CAN BUS TO 29 TRAYS" and "To Control PC". THUB: "TCD" sends "Clock & Commands" to THUB and receives "Busy"; two "SIU" boxes connect by "FIBER" to "L2" and to "DAQ"; "Reset & Clock From other THUBs" in, "Reset & Clock To other THUBs" out. Lower box "Start Detector": "PMTs" → "TPMD" (stacked, marked "3") → "TDIG" (stacked, marked "3") ↔ "Data, Clock & CANbus" ↔ "TCPU"; the start TCPU connects to THUB ("Copper; Data, Sample Clk, Reset Trg Strobe & Data") and to the CAN bus; a thick arrow from TPMD goes to "Fast Z-Vertex Electronics". Consistency: the tray is drawn as one half (4 MRPC groups → 4 TINO → 4 TDIG, "96 CHAN"), matching the text's two data cables of 4 TDIG / 96 pads each, while the text gives 8 TINO and 8 TDIG for 192 channels per tray; the second "96 CHAN" box presumably stands for the other half (not labelled). One drawn tray + "29 TRAYS" = 30 tray TCPUs, plus the start TCPU = 31, consistent with "30 or 31". **[note]** The TCPU–THUB label lists "DATA" twice, as printed. **Takeaway:** signals flow MRPC → TINO → TDIG → TCPU on each tray (start side PMT → TPMD → TDIG → TCPU); THUB collects the TCPUs over copper, takes clock and commands from TCD, and sends data to L2 and DAQ over SIU fibers.

Fig. 1 shows both the start and stop sides of the present system; by design the start-side chain is very similar to the stop side. The boards are described below.

**Readout concept.** On-detector electronics on the MRPC trays, tray-level buffering, and fiber-optic links to STAR DAQ. Each tray has:
- 192 MRPC detector channels;
- 8 amplifier/discriminator cards ("TINO"), 24 channels each;
- 8 time-to-digital converter cards ("TDIG"), 24 channels each;
- 1 buffer card ("TCPU") that stores and forwards the data of all 192 channels.

On the start-detector side the TINO is replaced by a "TPMD" card with level adapters and discriminators for the PMT signals. The TPMD can split the PMT signals for separate electronics that find the interaction-vertex position for triggering; those electronics are not part of the TOF electronics. The THUB card connects 30 TCPU cards to the STAR trigger and DAQ; two THUB cards have an extra interface for the TCPU of the start-detector electronics.

**TINO.** The interface between the MRPC tray and the TDIG readout card. It amplifies and discriminates the MRPC signals with the CERN/LAA analog ASIC "NINO" [2], developed for the MRPCs of ALICE [2].
- NINO has differential inputs, to use the MRPCs' differential signals; a fast amplifier with less than 1 ns rise time; and a discriminator with adjustable threshold.
- Slewing is corrected by estimating the rise-time slewing from the signal's time over threshold (ToT). So that this needs no separate trailing-edge TDC, NINO can add a fixed offset to the output-pulse length to cover the TDC's finite dead time.
- 8 inputs per NINO chip; 3 NINO chips per TINO board. Each TINO board serves 4 six-channel MRPC modules.

**TDIG.** Records the signal times relative to a system-wide clock with the CERN High-Performance TDC "HPTDC" [3], [4], [5], developed for ALICE and CMS.
- The HPTDC samples time with a tapped delay line. The 40 MHz input clock is multiplied on chip to 320 MHz by a phase-locked loop (PLL). This 3.125 ns clock goes through a 32-tap delay-locked loop (DLL), which is sampled when a hit arrives: 97.66 ps per least significant bit (LSB).
- In addition the chip samples the input 4 times, with small time offsets made by a 4-tap RC network. Finding in which sample the reference-clock edge leaves a DLL tap gives the hit time to within the sample interval, so the bin width becomes 24.41 ps.
- A clock-synchronous counter, recorded with each time sample, extends the dynamic range.
- Buffering: a small FIFO per channel; measurements pass to a data-processing unit and, after encoding, into 256-deep latency buffers to wait for a trigger-matching unit. Hits belonging to a trigger are picked by trigger time tags inside a programmable window and stored in a common 256-deep readout FIFO, read out over a parallel (8 or 32 bit) or serial bus. The chip can also run untriggered, sending every hit to the readout FIFO.
- 3 HPTDC chips per TDIG card; each TDIG handles the 24 channels from one TINO. Each HPTDC channel records the leading edge (timing) and trailing edge (ToT for the slewing correction).
- The card also has a slow serial interface (CANbus) for HPTDC and logic configuration, discriminator-threshold control and temperature monitoring.
- Each TDIG is mounted on top of its TINO on the tray; a water channel between the TINO and TDIG cards cools both.

**[note]** $3.125\,\mathrm{ns}/32 = 97.66$ ps and $97.66/4 = 24.41$ ps, as printed.

**TCPU.** Concentrates the data of 8 TDIG cards and sends them to THUB.
- Distributes the 40 MHz clock (received from THUB) to the TDIGs.
- Sends multiplicity information from the tray to the lowest trigger level ("L0 trigger").
- A built-in hardware handshake lets all 12 HPTDCs of four TDIG cards share one 80 Mbit/s serial output port, so only 2 data cables are needed per tray (4 TDIG boards, 96 MRPC pads each).
- Built from programmable logic plus an embedded CPU, with a serializer/deserializer (SERDES) chip that receives control and trigger commands from THUB and sends digitized data to it.

**THUB.** Connects 30 or 31 TCPU cards to STAR trigger and DAQ.
- Data interface: a high-speed SERDES chip sending and receiving over twisted pairs in low-cost CAT-6 cables. Data from 4 SERDES channels go through an FPGA into fast memory, which holds the detector data until they are sent to DAQ over the fiber link.
- THUB makes a low-jitter 40 MHz clock for the HPTDCs and sends it to the TCPU on each tray. One THUB acts as master clock generator and distributes its clock to the other three, giving one common clock for all timing measurements.
- 4 THUB cards in total, each in a chassis mounted on the magnet steel.
- Each THUB carries a custom daughter card from CERN ALICE, the "Source Interface Unit" (SIU), giving a dual-fiber half-duplex link to STAR DAQ. The TOF DAQ receiver is a Linux PC with a PCI optical interface card ("Read Out Receiver Card", RORC) and a Myrinet link to the rest of STAR DAQ.

**[note]** 120 trays / 4 THUBs = 30 tray TCPUs per THUB; the two THUBs that also serve a start-detector TCPU handle 31.

## IV. Cosmic-ray test stand

A cosmic-ray test stand was built to test MRPC timing and the electronics. A gas box holding up to 4 MRPC modules sits between two scintillators above and one below; together they form a telescope whose coincidence triggers on a cosmic ray crossing the MRPCs (Fig. 2).

![Fig. 2](assets/schambach2006-star-tof-electronics/fig2.png)

**Fig. 2.** The cosmic-ray test stand and its electronics: two scintillators above and one below a gas box holding up to four MRPC modules; prototype electronics do the readout and data acquisition.

**Figure 2 — vision description.** Schematic. A vertical black arrow "Cosmic Ray" passes, top to bottom, through "Plastic Paddle Scintillator 1", "Plastic Paddle Scintillator 2", a grey box "Gas Box (Freon)" containing a white box "MRPC Stack", and "Plastic Paddle Scintillator 3". Orange lines run from scintillators 1, 2 and 3 into "TPMD" → "TDIG" → "TCPU", and from the MRPC Stack into "TINO" → "TDIG" → "TCPU"; TCPU → "DAQ" (rounded box). Boards are green; no THUB is drawn. Consistency: two scintillators above and one below agree with the caption; scintillators into TPMD + TDIG, MRPCs into TINO + TDIG, both TDIGs into one TCPU and no THUB all agree with the text. The figure shows a single "MRPC Stack" without a module count, so "up to four" cannot be checked from it; PMTs are not drawn, and the readout end is labelled only "DAQ" (the text's CANbus link to a PC is not labelled). **Takeaway:** a scintillator coincidence (via TPMD) triggers on cosmics crossing an MRPC stack in a Freon gas box, read out by one TCPU with no THUB.

**Readout of the stand.**
- The scintillators are read out at one end by photomultiplier tubes (PMTs); their signals are discriminated on a TPMD board and digitized by a TDIG board.
- The MRPC modules (up to 4) connect to a TINO board; its discriminated outputs are digitized by the HPTDCs of a second TDIG board.
- Both TDIGs connect to one TCPU. Here the TCPU's CANbus interface reads the data out to a PC, where they are archived for analysis.
- The PMT signals are split before the TPMD; the copy forms a coincidence trigger for a cosmic ray crossing the MRPCs. One test input of the prototype TCPU takes this trigger into its programmable logic, which then reads out both TDIGs over their data cables.
- The only board of the Fig. 1 chain not used is THUB, unnecessary at cosmic-ray data rates.

**Analysis.** The stand exercised every component of the proposed electronics in a realistic setup and also tests production MRPC modules for timing resolution.
- One MRPC module is the stop; the other modules give the start.
- A valid cosmic event must hit pads in a single column only.
- The measured HPTDC non-linearities are corrected; then leading-edge ("slewing") corrections are found by fitting the time differences against ToT.
- The sigma of the corrected time-difference distribution is taken as the overall timing resolution (typical example in Fig. 3). Collecting enough data takes a few days.
- Overall timing resolutions vary from module to module, 80–110 ps.

![Fig. 3](assets/schambach2006-star-tof-electronics/fig3.png)

**Fig. 3.** A typical time-difference distribution from the cosmic-ray stand after all corrections. The x-axis is the arrival time of the cosmic ray in one MRPC module minus the average arrival time in the other modules in the gas box. Its sigma is about 85 ps.

**Figure 3 — vision description.** Histogram with a Gaussian fit (ROOT style). Title "dT(m=2, p=2) Histogram"; x-axis "dT [ps]", linear, labelled ticks −1000 to 400 in steps of 200 (axis ≈ −1100 to ≈ 480); y-axis "Yield", linear, 0–70 in steps of 10. Statistics box "dT3_m2_p2_rev4": Entries 1790; Mean −308.5; RMS 99.5; χ² / ndf 109.7 / 86; Constant 62.73 ± 2.10; Mean −309.8 ± 2.2; Sigma 85.39 ± 1.96. Bin width not printed. The distribution peaks near −320 ps at about 70 counts, with sparse entries from about −800 to about +100 ps and some excess above the fit between about −200 and 0 ps. Consistency: the fitted sigma 85.39 ± 1.96 ps agrees with the caption's "about 85ps". **[note]** The peak sits at −309.8 ps rather than 0; a constant offset (e.g. cable or module delays) does not affect the width and the text does not discuss it. The RMS (99.5) exceeds the fitted sigma, showing non-Gaussian tails. **Takeaway:** the module-vs-average time difference has a fitted width of 85.39 ± 1.96 ps from 1790 entries.

**[note] What the 80–110 ps means.** The quoted resolution is the width of a *difference* (one module minus the average of the others), not unfolded to a single module. If all $N$ modules had the same resolution $\sigma$, the difference width would be $\sigma\sqrt{1 + 1/(N-1)}$; for $N = 4$, 85 ps would correspond to $\sigma \approx 74$ ps per module. The paper does not say how many modules were in the stand for Fig. 3 or do this unfolding, so this is an estimate only.

## References (as printed)

1. http://www.star.bnl.gov/, and STAR TOF proposal: http://www.star.bnl.gov/STAR/tof/publications/TOF_20040524.pdf
2. F. Anghinolfi, P. Jarron, A.N. Martemyanov, E. Usenko, H. Wenninger, M.C.S. Williams, A. Zichichi, "NINO: An ultra-fast and low-power front-end amplifier/discriminator ASIC designed for the multigap resistive plate chamber," Nucl. Instrum. Methods Phys. Res., A 533 183-187 (2004).
3. http://micdigital.web.cern.ch/micdigital/hptdc.htm
4. M. Mota, J. Christiansen, S. Debieux, V. Ryjov, P. Moreira, A. Marchioro, "A flexible multichannel high-resolution time-to-digital converter ASIC," 2000 IEEE Nuclear Science Symposium Conference Record, Volume 2, 9/155-9/159 (2000).
5. M. Mota, J. Christiansen, "A high-resolution time interpolator based on a delay locked loop and an RC delay line," IEEE Journal of Solid-State Circuits, Volume 34, Issue 10, 1360-1366 (1999).
