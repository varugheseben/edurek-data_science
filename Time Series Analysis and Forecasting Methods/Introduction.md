# Time Series Analysis
  **Time Series Analysis (TSA)** is a specialized branch of statistics and data science dedicated to analyzing a sequence of data points collected consistently over a specific interval of time.

  Unlike standard tabular datasets where each row is assumed to be an independent observation (like a list of housing prices across different cities), time series data points are intrinsically dependent on their past values. The ordering of the data matters entirely.

## Core components of Time Series Data
  When you look at a time series plot—whether it's daily stock prices, hourly website traffic, or monthly climate data—the overall signal is typically a composite of four distinct underlying structural patterns:
   - Trend : Variation in data over a long period of time (no fixed interval). We have 3 types of trend
     - Positive Trend
     - Negative Trend
     - No Trend
   - Seasonality : Variation in data occurs at regular intervals over time
   - Cyclic Patterns : Data Patterns with uncertain timing and fluctuations
   - Irregular/Residual Noise : Data with short periodic, non-repeated and unpredictable events

## Time Series Analysis and Time Series Forecasting
  - **Time Series Analysis(Understanding the past)** : Analysis is retrospective. It focuses on breaking down the historical data to understand the underlying "why."
  - **Time Series Forecasting(Predicting the Future)** : Forecasting is prospective. It uses the mathematical rules and historical patterns uncovered during the analysis phase to project future data points over a short, medium, or long-term horizon.

## Stationarity
   A time series is considered stationary if its statistical properties do not change over time.
   - **Stationary Process (Constant mean and Variance)**
   - **Non Stationary Process(Changing mean and variance)**

## Lag Features
   Lag features are previous time steps of a series used as input features to predict future values.

## Rolling Statistics
   Rolling statistics compute moving averages or other metrics over a fixed-size sliding time window.

## ACF (Autocorrelation Function) and PACF(Partial Autocorrelation Function)
  In time series analysis, ACF anf PACF are essential diagnostic tools used to measure how data points in a time series relate to their own historical past values (lags).

## Time Series Models used for forecasting
  - **Auto Regression(AR) Model** : A time series model which uses past observation from the linear regression model to predict the values.
  - **Moving Average(MA) Model** : A time series model that takes the average of the data depending upon the M value and gives the predicted result.
  - **ARMA (AR + MA) Model** : This model uses the combination of AR and MA to predict the values.
  - **ARIMA (AR + I + MA) Model** : This model can be used with stationary and non stationary data to predict the values. ARIMA stands for AutoRegressive Integrated Moving Average.
     - I represents the use of differencing of raw observations to make the time series stationary
  - **SARIMA(Seasonal Autoregressive Integrated Moving Average)** : This model extends ARIMA by incorporating seasonality components to handle periodic fluctuations in the data and provide better forecasting results.

      SARIMA = ARIMA + Seasonal Components(AutoRegressive, Differencing, Moving Average)

    
