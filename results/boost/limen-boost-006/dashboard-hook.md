# Public-sector disclosure asymmetry dashboard hook

- Timestamp (UTC): 2026-06-07T02:36:28Z
- Lane: `limen-boost-006`
- Sprint route: hostile-reviewer pass via figure/table hardening, not new harvesting.

## Inputs

- `results/boost/limen-continuous-experiments/public-sector-disclosure-field-completeness-v0.1.tsv`
- `results/boost/limen-continuous-experiments/public-sector-disclosure-comparison-v0.1.tsv`
- `results/boost/limen-boost-006/disclosure-asymmetry-scoreboard.tsv`

## Figure/table proposal

Working figure title: `Public-sector AI disclosure asymmetry: project pages, regulator packages, and register rows expose different evidence strengths`

Recommended table rows: `psdc-001` to `psdc-005`.

Recommended visible columns:

1. `jurisdiction`
2. `surface_class`
3. `direct_source_resolved`
4. `procurement_or_register_trace`
5. `explicit_legal_basis_signal`
6. `deployment_stage_signal`
7. `human_review_or_governance_signal`
8. `supplier_signal`
9. `impact_assessment_signal`
10. `visible_signal_count`
11. `dominant_gap_type`

## Reviewer-safe interpretation

- The current local public-sector package does not support a single transparency score.
- The package now includes two positive municipal register rows rather than one: the Dutch Amsterdam entry remains the richest current disclosure surface in field visibility (`visible_signal_count=5`), while the Helsinki parking-chatbot register row exposes supplier, human-oversight, and risk-management sections but still lacks a public buyer-side procurement or DPIA companion (`visible_signal_count=4`).
- The two UK regulator-package rows are strongest for quoted legal-basis and remediation language (`visible_signal_count=3` each), but they still do not expose buyer-side procurement traces.
- The Slovenian project-page row shows public-body involvement and governance language (`visible_signal_count=1`) while remaining weak for procurement, supplier, impact-assessment, and deployment reconstruction.

## Dashboard hook

- Heatmap or dot-matrix view: one row per `comparison_row_id`, one column per disclosure field, with a sidecar `visible_signal_count` bar and a surface-class split that keeps the two register rows visible as separate municipal exemplars.
- Tooltip fields: `jurisdiction`, `surface_class`, `figure_caption_claim_safe`, `dominant_gap_type`.
- Legend should distinguish `yes`, `no`, and non-binary states such as `project_only` rather than collapsing them.

## Manuscript use

- Methods/data paper: compact demonstration that public-sector AI observability depends on surface type, not just presence of a public mention.
- Governance article: bounded claim that register visibility, regulator visibility, and project-page visibility create different reconstruction ceilings.
- Thesis/dashboard: reusable field schema for a disclosure-completeness panel and municipal/public-authority comparison view.

## Caution

Do not convert the scoreboard into legality, compliance, procurement-misconduct, or hidden-deployment claims. It only summarizes which disclosure fields are currently visible in the local public package.

## Next smallest publishability move

Add one public buyer-side tender, award, contract, or DPIA companion so the figure stops depending on register-only transparency surfaces.
