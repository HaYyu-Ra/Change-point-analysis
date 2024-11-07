// src/components/VolatilityData.js
import React from 'react';

function VolatilityData({ volatilityData }) {
    return (
        <div>
            <h2>Volatility Data</h2>
            {volatilityData && volatilityData.avg_change ? (
                <div>
                    <p><strong>Average Change:</strong> {volatilityData.avg_change.toFixed(4)}</p>
                    <p><strong>Volatility:</strong> {volatilityData.volatility.toFixed(4)}</p>
                </div>
            ) : (
                <p>No volatility data available.</p>
            )}
        </div>
    );
}

export default VolatilityData;
