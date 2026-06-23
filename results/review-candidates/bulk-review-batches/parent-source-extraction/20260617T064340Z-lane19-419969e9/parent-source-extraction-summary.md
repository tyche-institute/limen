# Parent source extraction summary

Batch: 20260617T064340Z-lane19-419969e9
Completed UTC: 2026-06-17T06:45:50Z
Input rows reviewed: 24
Output rows written: 24

## Verdict counts

- country_gap_no_parent_source: 22
- parent_source_wrapper: 2
- source_url_extracted: 0
- source_surface_only_no_case: 0
- duplicate_existing_core: 0
- reject_noise: 0

## Method

Reviewed every input row exactly once against local source_path/source_line evidence and nearby local context only. No web crawling or external lookup was used. Concrete public URLs were not extracted unless explicitly bound to the row's local metadata/source context; none were so bound in this batch. Research-queue and country profile/score placeholders were marked as country_gap_no_parent_source. Two source-pack target-evidence rows were marked parent_source_wrapper because they list evidence categories and require human selection of a concrete parent source.

## Boundary

Processing-state review only. No reviewed-core promotion, ObscureAI addition, incident truth, legal finding, safety finding, compliance finding, prevalence, or ranking was made.
