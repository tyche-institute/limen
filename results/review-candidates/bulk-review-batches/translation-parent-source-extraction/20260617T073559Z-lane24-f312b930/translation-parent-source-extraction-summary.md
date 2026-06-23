# Translation parent source extraction summary

Batch: 20260617T073559Z-lane24-f312b930
Task: translation-parent-source-extraction
Input: /srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/bulk-review-batches/translation-parent-source-extraction/20260617T073559Z-lane24-f312b930/input.tsv
Result TSV: /srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/bulk-review-batches/translation-parent-source-extraction/20260617T073559Z-lane24-f312b930/translation-parent-source-extraction-results.tsv

## Counts

- Input rows reviewed: 1
- Output rows written: 1
- source_url_extracted: 1
- parent_source_wrapper: 0
- country_gap_no_parent_source: 0
- source_surface_only_no_case: 0
- duplicate_existing_core: 0
- reject_noise: 0

## Notes

- Reviewed every non-header input row exactly once.
- Used only local metadata and local source context.
- Extracted the explicit `public_url` from `/srv/tyche/gaia/tyche-research-vault/release/gaia-preprint-freeze-20260605T0815EEST/data/global-agent-atlas-v0.1/backups-cycle188-active-lanes-32-foreign-language-public-service-hardening/records.jsonl:307` for `BTPS-00132`; the same URL is also present in local `source_urls`.
- No reviewed-core promotion, incident truth, legal finding, safety finding, compliance finding, prevalence, or ranking claim was made.

## Verification

- Result TSV header matches required schema.
- Result TSV queue_id set equals input.tsv queue_id set.
- Result TSV output row count equals input.tsv row count.
