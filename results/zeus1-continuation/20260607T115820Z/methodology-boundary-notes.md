# LIMEN Zeus1 Continuation Methodology Notes

Cycle timestamp: 2026-06-07T11:58:20Z

This bundle is additive. It does not overwrite existing reviewed-case ledgers, source-family ledgers, or dashboard-paper control surfaces. Its purpose is to give the public observatory builder a dated merge candidate with explicit evidence boundaries.

## Public Evidence Boundary

- Public sources only: official regulator/court/public-body pages, public publisher pages, public DOI metadata, public broadcaster/news pages, and local LIMEN artifacts derived from prior public-source checks.
- No paywall, access-control, 403, challenge, or rate-limit bypass was attempted.
- FTC pages were publicly discoverable through web/search open, but local shell checks returned 403. The bundle records that as a link-check limitation rather than trying alternate bypass routes.
- Non-English sources are paraphrased cautiously. Original-language URLs and language labels are preserved for translation review.

## Deduplication Discipline

- Bare `LIMEN-00000x` identifiers are not safe global keys. The existing cluster ledger shows collisions between authoritative, security, and AI-washing files.
- Dashboard joins should use file-qualified keys or a later globally normalized ID.
- Derivative multilingual queue rows are collapsed into one lineage when they share `LMWCS-*` IDs and source trail, but their queue/provenance history remains useful.
- SEC Delphia and Global Predictions are distinct cases, but shard-local SEC rows are derivative duplicates of the promoted authoritative rows.

## Promotion Discipline

- `reviewed-promotion-queue.tsv` separates:
  - promotion-ready direct document/source records;
  - source-checked but not-yet-canonical official leads;
  - complex posture rows that must be held until documents are read.
- FTC DoNotPay and Workado look like strong non-finance official AI-claim candidates, but the canonical case rows should wait for complaint/order document reading.
- FTC Rytr must not be counted as a simple final-order exemplar because the official case page records a later set-aside order.
- The Danish Datatilsynet row is an authoritative public-sector governance anchor, not a harmful-use case by itself.

## Claim Ceilings

- Do not make legal conclusions, illegality findings, compliance claims, AI Act risk classifications, prevalence claims, or safety/effectiveness claims from these rows.
- Regulator orders and consent decrees support narrow posture-aware statements about the issuing body's document text.
- Charging-stage records support accusation-stage statements only.
- Publisher retraction/status pages support notice-bounded research-integrity statements only.
- Direct article reachability is not official corroboration.

## Dashboard Use

Recommended import order:

1. `candidate-examples-table.tsv` for candidate cards and unresolved leads.
2. `reviewed-promotion-queue.tsv` for human review and canonical promotion decisions.
3. `authoritative-source-anchors.tsv` for source panels and evidence-tier badges.
4. `category-source-family-counts.tsv` for count widgets, with the caveat that visible-row counts are not lineage counts.
5. `date-normalization-notes.tsv` and `public-link-source-check-notes.tsv` for tooltips, source QA, and blocked-route badges.

Keep current headline lineage counts routed through `results/taxonomy/taxonomy-delta-v0.1.md` and duplicate controls until the new candidates are deliberately merged.
