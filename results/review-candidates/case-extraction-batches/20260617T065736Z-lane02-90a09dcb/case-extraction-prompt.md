You are Hermes/Codex performing LIMEN source-surface case extraction.

Input TSV:
/srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/case-extraction-batches/20260617T065736Z-lane02-90a09dcb/input.tsv

Required outputs:
/srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/case-extraction-batches/20260617T065736Z-lane02-90a09dcb/case-extraction-results.tsv
/srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/case-extraction-batches/20260617T065736Z-lane02-90a09dcb/case-extraction-summary.md

Update this manifest when complete:
/srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/case-extraction-batches/20260617T065736Z-lane02-90a09dcb/manifest.json

Task:
- Review every source_cluster_key in input.tsv exactly once.
- Your goal is to decide whether the cluster contains a concrete AI edge-case suitable for later reviewed-core/ObscureAI hardening, or whether it is finally a noncase source surface.
- Use the input row metadata. You may inspect exact local file locators and exact public URLs present in source_url_or_locator. Do not broad crawl, search the web generally, or invent URLs.
- Do not submit, publish, email, upload, register, pay, log into portals, or take public actions.
- Do not promote anything. This is extraction only.
- A case candidate must have a concrete event/action/vulnerability/finding/official record, a public source URL or precise locator, and a bounded claim that does not overread legality, safety, compliance, deployment, prevalence, or guilt.
- Scholarly DOI/index pages, algorithm registers, policy/guidance/law text, patents, vendor docs, product pages, and generic source-family surfaces are usually closed_noncase_source_surface unless they explicitly contain a concrete edge-case event/finding.

Write case-extraction-results.tsv with exactly this header:
source_cluster_key	case_extraction_verdict	source_url_or_locator	source_name	source_host	proposed_case_title	proposed_evidence_tier	proposed_limen_categories	source_record_date	jurisdiction	bounded_claim_candidate	claim_ceiling	forbidden_overread	rationale	required_before_reviewed_core	required_before_obscure_ai	next_action

Allowed case_extraction_verdict values:
- case_candidate_for_hardening
- closed_duplicate_existing_core
- closed_noncase_source_surface
- blocked_no_public_source
- needs_original_source_text
- reject_noise

Use one row per input source_cluster_key, no omissions, no extras, no duplicate source_cluster_key values.
Keep fields concise. Replace tabs/newlines inside fields with spaces.
Before stopping, verify that the result TSV has exactly the same source_cluster_key set and row count as input.tsv.
Boundary: no reviewed-core promotion, no ObscureAI addition, no incident truth, legal finding, safety finding, compliance finding, deployment proof, prevalence, or ranking claim.
