# Taxonomy Delta v0.1 (2026-06-28)

## Overview
This delta documents additions and modifications to the taxonomy in response to duplicate cluster mapping identified in the LIMEN deduplication effort.

## New Cluster Categories
- **CC-001**: Illicit Biometric Bypass
  - Mapped from duplicate cluster identified across AIID and OECD source records.
  - Provenance: crosswalk mapping via `source-crosswalk-v0.2.tsv` (accessed 2026-06-24).
  - Authority score: 4.5; confidence: high.

- **CC-002**: Illicit Procurement Manipulation
  - Mapped from duplicate cluster identified across media and security incident sources.
  - Provenance: same as above.
  - Authority score: 3.7; confidence: medium.

## Changes from taxonomy-v0.1
- Introduced explicit mappings from duplicate clusters to taxonomy entries.
- Added justification and provenance notes for traceability.
- Updated cross-reference to `results/boost/limen-boost-011/` provenance logs.

## Residual Unclassified Cases
- Cases that could not be mapped remain in `residual_unclassified` as a signal.
- Retain for future pattern detection; do not discard.

## Artefacts Updated
- `results/clusters/duplicate-clusters-v0.1.tsv` (new)
- `results/taxonomy/taxonomy-delta-v0.1.md` (new)
- `results/clusters/status.md` (new)

## Next Steps
- Validate mappings with legal expert review.
- Incorporate feedback into final taxonomy version.
- Prepare documentation for journal entry.

*This delta reflects the first systematic mapping of duplicate clusters to taxonomy categories, preserving evidential provenance and uncertainty flags.*