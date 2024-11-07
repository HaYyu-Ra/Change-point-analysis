import React from 'react';
import { CartesianGrid, Legend, Line, LineChart, ResponsiveContainer, Tooltip, XAxis, YAxis } from 'recharts';

function EventImpactChart({ eventData }) {
    // Prepare data for the chart
    const chartData = eventData.map(event => ({
        date: event.event_date,
        price_change: event.price_change,
        highlight: event.highlight ? 1 : 0, // 1 for highlighted, 0 for not highlighted
    }));

    return (
        <div>
            <h3>Event Impact Chart</h3>
            <div style={{ width: '100%', height: 300 }}>
                {/* ResponsiveContainer ensures the chart is responsive */}
                <ResponsiveContainer>
                    <LineChart data={chartData}>
                        <CartesianGrid strokeDasharray="3 3" />
                        <XAxis dataKey="date" />
                        <YAxis />
                        <Tooltip />
                        <Legend />
                        <Line
                            type="monotone"
                            dataKey="price_change"
                            stroke="#8884d8"
                            activeDot={{ r: 8 }}
                        />
                        <Line
                            type="monotone"
                            dataKey="highlight"
                            stroke="#82ca9d"
                            dot={false}
                            strokeWidth={2}
                        />
                    </LineChart>
                </ResponsiveContainer>
            </div>
        </div>
    );
}

export default EventImpactChart;
