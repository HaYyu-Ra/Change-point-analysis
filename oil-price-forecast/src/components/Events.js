import React from 'react';

function Events({ events }) {
    return (
        <div>
            <h2>Events Impacting Oil Prices</h2>
            <ul>
                {events.map((event, index) => (
                    <li key={index}>
                        <strong>{event.Event}</strong> ({event.Date}): {event.Description}
                    </li>
                ))}
            </ul>
        </div>
    );
}

export default Events;
