# LIMEN F1000 method-article route lock v2.8

- Updated UTC: 2026-06-19T13:35:33Z
- Lane: `limen-dashboard-paper-forge`
- Companion table: `results/boost/limen-dashboard-paper-forge/f1000-method-article-route-lock-v2.8.tsv`
- Companion SHA-256: `cd1d0e169e6773e6aecb4baa4837b52d8fbb1ea11063a424e0cb17ce0ddd0d1e`
- External actions performed: `0`

## Purpose

This artifact locks the current LIMEN dashboard/paper package to a bounded F1000Research Method Article route for human review. It does not submit, upload, deposit, publish, email, contact venues, open portal forms, or claim acceptance. It is a route-control and claim-ceiling artifact for the manuscript/dashboard package.

## Route decision

Current primary route: **F1000Research Method Article** using `draft/preprint-v0.3-f1000.md` as the live manuscript surface and `results/boost/limen-dashboard-paper-forge/si-package/` as the local supplementary-information packet.

Why this route is publication-safe now:

1. The manuscript's strongest contribution is methodological: evidence architecture, denominator discipline, source authority separation, claim ceilings, dashboard/paper parity, and reproducible gates.
2. The sprint explicitly asks LIMEN to patch methods/data article surfaces and avoid broad crawling or fused denominators.
3. The package has executable pre-submit and caption-currentness gates; those gates support package integrity and dashboard/paper parity, not empirical/legal/safety overclaims.
4. External release actions remain blocked until Anton performs the human-side decision.

## Claim ceiling

Safe release-card wording remains:

`The local LIMEN dashboard/paper package has passed its internal pre-submit consistency checks and currently supports methods/data-paper claims about provenance, denominator discipline, dashboard/paper parity, and claim-boundary control. It does not by itself support claims of corpus completeness, prevalence, legal compliance or violation, safety, certification, deployment status, country ranking, source truth, or third-party endorsement.`

## Pre-write verification

- `python3 -m json.tool manifest.json >/dev/null`: PASS (exit 0). 
- `python3 tools/limen_pre_submit_check.py --project-root /srv/tyche/projects/limen-ai-edge-case-atlas`: PASS (exit 0).  VERDICT: ALL CHECKS PASS — submission package is internally consistent. Remaining external blockers: Zenodo deposit, F1000Research upload (Anton).
- `pytest -q tests/test_limen_caption_currentness_gate.py`: PASS (exit 0). ..                                                                       [100%] 2 passed in 0.00s

## Route-lock table summary

| route_id | state | required human action |
|---|---|---|
| F1000-METHOD-ARTICLE | PRIMARY_ROUTE_LOCKED_FOR_HUMAN_REVIEW | final read and any portal/upload action |
| DASHBOARD-PARITY | SUPPORTS_ROUTE_WITH_BOUNDED_VIEW_CONTRACTS | do not enable row-level access/rights badges before file-qualified joins |
| ARTICLE-ARCHITECTURE | ROUTE_SELECTION_UPDATED | use F1000 route as current primary unless Anton changes publication target |
| SI-PACKAGE | LOCAL_SI_PACKET_AVAILABLE | check contents before any deposit/upload |
| AUTOMATED-GATES | PASS_BEFORE_V2_8_WRITE | rerun after any manuscript, figure, dashboard, manifest, SI, or caption edit |
| EXTERNAL-ACTIONS | BLOCKED_BY_BOUNDARY | explicit Anton-controlled action only |


## Observatory hook

A dashboard can consume the TSV as a non-count-bearing `publication_route_lock` or `release_route_control` panel. Suggested fields: `route_id`, `surface`, `state`, `consumer`, `claim_ceiling`, `required_human_action`, `forbidden_overread`, `provenance`, `path`, `sha256`, and `size_bytes`. Interpretation: this panel explains which route the package is prepared for and which claims/actions remain blocked; it must not be displayed as incident validation or release proof.

## Next smallest publishability move

Do not crawl broadly. The next useful move is either (a) Anton-side final read/upload decision, or (b) if another lane edit occurs first, rerun the automated gates and refresh this route lock/currentness evidence before any release review.
