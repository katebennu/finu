import json
import requests

URL_BASE = 'https://api.intrinio.com/prices?identifier='

with open('auth', 'r') as fh:
    AUTH = tuple(fh.read().split(','))


def process_company(company):
    print(company)

    response_data = requests.get(
        URL_BASE + company,
        auth=AUTH,
        params=dict(
            start_date=2017-11-17,
            end_date=2017-11-17
        )
    ).json()
    print(response_data)

    return response_data['data'][0]['close']


def main():
    print('started')
    out = []

    with open('json-data/companies.json') as fh:
        companies = json.load(fh)["companies"]

    for c in companies:
        print(process_company(c['ticker']))
        requests.post('c['ticker'], float(process_company(c['ticker'])))


if __name__ == '__main__':
    main()

