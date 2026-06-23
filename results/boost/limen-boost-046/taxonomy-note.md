# Taxonomy Residuals and New-Category Proposal

## Evidence Base
- Reviewed existing taxonomy records in `/srv/tyche/projects/limen-ai-edge-case-atlas/sources/taxonomy`
- Analyzed residual patterns in Finland/Kaleva case evidence consumer metadata
- Crosswalked with OECD AI Principle mappings (2023)

## Residual Gaps Identified
1. **Temporal Drift Markers**: Missing categories for evidence that becomes partially invalid over time due to regulation changes
2. **Hybrid Agency.CLASSIFICATION**: No classification for AI systems combining private/public sector roles
3. **Low-Resource Language Flags**: Inadequate tagging for evidence requiring non-English legal interpretation

## Proposed New Categories
| Category | Description | Evidence Hook |
|---------|-------------|--------------|
| Temporal Validity Flags | Time-sensitive evidence markers (e.g., GDPR-compliant until 2024) | Finland/Kaleva metadata
| Hybrid Sector Entities | AI systems operating across public/private boundaries | Swedish e-Identification Board analysis
| Translation Dependency | Evidence requiring non-English legal interpretation | Baltic state procurement records

## Dashboard Integration
Proposed visualization: Temporal validity timeline + Hybrid entity network graph

## Next Steps
1. Implement taxonomy schema update
2. Backfill existing evidence records
3. Update dashboard-hook.md with new category visualizations