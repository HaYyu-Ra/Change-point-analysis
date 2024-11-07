// src/components/EventImpact.js
import React, { useEffect, useState } from 'react';
import { fetchEventImpact } from '../api';

const EventImpact = () => {
    const [impacts, setImpacts] = useState([]);

    useEffect(() => {
        fetchEventImpact().then((response) => {
            setImpacts(response.data);
        });
    }, []);

    return (
        <div>
            <h2>Event Impact on Oil Prices</h2>
            <ul>
                {impacts.map((impact) => (
                    <li key={impact.event_date}>
                        <strong>{impact.event_description}</strong> - Price change: {impact.price_change} USD
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default EventImpact;
