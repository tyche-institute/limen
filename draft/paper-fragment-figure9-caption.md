## Figure 9: Jurisdictional Coverage Heatmap (Legal Procedural Integrity)

This heatmap visualizes jurisdictional risk scores derived from the LIMEN AI Edge-Case Atlas, Shard 019. Each cell represents a jurisdiction with a risk score computed from the presence and accessibility of authoritative legal and procedural sources related to AI governance, synthetic identity, and provenance confusion. Colors indicate:

- **Red (High)**: Jurisdictions with direct, machine-readable legal anchors and public enforcement records (e.g., U.S. FCC consent decree).
- **Orange (Medium)**: Jurisdictions with public but partial or machine-translated sources, requiring human verification (e.g., Estonia, Latvia, Lithuania).
- **Green (Low)**: Jurisdictions with only indirect or non-official sources, or where language barriers prevent reliable interpretation.

The visualization supports Claim C004: "Crosswalk Coverage Gaps in Non-English Jurisdictions" and is fed by the live `jurisdiction-coverage.json` endpoint. It does not imply legal compliance, regulatory equivalence, or event prevalence. All scores are bounded by the observatory limits framework and exclude unverified machine translations. Source provenance is tracked in `provenance-confusion-publication-cells.tsv` and `source-delta.tsv`. This figure is intended for inclusion in the manuscript as a methodological artifact, not as a policy recommendation.