import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';

import getRates from './fetchRates';

const data = getRates();
data.then((value) => {
    ReactDOM.render(<App data={value} />, document.getElementById('root'));
});
