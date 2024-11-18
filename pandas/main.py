import pandas as pd

# Example fundamental data for stock valuation
data = {
    'Company': ['Company A', 'Company A', 'Company A', 'Company B', 'Company B', 'Company B'],
    'Year': [2020, 2021, 2022, 2020, 2021, 2022],
    'Earnings': [500, 600, 700, 1000, 1200, 1300],  # Net income in millions
    'Revenue': [5000, 5500, 6000, 8000, 8500, 9000],  # Revenue in millions
    'Book Value': [3000, 3200, 3500, 5000, 5200, 5500],  # Book value in millions
    'Dividends': [200, 220, 250, 400, 420, 450],  # Dividends paid in millions
    'Market Price': [100, 110, 120, 150, 160, 170],  # Market price per share
    'Shares Outstanding': [1000, 1000, 1000, 1000, 1000, 1000]  # Shares in millions
}

df = pd.DataFrame(data)

print(df)
