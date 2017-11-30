import json, requests, os
from django.core.management.base import BaseCommand
from api.models import Company


class Command(BaseCommand):
    help = 'Fetch and save prices in the db'

    def handle(self, *args, **options):
        self.run()
        self.stdout.write(self.style.SUCCESS('Successfully fetched and saved prices'))

    def run(self):
        URL_BASE = 'https://api.intrinio.com/financials/reported?identifier='
        YEARS = ['2014', '2015', '2016']
        STATEMENTS = ['income_statement', 'balance_sheet', 'cash_flow_statement']

        module_dir = os.path.dirname(os.path.abspath(__file__))
        with open(os.path.join(module_dir, "fixtures", 'auth'), 'r') as fh:
            AUTH = tuple(fh.read().split(','))

        def process_company(company):
            for y in YEARS:
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
                        requests.put('http://localhost:8000/statement-entry/',
                                     params=dict(
                                         ticker=company,
                                         year=int(y),
                                         name=i['xbrl_tag'],
                                         value=i['value'],
                                         statement=s
                                     ))

        def main():
            print('started')

            companies = Company.objects.all()

            for c in companies:
                print(c.ticker)
                process_company(c.ticker)

        main()
