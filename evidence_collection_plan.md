# Evidence Collection Plan LIMEN Boost Shard 006

## Target Evidence Types
1. Public procurement contradictions
2. Public registry inconsistencies
3. Institutional absurdities in governance structures

## Data Sources
- European Public Procurement On-Line System (EPPO) [https://epo.eu](https://epo.eu)
- National public registries (focus: Baltics, Balkans, Central Europe)
- OECD AI Policy Observatory (for crosswalk validation)
- EU Open Data Portal (data.europa.eu)

## Collection Approach
1. **Automated Harvesting**: Use public APIs where available (EPPO, data.europa.eu)
2. **Targeted Web Search**: For jurisdictions without APIs, use controlled search patterns
3. **Registry Scraping**: Ethical scraping of public .gov domains with robots.txt compliance

## Storage Structure
```
/srv/tyche/projects/limen-ai-edge-case-atlas/results/boost/limen-boost-006/
  ├── procurement_contradictions/  # JSONL files with evidence + metadata
  ├── registry_inconsistencies/     # Normalized registry comparison reports
  └── institutional_absurdities/    # Structured case files with taxonomy mapping
```

## Pipeline Integration
- All evidence files will include:
  - source_path: URI of original document
  - access_date: ISO timestamp
  - jurisdiction: ISO 3166-1 alpha-2 code
  - language: ISO 639-1 code
  - taxonomy_route: From taxonomy_routes.tsv
  - crosswalk_mapping: From crosswalk_mappings.tsv
  - provenance_hash: SHA-256 of source content

## Verification Steps
1. Schema validation against LIMEN evidence schema
2. Crosswalk consistency check
3. Jurisdiction/language validation
4. Deduplication against existing evidence

## Status
getStatusCode: evidence_collection_prepared
NextAction: begin_harvesting_evidence
EvidenceScope: public-sector procurement + registry inconsistencies + institutional_absurdities