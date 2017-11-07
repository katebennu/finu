import json

# RATIOS LIST: http://www.cpaclass.com/fsa/ratio-01a.htm


def process_statement(statement):
    data = statement['data']
    ratios = {
        'Liquidity': {},
        'Profitability': {},
        'Activity': {},
        'CapitalStructure': {},
        'CapitalMarket': {},
        'ROA': {}
    }

    ratios['Liquidity']['CurrentRatio'] = data['AssetsCurrent'] / data['LiabilitiesCurrent']
    ratios['Liquidity']['QuickRatio'] = (data['AssetsCurrent'] - data['InventoryNet']) / data['LiabilitiesCurrent']
    ratios['Liquidity']['NetWorkingCapital'] = (data['AssetsCurrent'] - data['LiabilitiesCurrent']) / data['Assets']
    
    ratios['Profitability']['ReturnOnAssets'] = data['NetIncomeLoss'] / data['Assets']
    ratios['Profitability']['ReturnOnEquity'] = data['NetIncomeLoss'] / data['StockholdersEquity']
    # ratios['Profitability']['ReturnOnCommonEequity']
    ratios['Profitability']['ProfitMargin'] = data['NetIncomeLoss'] / data['SalesRevenueNet']
    ratios['Profitability']['EPS'] = data['EarningsPerShareBasic']
    ratios['Profitability']['dilutedEPS'] = data['EarningsPerShareDiluted']
    
    ratios['Activity']['AssetTurnover'] = data['SalesRevenueNet'] / data['Assets']
    ratios['Activity']['ReceivablesTurnover'] = data['SalesRevenueNet'] / data['Assets']
    ratios['Activity']['InventoryTurnover'] = data['CostOfGoodsAndServicesSold'] / data['InventoryNet']
    
    ratios['CapitalStructure']['DebtToEquity'] = data['Liabilities'] / data['StockholdersEquity']
    
    # ratios['CapitalMarket']['PE']
    # ratios['CapitalMarket']['MarketToBook']

    yield {
        'company': statement['company'],
        'year': statement['year'],
        'ratios': ratios
    }


def main():
    print('started creating ratios')
    out = []

    with open('api-data.json', 'r') as jh:
        statements = json.load(jh)

    for s in statements:
        out += list(process_statement(s))

    with open('ratios.json', 'w') as fil:
        json.dump(out, fil)


if __name__ == '__main__':
    main()