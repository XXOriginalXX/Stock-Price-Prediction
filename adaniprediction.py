import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import numpy as np

dataset = pd.read_csv('ADANIPORTS.csv')

features = ['Open', 'High', 'Low', 'Volume', 'Turnover']
target = 'Close'

X = dataset[features]
y = dataset[target]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

model = LinearRegression()
model.fit(X_train, y_train)

open_price = float(input("Enter Open: "))
high_price = float(input("Enter High: "))
low_price = float(input("Enter Low: "))
volume = int(input("Enter Volume: "))
turnover = float(input("Enter Turnover: "))


input_data = {
    'Open': [open_price],
    'High': [high_price],
    'Low': [low_price],
    'Volume': [volume],
    'Turnover': [turnover]
}
input_df = pd.DataFrame(input_data)


predicted_close = model.predict(input_df)
print(f"Predicted Close Price: {predicted_close[0]}")