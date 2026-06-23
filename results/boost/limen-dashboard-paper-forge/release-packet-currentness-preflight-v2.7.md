# LIMEN release-packet currentness preflight v2.7

- Updated UTC: 2026-06-19T12:58:00Z
- Lane: `limen-dashboard-paper-forge`
- Input baseline: `results/boost/limen-dashboard-paper-forge/human-release-packet-index-v2.6.tsv`
- Companion table: `results/boost/limen-dashboard-paper-forge/release-packet-currentness-preflight-v2.7.tsv`
- Companion SHA-256: `e147511dccb909f039475ab76378d0edaf0285d987b1ea6a6829779542d6dfa9`
- External actions performed: `0`

## Purpose

This preflight checks whether the v2.6 human release packet baseline still matches the local package before any new broad collection, upload, deposit, or portal action. It is a bounded package-integrity artifact for human release review, not a new empirical count surface.

## Result before this v2.7 write

- Packet rows checked: `15`.
- Hash matches against v2.6: `15`.
- Drift rows before this write: `0`.
- Missing rows before this write: `0`.

All v2.6 packet rows matched the local files at the start of this cycle. The subsequent v2.7 status/journal/manifest append will intentionally move append-only/control files, so a future release handoff should read this v2.7 audit as the currentness evidence for the pre-edit package state and rerun the same check after any further edit.

## Interpretation

The package remains suitable for internal human release review: no required indexed file was missing, no unexpected hash drift was detected against the v2.6 current baseline, and the automated package gates passed immediately before this artifact was written. This does not authorize external release and does not change dashboard denominators or manuscript claims.

## Claim ceiling

Supports package-integrity, release-review routing, and dashboard/paper parity only. It does not validate incidents, promote rows, prove source truth, establish legal compliance or non-compliance, establish safety, prove prevalence/completeness, rank countries, authorize public release, or merge GAIA/PALLAS/LIMEN denominators.

## Observatory hook

A dashboard can consume the TSV as a non-count-bearing `release_packet_currentness_preflight` panel. Suggested fields: `packet_id`, `path`, `currentness_state_before_v2_7_write`, `allowed_action`, `review_consumer`, `claim_ceiling`, and `note`. Interpretation: `MATCH` means the internal release-review packet baseline is locally reproducible at the audit time; external deposit/upload remains Anton-controlled.

## Verification

- Pre-write gate at 2026-06-19T12:56:27Z: `python3 -m json.tool manifest.json` PASS; `python3 tools/limen_pre_submit_check.py --project-root /srv/tyche/projects/limen-ai-edge-case-atlas` PASS (`9/9`, `0 FAIL`, `0 WARN`); `pytest -q tests/test_limen_caption_currentness_gate.py` PASS (`2 passed`).
- Hash-currentness table: `15/15` rows MATCH, `0` DRIFT, `0` MISSING before v2.7 writes.

- Post-write gate at 2026-06-19T12:57:27Z: manifest JSON PASS; LIMEN pre-submit check PASS (`9/9`, `0 FAIL`, `0 WARN`); caption-currentness pytest PASS (`2 passed`).

## Packet-currentness summary

| state | rows |
|---|---:|
| MATCH | 15 |
| DRIFT | 0 |
| MISSING | 0 |
