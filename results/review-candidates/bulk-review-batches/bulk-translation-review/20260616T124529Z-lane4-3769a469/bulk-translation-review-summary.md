# Bulk translation review summary

Batch: 20260616T124529Z-lane4-3769a469
Task: bulk-translation-review

## Verification

- Input rows reviewed: 16
- Output rows written: 16
- Queue-id set match: True
- Duplicate output queue_ids: []

## Verdict counts

- candidate_for_parent_source_extraction: 2
- needs_original_language_source: 1
- reject_noise: 5
- source_surface_only_no_case: 5
- translation_source_reviewed: 3

## Boundary notes

This batch is processing-state review only. No row was promoted to reviewed-core, ObscureAI, incident truth, legal finding, safety finding, compliance finding, prevalence, or ranking. Reviews used only local metadata/source files and multilingual surface understanding. Machine-translation-sensitive rows were capped at source-surface/context unless original-language extraction is still needed.

## High-value follow-up

- BTR-00582: extract bounded Swedish quotations from the Åland legislative proposal's sandbox chapter.
- BTR-00588: locate the local parent Ísland.is/Persónuvernd source rows and extract bounded Icelandic quotations for the 2022 healthcare AI sandbox pilot.
- BTR-00591: obtain an original Persian capture for the Nezamat AI steering council decree before any content claim.
