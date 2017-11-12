import * as React from 'react';
import * as ReactDOM from 'react-dom';
import App from './App';
// import getRates from './utils/fetchRates';

async function init() {
    // const data = await getRates();
    ReactDOM.render(<App />, document.getElementById('root'));
}

init();