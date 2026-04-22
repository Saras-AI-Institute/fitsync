import streamlit as st
from modules.processor import process_data
import pandas as pd
import plotly.express as px
from modules import theme

# Configure the Streamlit page
st.set_page_config(layout="wide", page_title="FitSync")

# Initialize and apply centralized theme (shared key 'theme')
theme.init_theme()
theme.render_theme_toggle()
theme.apply_theme()

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

# Add custom CSS for colored metric cards
st.markdown("""
<style>
.metric-green { background: linear-gradient(135deg, #4CAF50 0%, #45a049 100%); border-radius: 10px; padding: 20px; color: white; text-align: center; }
.metric-blue { background: linear-gradient(135deg, #2196F3 0%, #1976D2 100%); border-radius: 10px; padding: 20px; color: white; text-align: center; }
.metric-orange { background: linear-gradient(135deg, #FF9800 0%, #F57C00 100%); border-radius: 10px; padding: 20px; color: white; text-align: center; }
.metric-label { font-size: 14px; font-weight: 600; opacity: 0.9; margin-bottom: 8px; }
.metric-value { font-size: 32px; font-weight: bold; }
</style>
""", unsafe_allow_html=True)

# Display metrics with custom colors
with col1:
    st.markdown(f"""
    <div class="metric-green">
        <div class="metric-label">🚶 Average Steps</div>
        <div class="metric-value">{avg_steps:.0f}</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="metric-blue">
        <div class="metric-label">😴 Average Sleep Hours</div>
        <div class="metric-value">{avg_sleep_hours:.1f}</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="metric-orange">
        <div class="metric-label">💪 Average Recovery Score</div>
        <div class="metric-value">{avg_recovery_score:.1f}</div>
    </div>
    """, unsafe_allow_html=True)

# Display the processed data
st.write("Here is your processed health data:")
st.dataframe(df)

# Create dual line chart for Recovery Score and Sleep Hours
def create_dual_line_chart(data):
    fig = px.line(data, x='Date', y=['Recovery_Score', 'Sleep_Hour'],
                  title='Recovery Score & Sleep Trend',
                  labels={'value': 'Score/Hours', 'variable': 'Metric'})
    return theme.style_plotly_chart(fig)

# Create scatter plot for Recovery Score vs Steps colored by Sleep Hours
def create_scatter_plot(data):
    fig = px.scatter(data, x='Steps', y='Recovery_Score', color='Sleep_Hour',
                     title='Recovery Score vs Daily Steps',
                     labels={'x': 'Daily Steps', 'y': 'Recovery Score'})
    return theme.style_plotly_chart(fig)

# Create scatter plot for Recovery Score vs Heart Rate
def create_scatter_plot_hr(data):
    fig = px.scatter(data, x='Heart_Rate_bpm', y='Recovery_Score',
                     title='Recovery Score vs Heart Rate',
                     labels={'x': 'Heart Rate (bpm)', 'y': 'Recovery Score'})
    return theme.style_plotly_chart(fig)

# Create line chart for Calories Burned
def create_line_chart_calories(data):
    fig = px.line(data, x='Date', y='calories_burned',
                  title='Daily Calories Burned Trend',
                  labels={'y': 'Calories Burned'})
    return theme.style_plotly_chart(fig)

# Define layout for dual charts
dual_col1, dual_col2 = st.columns(2)
with dual_col1:
    st.plotly_chart(create_dual_line_chart(df), use_container_width=True, key='dual_line_1')
with dual_col2:
    st.plotly_chart(create_scatter_plot(df), use_container_width=True, key='scatter_steps_1')

# Define layout for scatter plots
scatter_col1, scatter_col2 = st.columns(2)
with scatter_col1:
    st.plotly_chart(create_scatter_plot_hr(df), use_container_width=True, key='scatter_hr_1')
with scatter_col2:
    st.plotly_chart(create_line_chart_calories(df), use_container_width=True, key='calories_1')

