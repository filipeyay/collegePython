import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

date = {
    'year': [2024, 2025, 2026, 2027, 2028, 2029],
    'expenses': [100, 150, 50, 110, 300, 200]
}

df = pd.DataFrame(date)

class TimeSeries:
    def __init__(self, df):
        self.df = df

    def plot(self):
        plt.figure(figsize=(10, 6))
        plt.plot(self.df['year'], self.df['expenses'], marker='o')
        plt.xlabel('Year')
        plt.ylabel('Expenses')
        plt.title('Annual Expense Chart')
        plt.grid(True)
        plt.show()

    def linear_regression(self):
        X = self.df['year'].values.reshape(-1, 1)
        y = self.df['expenses'].values

        model = LinearRegression()
        model.fit(X, y)

        plt.figure(figsize=(10, 6))
        plt.plot(X, y, marker='o', label='Expenses Data')
        plt.plot(X, model.predict(X), color='red',
                 linestyle='--', label='Linear Regression')
        plt.xlabel('Year')
        plt.ylabel('Expenses')
        plt.title('Linear Regression Of Annual Expenses Graph')
        plt.legend()
        plt.grid(True)
        plt.show()

time_series = TimeSeries(df)

time_series.plot()

time_series.linear_regression()
