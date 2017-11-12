import * as React from 'react';
import { connect, PromiseState } from 'react-refetch';

type Fetched = [
    {'data': StatementRatios[]},
    {'companies': Company[]}
]
type Company = {
    'ticker': string,
    'industries': string[]
}
type StatementRatios = {
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

const Tile = ({value}: { value: StatementRatios}) => (
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

const Tiles = ({data}: {data: StatementRatios[]}) => (
    <div style={{
        border: 'solid 1px'
    }}>
        {data.map(statement => <Tile key={statement.company} value={statement}/>)}
    </div>
);

// const FilterButtonIndustry =

const Menu = ({companies} : {companies: Company[]}) => (
    <div style={{
        border: 'solid 1px',
        marginBottom: '10px'
    }}>
        <div>Menu</div>
        <div>
            {companies.map(company => (
                <div style={{
                    display: 'inline-block',
                    padding: '5px'
                    }} key={company.ticker}>
                    {company.ticker}
                </div>))}
        </div>
    </div>
);

const App = ({fetched}: {fetched: Fetched}) => (
    <div style={{
        textAlign: 'center',
        width: '100%',
        maxWidth: '900px'
    }}>
        <div>
            {/*{JSON.stringify(fetched)}*/}
            <Menu companies={fetched[1].companies}/>
            <Tiles data={fetched[0].data}/>
        </div>
    </div>
);

const LoadableApp = ({dataFetch, companiesFetch}: {
    dataFetch: PromiseState<Fetched[0]>,
    companiesFetch: PromiseState<Fetched[1]>
}) => {
    const allFetches = PromiseState.all([dataFetch, companiesFetch]);
    if (allFetches.rejected) {
        return <p>{allFetches.reason}</p>
    } else if (allFetches.pending) {
        return <p>Loading...</p>
    } else {
        return <App fetched={allFetches.value} />
    }
}

export default connect(() => ({
    dataFetch: 'http://localhost:5000/all-rates/',
    companiesFetch: 'http://localhost:5000/companies/'
}))(LoadableApp);