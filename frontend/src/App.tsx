import * as React from 'react';

type Data = {
    company: string,
    year: string,
    ratios: Ratios
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

const Tile = ({value}: { value: Data}) => (
    <div style={{
        display: 'inline-block',
        width: '30%',
        minWidth: '200px',
        maxWidth: '300px',
        margin: '10px'
    }}>
        <div>{value.company} {value.year}</div>
        <div>Liquidity:
            <div>Current Ratio: {JSON.stringify(value.ratios.Liquidity.CurrentRatio)}</div>
        </div>
        <div>CapitalStructure:
            <div>Debt to Equity: {value.ratios.CapitalStructure.DebtToEquity}</div>
        </div>

    </div>

);

const App = ({data}: {data: Data[]}) => (
    <div style={{
        textAlign: 'center',
        width: '100%',
        maxWidth: '900px'
    }}>
        <div>
            {/*{JSON.stringify(data)}*/}
            {data.map(statement => <Tile key={statement.company} value={statement}/>)}
        </div>
    </div>
);

export default App;