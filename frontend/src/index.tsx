import * as React from 'react';
import * as ReactDOM from 'react-dom';
import App from './App';
import fetchData from './utils/fetchData';

async function init() {
    const data = await fetchData();
    ReactDOM.render(<App companies={data}/>, document.getElementById('root'));
}

init();