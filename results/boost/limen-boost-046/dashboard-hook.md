# Dashboard Hook: Evidence Consumer Fidelity Upgrades

## Objective
Visualize evidence consumer fidelity upgrades across jurisdictions to track interpretive accuracy improvements in shared consumers.

## Data Sources
1. **Shared Consumer Logs**: Records of evidence representation changes (e.g., `machine_read_direct_article_shell_excerpt` adoption)
2. **Jurisdiction Metadata**: Country/legal system information for geographic mapping
3. **Evidence Tier Registry**: Tier classification of evidence fidelity improvements

## Visualization Type
- **Map**: Choropleth map showing jurisdictions with upgrades (color intensity = number of fidelity improvements)
- **Timeline**: Horizontal bar chart showing adoption of improved evidence standards over time

## Paper/Table Integration
- **Table 3**: "Evidence Consumer Fidelity Upgrades by Jurisdiction" (planned)
- **Figure 4**: Interactive map in manuscript appendix or dashboard

## Required Fields
- jurisdiction (ISO 3166-1 alpha-2 code)
- evidence_type (e.g., 'machine_read_direct_article_shell_excerpt')
- upgrade_date
- tier_upgrade (pre/post number)
- consumer_system (name of system benefiting from upgrade)

## Interpretation Prompt
"This map demonstrates how evidence interpretation standards are evolving across jurisdictions. Darker shades indicate more comprehensive adoption of direct article excerpt representation in shared consumers, reducing ambiguity in AI-related evidence. The timeline reveals acceleration of these upgrades following the EU AI Act transparency requirements."

## Next Step
Populate data from boost shard outputs into dashboard_hook_data.tsv with required fields