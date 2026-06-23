# Source review summary: 20260617T063957Z-lane05-8fad5bfe

- batch id: 20260617T063957Z-lane05-8fad5bfe
- rows reviewed: 160

## Verdict counts

- source_reviewed_candidate: 11
- merge_existing_surface: 22
- negative_evidence_candidate: 44
- needs_named_source_extraction: 73
- translation_review_needed: 3
- reject_noise: 7

## Boundary statement

Reviewed every input row once using only local TSV metadata and local source-path/snippet context. This batch is source-surface triage only: it does not infer incident truth, legality, compliance, safety, deployment, prevalence, comprehensiveness, or ranking.

## Next smallest queue-hardening move

Add pre-drain filters that route aggregate wrappers separately: existing public-ai-registry accession rows to `merge_existing_surface`, observability research queues/country profiles to named-source extraction, and explicit `no public`/`negative check`/weak-source rows to the negative-evidence lane before direct-source review leasing.
