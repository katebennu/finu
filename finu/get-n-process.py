import pandas as pd
import requests
import json

# income = pd.read_json('aapl_income_statement.json')

# REQUEST ALL THREE STATEMENTS AND SAVE AS ONE FILE

income = json.loads(requests.get('https://api.intrinio.com/financials/reported?identifier=AAPL&statement=income_statement&fiscal_year=2016&fiscal_period=FY', auth=('4ea8ae0d11d482806d10558597cff3f5', '2db2b3521aef5cda7717c5bd9f8cb05b')).text)

bs = json.loads(requests.get('https://api.intrinio.com/financials/reported?identifier=AAPL&statement=balance_sheet&fiscal_year=2016&fiscal_period=FY', auth=('4ea8ae0d11d482806d10558597cff3f5', '2db2b3521aef5cda7717c5bd9f8cb05b')).text)

cf = json.loads(requests.get('https://api.intrinio.com/financials/reported?identifier=AAPL&statement=balance_sheet&fiscal_year=2016&fiscal_period=FY', auth=('4ea8ae0d11d482806d10558597cff3f5', '2db2b3521aef5cda7717c5bd9f8cb05b')).text)

out = {'IS':{}, 'BS':{}, 'CF':{}}

for i in income["data"]:
    out['IS'][i['xbrl_tag']] = i['value']

for i in bs["data"]:
    out['BS'][i['xbrl_tag']] = i['value']

for i in cf["data"]:
    out['CF'][i['xbrl_tag']] = i['value']


fh = open('AAPL_full_2016.json', 'w')

json.dump(out, fh)

fh.close()





