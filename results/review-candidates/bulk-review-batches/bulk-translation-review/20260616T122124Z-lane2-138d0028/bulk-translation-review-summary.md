# Bulk translation review summary

Batch: 20260616T122124Z-lane2-138d0028
Input rows reviewed: 16
Output rows written: 16

## Verdict counts
- candidate_for_parent_source_extraction: 2
- cross_project_duplicate: 8
- source_surface_only_no_case: 4
- translation_source_reviewed: 2

## Language/source notes
- Czech: 1
- Danish: 2
- Dutch: 7
- English: 1
- Greek: 1
- Portuguese: 1
- Slovenian: 1
- Swedish: 1
- Ukrainian: 1

## Boundary applied
All rows were treated as processing-state review only. No row was promoted to reviewed core, ObscureAI, incident truth, legal finding, safety finding, compliance finding, prevalence claim, or ranking. Dutch Algorithm Register rows derived from public-ai-registry artifacts were marked as cross-project duplicates. Official non-English public-sector surfaces without explicit item-level edge-case evidence were capped at source-surface/context or parent-source extraction.

## Verification
Result TSV was programmatically checked for exact header, allowed verdicts, no duplicate queue_id values, no embedded tabs/newlines in fields, and identical queue_id set and row count versus input.tsv.
