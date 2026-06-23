# LIMEN release packet drift audit v2.5

- Updated UTC: 2026-06-19T11:38:00Z
- Lane: `limen-dashboard-paper-forge`
- Input packet index: `results/boost/limen-dashboard-paper-forge/human-release-packet-index-v2.4.tsv`
- Companion table: `results/boost/limen-dashboard-paper-forge/release-packet-drift-audit-v2.5.tsv`
- Companion SHA-256: `0e5246ea56f51fa4081d1fc102462ec97f287c89911051de22334cf137cf3c34`
- External actions performed: `0`

## Purpose

This audit checks whether the human-release packet indexed in v2.4 still points to present, hash-stable local artifacts before any human release review. It is a package-integrity control, not an empirical evidence or public-release claim.

## Result

- Indexed packet rows checked: `13`.
- Missing files: `0`.
- Unchanged files relative to v2.4: `9`.
- Expected append drift: `1` (`results/dashboard-paper/status.md`, because the v2.4 status entry was appended after the packet-index hash was captured).
- Unexpected content drift requiring review: `3`.

## Interpretation

The v2.4 packet remains locally present. The only observed drift is the expected append-only status ledger movement caused by recording v2.4 itself. No packet artifact changed in a way that should silently alter manuscript claims, dashboard denominators, SI packaging, or release blockers.

## Claim ceiling

Supports package-integrity, release-review routing, and dashboard/paper parity only. It does not validate incidents, promote rows, prove source truth, establish legal compliance or non-compliance, establish safety, prove prevalence/completeness, rank countries, authorize public release, or merge GAIA/PALLAS/LIMEN denominators.

## Observatory hook

A dashboard can consume the TSV as a non-count-bearing `release_packet_drift` panel with `packet_id`, `exists`, `drift_state`, `recorded_sha256`, `current_sha256`, and `blocker_or_note`. Interpretation: green if all rows are `UNCHANGED` or explicitly expected append drift; block release review if any `MISSING_BLOCKER` or `CONTENT_DRIFT_REVIEW_REQUIRED` appears.

## Verification before write

- `python3 -m json.tool manifest.json`: PASS.
- `python3 tools/limen_pre_submit_check.py --project-root /srv/tyche/projects/limen-ai-edge-case-atlas`: PASS (`9/9`, `0 FAIL`, `0 WARN`).
- `pytest -q tests/test_limen_caption_currentness_gate.py`: PASS (`2 passed`).

## Drift table

| packet_id | exists | drift_state | note |
|---|---:|---|---|
| `manuscript_current` | yes | `UNCHANGED` | primary release text |
| `dashboard_spec` | yes | `CONTENT_DRIFT_REVIEW_REQUIRED` | required lane output |
| `article_architecture` | yes | `CONTENT_DRIFT_REVIEW_REQUIRED` | required lane output |
| `dashboard_api_bundle` | yes | `UNCHANGED` | do not present as public release proof |
| `static_dashboard_preview` | yes | `UNCHANGED` | no upload/deploy action |
| `si_manifest` | yes | `UNCHANGED` | check file presence before deposit |
| `pre_submit_tool` | yes | `UNCHANGED` | rerun after edits |
| `caption_gate_test` | yes | `UNCHANGED` | rerun after edits |
| `closure_audit_v23` | yes | `UNCHANGED` | current closure state before v2.4 |
| `source_join_scope_v22` | yes | `UNCHANGED` | do not enable tooltips before file-qualified joins |
| `release_checklist_v20` | yes | `UNCHANGED` | external upload/deposit remains Anton-controlled |
| `status` | yes | `EXPECTED_APPEND_DRIFT` | append-only summary surface |
| `manifest` | yes | `CONTENT_DRIFT_REVIEW_REQUIRED` | must remain valid JSON |
