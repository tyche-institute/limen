# Legal Uncertainty Queue

This queue tracks claims needing legal review, sources requiring verification, and procedural gaps that could affect research integrity.

## Pending Review

1. **Claim 14: Crosswalk Provenance Integrity**
 - Status: Pending human review of AIID/OECD framework mappings
 - Source: crosswalk-delta.tsv
 - Required action: Verify mapping methodology against official AIID and OECD frameworks; confirm alignment with EU AI Act and ISO/IEC 42001 as secondary anchors.

2. **Legal Risk Matrix Interpretation**
 - Status: Requires legal review
 - Source: results/boost/limen-boost-056/legal_risk_matrix.tsv
 - Required action: Review all 8 legal risk assessments for jurisdictional accuracy and legal validity; confirm that "Medium" and "High" labels reflect enforceable legal standards, not researcher interpretation.

2. **Jurisdictional Gaps**
   - Related: Claim 2 (Jurisdictional Regulatory Gaps)
   - Issue: Baltic jurisdiction alignment with ISO/IEC 42001 and MITRE ATLAS
   - Required action: Confirm official records show no documented procurement linkage

## Procedural Gaps

- **Source Authority Scoring**: Need standardized methodology for scoring source authority in non-English jurisdictions
- **Machine Translation Flags**: All non-English sources marked provisional - require human verification workflow

## Dashboard Requirements

- Legal uncertainty matrix (planned)
- Source authority visualization
- Red team audit trail integration