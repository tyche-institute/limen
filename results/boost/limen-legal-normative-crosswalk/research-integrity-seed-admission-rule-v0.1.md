# Research-integrity bounded seed-admission rule v0.1

Lane: `limen-legal-normative-crosswalk`
Project: `limen-ai-edge-case-atlas`
Updated: 2026-06-08T21:14:56Z
Scope: `research_integrity` only

## Purpose

This rule lets the legal/normative crosswalk admit one bounded research-integrity exemplar without collapsing publisher notice text into misconduct, illegality, compliance, or institutional-fault conclusions.

## What this rule changes

- It creates an explicit admission path for one authority-scored exemplar inside the legal lane.
- It does not by itself change seeded counts.
- It does not promote `research_integrity` into a broad legal family.
- It does not convert publisher/editor notice text into final findings about intent, fraud, or legal status.

## Admission gate for one exemplar

A `research_integrity` exemplar may move from `zero_seed_but_locally_non_empty_shadow_package` to one bounded seeded legal-row comparator only if all conditions below are met:

1. Exact case identity is stable in local normalization artifacts.
2. Public evidence includes direct publisher-originating notice text, or archive-resolved publisher-originating notice text, captured locally with exact support paths.
3. The notice itself states the editorial action and bounded rationale in directly observable wording.
4. The row can be narrated entirely with notice-bounded language such as `publisher notice states`, `archived notice states`, or `editor notice states`.
5. Downstream prose keeps `source_claim`, `curator_interpretation`, and `legal_status` separated.
6. The row is explicitly tagged as a publisher-notice anchor, not as a misconduct finding, legal conclusion, or institution-wide prevalence claim.
7. Any archive dependence, publisher concentration, venue-specific limitation, or blocked live page remains explicit in the row note or caption-safe claim.

## Exclusion gate

Do not admit a row into the bounded seeded comparator state when the strongest public support is only one of the following:

- mediated editor statement without captured direct notice text;
- specialist report only;
- residual platform-action text with no direct publisher/editor notice;
- title-level metadata, DOI linkage, or Crossref relation alone;
- machine translation or paraphrase that outruns the captured notice wording.

## Current candidate ranking under this rule

1. `LCPQ-032-006` / `LIMEN-008-RI-SPRINGER-ICM-FAKE-REFS-20260128`
   - Current state: `direct_publisher_editor_notice_text`
   - Rule result: eligible for one bounded seeded comparator if the legal row keeps notice-bounded wording only.
2. `LCPQ-032-007` / `LIMEN-008-RI-SPRINGER-BOOK-FAKE-CITES-20250630`
   - Current state: `direct_publisher_notice_text`
   - Rule result: also eligible, but keep the Springer concentration caution explicit.
3. `LCPQ-032-004` / `LIMEN-008-RI-NEJM-AI-IMAGERY-20260501`
   - Current state: `archived_direct_publisher_notice_text`
   - Rule result: admissible only with archive-dependence language kept explicit.
4. `LCPQ-032-003` / `LIMEN-008-RI-SAGE-CHATGPT-REFS-20240520`
   - Current state: `publisher_correction_metadata_plus_mediated_editor_statement`
   - Rule result: not yet admissible.

## Safe output shape if applied later

If a later cycle applies this rule, the seeded comparator should remain bounded to:

- category: `research_integrity`
- authority label: `publisher_notice_text_anchor`
- paper use: methods / limitations / dashboard source-depth comparator / thesis source-authority note
- forbidden overread: misconduct finding, intent finding, legal-status conclusion, institution-wide prevalence claim, or cross-publisher generalization

## Paper/thesis use now

This rule is itself a publishability artifact: it turns the blocker from `missing admission logic` into `apply one bounded rule to one exemplar or obtain stronger institutional evidence`. That makes the lane easier to reuse in methods sections, reviewer responses, and dashboard-tool explanation without widening claims.
