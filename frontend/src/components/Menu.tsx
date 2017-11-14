import * as React from 'react';

const Menu = ({companies, onClick}: { companies: Company[], onClick(f: string, type: string): any }) => (
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
                        onClick={() => onClick(company.ticker, 'selectedCompanies')}
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
                        onClick={() => onClick(year, 'selectedYears')}
                >
                    {year}
                </button>))}
        </div>
    </div>
);

export default Menu;