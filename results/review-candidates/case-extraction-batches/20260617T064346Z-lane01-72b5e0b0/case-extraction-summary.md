# Case extraction summary: 20260617T064346Z-lane01-72b5e0b0

Input: `/srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/case-extraction-batches/20260617T064346Z-lane01-72b5e0b0/input.tsv`

Output: `/srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/case-extraction-batches/20260617T064346Z-lane01-72b5e0b0/case-extraction-results.tsv`

## Scope and boundary

Reviewed each input `source_cluster_key` exactly once using the input metadata and the exact source URL/locator surfaces only. No broad crawl, search-engine expansion, portal login, upload, submission, publication, or promotion action was performed.

Boundary retained: extraction only. No reviewed-core promotion, no ObscureAI addition, and no incident truth, legal finding, safety finding, compliance finding, deployment proof, prevalence, ranking, or guilt claim was made.

## Verdict counts

- `closed_noncase_source_surface`: 8
- `case_candidate_for_hardening`: 0
- `closed_duplicate_existing_core`: 0
- `blocked_no_public_source`: 0
- `needs_original_source_text`: 0
- `reject_noise`: 0

## Extraction notes

All eight clusters remained source-surface/context records rather than concrete AI edge-case records. The reviewed surfaces were institutional portals, law/procurement portals, product/vendor pages, or generic source-family locators. None exposed, in the cluster metadata or exact locator inspection, a bounded concrete event/action/vulnerability/finding/official record suitable for reviewed-core hardening.

The `ine.gob.ve` locator returned HTTP 403 during inspection, but the input metadata and locator level still supplied only an institutional source-surface context and no case-level public record; it was therefore closed as a noncase source surface rather than promoted or treated as a case.

## Verification

- Input data rows: 8
- Result data rows: 8
- Source cluster key set: exact match with input
- Duplicate result keys: 0
- Extra result keys: 0
- Missing result keys: 0
