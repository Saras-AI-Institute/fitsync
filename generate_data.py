import numpy as np
import pandas as pd
from datetime import datetime, timedelta

# Constants for Data Generation
NUM_DAYS = 365
START_DATE = datetime(2025, 1, 1)

# Normal Distribution Parameters
STEP_MEAN = 8500
STEP_STD = 2000
SLEEP_MEAN = 7.2
SLEEP_STD = 1.0
HR_MEAN = 68
HR_STD = 10

# Data Ranges
STEPS_RANGE = (3000, 18000)
SLEEP_RANGE = (4.5, 9.5)
HR_RANGE = (48, 110)
CALORIES_RANGE = (1800, 4200)
ACTIVE_MINUTES_RANGE = (20, 180)

# Random State for Reproducibility
np.random.seed(0)

# Generate Dates
dates = [START_DATE + timedelta(days=i) for i in range(NUM_DAYS)]

# Generate Data
steps = np.clip(np.random.normal(STEP_MEAN, STEP_STD, NUM_DAYS), *STEPS_RANGE)
sleep_hours = np.clip(np.random.normal(SLEEP_MEAN, SLEEP_STD, NUM_DAYS), *SLEEP_RANGE)
heart_rate_bpm = np.clip(np.random.normal(HR_MEAN, HR_STD, NUM_DAYS), *HR_RANGE)

calories_burned = np.random.uniform(*CALORIES_RANGE, NUM_DAYS)
active_minutes = np.random.uniform(*ACTIVE_MINUTES_RANGE, NUM_DAYS)

# Create DataFrame
data = pd.DataFrame({
    'date': dates,
    'steps': steps,
    'sleep_hours': sleep_hours,
    'heart_rate_bpm': heart_rate_bpm,
    'calories_burned': calories_burned,
    'Active_minutes': active_minutes
})

# Introduce Missing Values
def introduce_missing_values(column):
    to_nan = np.random.choice(data.index, size=int(NUM_DAYS * 0.05), replace=False)
    data.loc[to_nan, column] = np.nan

for column in data.columns[1:]:  # skip the date column
    introduce_missing_values(column)

# Save to CSV
data.to_csv('data/health_data.csv', index=False)
