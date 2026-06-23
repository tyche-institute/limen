# LIMEN preprint residue audit

Cycle timestamp (UTC): 2026-06-17T11:25:02Z
Lane: `limen-dashboard-paper-forge`
Project: `limen-ai-edge-case-atlas`

## Purpose

Record the post-normalization residue that remains in `draft/preprint.md` after converting the front-door manuscript layer away from shard-fragment headings and several legacy table-slot labels.

## Inputs

- `draft/preprint.md`
- `results/dashboard-paper/live-export-audit-2026-06-17T10-50-02Z.tsv`
- `results/dashboard-paper/dashboard-paper-figure-route-registry-2026-06-16T23-33-03Z.tsv`
- `results/dashboard-paper/caption-control-register-v0.1.tsv`

## Residue counts

- Legacy `Table 1*` references: `3`
- Legacy `Table 6*` references: `3`
- Shard fragment headings: `0`
- Unique boost-local path references: `19`

## Interpretation

- The live dashboard/article front door remains current and unchanged at the shared-export level.
- The manuscript layer is cleaner than the 2026-06-17T10:50:02Z residue snapshot: shard-fragment headings are gone, the current audit timestamp is synchronized, and several front-door table references now follow the live Table A / Table B naming.
- Remaining residue is concentrated in appendix-style routing prose and boost-local provenance bundles, not in live denominator control.

## Quarantine rule

Treat the remaining `Table 1*`, `Table 6*`, and boost-local bundle references as appendix/control-surface residue unless each item is explicitly mapped to the live Figure 1-8 / Table A-C contract.

## Next bounded move

Normalize the remaining `Table 1D`, `Table 1F`, `Table 1G`, and `Table 6` mentions into route-safe appendix or companion naming, then trim boost-local provenance paths where the shared dashboard-paper controls already provide the necessary manuscript-facing authority.
