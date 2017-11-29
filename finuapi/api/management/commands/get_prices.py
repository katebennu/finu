import os
import requests
from django.core.management.base import BaseCommand
from api.models import Company


class Command(BaseCommand):
    help = 'Fetch and save prices in the db'

    def handle(self, *args, **options):
        self.run()
        self.stdout.write(self.style.SUCCESS('Successfully fetched and saved prices'))

    def run(self):
        module_dir = os.path.dirname(os.path.abspath(__file__))
        URL_BASE = 'https://api.intrinio.com/prices?identifier='

        with open(os.path.join(module_dir, "fixtures", 'auth'), 'r') as fh:
            AUTH = tuple(fh.read().split(','))

        def process_company(company):
            print(company)

            response_data = requests.get(
                URL_BASE + company,
                auth=AUTH
            ).json()

            return response_data['data'][0]['close']

        def main():
            print('started')

            companies = Company.objects.all()

            for c in companies:
                requests.put('http://localhost:8000/price/',
                             params=dict(
                                 ticker=c.ticker,
                                 price=float(process_company(c.ticker))
                             ))
        main()
