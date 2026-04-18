import streamlit as st
from modules.processor import process_data
import pandas as pd
import plotly.express as px

# Configure the Streamlit page
st.set_page_config(layout="wide", page_title="FitSync")

# Add theme toggle button
theme = st.sidebar.radio("Select Theme", ("Light", "Dark"))

# Apply theme settings
if theme == "Dark":
    st.markdown(
        """
        <style>
        body {background-color: #333; color: #fff}
        .css-1cpxqw2 {background-color: #2e2e2e !important} /* Sidebar */
        .css-1cpxqw2 .css-1vencpc, .css-1cpxqw2 .css-1v3fvcr {color: #ddd !important} /* Text in Sidebar and Inputs */
        </style>
        """,
        unsafe_allow_html=True
    )
else:
    st.markdown(
        """
        <style>
        body {background-color: #fff; color: #000}
        .css-1cpxqw2 {background-color: #f4f4f4 !important} /* Sidebar */
        .css-1cpxqw2 .css-1vencpc, .css-1cpxqw2 .css-1v3fvcr {color: #333 !important} /* Text in Sidebar and Inputs */
        </style>
        """,
        unsafe_allow_html=True
    )

# Title of the dashboard
st.title("FitSync - Personal Health Analytics")

# Sidebar Configuration
st.sidebar.title("FitSync Dashboard")

# User Information
st.sidebar.text("User: Moksh")

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

# Create dual line chart for Recovery Score and Sleep Hours
def create_dual_line_chart(data):
    fig = px.line(data, x='Date', y=['Recovery_Score', 'Sleep_Hour'],
                  title='Recovery Score & Sleep Trend',
                  labels={'value': 'Score/Hours', 'variable': 'Metric'})
    return fig

# Create scatter plot for Recovery Score vs Steps colored by Sleep Hours
def create_scatter_plot(data):
    fig = px.scatter(data, x='Steps', y='Recovery_Score', color='Sleep_Hour',
                     title='Recovery Score vs Daily Steps',
                     labels={'x': 'Daily Steps', 'y': 'Recovery Score'})
    return fig

# Create scatter plot for Recovery Score vs Heart Rate
def create_scatter_plot_hr(data):
    fig = px.scatter(data, x='Heart_Rate_bpm', y='Recovery_Score',
                     title='Recovery Score vs Heart Rate',
                     labels={'x': 'Heart Rate (bpm)', 'y': 'Recovery Score'})
    return fig

# Create line chart for Calories Burned
def create_line_chart_calories(data):
    fig = px.line(data, x='Date', y='calories_burned',
                  title='Daily Calories Burned Trend',
                  labels={'y': 'Calories Burned'})
    return fig

# Define layout for dual charts
dual_col1, dual_col2 = st.columns(2)
with dual_col1:
    st.plotly_chart(create_dual_line_chart(df), use_container_width=True)
with dual_col2:
    st.plotly_chart(create_scatter_plot(df), use_container_width=True)

# Define layout for scatter plots
scatter_col1, scatter_col2 = st.columns(2)
with scatter_col1:
    st.plotly_chart(create_scatter_plot_hr(df), use_container_width=True)
with scatter_col2:
    st.plotly_chart(create_line_chart_calories(df), use_container_width=True)

# Create scatter plot for Recovery Score vs Steps colored by Sleep Hours
def create_scatter_plot(data):
    fig = px.scatter(data, x='Steps', y='Recovery_Score', color='Sleep_Hour',
                     title='Recovery Score vs Daily Steps',
                     labels={'x': 'Daily Steps', 'y': 'Recovery Score'})
    return fig

# Create scatter plot for Recovery Score vs Heart Rate
def create_scatter_plot_hr(data):
    fig = px.scatter(data, x='Heart_Rate_bpm', y='Recovery_Score',
                     title='Recovery Score vs Heart Rate',
                     labels={'x': 'Heart Rate (bpm)', 'y': 'Recovery Score'})
    return fig

# Create line chart for Calories Burned
def create_line_chart_calories(data):
    fig = px.line(data, x='Date', y='calories_burned',
                  title='Daily Calories Burned Trend',
                  labels={'y': 'Calories Burned'})
    return fig

# Define layout for dual charts
dual_col1, dual_col2 = st.columns(2)
with dual_col1:
    st.plotly_chart(create_dual_line_chart(df), use_container_width=True)
with dual_col2:
    st.plotly_chart(create_scatter_plot(df), use_container_width=True)

# Define layout for scatter plots
scatter_col1, scatter_col2 = st.columns(2)
with scatter_col1:
    st.plotly_chart(create_scatter_plot_hr(df), use_container_width=True)
with scatter_col2:
    st.plotly_chart(create_line_chart_calories(df), use_container_width=True)

import streamlit as st
from modules.processor import process_data
import pandas as pd
import plotly.express as px

# Configure the Streamlit page
st.set_page_config(layout="wide", page_title="FitSync")

# Default theme to light mode if not set
if 'theme' not in st.session_state:
    st.session_state['theme'] = 'Light'

# Sidebar theme toggle for user
selected_theme = st.sidebar.radio("Select Theme", ("Light", "Dark"), index=0 if st.session_state['theme'] == 'Light' else 1)

# Update the session state with the selected theme
st.session_state['theme'] = selected_theme

# Apply consistent light theme
if st.session_state['theme'] == "Dark":
    # Dark mode styles are similar to before
    st.markdown(
        """
        <style>
        body {background-color: #333; color: #fff}
        .css-1cpxqw2 {background-color: #2e2e2e !important} /* Sidebar */
        .css-1cpxqw2 .css-1vencpc, .css-1cpxqw2 .css-1v3fvcr {color: #ddd !important} /* Text in Sidebar and Inputs */
        </style>
        """,
        unsafe_allow_html=True
    )
else:
    # Light mode styles
    st.markdown(
        """
        <style>
        body {background-color: #f9f9f9; color: #333}
        .css-1cpxqw2 {background-color: #ffffff !important} /* Sidebar */
        .css-1cpxqw2 .css-1vencpc, .css-1cpxqw2 .css-1v3fvcr {color: #333 !important} /* Text in Sidebar and Inputs */
        .css-1vq4p4l, .css-1pwf07v, .css-1ophc2l, .css-gg4vpm {background-color: #fff; box-shadow: 0 0 10px rgba(0,0,0,0.1);} /* Items */
        button {background-color: #007BFF; color: #fff; font-size: .875rem; padding: .5rem 1rem; border-radius: .25rem; border: none;}
        </style>
        """,
        unsafe_allow_html=True
    )

# Title of the dashboard
st.title("FitSync - Personal Health Analytics")