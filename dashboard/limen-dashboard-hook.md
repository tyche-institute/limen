 1|# Dashboard Hook for LIMEN Boost Shard 036
 2|
 3|## Jurisdiction Map Updates
 4|- **Expanded Coverage**: 
 5| - Added: Finland (LIMEN-000XXX partial), Italy (LIMEN-000001 full), Australia (10 cases)
 6| - Target Gaps: Baltic States, Slovenia, Caucasus (see source-delta.tsv)
 7|
 8|## Dynamic Visualizations
 9|1. **Source Family Coverage Map** 
 10| - Command: `dashboard render-map --source-family=regulator --jurisdictions=EU+US+AU` 
 11| - Input: `/results/boost/limen-boost-036/source-delta.tsv`
 12|2. **Evidence Tier Funnel** 
 13| - Command: `dashboard render-funnel --tiers=T3-T2-T1` 
 14| - Input: `/results/boost/limen-boost-036/status.md#progress`
 15|3. **Contamination Risk Matrix** (NEW)
 16| - Command: `dashboard render-matrix --risk-levels=low,medium,high --dimensions=legal,procedural,security`
 17| - Input: `/results/boost/limen-boost-036/contamination-risk-matrix.tsv`
 18|4. **Cross-Jurisdictional Sankey Flow** (NEW)
 19| - Command: `dashboard render-sankey --flow=source-jurisdiction→case-type→evidence-tier`
 20| - Input: `/results/boost/limen-boost-036/sankey-flow-data.json`
 21|
 22|## Gaps & Recommendations
 23|- **Company Notice Deficit**: 3/248 cases with direct regulator-to-company text
 24|- **Non-English Representation**: 11/157 regulator records with full text (see source-delta.tsv)
 25|- **Action Items**: 
 26| - Prioritize Baltic/Caucasus/Slovenian regulator portals 
 27| - Validate authority-weighted matrix gaps in `dashboard-api-bundle-v0.1.json`
 28| - Finalize contamination risk matrix for human review (due 2026-09-30)
 29|
 30|## Artefact Links
 31|- Status Report: `/results/boost/limen-boost-036/status.md`
 32|- Contamination Risk Matrix: `/results/boost/limen-boost-036/contamination-risk-matrix.tsv`
 33|- Sankey Flow Data: `/results/boost/limen-boost-036/sankey-flow-data.json`
 34|- **Claim-Support Matrix View**: Generate heatmap of claim-support confidence per jurisdiction; feed from experiments/claim-support-matrix.md; interpret as evidence of coverage depth.