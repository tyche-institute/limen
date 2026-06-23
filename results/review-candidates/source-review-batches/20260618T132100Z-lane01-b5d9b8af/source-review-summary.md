# Source review summary: 20260618T132100Z-lane01-b5d9b8af

- batch id: 20260618T132100Z-lane01-b5d9b8af
- rows reviewed: 160

## Verdict counts

| verdict | count |
|---|---:|
| source_reviewed_candidate | 66 |
| merge_existing_surface | 13 |
| negative_evidence_candidate | 1 |
| needs_named_source_extraction | 4 |
| translation_review_needed | 48 |
| reject_noise | 28 |

## Boundary statement

This was source-surface triage only, using local row metadata and local source files/paths. No broad web crawl and no public, portal, upload, email, submission, payment, deployment, or registration actions were taken. Verdicts do not infer incident truth, legality, compliance, safety, deployment, prevalence, or ranking.

## Next smallest queue-hardening move

Add a pre-source-review filter that removes internal package/prose/schema/figure artifacts and collapses aggregate registry-surface rows into existing surface models before leasing, while routing rows containing `English auto-translation from Dutch` directly to the translation-review queue.
