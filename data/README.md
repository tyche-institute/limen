# Data Documentation

## Overview
This project collects and structures data on AI edge cases, with emphasis on:
- Rare languages and underrepresented jurisdictions
- Public-sector AI deployments
- Trust architecture and digital identity systems
- Regulatory sandboxes and governance frameworks

## Data Sources
All data derived from public/open sources documented in `sources/sources.md`. Includes:
- Policy documents
- Regulatory filings
- Research papers
- Government reports
- Public procurement records

## Directory Structure
```
/data/
  └── raw/         # Unprocessed source data
  └── processed/   # Structured datasets (CSV/JSONL)
  └── codebooks/   # Metadata for datasets
  └── dictionaries/ # Taxonomy and mapping files
```

## File Formats
- **CSV**: Tabular data with UTF-8 encoding
- **JSONL**: One JSON object per line for structured records
- **YAML**: Metadata and configuration files

## Codebook
Key fields for all datasets:
| Field             | Description                          | Example                          
|-------------------|--------------------------------------|----------------------------------
| source_id         | Reference to sources.md entry       | SRC-00234                       
| jurisdiction       | Applicable legal jurisdiction       | LV-01 (Latvia)                 
| language           | ISO 639-1 language code             | 'lv' (Latvian)                 
| content_snippet   | Relevant excerpt (max 512 tokens)  | "AI governance requires..."  
| claim_links       | Related claim IDs                   | CLM-001,CLM-004               
| confidence_score   | Machine/analyst confidence (0-1)   | 0.87                           

## Data Quality
- All sources validated for public availability
- Non-English content marked with translation confidence
- Regular deduplication runs (weekly)
- Lineage tracking via manifest.json

## Versioning
- Changes tracked in journal.md
- Major versions tagged in Git
- Schema changes documented in codebooks/
