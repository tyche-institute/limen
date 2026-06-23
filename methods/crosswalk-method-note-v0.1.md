# Crosswalk Method Note v0.1

This document describes the methodology used to create the `source-crosswalk-v0.1.tsv` file for the LIMEN AI Edge Case Atlas project.

## Objective
Produce a lightweight crosswalk mapping public AI incident/risk/vulnerability sources to standardized categories, while capturing reuse permissions.

## Sources Reviewed
- **AI Incident Database (AIID)** – https://incidentdatabase.ai
- **OECD AI Governance Principles** – https://www.oecd.org/ai
- **AI Vulnerability Database (AVID)** – https://avid.dev
- **MIT AI Risk Repository** – https://github.com/aimodelrisk/aimodelrisk
- **CSET AI Harm Dataset** – https://cset.ai/ai-harm
- **MITRE ATLAS** – https://atlas.mitre.org

## Process
1. **Source Discovery** – Locate official public endpoints and documentation.
2. **Category Extraction** – Identify stated taxonomy or categories (e.g., harm types, threat tactics).
3. **Reuse Term Capture** – Record publicly stated licensing or reuse permissions (e.g., CC BY 4.0, MIT, Open OECD).
4. **Mapping** – Align each source’s categories to a common set of crosswalk categories.
5. **Documentation** – Store mappings in TSV format with source URL and license notes.

## Output
- `results/crosswalks/source-crosswalk-v0.1.tsv` – Tab‑separated mapping file.
- `results/crosswalks/status.md` – Status update on crosswalk creation.
- `methods/crosswalk-method-note-v0.1.md` – This methodology.

## Limitations
- Only publicly advertised licenses were considered; internal reuse policies may differ.
- Category alignment is approximate; some sources use different terminology.
- No large-scale data extraction was performed; mapping relies on publicly visible descriptions.

*End of note.*