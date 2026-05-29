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

  **Different Types of Forecast Accuracy Metrics**
   - Scale-Dependent Metrics
        These metrics are in the same unit as your data(e.g., dollars, units sold, temperature). They are great for comparing different models on the same dataset, but you cannot use them to compare different datasets.
      - **Mean Absolute Error (MAE)**
         - MAE takes the absolute value of each error and finds their average.
         - It tells you, on average, how far off your predictions are. If your MAE is 10, your forecast is typically wrong by 10 units.
         - It treats all errors equally. A single massive mistake doesn't warp the score disproportionately.
      - **Mean Squared Error (MSE)**
         - MSE squares each error before averaging them.
         - Because errors are squared, it heavily penalizes larger errors.
      - **Root Mean Squared Error (RMSE)**
         - RMSE is simply the square root of the MSE, bringing the metric back to the original units of the data
         - Like MSE, it penalizes large errors severely
   - Percentage Based Metrics
        These metrics scale the errors relative to the actual values, expressing the result as a percentage. This makes them unit-independent, allowing you to compare model performance across completely different products or businesses
      - **Mean Absolute Percentage Error (MAPE)**
         - MAPE measures the average absolute percentage drop between forecasted and actual values.
         - A MAPE of 5% means your forecast is, on average, off by 5% of the true value.
         - If any actual value ($Y_t$) is zero or very close to zero, the formula divides by zero, causing it to blow up or become undefined. It also penalizes over-forecasting more heavily than under-forecasting.
   - Scale Free Metrics
        Designed to solve the "division by zero" issue of MAPE while remaining unit-independent.
      - **Mean Absolute Scaled Error (MASE)**
         - MASE compares the absolute error of your model against the absolute error of a simple Naïve forecast (a baseline model where tomorrow's forecast is just today's actual value).
         - MASE > 1: Your model is performing worse than a simple baseline rule.
         - MASE < 1: Your model is performing better than the baseline.
       
  **Which Metric Should You Choose?**
  |Scenario|Recommended Metric|Why?|
  |--------|------------------|----|
  |Standard Evaluation|MAE|Easy to interpret and explain to stakeholders.|
  |Large Errors are Disastrous|RMSE|Strongly penalizes major forecasting failures.|
  |Comparing Different Products|MAPE|Provides a clean percentage comparison across scales (if no zero values exist).|
  |Data Contains Zeros/Intermittent Demand|MASE|Stable math that won't break when actual values hit zero.|
    
# Backtesting and Rolling Forecasts
   When evaluating time series models, testing them on a single static train-test split (like the last 20% of the data) is often insufficient and misleading. Because time series data is chronologically dependent, models can suffer from data leakage or quickly lose accuracy as the forecast horizon grows.

   To truly understand how a model will perform in production, data scientists use Backtesting and Rolling Forecasts.

   1. **What is Backtesting?**
      Backtesting is the overarching framework of simulating how a forecasting strategy would have performed historically. You "go back in time," train your model on data up to a specific historical point, forecast into the "future" (which is actually just your remaining historical data), and calculate your Forecast Error Metrics.

      In standard machine learning, you can randomly shuffle data for cross-validation. In time series backtesting, **you must strictly preserve chronological order** to avoid predicting the past using the future.
   2. **Rolling Forecast Origins (Time Series Cross-Validation)**
      The most robust way to backtest a time series model is through a Rolling Forecast strategy (also known as walk-forward validation or rolling-origin evaluation).

      Instead of training the model once, you iteratively move your "forecast origin" forward through time, making short-term predictions at each step.

      There are two primary ways to configure this:
        - Option A: Expanding Window (Accumulating History)
          In an expanding window, the start date of your training data remains fixed, and the training dataset grows larger at every iteration.
           - **Iteration 1**: Train on Month 1 $\rightarrow$ Forecast Month 2
           - **Iteration 2**: Train on Months 1–2 $\rightarrow$ Forecast Month 3
           - **Iteration 3**: Train on Months 1–3 $\rightarrow$ Forecast Month 4
          **Best for**: Long-term tracking where older historical data remains highly relevant to defining the overall baseline.

        - Option B: Sliding/Rolling Window (Fixed History Length)
          In a sliding window, the size of the training dataset remains constant. As the end of the window moves forward, the oldest data point is dropped.
            - **Iteration 1**: Train on Months 1–12 $\rightarrow$ Forecast Month 13
            - **Iteration 2**: Train on Months 2–13 $\rightarrow$ Forecast Month 14
            - **Iteration 3**: Train on Months 3–14 $\rightarrow$ Forecast Month 15
          **Best for**: Environments where patterns change rapidly (regime shifts), and old data becomes obsolete noise (e.g., high-frequency trading or fast-changing consumer trends).
