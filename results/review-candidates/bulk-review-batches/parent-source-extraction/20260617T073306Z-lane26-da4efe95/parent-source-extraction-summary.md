# Parent source extraction summary

Batch: 20260617T073306Z-lane26-da4efe95
Input rows reviewed: 24
Output rows written: 24

Verdict counts:
- country_gap_no_parent_source: 24

Method:
- Reviewed each input row once using only the configured local source_path and nearby/country-object local context.
- For research-queue rows, inspected the CSV row and adjacent local context; rows are generated country/query bundles with no named source URL.
- For atlas rows, inspected the enclosing pallas_atlas_countries.json country object and checked for a matching I03/I05 top_sources URL.
- No broad web crawl, portal interaction, publication, upload, or source promotion was performed.

Notes:
- BPSE-03369: atlas Qatar I03 matches=0
- BPSE-03370: research queue Morocco; no URL fields
- BPSE-03371: research queue Rwanda; no URL fields
- BPSE-03372: atlas Niue I03 matches=0
- BPSE-03373: research queue Sierra Leone; no URL fields
- BPSE-03374: atlas Marshall Islands I05 matches=0
- BPSE-03375: research queue Eswatini; no URL fields
- BPSE-03376: research queue Hungary; no URL fields
- BPSE-03377: research queue Venezuela; no URL fields
- BPSE-03378: research queue Greenland; no URL fields
- BPSE-03379: research queue Cameroon; no URL fields
- BPSE-03380: atlas French Southern and Antarctic Lands I05 matches=0
- BPSE-03381: research queue Vatican City; no URL fields
- BPSE-03382: research queue Niger; no URL fields
- BPSE-03383: research queue Venezuela; no URL fields
- BPSE-03384: atlas Guinea I05 matches=0
- BPSE-03385: research queue Ukraine; no URL fields
- BPSE-03386: research queue Venezuela; no URL fields
- BPSE-03387: research queue Mauritania; no URL fields
- BPSE-03388: atlas Bhutan I05 matches=0
- BPSE-03389: research queue Seychelles; no URL fields
- BPSE-03390: research queue North Macedonia; no URL fields
- BPSE-03391: research queue Kazakhstan; no URL fields
- BPSE-03392: atlas Kiribati I05 matches=0
