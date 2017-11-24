import json

with open('../json-data/companies.json', 'r') as fh:
    companies = json.load(fh)['companies']

for c in companies:
