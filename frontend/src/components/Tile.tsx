import * as React from 'react';

const RatiosSubGroup = ({title, items}: { title: string, items: object }) => (
    <div style={{
            border: 'solid 1px gray'
        }}>
        <b>{title}</b>
        <ul>
            {Object.keys(items).map((item: string) => (
                    <li>{item}: {items[item].toFixed(2)}</li>
                )
            )}
        </ul>
    </div>
);


const Tile = ({value}: { value: StatementRatios }) => (
    <div style={{
        display: 'inline-block',
        width: '30%',
        minWidth: '200px',
        maxWidth: '300px',
        margin: '10px',
        border: 'solid 2px black'
    }}>
        <div>{value.company} {value.year}</div>

        <div>
            {Object.keys(value.ratios).map((ratio: string) =>
                <RatiosSubGroup title={ratio} items={value.ratios[ratio]}/>
            )}
        </div>
    </div>
);

export default Tile;