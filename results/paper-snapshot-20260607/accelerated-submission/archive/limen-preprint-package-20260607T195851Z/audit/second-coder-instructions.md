# Second-coder audit instructions

Purpose: produce a small, real reliability/adjudication audit for the Route A LIMEN paper without reopening discovery.

## Scope

Use `second-coder-worksheet.tsv`. Code only the rows in that worksheet.

Fields to code:

- `evidence_tier_code`
- `source_family_code`
- `primary_category_code`
- `claim_ceiling_code`

Do not use bare legacy IDs. Use `public_id`.

## Allowed codes

Evidence tier:

- `T3_authoritative_source`
- `T3_authoritative_source_direct_url_resolved`
- `T1_single_public_source`
- `T3_authoritative_source_candidate`

Source family:

- `Regulator and enforcement sources`
- `Court and tribunal records`
- `Security research and advisories`
- `Company and platform notices`
- `Public-sector registers and procurement`
- `Reputable multilingual media and investigations`
- `Academic and research-integrity sources`

Primary category:

- `ai_washing_or_false_ai_claim`
- `security_risk`
- `agentic_control_failure`
- `public_sector_governance`
- `public_sector_misuse_or_gap`
- `legal_procedural_contamination`
- `research_integrity`
- `education_workplace_or_hr`
- `deepfake_or_synthetic_identity`
- `residual_or_low_cap_lead`

Claim ceiling:

- `narrow_source_supported_description`
- `official_summary_only`
- `charging_stage_only`
- `mechanism_exemplar_only`
- `translation_dependent_low_cap`
- `notice_bounded_only`
- `complaint_order_posture_only`
- `governance_anchor_not_harm_case`
- `appendix_candidate_hold`

## Reporting

After coding, compare the second-coder worksheet against `first-coder-answer-key.tsv`. Report:

- raw agreement by field;
- disagreements by public ID and field;
- adjudicated code;
- short reason.

Do not report kappa or alpha unless a methods reviewer specifically asks and the sample size/label distribution makes it meaningful. For this small audit, raw agreement plus disagreement typology is cleaner.
