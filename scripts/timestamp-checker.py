# Timestamp Checker Script

import os
import json
import datetime

def check_timestamp(file_path):
    # Get file modification time
    mod_time = os.path.getmtime(file_path)
    mod_datetime = datetime.datetime.fromtimestamp(mod_time)
    
    # Load JSON data
    with open(file_path, 'r') as f:
        data = json.load(f)
    
    # Generate report
    report = {
        'file_path': file_path,
        'modification_time': mod_datetime.isoformat(),
        'data_freshness_seconds': (datetime.datetime.now().timestamp() - mod_time),
        'data_size': len(data),
        'last_updated': mod_datetime.strftime('%Y-%m-%d %H:%M:%S')
    }
    
    return report

if __name__ == '__main__':
    import sys
    if len(sys.argv) != 2:
        print('Usage: python timestamp-checker.py <file_path>')
        sys.exit(1)
    
    file_path = sys.argv[1]
    result = check_timestamp(file_path)
    print(json.dumps(result, indent=2))