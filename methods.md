# Methods

## Research Methodology

### Data Collection

- **Source Identification**: Systematic search of public/open sources focusing on underrepresented jurisdictions and rare languages.
- **Inclusion Criteria**: Sources must address AI governance, digital identity, trust architectures, or related themes.
- **Exclusion Criteria**: Private, restricted, or non-public content.

### Evidence Collection Framework

All TSV artifacts (e.g., blocked-sources_sankey.tsv) are maintained in the project's data directory and referenced directly in this document. These files are version-controlled and accompany the manuscript submission.

## Research Methodology

### Data Collection
- **Source Identification**: Systematic search of public/open sources focusing on underrepresented jurisdictions and rare languages.
- **Inclusion Criteria**: Sources must address AI governance, digital identity, trust architectures, or related themes.
- **Exclusion Criteria**: Private, restricted, or non-public content.

### Data Analysis
- **Categorization**: Sources are classified by jurisdiction, language, and topic.
- **Quality Assessment**: Evaluation of source authority, relevance, and potential impact on research claims.
- **Translation**: Machine translation for non-English sources with explicit confidence scoring.

### Algorithms
- **Crosswalk Mapping**: Linking sources to frameworks like OECD AI Principles, eIDAS, and EU AI Act.
- **Clustering**: Grouping similar edge cases or governance approaches.

### Evidence Structuring
- **Claim-Support Links**: Explicit connections between sources and research claims.
### Visualization Hooks
- **Dashboard**: `public-procurement-overview` (automatically updates with source authority scores)
- **Figure**: Sankey diagram of procurement flows by language/country (see `results/boost/limen-boost-006/procurement-flow.png`)
- **Method**: Source authority scoring integrated into evidence weighting table (Table 2)

New artifact: crosswalk TSV with access_level column and contamination risk matrix analysis for legal review

### Denominator Classes
- **Publication-safe lineage**: The subset of evidence that meets bounded reproducibility and reviewer-safe thresholds (e.g., Figure 2 and Table 2 built on the 21-lineage denominator).
- **Live duplicate/taxonomy layer**: Evidence counted in the real-time duplicate control layer (e.g., Figure 5 evidence-funnel built on the 33/25 live taxonomy).
- **Broader stable-or-standalone duplicate/taxonomy package**: The fuller evidence set that includes both bounded and extended lineages (e.g., Figure 7 security threshold ladder anchored to the 25-lineage package).

These denominator classes ensure each figure reflects its intended coverage scope: Figure 2 uses the publication-safe lineage denominator, Figure 5 uses the live duplicate layer, and Figure 7 anchors to the broader package. Maintaining this separation prevents misinterpretation of evidence depth and preserves the manuscript's bounded claim ceiling.

### Source Coverage Matrix

- **Purpose**: Summarize language, jurisdiction, and saturation coverage for rare-language and regional sources in the LIMEN ledger.
- **Metrics**:
  - Language distribution (percentage of sources per language family).
  - Jurisdiction count (number of distinct legal jurisdictions represented).
  - Saturation level (high/medium/low) based on whether >80%/50-80%/ <50% of expected sources have been collected.
- **Current Status**: Initial draft added as Table X in `results/source-coverage-draft.tsv`.
- **Table Schema** (see `results/source-coverage-draft.tsv`):
  - Language (str)
  - Jurisdiction (str)
  - SourceCount (int)
  - Saturation (str: 'high' | 'medium' | 'low')
  - Notes (str)
- **Key Gaps**: Preliminary gaps identified in Baltic and Balkans clusters; targeted outreach planned.