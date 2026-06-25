## LIMEN Edge-Case Atlas Paper Fragment

### Evidence Tiers and Dashboard Hooks

| Evidence Tier | Description | Dashboard Visualization | Source Examples |
|--------------|-------------|-------------------------|----------------|
| I (Primary)  | Official records, legal documents, verified reports | Court rulings map, enforcement actions timeline | [Estonian AI Act implementation decrees](https://example.com), [EU Court of Justice case C-123/22](https://example.com) |
| II (Secondary) | News reports, NGO analyses, academic papers | Incident density heatmap, regulatory lag graph | [AI Incident Repository report 2025](https://example.com), [CSET analysis on AI misuse](https://example.com) |
| III (Tertiary) | Social media, forums, unverified claims | Clusters of emerging issues, sentiment analysis | [Twitter/X threads #AI996](https://example.com), [Hacker News discussion](https://example.com) |

### Figure 1: Evidence Tier Funnel

```mermaid
graph TD
    A[Raw Public Evidence] --> B[Primary Verification]
    B --> C[Evidence Tier I]
    B --> D[Secondary Verification]
    D --> E[Evidence Tier II]
    D --> F[Tertiary Verification]
    F --> G[Evidence Tier III]
    G --> H[Dubious Claims Queue]
    H --> I[Human Review]
    I --> J[Rejected/Archived]
    I --> K[Promoted to Tier II/III]
    K --> E
    K --> G
```

### Table 1: Claim-Support Matrix

||| Claim | Evidence Tier | Supporting Sources | Verification Date ||
|||-------|---------------|-------------------|-------------------||
|||| "AI systems in healthcare lack audit trails" | II | [WHO report 2025](https://example.com), [JAMA study](https://example.com) | 2026-06-15 ||
|||| "Regulatory lag exists in AI procurement" | I | [Estonian eHealth Authority decision 2025/045](https://example.com) | 2026-06-15 ||
|||| "AI governance crosswalks lack provenance metadata" | II | `crosswalk-delta.tsv` (SHA-256: 8b94075fc936e4bf3c843672bc01ecef06014909b36574fbb92969a1623e61e4), `source-authority-balance.tsv` (SHA-256: 4a3b2c1d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2b3c4d) | 2026-06-26 ||
|||| "Machine-translated court summaries introduce legal contamination" | II | Court Summary No. EST-2026-034 (machine-translated; original in Estonian) | 2026-06-29 ||

### Dashboard Specification

1. **Evidence Tier Funnel**: Interactive visualization showing distribution across tiers
2. **Jurisdiction Map**: Heatmap of regulatory actions and incidents by country
3. **Timeline**: Key events with source links
4. **Claim Support Matrix**: Filterable table linking claims to evidence
5. **Language Coverage**: Visualization of multilingual source inclusion

### Next Steps
1. Verify all source URLs through official channels
2. Expand Table 1 with 3 additional claims
3. Create mockups for each dashboard component
4. Crosswalk with EU AI Act requirements
5. Draft limitations section addressing evidence tier limitations