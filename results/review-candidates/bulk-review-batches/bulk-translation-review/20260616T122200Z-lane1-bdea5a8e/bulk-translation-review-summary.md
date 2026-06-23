# Bulk translation review summary — 20260616T122200Z-lane1-bdea5a8e

Input: `/srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/bulk-review-batches/bulk-translation-review/20260616T122200Z-lane1-bdea5a8e/input.tsv`
Results: `/srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/bulk-review-batches/bulk-translation-review/20260616T122200Z-lane1-bdea5a8e/bulk-translation-review-results.tsv`

Reviewed 16 input rows exactly once using local source rows and existing local LIMEN/Pallas/GAIA/public-ai-registry metadata only. No web crawl, portal use, submission, publication, upload, email, registration, payment, or case-level promotion was performed.

Verdict counts:

| verdict | count |
| --- | ---: |
| cross_project_duplicate | 8 |
| source_surface_only_no_case | 6 |
| translation_source_reviewed | 2 |

Notes:
- Dutch Algorithm Register rows from public-ai-registry/GAIA are treated as upstream duplicates or extraction targets, not independent LIMEN reviewed-core items.
- Pallas readiness source-pack rows were held at source-surface/context level where the local row did not contain a concrete edge-case claim.
- Pakistan Atlas rows identify English official source surfaces but local fetches failed; they remain source-surface only pending capture/extraction.
- Claim ceilings intentionally exclude incident truth, legal findings, safety findings, compliance findings, prevalence, and ranking.

Verification: result TSV row count and queue_id set were checked against input.tsv after writing.
