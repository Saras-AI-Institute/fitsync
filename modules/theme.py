import streamlit as st
from typing import Optional


def init_theme(default: str = "light") -> None:
    """Ensure a theme key exists in `st.session_state` before any widget is created.

    Call this at the start of the app (before rendering the theme toggle widget).
    """
    if "theme" not in st.session_state:
        st.session_state["theme"] = default


def render_theme_toggle(key: str = "theme") -> None:
    """Render a single global theme toggle in the sidebar.

    Important: do NOT mutate `st.session_state[key]` after calling this widget.
    Streamlit will manage the session state value for the widget key.
    """
    # Ensure default exists so widget doesn't try to set an unexpected default later
    init_theme()
    
    # Determine current theme (normalize any existing value)
    current_theme = st.session_state.get("theme", "light").lower()
    theme_index = 0 if "light" in current_theme else 1
    
    st.sidebar.radio("🎨 Theme", ("☀️ Light", "🌙 Dark"), 
                     index=theme_index, 
                     key=key,
                     horizontal=False)


def _get_minimal_css(theme: str) -> str:
    """Return a small, stable set of CSS overrides for light/dark themes.

    Avoid fragile Streamlit internal class names; only target broad elements.
    """
    if theme == "dark":
        return """
        <style>
        /* Dark theme */
        body, html { background-color: #0b1220 !important; color: #e6eef8 !important; }
        .stApp { background-color: #0b1220 !important; color: #e6eef8 !important; }
        main { background-color: #0b1220 !important; color: #e6eef8 !important; }
        .block-container { background-color: #0b1220 !important; color: #e6eef8 !important; }
        
        /* Sidebar - aggressive targeting */
        [data-testid="stSidebar"] { background-color: #0d1628 !important; }
        [data-testid="stSidebar"] > div { background-color: #0d1628 !important; }
        .stSidebar { background-color: #0d1628 !important; }
        .sidebar { background-color: #0d1628 !important; }
        aside { background-color: #0d1628 !important; }
        
        /* All sidebar text - VERY aggressive */
        [data-testid="stSidebar"] { color: #e6eef8 !important; }
        [data-testid="stSidebar"] * { color: #e6eef8 !important; }
        [data-testid="stSidebar"] p { color: #e6eef8 !important; }
        [data-testid="stSidebar"] span { color: #e6eef8 !important; }
        [data-testid="stSidebar"] h1, [data-testid="stSidebar"] h2, [data-testid="stSidebar"] h3, 
        [data-testid="stSidebar"] h4, [data-testid="stSidebar"] h5, [data-testid="stSidebar"] h6 { color: #e6eef8 !important; }
        [data-testid="stSidebar"] label { color: #e6eef8 !important; }
        [data-testid="stSidebar"] .stRadio label { color: #e6eef8 !important; }
        [data-testid="stSidebar"] .stSelectbox label { color: #e6eef8 !important; }
        [data-testid="stSidebar"] .stText { color: #e6eef8 !important; }
        [data-testid="stSidebar"] .stMarkdown { color: #e6eef8 !important; }
        [data-testid="stSidebar"] .stMarkdown p { color: #e6eef8 !important; }
        [data-testid="stSidebar"] .stMarkdown span { color: #e6eef8 !important; }
        
        /* Main content text */
        body { color: #e6eef8 !important; }
        p { color: #e6eef8 !important; }
        span { color: #e6eef8 !important; }
        h1, h2, h3, h4, h5, h6 { color: #e6eef8 !important; font-family: "Georgia", "Garamond", serif !important; font-weight: 600 !important; }
        
        /* Metric cards */
        .stMetric { background-color: #0f1725 !important; color: #e6eef8 !important; }
        .stMetric * { color: #e6eef8 !important; }
        .stDataFrame { background-color: #0f1725 !important; color: #e6eef8 !important; }
        
        /* Tables - Dark mode with blur effect */
        table { background-color: #0a0f1a !important; color: #e6eef8 !important; backdrop-filter: blur(10px) !important; }
        table thead { background-color: #0d1628 !important; color: #e6eef8 !important; }
        table tbody { background-color: #0a0f1a !important; color: #e6eef8 !important; }
        table tr { background-color: #0a0f1a !important; }
        table th { background-color: #0d1628 !important; color: #e6eef8 !important; }
        table td { color: #e6eef8 !important; border-color: #1a2540 !important; }
        [role="table"] { background-color: #0a0f1a !important; }
        
        /* Links */
        a { color: #9fd3ff !important; }
        </style>
        """

    # Light theme - Cream color
    return """
    <style>
    /* Light theme - Cream color */
    body, html { background-color: #FFF5E1 !important; color: #111111 !important; }
    .stApp { background-color: #FFF5E1 !important; color: #111111 !important; }
    main { background-color: #FFF5E1 !important; color: #111111 !important; }
    .block-container { background-color: #FFF5E1 !important; color: #111111 !important; }
    
    /* Sidebar - cream with lighter tone */
    [data-testid="stSidebar"] { background-color: #FFFBF0 !important; }
    [data-testid="stSidebar"] > div { background-color: #FFFBF0 !important; }
    .stSidebar { background-color: #FFFBF0 !important; }
    .sidebar { background-color: #FFFBF0 !important; }
    aside { background-color: #FFFBF0 !important; }
    
    /* All sidebar text */
    [data-testid="stSidebar"] { color: #111111 !important; }
    [data-testid="stSidebar"] * { color: #111111 !important; }
    [data-testid="stSidebar"] p { color: #111111 !important; }
    [data-testid="stSidebar"] span { color: #111111 !important; }
    [data-testid="stSidebar"] h1, [data-testid="stSidebar"] h2, [data-testid="stSidebar"] h3, 
    [data-testid="stSidebar"] h4, [data-testid="stSidebar"] h5, [data-testid="stSidebar"] h6 { color: #111111 !important; }
    [data-testid="stSidebar"] label { color: #111111 !important; }
    [data-testid="stSidebar"] .stRadio label { color: #111111 !important; }
    [data-testid="stSidebar"] .stSelectbox label { color: #111111 !important; }
    [data-testid="stSidebar"] .stText { color: #111111 !important; }
    [data-testid="stSidebar"] .stMarkdown { color: #111111 !important; }
    [data-testid="stSidebar"] .stMarkdown p { color: #111111 !important; }
    [data-testid="stSidebar"] .stMarkdown span { color: #111111 !important; }
    
    /* Main content text */
    body { color: #111111 !important; }
    p { color: #111111 !important; }
    span { color: #111111 !important; }
    h1, h2, h3, h4, h5, h6 { color: #111111 !important; font-family: "Georgia", "Garamond", serif !important; font-weight: 600 !important; }
    
    /* Metric cards - cream base */
    .stMetric { background-color: #FFFBF0 !important; color: #111111 !important; }
    .stMetric * { color: #111111 !important; }
    .stDataFrame { background-color: #FFFBF0 !important; color: #111111 !important; }
    
    /* Tables - Cream background for light mode */
    table { background-color: #FFFBF0 !important; color: #111111 !important; }
    table thead { background-color: #FFF5E1 !important; color: #111111 !important; }
    table tbody { background-color: #FFFBF0 !important; color: #111111 !important; }
    table tr { background-color: #FFFBF0 !important; }
    table th { background-color: #FFF5E1 !important; color: #111111 !important; }
    table td { color: #111111 !important; border-color: #f0e6d2 !important; }
    [role="table"] { background-color: #FFFBF0 !important; }
    
    /* Links */
    a { color: #007BFF !important; }
    </style>
    """


def apply_theme(theme: Optional[str] = None) -> None:
    """Apply minimal CSS based on `st.session_state['theme']`.

    Use sparingly — prefer Streamlit native theming via .streamlit/config.toml.
    """
    if theme is None:
        theme = st.session_state.get("theme", "light")
    
    # Normalize theme value (extract lowercase word from emoji labels like "☀️ Light")
    theme_normalized = theme.lower()
    if "light" in theme_normalized:
        theme_normalized = "light"
    elif "dark" in theme_normalized:
        theme_normalized = "dark"
    else:
        theme_normalized = "light"  # default to light
    
    css = _get_minimal_css(theme_normalized)
    st.markdown(css, unsafe_allow_html=True)


def style_plotly_chart(fig):
    """Apply consistent Plotly styling based on the active app theme.

    Returns the same figure object after updating layout values.
    """
    current_theme = str(st.session_state.get("theme", "light")).lower()
    is_dark = "dark" in current_theme

    if is_dark:
        fig.update_layout(
            template="plotly_dark",
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            font=dict(color="#e6eef8"),
            legend=dict(font=dict(color="#e6eef8")),
            margin=dict(l=20, r=20, t=55, b=20),
            hovermode="x unified",
        )
        fig.update_xaxes(gridcolor="rgba(230, 238, 248, 0.15)", zerolinecolor="rgba(230, 238, 248, 0.2)")
        fig.update_yaxes(gridcolor="rgba(230, 238, 248, 0.15)", zerolinecolor="rgba(230, 238, 248, 0.2)")
    else:
        fig.update_layout(
            template="plotly_white",
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(255,255,255,0.65)",
            font=dict(color="#111111"),
            legend=dict(font=dict(color="#111111")),
            margin=dict(l=20, r=20, t=55, b=20),
            hovermode="x unified",
        )
        fig.update_xaxes(gridcolor="rgba(17, 17, 17, 0.08)", zerolinecolor="rgba(17, 17, 17, 0.15)")
        fig.update_yaxes(gridcolor="rgba(17, 17, 17, 0.08)", zerolinecolor="rgba(17, 17, 17, 0.15)")

    return fig


# Backwards-compatible alias (previous code used render_theme_selector)
render_theme_selector = render_theme_toggle
