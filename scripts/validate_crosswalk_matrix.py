#!/usr/bin/env python3

import pandas as pd

def validate_crosswalk_matrix():
    """
    Validates the crosswalk coverage matrix against source ledger
    """
    try:
        # Load matrices
        crosswalk = pd.read_csv('/srv/tyche/projects/limen-ai-edge-case-atlas/results/boost/limen-boost-003/source-crosswalk-v0.1.tsv', sep='\t')
        ledger = pd.read_csv('/srv/tyche/projects/limen-ai-edge-case-atlas/sources/sources.md', sep='\t')
        
        # Basic checks
        if 'source_id' in crosswalk.columns and 'source_id' in ledger.columns:
            missing_sources = set(ledger['source_id']) - set(crosswalk['source_id'])
            if missing_sources:
                print(f"ERROR: Missing sources in crosswalk: {missing_sources}")
                return False
            
            # Check coverage fields
            required_fields = ['evidence_tier', 'jurisdiction', 'language', 'source_family']
            for field in required_fields:
                if field not in crosswalk.columns:
                    print(f"ERROR: Missing required field '{field}' in crosswalk")
                    return False
            
            print('SUCCESS: Basic validation passed')
            return True
        else:
            print('ERROR: source_id missing in one of the files')
            return False
    except Exception as e:
        print(f'ERROR: Validation failed - {str(e)}')
        return False

if __name__ == '__main__':
    success = validate_crosswalk_matrix()
    if success:
        print('VALIDATION PASSED')
    else:
        print('VALIDATION FAILED')