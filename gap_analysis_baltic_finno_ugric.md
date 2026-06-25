# Gap Analysis: Baltic/Finno-Ugric Language Coverage

## Current State (as of 2026-06-25)

| Language | Jurisdiction | Current_Source_Count | Coverage_Status |
|----------|--------------|----------------------|-----------------|
| Estonian | Estonia | 1 | Processing |
| Latvian | Latvia | 0 | Pending |
| Lithuanian | Lithuania | 0 | Pending |
| Finnish | Finland | 0 | Pending |
| Hungarian | Hungary | 0 | Pending |

## Analysis

- Only Estonian language sources are currently being processed; the rest (Latvian, Lithuanian, Finnish, Hungarian) have zero sources.
- The target for each language is to acquire at least one verified source to move from "Pending" to "Processing".
- The gaps represent coverage holes in the Baltic and Finno-Ugric language families, which are a focus under the AIID/OECD expansion priority.

## Recommendations

1. Conduct targeted searches for public sources in Latvian, Lithuanian, Finnish, and Hungarian that discuss AI governance, digital identity, or trust architectures.
2. Prioritize source families aligned with OECD AI Principles and EU AI Act for initial inclusion.
3. Once sources are identified, verify language and jurisdiction metadata, then add them to the `source-family-ledger.tsv` and update `language_coverage_baltic_finno_ugric.tsv`.
4. Record translation confidence scores and rights/notes for each new source.
5. Update the `gap_analysis_baltic_finno_ugric.md` to reflect progress in subsequent cycles.

## Next Steps

- Assign source-scraping tasks for each pending language.
- Integrate identified sources into the `source-family-ledger.tsv` and `public-source-families-v0.1.tsv`.
- Re-run coverage analysis in the next cycle to measure reduction in gaps.