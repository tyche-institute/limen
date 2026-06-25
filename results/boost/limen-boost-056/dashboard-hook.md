## Legal Contamination Risk Matrix Dashboard Hook

### Visualization Requirements
- **Fields to Include:**
  - `jurisdiction`: Legal jurisdiction of the case
  - `source_type`: Type of source (e.g., court decision, regulatory report)
  - `contamination_type`: Nature of the legal/procedural contamination
  - `evidence_grade`: Tiered evidence grade (1=High, 2=Moderate, 3=Low)

### Purpose
Feeds the Legal Contamination Risk Matrix in `dashboard/LIMEN-risk-matrix.md`, enabling analysis of legal risks across jurisdictions and evidence tiers.

### Update Protocol
- **Source:** `results/boost/limen-boost-056/status.md`
- **Frequency:** Per cycle update
- **Validation:** Legal review required for Tier 2 and below evidence