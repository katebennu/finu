type Company = {
    'ticker': string,
    'name': string,
    'industries': string[]
}
type Ratios = {
    Liquidity: Liquidity,
    Profitability: Profitability,
    CapitalStructure: CapitalStructure
}
type Liquidity = {
    CurrentRatio: number,
    QuickRatio: number,
    NetWorkingCapital: number
}
type Profitability = {
    ReturnOnAssets: number,
    ReturnOnEquity: number
}
type CapitalStructure = {
    DebtToEquity: number
}
type StatementRatios = {
    company: string,
    year: string,
    ratios: Ratios
}