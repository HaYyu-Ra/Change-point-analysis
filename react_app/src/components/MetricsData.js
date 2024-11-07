// src/components/MetricsData.js
import React from 'react';

function MetricsData({ metricsData }) {
    return (
        <div>
            <h2>Model Metrics</h2>
            {metricsData && metricsData.MAE ? (
                <div>
                    <p><strong>MAE:</strong> {metricsData.MAE.toFixed(3)}</p>
                    <p><strong>RMSE:</strong> {metricsData.RMSE.toFixed(3)}</p>
                </div>
            ) : (
                <p>No model metrics available.</p>
            )}
        </div>
    );
}

export default MetricsData;
