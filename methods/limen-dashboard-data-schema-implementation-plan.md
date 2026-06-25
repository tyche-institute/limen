# Dashboard Data Schema Implementation Plan v0.1

## 1. Objective
Define a robust data schema to connect the LIMEN dashboard with core data sources, enabling dynamic visualizations and analysis.

## 2. Schema Components
- **Data Sources**:
  - LIMEN core PostgreSQL database
  - Source ledger CSV
  - Claim-support matrix JSON
- **Dimensions**:
  - Jurisdiction
  - Language
  - Edge case category
  - Evidence tier
  - Regulatory framework
- **Metrics**:
  - Source count
  - Claim strength score
  - Uncertainty index
  - Coverage percentage

## 3. Visualization Mappings
| Visualization | Type | Data Source | Query |
|--------------|------|-------------|-------|
| Coverage Map | GeoJSON | limen-core-db | SELECT jurisdiction, COUNT(*) FROM edge_cases GROUP BY jurisdiction |
| Evidence Funnel | Bar Chart | sourceLedger | SELECT evidenceTier, COUNT(*) FROM sources GROUP BY evidenceTier |

## 4. Implementation Steps
1. **Schema Finalization** (1 day)
   - Validate with data team
   - Document all fields
2. **Connector Development** (2 days)
   - Database connection
   - CSV/JSON parsers
3. **Visualization Coding** (3 days)
   - D3.js implementations
   - Leaflet map integration
4. **Testing** (1 day)
   - Data integrity checks
   - Visualization functionality

## 5. Artifact Integration
- Output schema: `methods/limen-dashboard-data-schema-v0.1.json`
- Reference in dashboard spec: `dashboard/limen-dashboard-spec-v0.1.md`
- Link to article architecture: `papers/article-architecture-v0.1.md`

## 6. Compliance
- Verified against AGENT.md Section 5.4
- No prohibited content or vendor references
- Maintains Tyche Institute's research focus

## 7. Next Steps
- Share schema with data engineering team
- Begin connector implementation
- Update dashboard spec with final schema details