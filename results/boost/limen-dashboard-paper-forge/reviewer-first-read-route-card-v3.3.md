# LIMEN reviewer first-read route card v3.3

Updated UTC: 2026-06-19T16:34:09Z
Lane: `limen-dashboard-paper-forge`
Purpose: give a hostile reviewer or human release reviewer a one-page read order that separates evidence, interpretation, dashboard hooks, external-action blockers, and forbidden overreads.

## Summary

This is a non-count-bearing package-navigation artifact. It does not collect new cases, promote rows, change denominators, assert source truth, or perform any external release action. It turns the current v3.2 human-release packet baseline into seven reviewer questions with exact first-read paths and claim ceilings.

## Reviewer first-read table

| id | reviewer question | read first | answer boundary | dashboard hook | status |
|---|---|---|---|---|---|
| RFR-001 | What is LIMEN claiming, and what is it not claiming? | `draft/preprint-v0.3-f1000.md; papers/article-architecture-v0.1.md; claims.md` | Methods/data-paper contribution about evidence architecture, denominator discipline, provenance-label control, and dashboard/paper parity. Not completeness, prevalence, legality/compliance, safety, deployment, country ranking, public release proof, or fused GAIA/PALLAS/LIMEN denominator. | release packet overview / claim-ceiling card | `READY_FOR_HUMAN_REVIEW` |
| RFR-002 | Can the count-bearing figures be reproduced without denominator drift? | `results/boost/limen-dashboard-paper-forge/figure2-5-7-denominator-binding-register-v0.4.tsv; results/boost/limen-dashboard-paper-forge/caption-control-denominator-rewrite-v1.1.md; results/boost/limen-dashboard-paper-forge/caption-currentness-audit-v0.9.tsv` | Figure 2, Figure 5, and Figure 7 have explicit denominator bindings and stale-caption gates; the figures do not support stronger empirical or legal conclusions. | denominator registry / caption-currentness panel | `READY_FOR_HUMAN_REVIEW` |
| RFR-003 | Does the dashboard expose uncertainty rather than just counts? | `dashboard/limen-dashboard-spec-v0.1.md; results/boost/limen-dashboard-paper-forge/source-ledger-renderer-consumption-v1.4.md; results/boost/limen-dashboard-paper-forge/methods-caption-export-audit-v1.5.md` | The dashboard is safe as a bounded artifact-level/family-level provenance and uncertainty surface; row-level rights/access badges remain blocked unless file-qualified source joins are manually verified. | source-ledger join action table / provenance-label gate | `READY_WITH_ROW_LEVEL_BADGE_BLOCKER` |
| RFR-004 | Which files are the release packet and how current are they? | `results/boost/limen-dashboard-paper-forge/human-release-packet-index-v3.2.tsv; results/boost/limen-dashboard-paper-forge/post-v3-public-surface-gate-rerun-v3.1.md; manifest.json` | The v3.2 packet is the current local human-review baseline; any edit requires rerunning manifest, pre-submit, and caption-currentness gates. | human-release packet index card | `READY_FOR_HUMAN_REVIEW` |
| RFR-005 | Are public URLs/DOIs equivalent to submission, acceptance, or citation-safe release? | `results/boost/limen-dashboard-paper-forge/public-availability-and-external-action-reconciliation-v2.9.md; results/boost/limen-dashboard-paper-forge/public-surface-state-grammar-v3.0.md` | Observed public resolving and HTTP 200 states are separated from citation-safe resolution, portal submission, acceptance, endorsement, and versioning. External actions remain Anton-controlled. | public-surface state grammar panel | `READY_WITH_EXTERNAL_ACTION_BLOCKER` |
| RFR-006 | What is the current venue route? | `results/boost/limen-dashboard-paper-forge/f1000-method-article-route-lock-v2.8.md; papers/article-architecture-v0.1.md` | Primary internal route is F1000Research Method Article for human review; this is not a submission, acceptance, or external publication claim. | route-lock / venue-fit card | `READY_WITH_EXTERNAL_ACTION_BLOCKER` |
| RFR-007 | What should the next responsible action be? | `results/dashboard-paper/status.md; journal.md; next.md` | Hold broad crawling. If no package fields change, next action is human release review; if files change, rerun gates and refresh the packet index. | package-health status card | `HOLD_CRAWLING_RERUN_GATES_AFTER_EDITS` |


## Verification and provenance

- TSV: `results/boost/limen-dashboard-paper-forge/reviewer-first-read-route-card-v3.3.tsv`
- TSV SHA-256: `33eceb948ba6d0ae240a81775fdb4ded2dd4f9acc95f2ce0d4ed70eb35f7c9eb`
- Source package baseline: `results/boost/limen-dashboard-paper-forge/human-release-packet-index-v3.2.tsv`
- Gate baseline before write: manifest JSON PASS; LIMEN pre-submit PASS (`9/9`, `0 FAIL`, `0 WARN`); caption-currentness pytest PASS (`2 passed`) at 2026-06-19T16:33:04Z.
- External actions performed: `0`.

## Claim ceiling

Use this artifact only for package navigation, reviewer-read-order control, release-routing discipline, and dashboard/paper parity explanation. It does not support completeness, prevalence, incident truth, legal guilt, compliance, safety, deployment, source-truth, country ranking, public-release, F1000 submission/acceptance, or fused GAIA/PALLAS/LIMEN denominator claims.

## Next smallest publishability move

If no package fields change, keep broad crawling stopped and route the v3.2/v3.3 packet to human release review. If any manuscript, dashboard, SI, status, route, or public-surface file changes, rerun manifest JSON, `tools/limen_pre_submit_check.py`, and `tests/test_limen_caption_currentness_gate.py`, then refresh the human-release packet index.
