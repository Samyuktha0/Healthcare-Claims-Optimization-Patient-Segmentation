import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
import matplotlib.pyplot as plt

# Load monthly claims
df = pd.read_excel("data/claims_data.xlsx")
df['Month'] = pd.to_datetime(df['ClaimDate']).dt.to_period('M')
monthly = df.groupby('Month')['ClaimAmount'].sum()

# ARIMA model
model = ARIMA(monthly, order=(1,1,1))
results = model.fit()

# Forecast
forecast = results.forecast(steps=6)
forecast.plot()
plt.title("Claim Amount Forecast")
plt.ylabel("USD")
plt.show()
