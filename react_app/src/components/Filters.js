// src/components/Filters.js
import React from 'react';

function Filters({ startDate, endDate, setStartDate, setEndDate }) {
    return (
        <div className="filters-container">
            <label>
                Start Date:
                <input
                    type="date"
                    value={startDate}
                    onChange={(e) => setStartDate(e.target.value)}
                />
            </label>
            <label>
                End Date:
                <input
                    type="date"
                    value={endDate}
                    onChange={(e) => setEndDate(e.target.value)}
                />
            </label>
        </div>
    );
}

export default Filters;
