# LIMEN review-candidate adjudication batch 20260614T0820Z

Scope
- Ledger: `/srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/all-signals-review-candidates.tsv`
- Batch rule: first 120 rows in ledger order with `review_priority = P1_official_or_regulator_review`
- Network use: none; first-pass adjudication used only local ledger metadata (`source_path`, `snippet`, `queries`, `shards`)
- Boundary: this is candidate review only, not reviewed-core promotion and not an incident/legal/compliance/deployment finding

Counts by verdict
- `promote_to_source_review`: 24
- `merge_with_existing_surface`: 41
- `reject_as_cross_project_noise`: 9
- `hold_needs_direct_source`: 39
- `hold_needs_human_translation`: 0
- `hold_low_relevance`: 7

Reviewer-safe interpretation
- The batch contains a meaningful minority of plausible direct official/regulator surfaces, especially public AI register / algorithm register rows and some named sandbox/regulator pages, but most P1 rows are still derivative packaging artifacts or proxy/gap signals.
- Internal digests, prompts, draft tables, preprint packages, and claim-support summaries should not consume fresh review slots when they already point to an underlying source family; they are better merged back into the existing reviewed surface.
- A non-trivial residue of rows was over-prioritized into P1 even though the snippet is scholarly/theory context, GAIA cross-project material, or weak proxy evidence. Those rows are useful as corpus residue, but not as immediate LIMEN official/regulator review candidates.
- No row in this batch supports incident truth, legal violation, safety status, compliance status, deployment prevalence, or country ranking. At most, promoted rows justify opening a direct source review on the named official/regulator surface.

Pattern notes
- Strongest promote class: named official register rows from public-ai-registry packages and named regulator/sandbox surfaces from PALLAS source packs.
- Dominant merge class: Atlas/PALLAS/LIMEN internal digests, prompts, packaging tables, drafts, and code/config artifacts that summarize another surface.
- Dominant hold class: source-pack proxy rows, gap notes, open-data portals, UN knowledgebase references, and seed/query artifacts that still need a directly reviewable official page.

Observatory hook
- `batch-adjudication.tsv` can feed a reviewer funnel view with verdict counts, candidate-role breakdowns, and a "direct-reviewable vs derivative vs proxy" split for the LIMEN dashboard/paper pipeline.
- Recommended derived fields for later visualization: `verdict_group`, `is_direct_surface_candidate`, `is_derivative_artifact`, and `needs_named_source_resolution`.
