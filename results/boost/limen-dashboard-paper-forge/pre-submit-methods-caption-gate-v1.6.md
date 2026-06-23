# LIMEN pre-submit methods/caption gate v1.6

Updated UTC: 2026-06-19T04:35:45Z
Lane: `limen-dashboard-paper-forge`

## Purpose

Convert the v1.5 Methods/caption export audit from a lane artifact into an executable pre-submission package gate. This is a bounded hostile-reviewer hygiene patch: it checks dashboard/paper parity, current caption/export controls, and manuscript residue discipline before any submission-package use.

## Actions

1. Patched `tools/limen_pre_submit_check.py` to import `csv`, require `results/boost/limen-dashboard-paper-forge/methods-caption-export-audit-v1.5.tsv`, and fail closed unless required rows `MCE-001`..`MCE-007` are present, marked `PASS`, and carry evidence / claim-ceiling / blocked-overread text.
2. Added a new `[9/9] Methods/caption export audit gate (v1.5)` stage to the pre-submit check.
3. Repaired `draft/preprint.md` by replacing the manuscript-facing boost-local path with a reviewer-clean reference to the v1.4 source-ledger renderer gate in the reproducibility package.

## Verification

| Check | Result | Notes |
|---|---:|---|
| `python3 -m py_compile tools/limen_pre_submit_check.py` | PASS | syntax check |
| `pytest -q tests/test_limen_caption_currentness_gate.py` | PASS | 2 passed |
| `python3 tools/limen_pre_submit_check.py --project-root /srv/tyche/projects/limen-ai-edge-case-atlas` | PASS | 9 PASS / 0 FAIL / 0 WARN |

Machine-readable gate ledger: `results/boost/limen-dashboard-paper-forge/pre-submit-methods-caption-gate-v1.6.tsv`
SHA-256: `07c9ce877914d1ed7631f16978db59b0ffdfec18d48e74224dd6b60fd40c8d03`

## Paper-readiness delta

The pre-submission self-check now consumes the dashboard/paper Methods-caption audit directly, so stale caption/export state or missing v1.5 gate rows become package blockers rather than prose-only warnings. The preprint also no longer leaks a boost-local path in manuscript-facing prose.

## Claim ceiling

This verifies package integrity, dashboard/paper parity, caption/export currentness, and residue hygiene only. It does not support any new incident validation, source-truth claim, row promotion, legal/compliance/safety/deployment/certification claim, prevalence/completeness claim, country ranking, public release, or fused GAIA/PALLAS/LIMEN denominator. Row-level access-date/rights/terms/license badges remain blocked until file-qualified source joins are manually verified.

## Observatory hook

The dashboard/API/static/PDF export pipeline can treat `pre-submit-methods-caption-gate-v1.6.tsv` as the final package gate before rendering or submission-package assembly. A dashboard status badge can expose `PSC-004=PASS` as "pre-submit gate current" while keeping row-level provenance badges disabled.

## Remaining blocker

Run the pre-submit gate after any future edit to `draft/preprint.md`, caption-control rows, dashboard TSVs, API/static outputs, figures, PDF exports, or Methods/caption audit files. External deposit/upload actions remain Anton-controlled and were not performed.
