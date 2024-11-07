import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.api import VAR
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
import pandas_datareader.data as web
from datetime import datetime


# Function to load time series data from CSV
def load_data(file_path):
    """Load the time series data from a CSV file."""
    data = pd.read_csv(file_path, parse_dates=["Date"], index_col="Date")
    return data


# Function to download economic indicator data from FRED
def download_economic_data(indicator, start_date, end_date, fred_api_key):
    """Download economic indicator data from FRED."""
    data = web.DataReader(
        indicator, "fred", start=start_date, end=end_date, api_key=fred_api_key
    )
    return data


# Function to check for stationarity
def check_stationarity(series):
    """Perform the Augmented Dickey-Fuller test for stationarity."""
    result = adfuller(series)
    print("ADF Statistic:", result[0])
    print("p-value:", result[1])
    for key, value in result[4].items():
        print(f"Critical Values:\n   {key}: {value}")
    return result[1] <= 0.05  # Returns True if series is stationary


# Function to build and fit an ARIMA model
def build_arima_model(data, order):
    """Build and fit an ARIMA model."""
    model = ARIMA(data, order=order)
    model_fit = model.fit()
    print(model_fit.summary())
    return model_fit


# Function to build and fit a VAR model
def build_var_model(data):
    """Build and fit a VAR model."""
    model = VAR(data)
    results = model.fit(maxlags=15, ic="aic")
    print(results.summary())
    return results


# Function to build and fit a Random Forest Regressor model
def build_random_forest_model(X_train, y_train):
    """Build and fit a Random Forest Regressor model."""
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    return model


# Function to plot forecasted values
def plot_forecast(model, steps, data, model_type):
    """Plot the forecasted values."""
    if model_type == "ARIMA":
        forecast = model.forecast(steps)
        forecast_index = pd.date_range(
            start=data.index[-1] + pd.Timedelta(days=1), periods=steps
        )
        forecast_series = pd.Series(forecast, index=forecast_index)

        plt.figure(figsize=(12, 6))
        plt.plot(data.index, data, label="Historical Data")
        plt.plot(
            forecast_series.index,
            forecast_series,
            label="ARIMA Forecast",
            color="orange",
        )
        plt.title("ARIMA Forecast")
        plt.xlabel("Date")
        plt.ylabel("Values")
        plt.legend()
        plt.show()

    elif model_type == "VAR":
        forecast = model.forecast(data.values[-model.k_ar :], steps=steps)
        forecast_index = pd.date_range(
            start=data.index[-1] + pd.Timedelta(days=1), periods=steps
        )
        forecast_df = pd.DataFrame(forecast, index=forecast_index, columns=data.columns)

        plt.figure(figsize=(12, 6))
        for col in forecast_df.columns:
            plt.plot(forecast_df.index, forecast_df[col], label=f"Forecast {col}")
        plt.title("VAR Forecast")
        plt.xlabel("Date")
        plt.ylabel("Values")
        plt.legend()
        plt.show()


# Function to evaluate the model performance
def evaluate_model(model, X_test, y_test):
    """Evaluate the model performance using Mean Squared Error."""
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    print(f"Mean Squared Error: {mse}")
    return mse


def main():
    # Constants
    FRED_API_KEY = "b854a334011411eddeccad0687b69290"  # Your FRED API key
    gdp_data_file_path = r"C:\Users\hayyu.ragea\AppData\Local\Programs\Python\Python312\Change point analysis\data\processed\cleaned_GDP.csv"

    # Load GDP data
    gdp_data = load_data(gdp_data_file_path)

    # Download economic indicators (modify series ID as needed)
    start_date = "1987-05-20"
    end_date = "2022-09-30"
    economic_indicators = download_economic_data(
        "CPIA_GENDER_EQL_AN", start_date, end_date, FRED_API_KEY
    )  # Replace with the desired indicator

    # Check for stationarity
    stationary = check_stationarity(
        gdp_data["GDP"]
    )  # Make sure to reference the correct column name

    # Build ARIMA model
    if stationary:
        arima_order = (1, 0, 1)  # Example order
        arima_model = build_arima_model(gdp_data["GDP"], order=arima_order)
        plot_forecast(arima_model, steps=5, data=gdp_data["GDP"], model_type="ARIMA")

    # Build VAR model
    combined_data = pd.concat([gdp_data, economic_indicators], axis=1).dropna()
    var_model = build_var_model(combined_data)
    plot_forecast(var_model, steps=5, data=combined_data, model_type="VAR")

    # Prepare data for Random Forest model
    X = economic_indicators
    y = gdp_data["GDP"]  # Ensure you're predicting GDP
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Build and evaluate Random Forest model
    rf_model = build_random_forest_model(X_train, y_train)
    evaluate_model(rf_model, X_test, y_test)


if __name__ == "__main__":
    main()
