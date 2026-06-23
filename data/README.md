# Data README

No case-level dataset rows have been added yet.

Planned shard-007 row families
- candidate cases
- source ledger rows
- standards-to-evidence links
- claim-support links
- visualization-ready theme counts

Minimum future fields
- `case_id`
- `theme`
- `event_label`
- `country_or_jurisdiction`
- `language`
- `source_family`
- `source_url`
- `source_authority_tier`
- `public_access_status`
- `evidence_tier`
- `machine_translation_used`
- `provenance_confusion_mode`
- `claim_support_status`
- `notes`


Justice-sector governance sidecar
- `data/cases/justice-sector-ai-governance-seeds.tsv` stores bounded off-frontier justice-sector AI governance anchors that are usable for comparator/methods/dashboard work but must not be counted as monitored LIMEN misconduct or procedural-contamination rows.
- `results/boost/limen-continuous-experiments/justice-sector-ai-dashboard-thesis-routing-contract-v0.1.tsv` is the current routing/codebook contract for how these seeds may appear in dashboard/thesis sidecars without widening any main LIMEN denominator.
- `results/dashboard/justice-sector-ai-governance-sidecar.tsv` is the host-local shared export of those two bounded rows; always carry the row-level `count_behavior` and `forbidden_overread` fields and do not promote the sidecar into Figure 2, Figure 5, Table 1B, Table 1E, misconduct tallies, or procedural-contamination counts.
