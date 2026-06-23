# Taxonomy residual and category-pressure note

Generated: 2026-06-06T23:38:24Z
Lane: `limen-boost-010`
Method: local-only synthesis across authoritative, security, multilingual, and shard-009 local case artifacts using file-qualified case references to avoid namespace-collision errors.

## Why this cycle

The hostile-reviewer sprint asks for visible claim support and for weak or stale framing to be repaired. LIMEN already had a taxonomy/crosswalk package, but the current local corpus has moved faster than the crosswalk counts. This cycle therefore audited category pressure rather than collecting more leads.

## Empirical base

- 17 local case rows reviewed from 4 local files.
- 15 LIMEN top-level categories checked against `taxonomy/taxonomy-v0.1.md`.
- 12 categories now have at least one local row; 3 remain zero-seed (`health_medical_or_mental_health`, `research_integrity`, `residual_unclassified`).
- 10 categories now exceed the seed counts still shown in `results/crosswalks/legal-normative-crosswalk-v0.1.tsv`.

## Main findings

1. Residual pressure is currently better described as crosswalk lag than as `residual_unclassified` usage.
   - The residual bucket still has zero assigned rows.
   - But several categories that previously looked empty are now populated by local shard outputs that the shared legal/normative crosswalk does not yet count, especially `ai_washing_or_false_ai_claim`, `finance_insurance_or_market`, `institutional_absurdity`, and `deepfake_or_synthetic_identity`.

2. The strongest repeated combinations still fit the existing top-level taxonomy.
   - `agentic_control_failure` + `security_risk`: 5 rows (`security-agentic-candidates.jsonl:LIMEN-000001`; `security-agentic-candidates.jsonl:LIMEN-000002`; `security-agentic-candidates.jsonl:LIMEN-000003`; `security-agentic-candidates.jsonl:LIMEN-000004`).
   - `ai_washing_or_false_ai_claim` + `finance_insurance_or_market`: 2 rows (`candidate-cases.jsonl:LIMEN-000001`; `candidate-cases.jsonl:LIMEN-000002`).
   - This supports subtype/table work before any new top-level category split.

3. Reviewer-visible gap categories are now narrower and more defensible.
   - True zero-seed gaps are only health/medical, research integrity, and the intentionally preserved residual bucket.
   - Categories that still need support are often not empty; they are mixed-tier bridges with multilingual or candidate-heavy evidence that needs verification rather than recoding.

## Proposed interpretation discipline

- Do not describe `institutional_absurdity`, `deepfake_or_synthetic_identity`, `finance_insurance_or_market`, or `ai_washing_or_false_ai_claim` as unseeded anymore; local rows now exist.
- Keep `residual_unclassified` visible as a methods signal, but do not force multilingual weak leads into it just because direct-source resolution is incomplete.
- Treat mixed `T1` + `T3` categories as bridge zones for hostile-reviewer tables: the category exists, but the evidence stack remains heterogeneous.

## High-value dashboard/paper hooks

- `category-pressure.tsv` can feed the planned taxonomy support heatmap with columns for local count, authoritative/candidate split, crosswalk lag, and pressure status.
- A manuscript paragraph can now say that LIMEN has local support in 12/15 top-level categories, while only 3 categories remain true zero-seed gaps in the current local package.
- The delta-vs-crosswalk column is a quality-control signal: it shows where shared synthesis artifacts are stale relative to lane outputs.

## What this strengthens

- First LIMEN article package: sharper novelty claim around residual logic without falsely implying that most categories are still empty.
- Thesis use: a cleaner distinction between taxonomy novelty, evidence heterogeneity, and shared-ledger maintenance.
- Observatory use: category heatmap and dashboard readiness become more accurate without adding new external data.

## Uncertainty and evidence tier

- This is a local-corpus audit, not a claim about global prevalence.
- Several newly counted categories rely partly or entirely on `T1_single_public_source` multilingual leads and must stay provisional until direct-source resolution or corroboration occurs.
- Shard-local ID collisions remain real, so file-qualified references were used throughout.

## Next smallest publishability move

Update the shared legal/normative crosswalk or dashboard-layer heatmap from this local pressure table, then verify one candidate-heavy category (`deepfake_or_synthetic_identity` or `institutional_absurdity`) with direct-source follow-up so the article can replace gap language with mixed-tier language.
