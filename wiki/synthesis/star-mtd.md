---
title: STAR Muon Telescope Detector (MTD)
tags: [experiment, detector, technology, measurement, status]
sources: [ruan2009-mtd-concept.md, ruan2009-mtd-concept-note.md, yang2014-mtd-cosmic-calibration.md, yang2014-mtd-cosmic-calibration-note.md, huang2016-mtd-muon-id.md, huang2016-mtd-muon-id-note.md, llope2012-star-mrpc-systems.md, llope2012-star-mrpc-systems-note.md, beddo2003-bemc.md, beddo2003-bemc-note.md, star2026-detector-status.md, star2026-detector-status-note.md]
updated: 2026-11-11
---

# STAR Muon Telescope Detector (MTD)

Long-strip MRPCs at r ≈ 400 cm on the outside of the STAR magnet backlegs, which serve as hadron absorber; muons are identified by matching TPC tracks to MTD hits in time and position. Sources: design/concept with 2007–08 prototype data [ruan2009-mtd-concept-note](../../raw/ruan2009-mtd-concept-note.md), cosmic-ray calibration [yang2014-mtd-cosmic-calibration-note](../../raw/yang2014-mtd-cosmic-calibration-note.md), muon ID in p+p 500 GeV [huang2016-mtd-muon-id-note](../../raw/huang2016-mtd-muon-id-note.md), planned final design in [llope2012-star-mrpc-systems-note](../../raw/llope2012-star-mrpc-systems-note.md). Absorber geometry: [star-magnet-absorber](star-magnet-absorber.md). MRPC physics: [mrpc-technology](mrpc-technology.md). DAQ/trigger: [star-daq-trigger](star-daq-trigger.md).

## Module types and parameters across the papers

| Item | 2009 Ruan (design) | 2014 Yang (cosmics) | 2016 Huang (muon ID) |
|---|---|---|---|
| Module | long-MRPC, 2 stacks, 10 × 250 µm gaps, 6 strips 870 × 25 mm² | **Type A**: 2 stacks, 10 gaps, 6 strips 2.5 cm + 0.4 cm gap, 87 × 17 cm². **Type B (final)**: 1 stack, 5 × 250 µm gaps, 12 strips 3.8 cm + 0.6 cm gap, 87 × 52 cm²; Fig. 1 glass 1.1 mm outer / 0.7 mm inner. **Type C**: 6 gaps | — |
| Gas | 95% C₂H₂F₄ + 5% iso-butane, 1 atm | 95% R-134a + 5% isobutane | — |
| HV | 12.6 kV; > 95% eff. for 12.5–13.0 kV | — | — |
| Readout | trigger digitizers (8-bit ADC, TAC) 2007–08; TOF electronics from 2009 | TOF electronics (HPTDC), 40 MHz, 24.4 ps LSB | — |
| Timing | 60–70 ps bench; 200–300 ps in STAR 2007–08 | 90 ps type A (2010); 101 / 108 ps type B (Run 11 / Run 12) | ~100 ps, quoting 2014 |
| Position | 0.6–1 cm along strip (bench) | type A 0.8 cm (z), 2.2 mrad = 0.9 cm (φ); type B 1.4–2.6 cm (z), 1.6–1.9 cm (φ) | 1–2 cm, quoting 2014 |
| Radius / coverage | ~400 cm; plan 56% of 2π at \|η\| < 0.8 | ~400 cm; 45% at \|η\| < 0.5 | ~403 cm; ~45% at \|η\| < 0.5; 10/63/100% installed for Runs 2012/13/14 |
| Full-system size | 540 modules, 2160 strips, 4320 channels (plan) | 12 type-B modules = "10% of the full MTD" (Run 12) | — |

Planned final design [llope2012-star-mrpc-systems-note](../../raw/llope2012-star-mrpc-systems-note.md): **117 WMRPCs**, single stack, 5 gaps, outer 91.5 × 58.0 × 3 cm³, twelve 87 × 3.8 cm² strips with 0.6 cm gaps, double-ended TOF electronics, five trays per backleg; LMRPC prototype > 95%, ≈ 70 ps, < 1 cm along strip; MTD7 in STAR ≈ 300 ps.

Type-A timing check [note]: √(104² − 45² − 25²) ≈ 90 ps (quadrature subtraction, [yang2014-mtd-cosmic-calibration-note](../../raw/yang2014-mtd-cosmic-calibration-note.md)).

## Coverage and size

| Quantity | 2009 plan | As built (2014, 2016) | Derived check [note] |
|---|---|---|---|
| η range | \|η\| < 0.8 (full bar length) | \|η\| < 0.5 | 6.85 m bars at r = 400 cm span \|η\| < 0.78 ✓; \|η\| < 0.5 at 403 cm is \|z\| < 210 cm = 4.2 m → fits **5 type-B modules** (4.35 m) per backleg |
| φ coverage | 56% of 2π, bar faces only | ~45% | see below |
| Radius | ~400 cm | ~400 cm (2014), ~403 cm (2016) | — |
| Modules | 540 long-MRPCs | not stated; 12 type B = 10% | → ≈ 120 type-B modules |
| Strips / channels | 2160 / 4320 | not stated | 120 × 12 = 1440 strips; × 2 ends = 2880 channels |
| Area | 540 × 87 × 17 cm² ≈ 80 m² | type B 87 × 52 cm² | 120 × 0.452 m² ≈ 54 m² module; ≈ 47.6 m² strip area |

**As built (Zhiwen, personal communication, 2026-11-09): 122 MTD trays, each ≈ 90 cm × 55 cm.** Checks [note]:
- One tray holds one WMRPC (91.5 × 58 × 3 cm³ outer, Llope 2012; type B 87 × 52 cm², Yang 2014) → 90 × 55 cm fits ✓.
- 122 modules: 1464 strips, 2928 channels (two ends).
- Strip area 122 × 87 cm × 45.6 cm = **48.4 m²** = **45.5%** of the \|η\| < 0.5 band at 403 cm (2π × 403 × 420 cm ≈ 106 m²) ✓ quoted 45%.
- Tray footprint 122 × 0.90 × 0.55 m ≈ 60 m²; module footprint (87 × 52 cm) ≈ 55 m².
- Close to the ≈ 120 implied by Yang 2014 and the 117 planned in Llope 2012. With 117: strip area 46.4 m² (43.8%), outer footprint 62.1 m², 1404 strips, 2808 channels.
- 5 modules per backleg × 24 backlegs = 120; 122 does not divide evenly into 5 per backleg, so some backlegs carry a different number [note]. A "122 modules on 27 backlegs" figure is from memory and unverified ([open-questions](open-questions.md)).

**2009 plan inconsistency** [note]: 56% of 2π at 400 cm ⇒ ≈ 47 cm active width per bar, but the bar faces (30 × 57 cm at 363 cm) subtend ≈ 75% and the 2009 Fig. 2 event display shows ≈ 72–75%. Area at 56% × full bar length ≈ 96 m² vs ≈ 80 m² from 540 type-A-sized modules. Unexplained ([open-questions](open-questions.md) #11).

As-built coverage (45% at \|η\| < 0.5) is smaller than the 2009 plan (56% at \|η\| < 0.8).

## Muon identification

- **Absorber**: backlegs (≈ 61 cm Fe, ≈ 3.6 λ_I) + BEMC (≈ 0.7 λ_I) [note]; papers say "five interaction lengths" (2009), "about 5 absorption lengths" (2016), "about 6 interaction lengths (BEMC + back-legs)" (Llope 2012). See [star-magnet-absorber](star-magnet-absorber.md).
- **Resolution behind steel**: 2 GeV/c collision muons scatter by ≈ 10 cm and 100 ps in the backlegs [yang2014-mtd-cosmic-calibration-note](../../raw/yang2014-mtd-cosmic-calibration-note.md); consistent with σ_z ≈ 10 cm in 2009 prototype data.
- **2008 d+Au prototype** [ruan2009-mtd-concept-note](../../raw/ruan2009-mtd-concept-note.md): with MTD-hit association only, prompt muons are 6–10% of muon candidates; pion decays 30–40%, rest mostly kaon decays within the first ~2 m. Tight dE/dx (nσ_π > 1) raises primary/secondary to 1/6–1/3 at 26% efficiency. Within \|Δz\| < 20 cm, matching + dE/dx + velocity give muon purity > 80%. Simulation: < 1% of hadrons accepted (the quoted rejection factor 50–100 would mean 1–2% [note]).
- **Matching cut (2014)**: Δφ < 0.2 rad (HTML, PDF and arXiv agree); 2π/30 = 0.209 rad ⇒ same-backleg match, very loose (≈ 33σ) [note].
- **p+p 500 GeV (2016)** [huang2016-mtd-muon-id-note](../../raw/huang2016-mtd-muon-id-note.md): likelihood-ratio method plateau ≈ 90% for p_T > 3 GeV/c (text: ≈ 80% for the other methods, which matches the MC; the Fig. 6 data plateaus are ≈ 0.67 straight cuts and ≈ 0.72 N−1 [note], see [open-questions](open-questions.md)); J/ψ efficiency 0.81 (probed muon); significance ×1.38 with one muon, ×2.0 (S/√B = 31.89) with both. All methods cut background by > 65%. The conclusion's "about 60%" efficiency conflicts with the 81% (tagged [source issue]).
- **Triggers**: analog OR per module end to Level-0; dimuon trigger 2013 required ≥ 2 MTD hits in coincidence with the bunch crossing ([star-daq-trigger](star-daq-trigger.md)).
- Comparison to calorimeter-based π/μ separation: [pi-mu-separation-calorimetry](pi-mu-separation-calorimetry.md).

## Cross-paper discrepancies (resolved against the PDFs)

1. **Backleg thickness**: 60 cm (2009), 57 cm (2014), 61 cm (2016), all at r = 363 cm. 2009 Fig. 4 CAD prints 24.000" [60.96 cm] thick, 22.5" [≈ 57.1 cm] wide ⇒ Yang's "57 cm thick" is most likely the width. Use ≈ 61 cm thick, 57 cm wide ([star-magnet-absorber](star-magnet-absorber.md)).
2. **"About 5 interaction/absorption lengths"**: steel alone ≈ 3.6 λ_I; + BEMC ≈ 0.7 λ_I ⇒ ≈ 4.3 λ_I; coil and TOF/TPC add a little; "about 5" is a generous round number [note].
3. **Backleg field**: 1.2 T (2009) vs −1.26 T (2014, used in the extrapolation; opposite to the 0.5 T central field). Yang also says t_Steel uses 0.5 T; effect on timing ≪ 1 ps, matters only for position matching [note].
4. **TOF coverage**: −1 < η < 1 (2009), "η < 1" (2007), \|η\| < 0.9 (2014). As built: \|η\| < 0.9 ([star-barrel-tof](star-barrel-tof.md)).
5. **Strips per module (2009 plan)**: 2160/540 = 4, which does not match the 6 strips per prototype module (the paper does not state strips per module for the full design); built type B has 12. The 2009 channel count is obsolete.
6. **Azimuthal coverage (2009)**: 75% (bars, Fig. 2) vs 56% (text). Unexplained.
7. **Δφ < 0.2 rad (2014)**: not a typo; same-backleg match.

Other in-paper issues tagged in the notes: 2009 "energy loss due to multiple scattering" ≈ 1.2 GeV (it is ionization; ≈ 0.7–0.8 GeV for 60 cm Fe at normal incidence, so 1.2 GeV is the full material on oblique paths) [ruan2009-mtd-concept-note](../../raw/ruan2009-mtd-concept-note.md); 2016 "about 60%"; 2016 Fig. 3 caption listing ΔToF; 2014 Fig. 9 caption missing ⟨ToT⟩; figure-marker mismatches.

## Takeaways for MRPC design choices [note]

My reading of the results, not claims made in the papers.
- **Electronics, not the MRPC, drove in-situ timing**: the same modules went from 200–300 ps to ≈ 90 ps when the readout changed from trigger digitizers on long cables to on-board TOF electronics.
- **The final design chose area over timing**: single-stack 5-gap type B over double-stack type A despite ≈ 10–20 ps worse resolution. Yang 2014 gives no reason; cost per area (87 × 52 vs 87 × 17 cm²) is plausible but not citable.
- **What sets the resolution**: multiple scattering (≈ 10 cm, 100 ps at 2 GeV/c). Position resolution beyond ≈ 1 cm buys nothing behind an absorber.
- **φ resolution = strip pitch/√12**: 0.84 cm (type A; 0.9 measured), 1.27 cm (type B; 1.6–1.9 measured) — see [mrpc-technology](mrpc-technology.md). Run-12 type-B z = 2.6 cm equals the raw Fig. 5 width; may not be MS-corrected ([open-questions](open-questions.md) #12); Run-11 values (1.4 cm z, 1.6 cm φ) are the safer comparison.
- **Rate**: none of the MTD papers gives a rate capability (not needed behind steel); see [mrpc-technology](mrpc-technology.md).
- **Strip signal speed**: not stated in any paper ([open-questions](open-questions.md) #9).

## Availability

| Built | Remaining | Status | Source |
|---|---|---|---|
| 122 trays | **61 trays** | in situ, no readout | Zhiwen, personal communication, 2026-11-09; matches "Half" in [star2026-detector-status-note](../../raw/star2026-detector-status-note.md) ✓ |

61 trays ≈ 30 m² of tray, ≈ 24.2 m² of strips, 1464 channels [note]. See [rhic-detector-status](rhic-detector-status.md).

## Related
[star-magnet-absorber](star-magnet-absorber.md) · [mrpc-technology](mrpc-technology.md) · [star-barrel-tof](star-barrel-tof.md) · [star-daq-trigger](star-daq-trigger.md) · [pi-mu-separation-calorimetry](pi-mu-separation-calorimetry.md) · [star-bemc](star-bemc.md) · [open-questions](open-questions.md)
