# Case extraction summary: 20260616T225551Z-lane61-87f4d633

- Input: `/srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/case-extraction-batches/20260616T225551Z-lane61-87f4d633/input.tsv`
- Output TSV: `/srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/case-extraction-batches/20260616T225551Z-lane61-87f4d633/case-extraction-results.tsv`
- Rows reviewed: 15 source_cluster_key values
- Verdict counts:
  - closed_noncase_source_surface: 15
  - case_candidate_for_hardening: 0
  - closed_duplicate_existing_core: 0
  - blocked_no_public_source: 0
  - needs_original_source_text: 0
  - reject_noise: 0

## Extraction notes

All clusters in this batch are vendor documentation/product pages, software release pages, blog/proxy surfaces, or dataset/index source-family surfaces. None isolates a concrete AI edge-case event/action/vulnerability/finding/official record with a bounded claim suitable for reviewed-core/ObscureAI hardening.

Exact public URLs/locators supplied in `input.tsv` were treated as the permitted inspection boundary. No broad crawl, public action, promotion, reviewed-core addition, or ObscureAI addition was performed.

## Boundary retained

The output makes no incident-truth, legal-finding, safety-finding, compliance-finding, deployment-proof, prevalence, ranking, or guilt claim. Each row is closed as source-surface accounting unless a future separate extraction identifies a concrete original-source record.
