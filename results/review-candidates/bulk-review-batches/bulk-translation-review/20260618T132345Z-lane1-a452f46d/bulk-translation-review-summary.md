# Bulk translation review summary — 20260618T132345Z-lane1-a452f46d

Status: complete

Input rows reviewed: 16
Output rows written: 16

Verdict counts:
- translation_source_reviewed: 3
- source_surface_only_no_case: 2
- cross_project_duplicate: 11

Scope notes:
- Review used local TSV/CSV artifacts only; no web crawl or portal interaction was performed.
- Dutch Algorithm Register rows were treated as English auto-translation or English bulk-CSV source surfaces, not as original-language/legal/policy findings.
- No row is promoted to reviewed core, ObscureAI, incident truth, safety/compliance finding, prevalence, or ranking.
- Repeated package, preview, and Zenodo surfaces were marked as duplicates where they pointed to the same local Dutch Register record/accession.

Verification:
- Input queue_id count: 16
- Output queue_id count: 16
- Same queue_id set: True
- Duplicate output queue_id values: False
- Missing output queue_id values: []
- Extra output queue_id values: []
- Header exact: True
- Allowed verdicts only: True
