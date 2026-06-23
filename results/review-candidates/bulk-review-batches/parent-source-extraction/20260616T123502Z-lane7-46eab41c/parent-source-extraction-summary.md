# Parent-source extraction summary

Batch: `20260616T123502Z-lane7-46eab41c`
Completed UTC: `2026-06-16T12:38:13Z`

## Scope

Reviewed all 24 rows in `input.tsv` exactly once using local metadata and local source files only. No web crawl or external submission actions were used.

## Verdict counts

| Verdict | Count |
|---|---:|
| `source_url_extracted` | 5 |
| `parent_source_wrapper` | 5 |
| `country_gap_no_parent_source` | 8 |
| `source_surface_only_no_case` | 5 |
| `reject_noise` | 1 |

## Extracted source URLs

| Queue ID | Source name | URL |
|---|---|---|
| BPSE-01369 | Organisation - Terres australes et antarctiques françaises | https://www.data.gouv.fr/organizations/terres-australes-et-antarctiques-francaises |
| BPSE-01370 | Matching jobseekers with vacancies | https://algoritmes.overheid.nl/en/algoritme/gm0503/51854182/matching-jobseekers-with-vacancies |
| BPSE-01381 | African Union Data Policy Framework | https://au.int/es/node/42078 |
| BPSE-01386 | Regulatory Sandbox system | https://www.cas.go.jp/jp/seisaku/s-portal/regulatorysandbox.html |
| BPSE-01390 | FinTech and digitalisation of financial services in UEMOA | https://www.bceao.int/fr/content/fintech-et-digitalisation-des-services-financiers-dans-luemoa |

## Verification

- Output TSV header matches the required schema.
- Output TSV has one row per input queue_id.
- Output queue_id set equals input queue_id set.
- Output row count equals input row count: 24.
- No duplicate queue_id values in output.

## Boundary notes

This was processing-state review only. The results do not promote reviewed-core rows, add ObscureAI cases, or make incident truth, legal, safety, compliance, prevalence, or ranking findings.
