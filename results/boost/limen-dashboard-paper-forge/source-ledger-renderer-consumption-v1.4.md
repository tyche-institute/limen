# LIMEN source-ledger renderer consumption v1.4

Generated UTC: 2026-06-19T01:55:00Z
Lane: `limen-dashboard-paper-forge`
Project: `limen-ai-edge-case-atlas`

## Purpose

This bounded cycle closes the v1.3 blocker by making the local dashboard renderer/API gates consume `results/dashboard/source-ledger-join-v0.1.tsv` directly. The source-ledger join is now an executable render condition, not only a prose artifact.

No new crawling, network access, upload, deposit, portal action, row promotion, incident validation, legal/compliance assessment, source-truth assessment, or denominator relaxation was performed.

## Code changes

- `tools/limen_dashboard_ui_contract_check.py` now fails a view if any rendered TSV row lacks a matching `(dashboard_view, row_key)` in `results/dashboard/source-ledger-join-v0.1.tsv`, or if a join row lacks `public_dashboard_action`.
- `tools/build_limen_dashboard_api_bundle.py` now reads `results/dashboard/source-ledger-join-v0.1.tsv`, adds top-level join provenance/checksum metadata, enriches rendered sample rows with `_source_ledger_join`, and exposes `source_ledger_join_actions` per view.
- `tools/build_limen_static_dashboard_preview.py` now reads the same join table, fails closed on missing join rows, and renders per-view join-action summaries in the static preview.

## Machine-readable outputs

| artifact | result | notes |
|---|---:|---|
| `results/boost/limen-dashboard-paper-forge/dashboard-ui-contract-fail-closed-check-source-ledger-consumption-v1.4.tsv` | 7/7 PASS | UI contract now checks join coverage |
| `results/boost/limen-dashboard-paper-forge/dashboard-api-bundle-gate-v1.4.tsv` | 7/7 PASS | API bundle gate now carries join-action summaries |
| `results/boost/limen-dashboard-paper-forge/static-dashboard-preview-gate-v1.4.tsv` | 7/7 PASS | Static preview gate now carries join-action summaries |
| `dashboard/limen-dashboard-api-bundle-v0.1.json` | rebuilt | includes `source_ledger_join` and `source_ledger_join_sha256` |
| `dashboard/static-dashboard-preview-v0.1.html` | rebuilt | displays source-ledger join-action summaries |

## Verification

Commands run from `/srv/tyche/projects/limen-ai-edge-case-atlas`:

```bash
python3 -m py_compile tools/limen_dashboard_ui_contract_check.py tools/build_limen_dashboard_api_bundle.py tools/build_limen_static_dashboard_preview.py
python3 tools/limen_dashboard_ui_contract_check.py --write-artifacts --stamp source-ledger-consumption-v1.4
python3 tools/build_limen_dashboard_api_bundle.py --write-gate-tsv results/boost/limen-dashboard-paper-forge/dashboard-api-bundle-gate-v1.4.tsv
python3 tools/build_limen_static_dashboard_preview.py --write-gate-tsv results/boost/limen-dashboard-paper-forge/static-dashboard-preview-gate-v1.4.tsv
python3 -m json.tool manifest.json >/dev/null
pytest -q tests/test_limen_caption_currentness_gate.py
```

Observed results:

- Python compile: PASS.
- UI contract: PASS, 7/7 views.
- API bundle: PASS, 7/7 views.
- Static preview: PASS, 7/7 views.
- `manifest.json` parse: PASS.
- Caption-currentness unit tests: PASS, 2 passed.
- API bundle inspection: `source_ledger_join` present; 7/7 views contain join-action summaries.

## SHA-256 checksums

```text
8e5be4cc99235d664263661bd0d1fe4b346056d619cd414f48bd187b4b4c71eb  tools/limen_dashboard_ui_contract_check.py
8c62418e1a0d4065159720bd4c4fc4e183606a7a2c02330fd2a46fd56c5132eb  tools/build_limen_dashboard_api_bundle.py
833d7ec513456705002722f14ad0bced2d745071655833b38bfd67414682c750  tools/build_limen_static_dashboard_preview.py
2895d8d515a87e5bc78149dac78dff1e53d88fd9191bcfcedf6827ec3bb47636  dashboard/limen-dashboard-api-bundle-v0.1.json
142a870ffd69337df8bad968cffd7d6265bb4df9810e469fd049cdbeb55ec781  dashboard/static-dashboard-preview-v0.1.html
cca60b1e01c4b688b0f01e3e128a4b40170540fe122cc215bf408ad729defe0a  results/boost/limen-dashboard-paper-forge/dashboard-ui-contract-fail-closed-check-source-ledger-consumption-v1.4.tsv
2f6de784cc8c3842f075e57bfa7d4014687b281ac874668a055cd7b4193122d5  results/boost/limen-dashboard-paper-forge/dashboard-api-bundle-gate-v1.4.tsv
86a06b23d77fd5666a0f161e6bf16634aca56390fa69e6d03ace8b4b598f515f  results/boost/limen-dashboard-paper-forge/static-dashboard-preview-gate-v1.4.tsv
```

## Interpretation

Evidence: all seven bounded dashboard release-card views now require a join-action row before rendering. The renderer can distinguish family-level notes, candidate review links, and blocked row-level access/rights badges.

Interpretation: this strengthens dashboard/paper parity and hostile-reviewer provenance-label discipline. It does not convert family-level or aggregate rows into verified per-source access-date/rights facts.

## Claim ceiling

This artifact supports package-integrity, dashboard/paper parity, row-action provenance controls, and reproducible renderer gating only. It does not support completeness, prevalence, incident truth, legal guilt, compliance, certification, safety assurance, deployment claims, country ranking, official endorsement, source-truth claims, or a fused GAIA/PALLAS/LIMEN denominator.

## Next smallest publishability move

Patch `dashboard/limen-dashboard-spec-v0.1.md`, `papers/article-architecture-v0.1.md`, and `results/dashboard-paper/status.md` to cite v1.4 as the current source-ledger renderer gate, then keep broad crawling closed unless a specific manuscript sentence needs a bounded source-family gap check.
