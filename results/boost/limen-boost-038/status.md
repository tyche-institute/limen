## LIMEN Boost Shard 038 Status

- **Artifact**: `results/boost/limen-boost-038/crosswalk-updated.tsv` (filled crosswalk rows for LIMEN-001 and LIMEN-002)
- **Artifact**: `results/boost/limen-boost-038/crosswalk-sankey.tsv` (Sankey edges for dashboard Figure 5)
- **Paper/Thesis Use**: Supports manuscript sections *Methods* (crosswalk construction) and *Results* (Figure 5 visualizing mapping to AI governance frameworks).
- **Evidence Used**: Internal mapping files (`mappings/crosswalk_mapping.tsv`), source ledger entries.
- **Uncertainty / Evidence Tier**: Tier 2 for AIID mapping, Tier 1 for OECD mapping; other frameworks pending (TBD).
- **Dashboard Hook**: `dashboard/limen-dashboard-hook.md` can ingest `crosswalk-sankey.tsv` to render interactive Sankey chart.
- **Next Smallest Publishability Move**: Fill remaining TBD columns for AVID, MITRE ATLAS, CSET, NIST, EU AI Act, ISO/IEC 42001, OWASP for both cases using available source data or flag for manual expert review.
