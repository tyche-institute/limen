# Bulk translation review summary: 20260618T132345Z-lane3-db95949b

Completed: 2026-06-18T13:24:46Z

Input: `/srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/bulk-review-batches/bulk-translation-review/20260618T132345Z-lane3-db95949b/input.tsv`
Results: `/srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/bulk-review-batches/bulk-translation-review/20260618T132345Z-lane3-db95949b/bulk-translation-review-results.tsv`

## Scope

Reviewed 16 input rows exactly once using local metadata and local source files only. No web crawl, portal use, submission, upload, publication, email, payment, legal finding, safety finding, compliance finding, prevalence claim, ranking, reviewed-core promotion, or ObscureAI addition was made.

## Verdict counts

- cross_project_duplicate: 12
- needs_original_language_source: 1
- translation_source_reviewed: 3

## Review notes

- The batch is dominated by Dutch Algorithm Register rows whose local artifacts explicitly say `English auto-translation from Dutch`.
- Concrete local source-surface records reviewed: Zylab Disclosure Support, Datamask, and Octobox Anonymisation.
- One accession-only row (`Sounding language`) lacks original-language source text locally and should not be used beyond accession/source-surface state until the original Dutch record is attached.
- Duplicate package/gap-map/sample rows were marked `cross_project_duplicate` and should be deduplicated to the reviewed parent record before any extraction.
- Claim ceilings remain source-surface/context only; machine translation was not converted into factual/legal/policy/safety/compliance conclusions.

## Verification

- Output header matches the required schema.
- Output row count equals input row count.
- Output queue_id set equals input queue_id set.
- No duplicate output queue_id values.
