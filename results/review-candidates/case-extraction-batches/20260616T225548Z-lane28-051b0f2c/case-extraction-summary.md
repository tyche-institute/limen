# Case extraction summary

- Batch: 20260616T225548Z-lane28-051b0f2c
- Input rows reviewed: 16
- Output rows written: 16
- Verdicts: closed_noncase_source_surface=16
- Scope: extraction only; no reviewed-core promotion and no ObscureAI addition.
- Method: used provided row metadata and exact DOI/source locators only; no broad crawling, general web search, public actions, submissions, logins, or uploads.

## Disposition rationale

All 16 source_cluster_key values are DOI-hosted scholarly/index or wrapper surfaces already characterized in the input as noncase scholarly/index surfaces. None of the rows, as provided, exposes a concrete AI edge-case event/action/vulnerability/finding/official record with a bounded case-level claim. They are therefore closed as noncase source surfaces for this extraction batch.

## Verification

- The results TSV uses the required header.
- One result row was written per input source_cluster_key.
- Row-count and key-set equality were checked after writing; see manifest verification fields.
