# LIMEN introduction and related-work assembly note

Date (UTC): 2026-06-17T15:15:00Z
Lane: `limen-dashboard-paper-forge`
Patch-plan items addressed: 1 (Introduction) and 2 (Related Work and Positioning)

## What was done

Patched `draft/preprint.md` to add two new front-door sections and renumber
the remaining manuscript body:

1. **Section 1 — Introduction** (new). Opens with the observatory problem:
   edge-case corpora hide denominator drift, duplicate uncertainty, source
   heterogeneity, and translation/legal ceilings. States LIMEN's threefold
   contribution: (a) structured public-source observatory with shared
   dashboard/paper figure package; (b) explicit observability surfaces for
   source-family saturation, duplicate governance, legal uncertainty,
   multilingual visibility, security routing, and provenance limits;
   (c) bounded accountability arguments as publishable contributions.
   Names the three-observatory context (GAIA/PALLAS/LIMEN) without fusing
   denominators.

2. **Section 2 — Related Work and Positioning** (new). Positions LIMEN as a
   routing and control layer, not a replacement for existing databases.
   Covers four comparator groups:
   - Incident databases (AIID, MIT AI Risk, CSET AI Harm)
   - Governance observatories (OECD AIM, AVID)
   - Security taxonomies (MITRE ATLAS, NIST AI RMF, EU AI Act, ISO/IEC 42001)
   - Provenance standards (C2PA/HASH, EU AI Act Art. 50)
   Keeps all comparator claims bounded to local control surfaces and
   explicit non-equivalence.

3. **Section renumbering**. Renamed `## Methods/Data Package Framing` to
   `## 3. Observatory Architecture and Methods`. Created `## 4. Results:
   Evidence Architecture Surfaces` as the parent for all shard fragments
   (003, 004, 007, 008, 009, 010), public-sector, multilingual, and
   security claim-ceiling fragments. Numbered `## 5. Limitations` with
   subsections 5.1–5.7 and `## 6. Conclusion`.

## Paper-readiness delta

- The manuscript now has a proper academic front door: Introduction states
  the problem, the contribution, and the positioning; Related Work names
  six comparator surfaces with bounded claims.
- A hostile reviewer can read sections 1–2 and understand what LIMEN claims,
  what it does not claim, and how it differs from existing databases.
- The section structure (1–6) now matches standard journal article format.
- No denominator was changed, no new collection was performed, no claim
  ceiling was relaxed.

## Remaining patch-plan items

| Item | Status |
|------|--------|
| 1. Introduction | Done this cycle |
| 2. Related work | Done this cycle |
| 3. Data/source-family method | Partially addressed (Section 3 covers architecture; sf08/sf09/sf11 blockers named in 5.2) |
| 4. Duplicate governance / denominator discipline | Done in prior cycles (3.1 + 5.1) |
| 5. Taxonomy results | Done in prior cycles (shard 010 + 5.5) |
| 6. Multilingual / public-sector | Done in prior cycles (Section 4 subsections) |
| 7. Security threshold | Done in prior cycles (shard 004 + security claim-ceiling) |
| 8. Provenance/attestation | Done in prior cycles (5.6) |
| 9. Limitations | Done in prior cycles (Section 5) |
| 10. Conclusion | Done in prior cycles (Section 6) |

## What still needs work

- Inline appendix prose for shards 007, 008, 004 still uses boost-local-first
  sentence structure in places. A shared-control-first rewrite of those
  paragraphs would improve readability but does not change any denominator
  or claim.
- A venue-specific variant (e.g., data-descriptor format for Scientific Data,
  or governance-article format for AI & Ethics) has not yet been prepared.
- The abstract section is still in `papers/article-architecture-v0.1.md` as
  a starter, not yet integrated into the preprint front matter.

## Stop rule

No crawling, boost, or denominator expansion from this note.
