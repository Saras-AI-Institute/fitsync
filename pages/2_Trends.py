import streamlit as st
from modules.processor import process_data
import pandas as pd
import plotly.express as px

# Configure the Streamlit page
st.set_page_config(layout="wide", page_title="FitSync")

from modules import theme


@st.cache_data(show_spinner=False)
def get_processed_data():
    """Cache processed health data to avoid recomputing on every rerun."""
    return process_data()

# Initialize and apply centralized theme (shared key 'theme')
theme.init_theme()
theme.render_theme_toggle()
theme.apply_theme()

# Title of the dashboard
st.title("FitSync - Personal Health Analytics")
# Load and process data
df = get_processed_data().copy()

# Handle empty or None data early
if df is None or df.empty:
    st.warning("No data available. Please check your dataset.")
    st.stop()

# Ensure 'Date' is in datetime format
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# Sidebar Configuration
st.sidebar.title("Trends & Insights Dashboard")

# Sidebar filter
st.sidebar.header("Filter")
time_range = st.sidebar.selectbox(
    "Select Time Range",
    options=['Last 7 days', 'Last 30 days', 'All Time'],
    index=2
)

# 🔥 IMPORTANT FIX: Use dataset's latest date instead of today's date
current_date = df['Date'].max()

# Filter DataFrame based on selection
if time_range == 'Last 7 days':
    filtered_df = df[df['Date'] >= current_date - pd.Timedelta(days=7)]
elif time_range == 'Last 30 days':
    filtered_df = df[df['Date'] >= current_date - pd.Timedelta(days=30)]
else:
    filtered_df = df

# Display summary statistics
st.header("Summary Statistics")
summary_stats = filtered_df[['Recovery_Score', 'Sleep_Hour', 'Steps', 'calories_burned']].agg(['mean', 'min', 'max'])
st.dataframe(summary_stats)

st.header("Monthly Average Recovery Score")
monthly_avg = filtered_df.resample('ME', on='Date').mean().reset_index()
fig_line = px.line(monthly_avg, x='Date', y='Recovery_Score',
                   title='Average Recovery Score by Month',
                   labels={'Recovery_Score': 'Average Recovery Score', 'Date': 'Month'})
fig_line = theme.style_plotly_chart(fig_line)
st.plotly_chart(fig_line, use_container_width=True, key='line_recovery')
st.header("Histograms of Key Metrics")
metrics = ['Steps', 'calories_burned', 'Recovery_Score', 'Sleep_Hour']
for metric in metrics:
    st.subheader(f"Distribution of {metric.replace('_', ' ').title()}")
    fig_hist = px.histogram(filtered_df, x=metric, nbins=30,
                            title=f"Distribution of {metric.replace('_', ' ').title()}")
    fig_hist = theme.style_plotly_chart(fig_hist)
    st.plotly_chart(fig_hist, use_container_width=True, key=f"hist_{metric}")

