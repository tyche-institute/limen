# limen-boost-060 visual package current-source note

- Generated: 2026-06-07T13:54:20Z
- Manifest: `results/boost/limen-boost-060/visual-package-current-source-map.tsv`
- Shared visual artifacts mapped: 16
- Figure rows: 8
- Table rows: 8
- Boost-local export sources still blocked from shared `results/dashboard/` promotion: 10
- Already-shared or direct source surfaces without a blocked dashboard export step: 6
- Visuals with no caption-control row yet: 0
- Visuals with multiple caption-control rows: 1 (`LIMEN-VIS-002`)

Interpretation:
- The manifest now enumerates the full live reviewer-facing visual package, including `LIMEN-VIS-016` / Table 1G attestation trust-surface readiness ladder.
- Figure 2 and Figure 4 current-state wording now matches the newer shared priority/caption-control layer, so manifest consumers no longer inherit the older staged taxonomy `10 / 2 / 3` wording or the obsolete Figure 4 `17`-row duplicate-ledger summary from this routing file.
- Ten visuals still depend on boost-local sources because shared `results/dashboard/` promotion remains blocked on this host; six already use a shared or direct source surface.
- Every currently mapped visual has at least one shared caption-control row, so default QA can start from the manifest and then route into the listed `control_ids` instead of re-testing whether a visual is still uncaptained.
- The note is packaging infrastructure only. It does not add new case, legal, prevalence, or compliance claims.

Suggested default QA route:
1. Start from `visual-package-current-source-map.tsv`.
2. For each reused visual, open `current_source_path` first.
3. Open every listed `control_ids` row in `results/dashboard-paper/caption-control-register-v0.1.tsv`.
4. If `promotion_state` is `ready_but_not_promoted`, treat the boost-local or dashboard-paper source as canonical until the host write blocker on `results/dashboard/` is genuinely lifted.
5. Only then inspect shared prose surfaces such as `draft/preprint.md`, `papers/article-architecture-v0.1.md`, or `dashboard/limen-dashboard-spec-v0.1.md`.
6. Use lane-local repair ledgers only as provenance of why a current-source row changed; do not treat them as the live source of truth.
