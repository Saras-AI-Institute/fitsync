import streamlit as st
from modules import theme

# Set page config
st.set_page_config(
    page_title="FitSync - Health Analytics",
    page_icon="🏃‍♂️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize theme and render shared selector
theme.init_theme()
theme.render_theme_toggle(key='theme')
theme.apply_theme()

# Premium styling for home page
st.markdown("""
<style>
/* Global Styles */
:root {
    --primary: #4CAF50;
    --primary-dark: #45a049;
    --secondary: #2196F3;
    --accent: #FF9800;
}

.hero-section {
    background: linear-gradient(135deg, #4CAF50 0%, #45a049 50%, #2196F3 100%);
    padding: 80px 40px;
    border-radius: 20px;
    color: white;
    text-align: center;
    margin-bottom: 50px;
    box-shadow: 0 8px 32px rgba(0,0,0,0.15);
    animation: slideIn 0.6s ease-out;
}

@keyframes slideIn {
    from {
        opacity: 0;
        transform: translateY(-20px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

.hero-icon {
    font-size: 64px;
    margin-bottom: 20px;
    animation: bounce 2s infinite;
}

@keyframes bounce {
    0%, 100% { transform: translateY(0); }
    50% { transform: translateY(-10px); }
}

.hero-title {
    font-size: 56px;
    font-weight: 900;
    margin-bottom: 15px;
    text-shadow: 3px 3px 6px rgba(0,0,0,0.3);
    letter-spacing: -1px;
    font-family: "Georgia", "Garamond", serif;
}

.hero-subtitle {
    font-size: 24px;
    opacity: 0.95;
    margin-bottom: 20px;
    font-weight: 300;
    letter-spacing: 0.5px;
}

.hero-description {
    font-size: 16px;
    opacity: 0.9;
    max-width: 700px;
    margin: 0 auto;
    line-height: 1.8;
}

.section-title {
    font-size: 36px;
    font-weight: 800;
    color: #4CAF50;
    margin: 50px 0 30px 0;
    padding-bottom: 15px;
    border-bottom: 3px solid #4CAF50;
    letter-spacing: -0.5px;
    font-family: "Georgia", "Garamond", serif;
}

.feature-card {
    background: linear-gradient(135deg, #FFF5E1 0%, #FFFBF0 100%);
    padding: 35px;
    border-radius: 15px;
    margin: 20px 0;
    box-shadow: 0 6px 20px rgba(0,0,0,0.08);
    border-left: 6px solid #4CAF50;
    transition: all 0.3s ease;
    animation: fadeIn 0.6s ease-out;
}

@keyframes fadeIn {
    from {
        opacity: 0;
        transform: translateY(10px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

.feature-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 12px 28px rgba(0,0,0,0.12);
    border-left-color: #2196F3;
}

.feature-icon {
    font-size: 40px;
    margin-bottom: 15px;
}

.feature-title {
    font-size: 22px;
    font-weight: 700;
    color: #111111;
    margin-bottom: 10px;
}

.feature-description {
    font-size: 15px;
    color: #555555;
    line-height: 1.7;
}

.flow-card {
    background: linear-gradient(135deg, #ffffff 0%, #f7fbff 100%);
    border: 1px solid rgba(33, 150, 243, 0.2);
    border-radius: 14px;
    padding: 24px;
    margin: 10px 0;
    box-shadow: 0 4px 14px rgba(0,0,0,0.06);
}

.flow-step {
    display: inline-block;
    background: #4CAF50;
    color: white;
    border-radius: 20px;
    font-size: 12px;
    font-weight: 700;
    padding: 6px 12px;
    margin-bottom: 12px;
}

.preview-shell {
    background: linear-gradient(145deg, #0f172a 0%, #1e293b 100%);
    border-radius: 18px;
    padding: 24px;
    margin: 10px 0 20px 0;
    box-shadow: 0 10px 30px rgba(0,0,0,0.2);
}

.preview-topbar {
    display: flex;
    gap: 8px;
    margin-bottom: 18px;
}

.preview-dot {
    width: 10px;
    height: 10px;
    border-radius: 50%;
}

.preview-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 12px;
}

.preview-card {
    background: rgba(255,255,255,0.08);
    border: 1px solid rgba(255,255,255,0.12);
    border-radius: 10px;
    padding: 14px;
    color: #e2e8f0;
    min-height: 70px;
}

.theme-panel {
    background: linear-gradient(135deg, rgba(76, 175, 80, 0.14) 0%, rgba(33, 150, 243, 0.14) 100%);
    border-radius: 16px;
    padding: 28px;
    border: 1px solid rgba(76, 175, 80, 0.25);
}

.stat-box {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    padding: 40px;
    border-radius: 15px;
    color: white;
    text-align: center;
    box-shadow: 0 6px 20px rgba(0,0,0,0.15);
    transition: all 0.3s ease;
    animation: fadeIn 0.6s ease-out;
}

.stat-box:nth-child(2) {
    background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
}

.stat-box:nth-child(3) {
    background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
}

.stat-number {
    font-size: 44px;
    font-weight: 900;
    margin-bottom: 10px;
}

.stat-label {
    font-size: 15px;
    opacity: 0.95;
    font-weight: 600;
}

.highlights {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 20px;
    margin: 40px 0;
}

.highlight-item {
    background: linear-gradient(135deg, rgba(76, 175, 80, 0.1) 0%, rgba(33, 150, 243, 0.1) 100%);
    padding: 25px;
    border-radius: 12px;
    text-align: center;
    border-top: 4px solid #4CAF50;
}

.highlight-number {
    font-size: 32px;
    font-weight: 900;
    color: #4CAF50;
    margin-bottom: 8px;
}

.highlight-text {
    font-size: 14px;
    color: #555555;
    font-weight: 600;
}

.divider {
    height: 3px;
    background: linear-gradient(90deg, transparent, #4CAF50, transparent);
    margin: 50px 0;
}

.footer {
    text-align: center;
    color: #888;
    font-size: 13px;
    margin-top: 50px;
    padding-top: 30px;
    border-top: 1px solid #e0e0e0;
}

.footer-text {
    margin: 5px 0;
}

@media (max-width: 768px) {
    .hero-title { font-size: 36px; }
    .hero-subtitle { font-size: 18px; }
    .section-title { font-size: 28px; }
    .highlights { grid-template-columns: 1fr; }
    .preview-grid { grid-template-columns: 1fr; }
    .stat-box { padding: 25px; }
}
</style>
""", unsafe_allow_html=True)

# Hero Section with premium styling
st.markdown("""
<div class="hero-section">
    <div class="hero-icon">🏃‍♂️</div>
    <div class="hero-title">FitSync</div>
    <div class="hero-subtitle">Your Personal Health Analytics Dashboard</div>
    <div class="hero-description">
        Unlock powerful insights into your fitness journey. Track recovery patterns, analyze health metrics, 
        and optimize your wellness routine with real-time data visualization and intelligent analytics.
    </div>
</div>
""", unsafe_allow_html=True)

# Features Section
st.markdown('<div class="section-title">🎯 Core Features</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">📊</div>
        <div class="feature-title">Comprehensive Dashboard</div>
        <div class="feature-description">
        View all your health metrics in one beautifully organized dashboard. 
        Real-time data visualization with interactive charts showing your steps, sleep hours, 
        and recovery scores at a glance.
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">📈</div>
        <div class="feature-title">Advanced Trends Analysis</div>
        <div class="feature-description">
        Deep dive into your health trends with detailed analytics. 
        Track monthly averages, view distributions, and gain comprehensive 
        statistical insights into your fitness patterns.
        </div>
    </div>
    """, unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">🤖</div>
        <div class="feature-title">Smart Recovery Score</div>
        <div class="feature-description">
        Advanced algorithm calculates your daily recovery score based on 
        sleep quality, heart rate variations, and daily activity levels. 
        Understand your body's recovery capacity.
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">🎨</div>
        <div class="feature-title">Dark/Light Theming</div>
        <div class="feature-description">
        Seamless light and dark theme switching that works across all pages. 
        Comfortable viewing experience day or night with automatic color-coded metrics.
        </div>
    </div>
    """, unsafe_allow_html=True)

# How It Works
st.markdown('<div class="section-title">⚙️ How It Works</div>', unsafe_allow_html=True)

flow_col1, flow_col2, flow_col3 = st.columns(3)

with flow_col1:
    st.markdown("""
    <div class="flow-card">
        <div class="flow-step">STEP 1</div>
        <h4 style="margin: 0 0 8px 0;">Data Processing</h4>
        <p style="margin: 0; color: #555;">FitSync reads your health CSV, handles missing values, and normalizes dates for reliable analysis.</p>
    </div>
    """, unsafe_allow_html=True)

with flow_col2:
    st.markdown("""
    <div class="flow-card">
        <div class="flow-step">STEP 2</div>
        <h4 style="margin: 0 0 8px 0;">Recovery Intelligence</h4>
        <p style="margin: 0; color: #555;">A weighted recovery score is computed from sleep duration, resting heart rate, and daily activity.</p>
    </div>
    """, unsafe_allow_html=True)

with flow_col3:
    st.markdown("""
    <div class="flow-card">
        <div class="flow-step">STEP 3</div>
        <h4 style="margin: 0 0 8px 0;">Insights & Action</h4>
        <p style="margin: 0; color: #555;">Interactive visuals reveal trends so you can plan recovery, training intensity, and consistency better.</p>
    </div>
    """, unsafe_allow_html=True)

# Dashboard Preview
st.markdown('<div class="section-title">🖥️ Dashboard Preview</div>', unsafe_allow_html=True)

st.markdown("""
<div class="preview-shell">
    <div class="preview-topbar">
        <span class="preview-dot" style="background:#ef4444;"></span>
        <span class="preview-dot" style="background:#f59e0b;"></span>
        <span class="preview-dot" style="background:#22c55e;"></span>
    </div>
    <div class="preview-grid">
        <div class="preview-card"><strong>Average Steps</strong><br>9,240</div>
        <div class="preview-card"><strong>Sleep Hours</strong><br>7.1 h</div>
        <div class="preview-card"><strong>Recovery Score</strong><br>78 / 100</div>
        <div class="preview-card"><strong>Trend View</strong><br>Recovery vs Sleep</div>
        <div class="preview-card"><strong>Distribution</strong><br>Activity Histogram</div>
        <div class="preview-card"><strong>Insights</strong><br>Weekly Pattern Alerts</div>
    </div>
</div>
""", unsafe_allow_html=True)

# Theme Section
st.markdown('<div class="section-title">🎨 Theme Section</div>', unsafe_allow_html=True)
st.markdown("""
<div class="theme-panel">
    <h4 style="margin-top: 0;">Built-In Light & Dark Experience</h4>
    <p style="margin-bottom: 8px; color: #444;">
        FitSync supports a shared theme toggle across pages. Switch to light mode for daytime clarity
        and dark mode for low-light comfort without losing chart readability.
    </p>
    <p style="margin-bottom: 0; color: #444;"><strong>Use the sidebar toggle to change the full app appearance instantly.</strong></p>
</div>
""", unsafe_allow_html=True)

# Divider
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# CTA
st.markdown('<div class="section-title">🚀 Ready to Get Started?</div>', unsafe_allow_html=True)

st.markdown("""
<div style="text-align: center; margin: 30px 0;">
    <p style="font-size: 16px; color: #555; margin-bottom: 20px;">
        Explore your personalized health dashboard and discover insights about your fitness journey.
    </p>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    if st.button("📊 Dashboard", use_container_width=True, key="btn_dash"):
        st.switch_page("pages/1_Dashboard.py")

with col2:
    if st.button("📈 Trends", use_container_width=True, key="btn_trends"):
        st.switch_page("pages/2_Trends.py")

with col3:
    st.info("💡 **Tip:** Use the theme toggle in the sidebar to switch between light and dark modes!")

# Footer
st.markdown("""
<div class="divider"></div>
<div class="footer">
    <div class="footer-text"><strong>FitSync © 2026</strong> | Personal Health Analytics Platform</div>
    <div class="footer-text">Built with ❤️ using Streamlit | Optimize Your Health Journey</div>
    <div class="footer-text" style="margin-top: 15px; font-size: 12px; opacity: 0.7;">
        📱 Track • 📊 Analyze • 💪 Achieve
    </div>
</div>
""", unsafe_allow_html=True)
