# Bulk translation review summary: 20260618T132345Z-lane2-73c19dee

Input: `/srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/bulk-review-batches/bulk-translation-review/20260618T132345Z-lane2-73c19dee/input.tsv`
Results: `/srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/bulk-review-batches/bulk-translation-review/20260618T132345Z-lane2-73c19dee/bulk-translation-review-results.tsv`

Reviewed rows: 16

Verdict counts:
- cross_project_duplicate: 12
- candidate_for_parent_source_extraction: 1
- source_surface_only_no_case: 3

Notes:
- Review used only local metadata and the cited local source files.
- Dutch Algorithm Register rows are English auto-translations from Dutch, so all conclusions are capped at source-surface/context or extraction-lead status.
- Octobox Anonymisation, Zylab Disclosure Support, and Datamask rows expose registry/sample/gap-map fields but do not by themselves state a concrete LIMEN edge-case incident or finding.
- The accession row titled "Module to screen for language bias" is a parent-source extraction lead only; the local accession row lacks enough original-language record text for promotion.
- No reviewed-core promotion, ObscureAI addition, incident truth, legal finding, safety finding, compliance finding, prevalence claim, or ranking was made.

Verification:
- Result row count equals input row count.
- Result queue_id set equals input queue_id set.
- No duplicate queue_id values in result.
