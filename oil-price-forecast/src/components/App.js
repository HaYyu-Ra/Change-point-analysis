import { Container, Grid, Paper, Typography } from '@mui/material';
import axios from 'axios';
import React, { useEffect, useState } from 'react';
import { CartesianGrid, Legend, Line, LineChart, ResponsiveContainer, Tooltip, XAxis, YAxis } from 'recharts';
import Events from './components/Events';
import Forecast from './components/Forecast';
import Metrics from './components/Metrics';
import OilPrices from './components/OilPrices';
import Volatility from './components/Volatility';

function App() {
    const [oilPrices, setOilPrices] = useState([]);
    const [events, setEvents] = useState([]);
    const [metrics, setMetrics] = useState({});
    const [volatility, setVolatility] = useState(null);
    const [forecast, setForecast] = useState([]);
    const [startDate, setStartDate] = useState('1987-05-20');
    const [endDate, setEndDate] = useState('2022-09-30');

    // Fetch all data from Flask API
    useEffect(() => {
        axios.get(`http://localhost:5000/api/oil_prices?start_date=${startDate}&end_date=${endDate}`)
            .then(response => setOilPrices(response.data))
            .catch(error => console.error('Error fetching oil prices:', error));

        axios.get('http://localhost:5000/api/events')
            .then(response => setEvents(response.data))
            .catch(error => console.error('Error fetching events:', error));

        axios.get('http://localhost:5000/api/metrics')
            .then(response => setMetrics(response.data))
            .catch(error => console.error('Error fetching metrics:', error));

        axios.get(`http://localhost:5000/api/volatility?start_date=${startDate}&end_date=${endDate}`)
            .then(response => setVolatility(response.data))
            .catch(error => console.error('Error fetching volatility:', error));

        axios.get('http://localhost:5000/api/forecast')
            .then(response => setForecast(response.data))
            .catch(error => console.error('Error fetching forecast:', error));
    }, [startDate, endDate]);

    return (
        <Container>
            <Typography variant="h3" gutterBottom align="center">
                Oil Price Analysis Dashboard
            </Typography>

            {/* Date Range Filter */}
            <Grid container spacing={2} justifyContent="center">
                <Grid item>
                    <Typography>Start Date:</Typography>
                    <input
                        type="date"
                        value={startDate}
                        onChange={(e) => setStartDate(e.target.value)}
                    />
                </Grid>
                <Grid item>
                    <Typography>End Date:</Typography>
                    <input
                        type="date"
                        value={endDate}
                        onChange={(e) => setEndDate(e.target.value)}
                    />
                </Grid>
            </Grid>

            {/* Oil Prices Section */}
            <Grid container spacing={4} marginTop={4}>
                <Grid item xs={12} md={6}>
                    <Paper sx={{ padding: 2 }}>
                        <OilPrices oilPrices={oilPrices} />
                    </Paper>
                </Grid>

                {/* Events Impacting Prices */}
                <Grid item xs={12} md={6}>
                    <Paper sx={{ padding: 2 }}>
                        <Events events={events} />
                    </Paper>
                </Grid>
            </Grid>

            {/* Metrics Section */}
            <Grid container spacing={4} marginTop={4}>
                <Grid item xs={12} md={6}>
                    <Paper sx={{ padding: 2 }}>
                        <Metrics metrics={metrics} />
                    </Paper>
                </Grid>

                {/* Volatility Section */}
                <Grid item xs={12} md={6}>
                    <Paper sx={{ padding: 2 }}>
                        <Volatility volatility={volatility} />
                    </Paper>
                </Grid>
            </Grid>

            {/* Forecast Section */}
            <Grid container spacing={4} marginTop={4}>
                <Grid item xs={12} md={6}>
                    <Paper sx={{ padding: 2 }}>
                        <Forecast forecast={forecast} />
                    </Paper>
                </Grid>

                {/* Price Forecast Chart */}
                <Grid item xs={12} md={6}>
                    <Paper sx={{ padding: 2 }}>
                        <Typography variant="h6" gutterBottom>
                            Oil Price Forecast (Line Chart)
                        </Typography>
                        <ResponsiveContainer width="100%" height={300}>
                            <LineChart data={forecast}>
                                <CartesianGrid strokeDasharray="3 3" />
                                <XAxis dataKey="date" />
                                <YAxis />
                                <Tooltip />
                                <Legend />
                                <Line type="monotone" dataKey="forecast" stroke="#8884d8" />
                            </LineChart>
                        </ResponsiveContainer>
                    </Paper>
                </Grid>
            </Grid>
        </Container>
    );
}

export default App;
