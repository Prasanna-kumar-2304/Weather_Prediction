
# **Time Series Weather Forecasting App with Linear Regression**

## **Overview**

This project aims to build a **Weather Forecasting App** that predicts future temperatures using **Linear Regression**. The application leverages historical weather data to forecast future temperature values. The app is built using **Streamlit** for the user interface, providing an interactive experience for users to visualize the predicted temperature trends and make data-driven decisions.

## **Project Features**

### **Data Preprocessing:**

- The dataset contains historical weather data (temperature, humidity, wind speed, etc.).
- Missing values are handled and imputed appropriately to ensure the dataset is complete.
- The dataset is split into training and test sets for model evaluation.
- Time-based features are created, such as **date** and **season**, to capture seasonal trends.

### **Machine Learning Model:**

- **Linear Regression** is used as the baseline model for predicting future temperatures.
- Model evaluation includes metrics like **R² Score**, **Mean Squared Error (MSE)**, and **Root Mean Squared Error (RMSE)**.
- The model is trained on the historical data to forecast temperature values for future dates.

### **Streamlit App:**

- The app features a **user-friendly Streamlit interface** allowing users to interact with the model and predict future temperatures.
- **Interactive input fields**: Users can input different parameters such as date and location to get predictions.
- Visualizations include:
  - **Predicted Temperature Plot**: Displays the forecasted temperature for the upcoming days.
  - **Historical vs Predicted Plot**: Compares actual historical data with model predictions.
  - **Forecasting Trends**: Visualizes temperature trends over time.
  
### **Interactive Features:**

- Users can select the **date range** to get customized temperature predictions.
- Users can input a **specific location** to visualize temperature forecasts for that region (if location data is available).
  

## **Files**

- **weather_forecasting_model.ipynb**: The Jupyter notebook where data preprocessing, model training, and evaluation are done.
- **weather_data.csv**: The dataset used for the machine learning model.
- **app.py**: The Streamlit application that allows users to interact with the model and get predictions.
- **requirements.txt**: A list of dependencies for the project.

## **Results**

- **Linear Regression Model R² Score**: Example - 72.02% (this will be your model's evaluation metric).
  
- **Model Evaluation**:
  - **R² Score**: Measures the proportion of the variance in the dependent variable that is predictable from the independent variables.
  - **MSE (Mean Squared Error)**: Represents the average of the squares of the errors between actual and predicted values.
  - **RMSE (Root Mean Squared Error)**: The square root of the MSE, which gives an idea of how far off predictions are, on average.

- **Visualizations**:
  - **Predicted Temperature Plot**: Displays the predicted temperatures for future days.
  - **Historical vs Predicted**: Compares actual temperature data with predictions made by the model.
  - **Temperature Trend Visualization**: Shows how the temperature fluctuates over time, highlighting forecasted trends.
  
## **Acknowledgments**

- The dataset used in this project is from publicly available **weather data** sources.
- Special thanks to the open-source libraries such as **scikit-learn** and **Streamlit** that made this project possible.
- The visualizations were created using **matplotlib** and **seaborn**.

---
