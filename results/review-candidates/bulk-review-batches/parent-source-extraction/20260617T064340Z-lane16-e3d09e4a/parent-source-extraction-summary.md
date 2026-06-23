# Parent source extraction summary

Batch: 20260617T064340Z-lane16-e3d09e4a
Input: /srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/bulk-review-batches/parent-source-extraction/20260617T064340Z-lane16-e3d09e4a/input.tsv
Results: /srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/bulk-review-batches/parent-source-extraction/20260617T064340Z-lane16-e3d09e4a/parent-source-extraction-results.tsv

Reviewed 24 input rows exactly once. Used local TSV rows, local profile JSON context, warning-document context, and local source-pack/refresh rows only; no web crawl or external submission was performed.

## Verdict counts
- source_url_extracted: 2
- parent_source_wrapper: 1
- country_gap_no_parent_source: 21
- source_surface_only_no_case: 0
- duplicate_existing_core: 0
- reject_noise: 0

## Extracted URLs
- BPSE-02172: Bahrain iGA AI policy PDF, retained only as weak transparency/explainability context for I05; not an operational algorithm-register source.
- BPSE-02183: Costa Rica MICITT ENIA action-plan PDF, retained as planned/strategy sandbox evidence for I03.

## Wrapper requiring human choice
- BPSE-02175: Dominica I05 warning maps to multiple local negative-check anchors in source-refresh/source-pack rows; no single parent URL was selected.

## Boundary
Processing-state review only. No reviewed-core promotion, ObscureAI addition, incident truth, legal finding, safety finding, compliance finding, prevalence, or ranking claim is made.
