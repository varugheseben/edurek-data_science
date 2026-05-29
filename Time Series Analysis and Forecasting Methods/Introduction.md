# Time Series Data
  **A time series** is a set of observations on the values that a variable takes at different times. Such data may be collected at regular time intervals such as monthly, weekly, quarterly, yearly. Time series are used in statistics, econometrics, mathematical finance, weather forecasting, earthquake prediction and so on.

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
  In time series analysis, ACF anf PACF are essential diagnostic tools used to measure how data points in a time series relate to their own historical past values (lags). Basically ACF and PACF helps us to determine how many lags(past values) we need to use for forecasting.
  - In timer series analysis, **AUtocorrelation Function(ACF)** measures the linear relationship between a variable’s current value and its past values over various time intervals (lags). The prefix auto means self. Instead of measuring the relationship between two different variables (like height and weight), autocorrelation measures how a single variable correlates with itself shifted back in time.
    ACF: Measures the total correlation between $Y_t$ and $Y_{t-k}$, including all the indirect effects of the intermediate lags ($Y_{t-1}, Y_{t-2}$, etc.).

  - **Partial Autocorrelation Function** strips away the intermediary lags and finds the direct relations between two time series value.
    PACF (Partial ACF): Measures the direct correlation between $Y_t$ and $Y_{t-k}$ after stripping away the predictive linear effects of all shorter-interval lags.

## Time Series Models used for forecasting
  - **Auto Regression(AR) Model** : A time series model which uses past observation from the linear regression model to predict the values.
  - **Moving Average(MA) Model** : A time series model that takes the average of the data depending upon the M value and gives the predicted result.
  - **ARMA (AR + MA) Model** : This model uses the combination of AR and MA to predict the values.
  - **ARIMA (AR + I + MA) Model** : This model can be used with stationary and non stationary data to predict the values. ARIMA stands for AutoRegressive Integrated Moving Average. We should use this model in the case of data set which has seasonal dependency.
     - I represents the use of differencing of raw observations to make the time series stationary
  - **SARIMA(Seasonal Autoregressive Integrated Moving Average)** : This model extends ARIMA by incorporating seasonality components to handle periodic fluctuations in the data and provide better forecasting results.

      SARIMA = ARIMA + Seasonal Components(AutoRegressive, Differencing, Moving Average)
  - **Auto ARIMA**: An automated time series forecasting model that finds the optimal set of parameters(p, d, q) and seasonal parameters(P, D, Q, s) by minimizing an information criteria like AIC

## Importance of Time Series Analysis
  - Planning for future operations
  - Understanding past behavior of historical patterns
  - Business Forecasting
  - Evaluating current accomplishments

# Exponential Smoothing
  **Exponential Smoothing** is a popular time series forecasting method for univariate (single-variable) data.

  Unlike a simple moving average—which gives equal weight to all past observations—exponential smoothing assigns exponentially decreasing weights as the observations get older. In short: recent data has a huge impact on the forecast, while older data has a progressively smaller impact.

  - Captures short-term patterns better than simple averages
  - Works well for stationary or slowly changing series
  - Holt's and Holt-Winters methods based on this basis

  Example: Imagine you run a business and want to forecast tomorrow's sales
   - Yesterday's sales numbers are incredibly relevant because they capture current demand, current weather, and recent marketing.
   - Sales numbers from six months ago are much less relevant.

   Instead of completely ignoring old data, exponential smoothing retains it but dampens its influence. The rate at which the influence decreases is controlled by a smoothing parameter, typically denoted as $\alpha$ (alpha).

   ## Types of Exponential Smoothing
   - **Double Exponential Smoothing(Holt's Linear Trend Method)**
     - Extends exponential smoothing by adding a 'trend' component
     - Usefull when data has a steady upward and downward trend
     - **Forcast = Level + Trend * Time**
     - Two smoothing parameters
       - Level($\alpha$)
       - Trend($\beta$)
   - **Triple Exponential Smoothing(Holt-Winters Method)**
     - It has 2 versions
        - Additive (Constant seasonality)
        - Multiplicative (Growing seasonality)
     - Builds on Holt's method by adding seasonal adjustment
     - Handles trend + seasonality simulataneously
     - Three smothing parameters
        - Level($\alpha$)
        - Trend($\beta$)
        - Seasonality(($\gamma$)

# Forecasting tool
  1. **Facebook Prophet**
      - Open source forecasting tool by Facebook(Meta)
      - Easy to use, work well with messy real world data
      - Handles trend, seasonality, holidays/events automatically
      - Designed for business time series data

      **Different Flows of Prophet**
        - Step 1: Input data(Date + Value)
        - Step 2: Decompose into Trend + Seasonality + Holiday effects
        - Step 3: Fit model and generate forecast
        - Step 4: Visualize results with confidence intervals
    
      **Advantage of Forecast with Prophet**
        - Forecast includes future trend + seasonal patterns
        - Confidence intervals highlight uncertainity
        - Works well for sales, demand, web traffic, events
      
# Forecast Error Metrics
  **Forecast Error Metrics** are helpfull in determining how well a time series forecasting model is working. 
  
  An error is simply the difference between the actual observed value ($Y_t$) and the forecasted value ($\hat{Y}_t$) for a given time step:
  
   $$e_t = Y_t - \hat{Y}_t$$

  Because some errors are positive (under-forecasting) and others are negative (over-forecasting), you cannot just add them up—they would cancel each other out. Error  metrics process these numbers in different ways to give you an accurate picture of model performance.
