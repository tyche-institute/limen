# Public-sector portal/schema minimum note — limen-boost-006

## Why this artifact exists

The hostile-reviewer sprint and `next.md` both identify the same blocker: LIMEN already has public-sector and institutional-absurdity leads, but they are not yet comparable as a family because the project lacks a minimum portal/schema note. This artifact uses only local LIMEN records to define the smallest safe comparison frame before more register/procurement harvesting.

## Minimal comparison unit

For shard 006, the comparison unit should be a `public-sector AI disclosure surface`, not a presumed deployment. A surface may be:

1. an official project or authority page;
2. a procurement/tender/award page;
3. a public AI/algorithm register listing;
4. a media lead about a public workflow, kept explicitly below deployment status until direct source resolution.

## Minimum required fields before a row is family-comparable

| Field | Why it is required | ORION official page | Finnish Yle lead | Slovenian Radio Ptuj lead |
|---|---|---|---|---|
| `surface_id` | stable join key | yes | yes | yes |
| `jurisdiction` | map/table use | yes | yes | yes |
| `language` | translation-risk and coverage accounting | yes | yes | yes |
| `surface_class` | separates project page, register, procurement, and media lead | yes | yes | yes |
| `institution_type_now` | distinguishes police, ministry, municipality, school, etc. | yes | partial/unverified | unverified |
| `direct_source_resolved` | tells whether the row is reproducible from the cited source | yes | no | no |
| `listing_granularity_now` | page/listing/title-only distinction | yes | yes | yes |
| `evidence_tier_now` | prevents title-only leads from being read as authoritative records | yes | yes | yes |
| `ai_function_signal_now` | bounded statement of what the source actually says AI is doing | yes | title-only | title-only |
| `deployment_or_procurement_evidence_now` | keeps project-purpose, procurement, deployment, and rhetoric separate | partial/project-purpose only | none verified | none verified |
| `missing_fields_blocking_family_comparison` | reviewer-visible explanation of why rows remain weak | yes | yes | yes |

## Interpretation rules

1. Do not infer deployment, legality, vendor identity, or public-sector procurement merely because a source mentions AI and a public body.
2. Treat `project page`, `register entry`, `procurement notice`, and `media lead` as different surface classes with different claim ceilings.
3. A direct official page can support a narrow authoritative row about project existence and stated purpose, but not operational impact or compliance absent stronger text.
4. A title-only media lead can stay in the family as a discovery/limitations row, but should not be counted as a comparable public-sector deployment record.
5. Institutional-absurdity examples are publication-valuable only if the institution type, human fallback, and actual service or decision channel are explicit.

## What the current local rows show

- `LMWCS-20260606-004` is already strong enough to serve as the family's first official-source anchor, but it still lacks procurement/register-style comparability fields such as supplier identity, contract identifiers, and deployment stage.
- `LMWCS-20260606-001` is useful because it appears to connect AI-generated filings/complaints to a police/legal workflow, but it is still a title-gloss lead and should remain below family-comparable status until the direct Yle page or an official source is captured.
- `LMWCS-20260606-005` is useful as an institutional-absurdity candidate, but it is especially vulnerable to misclassification because the title alone does not confirm whether the setting is municipal government, tourism administration, or something private.

## Paper/thesis use now

- Methods/data paper: reviewer-legible explanation of how LIMEN avoids treating public-sector AI mention, procurement metadata, and deployment evidence as the same thing.
- Dashboard package: supports a `surface_class` filter and a disclosure-completeness panel rather than a misleading single count of public-sector AI cases.
- Thesis chapter: compact example of why evidence-tier and source-class separation matters for governance observatories.

## Smallest next move after this note

Resolve one of the two weak Slovenian/Finnish public-sector leads to a direct article or official page, then test whether the row can populate the minimum fields without forcing unsupported values.
