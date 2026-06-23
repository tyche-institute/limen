# Bulk translation review summary: 20260617T073304Z-lane2-970196d0

Scope: bounded processing-state review of every row in `input.tsv` using local metadata and local source files only. No web crawl, submission, publication, portal use, incident truth finding, legal finding, safety finding, compliance finding, prevalence claim, ranking, reviewed-core promotion, or ObscureAI addition was made.

Input rows: 16
Output rows: 16
Queue-id set match: yes
Duplicate queue IDs in output: no

Verdict counts:
- cross_project_duplicate: 7
- source_surface_only_no_case: 2
- translation_source_reviewed: 7

Language/posture counts:
- en: 5
- en / Dutch official registry surface: 5
- en metadata: 2
- zh: 4

Notes:
- Pallas Yemen rows were kept as source-surface/context because the local line is a weak/negative evidence warning, not a concrete AI case.
- Dutch Algorithm Register rows were treated as official registry source surfaces only; repeated local copies were marked as duplicates.
- Alibaba AgentTeams rows were reviewed as Chinese translation-sensitive vendor source surfaces; duplicate backups were deduplicated to a canonical source packet and retain human-review-needed posture.
- English GAIA source rows (Jugalbandi, Kore.ai Artemis, GovGuide Nigeria, Cabinet Office Assist) were reviewed only at named-source surface level, with no promotion beyond processing-state extraction eligibility.

Verification:
- Result TSV header matches the required header exactly.
- Result TSV row count equals input TSV row count.
- Result TSV queue_id set equals input TSV queue_id set.
- No extra, omitted, or duplicated queue_id values were found.
- All verdict values are from the allowed list.
