# CULTURETECHLENS

**"Culture, Clearly Seen."**

**Black Cultural Intelligence**

---

## CTL Black Cultural Knowledge Graph — Seed (CTL-KG-CORE-001)

The data backbone of CultureTechLens — Black cultural-intelligence infrastructure rooted in Chicago. Every CTL research lens feeds this shared graph; it is designed to grow append-only as the flagship research packages merge in.

## What is here

| File | Contents |
|---|---|
| `schema.json` | Entity types, relationship types, required fields, ID scheme, verification rules |
| `entities.json` | 300 seed entities, IDs `CTL-E-0001` … `CTL-E-0300` |
| `relationships.json` | Verified-only edges (see count below) |
| `validate.py` | Validates entities + relationships against the schema |

## Seed contents

- **300 entities**: 124 Person · 22 Venue · 10 Church · 8 School · 24 Institution · 6 RadioStation · 7 Business · 3 Archive · 20 Neighborhood · 14 Address · 27 Event · 10 Publication · 10 Work · 15 Organization
- **290 Verified / 10 Provisional** entities (Provisional = believed correct, some detail uncertain — never invented)
- **224 verified-only edges** across 18 relationship types
- Seven flagship projects represented: BCI-001, BMI-002, BPM-003, SCI-004, BVM-005, PLACE-001, MUSIC-001

## On the edge count

The seed aimed for 300–500 edges; it ships with 224 verified-only edges. That gap is deliberate: enrichment and curator passes exhausted the honestly-verifiable relationships inside this 300-entity seed, and the standing rule — *never invent facts or relationships* — outranks the numeric target. Growth comes through the merge path: each flagship research package contributes entity and relationship fragments that add verified edges as they land. `validate.py` warns (not fails) while the edge count is under 300.

## Schema summary

**Entity types** (19): Person, Institution, Venue, Business, Publication, Church, School, Neighborhood, Address, Event, Work, Organization, Technology, Archive, RadioStation — plus reserved `Policy` and `Migration` (defined for research-package use; no seed instances).

**Relationship types** (21), each with fixed from/to type constraints — see `schema.json` for the full list. Highlights: `affiliated_with`, `associated_with`, `located_in`, `performed_at`, `founded_by`, `organized`, `has_alumnus`, `wrote_for`, `hosted`, `archived_at`, `held_at`, `collaborated_with`, `recorded_for`, `nurtured`, `samples`, `played`, `distributed_by`, `initiated`, `related_to` (+ reserved `impacted_by`, `migration_link`).

**Required entity fields**: `id`, `type`, `name`, `aliases`, `description`, `era`, `project_ids`, `verification`, `sources`. Optional: `subtype`, `notes`.

**Required relationship fields**: `from`, `to`, `type`, `evidence`, `source`, `verification`. Every edge must be traceable to evidence — when in doubt, leave it out.

## How to add to the graph (append-only convention)

1. **Mint IDs from the next free number.** The seed occupies `CTL-E-0001`–`0300`; continue at **`CTL-E-0301`**. IDs are never reused or renumbered.
2. **Dedupe first.** Match incoming entities against existing `name` + `aliases` (case-insensitive, canonical names win over aliases). On a match, merge into the surviving entity: union aliases, project_ids, and sources; keep the surviving ID; never reassign the retired ID.
3. **Grade verification honestly.** `Verified` = well documented. `Provisional` = believed correct with some uncertainty. Never invent facts, dates, addresses, or relationships to fill gaps.
4. **Edges are verified-only.** Each needs `evidence` (1–2 sentences) and a `source`. No edge without evidence.
5. **Run `python3 validate.py`** before committing. Zero errors required.

## Evidence statuses

Entities and relationships are graded: VERIFIED · SUPPORTED · PROVISIONAL · DISPUTED · UNRESOLVED · REFUTED · UNVERIFIABLE. Unknowns are never zero — UNKNOWN, NOT APPLICABLE, NOT YET RESEARCHED, and NOT PUBLICLY AVAILABLE are statements about the record, not gaps in it.

## How to cite

> CultureTechLens NFP, "CTL Black Cultural Knowledge Graph — Seed (CTL-KG-CORE-001)," 2026-09-28.

## License

- All data files (JSON) and documentation (Markdown): Creative Commons Attribution 4.0 International (CC BY 4.0). You may share and adapt with attribution to CultureTechLens.
- All code (including `validate.py`): MIT License.

Copyright 2026 CultureTechLens NFP (EIN 39-3143901).

---

*CULTURETECHLENS · "Culture, Clearly Seen." · Black Cultural Intelligence*
