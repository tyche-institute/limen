# LIMEN Dashboard Specification v0.1

## Purpose
To visualize core research metrics and evidence structures from the LIMEN AI edge-case atlas, enabling publishable insights and methodological transparency.

## Dashboard Components
1. **Source-Family Coverage Map**
   - Purpose: Show geographic and jurisdictional distribution of source materials
   - Data Sources: sources/sources.md, manifest.json
   - Visualization: Choropleth map with source count tooltips

2. **Evidence-Tier Funnel
   - Purpose: Track evidence progression through tiers (raw → validated → publication-ready)
   - Data Sources: claims.md, data/README.md
   - Visualization: Interactive Sankey diagram

3. **Taxonomy Heatmap
   - Purpose: Matrix of evidence categories vs. jurisdictions showing coverage density
   - Data Sources: claims.md, sources/sources.md
   - Visualization: 2D heatmap with Drill-down capability

4. **Jurisdiction/Language Matrix
   - Purpose: Cross-tab of legal jurisdictions and language families in evidence
   - Data Sources: sources/sources.md (language/jurisdiction fields)
   - Visualization: Mosaic plot with filter controls

5. **Legal Uncertainty Matrix
   - Purpose: Quantify uncertainty levels across legal domains
   - Data Sources: claims.md (uncertainty flags), methods.md
   - Visualization: Risk matrix (likelihood vs. impact)

6. **Security/Agentic Crosswalk
   - Purpose: Map security frameworks to agentic AI claims
   - Data Sources: claims.md (security/agentic tags), sources/sources.md
   - Visualization: Biforce-directed graph

7. **Duplicate-Cluster Graph
   - Purpose: Identify and visualize duplicate evidence clusters
   - Data Sources: manifest.json (hashes), data/README.md
   - Visualization: Circular dendrogram with cluster labels