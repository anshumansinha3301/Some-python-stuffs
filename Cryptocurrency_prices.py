import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests

url = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency=usd&days=30"
data = requests.get(url).json()
prices = pd.DataFrame(data['prices'], columns=['timestamp', 'price'])
prices['timestamp'] = pd.to_datetime(prices['timestamp'], unit='ms')
prices.set_index('timestamp', inplace=True)
prices['price'].plot(title='Bitcoin Prices')
plt.show()
