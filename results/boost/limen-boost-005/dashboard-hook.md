# limen-boost-005 dashboard hook

Cycle timestamp: 2026-06-07T07:07:29Z
Project: `limen-ai-edge-case-atlas`
Theme: multilingual weird cases and under-covered languages

## Why this artifact exists

The shared package already says the multilingual overlay is useful, but it still lacks a lane-local routing surface that tells a manuscript or dashboard builder which rows can be shown as bounded substantive/supporting evidence, which rows belong only in a queue/limitations layer, and how each row should appear on a jurisdiction/language map without silently flattening translation and authority differences.

## Main routing result

`multilingual-reviewer-routing.tsv` converts the six-row multilingual queue into three reviewer-safe use buckets:

- `bounded_substantive_use_now`: 1 row (`LMWCS-20260606-004`, Slovenian official police source);
- `bounded_appendix_use_now`: 2 rows (`LMWCS-20260606-001`, `LMWCS-20260606-005`);
- `limitations_or_queue_only`: 3 rows (`LMWCS-20260606-002`, `LMWCS-20260606-003`, `LMWCS-20260606-006`).

## Suggested visualization behavior

1. Jurisdiction/language map:
   - Slovenia/sl may be shown with a caution overlay because one row is direct official and one remains direct non-official.
   - Finland/fi should remain a caution-layer geography row because it mixes one bounded broadcaster-resolved row with one unresolved queue row.
   - Lithuania/lt and Estonia/et should appear only if the map exposes queue/limitations states explicitly.
2. Reviewer appendix table:
   - show the three resolved rows in the main multilingual appendix slice;
   - keep the three unresolved rows in a separate methods/limitations block rather than a flat six-row "multilingual cases" table.
3. Dashboard interpretation:
   - treat multilingual material as a visibility/coverage surface and source-resolution funnel, not as a cross-country ranking or prevalence surface.

## Shared-package implication

The existing shared export promotion register includes a jurisdiction/language coverage export, but not a multilingual-specific reviewer-routing layer. This lane-local TSV is the missing intermediate contract that could later feed a promoted shared export without forcing dashboard prose to infer claim ceilings from the raw queue alone.
