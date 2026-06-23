# LIMEN human release packet index v2.4

- Updated UTC: 2026-06-19T10:59:51Z
- Lane: `limen-dashboard-paper-forge`
- Companion table: `results/boost/limen-dashboard-paper-forge/human-release-packet-index-v2.4.tsv`
- Companion SHA-256: `b4d0f113124e74aa4a3efd5bab68a7a6820fc8424bb91425c1962a68b7dd694d`
- Sprint posture: bounded manuscript/dashboard assembly; no broad crawling, no upload, no deposit, no portal action.

## Purpose

This artifact gives a human reviewer a single packet index for the current LIMEN F1000Research/dashboard release state. It is intentionally non-count-bearing: it records which local files should be read or rerun, what each file is allowed to support, and which external actions remain blocked.

## Result

- Indexed files: `13`.
- Missing indexed files: `0`.
- External actions performed: `0`.
- Public release / upload / deposit / portal action: `blocked; Anton-controlled`.
- Row-level access-date / rights / terms / license badges: `blocked pending file-qualified source joins`.

## Read order for human release review

1. `draft/preprint-v0.3-f1000.md` — read the submitted-article story and check whether all count language remains denominator-bound.
2. `results/boost/limen-dashboard-paper-forge/human-release-decision-checklist-v2.0.md` — confirm external-action blockers and decision gates.
3. `results/boost/limen-dashboard-paper-forge/required-output-closure-audit-v2.3.md` — confirm required dashboard/paper-forge outputs are present.
4. `results/boost/limen-dashboard-paper-forge/file-qualified-source-join-scope-audit-v2.2.md` — confirm row-level provenance labels remain blocked.
5. Run package gates after any edit: `python3 tools/limen_pre_submit_check.py --project-root /srv/tyche/projects/limen-ai-edge-case-atlas`, `pytest -q tests/test_limen_caption_currentness_gate.py`, and `python3 -m json.tool manifest.json`.

## Claim ceiling

This index supports package-integrity, release-review routing, and dashboard/paper parity claims only. It does not validate any incident, promote any row, prove source truth, prove legal compliance or non-compliance, establish safety, show prevalence/completeness, rank countries, or merge GAIA/PALLAS/LIMEN denominators.

## Observatory hook

A dashboard can consume `results/boost/limen-dashboard-paper-forge/human-release-packet-index-v2.4.tsv` as a non-count-bearing `release_packet_health` panel with columns: `packet_id`, `exists`, `artifact_role`, `review_consumer`, `claim_ceiling`, `allowed_action`, and `blocker_or_note`. Interpretation: show release-review readiness and blockers, not evidence volume.

## Missing-file handling

All indexed files exist locally at write time. This does not authorize external release; it only supports internal review readiness.

## Indexed artifact table

| packet_id | path | exists | allowed_action | blocker_or_note |
|---|---|---|---|---|
| manuscript_current | `draft/preprint-v0.3-f1000.md` | yes | read-only-review | primary release text |
| dashboard_spec | `dashboard/limen-dashboard-spec-v0.1.md` | yes | read-only-review | required lane output |
| article_architecture | `papers/article-architecture-v0.1.md` | yes | read-only-review | required lane output |
| dashboard_api_bundle | `dashboard/limen-dashboard-api-bundle-v0.1.json` | yes | internal-consume | do not present as public release proof |
| static_dashboard_preview | `dashboard/static-dashboard-preview-v0.1.html` | yes | internal-consume | no upload/deploy action |
| si_manifest | `results/boost/limen-dashboard-paper-forge/si-package/si-package-manifest.json` | yes | read-only-review | check file presence before deposit |
| pre_submit_tool | `tools/limen_pre_submit_check.py` | yes | internal-run | rerun after edits |
| caption_gate_test | `tests/test_limen_caption_currentness_gate.py` | yes | internal-run | rerun after edits |
| closure_audit_v23 | `results/boost/limen-dashboard-paper-forge/required-output-closure-audit-v2.3.md` | yes | read-only-review | current closure state before v2.4 |
| source_join_scope_v22 | `results/boost/limen-dashboard-paper-forge/file-qualified-source-join-scope-audit-v2.2.md` | yes | read-only-review | do not enable tooltips before file-qualified joins |
| release_checklist_v20 | `results/boost/limen-dashboard-paper-forge/human-release-decision-checklist-v2.0.md` | yes | read-only-review | external upload/deposit remains Anton-controlled |
| status | `results/dashboard-paper/status.md` | yes | read-only-review | append-only summary surface |
| manifest | `manifest.json` | yes | internal-consume | must remain valid JSON |
