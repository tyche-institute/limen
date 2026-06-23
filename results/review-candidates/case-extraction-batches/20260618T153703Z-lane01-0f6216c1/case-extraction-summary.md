# Case extraction summary: 20260618T153703Z-lane01-0f6216c1

- Input rows reviewed: 1
- Output rows written: 1
- Verdict counts:
  - closed_noncase_source_surface: 1

## Extraction decision

The only source_cluster_key, `https://eur-lex.europa.eu/eli/dir/2024/2853/oj`, was closed as `closed_noncase_source_surface`.
The supplied source surface is an EUR-Lex ELI/legal text surface for Directive (EU) 2024/2853. The input metadata does not expose a concrete AI edge-case event, authority action, vulnerability, finding, or official case-level record suitable for reviewed-core/ObscureAI hardening.

Boundary retained: no incident truth, legal finding, safety finding, compliance finding, deployment proof, prevalence, guilt, ranking, reviewed-core promotion, or ObscureAI addition was made.

## Verification

- Required TSV header used exactly.
- One output row per input source_cluster_key.
- No duplicate source_cluster_key values.
- Output source_cluster_key set matches input source_cluster_key set.
