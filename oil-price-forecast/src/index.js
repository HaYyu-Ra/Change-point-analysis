// src/index.js
import React from 'react';
import ReactDOM from 'react-dom';
import App from './App'; // <-- Correct import of the default export

ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById('root')
);
