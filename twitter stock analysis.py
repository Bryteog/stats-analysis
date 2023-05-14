import pandas as pd
import numpy as np
import datetime as dt
from datetime import date, timedelta
import plotly.graph_objects as go
import plotly.express as px
import plotly.io as pio
pio.templates.default = "plotly_white"

data = pd.read_csv("C:/Users/dell/Downloads/Datasets/Twttr/TWTR.csv")
print(data.head())
print(data.info())
print(data.describe())
print(data.isnull().sum())

data = data.dropna()

figure = go.Figure(data = [go.Candlestick(x = data["Date"],
                                          open = data["Open"],
                                          high = data["High"],
                                          low = data["Low"],
                                          close = data["Close"])
                           ])
figure.update_layout(title = "$TWTR Over the Years", xaxis_rangeslider_visible = False)
figure.show()

figure = px.bar(data,
                x = "Date",
                y = "Close",
                color = "Close")
figure.update_xaxes(rangeslider_visible = True)
figure.show()

figure = px.bar(data, x = "Date", y = "Close", color = "Close")
figure.update_xaxes(rangeslider_visible = True)
figure.update_layout(title = "$TWTR Over the Years", xaxis_rangeslider_visible = False)
figure.update_xaxes(
    rangeselector = dict(
        buttons = list([
            dict(count = 1, label = "1m", step = "month", stepmode = "backward"),
            dict(count = 3, label = "3m", step = "month", stepmode = "backward"),
            dict(count = 6, label = "6m", step = "month", stepmode = "backward"),
            dict(count = 1, label = "1Y", step = "year", stepmode = "backward"),
            dict(count = 2, label = "2Y", step = "year", stepmode = "backward"),
            dict(step = "all", label = "All Time")
        ])
    )
)

data["Date"] = pd.to_datetime(data["Date"], format = "%Y-%M-%D")
data["Month"] = data["Date"].dt.month
data["Year"] = data["Date"].dt.year
fig = px.line(data, 
              x = "Month",
              y = "Close",
              color = "Year",
              title = "Timeline of $TWTR"
              )
fig.show()