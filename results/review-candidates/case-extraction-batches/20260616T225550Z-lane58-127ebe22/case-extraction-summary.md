# Case extraction summary: 20260616T225550Z-lane58-127ebe22

Input: /srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/case-extraction-batches/20260616T225550Z-lane58-127ebe22/input.tsv
Results: /srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates/case-extraction-batches/20260616T225550Z-lane58-127ebe22/case-extraction-results.tsv

Reviewed source_cluster_key rows: 16

Verdict counts:
- closed_noncase_source_surface: 15
- needs_original_source_text: 1

Extraction notes:
- No reviewed-core promotion and no ObscureAI addition were performed.
- Exact supplied URLs/locators and input metadata were used; no broad web crawling or invented URLs were used.
- The batch is dominated by vendor home/product pages, official portals, policy/guideline/framework pages, and one malformed/inaccessible locator. These surfaces do not expose a concrete bounded AI edge-case event/action/vulnerability/finding suitable for hardening.
- One row (`https://ramp.com/blog/ramp-agents-announcement::Ramp`) needs original source text or a corrected exact locator because the supplied exact locator returned HTTP 404.

Boundary retained: dispositions are source-surface accounting only; they make no incident truth, legal finding, safety finding, compliance finding, deployment proof, prevalence, guilt, or ranking claim.
