# Parent source extraction summary

Batch: 20260616T121536Z-lane2-70d376a7

Scope: bounded processing-state review using local metadata and local source files only. No web crawl, promotion, incident/legal/safety/compliance finding, prevalence claim, or ranking was performed.

## Results

- Input rows reviewed: 24
- Output rows written: 24
- Queue ID set matches input: True
- Duplicate queue IDs in output: none

## Verdict counts

- country_gap_no_parent_source: 16
- parent_source_wrapper: 4
- source_surface_only_no_case: 3
- source_url_extracted: 1

## Extracted URL

- BPSE-00486 / LIMEN-SIGNAL-428106285B16F103: https://www.digital.nsw.gov.au/policy/artificial-intelligence/ai-governance-assurance-and-frameworks/nsw-ai-assessment-framework
  - Evidence: PALLAS_SECOND_PASS_SPRINT_16_COUNTRY_SCORE_DELTA.csv line 31 points to NSW AIAF; au-source-hardening/source_refresh.csv line 20 explicitly provides the matching local source URL.

## Notes

Rows marked `country_gap_no_parent_source` were country profile, country matrix/index, or research-queue placeholders without an extractable parent source URL for the requested surface. Rows marked `parent_source_wrapper` pointed to aggregates or source-pair/score wrappers where a human must choose among multiple or non-concrete parent surfaces. Rows marked `source_surface_only_no_case` named a candidate case but exposed only target evidence categories and no concrete parent URL.
