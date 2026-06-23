# Parent source extraction summary

Batch: 20260616T124840Z-lane4-4e7922a6

Input rows reviewed: 1
Output rows written: 1

Verdict counts:
- parent_source_wrapper: 1

Review notes:
- BPSE-01825 / LIMEN-SIGNAL-FFFBA21EDBBF53BD points at the Liechtenstein row in `PALLAS_OBSERVABILITY_COUNTRY_INDEX.csv:121`.
- Nearby local context and the local source-refresh ledger show LI I08 procurement entries at `PALLAS_SECOND_PASS_SPRINT_13_SOURCE_REFRESH.csv:150-151`, but they are general procurement surfaces and the ledger preserves the no-AI-specific-procurement-guidance caveat.
- No original public URL was extracted into the result because the row remains a wrapper requiring human selection of a single parent source before direct source review.

Boundary preserved: processing-state review only; no reviewed-core promotion, ObscureAI addition, incident truth, legal finding, safety finding, compliance finding, prevalence, or ranking.
