# Enforcement Type Taxonomy Mapping

## Standard Taxonomy
| Code | Description | Applicable Jurisdictions |
|------|-------------|--------------------------|
| WARNING | Formal cautionary notice | Global |
| FINE | Monetary penalty | Global |
| BAN | Product/service prohibition | Global |
| AUDIT | Mandatory compliance review | Global |
| RECOMMENDATION | Non-binding guidance | Global |
| CORRECTION | Mandatory corrective action | EU, US |
| LICENSURE | License revocation/ denial | Sector-specific |
|
## Mapping Methodology
1. **Source-Based Mapping**
   - Direct matches to known regulatory frameworks (e.g., DSA Article 14 warning = "WARNING")
   - Use OECD AI Principles alignment where possible

2. **Contextual Inference**
   - For non-standard terms, analyze accompanying sanctions/remedies
   - Cross-reference with jurisdiction's regulatory history

3. **Uncertainty Handling**
   - Mark ambiguous mappings with ` taxpolicy: Taxi Policy`
   - Flag cases requiring human review

## Implementation
- Create `enforcement-type-mapping.tsv` for source-specific mappings
- Add `standard_type` field to all regulatory action records
- Update dashboard script to accept taxonomy codes

## Compliance
- Maintains Tyche evidence tiering (Tier 1-3 sources)
- Supports multilingual enforcement records
- Enables cross-jurisdictional comparisons

## Approval
- Initial mapping reviewed by regulatory expert
- Quarterly updates based on new frameworks

## Example
```json
{
  "source_type": "DSA Warning Notice",
  "standard_type": "WARNING",
  "jurisdiction": "EU",
  "certainty": "high"
}
```
