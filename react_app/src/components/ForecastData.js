// src/components/ForecastData.js
import React from 'react';

function ForecastData({ forecastData }) {
    return (
        <div>
            <h2>Forecast Data</h2>
            {forecastData.length > 0 ? (
                <ul>
                    {forecastData.map((forecast, index) => (
                        <li key={index}>
                            <strong>{new Date(forecast.date).toLocaleDateString()}</strong>: ${forecast.forecast.toFixed(2)}
                        </li>
                    ))}
                </ul>
            ) : (
                <p>No forecast data available.</p>
            )}
        </div>
    );
}

export default ForecastData;
