import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# -------------------------------
# App Configuration
# -------------------------------
st.set_page_config(page_title="Stock Price Prediction", layout="wide")

st.title("📈 Stock Price Prediction App")
st.write("Predict *Next Day Close Price* using Machine Learning (Linear Regression)")

# -------------------------------
# Load Dataset
# -------------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("stocks.csv")
    df["Date"] = pd.to_datetime(df["Date"])
    return df

df = load_data()

# -------------------------------
# Select Stock Ticker
# -------------------------------
ticker = st.selectbox("Select Stock Ticker", df["Ticker"].unique())

data = df[df["Ticker"] == ticker].sort_values("Date")

st.subheader(f"📊 Data Preview for {ticker}")
st.dataframe(data.tail())

# -------------------------------
# Feature & Target
# -------------------------------
X = data[["Open", "High", "Low", "Volume"]]
y = data["Close"]

# -------------------------------
# Train-Test Split (No Shuffle)
# -------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, shuffle=False
)

# -------------------------------
# Train Model
# -------------------------------
model = LinearRegression()
model.fit(X_train, y_train)

# -------------------------------
# Predictions
# -------------------------------
y_pred = model.predict(X_test)

# -------------------------------
# Model Evaluation
# -------------------------------
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
st.metric("📉 RMSE Error", round(rmse, 2))

# -------------------------------
# Plot Actual vs Predicted
# -------------------------------
st.subheader("📈 Actual vs Predicted Close Price")

fig, ax = plt.subplots(figsize=(10, 4))
ax.plot(y_test.values, label="Actual Price")
ax.plot(y_pred, label="Predicted Price")
ax.set_xlabel("Days")
ax.set_ylabel("Close Price")
ax.legend()

st.pyplot(fig)

# -------------------------------
# Predict Next Day Price
# -------------------------------
st.subheader("🔮 Predict Next Day Close Price")

last_day = X.tail(1)
next_day_price = model.predict(last_day)[0]

st.success(f"Predicted Next Close Price for {ticker}: ₹ {round(next_day_price, 2)}")

# -------------------------------
# Footer
# -------------------------------
st.markdown("---")
st.caption("Built with ❤️ using Streamlit & Machine Learning")