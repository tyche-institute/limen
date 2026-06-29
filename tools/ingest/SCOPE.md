# LIMEN ingestion lane — GitHub Security Advisories (GHSA), AI-filtered

**Lane:** `ingest-ghsa-ai`
**Script:** `tools/ingest/ingest_ghsa_ai.py`
**Status:** STARTER. Writes candidates only. Never promotes, never touches `cases.json`.

---

## 1. Why this lane exists

The existing LIMEN candidate pool is dominated by **register entries** — e.g. the
Dutch national Algorithm Register (`algoritmes.overheid.nl`). The project itself
classifies these as `public_register_entry_noncase` / `closed_noncase_source_surface`:
a register listing proves a *source surface* exists; it is **not** a documented
edge-case event, incident, or finding. A spot check of
`results/review-candidates/reviewed-core-case-extraction-results-v0.1.tsv` shows it is
almost entirely `closed_noncase_source_surface` rows (agency homepages, legal-text
pages, static SVG assets, register listings). That pool cannot grow an *atlas of
genuine edge cases*.

GHSA is a high-yield public source of **genuine** AI edge cases: each GitHub-reviewed
advisory documents a concrete, often reproducible technical failure in a real, named
AI/agentic software component, with a stable citable URL, an issuing authority, severity,
CVSS, CWE, and dates. Filtered for AI tooling it surfaces exactly the
`security_risk` / `agentic_control_failure` / confused-deputy material LIMEN tracks
(cf. reviewed-core LIMEN-000008 LangChain, LIMEN-000010 export-control).

## 2. Source

- **Name:** GitHub Advisory Database (GHSA).
- **Authority:** GitHub, operating as a CVE Numbering Authority (CNA). The lane pulls
  only `type=reviewed` advisories (GitHub-curated), not raw `unreviewed` ones.
- **API:** `https://api.github.com/advisories` (REST, public, no auth required for read).
- **Query mechanism:** the **structured `affects=<package>` filter** against a curated
  list of known AI / agentic / LLM-tooling package names (`AI_PACKAGES` in the script).
  IMPORTANT: the endpoint's free-text `query` param is **silently ignored** (verified:
  `query=MCP` and `query=langchain` return the identical newest-first list). Driving the
  lane off affected-package names is both higher precision and the documented contract.

## 3. License / Terms-of-Service note

- GHSA advisory **content** is published by GitHub under **CC-BY-4.0**
  (github.com/github/advisory-database states CC-BY-4.0 for the database). Attribution to
  the GitHub Advisory Database + the per-advisory `GHSA-…`/`CVE-…` id satisfies it.
- API use is governed by the **GitHub Terms of Service** and **Acceptable Use Policies**.
  The lane stays within them: read-only, low volume, honours the documented rate limit,
  sends a descriptive `User-Agent`, sleeps 1 s between calls. Unauthenticated limit is
  ~60 requests/hour; the lane uses ~6 calls per run (packages batched 8 per call).
- Underlying CVE records are US-government public data (not copyrightable). Individual
  reproduction snippets quoted inside an advisory remain the advisory author's; the lane
  stores only short excerpts plus metadata and always links to the canonical advisory.
- **Recommended for production:** set a `GITHUB_TOKEN` to lift the limit to 5,000/hr (the
  starter deliberately runs unauthenticated to require no secrets).

## 4. Cadence

- **Suggested:** weekly. GHSA reviews a modest steady stream of new AI-package advisories;
  weekly keeps drift low without re-pulling the same records constantly.
- The lane sorts `published desc` and is **idempotent per day**: re-running writes into the
  same dated `ingest-ghsa-<date>/` dir. For a true incremental lane, add a high-water mark
  on `published_at` (left as a documented TODO; the starter pulls a recent window each run).
- Raw API pages are cached under `<out-dir>/raw-cache/` so `--dry-run` can re-map offline
  with zero network calls (useful for re-running the mapper after a logic change).

## 5. Expected yield (realistic)

- **Per run (this starter config, ~32 AI packages, `--per-query 10`):** ~40–50 distinct
  AI advisories pulled; the live test on 2026-06-29 returned **44 distinct, 44 kept,
  0 low-confidence** (all came back from the AI-package `affects` filter, so all are
  genuine AI components). Tier split: 32 `T4_reproducible_technical_finding`,
  12 `T1_single_public_source`.
- That ~44 is the *standing back-catalogue* for the seeded package list. After the first
  run, **net-new yield is the incremental rate of new AI advisories — realistically a
  handful per week**, not 44 every week. The big numbers come from widening `AI_PACKAGES`,
  not from re-running.
- **De-duplication is a human/next-stage job:** some advisories already exist in
  reviewed-core (the project notes a LangChain GHSA is reviewed-core `LIMEN-000008`).
  The lane flags `required_before_reviewed_core` = confirm non-duplication; it does not
  silently drop near-duplicates.

## 6. The human-accept boundary (STRICT)

Everything this lane emits is a **draft candidate for human review**. It is NOT a case.

- Output goes to `results/review-candidates/ingest-ghsa-<date>/` only.
- `cases.json` is **never** touched; reviewed-core is **never** written.
- Each record is `draft_status=draft_for_human_review`,
  `promotable=yes_as_candidate_edge_case_draft`.
- `claim_ceiling` caps every record at *advisory-surface accounting*: it confirms a
  GitHub-reviewed advisory exists describing the stated issue in the named component. It
  does **not** assert real-world exploitation, realized harm, prevalence, or culpability.
- `proposed_evidence_tier` is conservative: `T4_reproducible_technical_finding` only when
  the advisory carries a CWE **and** a reproduction or a first-patched version; otherwise
  `T1_single_public_source`. The lane never proposes `T3` from a GHSA alone.
- **A human must:** (a) confirm AI/agentic relevance, (b) confirm the record is a *distinct*
  LIMEN edge case and not a duplicate of an existing reviewed-core entry, and (c) decide
  tier and category before any promotion. Only then does a separate, existing promotion
  step add it to reviewed-core / `cases.json`.

## 7. Anti-fabrication guarantees

- Every emitted field traces to a real GHSA record field (id, summary, description excerpt,
  package, severity, CVSS, CWE, dates, references). No invented numbers, quotes, or URLs.
- `year` comes from `published_at`; if absent it is left blank, never guessed.
- AI relevance must come from AI-specific vocabulary OR an AI affected-package match — a
  security CWE is **never** used as an AI signal (every GHSA has one). This killed an early
  false positive where a non-AI pnpm advisory matched only because its patch was credited to
  "an agent (codex, gpt-5)".
- Records that match AI vocabulary only weakly (single prose token, component not itself an
  AI package) are written to `low-confidence-excluded-<date>.tsv` with `low_confidence=yes`
  and are NOT in the promotable set.

## 8. Outputs (per run)

| file | contents |
|---|---|
| `ingest-ghsa-<date>.tsv` | 36-col draft records: first 25 cols match the project's `extraction-drafts` schema; 11 appended GHSA-native provenance cols (cve, severity, cvss, package, cwe, dates, refs, rationale). |
| `ingest-ghsa-<date>.candidates.jsonl` | canonical candidate fields (`title, summary, authority, source_url, proposed_evidence_tier, claim_ceiling`, + categories/provenance), one JSON object per line. |
| `low-confidence-excluded-<date>.tsv` | advisories dropped from the promotable set + the exact exclusion reason. |
| `run-manifest.json` | run mode (LIVE/DRY-RUN), packages queried, counts, fetch notes, output paths, `promoted_to_reviewed_core=0`, `cases_json_touched=false`. |
| `raw-cache/raw-*.json` | verbatim API pages for reproducibility and offline `--dry-run` re-mapping. |

## 9. Run

```bash
cd /srv/tyche/projects/limen-ai-edge-case-atlas
python3 tools/ingest/ingest_ghsa_ai.py                 # live, small sample
python3 tools/ingest/ingest_ghsa_ai.py --per-query 5   # smaller
python3 tools/ingest/ingest_ghsa_ai.py --dry-run       # offline; re-map cached pages
```
