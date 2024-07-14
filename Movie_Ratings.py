import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

url = "https://datasets.imdbws.com/title.ratings.tsv.gz"
data = pd.read_csv(url, delimiter='\t')
data['averageRating'] = pd.to_numeric(data['averageRating'])
data['numVotes'] = pd.to_numeric(data['numVotes'])
plt.scatter(data['numVotes'], data['averageRating'], alpha=0.5)
plt.title('IMDb Movie Ratings vs. Number of Votes')
plt.xlabel('Number of Votes')
plt.ylabel('Average Rating')
plt.show()
