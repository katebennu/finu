import json, os, requests
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Add companies to db'

    def handle(self, *args, **options):
        self.run()
        self.stdout.write(self.style.SUCCESS('Successfully added companies to db'))

    def run(self):
        module_dir = os.path.dirname(os.path.abspath(__file__))

        with open(os.path.join(module_dir, "fixtures", 'companies.json'), 'r') as fh:
            companies = json.load(fh)['companies']

        for c in companies:
            print(c)
            r = requests.put('http://localhost:8000/company/',
                             params=dict(
                                 ticker=c['ticker'],
                                 name=str(c['name'])
                             )
                         )
            print(c['ticker'], r.status_code)
