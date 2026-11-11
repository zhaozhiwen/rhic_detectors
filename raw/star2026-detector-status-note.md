---
title: "STAR 2026 — STAR Detector status as of October 2026 (curated notes)"
type: raw-note
source_type: status-sheet
companion: star2026-detector-status.md
authors: not given
venue: "one-page status sheet, PDF created 2026-10-22"
doi: none
arxiv: none
notes_updated: 2026-11-09
ingested_version: "one-page PDF (assets/star2026-detector-status/source.pdf, created 2026-10-22), supplied by the repo author; transcribed 2026-11-09"
earlier_version: []
later_version: []
published_version: "none -- internal status sheet, not peer-reviewed; published in this repo with Zhiwen's agreement"
version_facts: "Heading: 'STAR Detector status as of October 2026'. No author, issuing body or document number printed. Zhiwen stated on 2026-11-09 that 112 barrel-TOF trays and 61 MTD trays remain."
versions_checked: 2026-11-09
---

# STAR Detector Status, October 2026 — Curated Notes

> **Full source:** [star2026-detector-status](star2026-detector-status.md) · Companion notes to [star2026-detector-status](star2026-detector-status.md) (full source).
> **Links:** no DOI (status sheet) · **PDF:** `assets/star2026-detector-status/source.pdf`

## Bibliographic / source

- **Title:** STAR Detector status as of October 2026
- **Author / issuer:** not given. PDF created 2026-10-22.
- **Form:** one page, one three-column table (Detector / Availability / Status) grouped under Trigger, Very Forward, Forward and Central detectors.

## What kind of source

Internal status sheet — **not peer-reviewed**; internal/collaboration material published with Zhiwen's agreement. Terse; gives availability and physical state of STAR subsystems after data taking, with no explanation, numbers or dates beyond "as of October 2026" and "Last used in 2017".

## Summary (paraphrased)

Inventory of what remains of each STAR subsystem in October 2026 and whether it is still in place, dismounted, stored or returned. Most calorimeters and the central detectors remain in situ, several without readout; some trigger and forward detectors are dismounted, stored, disposed of, or packed for return to their home institutions.

## Key numbers — every detector

| Group | Detector | Availability | Status |
|---|---|---|---|
| Trigger | BBC | (blank) | Disposed |
| Trigger | VPD | All | Radiation surveyed and stored |
| Trigger | EPD | All | Dismounted, packed, ready to be returned to Ohio |
| Very forward | ZDC | All | In situ |
| Very forward | ZDC SMD | All | Radiation surveyed and stored |
| Very forward | Roman pots | All | Last used in 2017; stored |
| Forward | Forward EMCal (FCS ECal) | All | In situ |
| Forward | Forward HCal (FCS HCal) | All | In situ |
| Forward | sTGC | All | Dismounted |
| (after blank row) | Endcap EMCal | All | In situ; no readout |
| (after blank row) | Endcap TOF | All | Dismounted, packed, ready to be returned to Germany |
| (after blank row) | FST | One of two halves (3 layers) | Dismounted |
| Central | TPC | All | In situ |
| Central | Barrel TOF | All except 8 trays | In situ; no readout |
| Central | MTD | Half | In situ; no readout |
| Central | Barrel EMCal | All | In situ; no readout |

- **Tray counts (Zhiwen, stated 2026-11-09):** 112 barrel-TOF trays and 61 MTD trays remain. Consistent with "All except 8 trays" (112 + 8 = 120 trays, the full barrel TOF per Zhiwen's tray count) and "Half" (61 of 122 MTD trays, per Zhiwen's tray count).
- **[note]** Grouping by status: in situ with no readout — Endcap EMCal, Barrel TOF, MTD, Barrel EMCal; in situ, readout not mentioned — ZDC, Forward EMCal, Forward HCal, TPC; dismounted — sTGC, FST (one half), EPD, Endcap TOF; stored — VPD, ZDC SMD, Roman pots; disposed — BBC.

## What it does not give

- No reason for "no readout" (electronics removed, disconnected or reassigned is not said); no readout statement for ZDC, FCS and TPC.
- No destination or owner for in-situ detectors; no dates for dismounting; no author or issuing body.
- Which 8 BTOF trays and which half of the MTD remain/are missing is not stated.

## Source issues and caveats

- Empty row between "sTGC" and "Endcap EMCal" with no section heading; so the grouping of Endcap EMCal, Endcap TOF and FST is ambiguous. **[note]** The FST is a forward-upgrade tracker ([wang2024-star-forward-upgrade-note](wang2024-star-forward-upgrade-note.md)), so the block probably continues "Forward Detectors".
- BBC availability cell is empty.
- **[note]** "FST: One of two halves (3 layers)" read together with the 3-disk FST of [wang2024-star-forward-upgrade-note](wang2024-star-forward-upgrade-note.md) suggests one half of each of the 3 disks remains; the sheet does not say so.
- **[note]** "Forward EMCal" and "Forward HCal" are taken to be the FCS ECal and HCal ([ruan2026-fcs-specs-email-note](ruan2026-fcs-specs-email-note.md)); the sheet uses no acronym.
- Not peer-reviewed; internal/collaboration material published with Zhiwen's agreement.

## Relevance

Current-state anchor for [rhic-detector-status](../wiki/synthesis/rhic-detector-status.md): tells which STAR hardware still physically exists in October 2026 — the barrel TOF (minus 8 trays), half the MTD, the BEMC and EEMC remain in situ without readout; the FCS calorimeters remain in situ; the FST (one half) and sTGC are dismounted. Feeds the hardware-availability sections of [star-barrel-tof](../wiki/synthesis/star-barrel-tof.md), [star-mtd](../wiki/synthesis/star-mtd.md), [star-bemc](../wiki/synthesis/star-bemc.md), [star-eemc](../wiki/synthesis/star-eemc.md), [star-fcs](../wiki/synthesis/star-fcs.md) and the trigger-detector context in [star-daq-trigger](../wiki/synthesis/star-daq-trigger.md).

## Related

- Synthesis: [rhic-detector-status](../wiki/synthesis/rhic-detector-status.md) · [star-barrel-tof](../wiki/synthesis/star-barrel-tof.md) · [star-mtd](../wiki/synthesis/star-mtd.md) · [star-bemc](../wiki/synthesis/star-bemc.md) · [star-eemc](../wiki/synthesis/star-eemc.md) · [star-fcs](../wiki/synthesis/star-fcs.md) · [star-daq-trigger](../wiki/synthesis/star-daq-trigger.md) · [mrpc-technology](../wiki/synthesis/mrpc-technology.md) · [open-questions](../wiki/synthesis/open-questions.md)
- Notes: [wu2007-star-barrel-tof-note](wu2007-star-barrel-tof-note.md) · [llope2012-star-mrpc-systems-note](llope2012-star-mrpc-systems-note.md) · [ruan2009-mtd-concept-note](ruan2009-mtd-concept-note.md) · [huang2016-mtd-muon-id-note](huang2016-mtd-muon-id-note.md) · [beddo2003-bemc-note](beddo2003-bemc-note.md) · [star2003-eemc-note](star2003-eemc-note.md) · [wang2024-star-forward-upgrade-note](wang2024-star-forward-upgrade-note.md) · [gagliardi2022-star-forward-upgrade-talk-note](gagliardi2022-star-forward-upgrade-talk-note.md) · [ruan2026-fcs-specs-email-note](ruan2026-fcs-specs-email-note.md)
