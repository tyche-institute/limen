# LIMEN static dashboard preview artifact

Generated: 2026-06-18T13:00:00Z
Lane: `limen-dashboard-paper-forge`
Project: `limen-ai-edge-case-atlas`
Sprint: `20260607-hostile-reviewer-pass`

## Purpose

This cycle converts the existing dashboard release-card/UI contract into a local, offline, reviewer-readable static dashboard preview. The preview is a bounded dashboard/paper parity artifact, not a public release.

It renders seven count-bearing dashboard surfaces only after a fail-closed gate confirms that the local TSV export still matches the release-card config by source path, row count, SHA-256, denominator/subtitle guardrail, required tooltip fields, prohibited-reading warning, and claim-boundary text.

No new collection, network access, upload, deposit, submission, portal action, or claim-ceiling relaxation was performed.

## Artifacts created

| Artifact | Role | SHA-256 |
|---|---|---|
| `tools/build_limen_static_dashboard_preview.py` | Offline renderer and gate exporter | `bcc0148c666d60137d18629ec1c8ecba7997f7940e53b15160d048ef6e968efb` |
| `dashboard/static-dashboard-preview-v0.1.html` | Human-readable static dashboard preview generated from the fail-closed config | `dd289fa0be62d7c5e9a2b934559e54a38dab126695ea68d4e1555264cb7246d5` |
| `results/boost/limen-dashboard-paper-forge/static-dashboard-preview-gate-2026-06-18T13-00-00Z.tsv` | Machine-readable render gate result for all views | `5db61789e6868f0e42510010af725e31b206a00e3afde2f590dcbb414bef63f8` |

## Gate result

Command run:

```bash
python3 tools/build_limen_static_dashboard_preview.py \
  --project-root /srv/tyche/projects/limen-ai-edge-case-atlas \
  --output dashboard/static-dashboard-preview-v0.1.html \
  --write-gate-tsv results/boost/limen-dashboard-paper-forge/static-dashboard-preview-gate-2026-06-18T13-00-00Z.tsv
```

Result:

| Metric | Value |
|---|---:|
| Verdict | PASS |
| Dashboard views checked | 7 |
| Views allowed to render | 7 |
| Views fail-closed | 0 |

The preview includes only compact row samples from existing TSV exports; full data remains in the source files listed in `dashboard/release-card-ui-config-v0.1.json`.

## Dashboard surfaces rendered

| Dashboard view | Source export | Guardrail interpretation |
|---|---|---|
| `source_family_saturation` | `results/dashboard/source-family-coverage.tsv` | Source-family saturation and uncertainty, not completeness. |
| `taxonomy_heatmap` | `results/dashboard/taxonomy-heatmap.tsv` | Core 39/29 and sidecar 44/34 taxonomy support, not prevalence. |
| `evidence_tier_funnel` | `results/dashboard/evidence-funnel.tsv` | 296 catalogued / 250 evidence-grade / 46 excluded / 21 publication-safe lineages where used. |
| `jurisdiction_language` | `results/dashboard/jurisdiction-language-coverage.tsv` | 34 jurisdictions broad; 12 reviewed-core non-English rows where panel used; no country ranking. |
| `legal_uncertainty` | `results/dashboard/legal-uncertainty-matrix.tsv` | Uncertainty routing only; no compliance/liability conclusion. |
| `security_agentic_threshold` | `results/dashboard/security-threshold-ladder-panel.tsv` | 4 threshold rows; 11 security rows where described; not security prevalence. |
| `duplicate_review_graph` | `results/dashboard/duplicate-review-graph.tsv` | 27 duplicate-review edges; 0 merge decisions; not proof all duplicates are absent. |

## Validation

Additional checks run after preview generation:

```bash
python3 tools/limen_dashboard_ui_contract_check.py --project-root /srv/tyche/projects/limen-ai-edge-case-atlas
python3 tools/limen_pre_submit_check.py --project-root /srv/tyche/projects/limen-ai-edge-case-atlas
```

Results:

- Dashboard UI contract check: PASS, 7/7 views renderable, 0 failures, 0 warnings.
- LIMEN pre-submit self-check: PASS, 8/8 checks pass, 0 FAIL, 0 WARN.

## Paper-readiness delta

This moves LIMEN from a machine-readable dashboard UI contract to a concrete offline dashboard preview that a reviewer or coauthor can open locally. The preview makes denominator labels, claim ceilings, prohibited readings, checksums, and row samples visible in the same surface, reducing the risk that a future interactive dashboard silently drops the hostile-reviewer guardrails.

## Claim boundary

This artifact verifies local renderer/config/export consistency only. It does not support completeness, prevalence, legal guilt, legal compliance, certification, safety assurance, official incident status, country ranking, third-party endorsement, or source-truth claims.

## Observatory hook

A future interactive dashboard can use `tools/build_limen_static_dashboard_preview.py` as a minimal reference implementation: import `dashboard/release-card-ui-config-v0.1.json`, verify row count and SHA-256 before rendering, display the subtitle/prohibited-reading warning next to every count-bearing view, and fail closed when any gate fails.

## Remaining blocker / next smallest move

Before any public interactive release, keep row-level access-date and rights/terms labels hidden unless source-ledger joins are verified. If a concrete dashboard app is added, wire it to the same fail-closed gate or reuse the generated TSV as a build-time release blocker.
