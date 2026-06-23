# LIMEN coding protocol v0.1

This protocol is for the Route A paper snapshot dated 2026-06-07. It supports a methods/data-observatory paper, not a prevalence or legal-conclusion paper.

## Unit of analysis

The primary unit is a duplicate-collapsed public evidence lineage. The frozen headline denominator is `exports/publication-safe-aggregate-matrix.tsv`, with 21 publication-safe lineages. Public IDs in `stable-public-id-alias-map.tsv` are the citable IDs; old local IDs are provenance aliases only.

Rows outside the headline denominator may be coded as `paper_anchor_addition_non_denominator`, `appendix_anchor_non_denominator`, or `appendix_candidate_non_denominator`.

## Two-pass coding

Pass 1 records:

- evidence tier
- source family
- category labels
- confidence cap
- translation status
- duplicate-control status
- legal/procedural posture
- paper claim ceiling

Pass 2 independently rechecks the same fields against the source table and claim register. Pass 2 must start from public ID, not bare local ID, to catch namespace collisions.

If the same person performs both passes, the result is an internal protocol dry-run only. It must not be reported as inter-rater reliability. A submission-ready reliability paragraph needs a second coder or a clearly labeled adjudication audit without kappa/alpha statistics.

## Evidence-tier rules

`T3_authoritative_source`: official regulator, court, tribunal, issuer, publisher, or similarly authoritative public record supports the narrow claim.

`T3_authoritative_source_direct_url_resolved`: direct official source was resolved from a multilingual or lead surface and supports a narrow official/disclosure claim.

`T1_single_public_source`: a single public source supports a lead, but stronger authority, corroboration, translation, or document depth is missing.

Evidence tier does not by itself authorize strong substantive claims. A T3 agency summary, T3 order PDF, T3 charging document, T3 publisher notice, and T3 final order carry different claim ceilings.

## Source-family rules

Assign the source family that supports the paper claim, not the subject matter of the case. For example:

- EEOC iTutorGroup remains `Regulator and enforcement sources` until open court-originating text is captured.
- Nate may use `Court and tribunal records` because a DOJ-hosted indictment PDF is represented, but it remains charging-stage.
- Springer retraction notices are `Academic and research-integrity sources`.
- Datatilsynet SU AI is a public-sector governance/source-depth anchor, not a harm row.

## Category rules

Categories may be multi-label, but each row needs one primary dashboard role. Use residual or low-cap categories when public evidence does not justify a stronger label. Media or translated leads must not be promoted into legal or harm categories without stronger sources.

## Adjudication rules

- If source family and topic conflict, code the source family by the document actually used.
- If complaint and final order conflict in posture, store both and use the narrower claim ceiling.
- If a row has official source text but no legal conclusion, code official source depth and legal uncertainty separately.
- If translation is required, use paraphrase and maintain the original-language source URL.
- If two records share a bare local ID, never join on the bare ID.

## Submission-ready reliability note

A paper submission should report either:

1. A true two-coder audit on a small stratified sample, with raw agreement and an adjudication table; or
2. A labeled single-team adjudication audit without inter-rater statistics.

Given the small sample, raw agreement plus disagreement typology is more defensible than overfit statistics.
