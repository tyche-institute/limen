# Case extraction summary: 20260616T225549Z-lane37-4b87dbcc

Completed: 2026-06-16T22:56:43Z

Input: /srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/case-extraction-batches/20260616T225549Z-lane37-4b87dbcc/input.tsv
Results: /srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/case-extraction-batches/20260616T225549Z-lane37-4b87dbcc/case-extraction-results.tsv

Rows reviewed: 16
Rows emitted: 16

Verdict counts:
- closed_noncase_source_surface: 16

Method:
- Reviewed each input `source_cluster_key` exactly once.
- Used input row metadata and exact DOI URLs only; no broad crawling, general web search, promotion, publishing, portal action, or public interaction.
- DOI content-negotiation metadata showed scholarly/report/proceedings/index records rather than direct concrete AI edge-case event/action/vulnerability/finding/official records.

Boundary:
- No reviewed-core promotion.
- No ObscureAI addition.
- No incident-truth, legal, safety, compliance, deployment, prevalence, guilt, or ranking claim.

Verification:
- Result TSV source_cluster_key set and row count match input.tsv.
- No duplicate source_cluster_key values in result TSV.
