## Methodology: Source Selection and Crosswalk Development

The LIMEN AI Edge-Case Atlas employs a structured methodology for source selection and crosswalk development to ensure comprehensive coverage of AI governance frameworks and enforcement mechanisms.

### Source Selection Criteria
1. **Authority and Relevance**: Sources are selected based on their authoritative status (e.g., EU AI Act, NIST frameworks) and direct relevance to AI governance and edge cases.
2. **Jurisdictional Coverage**: Prioritizing multinational and regional frameworks (EU, US, Baltic states) to capture diverse regulatory approaches.
3. **Language and Accessibility**: Ensuring inclusion of non-English sources where possible, with machine translation flagged for review.
4. **Provenance Tracking**: Maintaining detailed records of access dates, jurisdictions, and authority scores (1-5 scale).

### Crosswalk Development
1. **Taxonomy Alignment**: Mapping framework requirements to LIMEN edge-case taxonomy using standardized crosswalk artifacts (e.g., source-crosswalk-v0.2-enriched.tsv).
2. **Provenance Metadata**: Embedding metadata such as source URLs, access timestamps, and language flags in crosswalk files.
3. **Uncertainty Quantification**: Assigning confidence scores (0.0-1.0) based on source accessibility, currency, and authority.

### Visualization Integration
Dashboard hooks like the **EU Enforcement Mechanisms Map** and **Framework Crosswalk Viewer** are pre-configured to consume structured artifacts, enabling dynamic exploration of governance landscapes.

## Claim-Support Matrix

The claim-support-matrix.tsv (see results/boost/limen-boost-048/) provides a machine-readable record of evidence-to-claim linkages, including visualization integration paths and provenance details. This matrix supports reproducibility and transparent evidence tracing in the atlas.

## Limitations
- Machine-translated sources require human validation.
- Non-English coverage is currently skewed toward Baltic and Finno-Ugric frameworks.
- Confidence scores are subjective and require periodic review.