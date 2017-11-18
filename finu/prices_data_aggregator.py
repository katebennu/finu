import json
import requests

URL_BASE = 'https://api.intrinio.com/prices?identifier='

with open('auth', 'r') as fh:
    AUTH = tuple(fh.read().split(','))


def process_company(company):
    print(company)
    data = {
        'company': company,
        'price': None
    }
    response_data = requests.get(
        URL_BASE + company,
        auth=AUTH,
        params=dict(
            start_date=2017-11-17,
            end_date=2017-11-17
        )
    ).json()
    print(response_data)

    data['price'] = response_data['data'][0]['close']

    yield data


def main():
    print('started')
    out = []

    with open('companies.json') as fh:
        companies = json.load(fh)["companies"]

    for c in companies:
        out += list(process_company(c['ticker']))

    with open('prices-data.json', 'w') as fil:
        json.dump(out, fil)


if __name__ == '__main__':
    main()
