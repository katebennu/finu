import json
import requests
from datetime import date


URL_BASE = 'https://api.intrinio.com/prices?identifier='

with open('auth', 'r') as fh:
    AUTH = tuple(fh.read().split(','))


def process_company(company):
    print(company)

    t = date.today()
    today_str = str(t.year) + '-' + str(t.month) + '-' + str(t.day - 1)

    print(today_str)

    response_data = requests.get(
        URL_BASE + company,
        auth=AUTH,
        params=dict(
            start_date=today_str,
            end_date=today_str
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
        requests.put('http://localhost:5000/set-price/',
                     params=dict(
                         ticker=c['ticker'],
                         price=float(process_company(c['ticker']))
                     ))


if __name__ == '__main__':
    main()
