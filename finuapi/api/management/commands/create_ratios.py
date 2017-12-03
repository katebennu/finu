import json
from django.core.management.base import BaseCommand
from api.models import Company, ReportedEntry, AnalyticEntry


class Command(BaseCommand):
    help = 'Create ratios'

    def handle(self, *args, **options):
        self.run()
        self.stdout.write(self.style.SUCCESS('Successfully created ratios'))

    def run(self):
        YEARS = ['2014', '2015', '2016']

        # RATIOS LIST: http://www.cpaclass.com/fsa/ratio-01a.htm

        def process_report(report, c, y):

            def create_ratio(name, type, value):
                a, created = AnalyticEntry.objects.get_or_create(company=c,
                                                                 year=y,
                                                                 name=name,
                                                                 value=value,
                                                                 type=type)
                if created:
                    print(a.company.ticker, a.name)
                    a.save()

            try:
                create_ratio('CurrentRatio', 'Liquidity', report['AssetsCurrent'] / report['LiabilitiesCurrent'])
                create_ratio('QuickRatio', 'Liquidity',
                             (report['AssetsCurrent'] - report['InventoryNet']) / report['LiabilitiesCurrent'])
                create_ratio('NetWorkingCapital', 'Liquidity', (report['AssetsCurrent'] - report['LiabilitiesCurrent']) / report['Assets'])

                create_ratio('ReturnOnAssets', 'Profitability', report['NetIncomeLoss'] / report['Assets'])
                create_ratio('ReturnOnEquity', 'Profitability', report['NetIncomeLoss'] / report['StockholdersEquity'])
                # create_ratio(['Profitability']['ReturnOnCommonEequity']
                create_ratio('ProfitMargin', 'Profitability', report['NetIncomeLoss'] / report['SalesRevenueNet'])
                create_ratio('EPS', 'Profitability', report['EarningsPerShareBasic'])
                create_ratio('dilutedEPS', 'Profitability', report['EarningsPerShareDiluted'])

                create_ratio('AssetTurnover', 'Activity', report['SalesRevenueNet'] / report['Assets'])
                create_ratio('ReceivablesTurnover', 'Activity', report['SalesRevenueNet'] / report['Assets'])
                create_ratio('InventoryTurnover', 'Activity',
                             report['CostOfGoodsAndServicesSold'] / report['InventoryNet'])

                create_ratio('DebtToEquity', 'CapitalStructure', report['Liabilities'] / report['StockholdersEquity'])

                # ratios['CapitalMarket']['PE']
                # ratios['CapitalMarket']['MarketToBook']
            except:
                pass


        def main():
            companies = Company.objects.all()

            for c in companies:
                for y in YEARS:
                    process_report(c.get_report(y), c, y)

        main()
