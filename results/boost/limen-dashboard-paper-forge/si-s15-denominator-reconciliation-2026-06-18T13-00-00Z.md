# LIMEN SI S15 denominator reconciliation

Generated: 2026-06-18T13:00:00Z
Lane: `limen-dashboard-paper-forge`
Project: `limen-ai-edge-case-atlas`

## Purpose

Resolve the post-S15 manuscript/SI parity gap introduced when the standalone jurisdiction × tier table was materialized after the older 2026-06-14 reviewed-core panel.

## Inputs checked

- `draft/preprint.md`
- `draft/supplementary-information.md`
- `papers/article-architecture-v0.1.md`
- `results/dashboard-paper/venue-adaptation-scientific-data-2026-06-17.md`
- `results/dashboard-paper/supplementary-table-s1-spec-2026-06-17.md`
- `results/dashboard/supplementary-table-s1-panel-c-jurisdiction-tier.tsv`
- historical freeze: `results/dashboard-paper/reviewed-core-evidence-panel-2026-06-14.tsv`

## Changes made

1. `draft/preprint.md`
   - Abstract denominator changed from `248 cases / 32 jurisdictions` to `250 cases / 34 jurisdictions`.
   - §4.9 now explicitly cites `Supplementary Table S15` and states the current jurisdiction × tier result: 250 evidence-grade cases across 34 country/supranational jurisdictions, US 126/250, other 33 jurisdictions 1–14 rows each.
   - Data Availability changed from `Supplementary Tables S1–S14` to `Supplementary Tables S1–S15`.

2. `draft/supplementary-information.md`
   - Version history now records v0.1.2.
   - S15 reconciliation language now treats the 2026-06-14 evidence panel as a historical freeze, not the current controlling manuscript denominator.
   - Supplementary Figure S1 caption now explicitly identifies itself as a frozen 2026-06-14 tier-by-theme snapshot, preserving the older 248/32 denominator instead of silently conflicting with S15.

3. `papers/article-architecture-v0.1.md`
   - Claim C8 updated to 250 evidence-grade cases, T3 157 / T2 82 / T1 11, across 34 jurisdictions.
   - Added note that the +2 T2 delta versus the 2026-06-14 evidence panel is documented in S15 reconciliation notes.

4. `results/dashboard-paper/venue-adaptation-scientific-data-2026-06-17.md`
   - Reviewed-core demonstration updated to 250 cases.

5. `results/dashboard-paper/supplementary-table-s1-spec-2026-06-17.md`
   - S1 specification updated to 250 cases / 34 jurisdictions.
   - T2 row updated to 82 and 33%.
   - Panel C and article-ready caption updated to 34 jurisdictions.
   - Denominator-discipline note updated from 248-case to 250-case total.

## Verification

Current S15 source file:

- `results/dashboard/supplementary-table-s1-panel-c-jurisdiction-tier.tsv`
- 35 data rows plus header
- total row: T3 157, T2 82, T1 11, evidence-grade total 250
- top jurisdictions: United States 126, United Kingdom 14, Spain 13, Italy 11, Australia 10

Targeted scan results after patch:

- No `S1–S14` references remain in current preprint, article architecture, venue-adaptation note, or S1 spec.
- No stale `248 evidence`, `32 jurisdiction`, or `T2: 80` references remain in current preprint, article architecture, venue-adaptation note, or S1 spec.
- Remaining `248/32/T2=80` references in `draft/supplementary-information.md` are explicitly historical: S15 reconciliation note and frozen Supplementary Figure S1 snapshot.

## Claim ceiling

This reconciliation does not change LIMEN's claim ceiling:

- no completeness claim
- no prevalence claim
- no country ranking
- no legal/compliance/certification claim
- no fused GAIA/PALLAS/LIMEN denominator

The result strengthens dashboard/paper parity by making the current S15 jurisdiction × tier denominator visible while preserving the older Figure S1 snapshot as a historical tier-by-theme artifact.

## Next smallest publishability move

If time permits, regenerate Supplementary Figure S1 from a current 250-case tier-by-theme matrix or explicitly leave it as a frozen 2026-06-14 validation snapshot in the submission package. The latter is currently safe because the caption now names the freeze state.