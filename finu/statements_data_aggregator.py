import json
import requests

URL_BASE = 'https://api.intrinio.com/financials/reported?identifier='
YEARS = ['2014', '2015', '2016']
STATEMENTS = ['income_statement', 'balance_sheet', 'cash_flow_statement']

with open('auth', 'r') as fh:
    AUTH = tuple(fh.read().split(','))


def process_company(company):
    for y in YEARS:
        data = {
            'company': company,
            'year': int(y),
            'data': {}
        }
        for s in STATEMENTS:
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

            for i in statement_data["data"]:
                data['data'][i['xbrl_tag']] = i['value']

        yield data


def main():
    print('started')
    out = []

    with open('companies.json') as fh:
        companies = json.load(fh)["companies"]

    for c in companies:
        out += list(process_company(c['ticker']))

    with open('api-data.json', 'w') as fil:
        json.dump(out, fil)


if __name__ == '__main__':
    main()




# Define Class Company.
# Add methods for 1) Data update 2) Ratios calculation

# ??? Should all data be attributes of a company Class, attributes of a
# statement Class or smth else??? How about ratios?
