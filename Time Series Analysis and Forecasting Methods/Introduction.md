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

Stationary (Constant Mean & Variance)      Non-Stationary (Trending Mean)
   ▲                                          ▲
   │   /\    /\  /\                           │       /\    /\
   │  /  \  /  \/  \                          │      /  \  /  \  /\
   │ /    \/        \                         │   /\/    \/    \/  \
   └──────────────────► Time                  └─────────────────────► Time
