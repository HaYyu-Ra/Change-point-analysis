// src/api.js
import axios from 'axios';

// Fetch oil prices for the selected date range
export const fetchOilPrices = async (startDate, endDate) => {
    try {
        const response = await axios.get('http://localhost:5000/api/oil_prices', {
            params: {
                start_date: startDate,
                end_date: endDate
            }
        });
        return response;
    } catch (error) {
        console.error('Error fetching oil prices:', error);
        return [];
    }
};

// Fetch the price forecast data
export const fetchForecast = async () => {
    try {
        const response = await axios.get('http://localhost:5000/api/forecast');
        return response;
    } catch (error) {
        console.error('Error fetching forecast data:', error);
        return [];
    }
};
