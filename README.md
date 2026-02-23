## 📌 Project Overview

This project is a Machine Learning–based web application that predicts the **Next Day Closing Price** of selected stocks using **Linear Regression**.

The application is developed using Streamlit and allows users to select a stock ticker to view historical data, model performance, and predicted next-day closing price.

---

## 🎯 Problem Statement

Stock price prediction is a challenging time-series problem due to market volatility and multiple influencing factors.

The goal of this project is to build a regression model that predicts the next day's closing price based on historical stock data features such as:

* Open Price
* High Price
* Low Price
* Volume

---

## 📊 Dataset Description

The dataset (`stocks.csv`) contains:

* Date
* Ticker
* Open
* High
* Low
* Close
* Volume

Data is filtered dynamically based on the selected stock ticker.

---

## ⚙️ Machine Learning Workflow

### 1️⃣ Data Loading

* Dataset loaded using Pandas
* Date column converted to datetime format

### 2️⃣ Stock Selection

* User selects stock ticker from dropdown

### 3️⃣ Feature Selection

Input Features:

* Open
* High
* Low
* Volume

Target Variable:

* Close Price

### 4️⃣ Train-Test Split

* 80% Training Data
* 20% Testing Data
* Shuffle disabled (important for time-series data)

### 5️⃣ Model Training

* Linear Regression model trained using Scikit-learn

### 6️⃣ Model Evaluation

Model performance evaluated using:

* Root Mean Squared Error (RMSE)

### 7️⃣ Visualization

* Actual vs Predicted Close Price plotted using Matplotlib

### 8️⃣ Next Day Prediction

* Uses last available record
* Predicts next day closing price

---

## 🚀 Application Features

✅ Stock ticker selection
✅ Historical data preview
✅ RMSE error display
✅ Actual vs Predicted price visualization
✅ Next-day close price prediction
✅ Clean Streamlit interface

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Scikit-learn
* Streamlit

---

## 📂 Project Structure

```bash
├── app.py
├── stocks.csv
├── requirements.txt
└── README.md
```

---

## ▶️ How to Run the Project

### 1️⃣ Clone Repository

```bash
gh repo clone sachinsharma19112003/stock-market-app
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run Streamlit App

```bash
streamlit run app.py
```

---

## 📈 Model Performance

* The model evaluates prediction accuracy using RMSE.
* Lower RMSE indicates better performance.
* Actual vs Predicted graph visually compares model accuracy.

---

## ⚠️ Disclaimer

This project is for educational purposes only.
Stock market investments involve risk. Predictions are based on historical data and do not guarantee future results.

---

## 👨‍💻 Author

Sachin Sharma
Machine Learning Engineer | Data Scientist 🚀

