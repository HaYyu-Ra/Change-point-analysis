from flask import Flask, jsonify, request
from flask_cors import CORS
import pandas as pd
import numpy as np
from datetime import datetime
from statsmodels.tsa.arima.model import ARIMA

app = Flask(__name__)
CORS(app)  # This enables CORS


# Load Brent oil prices dataset
df_oil_prices = pd.read_csv(
    "C:/Users/hayyu.ragea/AppData/Local/Programs/Python/Python312/Change point analysis/Flask_Backend/data/processed/cleaned_brent_oil_prices.csv"
)
df_oil_prices["Date"] = pd.to_datetime(df_oil_prices["Date"])

# Load events data
df_events = pd.read_csv(
    "C:/Users/hayyu.ragea/AppData/Local/Programs/Python/Python312/Change point analysis/Flask_Backend/data/processed/cleaned_events_data.csv"
)
df_events["Date"] = pd.to_datetime(df_events["Date"])

# Model performance metrics (Example values)
model_metrics = {"RMSE": 0.02, "MAE": 0.015}


# Helper function to calculate volatility and average price change
def calculate_volatility_and_avg_change(start_date, end_date):
    filtered_data = df_oil_prices[
        (df_oil_prices["Date"] >= start_date) & (df_oil_prices["Date"] <= end_date)
    ]
    returns = filtered_data["Price"].pct_change()  # Percentage change in price
    volatility = returns.std()  # Volatility: standard deviation of returns
    avg_change = returns.mean()  # Average price change over time
    return float(volatility), float(avg_change)


# Helper function for forecasting oil prices
def forecast_oil_prices(n_periods=10):
    model = ARIMA(df_oil_prices["Price"], order=(5, 1, 0))  # ARIMA(5, 1, 0)
    model_fit = model.fit()
    forecast = model_fit.forecast(steps=n_periods)
    forecast_dates = pd.date_range(
        df_oil_prices["Date"].max(), periods=n_periods + 1, freq="D"
    )[1:]
    return forecast_dates, forecast


# Helper function to highlight significant price events
def highlight_event_impact():
    event_impact = []
    for _, row in df_events.iterrows():
        event_date = row["Date"]
        event_desc = row["Description"]
        price_data = df_oil_prices[df_oil_prices["Date"] == event_date]

        if not price_data.empty:
            price_impact = price_data["Price"].values[0]
            previous_price = (
                df_oil_prices[df_oil_prices["Date"] == event_date]["Price"]
                .shift(1)
                .values[0]
            )
            if not np.isnan(previous_price):
                price_change = price_impact - previous_price
                event_impact.append(
                    {
                        "event_date": event_date.strftime("%Y-%m-%d"),
                        "event_description": event_desc,
                        "price_change": float(price_change),
                        "highlight": abs(price_change) > 5,  # Threshold of 5
                    }
                )
    return event_impact


# API to fetch oil prices
@app.route("/api/oil_prices", methods=["GET"])
def get_oil_prices():
    try:
        start_date = request.args.get("start_date", default="1987-05-20")
        end_date = request.args.get("end_date", default="2022-09-30")
        start_date = pd.to_datetime(start_date)
        end_date = pd.to_datetime(end_date)

        # Filter oil prices based on date range
        filtered_data = df_oil_prices[
            (df_oil_prices["Date"] >= start_date) & (df_oil_prices["Date"] <= end_date)
        ]
        return jsonify(
            [
                {
                    "Date": row["Date"].strftime("%Y-%m-%d"),
                    "Price": float(row["Price"]),
                }
                for _, row in filtered_data.iterrows()
            ]
        )
    except Exception as e:
        return jsonify({"error": str(e)}), 400


# API to fetch events impacting Brent oil prices
@app.route("/api/events", methods=["GET"])
def get_events():
    events_data = [
        {
            "Date": row["Date"].strftime("%Y-%m-%d"),
            "Description": row["Description"],
            "Event": row["Event"],
        }
        for _, row in df_events.iterrows()
    ]
    return jsonify(events_data)


# API to fetch event impact
@app.route("/api/event_impact", methods=["GET"])
def get_event_impact():
    impacts = highlight_event_impact()
    return jsonify(impacts)


# API to fetch model metrics
@app.route("/api/metrics", methods=["GET"])
def get_metrics():
    return jsonify(model_metrics)


# API for volatility and average price change
@app.route("/api/volatility", methods=["GET"])
def get_volatility():
    try:
        start_date = request.args.get("start_date", default="1987-05-20")
        end_date = request.args.get("end_date", default="2022-09-30")
        start_date = pd.to_datetime(start_date)
        end_date = pd.to_datetime(end_date)

        volatility, avg_change = calculate_volatility_and_avg_change(
            start_date, end_date
        )
        return jsonify({"volatility": volatility, "avg_change": avg_change})
    except Exception as e:
        return jsonify({"error": str(e)}), 400


# API to get price forecast
@app.route("/api/forecast", methods=["GET"])
def get_forecast():
    try:
        forecast_dates, forecast = forecast_oil_prices()
        forecast_data = [
            {"date": date.strftime("%Y-%m-%d"), "forecast": float(price)}
            for date, price in zip(forecast_dates, forecast)
        ]
        return jsonify(forecast_data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
