## Dashboard Specification for LIMEN AI Edge-Case Atlas

### Overview
Defines the first iteration of dashboards to visualize LIMEN data, aligned with the publication goal card's required views. Built to support research, paper drafting, and hypothesis exploration.

### View 1: Evidence-Tier Funnel
- **Purpose**: Show distribution of evidence tiers (1-3) across cases.
- **Data Source**: `crosswalk-delta.tsv` (evidence_tier column).
- **Visualization**: Stacked bar chart with filtrable case identifiers.
- **Tools**: Consider D3.js or Matplotlib for static images; Tableau/Power BI for interactive.

### View 2: Source-Family Saturation Map
- **Purpose**: Visualize saturation scores across source families.
- **Data Source**: `source-family-saturation-ledger.tsv`.
- **Visualization**: Radial gauge chart or heatmap with score gradients.
- **Implementation**: Use Python's Plotly for interactive web versions.

### View 3: Jurisdiction/Language Map
- **Purpose**: Geospatial and linguistic distribution of cases.
- **Data Source**: Jurisdiction and language columns in `crosswalk-delta.tsv`.
- **Visualization**: Choropleth map (geographic) + donut chart (language distribution).
- **Tools**: Leaflet.js for maps, D3.js for language breakdown.

### View 4: Framework Coverage Heatmap
- **Purpose**: Highlight coverage gaps in framework mappings.
- **Data Source**: Mapping scores from `crosswalk-delta.tsv`.
- **Visualization**: Matrix heatmap with color intensity indicating score strength.
- **Implementation**: Pandas for data processing, Seaborn for heatmap generation.

### Next Implementation Steps
1. **Data Validation**: Ensure crosswalk and saturation data are complete and consistent.
2. **Tool Selection**: Finalize visualization tools based on interactivity and publication requirements.
3. **Draft Development**: Generate static figures for immediate use in papers;
   prepare interactive versions for the LIMEN dashboard portal.
4. **Integration**: Link dashboard components to underlying data sources for dynamic updates.

### Deliverables
- Static images for papers (PDF/EPS formats).
- Interactive dashboard prototypes (HTML/JS or Jupyter Notebook).
- Documentation for reproducibility and collaboration.