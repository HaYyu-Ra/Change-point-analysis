import React from 'react';

function Metrics({ metrics }) {
    return (
        <div>
            <h2>Model Performance Metrics</h2>
            <ul>
                <li>RMSE: {metrics.RMSE}</li>
                <li>MAE: {metrics.MAE}</li>
            </ul>
        </div>
    );
}

export default Metrics;
