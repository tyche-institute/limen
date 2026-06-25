# Baltic Language Coverage Probe (Experimental)

## Objective
Identify gaps in publicly available AI documentation coverage across Baltic languages (Estonian, Latvian, Lithuanian, Finnish, Hungarian) and map them to governance standards.

## Sample Sources
- Estonian e‑Government AI strategy (2023)
- Latvian Ministry of Transport AI use cases (2022)
- Lithuanian Cloud Program pilot reports (2024)
- Finnish AI Registry entries (2023)
- Hungarian Public Procurement AI tender data (2023‑2024)

## Mapping to Standards
| Baltic Source | Relevant Standard | Coverage Gap |
|---------------|-------------------|--------------|
| Estonian e‑ Gov AI | ISO/IEC 42001 | Metadata completeness |
| Latvian Ministry AI | EU AI Act Art. 5 | Human oversight |
| Lithuanian Cloud AI | NIST AI RMF CM‑201 | Data provenance |
| Finnish AI Registry | OECD AI Principle 5 | Transparency |
| Hungarian Procurement AI | MITRE ATLAS T0870 | Risk assessment |

## Next Steps
- Extract metadata fields from each source.
- Score completeness on a 0‑5 scale.
- Produce a saturation ledger entry for Baltic languages.
- Link gaps to claim‑support matrix (C010).

## Deliverable
- `baltic-language-coverage.tsv` with source IDs, completeness scores, and standard mappings.
- Update `claim-support-matrix.tsv` with claim C010.

*Note: This probe is a source‑family experiment; results will inform future crosswalk extensions.*