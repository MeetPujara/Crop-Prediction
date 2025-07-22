import streamlit as st
import joblib
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="🌾 Smart Crop Advisor",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Enhanced CSS styling
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    .stApp {
        background: linear-gradient(135deg, #0f1419 0%, #1a2332 50%, #0f1419 100%);
        font-family: 'Inter', sans-serif;
    }
    
    .main-header {
        background: linear-gradient(135deg, #28a745, #20c997);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-size: 3.5rem;
        font-weight: 700;
        text-align: center;
        margin-bottom: 1rem;
        text-shadow: 0 4px 8px rgba(40, 167, 69, 0.3);
    }
    
    .subtitle {
        text-align: center;
        font-size: 1.2rem;
        color: #8b949e;
        margin-bottom: 2rem;
        font-weight: 300;
    }
    
    .metric-card {
        background: linear-gradient(145deg, #21262d, #30363d);
        padding: 1.5rem;
        border-radius: 15px;
        border: 1px solid #30363d;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
        margin: 1rem 0;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    
    .metric-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 40px rgba(40, 167, 69, 0.2);
        border-color: #28a745;
    }
    
    .metric-title {
        color: #28a745;
        font-weight: 600;
        font-size: 1.1rem;
        margin-bottom: 0.5rem;
    }
    
    .metric-value {
        color: #f0f6fc;
        font-size: 2rem;
        font-weight: 700;
    }
    
    .stButton>button {
        background: linear-gradient(135deg, #28a745, #20c997);
        color: white;
        font-weight: 600;
        border: none;
        border-radius: 12px;
        padding: 0.75rem 2rem;
        font-size: 1.1rem;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(40, 167, 69, 0.3);
        width: 100%;
    }
    
    .stButton>button:hover {
        background: linear-gradient(135deg, #218838, #1ea085);
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(40, 167, 69, 0.4);
    }
    
    .stSidebar {
        background: linear-gradient(180deg, #161b22, #21262d);
        border-right: 1px solid #30363d;
    }
    
    .stSidebar .stSlider {
        background: rgba(40, 167, 69, 0.1);
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
    }
    
    .prediction-result {
        background: linear-gradient(135deg, #28a745, #20c997);
        color: white;
        padding: 2rem;
        border-radius: 15px;
        text-align: center;
        font-size: 1.5rem;
        font-weight: 600;
        margin: 2rem 0;
        box-shadow: 0 8px 32px rgba(40, 167, 69, 0.3);
    }
    
    .feature-card {
        background: linear-gradient(145deg, #21262d, #30363d);
        padding: 1.5rem;
        border-radius: 12px;
        border: 1px solid #30363d;
        margin: 1rem 0;
        transition: all 0.3s ease;
    }
    
    .feature-card:hover {
        border-color: #28a745;
        box-shadow: 0 4px 20px rgba(40, 167, 69, 0.2);
    }
    
    .info-section {
        background: rgba(40, 167, 69, 0.1);
        padding: 2rem;
        border-radius: 15px;
        border: 1px solid rgba(40, 167, 69, 0.3);
        margin: 2rem 0;
    }
    
    .footer {
        text-align: center;
        padding: 2rem;
        color: #8b949e;
        border-top: 1px solid #30363d;
        margin-top: 3rem;
    }
    
    .stExpander {
        background: linear-gradient(145deg, #21262d, #30363d);
        border: 1px solid #30363d;
        border-radius: 12px;
    }
    
    .streamlit-expanderHeader {
        background: transparent;
        color: #28a745;
        font-weight: 600;
    }
    
    h1, h2, h3 {
        color: #28a745;
        font-weight: 600;
    }
    
    .stMarkdown {
        color: #f0f6fc;
    }
    
    /* Animation for loading */
    @keyframes pulse {
        0% { opacity: 1; }
        50% { opacity: 0.5; }
        100% { opacity: 1; }
    }
    
    .loading {
        animation: pulse 1.5s infinite;
    }
    </style>
    """, unsafe_allow_html=True)

# Main header
st.markdown('<h1 class="main-header">🌾 Smart Crop Advisor</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Harness the power of AI to optimize your agricultural decisions with precision soil and climate analysis</p>', unsafe_allow_html=True)

# Project disclaimer
st.markdown("""
<div style="background: linear-gradient(135deg, #ff6b35, #f7931e); padding: 1rem 1.5rem; border-radius: 10px; margin: 1rem 0; text-align: center; border-left: 4px solid #ff8c42;">
    <strong>📚 Educational Project</strong> • This is a demonstration application created for learning purposes. 
    For actual agricultural decisions, please consult with qualified agronomists and use professional agricultural tools.
</div>
""", unsafe_allow_html=True)

# Create columns for layout
col1, col2 = st.columns([1, 2])

with col1:
    st.markdown("### 🎯 Control Panel")
    
    with st.container():
        st.markdown("#### 🧪 Soil Nutrients")
        N = st.slider('🔵 Nitrogen (N)', 0, 140, 50, help="Nitrogen content in the soil")
        P = st.slider('🟣 Phosphorous (P)', 5, 145, 50, help="Phosphorous content in the soil")
        K = st.slider('🟡 Potassium (K)', 5, 205, 50, help="Potassium content in the soil")
        
        st.markdown("#### 🌡️ Climate Conditions")
        temperature = st.slider('🌡️ Temperature (°C)', 8.0, 43.0, 25.0, help="Average temperature")
        humidity = st.slider('💧 Humidity (%)', 10.0, 100.0, 50.0, help="Relative humidity")
        ph = st.slider('⚗️ pH Level', 3.5, 9.5, 6.5, help="Soil pH level")
        rainfall = st.slider('🌧️ Rainfall (mm)', 20.0, 300.0, 100.0, help="Annual rainfall")

with col2:
    st.markdown("### 📊 Current Parameters Overview")
    
    # Create metrics display
    metrics_col1, metrics_col2, metrics_col3 = st.columns(3)
    
    with metrics_col1:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">🧪 Soil Nutrients</div>
            <div style="color: #f0f6fc; font-size: 1rem;">
                N: {N} | P: {P} | K: {K}
            </div>
        </div>
        """, unsafe_allow_html=True)
        
    with metrics_col2:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">🌡️ Temperature</div>
            <div class="metric-value">{temperature}°C</div>
        </div>
        """, unsafe_allow_html=True)
        
    with metrics_col3:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">💧 Humidity</div>
            <div class="metric-value">{humidity}%</div>
        </div>
        """, unsafe_allow_html=True)
    
    # Additional metrics
    metrics_col4, metrics_col5 = st.columns(2)
    
    with metrics_col4:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">⚗️ pH Level</div>
            <div class="metric-value">{ph}</div>
        </div>
        """, unsafe_allow_html=True)
        
    with metrics_col5:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">🌧️ Rainfall</div>
            <div class="metric-value">{rainfall}mm</div>
        </div>
        """, unsafe_allow_html=True)
    
    # Prediction button and result
    st.markdown("### 🚀 Get Recommendation")
    
    if st.button("🔮 Analyze & Recommend Optimal Crop", key="predict_btn"):
        try:
            with st.spinner('🧠 AI is analyzing your soil and climate data...'):
                input_df = pd.DataFrame({
                    'N': [N],
                    'P': [P],
                    'K': [K],
                    'temperature': [temperature],
                    'humidity': [humidity],
                    'ph': [ph],
                    'rainfall': [rainfall]
                })
                
                model = joblib.load('crop_recommendation_model.pkl')
                prediction = model.predict(input_df.values)[0]
                st.markdown(f"""
                <div class="prediction-result">
                    🎉 <strong>Recommended Crop: {prediction}</strong>
                    <br>
                    <small style="opacity: 0.9;">Based on your soil and climate conditions</small>
                    <br>
                    <small style="opacity: 0.7; font-size: 0.9rem;">⚠️ Demo prediction - For educational purposes only</small>
                </div>
                """, unsafe_allow_html=True)
                
        except FileNotFoundError:
            st.error("❌ Model file not found. Please ensure 'crop_recommendation_model.pkl' exists in your directory.")
        except Exception as e:
            st.error(f"❌ An error occurred: {str(e)}")

# Footer
st.markdown(f"""
<div class="footer">
    <strong>🌾 Smart Crop Advisor</strong> | Educational Machine Learning Project
    <br>
    <small>Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M')} | Made with ❤️ for learning and demonstration purposes</small>
    <br>
    <small style="opacity: 0.7;">⚠️ This is a student/educational project. Not intended for commercial agricultural use.</small>
</div>
""", unsafe_allow_html=True)