# Proposed Crosswalk Mapping for Language Coverage

## Mapping Overview
- **Evidence Tier**: II
- **Source Family**: Language Coverage (Baltic languages)
- **Description**: Documentation of AI-related sources across Baltic languages (Estonian, Latvian, Lithuanian, Finnish, Hungarian) indicating coverage status and verification level.
- **Evidence Level**: Medium
- **Standard(s)**: ISO/IEC 42001, ISO/IEC 27001, OWASP AI

## Rationale
- These languages represent underrepresented jurisdictions where AI governance documentation is emerging but not yet systematically captured.
- Mapping to ISO/IEC 42001 (AI management) and ISO/IEC 27001 (information security) supports formal governance frameworks.
- This mapping enables dashboard visualization of governance readiness by language category and supports targeted data collection efforts.

## Draft Row for `crosswalk-delta.tsv`
```tsv
evidence_tier,source_family,description,evidence_level,standard
"language coverage","Baltic languages","Coverage of AI documentation in Baltic languages (Estonian, Latvian, Lithuanian, Finnish, Hungarian)","medium","ISO/IEC 42001, ISO/IEC 27001, OWASP AI"
```