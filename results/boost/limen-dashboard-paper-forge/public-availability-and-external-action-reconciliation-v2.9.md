# LIMEN public-availability and external-action reconciliation v2.9

- Updated UTC: 2026-06-19T14:10:12Z
- Lane: `limen-dashboard-paper-forge`
- Companion table: `results/boost/limen-dashboard-paper-forge/public-availability-and-external-action-reconciliation-v2.9.tsv`
- Companion SHA-256: `666a60c5006ab66102e01dba184ff74bc8f87b591ab7018502041640a30bcbae`
- External actions performed: `0`

## Purpose

This artifact reconciles two truths that can otherwise look contradictory in the release packet: some LIMEN public surfaces and Zenodo DOIs already resolve publicly, while any new F1000Research submission, Zenodo versioning/upload, portal action, email, or publication action remains Anton-controlled and outside lane authority. The check is a bounded public reachability/metadata check only.

## Result

- Public availability surfaces checked: `4`.
- Publicly resolving at check time: `2`.
- F1000 portal/submission state checked by lane: `0` (intentionally not opened).
- New upload/deposit/submission/publication/contact actions performed: `0`.

## Interpretation

The manuscript may keep already-public DOI and live-site availability statements where they are accurate, but release-control language must distinguish them from any new external action. In short: existing public DOI/site reachability supports data-availability and prior-posting disclosure; it does not support a claim that this lane submitted to F1000Research, created a new Zenodo version, obtained peer review, received acceptance, or made any legal/compliance/safety/source-truth finding.

## Table summary

| Surface | State | Safe use |
|---|---|---|
| DATASET_DOI | PUBLICLY_RESOLVES | cite as already-public availability/provenance surface only |\n| MANUSCRIPT_PREPRINT_DOI | PUBLICLY_RESOLVES | cite as already-public availability/provenance surface only |\n| LIVE_OBSERVATORY | REVIEW_REQUIRED | do not cite without manual review |\n| CASE_ATLAS_JSON | REVIEW_REQUIRED | do not cite without manual review |\n| F1000_SUBMISSION_PORTAL | ANTON_ONLY_BLOCKED | treat package as route-ready for human review only |\n

## Claim ceiling

This artifact supports package-integrity, public-availability reconciliation, and external-action boundary control only. It does not support completeness, prevalence, incident truth, source truth, legal/compliance/safety/deployment/certification claims, country rankings, third-party endorsement, F1000 acceptance, or a fused GAIA/PALLAS/LIMEN denominator.

## Observatory hook

A dashboard can consume the TSV as a non-count-bearing `release_boundary` panel with fields `surface_id`, `url`, `state`, `safe_use`, `claim_ceiling`, and `external_action_boundary`. Interpretation: show what is already publicly reachable versus what remains Anton-only; do not display it as evidence validation or release proof.

## Next smallest publishability move

Before any human upload/submission decision, keep this reconciliation beside the route lock so the package can say both: existing DOI/site surfaces are public, and new F1000/Zenodo actions remain blocked without Anton. Rerun this check after any data-availability, DOI, site, route-lock, or submission-kit edit.
