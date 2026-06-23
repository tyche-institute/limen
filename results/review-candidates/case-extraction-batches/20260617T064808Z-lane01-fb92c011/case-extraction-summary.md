# Case extraction summary — 20260617T064808Z-lane01-fb92c011

Task: LIMEN source-surface case extraction.

Input rows reviewed: 9
Output rows written: 9

Verdict counts:
- closed_noncase_source_surface: 9

Extraction result:
- No cluster in this batch contains a concrete AI edge-case event/action/vulnerability/finding/official record suitable for later reviewed-core or ObscureAI hardening.
- All clusters remain source-surface/context/register/policy/product/search surfaces.
- No reviewed-core promotion, ObscureAI addition, incident truth claim, legal/safety/compliance finding, deployment proof, prevalence claim, guilt claim, or ranking claim was made.

Spot-check notes:
- Resolved during exact-URL checks: DGII chatbot page, Bahrain AI policy PDF, Cambodia GDT article page, Peru Decreto Supremo page, Falkland Islands procurement page, Palestine Monetary Authority homepage.
- Exact-URL access issue observed but not case-promoted: data.gouv.fr page returned 404; CBB fintech page returned 403; Yahoo search URL returned an error. These remain noncase source surfaces based on the input metadata and absence of a concrete case-level record.

Verification:
- Required TSV header written exactly as specified.
- One output row per input source_cluster_key.
- No duplicate output source_cluster_key values.
- Key-set and row-count verification passed.
