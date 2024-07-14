import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"
data = pd.read_csv(url)
data = data[data['Country/Region'] == 'India'].drop(columns=['Province/State', 'Country/Region', 'Lat', 'Long']).sum()
data.plot(title='COVID-19 Cases in India')
plt.show()
