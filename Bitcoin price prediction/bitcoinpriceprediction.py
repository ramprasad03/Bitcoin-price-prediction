# -*- coding: utf-8 -*-
"""bitcoinpriceprediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1q3tCcFb8dF2SasATfHXM4lY0d7uveQER
"""

pip install pandas

pip install fbprophet

import pandas as pd
from fbprophet import Prophet

from google.colab import files
uploaded=files.upload()

df=pd.read_csv('BTC-USD.csv')
df=df[["Date","Close"]]
df.columns=["ds","y"]
print(df)

prophet=Prophet()
prophet.fit(df)

future=prophet.make_future_dataframe(periods=365)
print(future)

forecast = prophet.predict(future)
forecast[["ds","yhat","yhat_lower","yhat_upper"]].tail(200)

from fbprophet.plot import plot
prophet.plot(forecast,figsize=(20,10))