# LIMEN methods/data article patch plan — 2026-06-14

Date: 2026-06-14
Lane: `limen-dashboard-paper-forge`
Primary manuscript surfaces: `draft/preprint.md`, `papers/article-architecture-v0.1.md`
Goal: turn LIMEN's observatory package into a bounded methods/data article without denominator drift or inflated edge-case claims

> For Hermes: treat this as a manuscript patch plan, not as a corpus-expansion plan.

## Article route

Lead route: LIMEN methods/data article centered on evidence architecture, denominator discipline, source-family governance, taxonomy support, and proof ceilings.

Safe title direction:
- LIMEN: a public-source observatory for AI edge cases under source, language, and governance uncertainty
- or equivalent wording that keeps the contribution on evidence architecture, not completeness

## Claim ceiling for the article

The article may claim:
- LIMEN is a structured public-source observatory for AI edge cases;
- the observatory keeps denominator classes, duplicate governance, source-family blockers, and legal/translation uncertainty visible;
- the dashboard and paper can share controlled figure/table surfaces;
- public evidence can support bounded accountability and observability claims without proving incident truth, legality, prevalence, compliance, or safety.

The article must not claim:
- total corpus completeness;
- incident prevalence or trend generalization;
- legal violation, non-compliance, certification, or official audit from weak public evidence;
- a single fused denominator across GAIA, PALLAS, and LIMEN;
- that Route C attestation equals external witness or trust assurance.

## Section-level manuscript edits

### 1. Introduction
Edit target:
- `draft/preprint.md` introduction/front-door framing

Required edits:
- Open with the observatory problem: edge-case corpora usually hide denominator drift, duplicate uncertainty, source heterogeneity, and translation/legal ceilings.
- State LIMEN's contribution as evidence architecture and reviewer-safe observability.
- Remove any wording that sounds like “largest corpus”, “broad coverage”, or implicit prevalence.

### 2. Related work and positioning
Edit target:
- `draft/preprint.md` related-work framing around incident databases, governance monitors, and provenance/attestation work

Required edits:
- Position LIMEN as a routing and control layer rather than a replacement for official documents, security registries, or incident databases.
- Keep comparator claims bounded to local control surfaces and explicit non-equivalence.

### 3. Data architecture and source-family method
Edit targets:
- `draft/preprint.md`
- `methods.md`

Required edits:
- Explain source families, thin-family blockers, and the difference between discovered material and publication-usable material.
- Name the live front door for source-family evidence: `results/dashboard/source-family-coverage.tsv`.
- Keep `sf08`, `sf09`, and `sf11` as visible blocker families rather than hidden deficiencies.

### 4. Duplicate governance and denominator discipline
Edit targets:
- `draft/preprint.md`
- figure/caption prose for Figure 4 and Figure 5

Required edits:
- Separate duplicate-governed records, publication-safe lineages, and figure-specific consumers.
- State clearly that Figure 4 is quality control, not recurrence evidence.
- State clearly that Figure 5 uses the `21` publication-safe-lineage denominator.

### 5. Taxonomy and category-support results
Edit targets:
- `draft/preprint.md` Figure 2 / Table 2 fragments
- `claims.md:LIMEN-C-016` as the claim ceiling anchor already in force

Required edits:
- Replace any ambiguous Figure 2 wording with the stabilized contract from `results/dashboard/taxonomy-heatmap.tsv`.
- Keep the live core `39 / 29`, the extended `44 / 34`, and the older mechanical `35 / 27` clearly separated.
- Emphasize zero-seed guardrails, overlay-ready slices, boxed comparators, appendix-nested subtypes, and queue-only pressure rather than “new categories discovered”.

### 6. Multilingual and public-sector asymmetry
Edit targets:
- `draft/preprint.md` multilingual and public-sector fragments

Required edits:
- Keep multilingual rows as evidence-maturity asymmetry, not comparative country readiness.
- Keep public-sector rows as disclosure-surface heterogeneity, not procurement proof or public-sector prevalence.
- Preserve translation-review burden and route blockage as results.

### 7. Security / agentic threshold section
Edit targets:
- `draft/preprint.md` security fragments

Required edits:
- Keep the package framed as publication-bucket asymmetry and threshold logic.
- Keep `results/dashboard/security-crosswalk-coverage-panel.tsv` explicit as Table C companion coverage, separate from Figure 7 threshold logic.
- Preserve the explicit gap state and do not flatten appendix/supporting rows into results-grade evidence.

### 8. Provenance / attestation section
Edit targets:
- `draft/preprint.md`
- any Route C summary paragraph

Required edits:
- Keep Route C companion-only.
- State local-bundle provenance only; no detached-signature, transparency, VC, or external witness claims.

### 9. Limitations
Edit target:
- `draft/preprint.md` limitations section

Required edits:
- Add a compact denominator paragraph covering Figure 2, Figure 5, and Figure 7 separately.
- Name source-family blocker order `sf08 -> sf09 -> sf11`.
- Keep translation dependence, authority imbalance, zero-seed categories, and stronger-witness absence explicit.

### 10. Conclusion
Edit target:
- `draft/preprint.md` conclusion

Required edits:
- Close on reusable evidence architecture and bounded observability.
- Do not close on completeness, prevalence, or generalized legal claims.

## Table / figure package for the article

Core package:
1. Figure 1 — source-family saturation map (`results/dashboard/source-family-coverage.tsv`)
2. Figure 2 — taxonomy support heatmap (`results/dashboard/taxonomy-heatmap.tsv`)
3. Figure 3 — legal uncertainty matrix (`results/dashboard/legal-uncertainty-matrix.tsv`)
4. Figure 4 — duplicate-review quality-control graph (`results/dashboard/duplicate-review-graph.tsv`)
5. Figure 5 — publication-safe evidence-tier funnel (`results/dashboard/evidence-funnel.tsv`)
6. Figure 6 — jurisdiction/language visibility map (`results/dashboard/jurisdiction-language-coverage.tsv`)
7. Table A — authoritative document-depth facet (`results/dashboard/authoritative-document-depth-facet.tsv`)
8. Table B — public-sector disclosure asymmetry comparison (`results/dashboard/public-sector-disclosure-comparison.tsv`)

Bounded companions only:
9. Table C — security / agentic crosswalk coverage (`results/dashboard/security-crosswalk-coverage-panel.tsv`)
10. Figure 7 — security threshold ladder (`results/dashboard/security-threshold-ladder-panel.tsv`)
11. Figure 8 — attestation trust-surface readiness (`results/dashboard/attestation-trust-surface-readiness.tsv`)

## What must stay out of the main denominator story

- CPU-mining lead counts
- screenshot numerals without a local source file
- boost-local Figure 2 mechanical counts treated as present-tense truth
- Figure 7 sidecar projections treated as default live panel values
- public-sector or multilingual sidecars silently promoted into the core table denominator

## Next 24-hour work queue

1. Patch the preprint's Figure 2 and limitations prose so the denominator split is explicit and stable.
2. Add one compact “denominator classes” methods paragraph covering Figure 2, Figure 5, and Figure 7.
3. Tighten the introduction and conclusion around observability/evidence architecture rather than corpus scope.
4. Verify every figure/table caption against the corresponding `results/dashboard/*.tsv` source path.
5. Keep Route B and Route C as bounded companions; do not widen them into the main claim spine.
6. If there is time after prose stabilization, prepare one reviewer-facing appendix note summarizing `sf08`, `sf09`, and `sf11` as the main remaining stronger-source blockers.

## Stop rule for this patch plan

Do not reopen crawling or boost work from this plan. The next move after this plan is manuscript patching against the existing local package, not corpus growth.
