# limen-boost-023 cluster publication routing note

## Why this artifact exists

Shard 023 rotates back to theme 011 (duplicate clustering, source authority, and confidence scoring) and this pass deepens the earlier normalization work by catching the local routing surfaces up to the live duplicate-cluster ledger.

## Current cluster posture summary

- `identifier_collision_blocker`: 10 clusters
- `stable_duplicate_cluster`: 7 clusters
- `reviewed_not_duplicate`: 8 clusters
- `no_cluster_review_row`: 7 rows

## Publication-routing interpretation

- `normalized_key_propagation`: 10 rows. These are not evidence duplicates; they are join hazards created by bare local `LIMEN-...` id reuse across distinct lineages.
- `representative_sync_and_provenance_preservation`: 7 rows. These should collapse to one lineage for counts while retaining derivative provenance trails for methods/reproducibility discussion.
- `subtype_caption_control`: 8 rows. These are repeated patterns in the same regulator/product/subtype neighborhood and should remain distinct cases, but captions and graph overlays must stop them from being read as one event.
- `singleton_watch_and_join_safety`: 7 rows. These are countable one-lineage records with no reviewed overlap package yet; they belong in bounded watch panels, not recurrence prose.

## Graph and ledger posture

- Pairwise graph overlays now total `22` fully materialized edges: `14` identifier-collision blocker edges and `8` reviewed-not-duplicate edges.
- Stable duplicate clusters and singleton watch rows remain ledger-only controls under the current Figure 4 contract.
- The local shard-023 routing surfaces now match the live `results/clusters/duplicate-clusters-v0.1.tsv` row universe instead of the older pre-singleton/pre-FTC local subset.

## Family concentration

- `same_case_id_string_across_distinct_events`: 10 rows
- `standalone_lineage_pending_future_overlap_review`: 7 rows
- `shared_candidate_id_and_selected_from_linkage`: 5 rows
- `shared_concrete_failure_mode`: 4 rows
- `shared_system_family_only`: 2 rows
- `shared_order_trail_and_local_promotion`: 2 rows
- `shared_authority_actor_only`: 1 row
- `shared_regulator_batch_only`: 1 row

## Paper/thesis use

- Methods/data paper: count-safe rules for lineages, duplicate collapse, non-merge subtype edges, and singleton watch-state handling.
- Thesis chapter on evidence infrastructure: compact explanation of why strong public rows still need identifier controls before they enter figures, maps, denominators, and recurrence prose.
- Dashboard QA: machine-readable cluster routing can gate whether a row becomes a count, a provenance footnote, a subtype-edge in a graph, or a singleton watch tile.
