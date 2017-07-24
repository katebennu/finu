import pandas as pd
import requests
import json


# data = pd.read_json('aapl_income_statement.json')

income = json.loads(requests.get('https://api.intrinio.com/financials/reported?identifier=AAPL&statement=income_statement&fiscal_year=2016&fiscal_period=FY', auth=('4ea8ae0d11d482806d10558597cff3f5', '2db2b3521aef5cda7717c5bd9f8cb05b')).text)

out = {}

for i in income["data"]:
    out[i['xbrl_tag']] = i['value']


#print(out)

# REQUEST ALL THREE STATEMENTS AND SAVE AS ONE FILE


