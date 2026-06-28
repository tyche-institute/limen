# Taxonomy Delta v0.1

## New Labels Added

- **BI-001**: Illicit Biometric Bypass – captures cases where biometric authentication systems are bypassed or subverted, observed in multiple source families (AIID, media reports, security advisories).
- **PR-001**: Illicit Procurement Manipulation – covers manipulation of public procurement processes via AI-driven deception or automated bid shading, sourced from regulatory reports and OECD incident monitor.

## Rationale

These labels were introduced after clustering duplicate incidents (see \`duplicate-clusters-v0.1.tsv\`). The clusters show consistent event patterns across AIID and OECD sources, justifying dedicated taxonomy nodes to improve claim‑support mapping and evidence‑tier categorisation.

## Provenance

- Cluster CC-001 mapped to **BI-001** using \`crosswalk_mappings.tsv\` (v0.3, accessed 2026-06-26); authority_score 4.5; confidence high; provenance logged in `/srv/tyche/projects/limen-ai-edge-case-atlas/notes/cluster-provenance-CC001.jsonl` (accessed 2026-06-26).
- Cluster CC-002 mapped to **PR-001** using \`crosswalk_mappings.tsv\` (v0.3, accessed 2026-06-26); authority_score 3.7; confidence medium; provenance logged in `/srv/tyche/projects/limen-ai-edge-case-atlas/notes/cluster-provenance-CC002.jsonl` (accessed 2026-06-26).

## Next Steps

- Verify cluster justifications with source documents.
- Extend taxonomy with additional labels as new duplicate clusters emerge.
- Update claim‑support matrix and manuscript sections accordingly.
