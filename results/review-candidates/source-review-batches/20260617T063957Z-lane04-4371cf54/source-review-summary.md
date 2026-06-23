# Source review summary: 20260617T063957Z-lane04-4371cf54

- batch id: 20260617T063957Z-lane04-4371cf54
- rows reviewed: 160

## Verdict counts

- source_reviewed_candidate: 16
- merge_existing_surface: 47
- negative_evidence_candidate: 47
- needs_named_source_extraction: 44
- translation_review_needed: 6
- reject_noise: 0

## Boundary statement

This batch used only local row metadata and local source-path context for source-surface triage. It does not infer incident truth, legality, compliance, safety, deployment, prevalence, ranking, or substantive source claims beyond whether the local row exposes a reviewable source surface or a bounded negative/gap artifact.

## Next smallest queue-hardening move

Deduplicate already-modeled Canada/Dutch registry accession rows before leasing and split wrapper/gap rows into separate queues: one for bounded negative evidence and one for named-source extraction from country profiles/source packs.
