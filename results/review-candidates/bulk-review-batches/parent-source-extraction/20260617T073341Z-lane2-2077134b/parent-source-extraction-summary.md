# Parent source extraction summary

Batch: 20260617T073341Z-lane2-2077134b
Input rows reviewed: 24
Output rows written: 24

## Verdict counts

- source_url_extracted: 1
- parent_source_wrapper: 15
- country_gap_no_parent_source: 8

## Method

Used local metadata and local source files only. Inspected the input TSV rows, the cited local JSON/CSV source lines, nearby context, and top_sources blocks where present. No broad web crawl or external submission/publishing actions were performed.

## Extracted URL

- BPSE-03596 / LIMEN-SIGNAL-F0BAF232BFA9BA93: https://www.cnil.fr/en/artificial-intelligence-and-public-services-cnil-publishes-results-its-sandbox from pallas_atlas_countries.json top_sources lines 37279-37283.

## Notes

Research-queue rows were marked parent_source_wrapper because they list generic country/query targets and multiple source-type categories without a concrete URL. Country indicator/profile rows without a matching explicit local top_source URL were marked country_gap_no_parent_source.
