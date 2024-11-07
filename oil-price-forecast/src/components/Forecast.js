import React from 'react';

function Forecast({ forecast }) {
    return (
        <div>
            <h2>Price Forecast</h2>
            <table>
                <thead>
                    <tr>
                        <th>Date</th>
                        <th>Forecast</th>
                    </tr>
                </thead>
                <tbody>
                    {forecast.map((forecastItem) => (
                        <tr key={forecastItem.date}>
                            <td>{forecastItem.date}</td>
                            <td>{forecastItem.forecast}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
}

export default Forecast;
