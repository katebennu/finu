import * as React from 'react';
import Tile from './Tile'

const Tiles = ({data}: {data: StatementRatios[]}) => (
    <div style={{
        border: 'solid 1px'
    }}>
        {data.map(statement => <Tile key={statement.company} value={statement}/>)}
    </div>
);

export default Tiles;