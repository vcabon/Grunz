"""
Change any part of paths in the .json file obtain from MegaDetector.
"""
import json
with open('grunz/output/Results_1p_Periode2_SD2.json') as f:
    data = json.load(f)

for item in data['images']:
    item['file'] = item['file'].replace('/content/drive/My Drive/1p_Periode2_SD2/', '')

with open('Results_1p_Periode2_SD2-2.json', 'w') as f:
    json.dump(data, f)