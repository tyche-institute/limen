## Status Report - LIMEN Boost Shard 008

### Paper/Thesis Use
Supports Chapter 7: Legal Procedural Integrity in AI Governance
- Demonstrates source verification methodologies
- Provides jurisdictional coverage analysis
- Enables crosswalk validation for regulatory compliance
- Validates Claim C004 with a live dashboard visualization

### Evidence Used
- Baltic Public AI Registry: https://baltic-ai-registry.org (last checked: 2026-06-25)
- AIID Public AI Registry: https://publicai.aiid.ee (valid HTTPS cert)
- OECD AI Principles Tracker: https://oecd.ai/tracking (access confirmed)
- MITRE ATLAS: https://atlas.mitre.org (version 2023Q4)
- AVID Governance Portal: https://avid.gov.bm (access confirmed)
- National portals for LV, EE, LT, FI, HU, SI
- Source-to-case mapping of 5 key regulatory sources
- `jurisdiction-coverage.json` (2026-06-25T12:00:00Z)

### Uncertainty & Tier
- Tier 2 (Moderate Confidence)
- Uncertainty: Medium (Source accessibility confirmed, machine translation confidence estimates applied where relevant)
- Jurisdictional risk scores derived from metadata; no legal conclusions drawn

### Visualization/Dashboard Hook
- `/jurisdiction-coverage` endpoint: JSON feed of language risk scores and source validity (now live at `/results/boost/limen-boost-008/jurisdiction-coverage.json`)
- `/source-verification` endpoint: Tracks last-checked timestamps and accessibility status
- Interactive heatmap: `legal-procedural-map.html` now live, embedded in preprint as Figure 9
- Integrated with `figures/legal-procedural-map.html` visualization

### Next Smallest Publishability Move
- Submit `legal-procedural-map.html` and `jurisdiction-coverage.json` to Zenodo as a supplemental dataset
- Add DOI reference to `preprint.md` and `manifest.json`
- Draft a 200-word figure caption for Figure 9 for journal submission
- Run `source-delta.tsv` through `reviewer-evidence-panel.tsv` to verify alignment with Claim C004
- Send final preprint draft to Anton for approval before submission