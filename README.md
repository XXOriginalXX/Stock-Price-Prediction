# Stock Price Prediction Model
## Overview

This project is a linear regression model designed to predict the closing price of a stock based on various financial metrics. The model utilizes historical stock data, including the opening price, highest and lowest prices of the day, trading volume, and turnover, to forecast the closing price.

## Features
- Open: The stock's opening price for the day.
- High: The highest price reached during the day.
- Low: The lowest price reached during the day.
- Volume: The total number of shares traded during the day.
- Turnover: The total value of shares traded during the day.

## How It Works
The model is trained on historical stock data, learning the relationship between the features and the closing price. Once trained, it can predict the closing price based on new input data provided by the user.

## Usage
To use the model, run the script and input the following values when prompted:

- Open: Enter the stock's opening price.
- High: Enter the stock's highest price of the day.
- Low: Enter the stock's lowest price of the day.
- Volume: Enter the total number of shares traded.
- Turnover: Enter the total value of shares traded.
The model will then output the predicted closing price based on these inputs.

## Applications
Stock Market Analysis: Helps in forecasting stock prices based on daily financial metrics.
Investment Decision Making: Assists investors in making informed decisions by predicting potential closing prices.
Financial Research: Useful for academic and professional research in finance and economics.
## Requirements
- Python 3.x
- pandas
- scikit-learn
- numpy
