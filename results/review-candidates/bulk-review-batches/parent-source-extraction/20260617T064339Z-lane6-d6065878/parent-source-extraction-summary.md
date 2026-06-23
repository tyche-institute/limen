# Parent source extraction summary: 20260617T064339Z-lane6-d6065878

Reviewed 24 input rows exactly once using local metadata, source context, and local source-pack/refresh/ledger matches only. No web crawl or external submission was performed.

Verdict counts:
- source_url_extracted: 3
- parent_source_wrapper: 7
- country_gap_no_parent_source: 14
- source_surface_only_no_case: 0
- duplicate_existing_core: 0
- reject_noise: 0

Notes:
- Research-queue rows were treated as country/profile discovery placeholders when their local CSV row contained only country/topic search prompts and no public URL.
- Country profile/index rows with multiple local source-pack candidates were marked `parent_source_wrapper` rather than forcing an arbitrary parent URL.
- Extracted URLs are processing-state source surfaces only; they do not assert incident truth, legal status, compliance, safety, prevalence, ranking, or reviewed-core promotion.

Verification: see manifest fields updated after TSV queue_id set and row-count checks.
