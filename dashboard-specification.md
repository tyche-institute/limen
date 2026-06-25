# Dashboard Specification for LIMEN AI Edge-Case Atlas

## 1. Overview
This dashboard specification defines the structure and components for visualizing legal uncertainty and evidence mapping in the LIMEN AI Edge-Case Atlas.

## 2. Legal Uncertainty Matrix (§7.8)

### 2.1 Purpose
To visualize the uncertainty levels and source authority scores of crosswalk mappings between legal frameworks and evidence sources, including validation status and language coverage.

### 2.2 Data Sources
- **Primary**: `results/boost/<lane_id>/legal-uncertainty-matrix.tsv`
- **Secondary**: `crosswalk-delta.tsv`, `source_authority_scores.tsv`

### 2.3 Visualization Requirements

|| Parameter | Description |
||---------|-------------|
|| X-axis | Legal Framework (EU AI Act, OECD, MITRE ATLAS, ISO/IEC 42001, OWASP AI, etc.) |
|| Y-axis | Source Authority Score (0.0–1.0) |
|| Color | Validation Status (Valid=Green, Pending=Yellow, Invalid=Red) |
|| Shape | Evidence Tier (Tier 1–5 as circles/squares/triangles) |
|| Size | Language Coverage (1–5 languages represented, proportional to circle size) |

### 2.4 Implementation
- React components per `design.md` §7.1-7.5
- URL parameters for bookmarking views
- Integration with currentness audit system

## 3. Currentness Board

### 3.1 Data Source
`results/boost/<lane_id>/currentness-audit.tsv`

### 3.2 Visualization
Heatmap showing recency of evidence sources by jurisdiction

## 4. Evidence Matrix

### 4.1 Data Source
`law-to-evidence-matrix-draft.tsv`

### 4.2 Visualization
Interactive graph showing claim-to-evidence links