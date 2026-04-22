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
theme.render_theme_toggle()
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
    background: linear-gradient(135deg, #667eea 0%, #764ba2 40%, #4CAF50 70%, #FF9800 100%);
    padding: 100px 40px;
    border-radius: 25px;
    color: white;
    text-align: center;
    margin-bottom: 50px;
    box-shadow: 0 20px 60px rgba(102, 126, 234, 0.3);
    animation: slideIn 0.8s ease-out;
    position: relative;
    overflow: hidden;
}

.hero-section::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: radial-gradient(circle at 20% 50%, rgba(255,255,255,0.1), transparent),
                radial-gradient(circle at 80% 80%, rgba(255,255,255,0.1), transparent);
    z-index: 1;
}

.hero-content {
    position: relative;
    z-index: 2;
}

@keyframes slideIn {
    from {
        opacity: 0;
        transform: translateY(-30px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

@keyframes fadeInUp {
    from {
        opacity: 0;
        transform: translateY(20px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

.hero-icon {
    font-size: 80px;
    margin-bottom: 20px;
    animation: bounce 2.5s infinite;
    filter: drop-shadow(0 5px 15px rgba(0,0,0,0.2));
}

@keyframes bounce {
    0%, 100% { transform: translateY(0) scale(1); }
    50% { transform: translateY(-15px) scale(1.05); }
}

.hero-title {
    font-size: 72px;
    font-weight: 900;
    margin-bottom: 20px;
    text-shadow: 5px 5px 15px rgba(0,0,0,0.3);
    letter-spacing: -2px;
    font-family: "Georgia", "Garamond", serif;
    background: linear-gradient(45deg, #ffffff, #f0f0f0);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

.hero-subtitle {
    font-size: 28px;
    opacity: 0.98;
    margin-bottom: 25px;
    font-weight: 500;
    letter-spacing: 0.5px;
    animation: fadeInUp 0.8s ease-out 0.2s backwards;
}

.hero-description {
    font-size: 17px;
    opacity: 0.92;
    max-width: 750px;
    margin: 0 auto;
    line-height: 1.9;
    animation: fadeInUp 0.8s ease-out 0.4s backwards;
}

.section-title {
    font-size: 42px;
    font-weight: 900;
    background: linear-gradient(90deg, #667eea, #4CAF50, #FF9800);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin: 60px 0 40px 0;
    padding-bottom: 20px;
    border-bottom: 4px solid #667eea;
    letter-spacing: -0.5px;
    font-family: "Georgia", "Garamond", serif;
    animation: fadeInUp 0.8s ease-out;
}

.feature-card {
    background: linear-gradient(135deg, #ffffff 0%, #f8f9ff 100%);
    padding: 40px;
    border-radius: 20px;
    margin: 20px 0;
    box-shadow: 0 10px 30px rgba(0,0,0,0.08);
    border-left: 8px solid #667eea;
    transition: all 0.4s cubic-bezier(0.23, 1, 0.320, 1);
    animation: fadeInUp 0.8s ease-out;
    position: relative;
    overflow: hidden;
}

.feature-card::before {
    content: '';
    position: absolute;
    top: -50%;
    right: -50%;
    width: 100%;
    height: 100%;
    background: radial-gradient(circle, rgba(102, 126, 234, 0.05), transparent);
    transition: all 0.4s ease;
}

.feature-card:hover {
    transform: translateY(-8px) scale(1.02);
    box-shadow: 0 20px 50px rgba(102, 126, 234, 0.2);
    border-left-color: #FF9800;
}

.feature-card:hover::before {
    top: 0;
    right: 0;
}

.feature-icon {
    font-size: 48px;
    margin-bottom: 20px;
    animation: bounce 2s infinite;
}

.feature-title {
    font-size: 24px;
    font-weight: 800;
    color: #111111;
    margin-bottom: 15px;
    position: relative;
    z-index: 1;
}

.feature-description {
    font-size: 16px;
    color: #555555;
    line-height: 1.8;
    position: relative;
    z-index: 1;
}

.stat-box {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    padding: 45px 30px;
    border-radius: 20px;
    color: white;
    text-align: center;
    box-shadow: 0 10px 35px rgba(102, 126, 234, 0.2);
    transition: all 0.4s cubic-bezier(0.23, 1, 0.320, 1);
    animation: fadeInUp 0.8s ease-out;
    position: relative;
    overflow: hidden;
}

.stat-box::before {
    content: '';
    position: absolute;
    top: 0;
    left: -100%;
    width: 100%;
    height: 100%;
    background: linear-gradient(90deg, transparent, rgba(255,255,255,0.2), transparent);
    transition: left 0.5s ease;
}

.stat-box:hover::before {
    left: 100%;
}

.stat-box:nth-child(2) {
    background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
    box-shadow: 0 10px 35px rgba(245, 87, 108, 0.2);
}

.stat-box:nth-child(3) {
    background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
    box-shadow: 0 10px 35px rgba(79, 172, 254, 0.2);
}

.stat-box:hover {
    transform: translateY(-10px) scale(1.05);
}

.stat-number {
    font-size: 48px;
    font-weight: 900;
    margin-bottom: 12px;
    animation: bounce 2s infinite;
}

.stat-label {
    font-size: 16px;
    opacity: 0.98;
    font-weight: 700;
}

.highlights {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 25px;
    margin: 45px 0;
}

.highlight-item {
    background: linear-gradient(135deg, rgba(102, 126, 234, 0.1) 0%, rgba(240, 147, 251, 0.1) 100%);
    padding: 35px;
    border-radius: 18px;
    text-align: center;
    border-top: 5px solid #667eea;
    transition: all 0.4s cubic-bezier(0.23, 1, 0.320, 1);
    animation: fadeInUp 0.8s ease-out;
    backdrop-filter: blur(10px);
}

.highlight-item:nth-child(2) {
    border-top-color: #f093fb;
}

.highlight-item:nth-child(3) {
    border-top-color: #4facfe;
}

.highlight-item:hover {
    transform: translateY(-8px) scale(1.05);
    box-shadow: 0 20px 40px rgba(102, 126, 234, 0.15);
    background: linear-gradient(135deg, rgba(102, 126, 234, 0.2) 0%, rgba(240, 147, 251, 0.2) 100%);
}

.highlight-number {
    font-size: 40px;
    font-weight: 900;
    background: linear-gradient(90deg, #667eea, #f093fb);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin-bottom: 12px;
    animation: bounce 2s infinite;
}

.highlight-text {
    font-size: 15px;
    color: #333333;
    font-weight: 700;
}

.divider {
    height: 4px;
    background: linear-gradient(90deg, transparent, #667eea 20%, #f093fb 50%, #4facfe 80%, transparent);
    margin: 60px 0;
    border-radius: 2px;
    box-shadow: 0 4px 15px rgba(102, 126, 234, 0.1);
}

.cta-button {
    display: inline-block;
    padding: 16px 40px;
    border-radius: 12px;
    font-weight: 700;
    font-size: 16px;
    border: none;
    cursor: pointer;
    transition: all 0.3s ease;
    box-shadow: 0 5px 20px rgba(0,0,0,0.15);
    text-decoration: none;
}

.cta-primary {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
}

.cta-primary:hover {
    transform: translateY(-3px);
    box-shadow: 0 10px 30px rgba(102, 126, 234, 0.3);
}

.cta-secondary {
    background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
    color: white;
}

.cta-secondary:hover {
    transform: translateY(-3px);
    box-shadow: 0 10px 30px rgba(245, 87, 108, 0.3);
}

.footer {
    text-align: center;
    color: #666;
    font-size: 14px;
    margin-top: 60px;
    padding: 40px 0;
    border-top: 2px solid #e0e0e0;
    animation: fadeInUp 0.8s ease-out;
}

.footer-text {
    margin: 8px 0;
    line-height: 1.8;
}

.quick-stats {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 20px;
    margin: 40px 0;
}

.stat-item {
    background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    padding: 25px;
    border-radius: 15px;
    text-align: center;
    box-shadow: 0 5px 15px rgba(0,0,0,0.08);
    transition: all 0.3s ease;
    animation: fadeInUp 0.8s ease-out;
}

.stat-item:hover {
    transform: translateY(-5px);
    box-shadow: 0 10px 25px rgba(0,0,0,0.12);
}

.stat-item-icon {
    font-size: 36px;
    margin-bottom: 10px;
}

.stat-item-value {
    font-size: 24px;
    font-weight: 900;
    color: #667eea;
    margin-bottom: 5px;
}

.stat-item-label {
    font-size: 13px;
    color: #666;
    font-weight: 600;
}

@media (max-width: 768px) {
    .hero-title { font-size: 44px; }
    .hero-subtitle { font-size: 20px; }
    .section-title { font-size: 32px; }
    .highlights { grid-template-columns: 1fr; }
    .quick-stats { grid-template-columns: repeat(2, 1fr); }
    .stat-box { padding: 30px; }
    .feature-card { padding: 30px; }
}
</style>
""", unsafe_allow_html=True)

# Hero Section with premium styling
st.markdown("""
<div class="hero-section">
    <div class="hero-content">
        <div class="hero-icon">🏃‍♂️</div>
        <div class="hero-title">FitSync</div>
        <div class="hero-subtitle">Your Personal Health Analytics Dashboard</div>
        <div class="hero-description">
            Transform your fitness journey with intelligent health analytics. Track recovery patterns, 
            analyze comprehensive metrics, and unlock personalized insights powered by advanced AI algorithms. 
            Make data-driven decisions to optimize your wellness routine.
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Quick Stats Overview
st.markdown('<div class="section-title">📊 What You Can Track</div>', unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="stat-item">
        <div class="stat-item-icon">👟</div>
        <div class="stat-item-value">Steps</div>
        <div class="stat-item-label">Daily Activity</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="stat-item">
        <div class="stat-item-icon">😴</div>
        <div class="stat-item-value">Sleep</div>
        <div class="stat-item-label">Sleep Quality</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="stat-item">
        <div class="stat-item-icon">❤️</div>
        <div class="stat-item-value">Recovery</div>
        <div class="stat-item-label">Recovery Score</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="stat-item">
        <div class="stat-item-icon">📈</div>
        <div class="stat-item-value">Trends</div>
        <div class="stat-item-label">Progress Tracking</div>
    </div>
    """, unsafe_allow_html=True)

# Key Metrics Overview
st.markdown('<div class="section-title">⚡ Platform Highlights</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="stat-box">
        <div class="stat-number">📊</div>
        <div class="stat-label">Real-Time Analytics</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="stat-box">
        <div class="stat-number">🎯</div>
        <div class="stat-label">Smart Recovery Insights</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="stat-box">
        <div class="stat-number">🚀</div>
        <div class="stat-label">AI-Powered Predictions</div>
    </div>
    """, unsafe_allow_html=True)

# Highlights section
st.markdown('<div class="section-title">✨ Why Choose FitSync?</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="highlight-item">
        <div class="highlight-number">📈</div>
        <div class="highlight-text">Advanced Visualizations</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="highlight-item">
        <div class="highlight-number">🎨</div>
        <div class="highlight-text">Dark & Light Modes</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="highlight-item">
        <div class="highlight-number">⚡</div>
        <div class="highlight-text">Lightning Performance</div>
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
            Real-time data visualization with interactive Plotly charts showing your daily steps, 
            sleep patterns, and recovery scores with stunning clarity.
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">📈</div>
        <div class="feature-title">Trend Analysis & Insights</div>
        <div class="feature-description">
            Deep dive into your health trends with advanced analytics. 
            Track monthly averages, view detailed distributions, and gain comprehensive 
            statistical insights to optimize your fitness strategy.
        </div>
    </div>
    """, unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">🤖</div>
        <div class="feature-title">Smart Recovery Algorithm</div>
        <div class="feature-description">
            Advanced AI algorithm calculates your daily recovery score based on 
            sleep quality metrics, heart rate variations, and daily activity levels. 
            Understand your body's recovery capacity and plan accordingly.
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">🎨</div>
        <div class="feature-title">Theme Customization</div>
        <div class="feature-description">
            Seamless light and dark theme switching that works across all pages. 
            Enjoy a comfortable viewing experience day or night with automatic 
            color-coded metrics and adaptive UI elements.
        </div>
    </div>
    """, unsafe_allow_html=True)

# Divider
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# Call to Action
st.markdown('<div class="section-title">🚀 Start Your Health Journey</div>', unsafe_allow_html=True)

st.markdown("""
<div style="text-align: center; margin: 40px 0; padding: 30px; background: linear-gradient(135deg, rgba(102, 126, 234, 0.05), rgba(240, 147, 251, 0.05)); border-radius: 20px; border: 2px solid rgba(102, 126, 234, 0.1);">
    <p style="font-size: 18px; color: #333; margin-bottom: 30px; font-weight: 600;">
        Choose your path to better health insights
    </p>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1.2, 1.2, 1.2])

with col1:
    if st.button("📊 Dashboard", use_container_width=True, key="btn_dash"):
        st.switch_page("pages/1_Dashboard.py")

with col2:
    if st.button("📈 Trends", use_container_width=True, key="btn_trends"):
        st.switch_page("pages/2_Trends.py")

with col3:
    st.info("💡 Tip: Use the sidebar theme toggle to switch between light and dark modes for optimal viewing!")

# Benefits Section
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">💪 Benefits at a Glance</div>', unsafe_allow_html=True)

benefit_col1, benefit_col2, benefit_col3 = st.columns(3)

with benefit_col1:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">🎯</div>
        <div class="feature-title">Personalized Insights</div>
        <div class="feature-description">
            Get customized analytics tailored to your health data and fitness goals.
        </div>
    </div>
    """, unsafe_allow_html=True)

with benefit_col2:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">📱</div>
        <div class="feature-title">Easy to Use</div>
        <div class="feature-description">
            Intuitive interface designed for everyone, from beginners to fitness enthusiasts.
        </div>
    </div>
    """, unsafe_allow_html=True)

with benefit_col3:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">⚡</div>
        <div class="feature-title">Fast & Reliable</div>
        <div class="feature-description">
            Lightning-fast data processing with reliable calculations and accurate metrics.
        </div>
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("""
<div class="divider"></div>
<div class="footer">
    <div class="footer-text"><strong>🏆 FitSync © 2026</strong> | Personal Health Analytics Platform</div>
    <div class="footer-text">Built with ❤️ using Streamlit & Plotly | Optimize Your Health Journey</div>
    <div class="footer-text" style="margin-top: 20px; font-size: 13px; opacity: 0.7;">
        📱 Track • 📊 Analyze • 💪 Achieve • 🚀 Transform
    </div>
</div>
""", unsafe_allow_html=True)
