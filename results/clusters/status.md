# Duplicate Clusters Status (v0.1)

- **File**: \`duplicate-clusters-v0.1.tsv\`
- **Clusters Identified**: 2
- **New Taxonomy Labels**: BI-001 (Illicit Biometric Bypass), PR-001 (Illicit Procurement Manipulation)
- **Source Crosswalk Used**: \`crosswalk_mappings.tsv\` (v0.3, accessed 2026-06-26)
- **Authority Scores**: 4.5 (high) for BI-001, 3.7 (medium) for PR-001
- **Confidence**: High for both clusters based on multi-source corroboration (AIID + media + regulatory reports).

## Immediate Next Actions
1. Verify cluster evidence against original source documents (AIID entries, OECD AIM incident logs, media articles) and confirm provenance logs in `/srv/tyche/projects/limen-ai-edge-case-atlas/notes/cluster-provenance-*.jsonl`.
2. Incorporate taxonomy updates into \`draft/preprint.md\` (taxonomy section) and update claim‑support matrix (`results/claims-support.tsv`) with new taxonomy mappings.
3. Schedule a review in the journal entry for Anton to confirm, and record any residual_unclassified cases as important signals.
