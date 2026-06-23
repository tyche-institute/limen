# Bulk translation review summary

Batch: 20260616T120553Z-lane3-853c3d09
Task: bulk-translation-review
Input rows reviewed: 16
Output rows written: 16

## Boundary applied

This batch was treated as processing-state review only. No row was promoted to reviewed-core, ObscureAI, incident truth, legal finding, safety finding, compliance finding, prevalence, or ranking.

Local source metadata and local source files were used only. Translation-dependent rows were kept at source-surface/context level unless the local row contained a concrete source-surface statement.

## Verdict counts

- translation_source_reviewed: 2
- needs_original_language_source: 2
- cross_project_duplicate: 2
- machine_translation_hold: 2
- candidate_for_parent_source_extraction: 3
- source_surface_only_no_case: 5
- reject_noise: 0

## Main routing notes

- Original-language or verified-source extraction is needed for Hebrew, Portuguese, Chinese, and Dutch auto-translated surfaces before substantive claims.
- Dutch Algorithm Register rows were retained as register/source surfaces, not legal or risk findings.
- PALLAS readiness rows were mostly context, parent-source, or gap surfaces; they were not promoted into case-level claims.
- The Chinese deep-synthesis source appears across GAIA digest, translation-review queue, and source-document metadata and should be deduplicated into a single original-language review path.

## Verification

Verified that output queue_id count and set match input.tsv exactly: 16 input queue_ids and 16 output queue_ids, with no omissions, extras, or duplicates.
