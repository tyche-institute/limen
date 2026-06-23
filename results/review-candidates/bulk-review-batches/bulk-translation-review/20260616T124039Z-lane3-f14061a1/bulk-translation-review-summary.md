# Bulk translation review summary: 20260616T124039Z-lane3-f14061a1

Status: completed
Input rows reviewed: 16
Output rows written: 16

## Verdict counts
- candidate_for_parent_source_extraction: 2
- cross_project_duplicate: 2
- needs_original_language_source: 1
- source_surface_only_no_case: 6
- translation_source_reviewed: 5

## Review boundary
- Local metadata and local source rows only; no broad web crawl or external portal interaction.
- Processing-state review only: no reviewed-core promotion, incident truth, legal finding, safety finding, compliance finding, prevalence, or ranking.
- Translation-sensitive rows were kept at source-surface/context ceilings unless local English metadata already supported parent-source extraction.

## Duplicate handling
- BTR-00501 duplicates the Indonesia source surface reviewed at BTR-00497.
- BTR-00511 duplicates the Malaysia AIGE source surface reviewed at BTR-00508.

## Verification
- Results TSV uses the required header exactly.
- One output row was written for every input queue_id with no extras or duplicates.
- Queue_id set and row count were verified after writing.
