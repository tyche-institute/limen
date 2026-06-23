# Data Management

## Data Directory Structure

```
/data
  └── raw/          # Unprocessed source data
  └── processed/    # Cleaned and annotated datasets
  └── intermediate/ # Temporary files during processing
  └── documentation/ # Data dictionaries, codebooks, and metadata
```

## Processing Workflow

1. **Ingestion**: Sources are downloaded and stored in `/data/raw`
2. **Cleaning**: 
   - Remove duplicates
   - Handle missing values
   - Normalize formats
3. **Annotation**: 
   - Add metadata tags (language, jurisdiction, etc.)
   - Map to evidence categories
4. **Storage**: 
   - Final datasets moved to `/data/processed`
   - Preservation of raw sources in `/data/raw`

## Key Data Artifacts

- **Source Ledgers**: `/sources/sources.md`
- **Claim-Support Matrices**: `/claims/claim-support-matrix.md`
- **Dashboard Data**: `/dashboard/data/limen-stats.json`
- **Codebook**: `/data/documentation/codebook.md`

## Tools in Use
- **Data Processing**: Python (Pandas, NumPy)
- **Version Control**: Git for dataset evolution
- **Validation**: Great Expectations for data quality checks