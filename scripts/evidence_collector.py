# Evidence Collector Script with Retry Logic

import requests
import argparse
import os
import json
import time

# Configuration
EPPO_URL = "https://epo.eu/api/procurements"  # Example endpoint
OUTPUT_DIR = "./procurement_contradictions"
MAX_RETRIES = 3
BASE_DELAY = 10  # Seconds

parser = argparse.ArgumentParser(description='Collect public procurement evidence')
parser.add_argument('--target', type=str, required=True, help='Evidence target (public_procurement)')
parser.add_argument('--jurisdiction', type=str, required=True, help='Jurisdiction code (EU/BG/RO/etc.')
parser.add_argument('--output_dir', type=str, required=True, help='Output directory')

def collect_evidence():
    """
    Enhanced evidence collector with retry logic and connection checks
    """
    os.makedirs(args.output_dir, exist_ok=True)

    headers = {
        "User-Agent": "Tyche-Research/1.0",
        "Accept": "application/json"
    }
    params = {
        "jurisdiction": args.jurisdiction,
        "type": "AI-related"
    }

    response = None
    for attempt in range(MAX_RETRIES):
        try:
            print(f"Attempt {attempt + 1}/{MAX_RETRIES}")
            response = requests.get(EPPO_URL, headers=headers, params=params, timeout=30)
            response.raise_for_status()
            break  # Success
        except requests.exceptions.RequestException as e:
            print(f"Attempt {attempt + 1} failed: {str(e)}")
            if attempt < MAX_RETRIES - 1:
                print(f"Retrying in {BASE_DELAY * (attempt + 1)} seconds...")
                time.sleep(BASE_DELAY * (attempt + 1))
            else:
                raise  # Propagate after final attempt

    if response is None:
        print("All retries failed. Check network connectivity to epo.eu")
        return

    # Example processing
    records = response.json().get("records", [])
    for record in records:
        # Extract relevant fields
        case_id = record.get("tender_id")
        jurisdiction = record.get("country")
        requirement = record.get("ai_requirements", {}).get("reliability")
        actual = record.get("vendor_performance")

        # Create evidence entry
        evidence = {
            "source_path": f"{EPPO_URL}?ji={case_id}",
            "access_date": datetime.now(datetime.UTC).isoformat(),
            "jurisdiction": jurisdiction,
            "language": "en",
            "taxonomy_route": "Procurement Contradiction",
            "crosswalk_mapping": "OECD AI Principle 5 (Robustness)",
            "provenance_hash": "mock_hash",  # In real code, compute actual hash
            "content": {
                "case_id": case_id,
                "jurisdiction": jurisdiction,
                "requirement": requirement,
                "actual": actual
            }
        }

        # Save as JSONL
        output_path = os.path.join(args.output_dir, f"{case_id}.jsonl")
        with open(output_path, "w") as f:
            json.dump(evidence, f)
            f.write("\n")

    print(f"Collected {len(records)} procurement records")

if __name__ == "__main__":
    args = parser.parse_args()
    collect_evidence()
