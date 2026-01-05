import streamlit as st
import pandas as pd
import numpy as np
from prophet import Prophet
import plotly.graph_objects as go
from pathlib import Path

st.set_page_config(page_title="AI Sales & Demand Forecasting", layout="wide")

st.title("📈 AI Sales & Demand Forecasting Dashboard")
st.markdown(
    "Forecast future sales using historical trends, seasonality, and key business factors."
)

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data" / "raw"

@st.cache_data
def load_data():
    train = pd.read_csv(DATA_DIR / "train.csv")
    features = pd.read_csv(DATA_DIR / "features.csv")
    stores = pd.read_csv(DATA_DIR / "stores.csv")

    df = train.merge(features, on=["Store", "Date", "IsHoliday"], how="left")
    df = df.merge(stores, on="Store", how="left")

    df["Date"] = pd.to_datetime(df["Date"])

    for col in ["Temperature", "Fuel_Price", "CPI", "Unemployment"]:
        df[col] = df[col].fillna(df[col].median())

    return df

df = load_data()

st.sidebar.header("Forecast Configuration")

store_id = st.sidebar.selectbox("Select Store", sorted(df["Store"].unique()))
dept_id = st.sidebar.selectbox("Select Department", sorted(df["Dept"].unique()))
forecast_weeks = st.sidebar.slider("Forecast Horizon (Weeks)", 4, 52, 12)

filtered_df = df[
    (df["Store"] == store_id) &
    (df["Dept"] == dept_id)
][["Date", "Weekly_Sales", "Temperature", "Fuel_Price"]]

filtered_df.columns = ["ds", "y", "temperature", "fuel_price"]

if len(filtered_df) < 50:
    st.warning("Not enough historical data for reliable forecasting.")
    st.stop()

@st.cache_resource
def train_prophet(data):
    model = Prophet(yearly_seasonality=True, seasonality_mode="multiplicative")
    model.add_regressor("temperature")
    model.add_regressor("fuel_price")
    model.fit(data)
    return model

model = train_prophet(filtered_df)

future = model.make_future_dataframe(periods=forecast_weeks, freq="W")
future["temperature"] = filtered_df["temperature"].mean()
future["fuel_price"] = filtered_df["fuel_price"].mean()

forecast = model.predict(future)

latest_sales = filtered_df["y"].iloc[-1]
next_week_sales = forecast.iloc[len(filtered_df)]["yhat"]
avg_sales = filtered_df["y"].mean()
growth = ((next_week_sales - avg_sales) / avg_sales) * 100

c1, c2, c3, c4 = st.columns(4)
c1.metric("Latest Weekly Sales", f"${latest_sales:,.0f}")
c2.metric("Next Week Forecast", f"${next_week_sales:,.0f}")
c3.metric("Average Weekly Sales", f"${avg_sales:,.0f}")
c4.metric("Expected Change", f"{growth:.2f}%")

fig = go.Figure()

fig.add_trace(go.Scatter(x=filtered_df["ds"], y=filtered_df["y"], mode="lines", name="Actual Sales"))
fig.add_trace(go.Scatter(x=forecast["ds"], y=forecast["yhat"], mode="lines", name="Forecast"))
fig.add_trace(go.Scatter(x=forecast["ds"], y=forecast["yhat_upper"], line=dict(width=0), showlegend=False))
fig.add_trace(
    go.Scatter(
        x=forecast["ds"],
        y=forecast["yhat_lower"],
        fill="tonexty",
        fillcolor="rgba(0,123,255,0.25)",
        line=dict(width=0),
        showlegend=False
    )
)

fig.update_layout(
    title=f"Sales Forecast | Store {store_id}, Department {dept_id}",
    xaxis_title="Date",
    yaxis_title="Weekly Sales",
    hovermode="x unified"
)

st.plotly_chart(fig, use_container_width=True)

components_fig = model.plot_components(forecast)
st.pyplot(components_fig)

output_df = forecast[["ds", "yhat", "yhat_lower", "yhat_upper"]]
csv = output_df.to_csv(index=False)

st.download_button(
    "📥 Download Forecast CSV",
    csv,
    file_name=f"store_{store_id}_dept_{dept_id}_forecast.csv",
    mime="text/csv"
)
