import streamlit as st
import joblib
import numpy as np
import matplotlib.pyplot as plt

@st.cache_resource
def load_trained_model():
    return joblib.load('trained_model.pkl')

st.title("Interactive Weather Forecasting Prediction with Time Series Insights")
st.write("This app uses a pre-trained regression model to forecast temperature based on weather data.")

model = load_trained_model()
st.success("Pre-trained model loaded successfully!")

st.subheader("Real-Time Prediction")
st.write("Enter feature values to predict temperature:")
lag_1 = st.number_input("Lag 1 (Previous Day Temperature)", value=15.0)
lag_2 = st.number_input("Lag 2 (Two Days Ago Temperature)", value=14.0)
humidity = st.number_input("Humidity (%)", value=65.0)
wind_speed = st.number_input("Wind Speed (km/h)", value=10.0)
rainfall = st.number_input("Rainfall (mm)", value=0.0)

if st.button("Predict Temperature"):
    new_features = np.array([[lag_1, lag_2, humidity, wind_speed, rainfall]])
    prediction = model.predict(new_features)
    st.markdown(
        f"<h2 style='color:white;'>Predicted Temperature: {prediction[0]:.2f} °C</h2>",
        unsafe_allow_html=True,
    )

    st.subheader("Forecasted Temperatures for the Next 7 Days")
    future_lags = [lag_1, lag_2]
    future_temps = []

    for _ in range(7):
        new_input = np.array([[future_lags[-1], future_lags[-2], humidity, wind_speed, rainfall]])
        next_temp = model.predict(new_input)[0]
        future_temps.append(next_temp)
        future_lags.append(next_temp)

    days = ["Day 1", "Day 2", "Day 3", "Day 4", "Day 5", "Day 6", "Day 7"]
    prediction_table = {"Day": days, "Predicted Temperature (°C)": [round(temp, 2) for temp in future_temps]}
    st.table(prediction_table)

    plt.figure(figsize=(8, 5))
    plt.plot(days, future_temps, marker="o", color="orange", label="Predicted Temperatures")
    plt.axhline(y=lag_1, color="blue", linestyle="--", label="Today's Temperature (Lag 1)")
    plt.title("Forecasted Temperatures for the Next 7 Days", fontsize=14)
    plt.xlabel("Days")
    plt.ylabel("Temperature (°C)")
    plt.grid(True)
    plt.legend()
    st.pyplot(plt)

    st.subheader("Input Feature Visualization")
    features = ["Lag 1", "Lag 2", "Humidity", "Wind Speed", "Rainfall"]
    values = [lag_1, lag_2, humidity, wind_speed, rainfall]
    plt.figure(figsize=(8, 5))
    plt.bar(features, values, color="skyblue")
    plt.title("Input Feature Values")
    plt.xlabel("Features")
    plt.ylabel("Values")
    plt.grid(axis="y")
    st.pyplot(plt)
