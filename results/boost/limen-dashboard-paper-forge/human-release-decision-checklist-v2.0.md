# LIMEN human release decision checklist v2.0

Generated UTC: 2026-06-19T08:24:02Z
Lane: `limen-dashboard-paper-forge`
Project: `limen-ai-edge-case-atlas`

## Purpose

This is an internal human-facing release decision artifact for the LIMEN dashboard/paper package. It converts the passing automated gates into a bounded checklist for Anton-side review. It is not a submission, deposit, upload, certification, legal review, safety assurance, or public release.

## Summary

- Automated pre-submit package gate: PASS (`9/9`, `0 FAIL`, `0 WARN`) at current cycle start.
- Caption-currentness pytest: PASS (`2 passed`).
- Manifest syntax: PASS before this checklist write.
- External actions remain blocked for the lane: Zenodo deposit and F1000Research upload require Anton-controlled action.
- Safe claim ceiling: dashboard/paper parity and internal package consistency only.

## Checklist

| check_id | surface | state | finding |
|---|---|---|---|
| HRDC-001 | STOP-file safety | PASS | No global/project/lane STOP file observed before work; no crawling, upload, deposit, email, portal, or public release action performed. |
| HRDC-002 | Automated pre-submit gate | PASS | tools/limen_pre_submit_check.py passed 9/9 with 0 FAIL and 0 WARN at current cycle start. |
| HRDC-003 | Caption-currentness test | PASS | pytest tests/test_limen_caption_currentness_gate.py passed 2/2. |
| HRDC-004 | Manifest syntax | PASS | python3 -m json.tool manifest.json passed before this checklist write. |
| HRDC-005 | Human-only external actions | BLOCKED_BY_POLICY | Zenodo deposit and F1000Research upload remain outside lane authority and require Anton-controlled action. |
| HRDC-006 | Claim ceiling for release card | PASS_WITH_LIMITATION | The safe public-facing sentence is package-readiness/internal consistency, not completeness, prevalence, legality, safety, certification, endorsement, or country ranking. |
| HRDC-007 | Row-level rights/access labels | BLOCKED_FOR_PUBLIC_TOOLTIP | Row-level access-date/rights/terms labels remain blocked except where file-qualified source joins are manually verified. |
| HRDC-008 | Dashboard/paper parity next action | READY_FOR_HUMAN_REVIEW | Next smallest move is human review of the release card and external submission checklist, not broad crawling. |

## Evidence/provenance inputs

- `manifest.json` — d03624a76e740d7d4c2e3a3e82eff33b1ddc3f8ff0d5654d544096b6801f5988
- `results/dashboard-paper/status.md` — fbabf6888f05f8139acf03dbd510b6e6680e322b155eadaf1037c1f30e5b2776
- `tools/limen_pre_submit_check.py` — 0db4c5154a92c2dfb5c15a8693c3d48ca36d454418c2e57a6f83fed61ec1bb32
- `tests/test_limen_caption_currentness_gate.py` — 76ecdcdca0a0380847c1ce4080421080ff2cb50ce519392e0c7816dfdf893f0d
- `draft/preprint-v0.3-f1000.md` — 74f77d887bf2dca2635cef96b0f8d177c1ecdd519f9bfec8c2d07a43599929cf
- `draft/cover-letter-f1000.md` — 364ee1eb8292f019708bf48ffb778c2ed38fced01876bb1bb482c3a1e5ae8771
- `draft/f1000-submission-kit.md` — 66269525465eae28648bca9f52fd751e334f285dcd7e85eb971e2ac3190690fc
- `dashboard/limen-dashboard-api-bundle-v0.1.json` — 722fa3655e3c4b504d8100b1514ed53d8b7f8e1daa17334b456a0b30a7649219
- `dashboard/static-dashboard-preview-v0.1.html` — 085e09d896bed3ddd207b6f57ea9a03bacad8ec1f29b9508e54f427446948a70
- `results/dashboard/source-ledger-join-v0.1.tsv` — 0a87c7f27f2e8c040258b17c78d6204a4298f8f5e3f117092f5b8e61de41851d

Checklist TSV: `results/boost/limen-dashboard-paper-forge/human-release-decision-checklist-v2.0.tsv`  
Checklist TSV SHA-256: `9457979b032ae4765bb6d7630f4bc8f0da45d5e66d322bbd54c6837ceceb7c19`

## Reviewer-safe release-card wording

`The local LIMEN dashboard/paper package has passed its internal pre-submit consistency checks and currently supports methods/data-paper claims about provenance, denominator discipline, dashboard/paper parity, and claim-boundary control. It does not by itself support claims of corpus completeness, prevalence, legal compliance or violation, safety, certification, deployment status, country ranking, source truth, or third-party endorsement.`

## Remaining external blockers

1. Anton-controlled Zenodo decision/deposit, if used.
2. Anton-controlled F1000Research upload, if used.
3. Human final read of manuscript, cover letter, SI package, figure captions, and public-affiliation text.
4. Any post-edit rerun of `python3 tools/limen_pre_submit_check.py --project-root /srv/tyche/projects/limen-ai-edge-case-atlas` plus `pytest -q tests/test_limen_caption_currentness_gate.py`.

## Observatory hook

Dashboard release-card UI can consume `results/boost/limen-dashboard-paper-forge/human-release-decision-checklist-v2.0.tsv` as a `package_health/human_decision` panel with fields `check_id`, `surface`, `state`, `finding`, `provenance`, and `claim_ceiling`. Interpretation should emphasize readiness gates and blocked external actions, not empirical counts.
