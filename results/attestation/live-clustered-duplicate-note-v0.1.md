# Live clustered duplicate note v0.1

Updated: 2026-06-07T06:13:45Z
Lane: `limen-attestation-receipt-profile`
Project: `limen-ai-edge-case-atlas`
Subject kind: `duplicate_cluster`
Subject id: `REVIEW-NOMERGE-CODEEXEC-002`

## Reviewed cluster-control subject

- Duplicate-control row: `REVIEW-NOMERGE-CODEEXEC-002`
- Source artifact: `results/clusters/duplicate-clusters-v0.1.tsv`
- Supporting status artifact: `results/clusters/status.md`

## Cluster/control finding

The row records a reviewed non-merge between LangChain `LIMEN-000006` and LlamaIndex `LIMEN-000007`. Both cases involve model-mediated code reaching execution surfaces, but the current package keeps them separate because they concern different frameworks, different advisories, and no shared event lineage.

## Cluster/control decision

- Action posture: `clustered`
- Keep the relationship as a duplicate-control linkage, not an event merge.
- Allow the pair to support a repeated execution-surface subtype in methods/results discussion.
- Do not use the linkage to claim recurrence counts, prevalence, or same-incident identity.

## Paper/thesis use

This note can feed a duplicate-control appendix or figure caption explaining why LIMEN uses relationship edges for subtype interpretation without collapsing distinct events.

## Dashboard hook

- `duplicate_cluster_graph`
- `attestation_timeline`

## Remaining verification need

A stronger merge claim would require shared event identifiers, shared actor lineage, or authoritative cross-source evidence tying the two rows to the same incident, which the current local package does not provide.
