import pandas as pd

# Define a list of dictionaries with event data
events = [
    {"Date": "1990-08-02", "Event": "Gulf War begins", 
     "Description": "Iraq invades Kuwait, causing a major oil price shock."},
    {"Date": "2001-09-11", "Event": "9/11 Terrorist Attacks", 
     "Description": "US markets experience shock, and oil prices fluctuate with economic uncertainty."},
    {"Date": "2014-06-01", "Event": "Oil Price Drop due to Increased US Shale Production", 
     "Description": "A significant drop in oil prices as US increases shale oil production, reducing OPEC’s influence over global oil supply."},
    {"Date": "2020-03-08", "Event": "Saudi-Russia Oil Price War and COVID-19 Pandemic Begins", 
     "Description": "An oil price war between Saudi Arabia and Russia, exacerbated by global demand drops due to COVID-19 lockdowns."}
]

# Convert the list of dictionaries to a DataFrame
events_df = pd.DataFrame(events)

# Convert the 'Date' column to datetime format
events_df['Date'] = pd.to_datetime(events_df['Date'])

# Save the DataFrame to a CSV file
events_df.to_csv('events_data.csv', index=False)

print("events_data.csv has been created successfully.")
