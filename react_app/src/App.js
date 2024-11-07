import React, { useState } from 'react';
import './App.css';
import EventData from './components/EventData';
import Filters from './components/Filters';
import ForecastData from './components/ForecastData';
import MetricsData from './components/MetricsData';
import PriceData from './components/PriceData';
import VolatilityData from './components/VolatilityData';

// Function to format the date to a readable format
const formatDate = (dateString) => {
  const date = new Date(dateString);
  return date.toLocaleDateString('en-US', { year: 'numeric', month: 'short', day: 'numeric' });
};

// Component for displaying and managing price data
function App() {
  const [priceData, setPriceData] = useState([]);
  const [eventData, setEventData] = useState([]);
  const [volatilityData, setVolatilityData] = useState({});
  const [forecastData, setForecastData] = useState([]);
  const [metricsData, setMetricsData] = useState({});
  const [startDate, setStartDate] = useState('');
  const [endDate, setEndDate] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  // Fetch price data based on selected date range
  const fetchData = async () => {
    if (!startDate || !endDate) {
      alert('Please select both start and end dates.');
      return;
    }

    setLoading(true);
    setError(null);

    const urls = [
      `http://127.0.0.1:5000/api/oil_prices?start_date=${startDate}&end_date=${endDate}`,
      `http://127.0.0.1:5000/api/events`,
      `http://127.0.0.1:5000/api/volatility?start_date=${startDate}&end_date=${endDate}`,
      `http://127.0.0.1:5000/api/forecast`,
      `http://127.0.0.1:5000/api/metrics`,
    ];

    try {
      const responses = await Promise.all(urls.map((url) => fetch(url)));
      const data = await Promise.all(responses.map((res) => res.json()));

      // Check for any failed responses
      responses.forEach((res, index) => {
        if (!res.ok) {
          console.error(`Failed to fetch data from ${urls[index]}. Status: ${res.status}`);
        }
      });

      const [priceRes, eventRes, volatilityRes, forecastRes, metricsRes] = data;

      setPriceData(priceRes);
      setEventData(eventRes);
      setVolatilityData(volatilityRes);
      setForecastData(forecastRes);
      setMetricsData(metricsRes);

      // Handle empty responses
      if (priceRes.length === 0) {
        setError('No price data available for the selected date range.');
      }
      if (eventRes.length === 0) {
        setError((prevError) => (prevError ? prevError + '\nNo event data available.' : 'No event data available.'));
      }
      if (Object.keys(volatilityRes).length === 0) {
        setError((prevError) => (prevError ? prevError + '\nNo volatility data available.' : 'No volatility data available.'));
      }
      if (forecastRes.length === 0) {
        setError((prevError) => (prevError ? prevError + '\nNo forecast data available.' : 'No forecast data available.'));
      }
      if (Object.keys(metricsRes).length === 0) {
        setError((prevError) => (prevError ? prevError + '\nNo model metrics available.' : 'No model metrics available.'));
      }
    } catch (error) {
      console.error("Error fetching data:", error);
      setError('Failed to fetch data. Please try again later.');
    } finally {
      setLoading(false);
    }
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    fetchData();
  };

  return (
    <div className="App">
      <h1>Brent Oil Price Data & Analysis</h1>
      <form onSubmit={handleSubmit}>
        <Filters startDate={startDate} endDate={endDate} setStartDate={setStartDate} setEndDate={setEndDate} />
        <button type="submit" disabled={loading}>
          {loading ? 'Loading...' : 'Fetch Data'}
        </button>
      </form>

      {/* Error Handling */}
      {error && <p className="error">{error}</p>}

      {/* Display Data */}
      <PriceData priceData={priceData} formatDate={formatDate} />
      <EventData eventData={eventData} formatDate={formatDate} />
      <VolatilityData volatilityData={volatilityData} />
      <ForecastData forecastData={forecastData} formatDate={formatDate} />
      <MetricsData metricsData={metricsData} />
    </div>
  );
}

export default App;
