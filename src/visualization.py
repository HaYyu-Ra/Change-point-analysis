import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Step 1: Define the file paths
brent_data_path = r"C:\Users\hayyu.ragea\AppData\Local\Programs\Python\Python312\Change point analysis\data\processed\cleaned_brent_oil_prices.csv"
events_data_path = r"C:\Users\hayyu.ragea\AppData\Local\Programs\Python\Python312\Change point analysis\data\processed\cleaned_events_data.csv"
exchange_rate_path = r"C:\Users\hayyu.ragea\AppData\Local\Programs\Python\Python312\Change point analysis\data\processed\Exchange_rate.csv"
gdp_data_path = r"C:\Users\hayyu.ragea\AppData\Local\Programs\Python\Python312\Change point analysis\data\processed\GDP.csv"
inflation_data_path = r"C:\Users\hayyu.ragea\AppData\Local\Programs\Python\Python312\Change point analysis\data\processed\inflation.csv"
unemployment_data_path = r"C:\Users\hayyu.ragea\AppData\Local\Programs\Python\Python312\Change point analysis\data\processed\unemployment.csv"


# Function to load data and handle errors
def load_data(file_path, date_col):
    try:
        data = pd.read_csv(file_path)
        # Strip spaces from column names
        data.columns = data.columns.str.strip()
        # Check if the date column exists
        if date_col not in data.columns:
            raise ValueError(f"Missing column provided to 'parse_dates': '{date_col}'")
        # Parse dates and set index
        data[date_col] = pd.to_datetime(
            data[date_col], errors="coerce"
        )  # Coerce invalid dates to NaT
        data.set_index(date_col, inplace=True)
        return data
    except Exception as e:
        print(f"Error loading data from {file_path}: {e}")
        return None  # Return None if there's an error


# Step 2: Load all datasets
brent_data = load_data(brent_data_path, "Date")  # Ensure 'Date' column is correct
events_data = load_data(
    events_data_path, "Event_Date"
)  # Ensure 'Event_Date' is correct
exchange_rate_data = load_data(exchange_rate_path, "Date")  # Ensure 'Date' is correct
gdp_data = load_data(gdp_data_path, "Date")  # Ensure 'Date' is correct
inflation_data = load_data(inflation_data_path, "Date")  # Ensure 'Date' is correct
unemployment_data = load_data(
    unemployment_data_path, "Date"
)  # Ensure 'Date' is correct

# Step 3: Clean GDP Data
if gdp_data is not None:
    # Check for any NaN values and remove them
    gdp_data.dropna(inplace=True)
    # Optionally, ensure 'GDP_Value' exists and is numeric
    if "GDP_Value" in gdp_data.columns:
        gdp_data["GDP_Value"] = pd.to_numeric(gdp_data["GDP_Value"], errors="coerce")
        gdp_data.dropna(
            subset=["GDP_Value"], inplace=True
        )  # Remove rows with NaN GDP values
    else:
        print("GDP data does not contain a 'GDP_Value' column.")

# Step 4: Visualize Brent Oil Prices if data is loaded successfully
if brent_data is not None:
    plt.figure(figsize=(12, 6))
    sns.lineplot(
        data=brent_data, x=brent_data.index, y="Price"
    )  # Ensure 'Price' is the correct column
    plt.title("Brent Oil Prices Over Time")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
else:
    print("Brent oil data could not be loaded.")

# Visualize GDP data if loaded
if gdp_data is not None:
    plt.figure(figsize=(12, 6))
    sns.lineplot(
        data=gdp_data, x=gdp_data.index, y="GDP_Value"
    )  # Ensure 'GDP_Value' is correct
    plt.title("GDP Over Time")
    plt.xlabel("Date")
    plt.ylabel("GDP Value")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
else:
    print("GDP data could not be loaded.")

# Add similar checks and visualizations for inflation, unemployment, and exchange rates here.
