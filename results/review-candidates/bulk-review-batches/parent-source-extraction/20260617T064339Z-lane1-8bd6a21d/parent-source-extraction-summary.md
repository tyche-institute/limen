# Parent source extraction summary

Batch: 20260617T064339Z-lane1-8bd6a21d
Input rows reviewed: 24
Output rows written: 24

## Verdict counts
- source_url_extracted: 1
- parent_source_wrapper: 0
- country_gap_no_parent_source: 23
- source_surface_only_no_case: 0
- duplicate_existing_core: 0
- reject_noise: 0

## Method
- Reviewed each input row exactly once against local TSV/JSON context only.
- Inspected nearby source lines and atlas top_sources where present.
- Extracted a URL only when the local atlas metadata explicitly named a concrete public source URL.
- Marked research-queue and country-profile gap rows without a concrete source URL as country_gap_no_parent_source.

## Extracted source
- BPSE-01847 / LIMEN-SIGNAL-25BF3C63CE2EACDC: official Bahrain iGA AI policy PDF from local top_sources.

## Boundary notes
This batch is processing-state review only. No reviewed-core promotion, ObscureAI addition, incident truth, legal finding, safety finding, compliance finding, prevalence, or ranking claim was made.
