# LIMEN Dashboard Specification

## 1. Evidence-Tier Funnel
Visualizes the proportion of cases in each evidence tier (Tier 1: Primary, Tier 2: Indirect, Tier 3: Secondary).

**Figure Type:** Stacked bar chart or donut chart showing tier distribution
**Data Source:** `source-family-saturation-ledger.tsv` + `crosswalk-mapping.tsv`
**Caption:** "Figure 1: Distribution of AI edge cases by evidence tier. Tier 1 represents primary research and legal authority, Tier 2 includes indirect evidence like government reports, and Tier 3 covers secondary sources such as news and commentary."
**Dashboard Hook:** This figure supports the method section's discussion on evidence grading methodology and sets the stage for crosswalk analysis.

## 2. Crosswalk Mapping Matrix

**Table Type:** Heatmap showing mapping completeness between source families and standard categories (AIID, OECD, AVID, MITRE, MIT, CSET)
**Data Source:** `crosswalk-mapping.tsv`
**Caption:** "Table 2: Mapping completeness between LIMEN source families and established AI governance frameworks. Darker shading indicates more complete crosswalk coverage."
**Dashboard Hook:** Appears in the methods section to demonstrate framework alignment and in the discussion to highlight coverage gaps.

## 3. Jurisdiction/Language Map

**Map Type:** Choropleth map showing density of cases by country and language
**Data Source:** (Future file: `jurisdiction-language-distribution.tsv`)
**Caption:** "Figure 3: Geographic and linguistic distribution of AI edge cases in LIMEN. Color intensity reflects case density per jurisdiction, with language diversity indicated by glyph complexity."
**Dashboard Hook:** Supports the global coverage claims in the introduction and methods.

## 4. Taxonomy Heatmap

**Heatmap Type:** Category coverage heatmap
**Data Source:** (Future file: `taxonomy_category_counts.tsv`)
**Caption:** "Figure 4: Heatmap of category coverage in LIMEN showing the relative frequency of different AI edge case types across jurisdictions."
**Dashboard Hook:** Key figure for the results section demonstrating categorization efficacy.

## 5. Security/Agentic Crosswalk

**Diagram Type:** Sankey diagram showing flow between security categories and agentic failure types
**Data Source:** (Future file: `security-agentic-crosswalk.tsv`)
**Caption:** "Figure 5: Sankey diagram illustrating the relationship between security failures and agentic accountability patterns in AI edge cases."
**Dashboard Hook:** Central to the analysis section linking technical failures to governance issues.

## Implementation Plan
1. Complete crosswalk validation (next cycle)
2. Generate evidence-tier funnel visualization (requires `jurisdiction-language-distribution.tsv`)
3. Develop taxonomy heatmap prototype using current crosswalk data as proxy
4. Finalize dashboard specifications in manuscript methods section
5. Schedule figure production for when all required data files are available

**Next Route:** Crosswalk validation > Visualization mockups > Manuscript integration