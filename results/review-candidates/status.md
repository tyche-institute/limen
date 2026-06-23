# LIMEN Review-Candidate Status

Generated UTC: 2026-06-23T19:57:01Z

Policy: all latest non-self CPU-mined signals are materialized as review candidates.

- Raw latest shard rows: `58516`
- Self-referential miner echoes excluded: `2791`
- Duplicate rows collapsed: `0`
- Review-candidate rows: `55725`
- Ledger: `/srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/all-signals-review-candidates.tsv`

## Review Priority Counts

- `P1_official_or_regulator_review`: `9300`
- `P2_article_relevance_review`: `33040`
- `P3_candidate_review`: `13385`

## Boundary

`review_candidate_pending` means every signal is in the review queue. It does not mean the signal is a reviewed core example, an incident truth finding, a legal conclusion, a prevalence denominator, or a deployment claim.
