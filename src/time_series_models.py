import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.api import VAR
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split


def load_data(file_path):
    """Load the time series data from a CSV file."""
    data = pd.read_csv(file_path, parse_dates=["Date"], index_col="Date")
    return data


def check_stationarity(series):
    """Perform the Augmented Dickey-Fuller test for stationarity."""
    result = adfuller(series)
    print("ADF Statistic:", result[0])
    print("p-value:", result[1])
    for key, value in result[4].items():
        print(f"Critical Values:\n   {key}: {value}")
    return result[1] <= 0.05  # Returns True if series is stationary


def build_arima_model(data, order):
    """Build and fit an ARIMA model."""
    model = ARIMA(data, order=order)
    model_fit = model.fit()
    print(model_fit.summary())
    return model_fit


def build_var_model(data):
    """Build and fit a VAR model."""
    model = VAR(data)
    results = model.fit(maxlags=15, ic="aic")
    print(results.summary())
    return results


def build_random_forest_model(X_train, y_train):
    """Build and fit a Random Forest Regressor model."""
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    return model


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


def evaluate_model(model, X_test, y_test):
    """Evaluate the model performance using Mean Squared Error."""
    if isinstance(model, RandomForestRegressor):
        y_pred = model.predict(X_test)
    else:
        y_pred = model.forecast(X_test.values[-model.k_ar :], steps=len(X_test))

    mse = mean_squared_error(y_test, y_pred)
    print(f"Mean Squared Error: {mse}")
    return mse


def main():
    # Load data
    file_path = r"C:\Users\hayyu.ragea\AppData\Local\Programs\Python\Python312\Change point analysis\data\processed\cleaned_brent_oil_prices.csv"
    data = load_data(file_path)

    # Check for stationarity
    stationary = check_stationarity(data["Price"])

    # Build ARIMA model
    if stationary:
        arima_order = (1, 0, 1)  # Example order
        arima_model = build_arima_model(data["Price"], order=arima_order)
        plot_forecast(arima_model, steps=5, data=data["Price"], model_type="ARIMA")

    # Build VAR model
    additional_data = pd.DataFrame(
        {
            "GDP": np.random.rand(len(data)),
            "Inflation": np.random.rand(len(data)),
            "Unemployment": np.random.rand(len(data)),
            "Exchange_Rate": np.random.rand(len(data)),
        },
        index=data.index,
    )

    var_model = build_var_model(pd.concat([data, additional_data], axis=1))
    plot_forecast(
        var_model,
        steps=5,
        data=pd.concat([data, additional_data], axis=1),
        model_type="VAR",
    )

    # Build Random Forest model for machine learning approach
    X = additional_data
    y = data["Price"]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    rf_model = build_random_forest_model(X_train, y_train)

    # Evaluate Random Forest model
    evaluate_model(rf_model, X_test, y_test)


if __name__ == "__main__":
    main()
