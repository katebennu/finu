import * as React from 'react';

const Menu = ({companies, onClick}: { companies: Company[], onClick(f: string, type: string, event: any): any }) => (
    <div style={{
        border: 'solid 1px',
        marginBottom: '10px'
    }}>
        <div>Menu</div>
        <div>
            {companies.map(company => (
                <button style={{
                            display: 'inline-block',
                            padding: '5px'
                        }}
                        key={company.ticker}
                        onClick={(e) => onClick(company.ticker, 'selectedCompanies', e)}
                >
                    {company.ticker}
                </button>))}
        </div>
        <div style={{
            margin: '20px'
        }}>
            {['2014', '2015', '2016'].map(year => (
                <button style={{
                            display: 'inline-block',
                            padding: '5px'
                        }}
                        key={year}
                        onClick={(e) => onClick(year, 'selectedYears', e)}
                >
                    {year}
                </button>))}
        </div>
    </div>
);

export default Menu;