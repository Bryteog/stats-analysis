import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

data = pd.read_csv("C:/Users/dell/Downloads/Datasets/Screentime-App-Details.csv")
data.head()

data.isnull().sum()

data.describe()

# App Usage
figure = px.bar(data_frame = data, x = "Date", y = "Usage", color = "App", title = "App Usage")
figure.show()

# App Notifications
figure = px.bar(data_frame = data, x = "Date", y = "Notifications", title = "Notifications", color = "App")
figure.show()

# Times Opened
figure = px.bar(data_frame = data, x = "Date", y = "Times opened", color = "App", title = "Times Opened")
figure.show()

# Usage against Notifications
figure = px.scatter(data_frame = data, x = "Notifications", y = "Usage", size = "Notifications", trendline = "ols", title = "Correlation between Notifications and Usage")
figure.show()
