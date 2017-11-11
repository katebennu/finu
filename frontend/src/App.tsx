import * as React from 'react';

type Rates = {
    company: string,
    year: string
}

const Tile = ({value}: { value: Rates}) => (
    <div>{value.company} {value.year}</div>
);

const App = ({data}: {data: Rates[]}) => (
    <div className="App">
        <header className="App-header">
            <h1 className="App-title">Welcome to React</h1>
        </header>
        <p className="App-intro">
            {/*{JSON.stringify(data)}*/}
            {data.map(statement => <Tile key={statement.company} value={statement}/>)}
        </p>
    </div>
);

export default App;