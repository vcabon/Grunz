"""
Change any part of paths in the .json file obtain from MegaDetector.
"""
import json
with open('grunz/output/20201028-2255.json') as f:
    data = json.load(f)

for item in data['images']:
    item['file'] = item['file'].replace('/content/drive/My Drive/1p_Periode3_SD2/', '')

with open('20201028-2255-2.json', 'w') as f:
    json.dump(data, f)