import React from 'react';

function Volatility({ volatility }) {
    return (
        <div>
            <h2>Volatility & Average Price Change</h2>
            {volatility ? (
                <div>
                    <p>Volatility: {volatility.volatility}</p>
                    <p>Average Price Change: {volatility.avg_change}</p>
                </div>
            ) : (
                <p>Loading...</p>
            )}
        </div>
    );
}

export default Volatility;
