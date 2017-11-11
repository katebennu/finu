import * as React from 'react';

const App = ({data}: {data: object}) => (
    <div className="App">
        <header className="App-header">
            <h1 className="App-title">Welcome to React</h1>
        </header>
        <p className="App-intro">
            {JSON.stringify(data)}
        </p>
    </div>
);

export default App;