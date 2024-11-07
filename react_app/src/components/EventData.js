import React from 'react';

const EventData = ({ eventData, formatDate }) => {
    return (
        <div>
            <h2>Event Data</h2>
            <table>
                <thead>
                    <tr>
                        <th>Date</th>
                        <th>Event</th>
                        <th>Description</th>
                    </tr>
                </thead>
                <tbody>
                    {eventData.map((event, index) => (
                        <tr key={index}>
                            <td>{formatDate(event.Date)}</td>
                            <td>{event.Event}</td>
                            <td>{event.Description}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
};

export default EventData;
