# Case extraction summary: 20260616T225503Z-lane24-c3bcb710

Input: `/srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/case-extraction-batches/20260616T225503Z-lane24-c3bcb710/input.tsv`
Results: `/srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/case-extraction-batches/20260616T225503Z-lane24-c3bcb710/case-extraction-results.tsv`

Reviewed source_cluster_key rows: 16
Output data rows: 16

Verdict counts:
- blocked_no_public_source: 1
- closed_noncase_source_surface: 14
- needs_original_source_text: 1

No source_cluster_key was promoted to reviewed-core or ObscureAI. Most rows are registry, policy, search, product, homepage, or readiness-report source surfaces rather than concrete edge-case events/findings. TED requires readable original notice text; the Turkey locator resolved to a 404 and is blocked as no public source text.

Verification:
- Result TSV header matches the required schema.
- Result TSV has one data row per input source_cluster_key.
- No duplicate output source_cluster_key values.
- Input and output source_cluster_key sets are identical.
