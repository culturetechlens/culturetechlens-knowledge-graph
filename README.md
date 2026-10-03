# CULTURETECHLENS

**"Culture, Clearly Seen."**

**Black Cultural Intelligence**

---

## CTL Black Cultural Knowledge Graph (CTL-KG-CORE-001)

The data backbone of CultureTechLens — Black cultural-intelligence infrastructure rooted in Chicago. Every CTL research lens feeds this shared graph; it is designed to grow append-only as the flagship research packages merge in.

**Current release (2026-10-03): 765 entities · 271 relationships.** This release promotes the full verified tier of the CultureTechLens master graph (1,441 entities) to the public graph — up from the 300-entity seed of 2026-09-28 — and folds in the Marcus Freeman dossier (CTL-RD-PER-000002) entities, including Freeman himself (CTL-E-1412).

## What is here

| File | Contents |
|---|---|
| `schema.json` | Entity types, relationship types, required fields, ID scheme, verification rules |
| `entities.json` | 765 entities, IDs `CTL-E-0001` … `CTL-E-1421` |
| `relationships.json` | 271 evidence-backed edges (see note below) |
| `validate.py` | Validates entities + relationships against the schema |

## Contents

- **765 entities**: 271 Person · 89 Organization · 87 Institution · 61 Event · 34 Address · 33 Venue · 29 Business · 29 Neighborhood · 26 Church · 25 Archive · 21 Practice · 18 School · 18 Publication · 10 Work · 7 Policy · 6 RadioStation · 1 Technology
- **754 Verified / 11 Provisional** entities (Provisional = believed correct, some detail uncertain — never invented)
- **271 edges** across 29 relationship types, every edge traceable to named evidence
- Nineteen research projects represented, from the seven founding flagships (BCI-001, BMI-002, BPM-003, SCI-004, BVM-005, PLACE-001, MUSIC-001) to the Freeman person dossier (PER-000002)

## On the edge count

The graph ships 271 edges, below the 300–500 working target. That gap is deliberate: every edge must trace to evidence, and the standing rule — *never invent facts or relationships* — outranks the numeric target. `validate.py` warns (not fails) while the edge count is under 300. Growth comes through the merge path: each flagship research package contributes entity and relationship fragments that add verified edges as they land.

## Schema summary

**Entity types** (18): Person, Institution, Venue, Business, Publication, Church, School, Neighborhood, Address, Event, Work, Organization, Technology, Archive, RadioStation, Practice, Policy, Migration.

**Relationship types** (33 in schema; 29 in use), each with fixed from/to type constraints — see `schema.json` for the full list. Highlights: `affiliated_with`, `associated_with`, `located_in`, `performed_at`, `founded_by`, `organized`, `has_alumnus`, `wrote_for`, `hosted`, `archived_at`, `held_at`, `collaborated_with`, `recorded_for`, `nurtured`, `samples`, `played`, `distributed_by`, `initiated`, `related_to`, plus sports-career types added with the Freeman dossier (`head_coach_of`, `drafted_by`, `played_for`, and kin).

**Required entity fields**: `id`, `type`, `name`, `aliases`, `description`, `era`, `project_ids`, `verification`, `sources`. Optional: `subtype`, `notes`.

**Required relationship fields**: `from`, `to`, `type`, `evidence`, `source`, `verification`. Every edge must be traceable to evidence — when in doubt, leave it out.

## How to add to the graph (append-only convention)

1. **Mint IDs from the next free number.** The public graph currently runs to `CTL-E-1421`; continue at **`CTL-E-1422`**. IDs are never reused or renumbered.
2. **Dedupe first.** Match incoming entities against existing `name` + `aliases` (case-insensitive, canonical names win over aliases). On a match, merge into the surviving entity: union aliases, project_ids, and sources; keep the surviving ID; never reassign the retired ID.
3. **Grade verification honestly.** `Verified` = well documented. `Provisional` = believed correct with some uncertainty. Never invent facts, dates, addresses, or relationships to fill gaps.
4. **Edges carry evidence.** Each needs `evidence` (1–2 sentences) and a `source`. No edge without evidence.
5. **Run `python3 validate.py`** before committing. Zero errors required.

## Evidence statuses

Entities and relationships are graded: VERIFIED · SUPPORTED · PROVISIONAL · DISPUTED · UNRESOLVED · REFUTED · UNVERIFIABLE. Grading provenance is preserved where a source package's grades differ from the graph's two-level publication scale. Unknowns are never zero — UNKNOWN, NOT APPLICABLE, NOT YET RESEARCHED, and NOT PUBLICLY AVAILABLE are statements about the record, not gaps in it.

## How to cite

> CultureTechLens NFP, "CTL Black Cultural Knowledge Graph (CTL-KG-CORE-001)," promoted release, 2026-10-03.

## License

- All data files (JSON) and documentation (Markdown): Creative Commons Attribution 4.0 International (CC BY 4.0). You may share and adapt with attribution to CultureTechLens.
- All code (including `validate.py`): MIT License.

Copyright 2026 CultureTechLens NFP (EIN 39-3143901).

---

*CULTURETECHLENS · "Culture, Clearly Seen." · Black Cultural Intelligence*
