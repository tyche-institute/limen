# Authoritative anchor priority note v0.1

- Date (UTC): 2026-06-07T07:25:55Z
- Scope: `data/cases/authoritative-candidates.jsonl` and `sources/authoritative-source-ledger.tsv`
- Purpose: convert the authoritative package from "document present" into a publication-safe anchor extraction queue.

## What changed

- Five rows are now explicitly treated as selective-anchor-ready for manuscript/table use: `LIMEN-000001`, `LIMEN-000003`, `LIMEN-000004`, `LIMEN-000006`, and `LIMEN-000007`.
- `LIMEN-000002` remains blocked not by translation or drafting work but by missing court-facing text.
- `LIMEN-000005` is mixed-state: the DOJ summary is quote-ready for accusation-stage wording, but exact caption/docket metadata remains normalization-limited.

## Reviewer-safe interpretation

- The next authoritative-package gain is not broad harvesting; it is selective anchor extraction from the strongest direct-document rows so manuscript prose and table captions can cite narrow document text instead of only row summaries.
- The package should keep two blocker classes visibly separate: source-absence (`LIMEN-000002`) versus normalization-limited captured document (`LIMEN-000005`).
- Non-English burden is currently concentrated in one high-value row (`LIMEN-000001`), which makes a small human-reviewed Italian anchor pass more defensible than another broad multilingual expansion attempt inside this lane.

## Next smallest publishability move

- Extract compact anchor sets for the four English direct-document rows plus the Italian order row before doing more same-family expansion.
- Keep `LIMEN-000002` on a separate court-surface route and do not let its blocker delay anchor extraction for rows that are already publication-safe.
- Treat the resulting anchor set as a future input for the manuscript, dashboard caption register, and claim-support table.
