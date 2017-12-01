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
                create_ratio('QuickRatio', 'Liquidity', (report['AssetsCurrent'] - report['InventoryNet']) / report['LiabilitiesCurrent'])
            except:
                pass




            #
            # ratios['Liquidity']['QuickRatio'] = (b_s['AssetsCurrent'] - b_s['InventoryNet']) / b_s['LiabilitiesCurrent']
            # ratios['Liquidity']['NetWorkingCapital'] = (b_s['AssetsCurrent'] - b_s['LiabilitiesCurrent']) / b_s['Assets']
            #
            # ratios['Profitability']['ReturnOnAssets'] = i_s['NetIncomeLoss'] / b_s['Assets']
            # ratios['Profitability']['ReturnOnEquity'] = i_s['NetIncomeLoss'] / b_s['StockholdersEquity']
            # # ratios['Profitability']['ReturnOnCommonEequity']
            # ratios['Profitability']['ProfitMargin'] = i_s['NetIncomeLoss'] / i_s['SalesRevenueNet']
            # ratios['Profitability']['EPS'] = i_s['EarningsPerShareBasic']
            # ratios['Profitability']['dilutedEPS'] = i_s['EarningsPerShareDiluted']
            #
            # ratios['Activity']['AssetTurnover'] = i_s['SalesRevenueNet'] / b_s['Assets']
            # ratios['Activity']['ReceivablesTurnover'] = i_s['SalesRevenueNet'] / b_s['Assets']
            # ratios['Activity']['InventoryTurnover'] = i_s['CostOfGoodsAndServicesSold'] / b_s['InventoryNet']
            #
            # ratios['CapitalStructure']['DebtToEquity'] = b_s['Liabilities'] / b_s['StockholdersEquity']
            #
            # # ratios['CapitalMarket']['PE']
            # # ratios['CapitalMarket']['MarketToBook']
            #
            # print(ratios)
            #

        def main():
            companies = Company.objects.all()

            for c in companies:
                for y in YEARS:
                    process_report(c.get_report(y), c, y)

        main()
