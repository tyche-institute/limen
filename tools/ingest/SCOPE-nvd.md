# LIMEN ingestion lane — NVD CVE 2.0 API, AI/ML-filtered

**Lane:** `ingest-nvd-ai`
**Script:** `tools/ingest/ingest_nvd_ai.py`
**Status:** STARTER (second dense lane, sibling to `ingest_ghsa_ai.py`). Writes
candidates only. Never promotes, never touches `cases.json`, never writes
reviewed-core.

---

## 1. Why this lane exists

The GHSA lane (`ingest_ghsa_ai.py`) is high precision but **narrow**: it is driven
by GitHub's `affects=<package>` filter, so it only sees vulnerabilities whose
*affected component is a package GitHub indexes* (PyPI / npm / etc.). It misses:

- AI/ML systems that are not a packaged library (model-serving appliances, vendor
  cloud products, ML platforms, AI gateways, firmware);
- CVEs published by non-GitHub CNAs that never receive a GHSA;
- the large body of "prompt injection" / "LLM" / "machine learning" CVEs that name
  an AI system in the description while their CPE is a broader product.

The **NVD CVE 2.0 API** is the authoritative US-government feed of *all* CVEs and is
fully reachable headless with **no auth**. It is strictly **broader** than GHSA's
package-affects approach (which is exactly the task brief), and the two lanes overlap
only on the subset of AI CVEs that also got a GHSA — which this lane explicitly
**de-duplicates** against by CVE id.

(The AI Incident Database — AIID — was rejected: its GraphQL endpoint is locked to its
own browser client and is not tractable headless. NVD is the tractable, dense,
genuine-edge-case alternative.)

## 2. Source

- **Name:** U.S. National Vulnerability Database (NVD), NIST.
- **Authority:** NIST/NVD; underlying CVE records issued by CVE Numbering Authorities
  and enriched by NVD analysts.
- **API:** `https://services.nvd.nist.gov/rest/json/cves/2.0` (REST, public, no auth).
- **Query mechanisms (two families, both documented and precise):**
  1. **`keywordSearch` + `keywordExactMatch`** — exact-phrase match over the CVE
     description, for a curated AI/agentic vocabulary (`STRONG_KEYWORDS`). High
     precision. Verified live: `"prompt injection"` exact -> 97 results,
     `"large language model"` -> 142, `"MCP server"` -> 132, `"AI agent"` -> 84.
  2. **`virtualMatchString=cpe:2.3:a:<vendor>:<product>`** — CPE match against a
     curated list of AI vendor:product pairs (`AI_CPE_VENDOR_PRODUCT`, e.g.
     `vllm:vllm`, `langchain:langchain`, `huggingface:transformers`). The CVE's
     affected product **is** an AI system. Verified live: `cpe:2.3:a:vllm:vllm`
     -> 46 results.
- Queries are **interleaved** (keyword, CPE, keyword, CPE, …) so a small `--max-queries`
  cap still samples both families.

## 3. License / Terms-of-Service note

- NVD data are **U.S. government public-domain works** (17 U.S.C. §105); CVE records
  and NVD enrichments are not copyrightable. Attribution to NVD / NIST and the
  per-record `CVE-…` id is courtesy, not a licence requirement.
- API use is governed by the NVD API rate limits / terms. The lane stays inside them:
  read-only, low volume, sleeps ~6.5 s between requests (unauthenticated limit is
  **5 requests / 30 s**), sends a descriptive `User-Agent`. A small run is ~8–12
  requests over ~1 minute — well within budget.
- **Recommended for production:** request a free NVD API key (lifts the limit to
  50 req / 30 s) and pass it as a header. The starter deliberately runs
  unauthenticated to require no secrets.

## 4. Cadence

- **Suggested:** weekly. NVD publishes a steady stream of new AI/ML CVEs; weekly keeps
  drift low without re-pulling the same back-catalogue.
- The lane sorts the NVD default (most-recent enrichment first) and is **idempotent per
  day**: re-running writes into the same dated `ingest-nvd-<date>/` dir.
- **Incremental upgrade (documented TODO):** add `lastModStartDate`/`lastModEndDate`
  (or `pubStartDate`/`pubEndDate`) bounds so each weekly run pulls only the new window.
  The starter pulls a recent window per query and relies on CVE-id dedup to suppress
  repeats.
- Raw API pages are cached under `<out-dir>/raw-cache/`, so `--dry-run` re-maps offline
  with zero network calls (verified: dry-run reproduces the live run's counts exactly).

## 5. Expected yield (realistic)

- **Per run (this starter, `--per-query 8 --max-queries 8`):** the live test on
  2026-06-30 pulled **51 distinct** CVEs, kept **43 clean candidates**, routed
  **3 to low-confidence** (excluded) and **5 to duplicates** (already in reviewed-core
  or the GHSA lane). Tier split: 31 `T4_reproducible_technical_finding`,
  12 `T1_single_public_source`. Origin split: 19 keyword-hit, 24 CPE-hit.
- That ~43 is the *standing back-catalogue* for the seeded vocabulary + CPE list at the
  current cap. Running the full query set (`--max-queries 0`) and a larger
  `--per-query` would pull substantially more in one go (hundreds of distinct AI CVEs
  exist across the seed terms).
- **Net-new per week** after the first sweep is the incremental rate of *new* AI CVEs
  that are not already in reviewed-core/GHSA — realistically **a handful to ~10–20 per
  week** depending on how wide `STRONG_KEYWORDS` / `AI_CPE_VENDOR_PRODUCT` are set and
  how much GHSA already covered. The big back-catalogue numbers come once; thereafter the
  lane tracks the genuine new-CVE rate.
- **Overlap with GHSA is real and handled:** the first live run already de-duplicated 5
  CVEs against reviewed-core + the latest GHSA lane (e.g. `CVE-2023-29374` = reviewed-core
  `LIMEN-000006`; `CVE-2025-47274` = `LIMEN-000016`; three already in
  `limen-reviewed-core-ghsa-v0.1.tsv`). The unique value is the CPE-driven products and
  non-GitHub CNAs the GHSA package filter cannot reach.

## 6. The human-accept boundary (STRICT)

Everything this lane emits is a **draft candidate for human review**. It is NOT a case.

- Output goes to `results/review-candidates/ingest-nvd-<date>/` only.
- `cases.json` is **never** touched; reviewed-core is **never** written (verified: no
  reviewed-core / cases.json mtimes change on a run).
- Each record is `draft_status=draft_for_human_review`,
  `promotable=yes_as_candidate_edge_case_draft`.
- `claim_ceiling` caps every record at *advisory-surface accounting*: it confirms an NVD
  CVE record exists describing the stated issue in the named AI/ML component. It does
  **not** assert real-world exploitation, realized harm, prevalence, or culpability.
- `proposed_evidence_tier` is conservative: `T4_reproducible_technical_finding` only when
  the CVE carries a CWE **and** a reference tagged `Patch`/`Exploit`/`*Advisory`;
  otherwise `T1_single_public_source`. The lane never proposes `T3` from a CVE alone.
- **A human must:** (a) confirm AI/agentic relevance, (b) confirm the record is a
  *distinct* LIMEN edge case (the lane already drops CVE-id duplicates, but human review
  must still catch near-duplicates and the same incident described differently), and
  (c) decide tier and category before any promotion. Only then does a separate, existing
  promotion step add it to reviewed-core / `cases.json`.

## 7. Anti-fabrication guarantees

- Every emitted field traces to a real NVD CVE field (id, English description, CWE,
  CVSS base score/severity/vector, CPE vendor:product, references + tags, published
  date, vulnStatus, sourceIdentifier). No invented numbers, quotes, dates, or URLs.
- `year` comes from the CVE id (`CVE-YYYY-…`), falling back to `published`; if neither
  is present it is left blank, never guessed.
- AI relevance must come from a **strong AI phrase in the description** OR an **AI CPE**
  (the affected product is an AI system). A security CWE is **never** used as an AI
  signal — every CVE has one. A single weak prose token (e.g. "model", "ai") with no AI
  CPE is routed to `low-confidence-excluded-<date>.tsv` with `low_confidence=yes` and is
  NOT in the promotable set.
- CVE ids already present in reviewed-core security TSVs or the latest GHSA lane are
  routed to `duplicates-excluded-<date>.tsv` and never re-proposed.

## 8. Outputs (per run)

| file | contents |
|---|---|
| `ingest-nvd-<date>.tsv` | 42-col draft records: **first 25 cols are byte-identical to the project's `extraction-drafts` schema**; 17 appended NVD-native provenance cols (cve, severity, cvss, product, all CPE vendor:products, cwe, dates, vuln_status, source_identifier, reference tags+urls, query_origin, rationale, matched terms/CPE). |
| `ingest-nvd-<date>.candidates.jsonl` | canonical candidate fields (`title, summary, authority, source_url, proposed_evidence_tier, claim_ceiling`, + categories/provenance), one JSON object per line. |
| `low-confidence-excluded-<date>.tsv` | CVEs dropped from the promotable set + the exact exclusion reason. |
| `duplicates-excluded-<date>.tsv` | CVEs already in reviewed-core / the GHSA lane, with the dedup reason. |
| `run-manifest.json` | run mode (LIVE/DRY-RUN), queries, counts, dedup index size + sources, fetch notes, output paths, `promoted_to_reviewed_core=0`, `cases_json_touched=false`. |
| `raw-cache/raw-*.json` | verbatim API pages for reproducibility and offline `--dry-run` re-mapping. |

## 9. Run

```bash
cd /srv/tyche/projects/limen-ai-edge-case-atlas
python3 tools/ingest/ingest_nvd_ai.py                       # live, small sample
python3 tools/ingest/ingest_nvd_ai.py --per-query 8 --max-queries 8   # the tested config
python3 tools/ingest/ingest_nvd_ai.py --max-queries 0      # full query set (larger pull)
python3 tools/ingest/ingest_nvd_ai.py --dry-run \
    --cache-dir results/review-candidates/ingest-nvd-<date>/raw-cache   # offline re-map
```

### Weekly cron (suggested — DO NOT auto-install; for the human to add)

```cron
# LIMEN NVD AI edge-case ingestion — weekly, Mondays 06:17 UTC. Writes draft
# candidates only; nothing is promoted. Log to the project results dir.
17 6 * * 1 cd /srv/tyche/projects/limen-ai-edge-case-atlas && /usr/bin/python3 tools/ingest/ingest_nvd_ai.py --per-query 8 --max-queries 8 >> results/review-candidates/ingest-nvd-cron.log 2>&1
```
