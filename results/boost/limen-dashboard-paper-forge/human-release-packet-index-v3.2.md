# LIMEN human release packet index v3.2

- Updated UTC: 2026-06-19T16:00:09Z
- Lane: `limen-dashboard-paper-forge`
- Companion table: `results/boost/limen-dashboard-paper-forge/human-release-packet-index-v3.2.tsv`
- Companion SHA-256: `bf0a2f2a5762e9abd559a061ae4c906b08e7188473b3138c6118e4a040b615b0`
- External actions performed: `0`

## Purpose

This refresh supersedes the v2.6 packet baseline after the F1000 Method Article route lock (v2.8), public-availability reconciliation (v2.9), public-surface state grammar (v3.0), and post-v3 gate rerun (v3.1). It gives a human reviewer one current read-order table for local release review without implying that any new submission, deposit, upload, portal action, outreach, public release, peer review, or acceptance occurred.

## Result

- Current packet rows indexed: `19`.
- Missing files: `0`.
- New rows since v2.6: `4` (`route_lock_v28`, `public_availability_v29`, `public_surface_grammar_v30`, `post_v3_gate_v31`).
- External actions performed: `0`.
- Baseline state: v3.2 is the current local human-release packet baseline; v2.6 remains provenance for the pre-route-lock packet, and v2.5 remains provenance for earlier drift.

## Interpretation

Use this as a non-count-bearing package-health and human-review routing artifact. It can support a cautious methods/data-paper statement that LIMEN has an internally consistent local release packet, current route lock, and public-surface wording discipline. It must not be used to claim corpus completeness, incident truth, source truth, legal compliance/non-compliance, safety assurance, deployment status, country ranking, F1000Research acceptance, public release by this lane, or a fused GAIA/PALLAS/LIMEN denominator.

## Observatory hook

A dashboard may expose the TSV as `human_release_packet_current_baseline_v3_2` with fields `packet_id`, `path`, `exists`, `sha256`, `artifact_role`, `review_consumer`, `allowed_action`, `blocker_or_note`, and `claim_ceiling`. Interpretation: all rows must exist before human release review; `allowed_action` distinguishes internal review/run actions from Anton-only external actions; the panel is not an empirical evidence surface.

## Verification

- Pre-write gate at 2026-06-19T16:00:09Z: manifest JSON PASS; LIMEN pre-submit PASS (`9/9`, `0 FAIL`, `0 WARN`); caption-currentness pytest PASS (`2 passed`).
- Post-write gate: recorded in `results/dashboard-paper/status.md` after this artifact is written.

## Packet rows

| packet_id | exists | allowed_action | note |
|---|---:|---|---|
| `manuscript_current` | yes | `read-only-review` | Review text, denominator captions, data availability, and limitations; no portal action. |
| `dashboard_spec` | yes | `read-only-review` | Use v3.0 grammar for public-surface rows; do not treat HTTP 200 as citation-safe release proof. |
| `article_architecture` | yes | `read-only-review` | Primary route is bounded F1000Research Method Article unless Anton changes route. |
| `dashboard_api_bundle` | yes | `internal-consume` | Not public release proof; rerun build gates after content edits. |
| `static_dashboard_preview` | yes | `internal-consume` | No deploy/upload action; content/version review still required before citation-safe use. |
| `si_manifest` | yes | `read-only-review` | Check presence and hashes before any Anton-controlled deposit/upload. |
| `pre_submit_tool` | yes | `internal-run` | Rerun after every package edit. |
| `caption_gate_test` | yes | `internal-run` | Rerun after every caption/control edit. |
| `closure_audit_v23` | yes | `read-only-review` | Internal package completeness only; not an empirical evidence count. |
| `source_join_scope_v22` | yes | `read-only-review` | Keep row-level access/rights badges blocked unless file-qualified joins are verified. |
| `release_checklist_v20` | yes | `read-only-review` | External upload/deposit/submission remains Anton-controlled. |
| `status` | yes | `read-only-review` | Use newest section as operational status; not a claim source by itself. |
| `manifest` | yes | `internal-consume` | Must remain valid JSON; list current gate artifacts. |
| `drift_audit_v25` | yes | `read-only-review` | Provenance only; superseded for current hashes by v2.6/v3.2. |
| `packet_index_v26` | yes | `read-only-review` | Superseded by v3.2 because route/public-surface/gate artifacts changed after v2.6. |
| `route_lock_v28` | yes | `read-only-review` | Route-control only; no submission, acceptance, endorsement, or public-release claim. |
| `public_availability_v29` | yes | `read-only-review` | Use as prior-public-availability reconciliation only; F1000 portal not checked. |
| `public_surface_grammar_v30` | yes | `read-only-review` | Prevents HTTP reachability from being overread as publication-safe public release. |
| `post_v3_gate_v31` | yes | `read-only-review` | Latest pre-v3.2 executable gate record; v3.2 also reruns post-write gates. |
