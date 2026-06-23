# Source review summary: 20260617T063958Z-lane07-37ff080b

- Batch id: 20260617T063958Z-lane07-37ff080b
- Rows reviewed: 160

## Verdict counts
- needs_named_source_extraction: 104
- negative_evidence_candidate: 46
- reject_noise: 2
- source_reviewed_candidate: 6
- translation_review_needed: 2

## Boundary statement
This bounded source-surface triage used only local row metadata and local source-path context available in the batch inputs. It did not infer incident truth, legality, compliance, safety, deployment, prevalence, or ranking, and it did not perform broad web crawling or any public/portal action.

## Next smallest queue-hardening move
Pre-filter generated research queues, atlas/index/profile wrappers, and warning-section headings into `needs_named_source_extraction` or `negative_evidence_candidate` before leasing direct-source review batches; reserve the direct-source queue for rows with an explicit named source title, issuing body, and URL/local locator.
