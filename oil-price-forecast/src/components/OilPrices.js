import React from 'react';

function OilPrices({ oilPrices }) {
    return (
        <div>
            <h2>Oil Prices</h2>
            <table>
                <thead>
                    <tr>
                        <th>Date</th>
                        <th>Price</th>
                    </tr>
                </thead>
                <tbody>
                    {oilPrices.map((price) => (
                        <tr key={price.Date}>
                            <td>{price.Date}</td>
                            <td>{price.Price}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
}

export default OilPrices;
