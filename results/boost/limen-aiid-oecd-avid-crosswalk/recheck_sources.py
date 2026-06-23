import json, re, urllib.request

checks = {}

def fetch(url, limit=2500000):
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 Hermes/1.0'})
    with urllib.request.urlopen(req, timeout=30) as r:
        data = r.read(limit)
        return data, r.headers.get('Content-Type', ''), dict(r.headers)

# AIID
aiid = {}
data, _, _ = fetch('https://incidentdatabase.ai/page-data/cite/1515/page-data.json')
obj = json.loads(data)
aiid['incident_id'] = obj['result']['data']['incident']['incident_id']
aiid['title_present'] = bool(obj['result']['data']['incident'].get('title'))
aiid['taxa_nodes'] = len(obj['result']['data'].get('allMongodbAiidprodTaxa', {}).get('nodes', []))
aiid['class_nodes'] = len(obj['result']['data'].get('allMongodbAiidprodClassifications', {}).get('nodes', []))
aiid['first_namespace'] = obj['result']['data']['allMongodbAiidprodTaxa']['nodes'][0]['namespace'] if aiid['taxa_nodes'] else None
checks['aiid'] = aiid

# OECD detail + vocab
oecd = {}
data, _, _ = fetch('https://incidents-server.oecdai.org/api/v1/incidents/2026-06-06-be52')
obj = json.loads(data)
oecd['id'] = obj.get('id')
oecd['title_present'] = bool(obj.get('title'))
oecd['publisher'] = (obj.get('articles') or [{}])[0].get('publisher')
for name in ['countries', 'languages', 'concepts', 'property-values']:
    data2, _, _ = fetch(f'https://incidents-server.oecdai.org/api/v1/incidents/get-{name}')
    obj2 = json.loads(data2)
    oecd[name.replace('-', '_') + '_count'] = len(obj2)
idx, _, _ = fetch('https://oecd.ai/en/incidents', limit=400000)
html = idx.decode('utf-8', 'ignore')
oecd['rights_footer_seen'] = 'All rights reserved' in html
oecd['sample_slug_seen'] = '2026-06-06-be52' in html
oecd['sample_slug_count_in_html'] = len(set(re.findall(r'/en/incidents/[^"\']+', html)))
checks['oecd_aim_incidents'] = oecd

# AVID
avid = {}
data, _, _ = fetch('https://raw.githubusercontent.com/avidml/avid-db/main/reports/2022/AVID-2022-R0001.json')
obj = json.loads(data)
avid['report_id'] = obj['metadata']['report_id']
avid['metric_name'] = obj['metrics'][0]['name']
avid['vuln_id'] = obj['impact']['avid']['vuln_id']
license_text, _, _ = fetch('https://raw.githubusercontent.com/avidml/avid-db/main/LICENSE', limit=20000)
avid['mit_license_seen'] = 'MIT License' in license_text.decode('utf-8', 'ignore')
checks['avid'] = avid

# MIT AI Risk
mitrisk = {}
data, _, _ = fetch('https://airisk.mit.edu/risks', limit=400000)
html = data.decode('utf-8', 'ignore')
mitrisk['cc_by_seen'] = 'creativecommons.org/licenses/by/4.0/' in html
mitrisk['google_sheets_seen'] = 'Google Sheets' in html
mitrisk['onedrive_seen'] = 'OneDrive' in html
mitrisk['domain_anchor_1_seen'] = ('Discrimination &amp; Toxicity' in html) or ('Discrimination & Toxicity' in html)
checks['mit_ai_risk_repo'] = mitrisk

# CSET
cset = {}
data, _, _ = fetch('https://cset.georgetown.edu/article/understanding-ai-harms-an-overview/', limit=250000)
html = data.decode('utf-8', 'ignore')
cset['title_seen'] = 'Understanding AI Harms: An Overview' in html
cset['creative_commons_seen'] = 'creativecommons.org' in html.lower()
checks['cset_ai_harm'] = cset

# MITRE ATLAS
atlas = {}
data, _, _ = fetch('https://raw.githubusercontent.com/mitre-atlas/atlas-data/main/dist/ATLAS.yaml', limit=1200000)
text = data.decode('utf-8', 'ignore')
atlas['deprecation_banner_seen'] = 'no longer being updated with new content' in text
m = re.search(r'^version:\s*"?([0-9.]+)"?', text, re.M)
atlas['version'] = m.group(1) if m else None
atlas['case_study_ids'] = len(set(re.findall(r'AML\.CS\d+', text)))
atlas['technique_ids_top_level'] = len(set(re.findall(r'AML\.T\d{4}(?!\.)', text)))
atlas['technique_ids_total'] = len(set(re.findall(r'AML\.T\d+(?:\.\d+)?', text)))
atlas['mitigation_ids'] = len(set(re.findall(r'AML\.M\d+', text)))
license_text, _, _ = fetch('https://raw.githubusercontent.com/mitre-atlas/atlas-data/main/LICENSE', limit=40000)
atlas['apache_2_seen'] = 'Apache License, Version 2.0' in license_text.decode('utf-8', 'ignore')
checks['mitre_atlas'] = atlas

print(json.dumps(checks, ensure_ascii=False, indent=2))
