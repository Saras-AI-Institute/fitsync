import pandas as pd

# Load the data
data = pd.read_csv('data/health_data.csv')

# Print first 5 rows of the data
print("First 5 rows of the data:")
print(data.head())

# Check for missing values in each column
missing_values = data.isnull().sum()
print("\nNumber of missing values in each column:")
print(missing_values)
