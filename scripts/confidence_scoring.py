import json
import sys

def score_cases(input_path, output_path, translation_threshold=0.7):
    with open(input_path, 'r') as infile:
        cases = [json.loads(line) for line in infile]
    
    # Example scoring logic (replace with actual implementation)
    for case in cases:
        case['confidence_score'] = (case['translation_confidence'] * 0.6) + (case['authority_score'] * 0.4)
        case['tier'] = 'Tier 1' if case['confidence_score'] >= 0.8 else 'Tier 2'
    
    with open(output_path, 'w') as outfile:
        for case in cases:
            outfile.write(json.dumps(case) + '\n')

if __name__ == '__main__':
    score_cases(
        input_path=sys.argv[1],
        output_path=sys.argv[2],
        translation_threshold=float(sys.argv[3]) if len(sys.argv) > 3 else 0.7
    )