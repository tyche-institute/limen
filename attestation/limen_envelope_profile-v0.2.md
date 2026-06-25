# LIMEN Evidence Envelope Profile v0.2

## Evidence Tiers
1. **Authoritative Public Source**
   - Government reports, official registries, court records
   - Example: EU AI Act enforcement notices, FDA AI approvals

2. **Trusted Third-Party Audit**
   - Qualified NGO assessments, certified auditor findings
   - Example: Algorithmic Impact Assessment by approved body

3. **Peer-Reviewed Literature**
   - Journal articles with methodological transparency

4. **Industry Standards Compliance**
   - ISO/IEC 42001 implementations, NIST AI RMF alignments

5. **Media Reports with Corroboration**
   - Newspaper articles with multiple independent sources

## Crosswalk Frameworks
|| Source Family       | AIID | OECD AIPR | MITRE ATLAS | CSET AI Harm | NIST AI RMF |
|---------------------|------|----------|-------------|--------------|-------------|
| Public Registries  | ✅   | ✅       | ❌          | ❌          | ✅         |
|---------------------|------|----------|-------------|--------------|-------------|
| Court Records        | ✅   | ❌       | ✅          | ✅          | ❌         |
|---------------------|------|----------|-------------|--------------|-------------|
| Academic Studies     | ❌   | ✅       | ❌          | ❌          | ❌         |
|---------------------|------|----------|-------------|--------------|-------------|
| Industry Standards   | ❌   | ✅       | ❌          | ❌          | ✅         |
|---------------------|------|----------|-------------|--------------|-------------|
| Media Investigations  | ❌   | ❌       | ❌          | ✅          | ❌         |

## Dashboard Specifications
1. **Evidence Tier Funnel**
   - Shows progression from raw reports to authoritative tiers
   - Metrics: source count, confidence score distribution

2. **Geographic Coverage Map**
   - Country/language breakdown of evidence sources
   - Highlight underserved regions/languages

3. **Taxonomy Heatmap**
   - Frequency of edge case categories (security failures, misuse, etc.)
   - Time-series trends

4. **Duplicate Cluster Graph**
   - Visualize redundant reports and their sources
   - Helps identify systemic issues vs. one-off cases

5. **Legal Uncertainty Matrix**
   - Cross-tab of jurisdictions vs. AI risk categories
   - Shows gaps in regulatory coverage

## Claim Mapping and Evidence Roles
- Map modest claims to RATS-style evidence roles (Source, Claim, Evidence Tier, Processing Step, Verification Flag).
- For each claim, indicate mapping to Verifiable Credentials (VC type Assertion with unique claim_code), SCITT/transparency receipts (receipt ID documenting processing step), and C2PA content provenance (hash for derived visualizations).
- Reference the companion attestation/claim-evidence-mapping.md for sample mappings and standardization notes.
- Ensure non-claim elements are clearly marked as not asserting truth, legality, compliance, or certification.

--- 
*This profile is a living document; future versions may refine evidence role definitions and mapping to emerging standards.*