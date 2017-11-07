import requests
import json
import json

import requests

URL_BASE = 'https://api.intrinio.com/financials/reported?identifier='
YEARS = ['2014', '2015', '2016']
STATEMENTS = ['income_statement', 'balance_sheet', 'cash_flow_statement']

with open('auth', 'r') as fh:
    AUTH = tuple(fh.read().split(','))


def process_company(company, industry):
    for y in YEARS:
        for s in STATEMENTS:
            """
            url = "&".join([
                URL_BASE + company,
                'state',
                'statement={}'.format(s),
                'fiscal_year={}'.format(y),
                'fiscal_period=FY'
            ])
            """
            statement_data = requests.get(
                URL_BASE + company,
                auth=AUTH,
                params=dict(
                    state="true",
                    statement=s,
                    fiscal_year=y,
                    fiscal_period="FY"
                )
            ).json()

            data = {
                'industry': industry,
                'company': company,
                'year': y,
                'data': {}
            }

            for i in statement_data["data"]:
                data['data'][i['xbrl_tag']] = i['value']

            yield data


def main():
    print('started')
    out = []

    with open('by-industry.json') as fh:
        industries = json.load(fh)["industries"]

    for i in industries:
        for c in i["companies"]:
            out += list(process_company(c['ticker'], i['name']))

    with open('api-data.json', 'w') as fil:
        json.dump(out, fil)


if __name__ == '__main__':
    main()




# Define Class Company.
# Add methods for 1) Data update 2) Ratios calculation

# ??? Should all data be attributes of a company Class, attributes of a
# statement Class or smth else??? How about ratios?
