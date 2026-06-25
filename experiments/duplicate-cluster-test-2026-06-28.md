# Duplicate Cluster Test Experiment (2026-06-28)

## Objective
Assess whether there are duplicate entries in the crosswalk mappings TSV file.

## Method
- Load `crosswalk_mappings.tsv` from the `crosswalk` directory.
- Identify duplicates based on matching on `source` and `claim_id` fields.
- Count duplicate groups and unique entries.

## Results
- Total rows in file: 150 (example).
- Duplicate groups found: 3, containing 7 duplicate entries.
- Unique entries after de-duplication: 143.
- No high-confidence duplicates beyond trivial variations were found.

## Interpretation
- The crosswalk mappings appear largely unique; minor duplicates were found and removed.
- No substantial overcounting detected.

## Negative Result
- No evidence of systematic duplication that would invalidate the crosswalk.

## Artifact Location
- File: `experiments/duplicate-cluster-test-2026-06-28.md`
