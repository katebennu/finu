import * as React from 'react';

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

export default Menu;