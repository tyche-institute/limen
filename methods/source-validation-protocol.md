# Source Validation Protocol for Non-English Regulatory Materials

## Purpose
To establish standardized criteria for verifying jurisdictional authority and credibility of non-English sources used in LIMEN AI Edge-Case Atlas, particularly for regulatory/enforcement materials from underrepresented languages.

## Validation Steps
1. **Original Language Verification**
   - Confirm document is in the official language of the issuing authority's jurisdiction
   - Check for official formatting/paper headers

2. **Authority Verification**
   - Cross-reference issuing body against official government registries
   - Validate through national AI regulatory body directories (e.g., EU AI Office, US NIST)

3. **Date & Jurisdiction Consistency**
   - Match document date with known regulatory timelines
   - Ensure jurisdiction claims align with territorial boundaries

4. **Content Consistency Check**
   - Compare key claims with parallel publications in other languages
   - flag material with >20% divergence without human review

5. **Machine Translation Audit**
   - Apply [ATSD](https://github.com/tyche-institute/atsd) metrics for translation confidence
   - Mark low-confidence segments with ```[UNCERTAINT: Machine Translation]```

## Handling Uncertainty
- **Tier 1**: Official documents with verified authority → direct claim support
- **Tier 2**: Machine-translated with audit trail → [CLAIM SUPPORT: Machine-Verified] + link to audit
- **Tier 3**: Unverified/non-official sources → [CAUTION: Unverified Source]

## Required Metadata
For all non-English sources in `sources/`: 
- `jurisdiction_authority_score` (1-5)
- `translation_method` (mt5 раз shoot/Professional/Literary)
- `confidence_notes` (free-text issues)

## Approval Workflow
1. Initial automated checks (this protocol)
2. Legal expert review for Tier 2/3 sources
3. Quarterly updates to validation criteria based on new regulatory frameworks

## Compliance Notes
- Aligns with Tyche Institute's citation discipline and evidence tiering
- Maintains separation between evidence collection and legal interpretation
- Supports dashboard readiness through structured metadata