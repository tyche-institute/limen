# Smallest Publishable Experiment - LIMEN Continuous Experiments

## Goal
Identify and execute the next smallest useful experiment that yields a durable research artifact (e.g., source ledger entry, matrix row, figure draft) while preserving citation discipline and public-affiliation rules.

## Context
- Current lane: `limen-continuous-experiments` in project `limen-ai-edge-case-atlas`.
- Active publication sprint directive: read `/etc/tyche-factory/current-publication-sprint.md` if it exists.
- Athena continuity requirement: must refer to memory capsule `/srv/tyche/repos/tyche-research-vault/meetings/ATHENA-CODEX-MEMORY-TRANSFER-2026-06-08.md`, which mandates consulting Zeus1 holding path for architecture-history context when needed.
- Must preserve Anton's public-affiliation rules, Zetes wall, citation discipline, approval gates.
- Must leave at least one durable artifact (e.g., source ledger update, matrix row, figure draft).
- Must record provenance: source URL, retrieval date, language, jurisdiction, rights notes, etc.
- Must separate evidence from interpretation; use cautious language.
- Must avoid external submissions, credential storage, legal compliance claims.
- Must not bulk download; prefer small reproducible batches.

## Proposed Approach
1. **Assess current state**: List files in project root, verify presence of `journal.md`, `next.md`, etc.
2. **Read sprint directive**: If `/etc/tyche-factory/current-publication-sprint.md` exists, parse its contents to identify priority.
3. **Select smallest experiment**: 
   - Conduct a source-family probe or duplicate-cluster test using publicly available data.
   - Capture results with full provenance metadata (source URL, access date, language, jurisdiction, rights, checksum).
4. **Update ledger**: Add a new entry to `sources/sources.md` with the provenance details.
5. **Update matrix/coverage**: If applicable, append a row to the relevant coverage matrix (e.g., country/language coverage).
6. **Draft journal entry**: Write a concise section in `journal.md` describing the experiment, its outcome, and any negative results.
7. **Log next step**: Update `next.md` with the subsequent smallest action (e.g., “monitor for readable body text threshold upgrade”).
8. **Compliance check**: Verify that all updates respect public-affiliation rules and citation discipline; ensure no prohibited actions (bulk download, credential storage) are performed.
9. **Record artifact**: Store the experiment output (e.g., a short markdown summary, a matrix row, or a figure draft) under `experiments/` for future reference.

## Risks and Open Questions
- Ensure no violation of public-affiliation rules or citation discipline.
- Approval gates: any step requiring external approval must be paused until user input.
- Repository creation is currently blocked due to GitHub auth constraints; manual intervention may be needed for publishing.

## Next Steps
Execute steps 1–9 in the upcoming cycle, prioritizing a source-ledger update with full provenance and a concise journal entry that can serve as evidence for future manuscript sections.