# Source review summary — 20260614T0830Z

Batch input: `source-review-input.tsv`
Rows reviewed: 100
Method boundary: local metadata and local source files only; no broad web crawling used.

## Verdict counts

- `source_reviewed_candidate`: 13
- `merge_existing_surface`: 21
- `negative_evidence_candidate`: 23
- `needs_named_source_extraction`: 22
- `translation_review_needed`: 6
- `reject_noise`: 15

## Reviewer-safe interpretation

- The batch contains a minority of rows that are already close to bounded direct-source promotion (`source_reviewed_candidate`: 13). These remain source-surface candidates only, not reviewed-core examples and not evidence of incident truth, legality, compliance, deployment, prevalence, or rank.
- Many rows are better treated as negative/gap evidence (`negative_evidence_candidate`: 23) or as placeholders that still need a named source extracted from adjacent local source packs (`needs_named_source_extraction`: 22).
- `merge_existing_surface` rows (21) mostly duplicate surfaces already modeled in registry/atlas/local resolution artifacts and should be deduplicated rather than re-promoted.
- `translation_review_needed` rows (6) identify named official surfaces whose current local snippets are materially non-English; safe ceiling is source-surface existence plus original-language title until translation-aware review.
- `reject_noise` rows (15) came from scripts, manuscript prose, config, or other derived/internal artifacts and should not remain in the direct-source queue.

## Observatory hook

- Feed `source_review_verdict`, `source_review_role`, and `claim_ceiling` into LIMEN dashboard/paper parity tables as a source-resolution sidecar for Figure/denominator discipline.
- Treat `negative_evidence_candidate` and `needs_named_source_extraction` as separate funnel stages so the observatory can distinguish "search-negative/gap evidence" from "candidate still lacks named source."

## Next smallest publishability move

- Prioritize the 13 `source_reviewed_candidate` rows and 6 `translation_review_needed` rows for reviewed-core triage or translation-aware hardening; separately purge the 15 `reject_noise` rows from future direct-source batches.
