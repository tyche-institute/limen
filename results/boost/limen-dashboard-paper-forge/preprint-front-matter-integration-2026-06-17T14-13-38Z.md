# LIMEN preprint front-matter integration and residue verification

Timestamp (UTC): 2026-06-17T14:13:38Z
Lane: `limen-dashboard-paper-forge`
Project: `limen-ai-edge-case-atlas`
Sprint posture: hostile-reviewer manuscript-assembly pass; bounded stabilization only.

## Action taken

Integrated the Route A abstract starter from `papers/article-architecture-v0.1.md`
into `draft/preprint.md` as proper front matter: title, authors, date, keywords,
and a self-contained abstract that names the key denominators and the reviewed-core
demonstration without overreaching.

Also resolved the last remaining `Table 1F` legacy slot reference in the
provenance-confusion shard prose (replaced with `appendix-grade provenance-confusion
reuse`) so that no front-door manuscript sentence now uses a legacy `Table 1*`
or `Table 6*` label.

## Verified preprint state after this cycle

| Metric | Before (2026-06-17T15:15:00Z) | After (2026-06-17T14:13:38Z) |
| --- | --- | --- |
| Total lines | 308 | 345 |
| `Table 1[A-Z]` references | 1 | 0 |
| `Table 6[A-Z]` references | 0 | 0 |
| `results/boost/` path lines | 13 | 11 |
| Top-level shard headings (`### Shard`) | 0 | 0 |
| Section headings (`## N.`) | 6 | 6 |
| Has abstract section | No | Yes |
| Has title/authors/keywords | No | Yes |

## Front matter added

- **Title:** LIMEN: A Public-Source Observatory for AI Edge Cases under Source, Language, and Governance Uncertainty
- **Authors:** Anton Sokolov (Tyche Institute)
- **Version:** v0.4
- **Keywords:** AI edge cases, evidence architecture, denominator discipline, source-family governance, duplicate governance, legal uncertainty, multilingual visibility, security crosswalk, provenance limits, observatory methods
- **Abstract:** ~180 words, names the 15-category taxonomy with 39/29 core denominator, the 44/34 extended sidecar, the 21 publication-safe lineages, the 27-edge duplicate graph, the 15-row source-family map, the 12-row jurisdiction/language surface, bounded companions, and the reviewed-core 248-case demonstration. Does not claim completeness, prevalence, legality, compliance, or safety.

## Denominator discipline preserved

- Figure 2: `39 governed record refs / 29 unique lineages` core, `44 / 34` extended sidecar — unchanged.
- Figure 5: `21 publication-safe lineages` — unchanged.
- Figure 7: `4 threshold rows` — unchanged.
- Reviewed-core: `248 evidence-grade cases / 32 jurisdictions` — unchanged, only now named in abstract.
- No denominator was widened, merged, or collapsed.

## Remaining boost-path references

11 lines still reference `results/boost/` paths. These are legitimate
appendix-grade provenance citations in the shard result prose (shards 003, 004,
007, 008, 009, 010, sf09). They document the exact local evidence bundles that
support each shard's bounded claim. They do not need removal because they are
the methods/results trail a reviewer would follow. The article architecture
already distinguishes front-door shared surfaces (Figure 1-8, Table A-C) from
appendix-grade shard provenance bundles.

## Paper-readiness delta

| Dimension | Before | After |
| --- | --- | --- |
| Front matter completeness | Missing title, abstract, keywords | Complete |
| Legacy slot label residue | 1 Table 1F in shard prose | 0 legacy labels in front-door prose |
| Reviewer first-impression | Opens on shard method | Opens on proper abstract and introduction |
| Venue submission readiness | Needs front matter | Can be adapted to venue template |

## Next smallest publishability move

1. Adapt the front matter to one specific venue template (e.g., Scientific Data
   data-descriptor format or AI & Ethics governance-article format).
2. Consider extracting the reviewed-core 248-case panel (Claim C8) into a
   standalone figure or supplementary table for the abstract.
3. Continue appendix-depth shard-prose normalization (boost-local-first sentence
   structure in shards 007, 008, 004) — readability improvement only, no
   denominator change.

## Claim boundaries preserved

- No completeness, prevalence, or generalized legality claim.
- No fused GAIA/PALLAS/LIMEN denominator.
- No external trust assurance or Route C witness-state upgrade.
- sf08, sf09, sf11 blockers unchanged.
