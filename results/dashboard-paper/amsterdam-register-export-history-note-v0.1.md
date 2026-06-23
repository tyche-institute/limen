# Amsterdam register export/history audit note

Date: 2026-06-07T09:57:46Z
Source lane: `limen-regulator-court-enforcement-scout`
Sprint: `20260607-hostile-reviewer-pass`

## Why this artifact exists

`sf08` remained stalled after bounded court-surface checks, and `next.md` explicitly routes the next substantive blocker pass to `sf09` exact-row/public-impact strengthening rather than to more register-like expansion. This audit exploits one existing municipal register row instead of widening the corpus.

## Bounded result

The Dutch ChatAmsterdam row now has a stronger exact-row provenance story than the shared note previously exposed:

- the official Dutch register API returns one current CSV export for `algorithm_id=23189993` and `org_id=gm0363`;
- the same API returns a 10-row downloadable revision-history CSV in Dutch;
- the same current+history export pair is also public in English;
- the history exports show a status transition (`In ontwikkeling` -> `In gebruik` / `In development` -> `In use`) and a provider-string wording change (`GPT4.0` -> `GPT4o`) while preserving the same stable identifiers.

This strengthens exact-row provenance, revision visibility, and bilingual exportability for Amsterdam. It does not solve the buyer-side procurement blocker and it does not add public legal-basis, source-code, process-index, or source-id fields.

## Reviewer-safe ceiling

Use this artifact for narrow claims that the Amsterdam municipal register exemplar is not only page-visible but machine-readable and revision-visible through public CSV exports. Do not turn that into claims about procurement transparency, implementation efficacy, legal basis, downloadable DPIA access, or public-code disclosure.

## Shared-table implication

For `LIMEN-VIS-008` / `CCR-015`, Amsterdam can now be described as:

- register-rich;
- tested public routes still show no exact-name procurement hit;
- same-buyer Azure/Public Cloud procurement-family bridge publicly visible below exact row-linked buyer-side or public-companion proof;
- exact-row machine-readable current+history export available.

That is stronger than page-only register visibility but still below Helsinki's family-level buyer-side procurement companion for acquisition traceability.

## Observatory hook

Suggested additional fields for a dashboard or appendix slice:

- `exact_row_export_available`
- `history_export_available`
- `history_row_count`
- `bilingual_export_available`
- `stable_identifier_present`
- `buyer_side_traceability_level`
- `blank_structured_fields`

## Next smallest publishability move

Either capture one buyer-side tender/award/contract/public-assessment companion for Amsterdam or Helsinki, or reuse this audit directly in methods/limitations prose so reviewers can see that exact-row export depth and buyer-side traceability are separate dimensions.
