# LIMEN human release packet index v2.6

- Updated UTC: 2026-06-19T12:16:00Z
- Lane: `limen-dashboard-paper-forge`
- Input: `results/boost/limen-dashboard-paper-forge/human-release-packet-index-v2.4.tsv` plus v2.5 drift audit surfaces
- Companion table: `results/boost/limen-dashboard-paper-forge/human-release-packet-index-v2.6.tsv`
- Companion SHA-256: `9f506e70a4cabd82a1ecae744c3bb7598fb117afc6599f6736905f4fefce9c32`
- External actions performed: `0`

## Purpose

This refresh converts the v2.5 drift finding into a new current-hash baseline for internal human release review. It is intentionally non-count-bearing: it records local file presence, hashes, consumer roles, allowed actions, and claim ceilings after the dashboard spec, article architecture, status ledger, and manifest moved during prior internal audits.

## Result

- Current packet rows indexed: `15`.
- Missing files: `0`.
- Rows inherited from v2.4 release packet: `13`.
- Drift-provenance rows added: `2` (`drift_audit_v25`, `drift_audit_v25_table`).
- Baseline state: current local hashes are now explicit in v2.6; v2.5 remains useful as provenance explaining why v2.4 hashes should no longer be used as the release-review baseline.

## Interpretation

The package remains present locally and executable gates passed immediately before this refresh. Human review should use v2.6 as the current packet-health index and v2.5 as the historical drift-control note. This refresh does not alter dashboard denominators, manuscript claims, SI contents, evidence tiers, source-truth posture, or release blockers.

## Claim ceiling

Supports package-integrity, release-review routing, and dashboard/paper parity only. It does not validate incidents, promote rows, prove source truth, establish legal compliance or non-compliance, establish safety, prove prevalence/completeness, rank countries, authorize public release, or merge GAIA/PALLAS/LIMEN denominators.

## Observatory hook

A dashboard can consume the TSV as a non-count-bearing `human_release_packet_current_baseline` panel with `packet_id`, `path`, `exists`, `sha256`, `artifact_role`, `review_consumer`, `allowed_action`, and `blocker_or_note`. Interpretation: all rows must exist before human release review; external deposit/upload remains a separate Anton-controlled action even when all rows exist.

## Verification

- Pre-write gate: `python3 -m json.tool manifest.json` PASS; `python3 tools/limen_pre_submit_check.py --project-root /srv/tyche/projects/limen-ai-edge-case-atlas` PASS (`9/9`, `0 FAIL`, `0 WARN`); `pytest -q tests/test_limen_caption_currentness_gate.py` PASS (`2 passed`).
- Post-write gate at 2026-06-19T12:17:22Z: manifest JSON PASS; LIMEN pre-submit check PASS (`9/9`, `0 FAIL`, `0 WARN`); caption-currentness pytest PASS (`2 passed`).

## Packet rows

| packet_id | exists | allowed_action | note |
|---|---:|---|---|
| `manuscript_current` | yes | `read-only-review` | primary release text |
| `dashboard_spec` | yes | `read-only-review` | required lane output |
| `article_architecture` | yes | `read-only-review` | required lane output |
| `dashboard_api_bundle` | yes | `internal-consume` | do not present as public release proof |
| `static_dashboard_preview` | yes | `internal-consume` | no upload/deploy action |
| `si_manifest` | yes | `read-only-review` | check file presence before deposit |
| `pre_submit_tool` | yes | `internal-run` | rerun after edits |
| `caption_gate_test` | yes | `internal-run` | rerun after edits |
| `closure_audit_v23` | yes | `read-only-review` | current closure state before v2.4 |
| `source_join_scope_v22` | yes | `read-only-review` | do not enable tooltips before file-qualified joins |
| `release_checklist_v20` | yes | `read-only-review` | external upload/deposit remains Anton-controlled |
| `status` | yes | `read-only-review` | append-only summary surface |
| `manifest` | yes | `internal-consume` | must remain valid JSON |
| `drift_audit_v25` | yes | `read-only-review` | records 3 review-required drift rows against v2.4; superseded for current packet hashes by v2.6 |
| `drift_audit_v25_table` | yes | `read-only-review` | consume as provenance, not as current baseline |
