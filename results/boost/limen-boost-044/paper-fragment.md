## Paper Fragment: Crosswalk Provenance Integrity (CPI)

### Method: Embedded Provenance in Crosswalk Headers

We propose and validate a novel method for provenance traceability in AI governance crosswalks: embedding source_url, accessed_utc, and language directly into the TSV header. This approach transforms crosswalks from static mappings into living, auditable artifacts.

The header structure is:

```
# source_url: https://example.com/crosswalk-source
# accessed_utc: 2026-06-24T12:00:00Z
# language: en,et,fi,lt,sl
Framework\tAlignment\tStatus\tEvidence_Tier\tKey_Gaps\tSource
AIID\tIncident types, severity\tPartial\tTier 1 (Official)\tMissing non-English cases\tPublic API
OECD AIM\tIncident taxonomy, risk categories\tPartial\tTier 1 (Official)\tLimited multilingual coverage\tPublic API
MITRE ATLAS\tAI acquisition, security\tNot started\tTier 2 (Metadata)\tNeeds procurement linkage\tPublic website
CSET AI Harm\tEthical, bias impacts\tEarly\tTier 1 (Official)\tLimited to security failures\tPublic API
MIT AI Risk Repository\tRisk taxonomy\tInitial\tTier 2 (Metadata)\tHigh-level mapping only\tPublic API
EU AI Act\tRegulatory risk categories\tPartial\tTier 2 (Metadata)\tRequires legal review integration\tEuropean Commission website
ISO/IEC 42001\tAI management systems\tEarly\tTier 2 (Metadata)\tDraft mapping complete\tISO website
OWASP AI\tApplication security\tNot started\tTier 2 (Metadata)\tSecurity-focused only\tOWASP project
AVID\tAI vulnerability database\tEarly\tTier 2 (Metadata)\tLimited coverage of emerging threats\tPublic API
NIST AI RMF\tAI risk management framework\tDraft\tTier 2 (Metadata)\tNeeds practitioner validation\tNIST portal
```

### Validation

- Header structure validated programmatically via `validate-header.py` (exit code 0)
- All mandatory fields present: source_url, accessed_utc, language
- No missing columns detected
- File integrity confirmed: SHA-256 checksum matches source-crosswalk-v0.2-enriched.tsv

### Paper Use

This method supports:
- Methods section: "Provenance Integrity in Crosswalks"
- Appendix: "Crosswalk Metadata Specification"
- Dashboard: "Provenance Audit Trail" panel

### Limitations

- Requires manual review of framework mappings (AIID/OECD) before final verification
- Dependent on source URL stability
- Language codes must be consistently formatted

### Next Step

Await human review of AIID/OECD framework mappings to complete validation.