# Dashboard Hook: Crosswalk Provenance Metadata

**Dashboard Tab**: Evidence Provenance Tracker
**Visualization**: Interactive table with expandable metadata rows
**Data Source**: `results/boost/limen-boost-044/crosswalk-delta.tsv` and `results/crosswalks/source-crosswalk-v0.2-enriched.tsv`
**Purpose**: Demonstrate automated provenance tracking for AI governance crosswalks

**Metrics**:
1. Source URL stability (last access date)
2. Language coverage completeness
3. Validation status per framework
4. Timestamp consistency
5. Source authority score (≥0.8 green, 0.6–0.79 yellow, <0.6 red)

**Visualization Notes**:
- Color-code validation status: green (valid), yellow (pending), red (invalid)
- Hover tooltips display full source_url, accessed_utc, language, and authority score
- Click to open source document in new tab (if public)
- Filter by language, jurisdiction, or authority score
- Toggle to show/hide authority-balance sidecar

**Paper Integration**: This hook will support Figure 3's metadata integrity analysis and Table 1's authority scoring in the preprint manuscript.