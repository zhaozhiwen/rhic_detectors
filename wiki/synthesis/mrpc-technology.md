---
title: MRPC technology — position resolution, rate capability, signal and readout
tags: [technology, detector, overview]
sources: [shao2002-mrpc-beam-test.md, shao2002-mrpc-beam-test-note.md, wu2007-star-barrel-tof.md, wu2007-star-barrel-tof-note.md, llope2012-star-mrpc-systems.md, llope2012-star-mrpc-systems-note.md, ruan2009-mtd-concept.md, ruan2009-mtd-concept-note.md, yang2014-mtd-cosmic-calibration.md, yang2014-mtd-cosmic-calibration-note.md, huang2016-mtd-muon-id.md, huang2016-mtd-muon-id-note.md, schambach2006-star-tof-electronics.md, schambach2006-star-tof-electronics-note.md]
updated: 2026-11-10
---

# MRPC technology — position resolution, rate capability, signal and readout

Cross-cutting questions about the STAR MRPCs: the barrel TOF ([star-barrel-tof](star-barrel-tof.md), pads) and the MTD ([star-mtd](star-mtd.md), long strips read at both ends). Answers from the seven STAR MRPC sources plus external web sources (listed at the end; items 1, 5, 6 are conference slides). Anything not taken from a cited source is tagged [note].

## 1. Position resolution: timing along a strip, strip/pad size across

**Along the strip (z, MTD): timing.** Each strip is read at both ends:

$$ z = \frac{v}{2}(t_L - t_R), \qquad \sigma_z = \frac{v}{2}\,\sigma_{\Delta t} $$

- Signal speed v: **not stated in any of the seven STAR papers**. A typical PCB-strip value is 15–18 cm/ns [note: from memory; [open-questions](open-questions.md) #9]. Then σ_z ≈ 1 cm ⇔ σ_Δt ≈ 110–130 ps.
- The avalanche's own jitter is common to both ends and cancels in t_L − t_R; what remains is electronics noise, threshold walk at each end and signal dispersion along the 87 cm strip. So σ_z is not directly the MRPC's 60–90 ps time resolution [note].
- Measured: 0.6–1 cm along the strip on the bench [ruan2009-mtd-concept-note](../../raw/ruan2009-mtd-concept-note.md); < 1 cm (LMRPC) [llope2012-star-mrpc-systems-note](../../raw/llope2012-star-mrpc-systems-note.md).

**Across the strips (φ, MTD): strip size.** [yang2014-mtd-cosmic-calibration-note](../../raw/yang2014-mtd-cosmic-calibration-note.md) assigns the hit to the centre of the strip with the largest signal, no charge interpolation ⇒ binary readout, σ = pitch/√12.

### Where √12 comes from [note]
With binary readout the error x − x_centre is uniform on [−p/2, +p/2] (p = pitch), so

$$ \sigma^2 = \frac{1}{p}\int_{-p/2}^{p/2} x^2\,dx = \frac{p^2}{12}, \qquad \sigma = \frac{p}{\sqrt{12}} \approx 0.29\,p . $$

**Why the integral is over x².** Variance is the mean squared distance from the mean, σ² = ∫(x − μ)² ρ(x) dx; here μ = 0 by symmetry and ρ(x) = 1/p across the strip.
- Plain x averages to zero: it measures offset, not spread.
- \|x\| also measures spread (gives p/4), but the squared form is standard because independent errors add in quadrature, σ²_tot = σ₁² + σ₂² — the rule used for every timing subtraction here, e.g. √(104² − 45² − 25²) ≈ 90 ps (MTD type A, Yang 2014).
- For a Gaussian, σ is exactly this RMS width, so p/√12 compares directly with fitted resolutions.
- Generally a flat distribution of full width w has σ = w/√12; the √12 is from the integral, not a detector property.

This is the best case for binary readout (one strip per hit, uniform illumination). Shared hits assigned to one centre and residual multiple scattering make it worse; interpolating with neighbouring signal sizes can beat it.

| Module | Pitch (strip + gap) | pitch/√12 [note] | Measured (Yang 2014, Table 2) |
|---|---|---|---|
| MTD type A | 2.5 + 0.4 = 2.9 cm | 0.84 cm | 0.9–1.1 cm ✓ |
| MTD type B (final) | 3.8 + 0.6 = 4.4 cm | 1.27 cm | 1.6–1.9 cm |

- Type B is worse than pitch/√12; the paper does not say why (leftover multiple scattering or charge sharing are candidates) [note].
- Caveat: the Run-12 type-B z (2.6 cm) equals the raw ΔZ width of Yang Fig. 5, so Run-12 values may be raw widths, not MS-corrected; the 1.9 cm φ may be inflated the same way ([open-questions](open-questions.md) #12). Run-11 type B (1.4 cm z, 1.6 cm φ) is the safer comparison.
- Why STAR didn't push further: collision muons at ~2 GeV/c scatter ≈ 10 cm in the backleg steel [yang2014-mtd-cosmic-calibration-note](../../raw/yang2014-mtd-cosmic-calibration-note.md) ([star-magnet-absorber](star-magnet-absorber.md)).

### 2D pads (BTOF) [note]
A pad of width a and length b is binary in both directions; x uniform on [−a/2, a/2] and y on [−b/2, b/2], independently:

$$ \sigma_x = \frac{a}{\sqrt{12}}, \qquad \sigma_y = \frac{b}{\sqrt{12}}, \qquad \sigma_{2D} = \sqrt{\sigma_x^2 + \sigma_y^2} $$

| Pad | Size | σ_x | σ_y | combined |
|---|---|---|---|---|
| Final BTOF [llope2012-star-mrpc-systems-note](../../raw/llope2012-star-mrpc-systems-note.md) | 3.5 × 6.1 cm² | 1.01 cm | 1.76 cm | 2.03 cm |
| 2002 USTC prototype [shao2002-mrpc-beam-test-note](../../raw/shao2002-mrpc-beam-test-note.md) | 3.1 × 3.0 cm² | 0.89 cm | 0.87 cm | 1.24 cm |

Conditions:
- Uniform illumination over the pad (true for tracks spread over many pads; a narrow beam breaks it).
- One pad fires per hit; edge hits that fire the neighbour are assigned to the wrong centre (Shao 2002: efficiency ≈ 80% and timing ≥ 100 ps in the 3 mm inter-pad gaps).
- Size vs pitch: if gap hits are lost use pad size; if they fire a neighbour use the pitch. The final BTOF gap is not given ⇒ 1.01/1.76 cm are lower bounds.
- Interpolation could beat it, but the STAR TOF reads only time and ToT per pad.
- BTOF position comes from the TPC track; the pad only matches track to hit. Inferred orientation (3.5 cm in φ, 6.1 cm along z) on [star-barrel-tof](star-barrel-tof.md).

A strip differs: binary only across its width; along its length the two-end time difference gives < 1 cm.

## 2. Rate capability (Hz/cm²)

**STAR MRPCs use float-glass electrodes ⇒ roughly hundreds of Hz/cm² up to ≈ 1 kHz/cm².** None of the seven STAR papers measures a rate limit:
- BTOF test beam ran at 200 Hz/cm², the highest rate expected at RHIC-II, with > 95% efficiency and < 75 ps [llope2012-star-mrpc-systems-note](../../raw/llope2012-star-mrpc-systems-note.md); the 2002 beam test ran below 100 Hz/cm² [shao2002-mrpc-beam-test-note](../../raw/shao2002-mrpc-beam-test-note.md).
- The MTD papers need none: rates behind the magnet steel are negligible.
- [wu2007-star-barrel-tof-note](../../raw/wu2007-star-barrel-tof-note.md) says only that rate capability and ageing were studied in USTC theses (its refs [3–5]), no numbers.

**Mechanism.** Avalanche charge drains through the resistive glass; the current drops a voltage across it:

$$ \Delta V = \rho \cdot d \cdot \langle q \rangle \cdot \Phi $$

(ρ glass bulk resistivity, d glass thickness, ⟨q⟩ mean avalanche charge, Φ particle flux). Rising flux lowers the gap field ⇒ efficiency and timing degrade. Levers: lower resistivity, thinner glass, smaller avalanche charge, warmer glass.

| Electrode | Rate capability | Notes / source |
|---|---|---|
| STAR TOF float glass (Llope 2012: 5 × 220 µm, 0.54 mm float glass, ~10¹³ Ω cm; [1] says 6 × 0.22 mm gaps; 2006 design [schambach2006-star-tof-electronics-note](../../raw/schambach2006-star-tof-electronics-note.md): 0.55 mm inner, 0.7 mm outer glass vs Llope's 1.1 mm outer) | < ~500 Hz/cm² | Wang Yi, RPC2018 [1]; STAR test beam 200 Hz/cm², > 95%, < 75 ps (Llope 2012) |
| Float glass, general | a few hundred Hz/cm² at most | Tsinghua high-rate MRPC study [2] |
| Thin float glass 0.7 / 0.5 / 0.35 mm | 0.5 / 0.75 / 3.2 kHz/cm², at ~75 ps | Tsinghua thin-glass study [3] |
| Low-resistivity doped glass (~10¹⁰ Ω cm) | ~25 kHz/cm²; tested to ~70 kHz/cm² | Tsinghua/CBM [2][4]; limit = 20 ps resolution loss or 5% efficiency drop |
| Ceramic (~10⁹ Ω cm) | ~500 kHz/cm², ~70 ps, 90% efficiency | CBM overview [5] |

Float glass ≈ 3 × 10¹² Ω cm per the CBM slides [5], about two orders above doped glass.

Caveats:
- **MTD glass**: thickness known (1.1 mm outer, 0.7 mm inner, 0.25 mm gaps; Yang 2014 Fig. 1), type and resistivity not stated. Given the STAR TOF lineage almost certainly float glass ⇒ ≈ 0.5 kHz/cm² by the thin-glass row; treat the MTD as sub-kHz/cm² [note].
- **Convert background rates first**: limits are for charged (MIP) flux; photons and neutrons count only through their detection efficiency. Tsinghua estimate for SoLID [6]: ≈ 250 kHz/cm² of photons ⇒ ≈ 12.5 kHz/cm² detected (~5%); total detected incl. electrons and neutrons ≈ 18 kHz/cm². Without per-species efficiencies the photon requirement is overstated ≈ 20×.
- **No transfer to high rate**: neither STAR design carries over to a 10 kHz/cm²-scale environment; that needs low-resistivity glass (the CBM and SoLID TOF route) [note].

## 3. No photosensor

The MRPC is a gas detector: avalanches in the thin gaps induce a current directly on the copper pads/strips; the floating resistive glass is transparent to the induced signal [shao2002-mrpc-beam-test-note](../../raw/shao2002-mrpc-beam-test-note.md). ≈ 25 fC per hit goes straight into a fast amplifier-discriminator (NINO) and then the HPTDC [llope2012-star-mrpc-systems-note](../../raw/llope2012-star-mrpc-systems-note.md). The pad signal is the sum of the avalanches in all gaps, picked up through resistive graphite-tape electrodes (10⁵ Ω) and 0.35 mm Mylar [schambach2006-star-tof-electronics-note](../../raw/schambach2006-star-tof-electronics-note.md).
- This is why STAR chose MRPCs: a scintillator TOF would need ≈ 25 000 fast PMTs (64 m²), too costly, and PMTs must cope with the magnetic field [shao2002-mrpc-beam-test-note](../../raw/shao2002-mrpc-beam-test-note.md).
- STAR still uses PMTs for the start time: the VPDs, 5.4 m from the nominal collision point on each side along the beam [ruan2009-mtd-concept-note](../../raw/ruan2009-mtd-concept-note.md). The 2006 design budget gives the VPD start 50 ps of a ≤ 100 ps total [schambach2006-star-tof-electronics-note](../../raw/schambach2006-star-tof-electronics-note.md).

## 4. Readout electronics: BTOF vs MTD

**BTOF: NINO/TINO by name. MTD: "STAR TOF electronics" only; no front-end board or chip named.**

| | BTOF (final) | MTD (final) |
|---|---|---|
| Front end | NINO on TINO boards: 3 NINO per 4 MRPCs, 24 channels [llope2012-star-mrpc-systems-note](../../raw/llope2012-star-mrpc-systems-note.md); NINO: differential inputs (MRPC signals are differential), < 1 ns rise, adjustable threshold [schambach2006-star-tof-electronics-note](../../raw/schambach2006-star-tof-electronics-note.md) | "STAR TOF electronics" (Llope 2012); "very similar to the STAR TOF system" [yang2014-mtd-cosmic-calibration-note](../../raw/yang2014-mtd-cosmic-calibration-note.md); not named |
| Digitizer | TDIG, 3 HPTDC each, 40 MHz, ~24.4 ps LSB; 40 → 320 MHz PLL (3.125 ns), 32-tap DLL (97.66 ps), 4-tap RC → 24.41 ps bin [schambach2006-star-tof-electronics-note](../../raw/schambach2006-star-tof-electronics-note.md) | HPTDC, 40 MHz, 24.4 ps LSB |
| Pulse size | ToT (leading + trailing edges), used for slewing; NINO adds a fixed offset to the output-pulse length to cover the TDC dead time, so no separate trailing-edge TDC is needed [schambach2006-star-tof-electronics-note](../../raw/schambach2006-star-tof-electronics-note.md) | ToT; slewing uses ⟨ToT⟩ = √(ToT_L·ToT_R) |
| Channels per detector | 6 pads → 6 per MRPC | 12 strips × 2 ends → 24 per module |
| Trigger output | TCPU sends tray multiplicity 0–24 to the earliest trigger level | analog OR of all strips from each module end to Level-0 |
| Signal path | pads → NINO directly, ~25 fC/hit | strips → front end directly |

MTD electronics history:
1. **MTD7 prototype (2007–08)**: simple front end, long cables, STAR trigger digitizers (8-bit ADC, 30 mV discriminator, TAC); ≈ 200–300 ps in STAR [ruan2009-mtd-concept-note](../../raw/ruan2009-mtd-concept-note.md), [llope2012-star-mrpc-systems-note](../../raw/llope2012-star-mrpc-systems-note.md).
2. **From 2009 (MTD9)**: on-board STAR TOF electronics; 90–110 ps ([yang2014-mtd-cosmic-calibration-note](../../raw/yang2014-mtd-cosmic-calibration-note.md)).

The MRPC did not change between the two; electronics and cable length did.

**Reading cosmic-stand resolutions** [note]: the BTOF cosmic stand quotes 80–110 ps for one module minus the mean of the other modules in the box, not unfolded to a single module; for 4 equal modules a difference width of 85 ps corresponds to ≈ 74 ps per module [schambach2006-star-tof-electronics-note](../../raw/schambach2006-star-tof-electronics-note.md). Compare single-module (pure stop) numbers only after such an unfolding. [note: from memory, unverified] The MTD front-end board is a TINO variant called "MINO", still NINO-based ([open-questions](open-questions.md)). DAQ chain: [star-daq-trigger](star-daq-trigger.md).

## Sources (external, paraphrased)
1. Wang Yi, "Status of MRPC TOF technology", RPC2018 — https://indico.gsi.de/event/7001/contributions/31638/attachments/22749/28543/status_of_MRPC_TOF_technology.pdf
2. "Study on high rate MRPC for high luminosity experiments" (Tsinghua) — https://www.aminer.org/pub/56d81c86dabfae2eee9e329e/study-on-high-rate-mrpc-for-high-luminosity-experiments
3. "Study on the rate capability of MRPCs assembled with thin glass" — https://manuscript.isc.ac/Inventory/49/687022.htm
4. J. Wang, PoS(RPC2012)015 — https://pos.sissa.it/159/015/pdf
5. I. Deppner, CBM-TOF, FAIR 2014 — https://indico.gsi.de/event/2443/contributions/9096/attachments/7133/8765/deppner_FAIR2014.pdf
6. Wang Yi, 9th Workshop on Hadron Physics in China (2017) — https://indico.ihep.ac.cn/event/6610/contributions/85812/attachments/44998/51741/WangYi.pdf

Items 1, 5 and 6 are conference slides, not peer-reviewed papers.

## Related
[star-barrel-tof](star-barrel-tof.md) · [star-mtd](star-mtd.md) · [star-daq-trigger](star-daq-trigger.md) · [star-magnet-absorber](star-magnet-absorber.md) · [open-questions](open-questions.md)
