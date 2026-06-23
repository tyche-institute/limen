# Bulk translation review summary

Batch: `20260616T121959Z-lane4-5d475839`
Task: `bulk-translation-review`
Completed UTC: `2026-06-16T12:22:12Z`

## Scope

Reviewed all 16 input rows exactly once using only local metadata and local source files. This is a processing-state translation/source-surface review only. No reviewed-core promotion, ObscureAI addition, incident truth, legal finding, safety finding, compliance finding, prevalence claim, or ranking was made.

## Verdict counts

- `source_surface_only_no_case`: 6
- `cross_project_duplicate`: 4
- `needs_original_language_source`: 3
- `candidate_for_parent_source_extraction`: 2
- `machine_translation_hold`: 1
- `translation_source_reviewed`: 0
- `reject_noise`: 0

## Main review notes

- Colombia Constitutional Court / PretorIA appears as a concrete official court source-surface candidate, but local evidence is translation-mediated and duplicate across three rows; only BTR-00225 was kept as the extraction candidate, with BTR-00229 and BTR-00232 marked duplicate.
- Dutch algorithm-register Octobox row is explicitly an English auto-translation from Dutch; it is a candidate for parent-source extraction, not a standalone factual/legal claim.
- Digital Austria, Digdir/Norwegian guidance, Cyprus strategy, Lithuania open-data portal, Guatemala UN/UNDP assessment, and Ethiopia summary rows were kept at source-surface/context ceiling only.
- Pakistan, Israel, and Brazil rows require original/local source review before substantive use because the local evidence is a seed/gap note/fetch-warning rather than reviewed source content.
- Chinese deep-synthesis legal paraphrase was placed on machine-translation hold; no legal or policy conclusion was made from the paraphrase.

## Verification

Automated verification was run after writing outputs:

- input rows: 16
- result rows: 16
- result header matches required header
- queue_id set matches input exactly
- no omitted queue_id values
- no extra queue_id values
- no duplicate queue_id values
- no tabs or newlines inside TSV fields beyond delimiters/record separators
