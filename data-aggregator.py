import pandas as pd
import requests
import json


years = ['2014', '2015', '2016']
statements = ['income_statement', 'balance_sheet', 'cash_flow_statement']
auth=('4ea8ae0d11d482806d10558597cff3f5', '2db2b3521aef5cda7717c5bd9f8cb05b')
url_base = 'https://api.intrinio.com/financials/reported?identifier='
out = {}


with open('by-industry.json') as fh:
    industries = json.load(fh)["industries"]

for i in industries:
    for c in i["companies"]:
        for y in years:
            for s in statements:
                url = url_base + c['ticker'] + '&state&statement=' + s + '&fiscal_year=' + y + '&fiscal_period=FY'
                statement_data = json.loads(requests.get(url, auth=auth).text)
                out[s] = {}

                for i in statement_data["data"]:
                    out[s][i['xbrl_tag']] = i['value']

                data_file_path = 'api-data/' + c["ticker"] + '_full_' + y
                fh = open(data_file_path, 'w')

                json.dump(out, fh)

                fh.close()




# Define Class Company.
# Add methods for 1) Data update 2) Ratios calculation

# ??? Should all data be attributes of a company Class, attributes of a
    # statement Class or smth else??? How about ratios?







