# Bulk translation review summary

Batch: 20260616T122515Z-lane2-72129a6b

Reviewed 16 input rows exactly once using local metadata/source files only. No web crawl or external submission actions were used. This is processing-state review only; no row was promoted to reviewed-core, ObscureAI, incident truth, legal finding, safety finding, compliance finding, prevalence, or ranking.

Verdict counts:
- candidate_for_parent_source_extraction: 1
- cross_project_duplicate: 2
- machine_translation_hold: 4
- needs_original_language_source: 1
- source_surface_only_no_case: 7
- translation_source_reviewed: 1

Notes:
- Dutch algorithm-register rows remain translation-safe because local evidence is English auto-translation or accession metadata; original Dutch source review is required before field-level claims.
- Polish GRAI and Dutch Zylab rows include duplicate local source surfaces and should be deduplicated before further extraction.
- Slovenian, Icelandic, Albanian, French, Curaçao, Pakistan, and Syrian rows are retained only as source-surface/context unless additional original-language evidence supports a concrete edge-case claim.

Verification:
- Output TSV header matches required schema.
- Output row count equals input row count.
- Output queue_id set equals input queue_id set, with no duplicate queue_id values.
