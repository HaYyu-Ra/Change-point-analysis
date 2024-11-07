# Required Libraries
import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.arima.model import ARIMA
import ruptures as rpt
from datetime import datetime
import os
from fredapi import Fred
import statsmodels.api as sm
from statsmodels.tsa.api import VAR
from keras.models import Sequential
from keras.layers import LSTM, Dense, Dropout

# FRED API key setup
fred_api_key = (
    "b854a334011411eddeccad0687b69290"  # Replace this with your actual FRED API key
)
fred = Fred(api_key=fred_api_key)

# Paths for data files
data_dir = r"C:\Users\hayyu.ragea\AppData\Local\Programs\Python\Python312\Change point analysis\data\processed"
brent_data_path = os.path.join(data_dir, "cleaned_brent_oil_prices.csv")
events_data_path = os.path.join(data_dir, "cleaned_events_data.csv")


# Download historical Brent oil prices
def download_data():
    ticker = "BZ=F"
    start_date = "1987-05-20"
    end_date = "2022-09-30"
    data = yf.download(ticker, start=start_date, end=end_date)
    data = data[["Close"]].rename(columns={"Close": "Price"})
    data.index.name = "Date"
    return data


# Load Data
def load_data():
    if os.path.exists(brent_data_path):
        data = pd.read_csv(brent_data_path, index_col="Date", parse_dates=True)
    else:
        data = download_data()
        data.to_csv(brent_data_path)
    return data


# Fetch Economic Indicators Data
def fetch_economic_data():
    # GDP Growth (U.S.)
    gdp_growth = fred.get_series("GDP")
    inflation = fred.get_series("CPIAUCSL")
    unemployment = fred.get_series("UNRATE")
    usd_index = fred.get_series("DTWEXBGS")
    economic_data = pd.DataFrame(
        {
            "GDP_Growth": gdp_growth,
            "Inflation": inflation,
            "Unemployment": unemployment,
            "USD_Index": usd_index,
        }
    )
    economic_data.index = pd.to_datetime(economic_data.index)
    economic_data = economic_data.resample("M").mean()
    return economic_data


# Merge Data
def merge_data_with_oil_prices(oil_data, economic_data):
    merged_data = oil_data.join(economic_data, how="inner")
    merged_data.dropna(inplace=True)
    return merged_data


# Perform EDA
def eda(data):
    print(data.describe())
    plt.figure(figsize=(14, 7))
    plt.plot(data["Price"], label="Brent Oil Price")
    plt.title("Brent Oil Prices Over Time")
    plt.xlabel("Date")
    plt.ylabel("Price (USD per barrel)")
    plt.legend()
    plt.show()

    # Check stationarity
    result = adfuller(data["Price"])
    print("ADF Statistic:", result[0])
    print("p-value:", result[1])
    if result[1] <= 0.05:
        print("Data is stationary")
    else:
        print(
            "Data is non-stationary, further differencing or transformation might be required."
        )


# Change Point Analysis
def change_point_detection(data):
    series = data["Price"].values
    algo = rpt.Binseg(model="l2").fit(series)
    change_points = algo.predict(n_bkps=10)
    plt.figure(figsize=(14, 7))
    plt.plot(series, label="Brent Oil Price")
    for cp in change_points:
        plt.axvline(
            cp,
            color="r",
            linestyle="--",
            label="Change Point" if cp == change_points[0] else "",
        )
    plt.title("Change Point Analysis on Brent Oil Prices")
    plt.xlabel("Time")
    plt.ylabel("Price (USD per barrel)")
    plt.legend()
    plt.show()
    return change_points


# Time Series Modeling (e.g., ARIMA)
def time_series_modeling(data, order=(1, 1, 1)):
    model = ARIMA(data["Price"], order=order)
    fitted_model = model.fit()
    print(fitted_model.summary())
    forecast = fitted_model.forecast(steps=30)
    plt.figure(figsize=(14, 7))
    plt.plot(data["Price"], label="Original")
    plt.plot(forecast, label="Forecast", color="red")
    plt.title("ARIMA Model Forecast")
    plt.xlabel("Date")
    plt.ylabel("Price (USD per barrel)")
    plt.legend()
    plt.show()
    return fitted_model


# Analyze Economic Factors
def analyze_economic_factors(merged_data):
    correlation_matrix = merged_data.corr()
    plt.figure(figsize=(10, 6))
    sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f")
    plt.title("Correlation Matrix of Brent Oil Prices with Economic Indicators")
    plt.show()

    # Plot each economic indicator against oil prices
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle("Economic Indicators vs. Brent Oil Prices", fontsize=16)

    axes[0, 0].plot(merged_data["Price"], label="Brent Oil Price")
    axes[0, 0].set_ylabel("USD per Barrel")
    axes[0, 0].set_title("Brent Oil Price")

    axes[0, 1].plot(merged_data["GDP_Growth"], color="green", label="GDP Growth")
    axes[0, 1].set_ylabel("GDP Growth Rate")
    axes[0, 1].set_title("GDP Growth Rate")

    axes[1, 0].plot(merged_data["Inflation"], color="red", label="Inflation Rate")
    axes[1, 0].set_ylabel("Inflation Rate")
    axes[1, 0].set_title("Inflation Rate")

    axes[1, 1].plot(
        merged_data["Unemployment"], color="purple", label="Unemployment Rate"
    )
    axes[1, 1].set_ylabel("Unemployment Rate")
    axes[1, 1].set_title("Unemployment Rate")

    for ax in axes.flat:
        ax.set_xlabel("Date")
        ax.legend()

    plt.tight_layout()
    plt.show()

    # Regression analysis
    for column in ["GDP_Growth", "Inflation", "Unemployment", "USD_Index"]:
        X = sm.add_constant(merged_data[column])
        model = sm.OLS(merged_data["Price"], X).fit()
        print(f"Regression analysis for {column} vs. Oil Price:")
        print(model.summary())


# Time Series Forecasting with LSTM
def lstm_forecasting(data):
    # Prepare data for LSTM
    from sklearn.preprocessing import MinMaxScaler

    scaler = MinMaxScaler()
    scaled_data = scaler.fit_transform(data["Price"].values.reshape(-1, 1))

    # Create dataset for LSTM
    def create_dataset(dataset, time_step=1):
        X, Y = [], []
        for i in range(len(dataset) - time_step - 1):
            X.append(dataset[i : (i + time_step), 0])
            Y.append(dataset[i + time_step, 0])
        return np.array(X), np.array(Y)

    time_step = 10
    X, Y = create_dataset(scaled_data, time_step)
    X = X.reshape(X.shape[0], X.shape[1], 1)

    # Build LSTM Model
    model = Sequential()
    model.add(LSTM(50, return_sequences=True, input_shape=(X.shape[1], 1)))
    model.add(Dropout(0.2))
    model.add(LSTM(50, return_sequences=False))
    model.add(Dropout(0.2))
    model.add(Dense(1))

    model.compile(loss="mean_squared_error", optimizer="adam")
    model.fit(X, Y, epochs=100, batch_size=32)

    # Forecasting
    predictions = model.predict(X)
    plt.plot(scaler.inverse_transform(predictions), label="LSTM Predictions")
    plt.title("LSTM Predictions on Brent Oil Prices")
    plt.xlabel("Date")
    plt.ylabel("Price (USD per barrel)")
    plt.legend()
    plt.show()


# Main execution function
if __name__ == "__main__":
    brent_data = load_data()
    economic_data = fetch_economic_data()
    merged_data = merge_data_with_oil_prices(brent_data, economic_data)
    eda(merged_data)
    change_points = change_point_detection(merged_data)
    fitted_model = time_series_modeling(merged_data)
    analyze_economic_factors(merged_data)
    lstm_forecasting(merged_data)
