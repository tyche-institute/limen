# Red Team Analysis for Legal-Procedural Contamination

## Objective
Identify potential contamination vectors between EU AI Act and NATO standards through:
1. Comparative analysis of framework overlaps
2. Mapping MITRE ATLAS entries to EU AI Act recitals
3. Rating severity of conflicts and gaps

## Methodology
- Use matrix-procedural-contamination.tsv as input
- Apply semantic similarity scoring for framework overlaps
- Manual review of top 10 high-risk overlaps
- produce contamination risk ratings (Low/Medium/High/Critical)

## Outputs
- red-team-risk-ratings.tsv: Risk scores for each overlap
- contamination-pathways.md: Detailed analysis of high-risk vectors
- sankey-diagram.svg: Visual representation of framework conflicts

## Next Steps
1. Extract framework overlaps from matrix-procedural-contamination.tsv
2. Run semantic similarity analysis using NLP tools
3. Generate initial risk ratings
4. Prioritize top 10 overlaps for manual review
5. Create Sankey diagram for visual analysis