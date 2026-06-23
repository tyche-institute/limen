# Case extraction summary: 20260616T225549Z-lane45-2df96ebd

Input: `/srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/case-extraction-batches/20260616T225549Z-lane45-2df96ebd/input.tsv`
Results: `/srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/case-extraction-batches/20260616T225549Z-lane45-2df96ebd/case-extraction-results.tsv`

Reviewed 16 source_cluster_key values exactly once. Extraction stayed within provided local locators and exact public URLs; no broad crawling, promotion, submission, upload, login, or public action was performed.

## Verdict counts

| verdict | count |
|---|---:|
| case_candidate_for_hardening | 1 |
| needs_original_source_text | 1 |
| closed_noncase_source_surface | 14 |

## Candidate/lead notes

- `https://link.springer.com/article/10.1007/s11192-024-05172-3` is a case candidate for hardening only as a bounded scholarly finding about retractions due to randomly generated content; it is not promoted and carries strict overread limits.
- `/srv/tyche/pallas/pallas-ai-agent-observatory/reports/pallas_second_pass_confidence_changes.csv:882` remains `needs_original_source_text`: it is a concrete Iceland healthcare AI sandbox lead, but the original official Ísland.is/Persónuvernd source URLs/text were not present in this batch row.
- All other rows are closed noncase source surfaces: DOI/index/chapter/report/policy/program/static-asset surfaces or internal route/context records without a bounded AI edge-case event/finding.

## Boundary

No reviewed-core promotion, no ObscureAI addition, no incident truth claim, and no legal/safety/compliance/deployment/prevalence/ranking claim was made.
