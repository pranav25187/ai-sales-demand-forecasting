# 📈 AI Sales & Demand Forecasting Dashboard

A business-focused AI application that forecasts future sales and demand using historical data, seasonality, and external business factors.  
This project demonstrates how time-series forecasting can support inventory planning, supply chain decisions, and sales strategy.

🔗 **Live Demo**  
👉 https://pranav25187-ai-sales-demand-forecasting-appapp-ixegud.streamlit.app/

---

## 🧠 Problem Statement

Retail companies face challenges such as:
- Demand fluctuations due to seasonality
- Sales spikes during holidays
- Overstocking or understocking due to poor forecasts

This project solves these problems by building a forecasting system that:
- Analyzes historical sales data
- Learns seasonal patterns
- Forecasts future demand with confidence intervals
- Presents results in an interactive dashboard

---

## 🚀 Features

- 📊 Store-wise and Department-wise sales forecasting  
- 📈 Time-series forecasting using Prophet  
- 🎯 Business-aware modeling with external factors (temperature, fuel price)  
- 📉 Confidence intervals for uncertainty estimation  
- 🧮 Key performance indicators (KPIs)  
- 📥 Downloadable forecast results (CSV)  
- 🖥️ Interactive Streamlit dashboard  

---

## 🛠️ Tech Stack

- **Programming Language:** Python  
- **Data Processing:** Pandas, NumPy  
- **Time Series Modeling:** Prophet  
- **Visualization:** Plotly  
- **Dashboard:** Streamlit  
- **Deployment:** Streamlit Cloud  

All tools and libraries used are **100% free and open-source**.

---

## 📂 Project Structure

```

ai-sales-demand-forecasting/
│
├── app/
│   └── app.py
│
├── data/
│   └── raw/
│       ├── train.csv
│       ├── features.csv
│       └── stores.csv
│
├── notebooks/
│   ├── 01_eda_feature_engineering.ipynb
│   └── 02_prophet_forecasting.ipynb
│
├── requirements.txt
└── README.md

````

---

## 📊 Dataset

**Walmart Sales Dataset (Kaggle)**  
- Weekly sales data across multiple stores and departments  
- Includes external features like temperature, fuel price, CPI, unemployment  
- Contains holiday indicators for demand spikes  

This dataset is widely used for real-world forecasting problems.

---

## 🔍 Exploratory Data Analysis (EDA)

Key insights discovered during analysis:
- Strong yearly seasonality in sales
- Significant sales increase during holiday weeks
- Larger stores generally generate higher sales
- Sales behavior varies significantly across departments

These insights guided the modeling approach.

---

## 🔮 Forecasting Approach

- Time-series forecasting using **Prophet**
- Yearly seasonality modeled explicitly
- External regressors added:
  - Temperature
  - Fuel price
- Forecast horizon configurable (4–52 weeks)
- Model outputs:
  - Predicted sales
  - Upper & lower confidence bounds

---

## 📊 Dashboard Overview

The Streamlit dashboard allows users to:
- Select store and department
- Choose forecast duration
- View historical vs forecasted sales
- Analyze trends and seasonality
- Download forecast results for further analysis

📸 Screenshots 
<img width="1919" height="837" alt="Screenshot 2026-01-05 212426" src="https://github.com/user-attachments/assets/c9685bbd-9526-4dcb-8cd1-5726c7d2ffc4" />

<img width="1411" height="945" alt="localhost_8501_ (4)" src="https://github.com/user-attachments/assets/5955b09d-3a1a-4914-af15-039f43f7fe84" />

<img width="1920" height="1032" alt="Screenshot 2026-01-05 212348" src="https://github.com/user-attachments/assets/0d430809-703c-465a-adcc-9863a808e974" />



## ▶️ Run Locally

```bash
git clone https://github.com/your-username/ai-sales-demand-forecasting.git
cd ai-sales-demand-forecasting
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
streamlit run app/app.py
````

---

## 🌐 Deployment

The application is deployed using **Streamlit Cloud** and accessible publicly at:

👉 [https://pranav25187-ai-sales-demand-forecasting-appapp-ixegud.streamlit.app/](https://pranav25187-ai-sales-demand-forecasting-appapp-ixegud.streamlit.app/)

---

## 💼 Interview Talking Points

* Built an end-to-end time-series forecasting system
* Used business-driven feature selection
* Handled seasonality and external regressors
* Designed an interactive dashboard for decision-makers
* Focused on interpretability, not black-box AI

---

## 📌 Future Improvements

* Multi-store batch forecasting
* Model comparison with LSTM or ARIMA
* Automatic holiday effect modeling
* Integration with inventory optimization logic

---

## 👤 Author

**Pranav**
Final Year Computer Engineering Student
Aspiring Data Scientist / ML Engineer

---
