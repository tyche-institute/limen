# Translation source review summary: 20260616T111817Z-lane3-3f3d9946

- batch id: 20260616T111817Z-lane3-3f3d9946
- rows reviewed: 32

## Verdict counts

- translation_source_reviewed: 2
- cross_project_duplicate: 20
- machine_translation_hold: 2
- candidate_for_url_extraction: 2
- reject_noise: 6

## Boundary statement

This was a bounded translation-aware source review using local metadata and local source files only. The review does not infer incident truth, legality, compliance, safety, deployment, prevalence, ranking, or national absence/presence from machine translation or derivative artifacts.

## Next smallest hardening move

Extract exact original-language source URLs/locators for the two candidate_for_url_extraction rows (Yemen MTIT/government pages and Lesotho gov.ls/AI policy checks), then rerun only those rows through the same bounded translation-source-review schema.
