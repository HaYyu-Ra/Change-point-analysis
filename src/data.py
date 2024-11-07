import yfinance as yf
import pandas as pd
import datetime
import os

# Set the date range for the data
start_date = "1987-05-20"
end_date = "2022-09-30"

# Define the file paths for saving data
base_path = "C:/Users/hayyu.ragea/AppData/Local/Programs/Python/Python312/Change point analysis/data/processed/"
os.makedirs(base_path, exist_ok=True)  # Create directory if it doesn't exist

files = {
    "Brent_Oil_Prices": "brent_oil_prices.csv",
    "GDP": "gdp.csv",  # Assuming you will download GDP data with a specific symbol
    "Inflation": "inflation.csv",  # Assuming you will download Inflation data with a specific symbol
    "Unemployment": "unemployment.csv",  # Assuming you will download Unemployment data with a specific symbol
    "Exchange_Rate": "exchange_rate.csv",  # File for Exchange Rates
    "Events": "events_data.csv",  # Placeholder for event data
}

# Metadata for Brent Oil Prices
brent_metadata = """
Dataset: Historical Brent Oil Prices
Description: This dataset contains daily Brent oil prices recorded from May 20, 1987, to September 30, 2022.
Fields:
- Date: The date of the recorded Brent oil price, formatted as 'day-month-year' (e.g., 20-May-87).
- Price: Brent oil price in USD per barrel for the given date.
"""


# Function to download and save Brent Oil prices
def download_brent_oil_prices(filename):
    try:
        data = yf.download("BZ=F", start=start_date, end=end_date)
        data.to_csv(os.path.join(base_path, filename))
        print(f"Downloaded {filename} successfully.\n\nMetadata:\n{brent_metadata}")
    except Exception as e:
        print(f"Error downloading {filename}: {e}")


# Function to download economic data (GDP, Inflation, Unemployment, Exchange Rate)
def download_economic_data(symbol, filename):
    try:
        data = yf.download(symbol, start=start_date, end=end_date)
        data.to_csv(os.path.join(base_path, filename))
        print(f"Downloaded {filename} successfully.")
    except Exception as e:
        print(f"Error downloading {filename}: {e}")


# Function to manually load event data
def load_event_data(filename):
    try:
        # Placeholder for actual event data download process or CSV load
        # Replace this with the actual download or loading method
        event_data = pd.DataFrame()  # Placeholder dataframe
        event_data.to_csv(os.path.join(base_path, filename))
        print(f"Event data saved as {filename}.")
    except Exception as e:
        print(f"Error saving {filename}: {e}")


# Download Brent Oil Prices
download_brent_oil_prices(files["Brent_Oil_Prices"])

# Example economic indicators to download (replace with actual symbols)
download_economic_data(
    "GDP", files["GDP"]
)  # Replace "GDP" with actual ticker if available
download_economic_data(
    "CPI", files["Inflation"]
)  # Replace "CPI" with actual ticker if available
download_economic_data(
    "UNRATE", files["Unemployment"]
)  # Replace "UNRATE" with actual ticker if available

# Load and save event data
load_event_data(files["Events"])

print("All data downloads attempted.")
