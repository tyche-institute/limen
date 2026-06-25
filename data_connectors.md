# LIMEN Data Connectors Implementation Plan

## 1. Source Family Coverage Map
- Connect to /data/source_family_metadata.csv
- Implement jurisdiction/language filters using dropdown UI components
- Generate heatmap with tooltips showing coverage counts

## 2. Evidence Tier Funnel
- Connect to /data/evidence_tier_progression.json
- Build Sankey diagram with click-through details
- Implement node-click handler to show underlying data

## 3. Taxonomy Heatmap
- Connect to /data/taxonomy_categories.parquet
- Color-coding scheme:
  - Green: High certainty
  - Yellow: Medium certainty
  - Red: Low certainty

## 4. Jurisdiction/Language Map
- Geospatial layer from /data/jurisdiction_geojson
- Language overlay from /data/language_distribution.csv

## 5. Legal Uncertainty Matrix
- Data source: /data/legal_uncertainty_matrix.xlsx
- Tooltip explanations from /data/legal_uncertainty_descriptions.yaml

## Implementation Status
- [ ] Data connectors implemented
- [ ] Visualization components prototyped
- [ ] Integration with publication pipeline