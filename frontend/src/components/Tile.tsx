import * as React from 'react';

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

export default Tile;