# Credit-Card-Fraud-Detection
### 📄 `` — *AK Detectors | Credit Card Fraud Detection Portal*

**🚀 Powered by PCA + LightGBM | Deployed on Render | Full ML Pipeline**

> **An intelligent AI-based system to detect fraudulent credit card transactions using PCA-driven features and LightGBM.**  
> ⚠️ This system is AI-generated and intended for demo/educational use only.

---

### 📍 Live Demo:
🔗 **[Access Deployed App on Render →](https://credit-card-fraud-detection-nxs3.onrender.com/)**
---





````markdown

# 🚀 Project Overview

This end-to-end credit card fraud detection system includes:

- ✅ Data cleaning & preprocessing
- 📊 PCA feature transformation with human-readable labels
- 🤖 ML model training (LightGBM)
- 💾 Model saving and joblib handling
- 🌐 Streamlit-based fraud detection dashboard
- 🧭 Deployed on **Render.com** for global accessibili
# 💳 AK Detectors | Credit Card Fraud Detection Portal 🚀

<p align="center">
  <img src="https://img.shields.io/badge/Status-Deployed-success?style=flat-square&color=brightgreen"/>
  <img src="https://img.shields.io/badge/Made%20by-Venkata%20Abhinandan%20Kancharla-blueviolet?style=flat-square"/>
  <img src="https://img.shields.io/badge/Deployment-Render-informational"/>
</p>

> 💡 A production-grade AI-powered fraud detection portal with PCA-enhanced insights and real-time prediction capability. Built with ❤️ using real-world banking-style features.

🔗 **Live App:** [https://credit-card-fraud-detection-nxs3.onrender.com/](https://credit-card-fraud-detection-nxs3.onrender.com/)  
👤 **Author:** [Venkata Abhinandan Kancharla](https://abhikancharla.vercel.app)

---

---

## 🧠 Technologies Used

| Area                 | Tech Stack |
|----------------------|------------|
| Data Handling        | Pandas, NumPy |
| EDA & Viz            | Seaborn, Matplotlib, Plotly |
| Model Building       | LightGBMClassifier |
| Dimensionality Reduction | PCA |
| Web App              | Streamlit |
| Deployment           | Render.com |

---
## 🧪 ML Pipeline Workflow

### 🧹 1. Data Cleaning
- Removed duplicates and nulls
- Handled outliers and class imbalance (fraud class)

### 📊 2. Exploratory Data Analysis (EDA)
- Visualized fraud patterns by amount, time, and transaction velocity
- Studied feature importance and correlations

### 🔍 3. Feature Engineering
- Created business-aligned interpretable PCA components:
  - `Transaction Velocity`
  - `Spending Diversity Index`
  - `Merchant Trust Score`
  - `Customer Risk Profile`
  - `Geo-Activity Variance`

### 🧠 4. Model Building
- Used `LightGBMClassifier` with:
  - Balanced class weights
  - Grid-tuned parameters
  - Trained on PCA-reduced features

### 💾 5. Saving Artifacts
- Saved model using `joblib`:
  - `lgbm_fraud_model.pkl`
  - `scaler_ccfd.pkl`

---

## 🌐 Deployment Steps (Render)

- **Push code to GitHub**
- On [Render.com](https://render.com):
  - Create new Web Service
  - Build Command: `pip install -r requirements.txt`
  - Start Command: `streamlit run app.py`
- ✅ Hosted on public URL with HTTPS

---

## 💻 App Pages & Features

| Page            | Description |
|-----------------|-------------|
| 🏠 **Home**      | Project overview and usage instructions |
| 📊 **Dashboard** | Real-time fraud stats, bar charts, probability distributions |
| 🔎 **Predict**   | Manual or CSV-based prediction (user-friendly PCA inputs) |
| ⚙️ **Settings**  | PCA info, scaling alert, and AI usage disclaimer |

---

## 🧾 Sample Input CSV Format

```csv
Transaction Velocity,Spending Diversity Index,Merchant Trust Score,Customer Risk Profile,Geo-Activity Variance
-1.123,0.567,1.789,-0.345,0.912
...
````

🧠 **Note**: Your CSV will be automatically processed, predicted, and downloadable with:

* `Prediction` → "Fraud" / "Not Fraud"
* `isFraud_Prob` → Probability score

---

## 📈 Sample Dashboard Visuals

* 📊 **Fraud vs Non-Fraud** (bar chart)
* 🧪 **Probability Histogram**
* 🧍 **User-Focused Radar Chart**
* 🧩 **Dynamic Metrics**: Total transactions, fraud % etc.

---

## ⚠️ Disclaimer

> ⚠️ This system is AI-generated and intended for educational/demo use.
> It may not reflect real-world fraud detection with complete accuracy.

---

## 👨‍💻 Author Info

**Venkata Abhinandan Kancharla**
🌐 [Portfolio](https://abhikancharla.vercel.app)
💼 Machine Learning Engineer | E2E ML Pipelines | AI Applications
📮 LinkedIn: [@abhinandan6123](https://linkedin.com/in/abhinandan6123)

---

## 📜 License

 License — Free to use with proper credit

---

## ⭐ Like this Project?

If you found this useful:

* ⭐ Star this repo
* 🍴 Fork and extend it
* 🧠 Share your use case with me!

```

---

### ✅ Next Step (Optional)
Let me know if you want:
- `.gif` of the app in action
- Video walkthrough for LinkedIn
- Auto-publish to Hugging Face Spaces too

```
