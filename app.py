import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import joblib
from sklearn.preprocessing import StandardScaler

# Set Page Configuration
st.set_page_config(
    page_title="AK Detectors | Credit Card Fraud Detection",
    layout="wide",
    page_icon="🚀"
)

# Header Title & Footer
st.markdown(
    """
    <style>
        body {
            background: linear-gradient(135deg, #f0f4ff, #e0eaff);
            font-family: 'Segoe UI', sans-serif;
        }
        .main-title {
            font-size: 40px;
            font-weight: bold;
            color: #004aad;
            text-shadow: 1px 1px 2px #00000020;
            animation: glow 2s ease-in-out infinite alternate;
        }
        .subtitle {
            font-size: 18px;
            font-weight: 500;
            color: #333;
        }
        hr {
            border: 1px solid #bbb;
        }
        @keyframes glow {
            from {
                text-shadow: 0 0 5px #91c6ff;
            }
            to {
                text-shadow: 0 0 20px #004aad, 0 0 30px #004aad;
            }
        }
    </style>
    <div style="text-align: center;">
        <h1 class="main-title">📈 AK Detectors - Credit Card Fraud Detection Portal 💳</h1>
        <p class="subtitle">
            by <strong>Venkata Abhinandan Kancharla</strong> • 
            <a href="https://abhikancharla.vercel.app" target="_blank" style="color:#004aad; text-decoration: none;">
                🌐 Portfolio
            </a>
        </p>
        <hr>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("""
    <hr>
    <p style='text-align: center; font-size: 15px; color: #555;'>
        © 2025 • <strong>AK Detectors</strong> | Designed by 
        <a href='https://abhikancharla.vercel.app' target='_blank' style='color: #004aad; text-decoration: none;'>
            Venkata Abhinandan Kancharla
        </a>
    </p>
""", unsafe_allow_html=True)


# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["🏠 Home", "📊 Dashboard", "🔎 Predict", "⚙️ Settings"])

# Load Model and Scaler
@st.cache_resource
def load_model():
    model = joblib.load("lgbm_fraud_model.pkl")
    return model

@st.cache_resource
def load_scaler():
    return joblib.load("scaler_ccfd.pkl")

model = load_model()
scaler = load_scaler()

# Input Columns
pca_features = [
    'Transaction Velocity',
    'Spending Diversity Index',
    'Merchant Trust Score',
    'Customer Risk Profile',
    'Geo-Activity Variance'
]



# Home Page
if page == "🏠 Home":
    st.markdown("""
    ### Welcome to AK Detectors
    This platform provides a high-security AI-based solution to detect fraudulent credit card transactions using PCA-transformed features.

    - Upload your processed `.csv` file with PCA features
    - Get real-time fraud predictions
    - View analytics, insights, and charts

    """)

# Dashboard
elif page == "📊 Dashboard":
    st.subheader("📊 Prediction Overview Dashboard")
    uploaded_file = st.file_uploader("Upload Prediction File (with `Prediction`, `isFraud_Prob`) column):", type=["csv"])
    if uploaded_file is not None:
        result = pd.read_csv(uploaded_file)

        # KPIs
        col1, col2, col3 = st.columns(3)
        col1.metric("📅 Total Transactions", len(result))
        col2.metric("⚠️ Fraud Predictions", (result['Prediction'] == 'Fraud').sum())
        col3.metric("📊 Fraud %", f"{(result['Prediction'] == 'Fraud').mean()*100:.2f}%")

        # Bar Chart
       value_counts_df = result['Prediction'].value_counts().reset_index()
value_counts_df.columns = ['Prediction', 'Count']

fig_bar = px.bar(value_counts_df,
                 x='Prediction', y='Count', color='Prediction',
                 title="Fraud vs Non-Fraud Transactions",
                 labels={'Prediction': 'Prediction', 'Count': 'Count'})

        st.plotly_chart(fig_bar, use_container_width=True)

        # Fraud Probability Histogram
        fig_hist = px.histogram(result, x='isFraud_Prob', nbins=30,
                                title="Fraud Probability Distribution",
                                color='Prediction')
        st.plotly_chart(fig_hist, use_container_width=True)

# Prediction Page
elif page == "🔎 Predict":
    st.subheader("🔍 Real-time Fraud Prediction")
    mode = st.radio("Input Mode", ["📝 Manual Entry", "📂 CSV Upload"])

    if mode == "📂 CSV Upload":
        input_file = st.file_uploader("Upload your PCA transformed data (20 PCs):", type=["csv"])
        if input_file:
            input_data = pd.read_csv(input_file)
            X_scaled = input_data[pca_features]
            probs = model.predict_proba(X_scaled)[:, 1]
            preds = np.where(probs > 0.5, 'Fraud', 'Not Fraud')
            input_data['isFraud_Prob'] = probs
            input_data['Prediction'] = preds
            st.write(input_data.head())

            st.download_button("📥 Download Results", data=input_data.to_csv(index=False),
                               file_name="fraud_predictions.csv", mime="text/csv")

    else:
        manual_input = {}
        cols = st.columns(4)
        for i, col in enumerate(pca_features):
            with cols[i % 4]:
                manual_input[col] = st.number_input(f"{col}", value=0.0)

        if st.button("📊 Predict Transaction"):
            df_input = pd.DataFrame([manual_input])
            prediction_proba = model.predict_proba(df_input)[0, 1]
            prediction = "Fraud" if prediction_proba > 0.5 else "Not Fraud"

            st.success(f"Prediction: {prediction} (Prob: {prediction_proba:.4f})")

            # Optional Radar Chart
            if st.checkbox("🔍 Show Radar Chart"):
                radar_df = pd.DataFrame({'Feature': pca_features, 'Value': list(manual_input.values())})
                fig_radar = px.line_polar(radar_df, r='Value', theta='Feature', line_close=True,
                                          title="Feature Radar View")
                st.plotly_chart(fig_radar, use_container_width=True)

# Settings Page
elif page == "⚙️ Settings":
    st.subheader("⚙️ Configuration & System Settings")

    # AI Disclaimer Alert
    st.markdown("""
    <div style='background-color: #ffdddd; padding: 15px; border-left: 6px solid #f44336; border-radius: 5px;'>
        <strong>⚠️ Alert:</strong> This prediction system is powered by AI and machine learning.<br>
        It may not always produce 100% accurate results. Please use responsibly for educational or assistive purposes.
    </div>
    """, unsafe_allow_html=True)

    # System Overview
    st.markdown("""
    <div style='padding: 10px; background-color: #222244; border-radius: 10px; margin-top: 20px;'>
    <h4 style='color: #00ffff;'>📌 Model Input Requirements:</h4>
    <ul>
        <li><strong>PCA Components:</strong> 5 features named <code>PC1</code> to <code>PC5</code></li>
        <li><strong>Preprocessing:</strong> Inputs must be scaled using the same StandardScaler used during training</li>
        <li><strong>Model:</strong> LightGBM Classifier with class_weight='balanced'</li>
    </ul>

    <h4 style='color: #00ffff;'>📁 Accepted Input Modes:</h4>
    <ul>
        <li>📂 <strong>CSV Upload:</strong> File with columns <code>PC1</code> to <code>PC5</code></li>
        <li>📝 <strong>Manual Entry:</strong> Form-based numeric input</li>
    </ul>

    <h4 style='color: #00ffff;'>🔐 Security & Transparency:</h4>
    <ul>
        <li>✅ All predictions run on the client-side Streamlit server</li>
        <li>🧪 Trained with fairness in mind, tested on unseen data</li>
        <li>🔄 Continuous updates available via GitHub integration</li>
    </ul>

    <h4 style='color: #00ffff;'>👨‍💻 Developer Contact:</h4>
    <ul>
        <li><strong>Venkata Abhinandan Kancharla</strong></li>
        <li>🌐 <a href='https://abhikancharla.vercel.app' target='_blank' style='color:#00ffcc;'>Visit Portfolio</a></li>
        <li>🛠️ Share feedback or report bugs through GitHub or website</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("""
    <hr>
    <p style='text-align: center;'>© 2025 - AK Detectors | Built by <a href='https://abhikancharla.vercel.app' target='_blank'>Venkata Abhinandan Kancharla</a></p>
""", unsafe_allow_html=True)
