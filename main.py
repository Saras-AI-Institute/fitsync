import streamlit as st

# Default theme in session state if not set
if 'theme' not in st.session_state:
    st.session_state['theme'] = 'Light'

# Sidebar theme toggle
selected_theme = st.sidebar.radio("Select Theme", ("Light", "Dark"), index=0 if st.session_state['theme'] == 'Light' else 1)

# Update session state with the selected theme
st.session_state['theme'] = selected_theme

# Apply theme settings
if st.session_state['theme'] == "Dark":
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

# Example content for main page
st.title("Welcome to the Main Page")
st.write("This page serves as the entry point to the application.")
