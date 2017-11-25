import json, requests


def main():
    with open('../json-data/companies.json', 'r') as fh:
        companies = json.load(fh)['companies']

    for c in companies:
        print(c)
        r = requests.put('http://localhost:5000/company/',
                         params=dict(
                             ticker=c['ticker'],
                             name=str(c['name'])
                         )
                     )
        print(c['ticker'], r.status_code)


if __name__ == '__main__':
    main()