import pandas as pd

# Define file paths
brent_prices_path = r"C:\Users\hayyu.ragea\AppData\Local\Programs\Python\Python312\Change point analysis\brent-oil-dashboard\backend\data\cleaned_brent_oil_prices.csv"
events_data_path = r"C:\Users\hayyu.ragea\AppData\Local\Programs\Python\Python312\Change point analysis\brent-oil-dashboard\backend\data\cleaned_events_data.csv"

# Load data
brent_prices_df = pd.read_csv(brent_prices_path)
events_data_df = pd.read_csv(events_data_path)

# Inspect column names (to verify)
print("Brent Prices DataFrame Columns:", brent_prices_df.columns)
print("Events Data DataFrame Columns:", events_data_df.columns)

# Rename "Date" column to lowercase "date" (optional)
brent_prices_df.rename(columns={"Date": "date"}, inplace=True)
events_data_df.rename(columns={"Date": "date"}, inplace=True)

# Convert date columns to datetime format
brent_prices_df["date"] = pd.to_datetime(brent_prices_df["date"])
events_data_df["date"] = pd.to_datetime(events_data_df["date"])

# Merge dataframes on "date" column, using an outer join to retain all data
merged_df = pd.merge(brent_prices_df, events_data_df, on="date", how="outer")

# Save the merged data to a new CSV file
output_path = r"C:\Users\hayyu.ragea\AppData\Local\Programs\Python\Python312\Change point analysis\brent-oil-dashboard\backend\data\merged_brent_events_data.csv"
merged_df.to_csv(output_path, index=False)

print(f"Merged data saved to {output_path}")
