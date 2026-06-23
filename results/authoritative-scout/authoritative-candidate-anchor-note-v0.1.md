# Authoritative candidate anchor note v0.1

- Date (UTC): 2026-06-07T17:51:48Z
- Lane: `limen-regulator-court-enforcement-scout`
- Scope: selective anchor extraction for authoritative FTC complaint/final-order candidates already captured in `sources/authoritative-source-ledger.tsv`

## What changed

- Added `results/authoritative-scout/authoritative-candidate-anchor-matrix-v0.1.tsv`, a four-row quote/paraphrase control table for `LIMEN-000010` (DoNotPay) and `LIMEN-000011` (Workado).
- Refreshed `data/cases/authoritative-candidates.jsonl` so both FTC rows now point manuscript-anchor reuse at the new candidate-anchor matrix instead of only the higher-level promotion register.
- Kept package roles explicit inside the anchor rows: DoNotPay remains a bounded shared non-finance sidecar, while Workado now travels as a bounded shared authoritative-core detector-governance row with complaint-versus-final-order discipline preserved.

## Reviewer-safe interpretation

- This cycle converts already captured FTC PDFs into article-ready anchor material without widening claim ceilings beyond the complaint/final-order record; later package-state controls subsequently promoted Workado into the shared authoritative core while leaving DoNotPay as the bounded non-finance sidecar.
- The anchor matrix sharpens the distinction between complaint-stage capability/allegation wording and final-order prohibition/remedy wording, which reduces later overread risk in manuscript, dashboard, and thesis reuse.
- The new artifact is immediately reusable for the non-finance AI-claim diversification sidecar, shared authoritative-core detector-governance wording, and reviewer-response prose about why the two FTC rows are not interchangeable even after Workado's core promotion.

## Remaining blocker

- DoNotPay still should not be treated as unauthorized-practice adjudication, hidden-human final-authority closure, or a denominator-changing Table 1C core row by default.
- Workado still should not be treated as a general detector-validity verdict, but it no longer remains frontier-only: it is now a bounded detector-governance official row inside the shared authoritative core, with complaint-versus-final-order posture and overread limits still explicit.
- Neither FTC row changes the main `sf08` court/public-record blocker or the accusation-stage ceiling on `LIMEN-000005`.
