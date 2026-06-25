## Evidence-Tier Visualization Specifications

This document defines how evidence tiers will be visualized in the LIMEN dashboard:

### 1. Evidence Tier Definitions
- **Tier 1 (Primary Sources):** Official documents, legal texts, primary research data
- **Tier 2 (Secondary Sources):** Analyses, interpretations, secondary datasets
- **Tier 3 (Tertiary Sources):** News articles, opinion pieces, informal reports

### 2. Visualization Types
| Evidence Tier |Recommended Visualization |Purpose|
|---|---|---|
|Tier 1 |Document cards with source metadata |Showcase primary evidence basis
|Tier 2 |Linked node graphs |Demonstrate analytical connections
|Tier 3 |Heatmap timelines |Track media coverage over time

### 3. Implementation Plan
1. Create React components for each visualization type
2. Implement filtering by evidence tier in dashboard backend
3. Develop color-coding scheme for tier differentiation

### 4. Legal Review Requirements
- Uncertainty handling disclaimer for Tier 3 visualizations
- Citation format validation for Tier 1 document cards