# Taxonomy Delta v0.1

## Summary
This delta captures the impact of duplicate source detection on the source taxonomy.

## Changes
- Added `duplicate_source` node to capture source records appearing in multiple ledger entries.
- Mapped the identified duplicate clusters to this node. In this cycle we discovered 13 duplicate clusters, including high-priority ones such as:
  - SEC press release 2024-36 (2 sources)
  - CORDIS project 101225611 (2 sources)
  - Additional clusters (list omitted for brevity but recorded in results/clusters/duplicate-clusters-v0.1.tsv).
- Updated `source_duplication_status` field to include `reviewed_by_human` flag.

## Impact
- No existing taxa were removed.
- The new category now contains 13 source record sets.
- Future cycles should watch for additional duplicates; if a pattern emerges beyond current clusters, a higher-level taxonomy adjustment may be warranted.

## References
- `results/clusters/duplicate-clusters-v0.1.tsv` (raw duplicate data)
- `sources/authoritative-source-ledger.tsv` (underlying ledger)