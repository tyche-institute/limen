# Security agentic publication cell note

Created: 2026-06-07T08:41:53Z
Lane: `limen-security-agentic-watch`

## Why this artifact exists

The shared security package already had routing, notice-depth, evidence-role, claim-ceiling, and balance-gap layers, but figure and dashboard consumers still had to reconstruct one publication-ready three-axis matrix by hand. This artifact promotes that control surface into `results/security/` so the first LIMEN article package can cite one shared machine-readable table rather than a lane-local boost file.

## Main result

`results/security/security-agentic-publication-cell-matrix-v0.1.tsv` normalizes each live security row into one publication cell with:

- `mechanism_family`
- `authority_family`
- `publication_bucket`
- `interoperability_state`
- `fix_visibility_state`
- reviewer-safe claim ceiling text and the next stronger source needed

It also preserves two explicit zero-state rows:

- `GAP-peer_reviewed_security_case_support`
- `GAP-supply_chain_or_plugin_extension`

## Paper-readiness delta

This is a packaging and visualization-readiness improvement, not a new-ingest step. The security package now has one shared cell-ready matrix that can directly feed a reviewer-safe heatmap, Sankey, appendix matrix, or dashboard facet without forcing downstream consumers to merge four separate shared control tables first.

## Suggested dashboard fields

`case_id`, `mechanism_family`, `authority_family`, `publication_bucket`, `interoperability_state`, `fix_visibility_state`, `evidence_tier`, `dashboard_cell`.

## Remaining blocker

The matrix makes two absences visible, but does not solve them: the package still lacks one same-format supply-chain/dependency-trust exemplar and still has no peer-reviewed public-security support.
