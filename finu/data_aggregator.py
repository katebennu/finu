import requests
import json
import json

import requests

URL_BASE = 'https://api.intrinio.com/financials/reported?identifier='
YEARS = ['2014', '2015', '2016']
STATEMENTS = ['income_statement', 'balance_sheet', 'cash_flow_statement']
AUTH = ('4ea8ae0d11d482806d10558597cff3f5', '2db2b3521aef5cda7717c5bd9f8cb05b')


def process_company(company):
    for y in YEARS:
        for s in STATEMENTS:
            url = "&".join([
                URL_BASE + company['ticker'],
                'state',
                'statement={}'.format(s),
                'fiscal_year={}'.format(y),
                'fiscal_period=FY'
            ])
            statement_data = json.loads(requests.get(url, auth=AUTH).text)
            data = {}

            for i in statement_data["data"]:
                data[i['xbrl_tag']] = i['value']

            yield data


def main():

    out = {}

    with open('by-industry.json') as fh:
        industries = json.load(fh)["industries"]

    for i in industries:
        for c in i["companies"]:
            out[c['ticker']] = list(process_company(c))

    with open('api-data.json', 'w') as fil:
        json.dump(out, fil)

if __name__ == 'main':
    main()




# Define Class Company.
# Add methods for 1) Data update 2) Ratios calculation

# ??? Should all data be attributes of a company Class, attributes of a
# statement Class or smth else??? How about ratios?
