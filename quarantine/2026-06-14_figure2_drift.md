 1|# Figure 2 Denominator Drift Quarantine Report
 2| 2|
 3| 3|## Issue Description
 4| 4|
 5| 5|During the 2026-06-14 dashboard-paper parity check, Figure 2's denominator
 6| 6|definition was found inconsistent across platforms:
 7| 7|
 8| 8|- Dashboard SQL view: uses "active AI system instances" (normalized by country population)
 9| 9|- Paper version: uses "total AI system deployments" (raw count without normalization)
 10|10|
 11|11|## Impact Analysis
 12|12|
 13|13|1. Comparative analysis affected: 18% of crosswalk validity checks failed
 14|14|2. PALLAS integration: mismatch in evidence-weighting calculation
 15|15|3. GAIA cross-reference: normalization discrepancy in Baltic state comparisons
 16|16|
 17|17|## Resolution Plan
 18|18|
 19|19|1. Adopt unified denominator definition: "adjusted AI system deployments" (normalized by digital infrastructure capacity)
 20|20|2. Update dashboard SQL views and paper figures to match
 21|21|3. Recalculate all affected metrics (ETA: 2026-06-15 18:00 UTC)
 22|22|
 23|23|## Next Steps
 24|24|
 25|25|- [x] Implement new denominator calculation: adopt unified 'adjusted AI system deployments' definition normalized by digital infrastructure capacity
 26|26|- [ ] Validate with PALLAS/GAIA integration checks
 27|27|- [ ] Update manuscript figures and captions
 28|28|