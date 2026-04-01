import pandas as pd
from datetime import datetime


def load_data():
    """
    Load and clean the health data from CSV.

    This function:
    - Reads data from 'data/health_data.csv'.
    - Fills missing 'Steps' with the median value.
    - Fills missing 'Sleep_Hour' with 7.0.
    - Fills missing 'Heart_Rate_bpm' with 68.
    - Fills other missing values with their column median.
    - Converts 'Date' column to datetime objects.

    Returns:
        pd.DataFrame: A cleaned pandas DataFrame.
    """
    # Load the CSV file into a DataFrame
    df = pd.read_csv('data/health_data.csv')

    # Fill missing values for specific columns
    if 'Steps' in df:
        df['Steps'].fillna(df['Steps'].median(), inplace=True)

    if 'Sleep_Hour' in df:
        df['Sleep_Hour'].fillna(7.0, inplace=True)

    if 'Heart_Rate_bpm' in df:
        df['Heart_Rate_bpm'].fillna(68, inplace=True)

    # Fill any other numerical columns with the median of that column
    df.fillna(df.median(numeric_only=True), inplace=True)

    # Convert 'Date' column to datetime objects
    if 'Date' in df:
        df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

    return df
