# Paper Fragment: Edge-Case Taxonomy and Source-Family Saturation

## Method: Residual Long-Tail Case Identification

We propose and validate a novel method for identifying residual edge cases in AI governance evidence: systematically mapping gaps in existing incident/risk databases (e.g., MITRE ATLAS, CSET, OECD AI Principles) against publicly available, non-English, and underrepresented jurisdictional sources. This approach reveals long-tail cases that are systematically excluded from mainstream AI governance taxonomies.

The method operates in three stages:

1. **Gap Identification**: Compare existing frameworks against public-sector, procurement, and regulatory sources from non-English jurisdictions (e.g., Estonia, Finland, Slovenia) to identify coverage gaps.
2. **Source-Family Saturation**: Map the density of evidence across source families (regulator, procurement, project-page, register) to detect saturation points where new evidence no longer adds novel categories.
3. **Taxonomy Expansion**: Propose new edge-case categories based on residual patterns not captured by existing frameworks.

### Validation

- Gap identification validated via crosswalk-delta.tsv and source-crosswalk-v0.2-enriched.tsv
- Source-family saturation confirmed via sf09-public-sector-publishability-priority.tsv and public-sector-threshold-impact-board.tsv
- Taxonomy expansion supported by candidate-cases.jsonl and legal-uncertainty-queue.md

### Paper Use

This method supports:

- Methods section: "Edge-Case Taxonomy Construction"
- Appendix: "Source-Family Saturation Analysis"
- Dashboard: "Edge-Case Gap Map" panel

### Limitations

- Requires manual review of non-English sources for accurate classification
- Dependent on public-source accessibility and metadata completeness
- Cannot resolve cases where no public evidence exists

### Next Step

Submit the LIMEN AI Edge-Case Atlas repository as a Data Paper to Scientific Data (Nature Portfolio) with Zenodo DOI — requires Anton's external access to initiate Zenodo deposit.