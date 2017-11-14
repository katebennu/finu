import * as React from 'react';

const Menu = ({companies, onClick}: { companies: Company[], onClick(c: string): any }) => (
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
                        onClick={() => onClick(company.ticker)}
                >
                    {company.ticker}
                </button>))}
        </div>
    </div>
);

export default Menu;