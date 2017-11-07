import pandas as pd
import json

jf = pd.read_json('AAPL_full_2016.json')

# select Income Statement and drop NaN from the table
# i_s = pd.DataFrame(jf['IS']).dropna()

# RATIOS LIST: http://www.cpaclass.com/fsa/ratio-01a.htm

ratios = {
    'Liquidity': {},
    'Profitability': {},
    'Activity': {},
    'CapitalStructure': {},
    'CapitalMarket': {},
    'ROA': {}
}

b_s = jf['BS']
i_s = jf['IS']
c_f = jf['CF']

ratios['Liquidity']['CurrentRatio'] = b_s['AssetsCurrent'] / b_s['LiabilitiesCurrent']
ratios['Liquidity']['QuickRatio'] = (b_s['AssetsCurrent'] - b_s['InventoryNet']) / b_s['LiabilitiesCurrent']
ratios['Liquidity']['NetWorkingCapital'] = (b_s['AssetsCurrent'] - b_s['LiabilitiesCurrent']) / b_s['Assets']

ratios['Profitability']['ReturnOnAssets'] = i_s['NetIncomeLoss'] / b_s['Assets']
ratios['Profitability']['ReturnOnEquity'] = i_s['NetIncomeLoss'] / b_s['StockholdersEquity']
# ratios['Profitability']['ReturnOnCommonEequity']
ratios['Profitability']['ProfitMargin'] = i_s['NetIncomeLoss'] / i_s['SalesRevenueNet']
ratios['Profitability']['EPS'] = i_s['EarningsPerShareBasic']
ratios['Profitability']['dilutedEPS'] = i_s['EarningsPerShareDiluted']

ratios['Activity']['AssetTurnover'] = i_s['SalesRevenueNet'] / b_s['Assets']
ratios['Activity']['ReceivablesTurnover'] = i_s['SalesRevenueNet'] / b_s['Assets']
ratios['Activity']['InventoryTurnover'] = i_s['CostOfGoodsAndServicesSold'] / b_s['InventoryNet']

ratios['CapitalStructure']['DebtToEquity'] = b_s['Liabilities'] / b_s['StockholdersEquity']

# ratios['CapitalMarket']['PE']
# ratios['CapitalMarket']['MarketToBook']

print(ratios)

fh = open('AAPL_ratios.json', 'w')
json.dump(ratios, fh)
