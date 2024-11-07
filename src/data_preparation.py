import pandas as pd

# Path to the Exchange Rate data file
exchange_rate_data_path = r"C:\Users\hayyu.ragea\AppData\Local\Programs\Python\Python312\Change point analysis\data\processed\Exchange_rate.csv"

try:
    # Load the exchange rate data, skipping the first two rows which contain unnecessary headers
    exchange_rate_df = pd.read_csv(exchange_rate_data_path, skiprows=2)

    # Display the initial structure of the DataFrame
    print("Initial DataFrame:")
    print(exchange_rate_df.head())

    # Clean column names (remove leading/trailing whitespace)
    exchange_rate_df.columns = exchange_rate_df.columns.str.strip()

    # Check if the first row contains proper headers, if not, set correct headers manually
    # Assuming the first two columns are 'Date' and 'Exchange Rate', you might need to adjust this
    exchange_rate_df.columns = ["Date", "Exchange_Rate"] + list(
        exchange_rate_df.columns[2:]
    )

    # Parse the 'Date' column to datetime format
    exchange_rate_df["Date"] = pd.to_datetime(exchange_rate_df["Date"], errors="coerce")

    # Drop rows where 'Date' or 'Exchange_Rate' is NaT or NaN
    exchange_rate_df.dropna(subset=["Date", "Exchange_Rate"], inplace=True)

    # Convert 'Exchange_Rate' to numeric, handling any potential conversion errors
    exchange_rate_df["Exchange_Rate"] = pd.to_numeric(
        exchange_rate_df["Exchange_Rate"], errors="coerce"
    )

    # Drop any remaining rows with NaN values
    exchange_rate_df.dropna(inplace=True)

    # Save the cleaned data to a new file
    cleaned_exchange_rate_data_path = r"C:\Users\hayyu.ragea\AppData\Local\Programs\Python\Python312\Change point analysis\data\processed\cleaned_exchange_rate.csv"
    exchange_rate_df.to_csv(cleaned_exchange_rate_data_path, index=False)
    print(f"\nCleaned data saved to: {cleaned_exchange_rate_data_path}")

except Exception as e:
    print(f"Error processing exchange rate data: {str(e)}")
