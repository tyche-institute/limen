# Venue Adaptation Note: Scientific Data (Data Descriptor)

Date: 2026-06-17
Lane: `limen-dashboard-paper-forge`
Source manuscript: `draft/preprint.md` (v0.4, 345 lines)
Target venue: *Scientific Data* (Nature Portfolio) — Data Descriptor format

## Why Scientific Data is the strongest Route A target

- The manuscript's primary contribution is evidence architecture, not empirical
  finding — exactly the Data Descriptor genre.
- The reviewed-core 250-case demonstration, 15-row source-family map, taxonomy
  heatmap, evidence funnel, and duplicate-review graph are reusable data objects.
- The venue's "data citation" mandate aligns with LIMEN's provenance discipline.
- The claim ceiling (no completeness, no prevalence, no legal conclusion) is
  already Scientific Data-safe.

## Section mapping: current preprint → Scientific Data template

| Scientific Data section | Current preprint section | Adaptation work needed |
|---|---|---|
| Abstract (≤150 words) | Abstract (~180 words) | Compress from 180 to ≤150 words; remove venue-generic phrasing; keep denominators. |
| Background & Summary | §1 Introduction + §2 Related Work | Merge; compress related work to one paragraph; emphasize the data gap LIMEN fills. |
| Methods | §3 Observatory Architecture and Methods | Rename subsections; add explicit "Data collection" and "Data processing" subheads per SD style. |
| Data Records | §4 Results (shard fragments) | Restructure as per-record descriptions with file paths, formats, and access info. Each shard becomes one "Data Record" subsection. |
| Technical Validation | §4.8–§4.9 (public-sector, multilingual) + §5 Limitations | Reframe limitations as validation boundaries; add one validation paragraph per denominator class. |
| Usage Notes | New section | Add: how to reuse the dashboard TSV exports, how to cite individual figures, how to integrate with GAIA/PALLAS. |
| Code availability | New section | Point to `tools/` directory and processing scripts. |
| Data availability | New section | Point to `results/dashboard/` TSV exports and `data/cases/` JSONL files. |
| References | Implicit (in-text) | Extract all boost-path references into a proper bibliography. |
| Acknowledgements | New section | Tyche Institute, coordinated observatory program. |
| Author contributions | New section | Single-author note. |
| Competing interests | New section | Standard declaration. |

## Supplementary Information mapping

Corrected 2026-06-18 to match `draft/supplementary-information.md` and
`draft/preprint.md` S-references (preprint wins over legacy venue-adaptation
note).

| SI object | Source artifact | Content |
|---|---|---|
| Supplementary Table S1 | `results/dashboard/authoritative-document-depth-facet.tsv` | Authoritative-document routing and support-state matrix (9 rows). |
| Supplementary Table S2 | `results/dashboard/security-threshold-ladder-panel.tsv` | Route B security threshold contract (4 rows). |
| Supplementary Table S3 | `results/security/security-agentic-threshold-change-matrix-v0.1.tsv` | Threshold-change matrix: row-level upgrade conditions. |
| Supplementary Table S4 | `results/dashboard/provenance-confusion-publication-cells.tsv` | Publication-cell geometry and question-role matrix (6 rows). |
| Supplementary Table S5 | `results/dashboard/security-publication-buckets.tsv` | Security evidence claim-ceiling and panel-split table (12 rows). |
| Supplementary Table S6 | `results/dashboard/security-crosswalk-coverage-panel.tsv` | Security publication-cell matrix. |
| Supplementary Table S7 | `results/dashboard/supplementary-table-s7-trust-boundary-breadth.tsv` | Trust-boundary breadth board (3 rows, derived from S5). |
| Supplementary Table S8 | `results/dashboard/supplementary-table-s8-supply-chain-frontier.tsv` | Supply-chain frontier panel (5 rows, derived from S5). |
| Supplementary Table S9 | `results/dashboard/supplementary-table-s9-peer-review-gap.tsv` | Peer-review frontier gap panel (1 row). |
| Supplementary Table S10 | `results/dashboard/procedural-contamination-source-depth-panel.tsv` | Procedural-contamination source-depth panel (7 rows). |
| Supplementary Table S11 | `results/dashboard/supplementary-table-s11-research-integrity.tsv` | Research-integrity hostile-reviewer panel (5 rows, branch of S10). |
| Supplementary Table S12 | `results/dashboard/procedural-contamination-source-depth-panel.tsv` | Procedural-contamination sidecar control surface (7 rows). |
| Supplementary Table S13 | `results/dashboard/public-sector-disclosure-comparison.tsv` | Institutional-asymmetry matrix. |
| Supplementary Table S14 | `results/dashboard/attestation-trust-surface-readiness.tsv` | Traceability ladder. |
| Supplementary Figure S1 | `results/dashboard-paper/figure-reviewed-core-tier-by-theme.svg` | Reviewed-core tier-by-theme segmented chart. |
| Supplementary Note 1 | `results/dashboard-paper/caption-control-register-v0.1.tsv` | Caption-control register and denominator-discipline rules. |

## Abstract compression target (≤150 words)

Current abstract is ~180 words. Required cuts:
- Remove "The current package supports" enumeration → replace with "The package includes"
- Compress denominator list from explicit counts to "governed taxonomy, publication-safe funnel, and bounded companions"
- Remove final sentence about "reusable across venues, thesis chapters" → keep "reusable across companion observatories"

## Claim-boundary preservation

All Scientific Data adaptations must preserve:
- No corpus completeness claim
- No prevalence or frequency claim
- No legal violation, compliance, certification, or safety claim
- No fused GAIA/PALLAS/LIMEN denominator
- No country ranking from multilingual evidence
- No machine-translation-only legal/policy conclusion

## Blocker before submission

1. Abstract must be compressed to ≤150 words.
2. References must be extracted from boost-path inline citations into proper bibliography entries.
3. Data Records section needs per-record file-format and access-info lines.
4. Code availability and Data availability sections need stable URLs or repository pointers.
5. One validation paragraph per denominator class (currently distributed across §5 limitations).

## Estimated adaptation effort

- Abstract compression: ~30 minutes of editorial work.
- Section restructuring: ~2 hours (mostly moving prose, not writing new content).
- Reference extraction: ~1 hour (19 boost-path references to formalize).
- SI assembly: ~1 hour (materials already exist as TSV/SVG).
- Total: ~4.5 hours of focused editorial work, no new data collection needed.
