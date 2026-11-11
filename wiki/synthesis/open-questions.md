---
title: Open questions
tags: [overview, status]
sources: [ruan2009-mtd-concept.md, ruan2009-mtd-concept-note.md, yang2014-mtd-cosmic-calibration.md, yang2014-mtd-cosmic-calibration-note.md, huang2016-mtd-muon-id.md, huang2016-mtd-muon-id-note.md, llope2012-star-mrpc-systems.md, llope2012-star-mrpc-systems-note.md, shao2002-mrpc-beam-test.md, shao2002-mrpc-beam-test-note.md, wu2007-star-barrel-tof.md, wu2007-star-barrel-tof-note.md, wang2024-star-forward-upgrade.md, wang2024-star-forward-upgrade-note.md, gagliardi2022-star-forward-upgrade-talk.md, gagliardi2022-star-forward-upgrade-talk-note.md, ruan2026-fcs-specs-email.md, ruan2026-fcs-specs-email-note.md, schambach2006-star-tof-electronics.md, schambach2006-star-tof-electronics-note.md]
updated: 2026-11-10
---

# Open questions

Unresolved items carried over from the pre-wiki notes (numbering kept from the old open-issue list; items 1–8 and 10 were closed on 2026-11-05; #16 added 2026-11-10).

| # | Topic | Issue | Next step |
|---|---|---|---|
| 9 | Strip signal speed ([[mrpc-technology]]) | 15–18 cm/ns is from memory; none of the seven STAR MRPC papers states it | check Sun et al., NIM A 593 (2008) 307, or Wang et al., NIM A 640 (2011) 85 |
| 11 | MTD 56% coverage ([[star-mtd]]) | 2009 plan: 56% of 2π ⇒ ≈ 47 cm active width per bar, vs ≈ 75% for the full bar faces (geometry and Fig. 2); 540 modules ≈ 80 m² vs ≈ 96 m² implied by 56% × \|η\| < 0.8 [[ruan2009-mtd-concept-note]] | unexplained in the paper; check the MTD proposal (2010) |
| 12 | Run-12 MTD z resolution ([[star-mtd]], [[mrpc-technology]]) | type-B z = 2.6 cm equals the raw Fig. 5 width; unclear whether corrected for multiple scattering [[yang2014-mtd-cosmic-calibration-note]] | unresolvable from the paper; use Run-11 values |
| 13 | TOF construction details ([[star-barrel-tof]]) | missing from the papers: MRPC outer size, inter-pad gap, MRPC tilt angles. Tray size (2.4 m × 21 cm) is Zhiwen, personal communication, 2026-11-09, not a paper; pad orientation (3.5 cm in φ, 6.1 cm along z) is inferred from it. [[schambach2006-star-tof-electronics-note]] (2006) adds only the tray wall (50 mil Al) and none of the missing items | STAR TOF proposal (2004; Llope 2012 ref. [3]; URL in Schambach 2006 ref. [1]: http://www.star.bnl.gov/STAR/tof/publications/TOF_20040524.pdf) or a dedicated TOF construction paper |
| 14 | MTD DAQ path ([[star-daq-trigger]]) | the MTD's path into STAR DAQ and its trigger boards are not stated in any paper | Landgraf 2003 (NIM A 499 762), Bieser 2003 (NIM A 499 766), Landgraf 2013 talk (indico 246374/542866) |
| 15 | FCS discrepancies ([[star-fcs]]) | ECal tower length 33 cm (talk) vs 37.73 cm (email); ECal depth 0.85 vs 0.93 λ; SiPMs on the "front face" (Wang 2024) vs fibres read at the back (email); no measured resolution | PHENIX PbSc documentation; an FCS NIM paper if one exists |
| 16 | TOF MRPC dimensions ([[star-barrel-tof]], [[mrpc-technology]]) | pad width **3.3 cm** ([[schambach2006-star-tof-electronics-note]]: 3.3 cm × 6.1 cm) vs **3.5 cm** ([[llope2012-star-mrpc-systems-note]]: 3.5 × 6.1 cm²); outer glass 0.7 mm vs 1.1 mm, inner 0.55 vs 0.54 mm (same two sources). Both papers share an author; neither explains the difference. The 2006 paper is a design, Llope 2012 the as-built system, but no source says the dimensions changed. Pad orientation inference holds for either width (19.8 or 21 cm across); σ across ≈ 0.95 vs 1.01 cm [note] | STAR TOF proposal (2004, URL in #13); a TOF MRPC production/QA paper; a hardware measurement |

## Unverified items stated from memory [note]
To be confirmed before quoting; none is in any raw source.
- MTD front-end board called "MINO" (NINO-based TINO variant) — [[mrpc-technology]].
- MTD shares the TOF THUB/DDL path into DAQ; trigger via STAR QT boards — [[star-daq-trigger]] (#14).
- "122 MTD modules on 27 backlegs": the 122 count is now confirmed (Zhiwen, personal communication, 2026-11-09); the backleg count is not — [[star-mtd]].
- STAR magnet geometry should be confirmed against Bergsma et al., NIM A 499 (2003) 633 (not ingested) — [[star-magnet-absorber]].

## Scope gap
Only STAR systems have been read. The other RHIC detectors on the SoLID wiki *RHIC detectors* page (https://solid.jlab.org/wiki/index.php?title=RHIC_detectors) are not yet listed or ingested ([[rhic-detector-status]]).

## Related
[[rhic-detector-status]] · [[star-mtd]] · [[star-barrel-tof]] · [[star-fcs]] · [[star-daq-trigger]] · [[mrpc-technology]]
