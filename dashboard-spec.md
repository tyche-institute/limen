# Dashboard Specification for LIMEN AI Edge-Case Atlas

## 1. Evidence Tier Funnel
- **Purpose**: Visualize evidence tiers distribution
- **Data Source**: crosswalk-delta.tsv
- **Visualization**: Stacked bar chart
- **Filter**: By source family, jurisdiction

## 2. Source Family Saturation Map
- **Purpose**: Geospatial view of source coverage
- **Data Source**: source-crosswalk-v0.2.tsv
- **Visualization**: Choropleth map with color intensity by source count
- **Filter**: Language, evidence tier

## 3. Language Coverage Matrix
- **Purpose**: Show language distribution and gaps
- **Data Source**: source-crosswalk-v0.2.tsv
- **Visualization**: Heatmap with language vs jurisdiction
- **Features**: Highlight rare languages (Baltic, Finno-Ugric, etc.)

## 4. Legal Uncertainty Matrix
- **Purpose**: Display legal uncertainty scoring
- **Data Source**: legal-uncertainty-matrix.tsv
- **Visualization**: Matrix with color-coded uncertainty levels
- **Features**: tooltip details on source authority, jurisdictional relevance

## 5. Authority Scoring Integration
- **Purpose**: Enhance evidence matrix with authority scores
- **Implementation**: Add authority score column in evidence matrix
- **Visual**: Color gradient in evidence matrix cells

## 6. Procedural Contamination Network
- **Purpose**: Show contamination pathways
- **Data Source**: regulatory-conflicts evidence
- **Visualization**: Directed graph (nodes: frameworks, edges: conflicts)

## 7. Security/Agentic Crosswalk
- **Purpose**: Map security incidents to frameworks
- **Data Source**: boost/limen-boost-004/crosswalk-delta.tsv
- **Visualization**: Sankey diagram

## 8. Dashboard Update History
- 2026-06-24: Added authority scoring integration, updated legal uncertainty matrix
