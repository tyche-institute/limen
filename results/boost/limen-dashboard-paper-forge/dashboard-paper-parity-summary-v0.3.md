# LIMEN Dashboard/Paper Parity Pack v0.3 — second-stage funnel

Generated UTC: 2026-06-18T15:38:51Z
Lane: `limen-dashboard-paper-forge`

## What changed

This pass corrects the AI-washing posture input pointer and builds a second-stage funnel from review candidates through source review, promotion hardening, case extraction, hardening review, auto-review, final adjudication, and posture-aware exemplar rows.

## Outputs

- `second-stage-reviewed-core-funnel-v0.3.tsv` — dashboard/paper funnel rows with explicit denominators, claim ceilings, paper use, and next actions.
- `second-stage-reviewed-core-breakdowns-v0.3.tsv` — categorical breakdowns for triage verdicts, completion states, promotion/readiness states, extraction verdicts, hardening decisions, final decisions, and AI-washing authority posture.
- `ai-washing-posture-pointer-resolution-2026-06-18.md` — provenance note resolving the missing `limen-boost-009` pointer to the live `results/dashboard-paper/ai-washing-posture-table-v0.1.tsv` artifact.
- `dashboard-paper-parity-manifest-v0.3.json` — checksums for this pass.

## Key counts

| Surface | Count | Reviewer-safe interpretation |
|---|---:|---|
| Materialized review candidates | 55725 | Triage denominator only. |
| First-pass reviewed rows | 55725 | Routing labels only. |
| Direct-source review queue | 13918 | Needs source/source-pack/translation-aware review before example promotion. |
| Source-review completion ledger | 1646 | Completion/closure states, not incident proof. |
| Source-review promotion hardening rows | 1646 | Workflow gates; 7 linked existing reviewed-core case IDs. |
| Reviewed-core promotion packet rows | 2006 | Readiness packet, not final acceptance. |
| Case extraction result rows | 977 | Extraction verdicts include noncase closures and proposals. |
| Hardened case review rows | 13 | 11 rows ready for human acceptance but not promoted automatically. |
| Auto-review rows | 13 | Advisory crosscheck only. |
| Final adjudication rows | 14 | Inclusion/exclusion actions and rationale sidecar. |
| AI-washing posture exemplar rows | 4 | Authority-posture exemplars from corrected dashboard-paper path. |

## Paper-readiness delta

Figure 2 can now show a true second-stage attrition path rather than stopping at source-level audit denominators. The manuscript can describe a reproducible gate sequence: review candidate → first-pass review → direct-source queue → source-review completion → promotion hardening → case extraction → hardening review → final adjudication/exemplar posture, while preserving the rule that automation does not silently promote new reviewed-core cases.

## Limitations and negative evidence

- The old boost-009 path is absent; the corrected live AI-washing posture table is under `results/dashboard-paper/`.
- Hardening and auto-review rows remain advisory where `human_acceptance_required` or `ready_for_human_acceptance_not_promoted` applies.
- The v0.3 funnel supports workflow transparency and dashboard/paper denominator parity; it does not support completeness, prevalence, legal guilt, compliance, deployment, safety, or country ranking claims.

## Next smallest publishability move

Wire `second-stage-reviewed-core-funnel-v0.3.tsv` into the dashboard Figure 2 panel and add a manuscript methods paragraph stating the automation/human-acceptance boundary before using any new examples.
