import json, os, requests
from django.core.management.base import BaseCommand
from api.models import Industry, Company


class Command(BaseCommand):
    help = 'Add industries to db'

    def handle(self, *args, **options):
        self.run()
        self.stdout.write(self.style.SUCCESS('Successfully added industries to db'))

    def run(self):
        module_dir = os.path.dirname(os.path.abspath(__file__))

        with open(os.path.join(module_dir, "fixtures", 'companies.json'), 'r') as fh:
            companies = json.load(fh)['companies']

        for c in companies:
            print(c)
            company = Company.objects.get(ticker=c['ticker'])
            for i in c['industries']:
                print(i)
                industry, created = Industry.objects.get_or_create(name=i)
                if created:
                    industry.save()
                    print(industry.name, created)
                company.industries.add(industry)
