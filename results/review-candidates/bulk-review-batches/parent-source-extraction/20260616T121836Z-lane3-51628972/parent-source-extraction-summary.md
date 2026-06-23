# Parent source extraction summary — 20260616T121836Z-lane3-51628972

Completed bounded local-only parent-source extraction for 24 input rows.

Verdict counts:

| verdict | count |
|---|---:|
| source_url_extracted | 1 |
| parent_source_wrapper | 6 |
| country_gap_no_parent_source | 17 |
| source_surface_only_no_case | 0 |
| duplicate_existing_core | 0 |
| reject_noise | 0 |

Verification:
- Input rows: 24
- Output rows: 24
- Queue IDs: exact set match verified during write.
- Local-only boundary observed; no web crawl, portal submission, publication, upload, email, registration, payment, legal/safety/compliance finding, prevalence, or ranking.

Notes:
- One concrete URL was extracted from local NL hardening source context: `https://algoritmes.overheid.nl/nl`.
- Source-family/summary/gap-sprint wrappers were retained as wrappers where local context required a human or subsequent bounded extractor to choose a concrete parent source.
- Country research/profile/score placeholders without explicit URLs were marked `country_gap_no_parent_source`.
