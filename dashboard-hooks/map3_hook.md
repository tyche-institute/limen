# Dashboard Hook for Map 3: Source Authority Coverage

## Purpose
Visualize source authority scoring tiers and evidence coverage across jurisdictions, highlighting blocked sources and machine-translated content confidence intervals.

## Data Source
`data/source_authority_scoring_matrix_v0.1.tsv`

## Visualization Type
Interactive map with layered filters:
- **Base Layer:** Geographic jurisdiction map (Baltic + Caucasus regions)
- **Overlay 1:** Source authority tier (Tier 1: High Authority, Tier 2: Public Portal, Tier 3: Secondary)
- **Overlay 2:** Confidence scores for machine-translated content (0.7-0.85 range)
- **Overlay 3:** Blocked sources (marked in red with contact form status)

## Features
- Clickable regions for detailed source breakdown
- Filter controls for source type and confidence thresholds
- Export options: PNG, SVG, CSV data

## Implementation Notes
- Use `tyche-dashboard` for backend integration
- Mapbox GL JS or D3.js for frontend rendering
- Update frequency: Weekly

## Stakeholders
- @anton.sokolov (primary)
- Legal review team (blocked source workflow)
- Dashboard maintainers