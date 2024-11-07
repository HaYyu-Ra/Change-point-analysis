import React from 'react';

const PriceData = ({ priceData, formatDate }) => {
    return (
        <div>
            <h2>Price Data</h2>
            <table>
                <thead>
                    <tr>
                        <th>Date</th>
                        <th>Price</th>
                    </tr>
                </thead>
                <tbody>
                    {priceData.map((data, index) => (
                        <tr key={index}>
                            <td>{formatDate(data.Date)}</td>
                            <td>{data.Price}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
};

export default PriceData;
