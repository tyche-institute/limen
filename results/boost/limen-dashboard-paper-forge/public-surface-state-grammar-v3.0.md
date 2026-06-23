# LIMEN public-surface state grammar v3.0

- Updated UTC: 2026-06-19T14:45:00Z
- Lane: `limen-dashboard-paper-forge`
- Companion table: `results/boost/limen-dashboard-paper-forge/public-surface-state-grammar-v3.0.tsv`
- Companion SHA-256: `4a6b32aa689e18cf09201c755b1f38f3f679af82ec9469a081d50217066ee11a`
- External actions performed: `0`

## Purpose

This artifact closes a wording ambiguity left by the v2.9 public-availability reconciliation: `HTTP 200` reachability for a live site or JSON endpoint is not the same state as a DOI/resolver surface that may be cited as already-public availability. The dashboard and article package must separate four states: `PUBLICLY_RESOLVES`, `REVIEW_REQUIRED`, `ANTON_ONLY_BLOCKED`, and the explicit rule `HTTP_200_NOT_EQUAL_PUBLICLY_RESOLVES`.

## Result

- State rows defined: `4`.
- Empirical records added or promoted: `0`.
- External submission/deposit/upload/portal/contact actions performed: `0`.
- Correction scope: wording and release-boundary grammar only.

## Interpretation

Use DOI surfaces that v2.9 marked `PUBLICLY_RESOLVES` for already-public availability/provenance wording. Treat `LIVE_OBSERVATORY` and `CASE_ATLAS_JSON` as reachable-but-review-required until a human or a later bounded audit checks content/version stability and manuscript citation wording. Do not collapse HTTP reachability into release proof.

## Dashboard hook

Expose this TSV as a non-count-bearing `release_boundary/state_grammar` panel with fields `surface_state`, `meaning`, `allowed_wording`, `blocked_wording`, and `dashboard_panel_use`. The panel should sit beside the v2.9 release-boundary panel and prevent legends/captions from saying that all HTTP 200 surfaces are publication-safe.

## Claim ceiling

This artifact supports package-integrity, public-availability wording discipline, dashboard/paper parity, and external-action boundary control only. It does not support completeness, prevalence, incident truth, source truth, legal/compliance/safety/deployment/certification claims, country rankings, F1000 acceptance, peer review, third-party endorsement, public release by this lane, or a fused GAIA/PALLAS/LIMEN denominator.

## Next smallest publishability move

Keep v2.9 and v3.0 together in the release packet. If the manuscript cites the live observatory or public cases JSON, run a separate content/version review first and record exact access date, version/hash if available, and citation-safe wording.
