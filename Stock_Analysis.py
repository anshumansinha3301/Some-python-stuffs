import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf


data = yf.download('AAPL', start='2022-01-01', end='2023-01-01')
data['Close'].plot(title='AAPL Stock Price')
plt.show()
