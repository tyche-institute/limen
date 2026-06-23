# Case extraction summary — 20260617T073601Z-lane01-37e0e1bb

Input: `/srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/case-extraction-batches/20260617T073601Z-lane01-37e0e1bb/input.tsv`
Results: `/srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/case-extraction-batches/20260617T073601Z-lane01-37e0e1bb/case-extraction-results.tsv`

## Outcome

- Input source clusters reviewed: 16
- Output rows written: 16
- Case candidates for hardening: 0
- Closed noncase source surfaces: 16
- Other verdicts: 0

## Extraction notes

Every cluster was reviewed exactly once against the provided metadata and, where reachable, the exact public URL in `source_url_or_locator`. The batch consists of algorithm-register, procurement-portal, legal/policy, strategy, public-service launch, conference/news, and vendor-product surfaces. None contains a bounded concrete AI edge-case event/action/vulnerability/finding suitable for reviewed-core or ObscureAI hardening at this extraction stage.

No broad crawling, web search, submission, publication, login, upload, registration, payment, reviewed-core promotion, or ObscureAI addition was performed.

## Verification

The result TSV was validated to have the required header, 16 data rows, no duplicate `source_cluster_key` values, and the same `source_cluster_key` set as the input TSV.
