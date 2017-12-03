import * as React from 'react';
import CompanyTile from './CompanyTile'


const Tiles = ({selectedCompanies, selectedYears}: {selectedCompanies: Company[], selectedYears: string[]}) => (
    <div style={{
        border: 'solid 1px'
    }}>
        {selectedCompanies.map(company => <CompanyTile key={company.ticker} company={company} selectedYears={selectedYears}/>)}
    </div>
);

export default Tiles;