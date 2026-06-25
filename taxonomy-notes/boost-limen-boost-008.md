# Taxonomy Note for LIMEN Boost Shard 008

**Theme:** Legal/Procedural Contamination and Research Integrity

## Background
Recent internal reviews uncovered several instances where procedural documentation inadvertently mixed legal interpretation with empirical observation. These *contamination* cases risk conflating normative claims with descriptive evidence, undermining the evidentiary rigor required for the LIMEN AI Edge‑Case Atlas.

## Proposed Taxonomy Extensions
| Category ID | Description | Example Source | Contamination Type |
|------------|-------------|----------------|-------------------|
| LC‑01 | *Legal‐normative statements presented as empirical findings* | Internal policy brief (Zetes) – “AI Act mandates X” | Normative → Empirical |
| LC‑02 | *Procedural footnotes that embed author opinions* | Claims‑human‑review‑059.md – author note on “likely impact” | Opinion → Evidence |
| LC‑03 | *Mixed‑language translations without confidence scores* | Baltic language vitality mapping (automatically translated) | Translation → Evidence |

## Recommended Actions
1. Flag each source in `blocked-source-ledger.tsv` that exhibits LC‑01 or LC‑02 contamination.
2. Add a `contamination_confidence` field to the source ledger JSON with values `high`, `medium`, `low`.
3. Draft a *Methodology* subsection (`methods.md`) describing how contamination is identified, recorded, and mitigated.

## Research‑Integrity Implications
- Improves transparency for reviewers by clearly separating normative statements from descriptive data.
- Enables downstream dashboards to filter out contaminated entries when generating claim‑support matrices.

## Next Steps
- Implement a small Python script `scripts/contamination_tagger.py` to auto‑detect LC‑01/LC‑02 patterns in source files.
- Update the `integrity-dashboard` (see `dashboard-hooks/integrity-dashboard.md`) to display contamination counts per jurisdiction.
