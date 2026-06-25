# LIMEN Dashboard API Specification v0.1

## Overview
RESTful API endpoints for the LIMEN dashboard to fetch and manipulate data for visualization.

## Endpoints

### 1. Source Family Coverage
**GET /api/source-coverage**
- **Description**: Retrieve hierarchical source coverage data for sunburst chart
- **Params**: 
  - `depth`: integer (1-3) for hierarchy level
- **Response**: JSON array with source family, subcategories, counts, and gaps

### 2. Evidence Tier Funnel
**GET /api/evidence-funnel**
- **Description**: Get evidence progression data for stacked bar chart
- **Params**: 
  - `stage`: filter by evidence stage (raw/reviewed/validated/claim-supported/published)
- **Response**: Object with stage counts and transition metrics

### 3. Taxonomy Heatmap
**GET /api/taxonomy-heatmap**
- **Description**: Retrieve matrix data for heatmap visualization
- **Params**:
  - `jurisdiction`: filter by jurisdiction code
  - `category`: filter by taxonomy category
- **Response**: 2D array with jurisdiction × category frequencies

### 4. Jurisdiction/Language Map
**GET /api/language-map**
- **Description**: Get geographic and linguistic data for choropleth map
- **Params**:
  - `language_vitality`: filter by UNESCO vitality status (1-4)
- **Response**: GeoJSON with language distribution and vitality overlay

### 5. Legal Uncertainty Matrix
**GET /api/legal-matrix**
- **Description**: Retrieve legal framework alignment scores
- **Params**:
  - `dimension`: filter by matrix dimension (compliance/enforceability/clarity/adaptability)
- **Response**: Radar chart data with framework scores

### 6. Security/Agentic Crosswalk
**GET /api/security-crosswalk**
- **Description**: Get relationships between security protocols and trust components
- **Params**:
  - `protocol`: filter by security standard
  - `component`: filter by agentic trust element
- **Response**: Sankey diagram data structure

### 7. Language Vitality Risk Overlay

**GET /api/language-vitality-risk**
- **Description**: Retrieve AI deployment risk flags for jurisdictions with low language vitality, using UNESCO metrics and observed translation confidence thresholds.
- **Params**:
   - `jurisdiction` (string, optional): Filter by jurisdiction code (e.g., 'EE' for Estonia). Defaults to global overview.
- **Response**:
   - JSON object containing:
     - `low_vitality_risk` (boolean): True if the primary language of the jurisdiction is classified as Severely Endangered or Critically Endangered.
     - `translation_confidence_floor` (float): Minimum observed translation confidence for edge cases in this jurisdiction (e.g., ≤0.52).
     - `risk_level` (string): Categorical risk assessment: "High", "Medium", or "Low".
   - **Example**:
     {
       "low_vitality_risk": true,
       "translation_confidence_floor": 0.51,
       "risk_level": "High"
     }

## Authentication
- Bearer token in Authorization header
- Token obtained via `/auth/login` (not described here)

## Error Handling
- 400 Bad Request: Malformed requests
- 401 Unauthorized: Missing/invalid token
- 404 Not Found: Endpoint/resource missing
- 500 Server Error: Unexpected failures

## Versioning
- API version specified in Content-Type header
- Current version: `application/vnd.limen.v1+json`

## Linked Artifacts
- Dashboard Spec: [limen-dashboard-spec-v0.1.md](/srv/tyche/projects/limen-ai-edge-case-atlas/dashboard/limen-dashboard-spec-v0.1.md)
- Article Architecture: [article-architecture-v0.1.md](/srv/tyche/projects/limen-ai-edge-case-atlas/papers/article-architecture-v0.1.md)