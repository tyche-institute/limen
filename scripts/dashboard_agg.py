import csv, json, os, re
from collections import Counter, defaultdict

# Paths
SOURCE_LEDGER_PATH = "/srv/tyche/projects/limen-ai-edge-case-atlas/sources/source-family-ledger.tsv"
CLAIM_MATRIX_PATH = "/srv/tyche/projects/limen-ai-edge-case-atlas/claims/claim-support-matrix.tsv"
LANGUAGE_COVERAGE_PATH = "/srv/tyche/projects/limen-ai-edge-case-atlas/sources/language_coverage_baltic_finno_ugric.tsv"
UNCERTAINTY_MATRIX_PATH = "/srv/tyche/projects/limen-ai-edge-case-atlas/results/dashboard/legal-uncertainty-matrix.tsv"
API_DIR = "/srv/tyche/projects/limen-ai-edge-case-atlas/api/dashboard"

# Ensure output directory exists
os.makedirs(API_DIR, exist_ok=True)

# ---------- 1. Source-Family Saturation Map bubble data ----------
bubble_data = []
with open(SOURCE_LEDGER_PATH, newline='') as f:
    reader = csv.DictReader(f, delimiter='\t')
    for row in reader:
        domain = row["source_family"]
        region = row["language_jurisdiction_scope"]
        size_text = row["saturation_metric"] or ""
        # Extract numeric part for size if present
        size_num_match = re.search(r'\d+', size_text)
        size_val = int(size_num_match.group(0)) if size_num_match else 0
        bubble_data.append({
            "id": row["source_family"],
            "domain": domain,
            "region": region,
            "size": size_val,
            "size_text": size_text,
            "authority": row["authority"],
            "access_method": row["access_method"]
        })

# ---------- 2. Evidence‑Tier Funnel data ----------
# Count raw sources
with open(SOURCE_LEDGER_PATH, newline='') as f:
    raw_source_count = sum(1 for _ in f) - 1  # subtract header line

# Count validated evidence (claims with any evidence_tier)
claim_tier_counts = Counter()
with open(CLAIM_MATRIX_PATH, newline='') as f:
    reader = csv.DictReader(f, delimiter='\t')
    for row in reader:
        claim_tier_counts[row["evidence_tier"]] += 1
validated_evidence_count = sum(claim_tier_counts.values())

# Count claim-support entries (non‑empty source_ids)
claim_support_count = sum(1 for row in csv.DictReader(open(CLAIM_MATRIX_PATH, newline=''), delimiter='\t') if row["source_ids"].strip())

# Count publication‑ready claims (non‑empty mapping_to_frameworks)
publication_ready_count = sum(1 for row in csv.DictReader(open(CLAIM_MATRIX_PATH, newline=''), delimiter='\t') if row["mapping_to_frameworks"].strip())

# Compute drop‑off percentages
drop_offs = {
    "Raw_to_Validated": round((raw_source_count - validated_evidence_count) / raw_source_count * 100, 1) if raw_source_count else 0,
    "Validated_to_ClaimSupport": round((validated_evidence_count - claim_support_count) / validated_evidence_count * 100, 1) if validated_evidence_count else 0,
    "ClaimSupport_to_Publication": round((claim_support_count - publication_ready_count) / claim_support_count * 100, 1) if claim_support_count else 0
}
funnel_data = {
    "steps": [
        {"name": "Raw Sources", "count": raw_source_count},
        {"name": "Validated Evidence", "count": validated_evidence_count},
        {"name": "Claim‑Support", "count": claim_support_count},
        {"name": "Publication Ready", "count": publication_ready_count}
    ],
    "drop_offs": drop_offs
}

# ---------- 3. Jurisdiction/Language Coverage heatmap ----------
heatmap_data = {}
with open(LANGUAGE_COVERAGE_PATH, newline='') as f:
    reader = csv.DictReader(f, delimiter='\t')
    for row in reader:
        jurisdiction = row["Jurisdiction"]
        language = row["Language"]
        heatmap_data.setdefault(jurisdiction, {})[language] = {
            "source_count": int(row["Source_Count"]),
            "coverage_status": row["Coverage_Status"]
        }

# ---------- 4. Legal‑Uncertainty Matrix data ----------
uncertainty_matrix_data = []
with open(UNCERTAINTY_MATRIX_PATH, newline='') as f:
    reader = csv.DictReader(f, delimiter='\t')
    for row in reader:
        uncertainty_matrix_data.append({
            "category_code": row["category_code"],
            "category_label": row["category_label"],
            "seed_case_count": int(row["seed_case_count"]),
            "review_priority": row["review_priority"],
            "minimum_stronger_source_needed": row["minimum_stronger_source_needed"],
            "why_public_evidence_is_insufficient": row["why_public_evidence_is_insufficient"],
            "legal_conclusion_limit": row["legal_conclusion_limit"],
            "observatory_hook": row.get("observatory_hook", "")
        })

# ---------- 5. Crosswalk table (claim → frameworks) ----------
crosswalk_table_data = []
with open(CLAIM_MATRIX_PATH, newline='') as f:
    reader = csv.DictReader(f, delimiter='\t')
    for row in reader:
        crosswalk_table_data.append({
            "claim_id": row["claim_id"],
            "frameworks": row["mapping_to_frameworks"].split(";") if row["mapping_to_frameworks"] else []
        })

# ---------- Write aggregated JSON ----------
aggregated = {
    "bubble_data": bubble_data,
    "funnel_data": funnel_data,
    "heatmap_data": heatmap_data,
    "uncertainty_matrix_data": uncertainty_matrix_data,
    "crosswalk_table_data": crosswalk_table_data
}
with open(os.path.join(API_DIR, "aggregates.json"), "w") as f:
    json.dump(aggregated, f, indent=2)

print("Dashboard aggregates written to", API_DIR)