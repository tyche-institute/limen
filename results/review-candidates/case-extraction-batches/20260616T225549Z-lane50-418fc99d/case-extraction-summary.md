# Case extraction summary — 20260616T225549Z-lane50-418fc99d

Input: `/srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/case-extraction-batches/20260616T225549Z-lane50-418fc99d/input.tsv`
Output: `/srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/case-extraction-batches/20260616T225549Z-lane50-418fc99d/case-extraction-results.tsv`

Reviewed 16 source_cluster_key values exactly once.

Verdict counts:
- case_candidate_for_hardening: 1
- closed_noncase_source_surface: 15
- closed_duplicate_existing_core: 0
- blocked_no_public_source: 0
- needs_original_source_text: 0
- reject_noise: 0

Candidate extracted:
- Stanford CRFM Alpaca page: official self-described disabling of the public demo, bounded to CRFM's stated reasons including hosting costs and inadequacies of content filters. This is queued only for later hardening, not promoted.

Noncase pattern notes:
- CNBS, CNIL, San Marino, Datatilsynet, DPO Mauritius, NIST, IETF, ITU, and open-data/government portal clusters were retained as source-surface or index/context records because they do not by themselves isolate a single concrete AI edge-case event/finding.
- No public actions, submissions, uploads, accounts, or promotions were performed.

Verification:
- Result TSV key set and row count must match input TSV; see manifest for verification fields.
