## Dashboard Hook: false-claims-over-time

**Dataset**: `crosswalk-delta.tsv` (located at `/srv/tyche/projects/limen-ai-edge-case-atlas/results/boost/limen-boost-046/crosswalk-delta.tsv`)
**Visualization Type**: Interactive time-series bar chart
**Fields**:
- X-axis: `jurisdiction` (categorical)
- Y-axis: `claim_type` (count, stacked by sector)
- Color: `uncertainty` (gradient from low to high)
- Hover: `evidence`, `access_date`, `language`
**Parameters**:
- Date Range: 2020-2024 (from dataset Metadata)
- Filters: Sector, Jurisdiction, Claim Type
- Animation: Slide-by-year

**Description**: Visualizes the proliferation of false/misleading AI claims across jurisdictions and sectors over time, with uncertainty indicators. Supports claims in Section 4.3 and Table 5 of the manuscript.

**Metadata**:
- Created: 2026-09-28
- Provenance: Generated from EUR-Lex, EDPB, UK ICO, and German Federal Cartel Office sources
- Language: English (primary), with provisional translations marked
- Visualization Hook ID: `false-claims-over-time-v1`
- Dashboard Path: `src/app/visualizations/false-claims`