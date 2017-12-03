import * as React from 'react';
import CompanyTile from './CompanyTile'


const Tiles = ({
                   selectedCompanies,
                   selectedYears,
                   selectedIndustries
               }: {
    selectedCompanies: Company[],
    selectedYears: string[],
    selectedIndustries: string[]
},) => (
    <div style={{
        border: 'solid 1px'
    }}>
        {selectedCompanies.filter(company => company.industries.some(i => selectedIndustries.indexOf(i) > -1))
            .map(company => <CompanyTile key={company.ticker} company={company}
                                         selectedYears={selectedYears}/>)}
    </div>
);

export default Tiles;