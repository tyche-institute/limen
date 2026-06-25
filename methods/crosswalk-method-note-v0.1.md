# Crosswalk Method Note (v0.1)

## Overview
This document describes the methodology used to create the `results/crosswalks/source-crosswalk-v0.1.tsv` mapping between LIMEN sources and external public AI incident/risk/vulnerability repositories.

## Source Selection
- Identified publicly accessible sources: AIID, OECD AI Incident Monitoring (AIM), AVID, MIT AI Risk Repository, CSET AI Harm, MITRE ATLAS.
- Sources were chosen based on openly published datasets, press releases, or taxonomy documents relevant to AI governance, digital identity, trust architectures.
- Inclusion criteria: openly available, with clear reuse permissions (open access), relevance to edge-case taxonomy, jurisdiction coverage, or technical detail.
- Exclusion criteria: private, restricted, or non-public content.

## Mapping Process
1. **Label Assignment**: Each source was assigned a `label` reflecting the primary evidence type it provides:
   - AIID → `cases` (incident case records)
   - OECD_AIM → `risk_definitions` (risk taxonomy and hazard definitions)
   - AVID → `vulnerabilities` (vulnerability data)
   - MIT_AI_RISK → `cases` (case studies)
   - CSET_AI_HARM → `taxonomies` (harm taxonomy)
   - MITRE_ATLAS → `techniques` (adversarial technique mappings)

2. **Provides Field**: Populated with the standardized evidence category (`cases`, `risk_definitions`, `vulnerabilities`, `taxonomies`, `techniques`).

3. **Description Field**: Summarized the source’s offering, focusing on:
   - Content type (e.g., incident records, taxonomy, vulnerability entries).
   - Coverage (e.g., cross‑jurisdictional, severity scoring).
   - Access conditions (open reuse with attribution).

4. **Access_Level**: Determined based on the source’s licensing and usage terms; all listed sources are marked `open` for research reuse with proper citation.

## Category Coverage
| Source | Provides | Coverage |
|--------|----------|----------|
| AIID | cases | Incident case records with timestamps, actors, outcomes |
| OECD_AIM | risk_definitions | Cross‑jurisdiction risk taxonomy and hazard definitions |
| AVID | vulnerabilities | Disclosed AI system vulnerabilities with severity scores |
| MIT_AI_RISK | cases | Technical case studies of AI failures |
| CSET_AI_HARM | taxonomies | Categorization schema for AI harms |
| MITRE_ATLAS | techniques | Adversarial attack technique mappings for AI systems |

## Seed Import Plan (high‑level)
1. Retrieve metadata only (IDs, titles, URLs, access dates) via public APIs or HTML meta‑scraping respecting robots.txt.
2. Store metadata in `data/sources_meta/crosswalk_seed.jsonl` (or similar) to avoid bulk dataset transfer.
3. Use the metadata to pre‑populate the crosswalk TSV and to drive downstream evidence matrices.
4. Flag any source requiring legal review (e.g., potential IP or privacy constraints) in `results/crosswalks/legal-uncertainty-queue.md`.

## Validation
- Cross‑checked each mapping against source documentation to ensure accuracy.
- Verified that all listed sources provide at least one of the target categories: cases, hazards/risk definitions, vulnerabilities, taxonomies, techniques.
- Confirmed that no private or restricted data is ingested; only open metadata is harvested.

## Notes
- This version (v0.1) serves as the foundational mapping for subsequent evidence‑integration cycles.
- Future work includes extending mappings to additional sources (e.g., European ENISA reports) and enriching the `description` field with granular sub‑category details.
- All mappings are intentionally descriptive, not normative; they do not imply conformance or endorsement.