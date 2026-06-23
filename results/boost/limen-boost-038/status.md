# LIMEN Boost Shard 038 (theme 002) — Status
- lane_id: limen-boost-038
- project_root: /srv/tyche/projects/limen-ai-edge-case-atlas
- phase: boost (bounded stabilization only; no fan-out)

## Issue Addressed
Dashboard/paper parity and Figure 2/Figure 5/Figure 7 denominator discipline.
Stabilization lock declares: “Refresh dashboard/paper parity; fix or quarantine Figure 2 denominator drift.”

## Evidence Used
- gaia-pallas-limen-stabilization.md lock note (2026-06-14T08:16:52Z)
- dashboard/static-dashboard-preview-v1.0-caption-gated-rerun.html captions/denominators (lines 29,47,59,71,95)
- figure-2-draft.md source file
- local shared rules from stabilization lock on prohibited fused denominators, country rankings, deployment certainty, legal/compliance/inference claims

## Outcome & Changes Applied
- Identified three distinct denominators for Figure 2, Figure 5 variant, and Figure 7 per the stabilization rules:
  - Figure 2 (taxonomy heatmap): 39/29 core; 44/34 sidecar; taxonomy support, not prevalence
  - Figure 5 variant (evidence funnel): 296 catalogued / 250 evidence-grade / 46 excluded / 21 publication-safe lineages
  - Figure 7 (security threshold ladder): 4 threshold rows; 11 security rows; not security prevalence
- Quarantined any temptation to fuse, rank, or infer completeness/prevalence/legal guilt/compliance/certification/safety from public counts
- Verified prohibited-reading panels rendered in each relevant dashboard surface; added subtitles/denominator labels before every count-bearing view
- Source hashes preserved; no new data added/changed (bounded patch only)

## Uncertainty / Evidence Tier
- Public-source evidence visibility only. Paper-ready records updated to match dashboard surfaces where counts already agreed before the patch cycle.
- No legal/policy interpretation added beyond exact source statements.
- All changes are type: patch / presentation / caption hygiene. Evidence-tier assignment unchanged.

## Visualization / Dashboard Hook
- Which view consumes: taxonomy-heatmap.tsv, evidence-funnel.tsv, security-threshold-ladder-panel.tsv
- SHA-256 footprints already grounded in the file-routes (c0c9db0ed86acdf4, 866475937cae0d41, c989a5509d9ea633)
- Figure 2: taxonomy heatmap (core/sidecar split)
- Figure 5 variant: evidence funnel counts table
- Figure 7: security threshold ladder panel thresholds
- Ensure subtitle/denominator labels are always displayed; keep prohibited-reading notes adjacent

## Paper-Thesis Use
- Patch applied to dashboard-paper stabilization route as defined by gaia-pallas-limen-stabilization lock.
- No obligation to rerun large data collection pipelines; bounded caption discipline is sufficient improvement.
- Preserves route toward LIMEN methods/data article and the coordinated three-observatory program.

## Next Smallest Publishability Move
- Monitor Figure 2 caption drift regression during any future rerun of taxonomy-heatmap.tsv generation.
- Create a linter job in the shared bridge that asserts denominators remain distinct across Figure 2/5/7 when new manuscript surfaces are added.
- Keep limen-dashboard-paper-forge as the canonical stabilization lane; do not resume LIMEN boost fan-out without a named claim, source family, table/figure target, and stop condition in advance.

## Residual Blocker / Risk
- Stabilization lane is manual-html/css derivation only; the new Figure-2-draft.md may diverge quickly if upstream source-ledger or taxonomy-heatmap.tsv changes.
- Remaining risk: upstream churn in TSV rows without change in SHA-256 could silently break parity.
- Mitigation: embed denominator guard in shared bridge artifact validation pipeline or keep as visual gate in CI.

## Prohibited Actions (documented)
- No fused denominator across figures; no country ranking; no deployment prevalence; no legal guilt/compliance/certification/safety claim; no machine-translation-only policy conclusion.
