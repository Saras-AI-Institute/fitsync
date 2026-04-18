import streamlit as st
from modules.processor import process_data
import pandas as pd
import plotly.express as px

# Configure the Streamlit page
st.set_page_config(layout="wide", page_title="FitSync")


# Default theme to light mode if not set

# Default theme to light mode if not set
if 'theme' not in st.session_state:

# Sidebar theme toggle for user



# Update the session state with the selected theme
selected_theme = st.sidebar.radio("Select Theme", ("Light", "Dark"), index=0 if st.session_state['theme'] == 'Light' else 1)


# Apply consistent light theme
# Update the session state with the selected theme
    # Dark mode styles are similar to before
st.session_state['theme'] = selected_theme


# Apply consistent light theme
if st.session_state['theme'] == "Dark":
    # Dark mode styles are similar to before
    st.markdown(
        """
        <style>
        body {background-color: #333; color: #fff}
        .css-1cpxqw2 {background-color: #2e2e2e !important} /* Sidebar */
    # Light mode styles
        .css-1cpxqw2 .css-1vencpc, .css-1cpxqw2 .css-1v3fvcr {color: #ddd !important} /* Text in Sidebar and Inputs */
        </style>
        """,


        body {background-color: #f9f9f9; color: #333}
        .css-1cpxqw2 {background-color: #ffffff !important} /* Sidebar */
else:
        .css-1vq4p4l, .css-1pwf07v, .css-1ophc2l, .css-gg4vpm {background-color: #fff; box-shadow: 0 0 10px rgba(0,0,0,0.1);} /* Items */
        button {background-color: #007BFF; color: #fff; font-size: .875rem; padding: .5rem 1rem; border-radius: .25rem; border: none;}
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
# Load and process data
df = process_data()

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
monthly_avg = filtered_df.resample('M', on='Date').mean().reset_index()
fig_line = px.line(monthly_avg, x='Date', y='Recovery_Score',
                   title='Average Recovery Score by Month',
                   labels={'Recovery_Score': 'Average Recovery Score', 'Date': 'Month'})
st.plotly_chart(fig_line, use_container_width=True)
st.header("Histograms of Key Metrics")
metrics = ['Steps', 'calories_burned', 'Recovery_Score', 'Sleep_Hour']
for metric in metrics:
    st.subheader(f"Distribution of {metric.replace('_', ' ').title()}")
    fig_hist = px.histogram(filtered_df, x=metric, nbins=30,
                            title=f"Distribution of {metric.replace('_', ' ').title()}")
    st.plotly_chart(fig_hist, use_container_width=True)
    st.plotly_chart(fig_hist, use_container_width=True)

