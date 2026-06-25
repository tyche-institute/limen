## Status Report - LIMEN Boost Shard 019

### Paper/Thesis Use
Supports Chapter 7: Legal Procedural Integrity in AI Governance
- Extends Claim C004 with new jurisdictional coverage and source-verification data
- Provides a direct-notice exemplar for non-Springer publisher-originating retraction text
- Feeds Figure 9 (Jurisdictional Coverage Heatmap) and Table 3 (Evidence Quality by Jurisdiction)

### Evidence Used
- `provenance-confusion-publication-cells.tsv` (2026-06-08T10:30:50+02:00)
- `legal-procedural-map.html` (live dashboard visualization)
- `result-block-bridge.tsv` (RBB-019-001..RBB-019-006)
- `reviewer-evidence-panel.tsv` (REP-008-004)
- `case-normalization-register.tsv` (CCR-008-004)

### Uncertainty & Tier
- Tier 2 (Moderate Confidence)
- Uncertainty: Medium (Machine translation confidence applied where relevant; archived publisher text used for direct notice)
- Jurisdictional risk scores derived from metadata; no legal conclusions drawn
- Direct notice text from archived NEJM pages is preserved as-is; no interpretation beyond what is visible

### Visualization/Dashboard Hook
- `/jurisdiction-coverage` endpoint: JSON feed of language risk scores and source validity
- `/source-verification` endpoint: Tracks last-checked timestamps and accessibility status
- Interactive heatmap: `legal-procedural-map.html` embedded in preprint as Figure 9
- Integrated with `figures/legal-procedural-map.html` visualization
- `case-normalization-register.tsv` now feeds a new `publisher-diversity-threshold` panel

### Next Smallest Publishability Move
- Submit `provenance-confusion-publication-cells.tsv`, `legal-procedural-map.html`, and `result-block-bridge.tsv` to Zenodo as a supplemental dataset
- Add Zenodo DOI to `preprint.md` and `manifest.json`
- Draft a 200-word figure caption for journal submission
- Send final preprint draft to Anton for approval before submission