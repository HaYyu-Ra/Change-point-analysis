import pandas as pd
import pandas_datareader.data as web
from datetime import datetime


# Function to download economic indicator data from FRED
def download_economic_data(indicator, start_date, end_date, fred_api_key):
    """Download economic indicator data from FRED."""
    try:
        data = web.DataReader(
            indicator, "fred", start=start_date, end=end_date, api_key=fred_api_key
        )
        return data
    except Exception as e:
        print(f"Error occurred while fetching data: {e}")
        return None


# Constants
FRED_API_KEY = "YOUR_FRED_API_KEY"  # Replace with your FRED API key
start_date = "2020-01-01"  # Change to a smaller date range if needed
end_date = "2023-01-01"

# Download economic indicators (try with a different indicator)
economic_indicators = download_economic_data(
    "CPI", start_date, end_date, FRED_API_KEY
)  # Use 'CPI' as an example

# Check if data was successfully retrieved
if economic_indicators is not None:
    # Save to CSV
    economic_indicators.to_csv("economic_indicators.csv")
    print("Economic indicators data saved to 'economic_indicators.csv'.")
else:
    print("Failed to retrieve economic indicators data.")
