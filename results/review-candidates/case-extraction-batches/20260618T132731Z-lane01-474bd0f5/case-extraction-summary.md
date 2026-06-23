# Case extraction summary: 20260618T132731Z-lane01-474bd0f5

- Input: `/srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/case-extraction-batches/20260618T132731Z-lane01-474bd0f5/input.tsv`
- Results: `/srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/case-extraction-batches/20260618T132731Z-lane01-474bd0f5/case-extraction-results.tsv`
- Reviewed source_cluster_key count: 1
- Output row count: 1
- Verdicts:
  - closed_noncase_source_surface: 1

## Reviewed cluster

1. `https://algoritmes.overheid.nl/en/algoritme/15583895` — closed_noncase_source_surface
   - Source inspected: `https://algoritmes.overheid.nl/en/algoritme/15583895` (HTTP 200; redirected canonical page observed as `/en/algoritme/zb000162/15583895/module-to-screen-for-language-bias`).
   - Reason: Dutch Algorithm Register transparency entry for the TNO/CompetentNL language-bias screening module. It states status, purpose, risks, mitigations, and last-change metadata, but it does not document a concrete event, official finding, vulnerability, adverse action, harm, or legal/safety/compliance determination.
   - Boundary retained: extraction only; no reviewed-core promotion, no ObscureAI addition, no incident-truth or compliance finding.

## Verification

- Input source_cluster_key set equals output source_cluster_key set.
- Input data rows: 1.
- Output data rows: 1.
- No duplicate output source_cluster_key values.
