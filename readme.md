# 🏥 Medical Cost Prediction App

An end-to-end Machine Learning web application that predicts individual medical insurance costs based on patient demographic and lifestyle attributes. Built using Python, Scikit-Learn, and Streamlit.

---

## 📊 Project Overview
Healthcare costs vary significantly depending on factors like age, body mass index (BMI), smoking status, and family size. This project explores the **Medical Cost Personal Dataset** to uncover key cost drivers, train a predictive regression model, and deploy it as an interactive web app.

- **Target Variable:** Unscaled continuous numerical target (`charges` in USD).
- **Key Insights Discovered:** Smoking status (`smoker`) and `age` have the strongest linear correlation with high medical bills.

---

## 🤖 Model Performance
A Linear Regression model was trained on an 80/20 train-test split after proper categorical encoding (Binary & One-Hot Encoding) and feature scaling (`StandardScaler`).

- **$R^2$ Score:** `0.7836` (Explains ~78% of the variance in medical charges)
- **Mean Absolute Error (MAE):** `$4,181.19`
- **Root Mean Squared Error (RMSE):** `$5,796.28`

---

## 🛠️ Tech Stack & Libraries
- **Language:** Python 3.12
- **Data Manipulation & Analysis:** Pandas, NumPy
- **Machine Learning:** Scikit-Learn (`LinearRegression`, `StandardScaler`, metrics)
- **Model Persistence:** Joblib
- **Web Application:** Streamlit

---

## 🚀 How to Run Locally

Follow these steps to run the project on your own machine:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/YOUR-USERNAME/medical-cost-prediction.git
   cd medical-cost-prediction
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Launch the Streamlit app:**
   ```bash
   streamlit run app.py
   ```