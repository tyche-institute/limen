# LIMEN Envelope Profile v0.1
*Created: 2026-06-24  
Project: LIMEN AI Edge-Case Atlas (limen-ai-edge-case-atlas)
Lane: limen-boost-053  
Intended use: reproduce manuscript paper surfaces before hostile-reviewer gate

## Build Signature
reference_uuids:
  - corpus_v20260614_audit   # ledger snapshot used for manuscript baseline
  - sites_20260614_verified   # URLs already visited and archived
  - pipeline_iteration_s03_c   # obsessive deduplication / cluster pipeline with known deterministic seed

retrieval_at: "2026-06-14T12:00:00+03:00"
sha256_ledger_snapshot: "<stub pending reproduction run>"
cpu_profile: "zen3-16c-no-dgpu"
ram_mb: 32768
elapsed_minutes: TBD
reproduction_seed: 0x4e56436c_20260624
outputs_tagged:
  - figure_2_paper_source
  - figure_5_table_c
  - figure_7_dashboard_metric

## Baseline Claim Parity Rules
- manifest.observations.total_base corpus fits into envelope.profile.cpu_seconds
- every Figure referenced in the preprint must be reproducible from baselines declared above
- duplicate_count must be <= 1.2% erroneous duplicates (observed in audit); if > threshold, flag as blocker

## Output Fields Expected by Paper (checklist)
- [ ] manifest_{uuid}_baseline.tsv  # reproducibility table (ledger columns match)
- [ ] figure_2_paper_source.tsv      # Table S2 placeholders ready for indesign tool
- [ ] figure_5_table_c.tsv          # Consolidated safety/governance figures baseline
- [ ] figure_7_dashboard_metric.tsv  # Real-time dashboard metric baseline
- [ ] manuscript_json_links.json     # machine-readable mapping paper-figures ↔ ledger rows
- [ ] sha256_manifest.txt           # single file integrity hash

## Reproduction Command (runnable under /
/srv/tyche/projects/limen-ai-edge-case-atlas on zeus1)
```bash
./scripts/limen_repro_envelope.sh \
   --ref-uuid corpus_v20260614_audit \
   --seed 0x4e56436c_20260624 \
   --timeout 120m \
   --outdir ./draft/envelope_v0.1/
```

## Memory Locks & Guardrails
- Source provenance retained via ledger.origin_url and ledger.access_date
- Rights/terms notes attached to each observation_uuid in the ledger
- Athena identity continuity enforced: no cross-project permissions without explicit gate AND capsule consult
- Standard manuscript captions policy applies—not to assert compliance but to quote the recorded source language verbatim

## Next Immediate Steps (inside this lane cycle)
1. Run limen_repro_envelope.sh against already-local ledgers and let it write sha256_ledger_snapshot, manifest_{uuid}_baseline.tsv, and manuscript_json_links.json
2. Verify deterministic hashes in TDD style before touching Figures 2/5/7
3. If successful → patch Figures into draft/preprint.md; if failed → write explicit negative result to journal.md and don’t patch Figures; escalate blocker to Anton.

---
*Template version: v0.1_draft_20260624*
*Keep this under revision control along with project repo*

