import yfinance as yf

# Download historical Brent crude oil prices
brent_data = yf.download('BZ=F', start='1987-05-20', end='2022-09-30')

# Select only the 'Close' price and rename it to 'Price'
brent_data = brent_data[['Close']].rename(columns={'Close': 'Price'})

# Save to CSV
brent_data.to_csv('brent_oil_prices.csv')
