# LIMEN source-family ledger bootstrap

Date: 2026-06-06T22:55:07Z
Lane: `limen-continuous-experiments`
Project: `limen-ai-edge-case-atlas`
Sprint context: hostile reviewer pass

## Question

What is the smallest artifact that improves paper readiness before any new crawl batch?

## Decision

Bootstrap a machine-readable `sources/source-family-ledger.tsv` from the existing
`sources/public-source-families-v0.1.tsv`, using the completeness model in
`methods/evidence-protocol-v0.1.md`.

## Inputs

- Local path: `/srv/tyche/projects/limen-ai-edge-case-atlas/sources/public-source-families-v0.1.tsv`
- Local path: `/srv/tyche/projects/limen-ai-edge-case-atlas/methods/evidence-protocol-v0.1.md`
- Local path: `/etc/tyche-factory/current-publication-sprint.md`
- Negative result: `/srv/tyche/projects/limen-ai-edge-case-atlas/publication-goal-card-current.md` not present at access time.

## Artifact created

- `/srv/tyche/projects/limen-ai-edge-case-atlas/sources/source-family-ledger.tsv`

## Paper-readiness delta

- Converts the source-family plan into a reviewer-readable ledger with explicit
  authority baseline, access method, update cadence, reuse-review status, and
  dashboard/paper hooks.
- Makes the "coverage against declared source families" claim testable without
  pretending corpus completeness.
- Creates a stable place to record future counts, duplicate rates, saturation,
  and unresolved verification queues.

## Claims verified, rewritten, or dropped

- Strengthened method claim: LIMEN completeness should be evaluated against
  declared public source families rather than total AI reality.
- Preserved caution: no source family has yet been imported, so all count-like
  fields remain `0` or `unknown`.
- Preserved caution: social/web leads remain lead-only and are not case-grade
  evidence without corroboration.

## Remaining blocker

The ledger is still a design-stage artifact. It lacks field-populated evidence
from actual small-batch probes, rights-review notes, and duplicate-rate tests.

## Next smallest publishability move

Run a bounded negative-control/source-authority experiment on one P2 family and
one P0/P1 family, then populate first non-zero ledger fields and produce a small
authority-vs-lead comparison table.

## Observatory hook

This ledger can feed:

- a source-family coverage dashboard;
- a source-authority vs lead-only matrix;
- a saturation/verification queue table for manuscript methods and limitations.
