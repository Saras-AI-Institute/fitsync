import streamlit as st
from modules.processor import process_data
import pandas as pd

# Configure the Streamlit page
st.set_page_config(layout="wide", page_title="FitSync")

# Title of the dashboard
st.title("FitSync - Personal Health Analytics")

# Sidebar Configuration
st.sidebar.title("FitSync Dashboard")

# User Information
st.sidebar.write("User: Moksh")

# Sidebar filter
st.sidebar.header("Filter")
time_range = st.sidebar.selectbox(
    "Select Time Range",
    options=['Last 7 days', 'Last 30 days', 'All Time'],
    index=2
)

# Load and process data
df = process_data()

# Handle empty or None data early
if df is None or df.empty:
    st.warning("No data available. Please check your dataset.")
    st.stop()

# Ensure 'Date' is in datetime format
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# Drop rows where Date is invalid
df = df.dropna(subset=['Date'])

# Debugging: Show dataset date range
st.write("📊 Data available from:", df['Date'].min(), "to", df['Date'].max())

# 🔥 IMPORTANT FIX: Use dataset's latest date instead of today's date
current_date = df['Date'].max()

# Filter DataFrame based on selection
if time_range == 'Last 7 days':
    df = df[df['Date'] >= current_date - pd.Timedelta(days=7)]
elif time_range == 'Last 30 days':
    df = df[df['Date'] >= current_date - pd.Timedelta(days=30)]

# Debugging after filtering
if not df.empty:
    st.write("✅ Filtered data from:", df['Date'].min(), "to", df['Date'].max())
else:
    st.warning("⚠️ No data available for the selected time range.")

# Calculate necessary metrics
avg_steps = df['Steps'].mean() if not df.empty else 0
avg_sleep_hours = round(df['Sleep_Hour'].mean(), 1) if not df.empty else 0
avg_recovery_score = round(df['Recovery_Score'].mean(), 1) if not df.empty else 0

# Create a 3-column layout for metrics
col1, col2, col3 = st.columns(3)

# Display metrics
col1.metric(label="Average Steps", value=f"{avg_steps:.0f}")
col2.metric(label="Average Sleep Hours", value=f"{avg_sleep_hours:.1f}")
col3.metric(label="Average Recovery Score", value=f"{avg_recovery_score:.1f}")

# Display the processed data
st.write("Here is your processed health data:")
st.dataframe(df)