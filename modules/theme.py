import streamlit as st
from typing import Optional


def init_theme(default: str = "light") -> None:
    """Initialize theme from query params, session state, or default.

    Call this at the start of the app (before rendering the theme toggle widget).
    """
    # Check URL query params first (persists across page navigation)
    query_params = st.query_params
    if "theme" in query_params:
        theme_value = query_params["theme"]
        if theme_value in ["light", "dark"]:
            st.session_state["theme"] = theme_value
            return
    
    # Fall back to session state
    if "theme" not in st.session_state:
        st.session_state["theme"] = default


def render_theme_toggle(key: str = "theme") -> None:
    """Render a toggle button in the sidebar with persistent state.

    Uses URL query parameters to maintain theme across page navigation.
    """
    # Ensure default exists
    init_theme()
    
    # Get current theme
    current_theme = st.session_state.get("theme", "light").lower()
    is_dark = "dark" in current_theme
    
    # Add toggle styling
    st.sidebar.markdown("""
    <style>
    .toggle-container {
        display: flex;
        align-items: center;
        gap: 15px;
        margin: 20px 0;
        padding: 15px;
        background: linear-gradient(135deg, rgba(102, 126, 234, 0.1), rgba(240, 147, 251, 0.1));
        border-radius: 15px;
        border: 2px solid rgba(102, 126, 234, 0.2);
    }
    
    .toggle-label {
        font-weight: 700;
        font-size: 15px;
        margin: 0;
    }
    
    .toggle-switch {
        position: relative;
        display: inline-block;
        width: 60px;
        height: 34px;
        cursor: pointer;
    }
    
    .toggle-switch input {
        opacity: 0;
        width: 0;
        height: 0;
    }
    
    .toggle-slider {
        position: absolute;
        cursor: pointer;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background-color: #ccc;
        transition: 0.4s;
        border-radius: 34px;
        box-shadow: inset 0 2px 4px rgba(0,0,0,0.2);
    }
    
    .toggle-slider:before {
        position: absolute;
        content: "";
        height: 26px;
        width: 26px;
        left: 4px;
        bottom: 4px;
        background-color: white;
        transition: 0.4s;
        border-radius: 50%;
        box-shadow: 0 2px 4px rgba(0,0,0,0.2);
    }
    
    input:checked + .toggle-slider {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    
    input:checked + .toggle-slider:before {
        transform: translateX(26px);
    }
    
    .icon-sun {
        font-size: 20px;
    }
    
    .icon-moon {
        font-size: 20px;
    }
    
    /* Animation for toggle button */
    @keyframes toggleSlide {
        0% {
            transform: scaleX(0.9);
            opacity: 0.7;
        }
        50% {
            transform: scaleX(1.05);
        }
        100% {
            transform: scaleX(1);
            opacity: 1;
        }
    }
    
    @keyframes togglePulse {
        0% {
            box-shadow: 0 0 0 0 rgba(102, 126, 234, 0.7);
        }
        70% {
            box-shadow: 0 0 0 10px rgba(102, 126, 234, 0);
        }
        100% {
            box-shadow: 0 0 0 0 rgba(102, 126, 234, 0);
        }
    }
    
    /* Animated button container */
    button[kind="secondary"] {
        animation: toggleSlide 0.5s ease-in-out !important;
    }
    
    /* Icon animations */
    .icon-sun {
        animation: spinRotate 0.6s ease-in-out;
    }
    
    .icon-moon {
        animation: spinRotate 0.6s ease-in-out;
    }
    
    @keyframes spinRotate {
        0% {
            transform: rotate(0deg) scale(0.8);
            opacity: 0;
        }
        50% {
            transform: rotate(180deg) scale(1.1);
        }
        100% {
            transform: rotate(360deg) scale(1);
            opacity: 1;
        }
    }
    
    @keyframes slideIn {
        from {
            transform: translateX(-20px);
            opacity: 0;
        }
        to {
            transform: translateX(0);
            opacity: 1;
        }
    }
    
    @keyframes slideOut {
        from {
            transform: translateX(0);
            opacity: 1;
        }
        to {
            transform: translateX(20px);
            opacity: 0;
        }
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Create columns for better layout
    col1, col2, col3 = st.sidebar.columns([0.8, 1.5, 1])
    
    with col1:
        st.markdown("""
        <div style="animation: slideIn 0.6s ease-out; font-size: 24px; display: flex; align-items: center; justify-content: center; height: 40px;">
            ☀️
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        # Create a toggle button using columns and buttons
        if st.button(
            label="🌙" if is_dark else "☀️",
            key=f"{key}_toggle",
            use_container_width=True,
            help="Toggle between light and dark mode"
        ):
            # Switch theme
            new_theme = "light" if is_dark else "dark"
            st.session_state["theme"] = new_theme
            st.query_params["theme"] = new_theme
            st.rerun()
    
    with col3:
        st.markdown("""
        <div style="animation: slideIn 0.6s ease-out; font-size: 24px; display: flex; align-items: center; justify-content: center; height: 40px;">
            🌙
        </div>
        """, unsafe_allow_html=True)


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
        
        /* Tables - Dark blue background for dark mode */
        table { background-color: #0f1725 !important; color: #e6eef8 !important; }
        table thead { background-color: #0d1628 !important; color: #e6eef8 !important; border-bottom: 2px solid #1a2540 !important; }
        table tbody { background-color: #0f1725 !important; color: #e6eef8 !important; }
        table tbody tr { background-color: #0f1725 !important; }
        table tbody tr:hover { background-color: #1a2540 !important; }
        table tr { background-color: #0f1725 !important; }
        table th { background-color: #0d1628 !important; color: #e6eef8 !important; padding: 12px !important; font-weight: 700 !important; }
        table td { color: #e6eef8 !important; border-color: #1a2540 !important; padding: 10px 12px !important; }
        [role="table"] { background-color: #0f1725 !important; }
        
        /* Streamlit dataframe styling */
        .stDataFrame [data-testid="stDataFrame"] { background-color: #0f1725 !important; }
        .stDataFrame table { background-color: #0f1725 !important; }
        
        /* Aggressive dataframe targeting */
        [data-testid="stDataFrame"] { background-color: #0f1725 !important; }
        [data-testid="stDataFrame"] table { background-color: #0f1725 !important; }
        [data-testid="stDataFrame"] thead { background-color: #0d1628 !important; }
        [data-testid="stDataFrame"] tbody { background-color: #0f1725 !important; }
        [data-testid="stDataFrame"] tr { background-color: #0f1725 !important; }
        [data-testid="stDataFrame"] th { background-color: #0d1628 !important; color: #e6eef8 !important; }
        [data-testid="stDataFrame"] td { background-color: #0f1725 !important; color: #e6eef8 !important; }
        
        /* Arrow table styling */
        .stArrowTable table { background-color: #0f1725 !important; }
        .stArrowTable tbody tr { background-color: #0f1725 !important; }
        .stArrowTable tbody tr:nth-child(odd) { background-color: #0f1725 !important; }
        .stArrowTable tbody tr:nth-child(even) { background-color: #0f1725 !important; }
        .stArrowTable tbody tr:hover { background-color: #1a2540 !important; }
        
        /* Hero section and containers - dark mode */
        .hero-section {
            background: linear-gradient(135deg, #1a2540 0%, #0d1628 50%, #0f1725 100%) !important;
            color: #e6eef8 !important;
        }
        
        .hero-title, .hero-subtitle, .hero-description {
            color: #e6eef8 !important;
        }
        
        .hero-title {
            background: linear-gradient(45deg, #e6eef8, #b0c4ff) !important;
            -webkit-background-clip: text !important;
            -webkit-text-fill-color: transparent !important;
            background-clip: text !important;
        }
        
        /* Section titles */
        .section-title {
            background: linear-gradient(90deg, #667eea, #e6eef8, #4facfe) !important;
            -webkit-background-clip: text !important;
            -webkit-text-fill-color: transparent !important;
            background-clip: text !important;
        }
        
        /* Feature cards dark mode */
        .feature-card {
            background: linear-gradient(135deg, #0f1725 0%, #1a2540 100%) !important;
            color: #e6eef8 !important;
        }
        
        .feature-title {
            color: #e6eef8 !important;
        }
        
        .feature-description {
            color: #b0c4ff !important;
        }
        
        /* Highlight items dark mode */
        .highlight-item {
            background: linear-gradient(135deg, rgba(102, 126, 234, 0.2) 0%, rgba(15, 23, 37, 0.8) 100%) !important;
        }
        
        .highlight-text {
            color: #e6eef8 !important;
        }
        
        /* Divider dark mode */
        .divider {
            background: linear-gradient(90deg, transparent, #667eea 20%, #764ba2 50%, #4facfe 80%, transparent) !important;
        }
        
        /* Button animation for dark mode */
        button {
            transition: all 0.4s cubic-bezier(0.68, -0.55, 0.265, 1.55) !important;
        }
        
        button:active, button:focus {
            transform: scale(0.98) !important;
            animation: buttonShift 0.6s ease-in-out !important;
        }
        
        @keyframes buttonShift {
            0% { transform: scale(0.95) translateY(0); }
            50% { transform: scale(1.05) translateY(-2px); }
            100% { transform: scale(1) translateY(0); }
        }
        
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
    
    /* Tables - Light cream background for light mode */
    table { background-color: #FFFBF0 !important; color: #111111 !important; }
    table thead { background-color: #FFF5E1 !important; color: #111111 !important; border-bottom: 2px solid #f0e6d2 !important; }
    table tbody { background-color: #FFFBF0 !important; color: #111111 !important; }
    table tbody tr { background-color: #FFFBF0 !important; }
    table tbody tr:hover { background-color: #FFF5E1 !important; }
    table tr { background-color: #FFFBF0 !important; }
    table th { background-color: #FFF5E1 !important; color: #111111 !important; padding: 12px !important; font-weight: 700 !important; }
    table td { color: #111111 !important; border-color: #f0e6d2 !important; padding: 10px 12px !important; }
    [role="table"] { background-color: #FFFBF0 !important; }
    
    /* Streamlit dataframe styling */
    .stDataFrame [data-testid="stDataFrame"] { background-color: #FFFBF0 !important; }
    .stDataFrame table { background-color: #FFFBF0 !important; }
    
    /* Aggressive dataframe targeting */
    [data-testid="stDataFrame"] { background-color: #FFFBF0 !important; }
    [data-testid="stDataFrame"] table { background-color: #FFFBF0 !important; }
    [data-testid="stDataFrame"] thead { background-color: #FFF5E1 !important; }
    [data-testid="stDataFrame"] tbody { background-color: #FFFBF0 !important; }
    [data-testid="stDataFrame"] tr { background-color: #FFFBF0 !important; }
    [data-testid="stDataFrame"] th { background-color: #FFF5E1 !important; color: #111111 !important; }
    [data-testid="stDataFrame"] td { background-color: #FFFBF0 !important; color: #111111 !important; }
    
    /* Arrow table styling */
    .stArrowTable table { background-color: #FFFBF0 !important; }
    .stArrowTable tbody tr { background-color: #FFFBF0 !important; }
    .stArrowTable tbody tr:nth-child(odd) { background-color: #FFFBF0 !important; }
    .stArrowTable tbody tr:nth-child(even) { background-color: #FFFBF0 !important; }
    .stArrowTable tbody tr:hover { background-color: #FFF5E1 !important; }
    
    /* Hero section and containers - light mode */
    .hero-section {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 40%, #4CAF50 70%, #FF9800 100%) !important;
        color: #ffffff !important;
    }
    
    .hero-title, .hero-subtitle, .hero-description {
        color: #ffffff !important;
    }
    
    .hero-title {
        background: linear-gradient(45deg, #ffffff, #f0f0f0) !important;
        -webkit-background-clip: text !important;
        -webkit-text-fill-color: transparent !important;
        background-clip: text !important;
    }
    
    /* Section titles */
    .section-title {
        background: linear-gradient(90deg, #667eea, #4CAF50, #FF9800) !important;
        -webkit-background-clip: text !important;
        -webkit-text-fill-color: transparent !important;
        background-clip: text !important;
    }
    
    /* Feature cards light mode */
    .feature-card {
        background: linear-gradient(135deg, #ffffff 0%, #f8f9ff 100%) !important;
        color: #111111 !important;
    }
    
    .feature-title {
        color: #111111 !important;
    }
    
    .feature-description {
        color: #555555 !important;
    }
    
    /* Highlight items light mode */
    .highlight-item {
        background: linear-gradient(135deg, rgba(102, 126, 234, 0.1) 0%, rgba(240, 147, 251, 0.1) 100%) !important;
    }
    
    .highlight-text {
        color: #333333 !important;
    }
    
    /* Divider light mode */
    .divider {
        background: linear-gradient(90deg, transparent, #667eea 20%, #f093fb 50%, #4facfe 80%, transparent) !important;
    }
    
    /* Button animation for light mode */
    button {
        transition: all 0.4s cubic-bezier(0.68, -0.55, 0.265, 1.55) !important;
    }
    
    button:active, button:focus {
        transform: scale(0.98) !important;
        animation: buttonShift 0.6s ease-in-out !important;
    }
    
    @keyframes buttonShift {
        0% { transform: scale(0.95) translateY(0); }
        50% { transform: scale(1.05) translateY(-2px); }
        100% { transform: scale(1) translateY(0); }
    }
    
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


# Backwards-compatible alias (previous code used render_theme_selector)
render_theme_selector = render_theme_toggle


def style_plotly_chart(fig, theme: Optional[str] = None):
    """Apply theme styling to Plotly figures.
    
    Updates figure layout with appropriate colors based on light/dark theme.
    """
    if theme is None:
        theme = st.session_state.get("theme", "light")
    
    # Normalize theme value
    theme_normalized = theme.lower()
    if "light" in theme_normalized:
        theme_normalized = "light"
    elif "dark" in theme_normalized:
        theme_normalized = "dark"
    else:
        theme_normalized = "light"
    
    if theme_normalized == "dark":
        # Dark mode - dark blue background
        fig.update_layout(
            template="plotly_dark",
            plot_bgcolor="#0f1725",
            paper_bgcolor="#0b1220",
            font=dict(color="#e6eef8", family="Georgia, Garamond, serif"),
            title_font=dict(size=18, color="#e6eef8"),
            xaxis=dict(
                gridcolor="#1a2540",
                zerolinecolor="#1a2540",
                linecolor="#1a2540"
            ),
            yaxis=dict(
                gridcolor="#1a2540",
                zerolinecolor="#1a2540",
                linecolor="#1a2540"
            ),
            legend=dict(
                bgcolor="rgba(15, 23, 37, 0.8)",
                bordercolor="#1a2540",
                font=dict(color="#e6eef8")
            ),
            hovermode="closest"
        )
    else:
        # Light mode - light background
        fig.update_layout(
            template="plotly",
            plot_bgcolor="#FFFBF0",
            paper_bgcolor="#FFF5E1",
            font=dict(color="#111111", family="Georgia, Garamond, serif"),
            title_font=dict(size=18, color="#111111"),
            xaxis=dict(
                gridcolor="#f0e6d2",
                zerolinecolor="#f0e6d2",
                linecolor="#f0e6d2"
            ),
            yaxis=dict(
                gridcolor="#f0e6d2",
                zerolinecolor="#f0e6d2",
                linecolor="#f0e6d2"
            ),
            legend=dict(
                bgcolor="rgba(255, 251, 240, 0.9)",
                bordercolor="#f0e6d2",
                font=dict(color="#111111")
            ),
            hovermode="closest"
        )
    
    return fig
