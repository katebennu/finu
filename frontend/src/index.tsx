import * as React from 'react';
import * as ReactDOM from 'react-dom';
import App from './App';
import fetchData from './utils/fetchData';

async function init() {
    const data = await fetchData('/all-companies/');
    ReactDOM.render(<App companies={data.companies}/>, document.getElementById('root'));
}

init();